#!/usr/bin/env python3
"""Pump-science review orchestrator.

Single compound  →  run_review.py (full pipeline including evidence audit)

Multiple compounds → run_review.py per compound (unless ``--skip-individual``) with
                     reviews written under ``reviews/compounds/<combination-slug>/individual/<compound>/``
                     (no top-level ``reviews/compounds/<Compound>/`` folders for each name alone). Then ``interactions.py``,
                     ``review-multiple.py``, per-compound ``evidence-doc.py``, and finally
                     combination ``evidence-doc.py`` (all audits deferred to the end).

Usage:
  python orchestrate.py --compounds Doxycycline
  python orchestrate.py --compounds Omipalisib "Ginsenoside Rh2" "Urolithin A"
  python orchestrate.py --compounds Omipalisib "Ginsenoside Rh2" --skip-individual
  python orchestrate.py --compounds Omipalisib "Ginsenoside Rh2" --model mixtral-8x7b
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
_DATA = _DIR / "data"

_WIN_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
}


def _safe_data_dir_name(compound: str) -> str:
    """Same as ``run_review._safe_dir_name`` / ``discover.safe_compound_dir``."""
    safe = re.sub(r"[^\w\-.]+", "_", compound, flags=re.UNICODE).strip("._- ")[:80] or "compound"
    if safe.upper() in _WIN_RESERVED:
        safe = f"_{safe}_"
    return safe


def _safe_review_slug(compound: str) -> str:
    """Same as ``review.py`` / ``evidence-doc`` review path segment."""
    return re.sub(r'[<>:"/\\|?*]', "_", compound).strip()


def _combo_session_slug(compound_names: list[str]) -> str:
    """Same slug as ``review-multiple`` / ``evidence-doc`` combo folder under ``reviews/compounds/``."""
    combo_name = " + ".join(compound_names)
    return re.sub(r'[<>:"/\\|?*]', "_", combo_name).strip().replace(" ", "-")[:80]


def _run(label: str, cmd: list) -> None:
    print(f"\n[{label}]", flush=True)
    result = subprocess.run([str(c) for c in cmd])
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--compounds", nargs="+", required=True, metavar="COMPOUND")
    ap.add_argument("--model", default=None)
    ap.add_argument("--skip-risk", action="store_true")
    ap.add_argument("--skip-discover", action="store_true")
    ap.add_argument("--skip-individual", action="store_true", help="Multi only: skip per-compound pipelines.")
    ap.add_argument("--skip-upload", action="store_true", help="Skip Arweave upload step.")
    args = ap.parse_args()

    py = sys.executable
    compounds = [c.strip() for c in args.compounds if c.strip()]

    def review_flags() -> list:
        f = []
        if args.model:
            f += ["--model", args.model]
        if args.skip_risk:
            f.append("--skip-risk")
        if args.skip_discover:
            f.append("--skip-discover")
        return f

    if len(compounds) == 1:
        _run(
            f"review: {compounds[0]}",
            [py, _DIR / "pipeline" / "single" / "run_review.py", "--compound", compounds[0]] + review_flags(),
        )

        if not args.skip_upload:
            c = compounds[0]
            dd = _safe_data_dir_name(c)
            slug_r = _safe_review_slug(c)
            evidence_p = (_DATA / dd / "evidence_audit.md").resolve()
            review_p = (_DIR.parent / "reviews" / "compounds" / slug_r / f"{slug_r}-review.json").resolve()
            _run(
                f"upload: {c}",
                [py, _DIR / "uploader.py", "--review", str(review_p), "--evidence", str(evidence_p)],
            )
    else:
        session_slug = _combo_session_slug(compounds)
        session_dir = (_DIR.parent / "reviews" / "compounds" / session_slug).resolve()
        individual_root = session_dir / "individual"

        if not args.skip_individual:
            individual_root.mkdir(parents=True, exist_ok=True)
            for c in compounds:
                slug_r = _safe_review_slug(c)
                review_out = individual_root / slug_r / f"{slug_r}-review.json"
                review_out.parent.mkdir(parents=True, exist_ok=True)
                _run(
                    f"review: {c}",
                    [
                        py,
                        _DIR / "pipeline" / "single" / "run_review.py",
                        "--compound",
                        c,
                        "--skip-evidence-audit",
                        "--review-output",
                        str(review_out),
                    ]
                    + review_flags(),
                )

        slug = "-".join(c[:5].lower() for c in compounds)
        bundle = _DATA / f"{slug}-bundle.json"
        int_cmd = [
            py,
            _DIR / "pipeline" / "multi" / "interactions.py",
            "--compounds",
            *compounds,
        ]
        if not args.skip_individual:
            int_cmd += ["--reviews-root", str(individual_root)]
        int_cmd += ["-o", str(bundle)]

        _run("interactions", int_cmd)

        combo_flags = ["--model", args.model] if args.model else []
        _run("review-multiple", [py, _DIR / "pipeline" / "multi" / "review-multiple.py", str(bundle)] + combo_flags)

        evidence_script = _DIR / "pipeline" / "evidence-doc.py"
        if not args.skip_individual:
            for c in compounds:
                slug_r = _safe_review_slug(c)
                dd = _safe_data_dir_name(c)
                compound_dir = (_DATA / dd).resolve()
                review_p = individual_root / slug_r / f"{slug_r}-review.json"
                _run(
                    f"evidence audit: {c}",
                    [
                        py,
                        evidence_script,
                        "-d",
                        str(compound_dir),
                        "--review",
                        str(review_p),
                        "-o",
                        str(compound_dir / "evidence_audit.md"),
                    ],
                )

        _run(
            "evidence audit (combination)",
            [py, evidence_script, "--combination-bundle", str(bundle)],
        )

        if not args.skip_upload:
            _run(
                "upload",
                [py, _DIR / "uploader.py", "--review-dir", str(session_dir)],
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
