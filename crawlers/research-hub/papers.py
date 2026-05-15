#!/usr/bin/env python3
"""
Fetch in-journal papers (same feed as PaperParser), merge per-paper API data for pdf_url,
and write compact JSON (hub URL, title, abstract, dates, authors + institutions).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import quote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.api_client import ResearchHubAPIClient

FEED_ENDPOINT = "/journal_feed/"
FEED_PARAMS = {"publication_status": "ALL", "journal_status": "IN_JOURNAL"}
SITE_BASE = "https://www.researchhub.com"


def normalize_pdf_url(raw: Optional[str]) -> Optional[str]:
    if not raw or not isinstance(raw, str):
        return None
    parts = urlsplit(raw.strip())
    path = quote(parts.path, safe="/")
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def paper_page_url(paper_id: int, slug: Optional[str]) -> str:
    slug = (slug or "").strip()
    if slug:
        return f"{SITE_BASE}/paper/{paper_id}/{slug}"
    return f"{SITE_BASE}/paper/{paper_id}"


def _add_institution(names: List[str], seen: set, s: Optional[str]) -> None:
    if not s or not isinstance(s, str):
        return
    t = s.strip()
    if not t or t.lower() in seen:
        return
    seen.add(t.lower())
    names.append(t)


def _education_institution_strings(edu: Dict[str, Any]) -> List[str]:
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


def institutions_from_profile(profile: Dict[str, Any]) -> List[str]:
    names: List[str] = []
    seen: set = set()
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
    return names


def build_author_entries(
    api: ResearchHubAPIClient,
    feed_authors: List[Dict[str, Any]],
    fetch_profiles: bool,
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for a in feed_authors or []:
        if not isinstance(a, dict):
            continue
        fn = (a.get("first_name") or "").strip()
        ln = (a.get("last_name") or "").strip()
        name = f"{fn} {ln}".strip()
        if not name:
            continue
        user = a.get("user")
        user_id = user.get("id") if isinstance(user, dict) else None
        author_id = a.get("id")
        inst: List[str] = []
        seen: set = set()
        aff = _headline_affiliation(a.get("headline"))
        if aff:
            _add_institution(inst, seen, aff)
        if fetch_profiles and author_id is not None:
            try:
                profile = api.get(f"/author/{author_id}/")
                if isinstance(profile, dict):
                    for x in institutions_from_profile(profile):
                        _add_institution(inst, seen, x)
            except Exception:
                pass
        out.append(
            {
                "name": name,
                "author_id": author_id,
                "user_id": user_id,
                "institutions": inst,
            }
        )
    return out


def build_record(
    feed_item: Dict[str, Any],
    detail: Dict[str, Any],
    authors: List[Dict[str, Any]],
) -> Dict[str, Any]:
    co = feed_item.get("content_object") or {}
    if not isinstance(co, dict):
        raise ValueError("missing content_object")
    paper_id = int(co["id"])
    slug = detail.get("slug") or co.get("slug")
    pdf_raw = detail.get("pdf_url")
    record: Dict[str, Any] = {
        "paper_id": paper_id,
        "url": paper_page_url(paper_id, slug if isinstance(slug, str) else None),
        "pdf_url": normalize_pdf_url(pdf_raw) if pdf_raw else None,
        "title": detail.get("title") or co.get("title"),
        "abstract": detail.get("abstract") or co.get("abstract"),
        "doi": detail.get("doi") or co.get("doi"),
        "work_type": detail.get("work_type") or co.get("work_type"),
        "dates": {
            "created": detail.get("created_date") or co.get("created_date"),
            "feed_action_date": feed_item.get("action_date"),
            "paper_publish_date": detail.get("paper_publish_date")
            or co.get("paper_publish_date"),
        },
        "authors": authors,
    }
    return record


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


def run(
    output_dir: Path,
    delay: float,
    max_pages: Optional[int],
    fetch_author_profiles: bool,
    crawl_skip_paths: Optional[set[str]] = None,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    api = ResearchHubAPIClient(delay=delay)
    feed = api.get_paginated(FEED_ENDPOINT, params=dict(FEED_PARAMS), max_pages=max_pages)
    print(f"Journal feed items: {len(feed)}")

    errors: List[Dict[str, Any]] = []
    for i, item in enumerate(feed):
        if not isinstance(item, dict):
            continue
        co = item.get("content_object")
        if not isinstance(co, dict):
            continue
        pid = co.get("id")
        if pid is None:
            continue
        try:
            paper_id = int(pid)
        except (TypeError, ValueError):
            continue
        rel_path = f"papers/PaperRecord_{paper_id}.json"
        if crawl_skip_paths and rel_path in crawl_skip_paths:
            print(f"  [{i + 1}] skip (crawl_log): {rel_path}")
            continue
        try:
            detail = api.get(f"/paper/{paper_id}/")
        except Exception as e:
            errors.append({"paper_id": paper_id, "phase": "paper_detail", "error": str(e)})
            print(f"  [{i + 1}] paper {paper_id}: detail fetch failed: {e}")
            continue

        authors = build_author_entries(
            api, co.get("authors") or [], fetch_profiles=fetch_author_profiles
        )
        rec = build_record(item, detail, authors)
        path = output_dir / f"PaperRecord_{paper_id}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2, ensure_ascii=False)
        print(f"  [{i + 1}] wrote {path.name}")

    manifest = {"count": len(list(output_dir.glob("PaperRecord_*.json"))), "errors": errors}
    with open(output_dir / "papers_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Done. Manifest: {output_dir / 'papers_manifest.json'}")


def main() -> None:
    p = argparse.ArgumentParser(description="Journal papers + pdf_url + slim metadata JSON")
    p.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "proposals_temp" / "papers",
        help="Directory for PaperRecord_<id>.json",
    )
    p.add_argument("--delay", type=float, default=0.5, help="API delay (seconds)")
    p.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Max journal_feed pages (None = all)",
    )
    p.add_argument(
        "--no-author-profiles",
        action="store_true",
        help="Skip GET /author/<id>/ (only headline 'at …' from feed)",
    )
    p.add_argument(
        "--crawl-skip-file",
        type=Path,
        default=None,
        help="JSON with researchhubFiles list (from full-crawl); skip those relative paths",
    )
    args = p.parse_args()
    skip_paths = _load_crawl_skip_paths(args.crawl_skip_file)
    run(
        output_dir=args.output_dir.resolve(),
        delay=args.delay,
        max_pages=args.max_pages,
        fetch_author_profiles=not args.no_author_profiles,
        crawl_skip_paths=skip_paths,
    )


if __name__ == "__main__":
    main()
