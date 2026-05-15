#!/usr/bin/env python3
"""
Crawl ResearchHub funding feed, keep rows with an active fundraise window (end_date in the
future, status OPEN), fetch full post HTML, strip to plain text, and write one JSON file per
proposal plus a small manifest.json (counts, ids, errors).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.api_client import ResearchHubAPIClient

FEED_ENDPOINT = "/funding_feed/"
SITE_BASE = "https://www.researchhub.com"


def _load_crawl_skip_paths(skip_file: Optional[Path]) -> set[str]:
    if skip_file is None:
        return set()
    p = skip_file.expanduser().resolve()
    if not p.is_file():
        return set()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    files = data.get("researchhubFiles")
    if not isinstance(files, list):
        return set()
    return {str(x).replace("\\", "/") for x in files}


def _parse_utc(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def is_active_fundraise(item: Dict[str, Any], now: datetime) -> bool:
    co = item.get("content_object")
    if not isinstance(co, dict):
        return False
    fr = co.get("fundraise")
    if not isinstance(fr, dict):
        return False
    st = fr.get("status")
    if st not in (None, "OPEN"):
        return False
    end = _parse_utc(fr.get("end_date"))
    if end is None or end <= now:
        return False
    return True


def clean_html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def proposal_url(post_id: int, slug: str) -> str:
    slug = (slug or "post").strip() or "post"
    return f"{SITE_BASE}/post/{post_id}/{slug}"


def authors_from_detail(detail: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for a in detail.get("authors") or []:
        if not isinstance(a, dict):
            continue
        fn = (a.get("first_name") or "").strip()
        ln = (a.get("last_name") or "").strip()
        name = f"{fn} {ln}".strip()
        if not name:
            continue
        entry: Dict[str, Any] = {"name": name}
        if a.get("id") is not None:
            entry["author_id"] = a["id"]
        out.append(entry)
    return out


def _add_institution(names: List[str], seen: set, s: Optional[str]) -> None:
    if not s or not isinstance(s, str):
        return
    t = s.strip()
    if not t or t.lower() in seen:
        return
    seen.add(t.lower())
    names.append(t)


def _education_institution_strings(edu: Dict[str, Any]) -> List[str]:
    """School names from one education row (API has flat `name` or nested `university`)."""
    found: List[str] = []
    uni = edu.get("university")
    if isinstance(uni, dict) and uni.get("name"):
        found.append(str(uni["name"]).strip())
    en = edu.get("name")
    if isinstance(en, str) and en.strip():
        t = en.strip()
        if not found or t.lower() != found[0].lower():
            found.append(t)
    summary = edu.get("summary")
    if isinstance(summary, str) and summary.strip():
        parts = [p.strip() for p in summary.split(",") if p.strip()]
        if len(parts) >= 2:
            tail = parts[-1]
            if len(tail) > 3:
                lower_existing = {x.lower() for x in found}
                if tail.lower() not in lower_existing:
                    found.append(tail)
    return [x for x in found if x]


def _headline_affiliation(headline: Any) -> Optional[str]:
    if not isinstance(headline, str):
        return None
    h = headline.strip()
    low = h.lower()
    if " at " not in low:
        return None
    idx = low.rfind(" at ")
    frag = h[idx + 4 :].strip()
    if "|" in frag:
        frag = frag.split("|")[0].strip()
    return frag if len(frag) > 4 else None


def _collect_from_author_profile(profile: Dict[str, Any], names: List[str], seen: set) -> None:
    if not isinstance(profile, dict):
        return
    u = profile.get("university")
    if isinstance(u, dict) and u.get("name"):
        _add_institution(names, seen, u.get("name"))
    for edu in profile.get("education") or []:
        if isinstance(edu, dict):
            for part in _education_institution_strings(edu):
                _add_institution(names, seen, part)
    aff = _headline_affiliation(profile.get("headline"))
    if aff:
        _add_institution(names, seen, aff)


def institutions_from_feed_and_detail(
    feed_item: Dict[str, Any], detail: Dict[str, Any]
) -> List[str]:
    """Team / org affiliations from nonprofit, grants, post authors, and fundraise creator.
    Does not use `contributors.top` (those are funders, not proposal authors)."""
    names: List[str] = []
    seen: set = set()

    np = feed_item.get("nonprofit")
    if isinstance(np, dict):
        _add_institution(names, seen, np.get("name"))

    for g in feed_item.get("associated_grants") or []:
        if isinstance(g, dict) and g.get("organization"):
            _add_institution(names, seen, str(g["organization"]))

    co = feed_item.get("content_object") or {}
    fr = co.get("fundraise")
    if isinstance(fr, dict):
        cb = fr.get("created_by")
        if isinstance(cb, dict):
            prof = cb.get("author_profile")
            if isinstance(prof, dict):
                _collect_from_author_profile(prof, names, seen)

    for a in detail.get("authors") or []:
        if not isinstance(a, dict):
            continue
        u = a.get("university")
        if isinstance(u, dict) and u.get("name"):
            _add_institution(names, seen, u.get("name"))
        for edu in a.get("education") or []:
            if isinstance(edu, dict):
                for part in _education_institution_strings(edu):
                    _add_institution(names, seen, part)
        aff = _headline_affiliation(a.get("headline"))
        if aff:
            _add_institution(names, seen, aff)

    return names


def build_record(
    feed_item: Dict[str, Any], detail: Dict[str, Any], now: datetime
) -> Dict[str, Any]:
    co = feed_item["content_object"]
    fr = co["fundraise"]
    post_id = int(co["id"])
    slug = str(co.get("slug") or "")

    full_md = detail.get("full_markdown")
    if not isinstance(full_md, str):
        full_md = ""
    body_plain = clean_html_to_text(full_md) if full_md.strip() else ""

    ar = fr.get("amount_raised") if isinstance(fr.get("amount_raised"), dict) else {}
    ga = fr.get("goal_amount") if isinstance(fr.get("goal_amount"), dict) else {}
    contrib = fr.get("contributors") if isinstance(fr.get("contributors"), dict) else {}

    dates: Dict[str, Optional[str]] = {
        "post_created": detail.get("created_date") or co.get("created_date"),
        "fundraise_start": fr.get("start_date"),
        "fundraise_end": fr.get("end_date"),
        "action_date": feed_item.get("action_date"),
    }

    amount_raised = ar.get("usd")
    goal_amount = ga.get("usd")

    record: Dict[str, Any] = {
        "id": post_id,
        "title": detail.get("title") or co.get("title"),
        "authors": authors_from_detail(detail),
        "institutions": institutions_from_feed_and_detail(feed_item, detail),
        "amount_raised": amount_raised,
        "goal_amount": goal_amount,
        "contributor_count": contrib.get("total"),
        "dates": dates,
        "type": co.get("type") or detail.get("document_type"),
        "url": proposal_url(post_id, slug),
    }
    record["proposal-body"] = {
        "format": "text/plain",
        "text": body_plain,
    }
    return record


def main() -> None:
    p = argparse.ArgumentParser(
        description="Export active ResearchHub proposals to one JSON file per proposal"
    )
    p.add_argument(
        "--output-dir",
        default="proposal_output",
        help="Directory for proposal_<id>.json files and manifest.json (default: proposal_output)",
    )
    p.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Max funding_feed pages (for testing)",
    )
    p.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Seconds between API calls (default: 0.5)",
    )
    p.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="HTTP timeout seconds (default: 60)",
    )
    p.add_argument(
        "--crawl-skip-file",
        type=Path,
        default=None,
        help="JSON with researchhubFiles list; skip matching proposals/… paths",
    )
    args = p.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    skip_paths = _load_crawl_skip_paths(args.crawl_skip_file)

    now = datetime.now(timezone.utc)
    api = ResearchHubAPIClient(delay=args.delay, timeout=args.timeout)

    print("Fetching funding feed…")
    items = api.get_paginated(FEED_ENDPOINT, max_pages=args.max_pages)
    print(f"Feed rows: {len(items)} (UTC now: {now.isoformat()})")

    active = [it for it in items if isinstance(it, dict) and is_active_fundraise(it, now)]
    print(f"Active fundraise (OPEN + end_date in future): {len(active)}")

    proposal_ids: List[int] = []
    errors = 0

    for i, item in enumerate(active):
        co = item.get("content_object") or {}
        post_id = co.get("id")
        print(f"  [{i + 1}/{len(active)}] post {post_id} …", flush=True)
        try:
            pid = int(post_id)
            rel_path = f"proposals/proposal_{pid}.json"
            if rel_path in skip_paths:
                print(f"    skip (crawl_log): {rel_path}", flush=True)
                continue
            detail = api.get(f"/researchhubpost/{pid}/")
            fm = detail.get("full_markdown")
            if not isinstance(fm, str) or not fm.strip():
                print(f"    skip: no full_markdown")
                errors += 1
                continue
            record = build_record(item, detail, now)
            out_path = out_dir / f"proposal_{record['id']}.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
            proposal_ids.append(int(record["id"]))
            print(f"    wrote {out_path.name}")
        except Exception as e:
            print(f"    error: {e}")
            errors += 1

    manifest = {
        "generated_at": now.isoformat(),
        "count": len(proposal_ids),
        "errors_skipped": errors,
        "proposal_ids": proposal_ids,
    }
    manifest_path = out_dir / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(
        f"Done: {len(proposal_ids)} files in {out_dir} "
        f"({errors} skipped), manifest {manifest_path.name}"
    )


if __name__ == "__main__":
    main()
