#!/usr/bin/env python3
r"""Generate a four-category combination review from an interactions.py evidence bundle via vLLM.

Reads the JSON output of ``interactions.py`` and calls the LLM four times:

1. ``prompts/pump-science-combination-scientific-grounding-evaluation.md``
   Receives per-compound {name, score, grounding_rationale}.
   Produces a combined ``scientific_grounding`` paragraph.

2. ``prompts/pump-science-combination-risk-statement-evaluation.md``
   Receives per-compound {name, risk_rationale, spl_available, spl_interaction_excerpts}.
   Produces a combined ``risk`` paragraph.

3. ``prompts/pump-science-compatibility-evaluation.md``
   Receives the cross_reference bundle + per-compound {kegg_flags_present, spl_interaction_excerpts,
   mechanism_snippets}.
   Produces the ``compatibility`` paragraph.

4. ``prompts/pump-science-combination-review-statement-evaluation.md``
   Receives a compact bundle (all three paragraphs + scores + combination metadata).
   Produces the final ``review_statement`` paragraph.

Output is written as ``<repo>/reviews/compounds/<combination>/<combination>-combo-review.json``
by default, or to a path supplied via ``-o``. The JSON shape matches article ``overview.json``
(fewer fields): ``research_name``, ``review_date``, ``composite_score`` (0–100),
``review_statement`` (with a ``Compound(s): …`` prefix), and ``categories`` with
percent scores (0–100) plus rationales.

Usage:
  python review-multiple.py pump-science/data/omipa-ginse-uroli.json
  python review-multiple.py bundle.json -o my-review.json --model mixtral-8x7b-instruct
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

from openai import OpenAI, RateLimitError


def get_available_model(client: OpenAI, env_var_name: str, fallback_env_vars: list[str]) -> str:
    """
    Discover available model from vLLM server or environment variables.
    
    Priority:
    1. Query vLLM /v1/models endpoint
    2. Check env_var_name (e.g., TAGGER_MODEL, REVIEWER_MODEL)
    3. Check fallback_env_vars (e.g., CLASSIFIER_MODEL, VALIDATOR_MODEL)
    4. Raise error with helpful message
    """
    # Try to query vLLM for available models
    try:
        models = client.models.list()
        if models.data and len(models.data) > 0:
            model_id = models.data[0].id
            print(f"  Auto-discovered model: {model_id}", file=sys.stderr)
            return model_id
    except Exception as e:
        print(f"  Could not auto-discover models from vLLM: {e}", file=sys.stderr)
    
    # Fallback to environment variables
    for env_name in [env_var_name] + fallback_env_vars:
        val = os.environ.get(env_name)
        if val:
            print(f"  Using model from {env_name}: {val}", file=sys.stderr)
            return val
    
    # No model found - provide helpful error
    env_list = ", ".join([env_var_name] + fallback_env_vars)
    raise ValueError(
        f"No model specified and could not auto-discover from vLLM.\n"
        f"Please set one of these environment variables: {env_list}\n"
        f"Or ensure vLLM is running at {os.environ.get('VLLM_BASE_URL', 'http://localhost:8000/v1')}"
    )


REPO_ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = REPO_ROOT / "prompts"

_PROMPT_GROUNDING = PROMPTS_DIR / "pump-science-combination-scientific-grounding-evaluation.md"
_PROMPT_RISK = PROMPTS_DIR / "pump-science-combination-risk-statement-evaluation.md"
_PROMPT_COMPAT = PROMPTS_DIR / "pump-science-compatibility-evaluation.md"
_PROMPT_STATEMENT = PROMPTS_DIR / "pump-science-combination-review-statement-evaluation.md"

if load_dotenv is not None:
    load_dotenv(REPO_ROOT / ".env")

VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
VLLM_API_KEY = os.environ.get("VLLM_API_KEY", "none")

DEFAULT_RISK_SCORE_PCT = 25.0

# Model discovery happens later in main() after client is created
MAX_RETRIES = 4
MAX_REVIEWER_TOKENS = max(256, int(os.environ.get("REVIEWER_MAX_TOKENS", "2048")))

_END_THINK_MARKERS = (
    "</think>",
    "</think>",
    "</thinking>",
    "</reasoning>",
    "</thought>",
)


# ---------------------------------------------------------------------------
# LLM helpers (identical contract to review.py)
# ---------------------------------------------------------------------------

def strip_reasoning_markup(s: str) -> str:
    """Drop chain-of-thought wrappers; prefer text after the last end-thinking marker."""
    t = s.strip()
    low = t.lower()
    best_idx = -1
    best_len = 0
    for m in _END_THINK_MARKERS:
        pos = low.rfind(m.lower())
        if pos > best_idx:
            best_idx = pos
            best_len = len(m)
    if best_idx >= 0:
        t = t[best_idx + best_len:].lstrip()
    block_patterns = (
        r"<think\b[^>]*>[\s\S]*?</think>",
        r"<thinking\b[^>]*>[\s\S]*?</thinking>",
        r"<reasoning\b[^>]*>[\s\S]*?</reasoning>",
        r"<thought\b[^>]*>[\s\S]*?</thought>",
        r"<redacted_thinking\b[^>]*>[\s\S]*?</think>",
    )
    for _ in range(8):
        prev = t
        for pat in block_patterns:
            t = re.sub(pat, "", t, flags=re.IGNORECASE)
        if t == prev:
            break
    # Strip unclosed opening think block (model output thinking but never closed the tag).
    t = re.sub(r"<think\b[^>]*>[\s\S]*$", "", t, flags=re.IGNORECASE).strip()
    return t.strip()


def call_llm(client: OpenAI, model: str, system_prompt: str, user_content: str) -> str:
    """Send a chat completion and return the stripped response text."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content},
    ]

    def _complete() -> object:
        kw: dict[str, object] = dict(
            model=model,
            max_tokens=MAX_REVIEWER_TOKENS,
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=messages,
        )
        try:
            return client.chat.completions.create(**kw, extra_body={"top_k": -1})
        except TypeError:
            return client.chat.completions.create(**kw)

    for attempt in range(MAX_RETRIES):
        try:
            response = _complete()
            content = response.choices[0].message.content
            return strip_reasoning_markup((content or "").strip())
        except RateLimitError:
            wait = (2 ** attempt) * 5
            print(
                f"  [RATE LIMIT] attempt {attempt + 1}/{MAX_RETRIES} — waiting {wait}s...",
                file=sys.stderr,
            )
            time.sleep(wait)
        except Exception as e:
            msg = str(e)[:120]
            print(
                f"  [ERROR] attempt {attempt + 1}/{MAX_RETRIES}: {msg}",
                file=sys.stderr,
            )
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** attempt)
            else:
                return ""
    return ""


