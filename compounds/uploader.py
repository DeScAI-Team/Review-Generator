#!/usr/bin/env python3
"""
Sequential Arweave uploader for compound review outputs.

Uploads evidence_audit.md first, then the review JSON with the evidence
Arweave link appended to ``review_statement``.

Two modes:
  --review-dir <dir>   Auto-detect combo + individual reviews under a
                       reviews/compounds/<slug>/ directory.
  --review + --evidence Explicit pair of files to upload.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent
_UPLOAD_CLI = _REPO_ROOT / "articles" / "article_uploader" / "upload_cli.js"
_UPLOAD_CLI_CWD = _UPLOAD_CLI.parent

PLATFORM = "PumpScience"
CATEGORY = "compounds"


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _run_node_upload(
    file_path: Path,
    tags: list[dict[str, str]],
) -> dict[str, Any]:
    """Call the Node.js upload CLI and return the parsed JSON result."""
    cmd = ["node", str(_UPLOAD_CLI), str(file_path)]

    if tags:
        cmd.extend(["--tags", json.dumps(tags)])

    print(f"\n  Uploading: {file_path.name}")
    if tags:
        print(f"  Tags: {json.dumps(tags, indent=2)}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(_UPLOAD_CLI_CWD),
        )

        try:
            upload_result = json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": (
                    f"Invalid JSON response. stdout: {result.stdout[:200]}, "
                    f"stderr: {result.stderr[:200]}"
                ),
            }

        return upload_result

    except subprocess.SubprocessError as e:
        return {"success": False, "error": f"Subprocess error: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {e}"}


def _build_tags(
    doctype: str,
    compound_name: str | None = None,
    review_date: str | None = None,
) -> list[dict[str, str]]:
    """Build Arweave GraphQL tags for a compound upload."""
    tags: list[dict[str, str]] = [
        {"name": "doctype", "value": doctype},
        {"name": "platform", "value": PLATFORM},
        {"name": "category", "value": CATEGORY},
    ]
    if compound_name:
        tags.append({"name": "compounds", "value": compound_name})
    if review_date:
        tags.append({"name": "date", "value": review_date})
    return tags


def _create_modified_json_with_link(json_path: Path, append_text: str) -> Path:
    """Return a temp copy of *json_path* with *append_text* added to ``review_statement``."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "review_statement" not in data:
        raise ValueError(f"No 'review_statement' field found in {json_path}")

    data["review_statement"] = data["review_statement"] + append_text

    temp_fd, temp_path = tempfile.mkstemp(suffix=".json", prefix="upload_", text=True)
    try:
        with os.fdopen(temp_fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        os.close(temp_fd)
        raise

    return Path(temp_path)


def _save_upload_metadata(target_dir: Path, metadata: dict[str, Any]) -> None:
    metadata_path = target_dir / "upload_metadata.json"
    target_dir.mkdir(parents=True, exist_ok=True)
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"\n  Saved upload metadata: {metadata_path}")


# ---------------------------------------------------------------------------
# Core upload pair: evidence → review
# ---------------------------------------------------------------------------

