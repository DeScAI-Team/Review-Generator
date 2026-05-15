#!/usr/bin/env python3
"""
Top-level orchestrator.

Step 1: Crawl  (node crawlers/full-crawl.mjs)
Step 2: Review articles  (articles/pipeline/run_full_pipeline.py per paper)
Step 3: DAO reviews  (DAOs/molecule/pipeline/run_dao_pipeline.py --batch)
Step 4: Proposal reviews  (proposals/pipeline/proposal_pipe.py per proposal)
Step 5: Compound reviews  (compounds/orchestrate.py per token)

Usage:
  python orchestrate.py                   # full run
  python orchestrate.py --dry-run         # smoke test: print commands, execute nothing
  python orchestrate.py --no-vis          # skip vision/LLM steps (stop article pipeline after add_data)
  python orchestrate.py --skip-crawl      # reuse existing crawl output
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

PAPERS_DIR = REPO_ROOT / "crawlers" / "output" / "researchhub" / "papers"
ARTICLE_OUTPUT_DIR = REPO_ROOT / "reviews" / "articles"
PIPELINE_SCRIPT = REPO_ROOT / "articles" / "pipeline" / "run_full_pipeline.py"
CRAWL_SCRIPT = REPO_ROOT / "crawlers" / "full-crawl.mjs"

MOLECULE_INPUT_DIR = REPO_ROOT / "crawlers" / "output" / "molecule"
DAO_OUTPUT_DIR = REPO_ROOT / "reviews" / "DAOs"
DAO_PIPELINE_SCRIPT = REPO_ROOT / "DAOs" / "molecule" / "pipeline" / "run_dao_pipeline.py"

PROPOSALS_DIR = REPO_ROOT / "crawlers" / "output" / "researchhub" / "proposals"
PROPOSAL_OUTPUT_DIR = REPO_ROOT / "reviews" / "proposals"
PROPOSAL_PIPELINE_SCRIPT = REPO_ROOT / "proposals" / "pipeline" / "proposal_pipe.py"

COMPOUND_TOKENS_FILE = REPO_ROOT / "crawlers" / "output" / "pump.science" / "compound-tokens.json"
COMPOUND_ORCHESTRATOR = REPO_ROOT / "compounds" / "orchestrate.py"

PY = sys.executable


def _banner(msg: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {msg}")
    print(f"{'=' * 60}\n", flush=True)


# ── Step 1: Crawl ────────────────────────────────────────────

def run_crawl(*, dry_run: bool) -> None:
    _banner("Step 1 — Crawl (full-crawl.mjs)")
    cmd = ["node", str(CRAWL_SCRIPT), "--no-upload"]
    print(f"  cmd: {' '.join(cmd)}")

    if dry_run:
        print("  [dry-run] skipped")
        return

    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if result.returncode != 0:
        print(f"\n  FAILED (exit {result.returncode}). Stopping.", file=sys.stderr)
        sys.exit(result.returncode)
    print("  OK")


# ── Step 2: Article reviews (batch) ──────────────────────────

def _collect_papers() -> list[tuple[Path, str]]:
    """Return [(json_path, pdf_url), ...] for every paper with a usable pdf_url."""
    if not PAPERS_DIR.is_dir():
        return []
    pairs: list[tuple[Path, str]] = []
    for p in sorted(PAPERS_DIR.glob("PaperRecord_*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"  ! skipping {p.name}: {exc}")
            continue
        url = data.get("pdf_url")
        if not url:
            print(f"  ! skipping {p.name}: no pdf_url")
            continue
        pairs.append((p, url))
    return pairs


def run_article_reviews(*, dry_run: bool, no_vis: bool) -> None:
    _banner("Step 2 — Article reviews")

    papers = _collect_papers()
    if not papers:
        print("  No papers found in", PAPERS_DIR)
        return

    print(f"  Found {len(papers)} paper(s) with pdf_url\n")

    ARTICLE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, bool, str]] = []  # (name, ok, detail)

    for i, (json_path, pdf_url) in enumerate(papers, 1):
        label = json_path.stem
        _banner(f"[{i}/{len(papers)}] {label}")

        cmd = [
            PY,
            str(PIPELINE_SCRIPT),
            pdf_url,
            "--output-dir", str(ARTICLE_OUTPUT_DIR),
            "--skip-upload",
        ]
        if no_vis:
            cmd += ["--stop-after", "add_data"]

        print(f"  cmd: {' '.join(cmd)}")

        if dry_run:
            print("  [dry-run] skipped")
            results.append((label, True, "dry-run"))
            continue

        t0 = time.monotonic()
        result = subprocess.run(cmd, cwd=str(REPO_ROOT))
        elapsed = time.monotonic() - t0

        if result.returncode != 0:
            detail = f"exit {result.returncode} ({elapsed:.0f}s)"
            print(f"  FAILED — {detail}")
            results.append((label, False, detail))
        else:
            detail = f"ok ({elapsed:.0f}s)"
            print(f"  OK — {detail}")
            results.append((label, True, detail))

    # ── Summary ──────────────────────────────────────────────
    _banner("Article review summary")
    ok_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - ok_count
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}  {detail}")
    print(f"\n  Total: {len(results)}  |  passed: {ok_count}  |  failed: {fail_count}")
    if fail_count:
        print("  ⚠ Some papers failed. See logs above for details.", file=sys.stderr)


# ── Step 3: DAO reviews (batch) ───────────────────────────────

def run_dao_reviews(*, dry_run: bool, no_vis: bool) -> None:
    _banner("Step 3 — DAO reviews (Molecule IP-NFTs)")

    cmd = [
        PY,
        str(DAO_PIPELINE_SCRIPT),
        "--batch", str(MOLECULE_INPUT_DIR),
        "--output-dir", str(DAO_OUTPUT_DIR),
        "--skip-upload",
    ]
    if no_vis:
        cmd += ["--stop-after", "ocr"]

    print(f"  cmd: {' '.join(cmd)}")

    if dry_run:
        print("  [dry-run] skipped")
        return

    t0 = time.monotonic()
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))
    elapsed = time.monotonic() - t0

    if result.returncode != 0:
        print(f"\n  FAILED (exit {result.returncode}) after {elapsed:.0f}s", file=sys.stderr)
        sys.exit(result.returncode)
    print(f"  OK ({elapsed:.0f}s)")


# ── Step 4: Proposal reviews (batch) ─────────────────────────

def _collect_proposals() -> list[Path]:
    """Return sorted list of proposal JSON files from the crawl output."""
    if not PROPOSALS_DIR.is_dir():
        return []
    return sorted(PROPOSALS_DIR.glob("proposal_*.json"))


def run_proposal_reviews(*, dry_run: bool, no_vis: bool) -> None:
    _banner("Step 4 — Proposal reviews")

    proposals = _collect_proposals()
    if not proposals:
        print("  No proposals found in", PROPOSALS_DIR)
        return

    print(f"  Found {len(proposals)} proposal(s)\n")

    PROPOSAL_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, bool, str]] = []

    for i, json_path in enumerate(proposals, 1):
        label = json_path.stem
        proposal_out = PROPOSAL_OUTPUT_DIR / label
        _banner(f"[{i}/{len(proposals)}] {label}")

        cmd = [
            PY,
            str(PROPOSAL_PIPELINE_SCRIPT),
            "--input-json", str(json_path),
            "--output-dir", str(proposal_out),
        ]
        if no_vis:
            cmd.append("--skip-llm")

        print(f"  cmd: {' '.join(cmd)}")

        if dry_run:
            print("  [dry-run] skipped")
            results.append((label, True, "dry-run"))
            continue

        t0 = time.monotonic()
        result = subprocess.run(cmd, cwd=str(REPO_ROOT))
        elapsed = time.monotonic() - t0

        if result.returncode != 0:
            detail = f"exit {result.returncode} ({elapsed:.0f}s)"
            print(f"  FAILED — {detail}")
            results.append((label, False, detail))
        else:
            detail = f"ok ({elapsed:.0f}s)"
            print(f"  OK — {detail}")
            results.append((label, True, detail))

    # ── Summary ──────────────────────────────────────────────
    _banner("Proposal review summary")
    ok_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - ok_count
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}  {detail}")
    print(f"\n  Total: {len(results)}  |  passed: {ok_count}  |  failed: {fail_count}")
    if fail_count:
        print("  Some proposals failed. See logs above for details.", file=sys.stderr)


# ── Step 5: Compound reviews (batch) ─────────────────────────

def _parse_intervention(intervention: str) -> list[str]:
    """Parse an intervention string into individual compound names.

    "Doxycycline"                                  -> ["Doxycycline"]
    "compound 1: Omipalisib; compound 2: Doxycycline" -> ["Omipalisib", "Doxycycline"]
    """
    if re.search(r"compound\s+\d+\s*:", intervention, re.IGNORECASE):
        parts = re.split(r";\s*", intervention)
        names = []
        for part in parts:
            m = re.match(r"compound\s+\d+\s*:\s*(.+)", part.strip(), re.IGNORECASE)
            if m:
                names.append(m.group(1).strip())
        return names
    return [intervention.strip()] if intervention.strip() else []


def _collect_compound_tokens() -> list[tuple[str, list[str]]]:
    """Return [(ticker, [compound_names]), ...] from the crawl output."""
    if not COMPOUND_TOKENS_FILE.is_file():
        return []
    try:
        tokens = json.loads(COMPOUND_TOKENS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"  ! failed to read {COMPOUND_TOKENS_FILE.name}: {exc}")
        return []
    entries: list[tuple[str, list[str]]] = []
    for t in tokens:
        ticker = t.get("ticker", "")
        intervention = t.get("intervention", "")
        names = _parse_intervention(intervention)
        if names:
            entries.append((ticker, names))
        else:
            print(f"  ! skipping {ticker}: empty intervention")
    return entries


def run_compound_reviews(*, dry_run: bool, no_vis: bool) -> None:
    _banner("Step 5 — Compound reviews (pump.science)")

    tokens = _collect_compound_tokens()
    if not tokens:
        print("  No compound tokens found in", COMPOUND_TOKENS_FILE)
        return

    print(f"  Found {len(tokens)} token(s)\n")

    results: list[tuple[str, bool, str]] = []

    for i, (ticker, compounds) in enumerate(tokens, 1):
        label = f"{ticker} ({', '.join(compounds)})"
        _banner(f"[{i}/{len(tokens)}] {label}")

        cmd = [
            PY,
            str(COMPOUND_ORCHESTRATOR),
            "--compounds", *compounds,
        ]
        if no_vis:
            cmd.append("--skip-upload")

        print(f"  cmd: {' '.join(cmd)}")

        if dry_run:
            print("  [dry-run] skipped")
            results.append((label, True, "dry-run"))
            continue

        t0 = time.monotonic()
        result = subprocess.run(cmd, cwd=str(REPO_ROOT))
        elapsed = time.monotonic() - t0

        if result.returncode != 0:
            detail = f"exit {result.returncode} ({elapsed:.0f}s)"
            print(f"  FAILED — {detail}")
            results.append((label, False, detail))
        else:
            detail = f"ok ({elapsed:.0f}s)"
            print(f"  OK — {detail}")
            results.append((label, True, detail))

    # ── Summary ──────────────────────────────────────────────
    _banner("Compound review summary")
    ok_count = sum(1 for _, ok, _ in results if ok)
    fail_count = len(results) - ok_count
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}  {detail}")
    print(f"\n  Total: {len(results)}  |  passed: {ok_count}  |  failed: {fail_count}")
    if fail_count:
        print("  Some compounds failed. See logs above for details.", file=sys.stderr)


# ── Main ─────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Top-level orchestrator: crawl → articles → DAOs → proposals → compounds.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print commands but don't execute anything (smoke test)",
    )
    parser.add_argument(
        "--no-vis",
        action="store_true",
        help="Skip vision/LLM model steps (article pipeline stops after add_data)",
    )
    parser.add_argument(
        "--skip-crawl",
        action="store_true",
        help="Skip step 1; use existing crawl output",
    )
    args = parser.parse_args()

    if not args.skip_crawl:
        run_crawl(dry_run=args.dry_run)

    run_article_reviews(dry_run=args.dry_run, no_vis=args.no_vis)

    run_dao_reviews(dry_run=args.dry_run, no_vis=args.no_vis)

    run_proposal_reviews(dry_run=args.dry_run, no_vis=args.no_vis)

    run_compound_reviews(dry_run=args.dry_run, no_vis=args.no_vis)


if __name__ == "__main__":
    main()
