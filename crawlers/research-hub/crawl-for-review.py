#!/usr/bin/env python3
"""
Run papers.py (journal metadata + PDF URLs) and proposal.py (active fundraises) in parallel.
Writes to <output-dir>/papers and <output-dir>/proposals respectively.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _run_subprocess(label: str, cmd: list[str]) -> tuple[str, int]:
    print(f"Starting {label}…", flush=True)
    r = subprocess.run(cmd, cwd=str(ROOT))
    print(f"Finished {label} (exit {r.returncode})", flush=True)
    return label, r.returncode


def main() -> None:
    p = argparse.ArgumentParser(
        description="Run journal papers export and active proposals export (parallel)."
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=Path("review_crawl"),
        help="Root directory; creates papers/ and proposals/ inside it",
    )
    p.add_argument(
        "--crawl-skip-file",
        type=Path,
        default=None,
        help="JSON with moleculeFolders + researchhubFiles (written by full-crawl.mjs)",
    )
    args = p.parse_args()

    out = args.output_dir.resolve()
    papers_dir = out / "papers"
    proposals_dir = out / "proposals"
    papers_dir.mkdir(parents=True, exist_ok=True)
    proposals_dir.mkdir(parents=True, exist_ok=True)

    py = sys.executable
    papers_cmd = [
        py,
        str(ROOT / "papers.py"),
        "--output-dir",
        str(papers_dir),
    ]
    proposal_cmd = [
        py,
        str(ROOT / "proposal.py"),
        "--output-dir",
        str(proposals_dir),
    ]
    if args.crawl_skip_file is not None:
        sf = str(args.crawl_skip_file.resolve())
        papers_cmd.extend(["--crawl-skip-file", sf])
        proposal_cmd.extend(["--crawl-skip-file", sf])

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [
            pool.submit(_run_subprocess, "papers.py", papers_cmd),
            pool.submit(_run_subprocess, "proposal.py", proposal_cmd),
        ]
        results = [f.result() for f in futures]

    failed = [name for name, code in results if code != 0]
    if failed:
        print(f"Failed: {', '.join(failed)}", file=sys.stderr)
        sys.exit(1)
    print(f"All done. Output: {out}")


if __name__ == "__main__":
    main()
