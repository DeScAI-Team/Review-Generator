#!/usr/bin/env python3
"""
Sequential Arweave uploader for DAO review outputs.

Uploads dao_evidence_audit.md, then dao_review.json (with evidence link
appended to ``review_statement``), then overview.json (with review link
appended to ``review_statement``).

Usage:
  python uploader.py --synthesis-dir DAOs/molecule/output/CLAW/synthesis
  python uploader.py --synthesis-dir DAOs/molecule/output/CLAW/synthesis --resume
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
_REPO_ROOT = _THIS_DIR.parent.parent
_UPLOAD_CLI = _REPO_ROOT / "articles" / "article_uploader" / "upload_cli.js"
_UPLOAD_CLI_CWD = _UPLOAD_CLI.parent

PLATFORM = "Molecule"
CATEGORY = "ResearchDAO"


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
    dao_name: str | None = None,
    review_date: str | None = None,
) -> list[dict[str, str]]:
    """Build Arweave GraphQL tags for a DAO upload."""
    tags: list[dict[str, str]] = [
        {"name": "doctype", "value": doctype},
        {"name": "DaoName", "value": dao_name or ""},
        {"name": "platform", "value": PLATFORM},
        {"name": "category", "value": CATEGORY},
    ]
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
# Core upload sequence: evidence → review → overview
# ---------------------------------------------------------------------------

def run_upload_sequence(
    synthesis_dir: Path | str,
    resume: bool = False,
) -> dict[str, Any]:
    """Run the full 3-step upload sequence for a DAO synthesis directory.

    Args:
        synthesis_dir: Path containing dao_evidence_audit.md, dao_review.json,
                       and overview.json
        resume: If True, skip already-completed steps using existing metadata
    """
    synthesis_dir = Path(synthesis_dir).resolve()

    evidence_path = synthesis_dir / "dao_evidence_audit.md"
    review_path = synthesis_dir / "dao_review.json"
    overview_path = synthesis_dir / "overview.json"
    metadata_path = synthesis_dir / "upload_metadata.json"

    missing = []
    if not evidence_path.is_file():
        missing.append("dao_evidence_audit.md")
    if not review_path.is_file():
        missing.append("dao_review.json")
    if not overview_path.is_file():
        missing.append("overview.json")

    if missing:
        error_msg = f"Missing required files in {synthesis_dir}: {', '.join(missing)}"
        print(f"\n  Error: {error_msg}", file=sys.stderr)
        return {"success": False, "error": error_msg}

    # Read dao_review.json for tag values
    try:
        with open(review_path, "r", encoding="utf-8") as f:
            review_data = json.load(f)
        dao_name = review_data.get("research_name", "")
        review_date = review_data.get("review_date", "")
    except Exception as e:
        error_msg = f"Failed to read dao_review.json: {e}"
        print(f"\n  Error: {error_msg}", file=sys.stderr)
        return {"success": False, "error": error_msg}

    metadata: dict[str, Any] = {
        "upload_date": datetime.now(timezone.utc).isoformat(),
        "synthesis_dir": str(synthesis_dir),
        "evidence_audit": {},
        "review": {},
        "overview": {},
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
            if existing.get("overview", {}).get("txid"):
                start_step = 3
                metadata["overview"] = existing["overview"]
                print(f"\n  Resuming: overview already uploaded")
        except Exception as e:
            print(f"\n  Warning: Could not load existing metadata: {e}")

    print(f"\n{'='*60}")
    print(f"  DAO Upload Sequence")
    print(f"{'='*60}")
    print(f"  Synthesis dir: {synthesis_dir}")
    print(f"  DAO name:      {dao_name}")
    print(f"  Date:          {review_date}")

    # Step 1 — dao_evidence_audit.md
    if start_step <= 0:
        print(f"\n{'='*60}")
        print(f"  Step 1/3: Upload dao_evidence_audit.md")
        print(f"{'='*60}")

        tags = _build_tags("evidence", dao_name, review_date)
        result = _run_node_upload(evidence_path, tags)

        if not result.get("success"):
            error_msg = result.get("error", "Unknown error")
            print(f"\n  Upload failed: {error_msg}", file=sys.stderr)
            metadata["evidence_audit"] = {"error": error_msg}
            _save_upload_metadata(synthesis_dir, metadata)
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
        _save_upload_metadata(synthesis_dir, metadata)
    else:
        evidence_txid = metadata["evidence_audit"]["txid"]
        evidence_url = metadata["evidence_audit"]["url"]

    # Step 2 — dao_review.json (with evidence link injected)
    if start_step <= 1:
        print(f"\n{'='*60}")
        print(f"  Step 2/3: Upload dao_review.json (with evidence link)")
        print(f"{'='*60}")

        append_text = f" Find evidence audit at arweave.net/{evidence_txid}"
        try:
            modified_review = _create_modified_json_with_link(review_path, append_text)
        except Exception as e:
            error_msg = f"Failed to create modified dao_review.json: {e}"
            print(f"\n  Error: {error_msg}", file=sys.stderr)
            metadata["review"] = {"error": error_msg}
            _save_upload_metadata(synthesis_dir, metadata)
            return {"success": False, "error": error_msg, "metadata": metadata}

        try:
            tags = _build_tags("review", dao_name, review_date)
            result = _run_node_upload(modified_review, tags)

            if not result.get("success"):
                error_msg = result.get("error", "Unknown error")
                print(f"\n  Upload failed: {error_msg}", file=sys.stderr)
                metadata["review"] = {"error": error_msg}
                _save_upload_metadata(synthesis_dir, metadata)
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
            _save_upload_metadata(synthesis_dir, metadata)
        finally:
            if modified_review.exists():
                modified_review.unlink()
    else:
        review_txid = metadata["review"]["txid"]
        review_url = metadata["review"]["url"]

    # Step 3 — overview.json (with review link injected)
    if start_step <= 2:
        print(f"\n{'='*60}")
        print(f"  Step 3/3: Upload overview.json (with review link)")
        print(f"{'='*60}")

        append_text = f" Find full review at descai.net/review/{review_txid}"
        try:
            modified_overview = _create_modified_json_with_link(overview_path, append_text)
        except Exception as e:
            error_msg = f"Failed to create modified overview.json: {e}"
            print(f"\n  Error: {error_msg}", file=sys.stderr)
            metadata["overview"] = {"error": error_msg}
            _save_upload_metadata(synthesis_dir, metadata)
            return {"success": False, "error": error_msg, "metadata": metadata}

        try:
            tags = _build_tags("overview", dao_name, review_date)
            result = _run_node_upload(modified_overview, tags)

            if not result.get("success"):
                error_msg = result.get("error", "Unknown error")
                print(f"\n  Upload failed: {error_msg}", file=sys.stderr)
                metadata["overview"] = {"error": error_msg}
                _save_upload_metadata(synthesis_dir, metadata)
                return {"success": False, "error": error_msg, "metadata": metadata}

            overview_txid = result["txId"]
            overview_url = result["webUrl"]

            metadata["overview"] = {
                "txid": overview_txid,
                "url": overview_url,
                "tags": tags,
            }

            print(f"\n  Overview uploaded!")
            print(f"    TX ID: {overview_txid}")
            print(f"    URL:   {overview_url}")
            _save_upload_metadata(synthesis_dir, metadata)
        finally:
            if modified_overview.exists():
                modified_overview.unlink()

    print(f"\n{'='*60}")
    print(f"  Upload Sequence Complete!")
    print(f"{'='*60}")
    print(f"  Evidence: {metadata['evidence_audit'].get('url', '(skipped)')}")
    print(f"  Review:   {metadata['review'].get('descai_url', '(skipped)')}")
    print(f"  Overview: {metadata['overview'].get('url', '(skipped)')}")

    return {"success": True, "metadata": metadata}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Upload DAO review outputs to Arweave with automatic linking.",
    )
    parser.add_argument(
        "--synthesis-dir",
        type=Path,
        required=True,
        help=(
            "Path to synthesis directory containing dao_evidence_audit.md, "
            "dao_review.json, and overview.json"
        ),
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from a failed upload using existing upload_metadata.json.",
    )
    args = parser.parse_args()

    result = run_upload_sequence(args.synthesis_dir, resume=args.resume)
    return 0 if result.get("success") else 1


if __name__ == "__main__":
    raise SystemExit(main())