# ---------------------------------------------------------------------------
# Context builders — one per LLM pass
# ---------------------------------------------------------------------------

def _build_grounding_ctx(bundle: dict) -> dict:
    """Pass 1: per-compound grounding scores and rationales."""
    compounds_list = []
    for name, ev in bundle.get("compounds", {}).items():
        compounds_list.append({
            "compound_name": name,
            "scientific_grounding_score": ev.get("scientific_grounding_score"),
            "scientific_grounding_rationale": ev.get("scientific_grounding_rationale") or "",
        })
    return {
        "combination_name": bundle.get("combination_name", "Unknown combination"),
        "compounds": compounds_list,
    }


def _build_risk_ctx(bundle: dict) -> dict:
    """Pass 2: per-compound risk rationales and SPL interaction excerpts."""
    compounds_list = []
    for name, ev in bundle.get("compounds", {}).items():
        spl = ev.get("spl") or {}
        compounds_list.append({
            "compound_name": name,
            "risk_rationale": ev.get("risk_rationale") or "",
            "spl_available": spl.get("label_matched", False),
            "spl_interaction_excerpts": spl.get("interaction_excerpts") or [],
        })
    return {
        "combination_name": bundle.get("combination_name", "Unknown combination"),
        "compounds": compounds_list,
    }


def _build_compat_ctx(bundle: dict) -> dict:
    """Pass 3: cross-reference bundle + per-compound pathway/mechanism context."""
    compounds_list = []
    for name, ev in bundle.get("compounds", {}).items():
        spl = ev.get("spl") or {}
        kegg = ev.get("kegg") or {}
        mechanism_snippets = [
            mu.get("snippet") for mu in (ev.get("mechanism_units") or [])
            if mu.get("snippet")
        ][:5]  # cap at 5 snippets per compound to keep context tractable
        compounds_list.append({
            "compound_name": name,
            "kegg_flags_present": kegg.get("flags_present") or [],
            "spl_available": spl.get("label_matched", False),
            "spl_interaction_excerpts": spl.get("interaction_excerpts") or [],
            "mechanism_snippets": mechanism_snippets,
        })

    xref = bundle.get("cross_reference") or {}
    return {
        "combination_name": bundle.get("combination_name", "Unknown combination"),
        "compounds": compounds_list,
        "cross_reference": {
            "shared_pathways": xref.get("shared_pathways") or [],
            "explicit_mentions": xref.get("explicit_mentions") or [],
            "spl_coverage_summary": xref.get("spl_coverage_summary") or "",
        },
    }


