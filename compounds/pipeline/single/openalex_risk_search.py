#!/usr/bin/env python3
"""Supplemental OpenAlex literature search for compound medication-risk context.

Runs after group_by_stance (step 5b) and before review.py. Writes
``openalex_risk_context.json`` in the compound data directory. Does not replace
tag.py / group_by_stance risk scoring.

Usage:
  python openalex_risk_search.py --compound Omipalisib --compound-dir compounds/data/Omipalisib
  python openalex_risk_search.py --compound Omipalisib --compound-dir ... --skip-windows
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests
from openai import OpenAI

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = REPO_ROOT / "prompts"
PROMPT_TERMS = PROMPTS_DIR / "compound-risk-openalex-terms.md"
PROMPT_PICKER = PROMPTS_DIR / "compound-risk-openalex-title-picker.md"
PROMPT_WINDOW = PROMPTS_DIR / "compound-risk-openalex-window.md"

if load_dotenv is not None:
    load_dotenv(REPO_ROOT / ".env")

VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
VLLM_API_KEY = os.environ.get("VLLM_API_KEY", "none")
OPENALEX_EMAIL = os.environ.get("OPENALEX_EMAIL", "team@descai.org")

OPENALEX_SEARCH_URL = "https://api.openalex.org/works"
OPENALEX_SLEEP = 1.0 / 8.0
MAX_RETRIES = 4
DEFAULT_MAX_WORKS = 20
PER_PAGE_PER_TERM = 6
MAX_TERMS = 4
WINDOW_CHARS = 800
WINDOW_OVERLAP = 200
MAX_WINDOWS_PER_WORK = 3
TERM_MAX_TOKENS = 512
PICKER_MAX_TOKENS = 512
WINDOW_MAX_TOKENS = 512

OUTPUT_FILENAME = "openalex_risk_context.json"
CACHE_FILENAME = "openalex_risk_cache.json"
GROUPED_FILENAME = "grouped_by_stance.json"

_FENCE_BLOCK = re.compile(r"```(?:json)?\s*([\s\S]*?)\s*```", re.I)


def _parse_json_array(raw: str) -> list[Any] | None:
    raw = raw.strip()
    if not raw:
        return None
    m = _FENCE_BLOCK.search(raw)
    candidate = m.group(1).strip() if m else raw
    start = candidate.find("[")
    if start == -1:
        return None
    candidate = candidate[start:]
    end = candidate.rfind("]")
    if end != -1:
        try:
            parsed = json.loads(candidate[: end + 1])
            if isinstance(parsed, list):
                return parsed
        except json.JSONDecodeError:
            pass
    closed = candidate.rstrip().rstrip(",").rstrip() + "]"
    try:
        parsed = json.loads(closed)
        if isinstance(parsed, list):
            return parsed
    except json.JSONDecodeError:
        pass
    return None


def _reconstruct_abstract(inverted: dict[str, list[int]] | None) -> str | None:
    if not inverted or not isinstance(inverted, dict):
        return None
    slots: list[tuple[int, str]] = []
    for word, positions in inverted.items():
        if not isinstance(positions, list):
            continue
        for pos in positions:
            if isinstance(pos, int):
                slots.append((pos, str(word)))
    if not slots:
        return None
    slots.sort(key=lambda x: x[0])
    return " ".join(w for _, w in slots)


def call_llm(client: OpenAI, model: str, system_prompt: str, user_content: str, max_tokens: int) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content},
    ]
    extra_body = {"top_k": -1, "chat_template_kwargs": {"enable_thinking": False}}
    for attempt in range(MAX_RETRIES):
        try:
            try:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=max_tokens,
                    temperature=0,
                    messages=messages,
                    extra_body=extra_body,
                )
            except TypeError:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=max_tokens,
                    temperature=0,
                    messages=messages,
                )
            return (response.choices[0].message.content or "").strip()
        except Exception as exc:
            print(f"  [openalex-risk] LLM attempt {attempt + 1}/{MAX_RETRIES}: {exc}", file=sys.stderr)
            if attempt == MAX_RETRIES - 1:
                return ""
            time.sleep(2 ** attempt)
    return ""


def get_available_model(client: OpenAI) -> str:
    try:
        models = client.models.list()
        if models.data:
            return models.data[0].id
    except Exception:
        pass
    for env_name in ("REVIEWER_MODEL", "TAGGER_MODEL", "CLASSIFIER_MODEL", "VALIDATOR_MODEL"):
        val = os.environ.get(env_name)
        if val:
            return val
    return os.environ.get("VALIDATOR_MODEL", "/model")


def _search_openalex(query: str, session: requests.Session, n: int) -> list[dict[str, Any]]:
    params = {
        "search": query,
        "per-page": str(n),
        "mailto": OPENALEX_EMAIL,
        "select": "id,doi,title,type,publication_year,cited_by_count,abstract_inverted_index",
    }
    headers = {
        "User-Agent": f"Claim-extractor/1.0 (mailto:{OPENALEX_EMAIL})",
        "Accept": "application/json",
    }
    time.sleep(OPENALEX_SLEEP)
    try:
        r = session.get(OPENALEX_SEARCH_URL, params=params, headers=headers, timeout=20)
    except requests.RequestException as exc:
        print(f"  [openalex-risk] request error {query!r}: {exc}", file=sys.stderr)
        return []
    if r.status_code != 200:
        print(f"  [openalex-risk] HTTP {r.status_code} for {query!r}", file=sys.stderr)
        return []
    works: list[dict[str, Any]] = []
    for item in r.json().get("results") or []:
        if not isinstance(item, dict):
            continue
        inv = item.get("abstract_inverted_index")
        abstract = _reconstruct_abstract(inv) if isinstance(inv, dict) else None
        works.append({
            "openalex_id": item.get("id") or "",
            "doi": item.get("doi") or "",
            "title": item.get("title") or item.get("display_name") or "",
            "year": item.get("publication_year"),
            "cited_by_count": item.get("cited_by_count"),
            "abstract": abstract,
        })
    return works


def _load_context_snippet(compound_dir: Path) -> str:
    agents = sorted(
        compound_dir.glob("prepared_report_*_agent.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not agents:
        return ""
    try:
        data = json.loads(agents[0].read_text(encoding="utf-8"))
        ac = data.get("agent_context") or {}
        mech = ac.get("mechanism_hypotheses_excerpt") or {}
        if isinstance(mech, dict):
            txt = str(mech.get("summary") or mech.get("text") or "")[:400]
            if txt:
                return txt
    except (OSError, json.JSONDecodeError):
        pass
    return ""


def _curated_risk_count(compound_dir: Path) -> int:
    grouped_path = compound_dir / GROUPED_FILENAME
    if not grouped_path.is_file():
        return 0
    try:
        grouped = json.loads(grouped_path.read_text(encoding="utf-8"))
        by = grouped.get("by_stance") or {}
        n = len(by.get("raises_caution", {}).get("members", []) or [])
        n += len(by.get("risk_information", {}).get("members", []) or [])
        return n
    except (OSError, json.JSONDecodeError):
        return 0


def _chunk_text(text: str, size: int, overlap: int, max_chunks: int) -> list[str]:
    text = text.strip()
    if not text:
        return []
    if len(text) <= size:
        return [text]
    chunks: list[str] = []
    start = 0
    while start < len(text) and len(chunks) < max_chunks:
        end = min(start + size, len(text))
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return chunks


def _should_skip_fetch(output_path: Path, grouped_path: Path) -> bool:
    if os.environ.get("OPENALEX_RISK_REUSE", "").strip() not in ("1", "true", "yes"):
        return False
    if not output_path.is_file():
        return False
    if grouped_path.is_file() and output_path.stat().st_mtime >= grouped_path.stat().st_mtime:
        print(f"  [openalex-risk] Reusing {output_path.name} (newer than grouped file)", file=sys.stderr)
        return True
    return False


def run_search(
    *,
    compound_name: str,
    compound_dir: Path,
    output_path: Path,
    cache_path: Path,
    client: OpenAI,
    model: str,
    max_works: int,
    skip_windows: bool,
) -> dict[str, Any]:
    grouped_path = compound_dir / GROUPED_FILENAME
    curated_count = _curated_risk_count(compound_dir)
    print(
        f"  [openalex-risk] compound={compound_name!r} curated_risk_excerpts={curated_count}",
        file=sys.stderr,
    )

    context_snippet = _load_context_snippet(compound_dir)
    terms_prompt = PROMPT_TERMS.read_text(encoding="utf-8")
    term_user = json.dumps(
        {"compound_name": compound_name, "context_snippet": context_snippet},
        ensure_ascii=False,
    )
    raw_terms = call_llm(client, model, terms_prompt, term_user, TERM_MAX_TOKENS)
    terms = _parse_json_array(raw_terms) or []
    terms = [str(t).strip() for t in terms if str(t).strip()][:MAX_TERMS]
    if not terms:
        terms = [
            f'"{compound_name}" adverse effects toxicity',
            f'"{compound_name}" contraindications safety',
            f'"{compound_name}" drug safety humans',
        ][:MAX_TERMS]
    print(f"  [openalex-risk] search terms: {terms}", file=sys.stderr)

    cache: dict[str, list[dict[str, Any]]] = {}
    if cache_path.is_file():
        try:
            raw_cache = json.loads(cache_path.read_text(encoding="utf-8"))
            if isinstance(raw_cache, dict):
                cache = raw_cache
        except (OSError, json.JSONDecodeError):
            pass

    session = requests.Session()
    candidates: list[dict[str, Any]] = []
    seen: set[str] = set()
    for term in terms:
        key = f"search:{term}"
        if key not in cache:
            cache[key] = _search_openalex(term, session, PER_PAGE_PER_TERM)
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        for w in cache.get(key, []):
            oid = w.get("openalex_id") or w.get("doi") or ""
            if oid and oid in seen:
                continue
            if oid:
                seen.add(oid)
            entry = dict(w)
            entry["search_term"] = term
            candidates.append(entry)

    print(f"  [openalex-risk] {len(candidates)} unique works from OpenAlex", file=sys.stderr)

    picker_prompt = (
        PROMPT_PICKER.read_text(encoding="utf-8").replace("{max_works}", str(max_works))
    )
    picker_input = {
        "compound_name": compound_name,
        "candidates": [
            {
                "index": i,
                "title": c.get("title") or "",
                "year": c.get("year"),
                "cited_by_count": c.get("cited_by_count"),
                "has_abstract": bool(c.get("abstract")),
            }
            for i, c in enumerate(candidates)
        ],
    }
    raw_pick = call_llm(client, model, picker_prompt, json.dumps(picker_input, ensure_ascii=False), PICKER_MAX_TOKENS)
    picked = _parse_json_array(raw_pick) or []
    indices: list[int] = []
    for x in picked:
        try:
            indices.append(int(x))
        except (TypeError, ValueError):
            continue
    indices = [i for i in indices if 0 <= i < len(candidates)][:max_works]
    if not indices and candidates:
        ranked = sorted(
            range(len(candidates)),
            key=lambda i: (candidates[i].get("cited_by_count") or 0),
            reverse=True,
        )
        indices = ranked[:max_works]

    selected = [candidates[i] for i in indices]
    print(f"  [openalex-risk] selected {len(selected)} works for screening", file=sys.stderr)

    window_prompt = PROMPT_WINDOW.read_text(encoding="utf-8")
    risk_findings: list[dict[str, Any]] = []

    if not skip_windows:
        for work in selected:
            abstract = work.get("abstract") or ""
            if not abstract:
                continue
            excerpts: list[str] = []
            for window_text in _chunk_text(abstract, WINDOW_CHARS, WINDOW_OVERLAP, MAX_WINDOWS_PER_WORK):
                w_user = json.dumps(
                    {
                        "compound_name": compound_name,
                        "title": work.get("title"),
                        "year": work.get("year"),
                        "doi": work.get("doi"),
                        "openalex_id": work.get("openalex_id"),
                        "window_text": window_text,
                    },
                    ensure_ascii=False,
                )
                raw_w = call_llm(client, model, window_prompt, w_user, WINDOW_MAX_TOKENS)
                chunk_findings = _parse_json_array(raw_w) or []
                for f in chunk_findings:
                    s = str(f).strip()
                    if s and s not in excerpts:
                        excerpts.append(s)
            if excerpts:
                risk_findings.append({
                    "title": work.get("title"),
                    "year": work.get("year"),
                    "doi": work.get("doi"),
                    "openalex_id": work.get("openalex_id"),
                    "search_term": work.get("search_term"),
                    "excerpts": excerpts[:5],
                    "relevance": "openalex_risk_screen",
                })

    payload: dict[str, Any] = {
        "$schema_hint": "pump-science.openalex_risk_context.v1",
        "compound_name": compound_name,
        "source_grouped_file": GROUPED_FILENAME,
        "curated_risk_unit_count": curated_count,
        "search_terms": terms,
        "works_considered": len(candidates),
        "works_selected": len(selected),
        "risk_findings": risk_findings,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  [openalex-risk] wrote {output_path} ({len(risk_findings)} works with findings)", file=sys.stderr)
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--compound", required=True, help="Compound name")
    ap.add_argument("--compound-dir", type=Path, required=True, help="Compound data directory")
    ap.add_argument("--output", type=Path, default=None, help=f"Output JSON (default: <dir>/{OUTPUT_FILENAME})")
    ap.add_argument("--cache", type=Path, default=None, help=f"OpenAlex cache (default: <dir>/{CACHE_FILENAME})")
    ap.add_argument("--model", default=None, help="LLM model id")
    ap.add_argument("--max-works", type=int, default=DEFAULT_MAX_WORKS, help="Max works to screen (default 20)")
    ap.add_argument("--skip-windows", action="store_true", help="Title pick only; skip abstract window screening")
    args = ap.parse_args()

    compound_dir = args.compound_dir.expanduser().resolve()
    compound_dir.mkdir(parents=True, exist_ok=True)
    output_path = (args.output or compound_dir / OUTPUT_FILENAME).expanduser().resolve()
    cache_path = (args.cache or compound_dir / CACHE_FILENAME).expanduser().resolve()
    grouped_path = compound_dir / GROUPED_FILENAME

    if _should_skip_fetch(output_path, grouped_path):
        return 0

    client = OpenAI(base_url=VLLM_BASE_URL, api_key=VLLM_API_KEY)
    model = args.model or get_available_model(client)

    run_search(
        compound_name=args.compound.strip(),
        compound_dir=compound_dir,
        output_path=output_path,
        cache_path=cache_path,
        client=client,
        model=model,
        max_works=max(1, min(args.max_works, DEFAULT_MAX_WORKS)),
        skip_windows=args.skip_windows,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
