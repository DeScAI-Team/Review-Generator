#!/usr/bin/env python3
"""
Run the full empirical evidence-review pipeline (triage → retrieve_compare →
prep → review → originality_check → screener → score).

Expects an article folder (typically under articles/data/<stem>/) that already
contains upstream artifacts:

  - grouped.json
  - text_knowledge_base.jsonl
  - full.md

Writes all intermediates and final review.json under:

  <output-dir>/<research-folder>/

where <research-folder> is derived from the paper title extracted from the KB
(same heuristic as profile_read_paper.extract_title), not the PDF filename.

Environment: same as other empirical scripts (VLLM_BASE_URL, VLLM_API_KEY).
Model id is passed via --model (sets VALIDATOR_MODEL for subprocesses).

Example:
  python empirical-pipe.py --input-dir "../../../articles/data/document (10)"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

_EMPIRICAL = Path(__file__).resolve().parent
_PIPELINE = _EMPIRICAL.parent
_REPO_ROOT = _PIPELINE.parent.parent
DEFAULT_OUTPUT_DIR = _REPO_ROOT / "articles" / "data"
MAPPINGS = _PIPELINE / "mappings.json"
PY = sys.executable

_WIN_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
}


def _safe_research_name(name: str) -> str:
    """Filesystem-safe folder name (Windows-friendly)."""
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" ._-") or "research"
    if len(safe) > 120:
        safe = safe[:120]
    if safe.upper() in _WIN_RESERVED:
        safe = f"_{safe}_"
    return safe


def _import_profile_helpers():
    """Load extract_title / load_chunks from profile_read_paper (same dir as empirical/)."""
    if str(_PIPELINE) not in sys.path:
        sys.path.insert(0, str(_PIPELINE))
    from profile_read_paper import extract_title, load_chunks  # noqa: PLC0415

    return extract_title, load_chunks


def _first_doc_name_from_grouped(grouped_path: Path) -> str:
    data = json.loads(grouped_path.read_text(encoding="utf-8"))
    for dim_data in data.values():
        if not isinstance(dim_data, dict):
            continue
        for m in dim_data.get("members") or []:
            if not isinstance(m, dict):
                continue
            dn = m.get("doc_name")
            if dn:
                return str(dn).strip()
    return ""


def _title_from_fullmd(fullmd_path: Path) -> str | None:
    text = fullmd_path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# ") and len(line) > 3:
            title = line[2:].strip()
            if title:
                return title
    return None


def resolve_run_folder_name(input_dir: Path, kb_path: Path, grouped_path: Path, fullmd_path: Path) -> str:
    """Paper title from KB chunks (profile heuristic), else full.md H1, else folder name."""
    extract_title, load_chunks = _import_profile_helpers()
    doc_name = _first_doc_name_from_grouped(grouped_path) or input_dir.name
    chunks = load_chunks(kb_path, doc_name)
    title = extract_title(chunks) if chunks else None
    if title and str(title).strip():
        raw = str(title).strip()
    else:
        raw = _title_from_fullmd(fullmd_path) or input_dir.name
    return _safe_research_name(raw)


def _unique_run_dir(base: Path) -> Path:
    if not base.exists():
        return base
    stem = base.name
    parent = base.parent
    for n in range(2, 1000):
        cand = parent / f"{stem}_{n}"
        if not cand.exists():
            return cand
    raise FileExistsError(f"could not allocate unique folder under {parent}")


def run_step(label: str, cmd: list[str], *, env: dict | None = None) -> None:
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    print(f"  cmd: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env)
    if result.returncode != 0:
        print(f"  FAILED (exit {result.returncode})")
        sys.exit(result.returncode)
    print("  OK")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run empirical pipeline (triage through unified score).",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Article folder with grouped.json, text_knowledge_base.jsonl, and full.md",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Parent directory for the run folder (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=os.environ.get("VALIDATOR_MODEL", "/model"),
        help="LLM model id for vLLM-compatible API (sets VALIDATOR_MODEL; default: env or /model)",
    )
    parser.add_argument(
        "--skip-llm",
        action="store_true",
        help="Skip LLM in retrieve_compare, originality_check, screener, and score",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Use output path even if it already exists (may mix runs)",
    )
    args = parser.parse_args()

    input_dir = args.input_dir.expanduser().resolve()
    output_parent = args.output_dir.expanduser().resolve()

    grouped_src = input_dir / "grouped.json"
    kb_src = input_dir / "text_knowledge_base.jsonl"
    fullmd_src = input_dir / "full.md"

    for p, label in (
        (grouped_src, "grouped.json"),
        (kb_src, "text_knowledge_base.jsonl"),
        (fullmd_src, "full.md"),
    ):
        if not p.is_file():
            print(f"error: missing {label}: {p}", file=sys.stderr)
            sys.exit(1)

    folder_key = resolve_run_folder_name(input_dir, kb_src, grouped_src, fullmd_src)
    run_dir = output_parent / folder_key
    if not args.overwrite:
        run_dir = _unique_run_dir(run_dir)

    run_dir.mkdir(parents=True, exist_ok=True)

    grouped = run_dir / "grouped.json"
    kb_dest = run_dir / "text_knowledge_base.jsonl"
    full_md = run_dir / "full.md"

    shutil.copy2(grouped_src, grouped)
    shutil.copy2(kb_src, kb_dest)
    shutil.copy2(fullmd_src, full_md)

    print(f"Research folder name (from pipeline title heuristic): {folder_key}")
    print(f"Run directory: {run_dir}")

    base_env = {**os.environ, "VALIDATOR_MODEL": args.model}

    triaged = run_dir / "triaged.json"
    run_step(
        "1/7 — Triage",
        [
            PY,
            str(_EMPIRICAL / "triage.py"),
            str(grouped),
            "-o",
            str(triaged),
            "--mappings",
            str(MAPPINGS),
        ],
        env=base_env,
    )

    use_llm = not args.skip_llm
    rc_out = run_dir / ("retrieve_compare_llm.json" if use_llm else "retrieve_compare_out.json")
    rc_cmd = [
        PY,
        str(_EMPIRICAL / "retrieve_compare.py"),
        str(triaged),
        "--kb",
        str(kb_dest),
        "--fullmd",
        str(full_md),
        "--openalex-cache",
        str(run_dir / "openalex_cache.json"),
        "-o",
        str(rc_out),
    ]
    if not use_llm:
        rc_cmd.append("--skip-llm")
    run_step(
        f"2/7 — Retrieve & compare ({'LLM' if use_llm else 'skip-llm'})",
        rc_cmd,
        env=base_env,
    )

    prepped_evidence = run_dir / "prepped_evidence.json"
    run_step(
        "3/7 — Prep evidence narratives",
        [PY, str(_EMPIRICAL / "prep.py"), str(rc_out), "-o", str(prepped_evidence)],
        env=base_env,
    )

    review_out = run_dir / "review.json"
    review_cmd = [
        PY,
        str(_EMPIRICAL / "review.py"),
        str(prepped_evidence),
        "--mappings",
        str(MAPPINGS),
        "-o",
        str(review_out),
        "--pre-condensed-dump",
        str(run_dir / "pre_condensed_rationales.json"),
    ]
    run_step("4/7 — Review (rationales)", review_cmd, env=base_env)

    originality_out = run_dir / "originality.json"
    originality_cmd = [
        PY,
        str(_EMPIRICAL / "originality_check.py"),
        "--directory",
        str(run_dir),
        "--fullmd",
        str(full_md),
        "--kb",
        str(kb_dest),
        "--openalex-cache",
        str(run_dir / "originality_openalex_cache.json"),
        "-o",
        str(originality_out),
        "--review",
        str(review_out),
    ]
    if args.skip_llm:
        originality_cmd.append("--skip-llm")
    run_step(
        f"5/7 — Originality ({'LLM' if use_llm else 'skip-llm'})",
        originality_cmd,
        env=base_env,
    )

    screener_out = run_dir / "screener.json"
    screener_cmd = [
        PY,
        str(_EMPIRICAL / "screener.py"),
        "--fullmd",
        str(full_md),
        "--openalex-cache",
        str(run_dir / "openalex_cache.json"),
        "--mappings",
        str(MAPPINGS),
        "--review",
        str(review_out),
        "-o",
        str(screener_out),
    ]
    if args.skip_llm:
        screener_cmd.append("--skip-llm")
    run_step(
        f"6/7 — Screener ({'LLM' if use_llm else 'skip-llm'})",
        screener_cmd,
        env=base_env,
    )

    score_cmd = [
        PY,
        str(_EMPIRICAL / "score.py"),
        "--review",
        str(review_out),
        "--prepped-evidence",
        str(prepped_evidence),
        "--originality",
        str(originality_out),
        "--screener",
        str(screener_out),
        "--mappings",
        str(MAPPINGS),
        "-o",
        str(review_out),
    ]
    if args.skip_llm:
        score_cmd.append("--skip-llm")
    run_step(
        f"7/7 — Unified score ({'LLM' if use_llm else 'skip-llm'})",
        score_cmd,
        env=base_env,
    )

    print(f"\n{'='*60}")
    print("  EMPIRICAL PIPELINE COMPLETE")
    print(f"  Output: {run_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