def _build_statement_ctx(
    bundle: dict,
    grounding_text: str,
    risk_text: str,
    compat_text: str,
) -> dict:
    """Pass 4: compact bundle — all three paragraphs + aggregate metadata."""
    compounds_scores = [
        {
            "compound_name": name,
            "scientific_grounding_score": ev.get("scientific_grounding_score"),
            "risk_score": ev.get("risk_score"),
        }
        for name, ev in bundle.get("compounds", {}).items()
    ]

    # Aggregate coverage: collect coverage dicts across compounds (may be empty for some).
    # We report which fields were present in at least one compound.
    coverage_union: dict = {}
    for ev in bundle.get("compounds", {}).values():
        for field, info in (ev.get("coverage") or {}).items():
            if info.get("present") and field not in coverage_union:
                coverage_union[field] = True

    return {
        "combination_name": bundle.get("combination_name", "Unknown combination"),
        "compounds": compounds_scores,
        "total_units": None,       # not available from evidence bundle; prompt handles null
        "coverage": coverage_union or None,
        "scientific_grounding": grounding_text,
        "risk": risk_text,
        "compatibility": compat_text,
    }


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _default_output_path(in_path: Path, combination_name: str) -> Path:
    safe = re.sub(r'[<>:"/\\|?*]', "_", combination_name).strip().replace(" ", "-")[:80]
    # Output to reviews/compounds/<combination>/ instead of data/
    reviews_dir = REPO_ROOT.parent / "reviews" / "compounds" / safe
    reviews_dir.mkdir(parents=True, exist_ok=True)
    return reviews_dir / f"{safe}-combo-review.json"


def _avg_score(bundle: dict, field: str) -> float | None:
    scores = [
        ev.get(field)
        for ev in bundle.get("compounds", {}).values()
        if ev.get(field) is not None
    ]
    return round(sum(scores) / len(scores), 4) if scores else None


def _fraction_to_percent(value: float | None) -> float | None:
    """Scores from bundles are 0–1; overview-style output uses 0–100."""
    if value is None:
        return None
    v = float(value)
    if v <= 1.0:
        v *= 100.0
    return round(v, 2)


def _compound_subject_line(names: list[str]) -> str:
    if not names:
        return "Compound(s): (unknown)."
    if len(names) == 1:
        return f"Compound(s): {names[0]}."
    if len(names) == 2:
        return f"Compound(s): {names[0]} and {names[1]}."
    return "Compound(s): " + ", ".join(names[:-1]) + f", and {names[-1]}."


def _compat_signal_preamble(bundle: dict) -> str:
    xref = bundle.get("cross_reference") or {}
    sp = xref.get("shared_pathways") or []
    em = xref.get("explicit_mentions") or []
    if not isinstance(sp, list):
        sp = []
    if not isinstance(em, list):
        em = []
    if sp:
        sp_part = "Shared KEGG longevity pathway flags (hypothesis-level overlap): " + ", ".join(str(x) for x in sp) + ". "
    else:
        sp_part = "No shared KEGG longevity pathway flags between compounds. "
    return sp_part + f"Explicit name-token mentions of partner compounds in SPL/mechanism text: {len(em)}. "


def _compatibility_percent_score(bundle: dict) -> float:
    xref = bundle.get("cross_reference") or {}
    sp = xref.get("shared_pathways") or []
    em = xref.get("explicit_mentions") or []
    n_sp = len(sp) if isinstance(sp, list) else 0
    n_em = len(em) if isinstance(em, list) else 0
    raw = 100.0 - (n_sp * 14.0 + n_em * 12.0)
    return round(max(42.0, min(100.0, raw)), 2)