def _upload_pair(
    evidence_path: Path,
    review_path: Path,
    metadata_dir: Path,
    *,
    resume: bool = False,
    label: str = "",
) -> dict[str, Any]:
    """Upload an evidence doc then its review, linking the two.

    *metadata_dir* is where ``upload_metadata.json`` is written (usually the
    directory that contains the review JSON).
    """
    metadata_path = metadata_dir / "upload_metadata.json"

    # Read review JSON for tag values
    try:
        with open(review_path, "r", encoding="utf-8") as f:
            review_data = json.load(f)
        compound_name = review_data.get("research_name", "")
        review_date = review_data.get("review_date", "")
    except Exception as e:
        error_msg = f"Failed to read {review_path.name}: {e}"
        print(f"\n  Error: {error_msg}", file=sys.stderr)
        return {"success": False, "error": error_msg}

    metadata: dict[str, Any] = {
        "upload_date": datetime.now(timezone.utc).isoformat(),
        "review_file": str(review_path),
        "evidence_file": str(evidence_path),
        "evidence_audit": {},
        "review": {},
    }

    # Resume logic
    start_step = 0
    if resume and metadata_path.is_file():
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing.get("evidence_audit", {}).get("txid"):
                start_step = 1
                metadata["evidence_audit"] = existing["evidence_audit"]
                print(f"\n  Resuming: evidence_audit already uploaded")
            if existing.get("review", {}).get("txid"):
                start_step = 2
                metadata["review"] = existing["review"]
                print(f"\n  Resuming: review already uploaded")
        except Exception as e:
            print(f"\n  Warning: Could not load existing metadata: {e}")

    prefix = f"[{label}] " if label else ""

    print(f"\n{'='*60}")
    print(f"  {prefix}Compound Upload Sequence")
    print(f"{'='*60}")
    print(f"  Compound:  {compound_name}")
    print(f"  Date:      {review_date}")
    print(f"  Evidence:  {evidence_path}")
    print(f"  Review:    {review_path}")

    # Step 1 — evidence_audit.md
    if start_step <= 0:
        print(f"\n{'='*60}")
        print(f"  {prefix}Step 1/2: Upload evidence_audit.md")
        print(f"{'='*60}")

        tags = _build_tags("evidence", compound_name, review_date)
        result = _run_node_upload(evidence_path, tags)

        if not result.get("success"):
            error_msg = result.get("error", "Unknown error")
            print(f"\n  Upload failed: {error_msg}", file=sys.stderr)
            metadata["evidence_audit"] = {"error": error_msg}
            _save_upload_metadata(metadata_dir, metadata)
            return {"success": False, "error": error_msg, "metadata": metadata}

        evidence_txid = result["txId"]
        evidence_url = result["webUrl"]

        metadata["evidence_audit"] = {
            "txid": evidence_txid,
            "url": evidence_url,
            "tags": tags,
        }

        print(f"\n  Evidence audit uploaded!")
        print(f"    TX ID: {evidence_txid}")
        print(f"    URL:   {evidence_url}")
        _save_upload_metadata(metadata_dir, metadata)
    else:
        evidence_txid = metadata["evidence_audit"]["txid"]
        evidence_url = metadata["evidence_audit"]["url"]

    # Step 2 — review JSON (with evidence link injected)
    if start_step <= 1:
        print(f"\n{'='*60}")
        print(f"  {prefix}Step 2/2: Upload review (with evidence link)")
        print(f"{'='*60}")

        append_text = f" You can find evidence audit at arweave.net/{evidence_txid}"
        try:
            modified_path = _create_modified_json_with_link(review_path, append_text)
        except Exception as e:
            error_msg = f"Failed to create modified review: {e}"
            print(f"\n  Error: {error_msg}", file=sys.stderr)
            metadata["review"] = {"error": error_msg}
            _save_upload_metadata(metadata_dir, metadata)
            return {"success": False, "error": error_msg, "metadata": metadata}

        try:
            tags = _build_tags("review", compound_name, review_date)
            result = _run_node_upload(modified_path, tags)

            if not result.get("success"):
                error_msg = result.get("error", "Unknown error")
                print(f"\n  Upload failed: {error_msg}", file=sys.stderr)
                metadata["review"] = {"error": error_msg}
                _save_upload_metadata(metadata_dir, metadata)
                return {"success": False, "error": error_msg, "metadata": metadata}

            review_txid = result["txId"]
            review_url = result["webUrl"]

            metadata["review"] = {
                "txid": review_txid,
                "url": review_url,
                "descai_url": f"https://descai.net/review/{review_txid}",
                "tags": tags,
            }

            print(f"\n  Review uploaded!")
            print(f"    TX ID:     {review_txid}")
            print(f"    URL:       {review_url}")
            print(f"    DeScAi:    https://descai.net/review/{review_txid}")
            _save_upload_metadata(metadata_dir, metadata)
        finally:
            if modified_path.exists():
                modified_path.unlink()

    print(f"\n{'='*60}")
    print(f"  {prefix}Upload Complete!")
    print(f"{'='*60}")
    print(f"  Evidence: {metadata['evidence_audit'].get('url', '(skipped)')}")
    print(f"  Review:   {metadata['review'].get('descai_url', '(skipped)')}")

    return {"success": True, "metadata": metadata}


