"""Generate a project health report as a markdown evidence audit document.

Produces dao_evidence_audit.md from the scored DAO review, including:
  - Project identity and metadata summary
  - Composite score and dimension breakdown
  - Per-document review provenance
  - Tokenomics and governance status
  - Timeline and activity indicators
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GENERATOR_VERSION = "1.0.0"


def _score_bar(score: float | None, width: int = 20) -> str:
    """Render a simple ASCII score bar."""
    if score is None:
        return "[" + "?" * width + "]"
    filled = int(score * width)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {score:.2f}"


def _severity_icon(score: float | None) -> str:
    if score is None:
        return "?"
    if score >= 0.7:
        return "STRONG"
    if score >= 0.5:
        return "MODERATE"
    if score >= 0.3:
        return "WEAK"
    return "CRITICAL"


def generate_evidence_doc(
    scored_review: dict[str, Any],
    output_path: Path,
) -> None:
    """Generate the DAO evidence audit markdown document.

    Reads DAO-specific identity and rich category data from ``dao_metadata``
    while using top-level ``research_name`` / ``review_date`` / ``composite_score``.
    """
    lines: list[str] = []

    dao_meta = scored_review.get("dao_metadata", {})
    full_categories = dao_meta.get("full_categories", scored_review.get("categories", {}))

    symbol = dao_meta.get("ipnft_symbol", "Unknown")
    name = scored_review.get("research_name", dao_meta.get("ipnft_name", "Unknown"))
    org = dao_meta.get("organization", "Unknown")
    composite = scored_review.get("composite_score", 0.0)
    review_date = scored_review.get("review_date", datetime.now(timezone.utc).isoformat())
    per_doc = dao_meta.get("per_document_reviews", [])

    lines.append(f"# DAO Project Health Report: {symbol}")
    lines.append("")
    lines.append(f"**Project:** {name}")
    lines.append(f"**Organization:** {org}")
    lines.append(f"**Review Date:** {review_date}")
    lines.append(f"**Generator Version:** {GENERATOR_VERSION}")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Composite Score")
    lines.append("")
    lines.append(f"**{composite:.4f}** / 1.0 — {_severity_icon(composite)}")
    lines.append("")
    lines.append("```")
    lines.append(f"  {_score_bar(composite, 40)}")
    lines.append("```")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Dimension Scores")
    lines.append("")
    lines.append("| Dimension | Score | Assessment | Method | Sources |")
    lines.append("|-----------|-------|------------|--------|---------|")

    scored_dims = {k: v for k, v in full_categories.items()
                   if isinstance(v, dict) and v.get("score") is not None
                   and k not in ("cross_doc_consistency", "synthesis_rationale")}

    for dim_key in sorted(scored_dims.keys()):
        dim_data = scored_dims[dim_key]
        score = dim_data.get("score", 0)
        method = dim_data.get("score_method", "unknown")
        source_count = dim_data.get("source_count", "")
        sources_str = str(source_count) if source_count else "1"
        assessment = _severity_icon(score)
        display_name = dim_key.replace("_", " ").title()
        lines.append(f"| {display_name} | {score:.4f} | {assessment} | {method} | {sources_str} |")

    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Dimension Details")
    lines.append("")

    for dim_key in sorted(scored_dims.keys()):
        dim_data = scored_dims[dim_key]
        display_name = dim_key.replace("_", " ").title()
        lines.append(f"### {display_name}")
        lines.append("")
        lines.append(f"**Score:** {dim_data.get('score', 'N/A'):.4f} ({_severity_icon(dim_data.get('score'))})")
        lines.append(f"**Method:** {dim_data.get('score_method', 'unknown')}")
        lines.append("")

        rationale = dim_data.get("rationale", "")
        if rationale:
            lines.append(f"**Rationale:** {rationale[:500]}")
            lines.append("")

        dao_rationale = dim_data.get("dao_rationale", "")
        if dao_rationale:
            lines.append(f"**DAO-Level Assessment:** {dao_rationale[:500]}")
            lines.append("")

        findings = dim_data.get("findings", []) or dim_data.get("dao_findings", [])
        if findings:
            lines.append("**Findings:**")
            for f in findings[:10]:
                if isinstance(f, dict):
                    signal = f.get("signal", f.get("severity", ""))
                    detail = f.get("detail", f.get("description", ""))
                    lines.append(f"  - {signal}: {detail}")
                else:
                    lines.append(f"  - {f}")
            lines.append("")

        sources = dim_data.get("sources", [])
        if sources:
            lines.append("**Source Documents:**")
            for s in sources[:5]:
                lines.append(f"  - {s.get('doc', 'unknown')}: {s.get('score', 'N/A'):.4f} ({s.get('method', '')})")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Project Metadata")
    lines.append("")

    if dao_meta.get("trl"):
        lines.append(f"**TRL:** {dao_meta['trl']}")
    if dao_meta.get("funding_amount"):
        lines.append(f"**Funding:** {dao_meta['funding_amount']:,.2f} {dao_meta.get('funding_currency', '')}")
    if dao_meta.get("holder_count"):
        lines.append(f"**Token Holders:** {dao_meta['holder_count']}")
    if dao_meta.get("market_cap_usd"):
        lines.append(f"**Market Cap:** ${dao_meta['market_cap_usd']:,.2f}")
    lines.append(f"**Documents Processed:** {dao_meta.get('documents_processed', 0)}")
    lines.append(f"**Dimensions Scored:** {dao_meta.get('dimensions_scored', 0)}")
    lines.append("")

    if dao_meta.get("dimension_weights_used"):
        lines.append("**Dimension Weights Applied:**")
        for dim, weight in sorted(dao_meta["dimension_weights_used"].items()):
            lines.append(f"  - {dim.replace('_', ' ').title()}: {weight:.2f}")
        lines.append("")

    if per_doc:
        lines.append("---")
        lines.append("")
        lines.append("## Per-Document Reviews")
        lines.append("")
        lines.append("| Document | Type | Score |")
        lines.append("|----------|------|-------|")
        for doc in per_doc:
            fname = doc.get("filename", "unknown")
            atype = doc.get("article_type", "unknown")
            dscore = doc.get("composite_score", 0.0)
            lines.append(f"| {fname} | {atype} | {dscore:.4f} |")
        lines.append("")

    consistency = full_categories.get("cross_doc_consistency", {})
    if consistency.get("rationale"):
        lines.append("---")
        lines.append("")
        lines.append("## Cross-Document Consistency")
        lines.append("")
        lines.append(consistency["rationale"][:1000])
        lines.append("")

    review_statement = scored_review.get("review_statement", "")
    if review_statement:
        lines.append("---")
        lines.append("")
        lines.append("## Review Statement")
        lines.append("")
        lines.append(review_statement[:2000])
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by DAO Review Pipeline v{GENERATOR_VERSION}*")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def _clean_overview_rationale(text: str) -> str:
    """Extract plain-text rationale from potentially JSON-wrapped LLM output."""
    import re

    if not text or not text.lstrip().startswith("{"):
        return text
    try:
        parsed = json.loads(text)
        return parsed.get("rationale", text)
    except json.JSONDecodeError:
        m = re.search(r'"rationale":\s*"((?:[^"\\]|\\.)*)"', text)
        if m:
            return m.group(1).replace('\\"', '"').replace("\\n", "\n")
        return text


def generate_overview(
    scored_review: dict[str, Any],
    output_path: Path,
) -> None:
    """Generate a frontend-compatible overview.json matching the article pipeline format.

    Structure: { research_name, review_date, composite_score, review_statement,
                 categories: { dim: { score, score_method, claim_count, rationale } } }

    Expects *scored_review* in article-shaped format (research_name at top level,
    categories already cleaned by dao_score).
    """
    categories = scored_review.get("categories", {})
    dao_meta = scored_review.get("dao_metadata", {})

    overview_categories: dict[str, Any] = {}
    for dim_key, dim_data in categories.items():
        if not isinstance(dim_data, dict) or dim_data.get("score") is None:
            continue

        overview_categories[dim_key] = {
            "score": round(float(dim_data["score"]), 4),
            "rationale": _clean_overview_rationale(dim_data.get("rationale", "")),
        }

    review_statement = scored_review.get("review_statement", "")
    if not review_statement:
        full_cats = dao_meta.get("full_categories", {})
        consistency = full_cats.get("cross_doc_consistency", {})
        review_statement = consistency.get("rationale", "")

    overview = {
        "research_name": scored_review.get("research_name", ""),
        "review_date": scored_review.get("review_date", ""),
        "composite_score": scored_review.get("composite_score", 0.0),
        "review_statement": review_statement,
        "categories": overview_categories,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(overview, indent=2), encoding="utf-8")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate DAO evidence audit document")
    parser.add_argument("review", type=Path, help="Path to scored dao_review.json")
    parser.add_argument("-o", "--output", type=Path, help="Output markdown path")
    args = parser.parse_args()

    review = json.loads(args.review.read_text(encoding="utf-8"))
    output_path = args.output or args.review.parent / "dao_evidence_audit.md"

    generate_evidence_doc(scored_review=review, output_path=output_path)
    generate_overview(scored_review=review, output_path=output_path.parent / "overview.json")
    print(f"Evidence audit -> {output_path}")
    print(f"Overview -> {output_path.parent / 'overview.json'}")


if __name__ == "__main__":
    main()
