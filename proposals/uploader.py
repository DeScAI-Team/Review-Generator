#!/usr/bin/env python3
"""
Sequential Arweave uploader for proposal review outputs.

Uploads evidence_audit.md and review.json in sequence,
automatically linking the review to the evidence upload via transaction IDs.

Upload order:
  1. evidence_audit.md  → txid1
  2. review.json        → append "Evidence bundle available at arweave.net/<txid1>"
                          to review_statement → upload → txid2

Tags applied to every upload:
  platform, category, doctype, proposal_name, review_date

Usage:
  python uploader.py --output-dir ../data/4459
  python uploader.py --output-dir ../data/4459 --resume
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

_UPLOADER_DIR = Path(__file__).resolve().parent
_UPLOAD_CLI = _UPLOADER_DIR.parent / "articles" / "article_uploader" / "upload_cli.js"


# ── Node upload helper ─────────────────────────────────────────────────────

def _run_node_upload(
    file_path: Path,
    tags: list[dict[str, str]],
) -> dict[str, Any]:
    """Call the shared Node.js upload CLI and return parsed JSON result."""
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
            cwd=str(_UPLOAD_CLI.parent),
        )
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": f"Invalid JSON response. stdout: {result.stdout[:200]}, stderr: {result.stderr[:200]}",
            }
    except subprocess.SubprocessError as e:
        return {"success": False, "error": f"Subprocess error: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {e}"}


# ── Tag builder ────────────────────────────────────────────────────────────

DEFAULT_PLATFORM = "ResearchHub"
DEFAULT_CATEGORY = "Proposal"


def _build_tags(
    doctype: str,
    proposal_name: str | None = None,
    review_date: str | None = None,
    *,
    platform: str = DEFAULT_PLATFORM,
    category: str = DEFAULT_CATEGORY,
) -> list[dict[str, str]]:
    """Build Arweave GraphQL tags for a proposal upload."""
    tags = [
        {"name": "platform", "value": platform},
        {"name": "category", "value": category},
        {"name": "doctype", "value": doctype},
    ]
    if proposal_name:
        tags.append({"name": "name", "value": proposal_name})
    if review_date:
        tags.append({"name": "date", "value": review_date})
    return tags


# ── JSON mutation helper ───────────────────────────────────────────────────

def _create_modified_json_with_link(
    json_path: Path,
    append_text: str,
) -> Path:
    """Create a temp copy of a JSON file with text appended to review_statement."""
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


# ── Metadata persistence ──────────────────────────────────────────────────

def _save_upload_metadata(output_dir: Path, metadata: dict[str, Any]) -> None:
    metadata_path = output_dir / "upload_metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"\n  ✓ Saved upload metadata: {metadata_path}")


# ── Main upload sequence ──────────────────────────────────────────────────

def run_upload_sequence(
    output_dir: Path | str,
    resume: bool = False,
) -> dict[str, Any]:
    """
    Upload evidence_audit.md → review.json for a proposal,
    chaining Arweave tx IDs between each step.
    """
    output_dir = Path(output_dir).resolve()

    evidence_path = output_dir / "evidence_audit.md"
    review_path = output_dir / "review.json"
    metadata_path = output_dir / "upload_metadata.json"

    missing = [
        name
        for name, p in [
            ("evidence_audit.md", evidence_path),
            ("review.json", review_path),
        ]
        if not p.is_file()
    ]
    if missing:
        msg = f"Missing required files in {output_dir}: {', '.join(missing)}"
        print(f"\n  ✗ Error: {msg}", file=sys.stderr)
        return {"success": False, "error": msg}

    # Read review.json to extract name / date for tags
    try:
        with open(review_path, "r", encoding="utf-8") as f:
            review_data = json.load(f)
        proposal_name = review_data.get("research_name", review_data.get("proposal_name", ""))
        review_date = review_data.get("review_date", "")
    except Exception as e:
        msg = f"Failed to read review.json: {e}"
        print(f"\n  ✗ Error: {msg}", file=sys.stderr)
        return {"success": False, "error": msg}

    metadata: dict[str, Any] = {
        "upload_date": datetime.now(timezone.utc).isoformat(),
        "output_dir": str(output_dir),
        "evidence_audit": {},
        "review": {},
    }

    # ── Resume handling ────────────────────────────────────────────────
    start_step = 0
    if resume and metadata_path.is_file():
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing.get("evidence_audit", {}).get("txid"):
                start_step = 1
                metadata["evidence_audit"] = existing["evidence_audit"]
                print(f"\n  → Resuming: evidence_audit already uploaded")
            if existing.get("review", {}).get("txid"):
                start_step = 2
                metadata["review"] = existing["review"]
                print(f"\n  → Resuming: review already uploaded")
        except Exception as e:
            print(f"\n  ! Warning: Could not load existing metadata: {e}")

    print(f"\n{'='*60}")
    print(f"  Arweave Upload Sequence — Proposal")
    print(f"{'='*60}")
    print(f"  Output directory: {output_dir}")
    print(f"  Proposal: {proposal_name}")
    print(f"  Date: {review_date}")

    # ── Step 1: evidence_audit.md ──────────────────────────────────────
    if start_step <= 0:
        print(f"\n{'='*60}")
        print(f"  Step 1/2: Upload evidence_audit.md")
        print(f"{'='*60}")

        tags = _build_tags("EvidenceAudit", proposal_name, review_date)
        result = _run_node_upload(evidence_path, tags)

        if not result.get("success"):
            err = result.get("error", "Unknown error")
            print(f"\n  ✗ Upload failed: {err}", file=sys.stderr)
            metadata["evidence_audit"] = {"error": err}
            _save_upload_metadata(output_dir, metadata)
            return {"success": False, "error": err, "metadata": metadata}

        evidence_txid = result["txId"]
        evidence_url = result["webUrl"]
        metadata["evidence_audit"] = {
            "txid": evidence_txid,
            "url": evidence_url,
            "tags": tags,
        }

        print(f"\n  ✓ Evidence audit uploaded!")
        print(f"    TX ID: {evidence_txid}")
        print(f"    URL: {evidence_url}")
        _save_upload_metadata(output_dir, metadata)
    else:
        evidence_txid = metadata["evidence_audit"]["txid"]
        evidence_url = metadata["evidence_audit"]["url"]

    # ── Step 2: review.json (with evidence link) ──────────────────────
    if start_step <= 1:
        print(f"\n{'='*60}")
        print(f"  Step 2/2: Upload review.json (with evidence link)")
        print(f"{'='*60}")

        append_text = f" Evidence bundle available at arweave.net/{evidence_txid}"
        try:
            modified_review = _create_modified_json_with_link(review_path, append_text)
        except Exception as e:
            msg = f"Failed to create modified review.json: {e}"
            print(f"\n  ✗ Error: {msg}", file=sys.stderr)
            metadata["review"] = {"error": msg}
            _save_upload_metadata(output_dir, metadata)
            return {"success": False, "error": msg, "metadata": metadata}

        try:
            tags = _build_tags("review", proposal_name, review_date)
            result = _run_node_upload(modified_review, tags)

            if not result.get("success"):
                err = result.get("error", "Unknown error")
                print(f"\n  ✗ Upload failed: {err}", file=sys.stderr)
                metadata["review"] = {"error": err}
                _save_upload_metadata(output_dir, metadata)
                return {"success": False, "error": err, "metadata": metadata}

            review_txid = result["txId"]
            review_url = result["webUrl"]
            metadata["review"] = {
                "txid": review_txid,
                "url": review_url,
                "descai_url": f"https://descai.net/review/{review_txid}",
                "tags": tags,
            }

            print(f"\n  ✓ Review uploaded!")
            print(f"    TX ID: {review_txid}")
            print(f"    URL: {review_url}")
            print(f"    DeScAi: https://descai.net/review/{review_txid}")
            _save_upload_metadata(output_dir, metadata)
        finally:
            if modified_review.exists():
                modified_review.unlink()
    # ── Done ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  Upload Sequence Complete!")
    print(f"{'='*60}")
    print(f"  Evidence: {metadata['evidence_audit']['url']}")
    print(f"  Review:   {metadata['review']['descai_url']}")

    return {"success": True, "metadata": metadata}


# ── CLI ───────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Upload proposal review outputs to Arweave in sequence with automatic linking.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Path to proposal output directory containing evidence_audit.md and review.json",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from a failed upload using existing upload_metadata.json",
    )
    args = parser.parse_args()

    result = run_upload_sequence(args.output_dir, resume=args.resume)
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    sys.exit(main())