# ---------------------------------------------------------------------------
# --review-dir auto-detection
# ---------------------------------------------------------------------------

def _find_combo_review(review_dir: Path) -> Path | None:
    """Return the ``*-combo-review.json`` in *review_dir*, or None."""
    candidates = list(review_dir.glob("*-combo-review.json"))
    return candidates[0] if candidates else None


def _find_individual_pairs(
    review_dir: Path,
) -> list[tuple[Path, Path]]:
    """Return (evidence, review) pairs for each individual compound."""
    individual_dir = review_dir / "individual"
    if not individual_dir.is_dir():
        return []

    pairs: list[tuple[Path, Path]] = []
    for compound_dir in sorted(individual_dir.iterdir()):
        if not compound_dir.is_dir():
            continue
        reviews = list(compound_dir.glob("*-review.json"))
        if not reviews:
            continue
        review_json = reviews[0]
        compound_name = compound_dir.name
        evidence = _REPO_ROOT / "compounds" / "data" / compound_name / "evidence_audit.md"
        if not evidence.is_file():
            print(
                f"\n  Warning: no evidence_audit.md for {compound_name} "
                f"at {evidence}, skipping individual upload.",
                file=sys.stderr,
            )
            continue
        pairs.append((evidence, review_json))
    return pairs


def upload_review_dir(
    review_dir: Path,
    *,
    resume: bool = False,
) -> dict[str, Any]:
    """Auto-detect and upload everything under a review directory."""
    review_dir = Path(review_dir).resolve()
    results: dict[str, Any] = {"success": True, "uploads": []}

    # Individual compounds first
    individual_pairs = _find_individual_pairs(review_dir)
    for evidence_path, review_path in individual_pairs:
        compound_name = review_path.parent.name
        r = _upload_pair(
            evidence_path,
            review_path,
            review_path.parent,
            resume=resume,
            label=compound_name,
        )
        results["uploads"].append({"compound": compound_name, **r})
        if not r["success"]:
            results["success"] = False

    # Combo review
    combo_review = _find_combo_review(review_dir)
    combo_evidence = review_dir / "evidence_audit.md"
    if combo_review and combo_evidence.is_file():
        r = _upload_pair(
            combo_evidence,
            combo_review,
            review_dir,
            resume=resume,
            label="combo",
        )
        results["uploads"].append({"compound": "combo", **r})
        if not r["success"]:
            results["success"] = False
    elif combo_review:
        print(
            f"\n  Warning: combo review found but no evidence_audit.md "
            f"in {review_dir}",
            file=sys.stderr,
        )

    if not results["uploads"]:
        results["success"] = False
        results["error"] = f"No uploadable review/evidence pairs found in {review_dir}"
        print(f"\n  Error: {results['error']}", file=sys.stderr)

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Upload compound review outputs to Arweave with automatic evidence linking.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--review-dir",
        type=Path,
        help=(
            "Directory under reviews/compounds/<slug>/ to auto-detect "
            "combo + individual reviews for upload."
        ),
    )
    group.add_argument(
        "--review",
        type=Path,
        help="Explicit path to a single review JSON file.",
    )
    parser.add_argument(
        "--evidence",
        type=Path,
        help="Explicit path to the evidence_audit.md (required with --review).",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from a failed upload using existing upload_metadata.json.",
    )
    args = parser.parse_args()

    if args.review and not args.evidence:
        parser.error("--evidence is required when using --review")

    if args.review_dir:
        result = upload_review_dir(args.review_dir, resume=args.resume)
    else:
        review_path = args.review.resolve()
        evidence_path = args.evidence.resolve()

        if not review_path.is_file():
            print(f"\n  Error: review file not found: {review_path}", file=sys.stderr)
            return 1
        if not evidence_path.is_file():
            print(f"\n  Error: evidence file not found: {evidence_path}", file=sys.stderr)
            return 1

        result = _upload_pair(
            evidence_path,
            review_path,
            review_path.parent,
            resume=args.resume,
        )

    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