def _mean_of_numbers(values: list[float | None]) -> float | None:
    nums = [v for v in values if v is not None]
    if not nums:
        return None
    return round(sum(nums) / len(nums), 2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a four-category combination review "
            "(scientific_grounding + risk + compatibility + review_statement) "
            "from an interactions.py evidence bundle via vLLM."
        )
    )
    parser.add_argument(
        "input",
        type=Path,
        help="JSON evidence bundle produced by interactions.py.",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        metavar="PATH",
        help="Output JSON path (default: <repo>/reviews/compounds/<combination>/<combination>-combo-review.json).",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        metavar="NAME",
        help="Model id to use (default: auto-discovered from vLLM or REVIEWER_MODEL/TAGGER_MODEL/CLASSIFIER_MODEL/VALIDATOR_MODEL env vars).",
    )
    args = parser.parse_args()

    in_path: Path = args.input.expanduser().resolve()

    print(f"Loading {in_path}", file=sys.stderr)
    try:
        bundle = json.loads(in_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Cannot read input bundle: {exc}", file=sys.stderr)
        return 1

    combination_name: str = bundle.get("combination_name") or "Unknown combination"
    compound_names = list(bundle.get("compounds", {}).keys())

    print(f"  combination: {combination_name}", file=sys.stderr)
    print(f"  compounds:   {', '.join(compound_names)}", file=sys.stderr)

    # Check that per-compound review data is present.
    missing_review = [
        name for name, ev in bundle.get("compounds", {}).items()
        if not ev.get("scientific_grounding_rationale") and not ev.get("risk_rationale")
    ]
    if missing_review:
        print(
            f"  WARN: missing review data for: {missing_review}. "
            "Run review.py for each compound before review-multiple.py.",
            file=sys.stderr,
        )

    grounding_prompt = _PROMPT_GROUNDING.read_text(encoding="utf-8")
    risk_prompt = _PROMPT_RISK.read_text(encoding="utf-8")
    compat_prompt = _PROMPT_COMPAT.read_text(encoding="utf-8")
    statement_prompt = _PROMPT_STATEMENT.read_text(encoding="utf-8")

    client = OpenAI(base_url=VLLM_BASE_URL, api_key=VLLM_API_KEY)
    
    # Discover model
    model = args.model or get_available_model(
        client,
        "REVIEWER_MODEL",
        ["TAGGER_MODEL", "CLASSIFIER_MODEL", "VALIDATOR_MODEL"]
    )

    # ---- Pass 1: combined scientific grounding ----
    print("  [1/4] Generating combined scientific_grounding...", file=sys.stderr)
    grounding_ctx = _build_grounding_ctx(bundle)
    grounding_text = call_llm(
        client, model, grounding_prompt, json.dumps(grounding_ctx, ensure_ascii=False)
    )

    # ---- Pass 2: combined risk statement ----
    print("  [2/4] Generating combined risk statement...", file=sys.stderr)
    risk_ctx = _build_risk_ctx(bundle)
    risk_text = call_llm(
        client, model, risk_prompt, json.dumps(risk_ctx, ensure_ascii=False)
    )

    # ---- Pass 3: compatibility ----
    print("  [3/4] Generating compatibility assessment...", file=sys.stderr)
    compat_ctx = _build_compat_ctx(bundle)
    compat_text = call_llm(
        client, model, compat_prompt, json.dumps(compat_ctx, ensure_ascii=False)
    )
    if not compat_text:
        compat_text = (
            "Compatibility assessment could not be generated. "
            "Inspect the evidence bundle for cross-reference data."
        )

    # ---- Pass 4: combined review statement ----
    print("  [4/4] Generating combined review_statement...", file=sys.stderr)
    statement_ctx = _build_statement_ctx(bundle, grounding_text, risk_text, compat_text)
    review_statement = call_llm(
        client, model, statement_prompt, json.dumps(statement_ctx, ensure_ascii=False)
    )

    _now = datetime.now(timezone.utc)
    review_date = f"{_now.strftime('%B')} {_now.day}, {_now.year}"

    out_path: Path = (
        args.output.expanduser().resolve()
        if args.output is not None
        else _default_output_path(in_path, combination_name)
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sg_pct = _fraction_to_percent(_avg_score(bundle, "scientific_grounding_score"))
    risk_pct = _fraction_to_percent(_avg_score(bundle, "risk_score"))
    if risk_pct is None:
        risk_pct = DEFAULT_RISK_SCORE_PCT
    compat_pct = _compatibility_percent_score(bundle)
    compat_rationale = _compat_signal_preamble(bundle) + (compat_text or "").strip()

    composite = _mean_of_numbers([sg_pct, risk_pct, compat_pct])

    subject = _compound_subject_line(compound_names)
    stmt = (review_statement or "").strip()
    review_statement_out = f"{subject} {stmt}".strip() if stmt else subject

    review = {
        "research_name": combination_name,
        "review_date": review_date,
        "composite_score": composite,
        "review_statement": review_statement_out,
        "categories": {
            "scientific_grounding": {
                "score": sg_pct,
                "rationale": grounding_text,
            },
            "risk_assessment": {
                "score": risk_pct,
                "rationale": risk_text,
            },
            "compatibility": {
                "score": compat_pct,
                "rationale": compat_rationale,
            },
        },
    }

    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(review, fh, ensure_ascii=False, indent=2)

    print(f"Done. Wrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
