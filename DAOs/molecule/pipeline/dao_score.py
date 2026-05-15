"""DAO-specific scoring with custom dimension weights and composite calculation.

Applies dao_mappings.json weights to produce a final composite_score,
handles the token_alignment dimension from structured data, and applies
rubric penalties for dimensions scored by the screener/LLM findings.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _apply_rubric_score(
    findings: list[dict[str, Any]],
    rubric: dict[str, Any],
) -> float:
    """Apply penalty-based rubric scoring from findings."""
    baseline = rubric.get("baseline", 0.7)
    penalties = rubric.get("penalties", {})
    floor = rubric.get("floor", 0.1)

    score = baseline
    for finding in findings:
        severity = finding.get("severity", "info")
        penalty = penalties.get(severity, 0.0)
        score += penalty

    return max(score, floor)


def _score_token_alignment(metadata: dict[str, Any]) -> dict[str, Any]:
    """Score token alignment from structured tokenomics data."""
    tokenomics = metadata.get("tokenomics")
    if not tokenomics:
        return {
            "score": None,
            "rationale": "No IPT token exists for this IPNFT.",
            "score_method": "no_data",
        }

    score = 0.6
    findings = []

    holder_count = tokenomics.get("holder_count", 0) or 0
    if holder_count >= 200:
        score += 0.1
        findings.append({"signal": "healthy_distribution", "detail": f"{holder_count} holders"})
    elif holder_count < 50:
        score -= 0.1
        findings.append({"signal": "concentrated_ownership", "detail": f"Only {holder_count} holders"})

    liquidity = tokenomics.get("primary_liquidity_usd", 0) or 0
    if liquidity >= 50000:
        score += 0.1
        findings.append({"signal": "deep_liquidity", "detail": f"${liquidity:,.0f} liquidity"})
    elif liquidity < 10000:
        score -= 0.1
        findings.append({"signal": "thin_liquidity", "detail": f"${liquidity:,.0f} liquidity"})

    market_cap = tokenomics.get("primary_market_cap_usd", 0) or 0
    if market_cap > 0 and liquidity > 0:
        liq_ratio = liquidity / market_cap
        if liq_ratio >= 0.1:
            score += 0.05
            findings.append({"signal": "good_liq_ratio", "detail": f"{liq_ratio:.1%} of mcap"})
        elif liq_ratio < 0.03:
            score -= 0.05
            findings.append({"signal": "poor_liq_ratio", "detail": f"{liq_ratio:.1%} of mcap"})

    score = max(0.1, min(1.0, score))

    rationale_parts = [f"Token alignment scored at {score:.2f}."]
    for f in findings:
        rationale_parts.append(f"  - {f['signal']}: {f['detail']}")

    return {
        "score": round(score, 4),
        "rationale": " ".join(rationale_parts),
        "score_method": "structured_data",
        "findings": findings,
    }


def _score_governance(metadata: dict[str, Any]) -> dict[str, Any] | None:
    """Score governance from structured agreement data if no doc-based score exists."""
    gov = metadata.get("governance", {})
    if not gov or gov.get("agreement_count", 0) == 0:
        return None

    score = 0.5
    findings = []

    if gov.get("has_assignment_agreement"):
        score += 0.15
        findings.append({"signal": "assignment_agreement", "severity": "positive"})

    if gov.get("has_development_agreement"):
        score += 0.1
        findings.append({"signal": "development_agreement", "severity": "positive"})

    agreement_count = gov.get("agreement_count", 0)
    if agreement_count >= 2:
        score += 0.05
        findings.append({"signal": "multiple_agreements", "detail": f"{agreement_count} agreements"})

    score = max(0.1, min(1.0, score))

    return {
        "score": round(score, 4),
        "rationale": f"Governance scored from {agreement_count} on-chain agreement(s).",
        "score_method": "structured_data",
        "findings": findings,
    }


def _score_execution_timeline(metadata: dict[str, Any]) -> dict[str, Any] | None:
    """Provide a timeline-based modifier for execution credibility."""
    timeline = metadata.get("timeline", {})
    days_since_update = timeline.get("days_since_update")

    if days_since_update is None:
        return None

    findings = []
    modifier = 0.0

    if days_since_update <= 30:
        modifier = 0.05
        findings.append({"signal": "recently_updated", "detail": f"{days_since_update} days ago"})
    elif days_since_update <= 90:
        modifier = 0.0
        findings.append({"signal": "moderate_update_gap", "detail": f"{days_since_update} days ago"})
    elif days_since_update <= 180:
        modifier = -0.05
        findings.append({"signal": "stale_updates", "detail": f"{days_since_update} days since update"})
    else:
        modifier = -0.1
        findings.append({"signal": "inactive_project", "detail": f"{days_since_update} days since update"})

    return {
        "modifier": modifier,
        "findings": findings,
    }


def _extract_llm_scores(categories: dict[str, Any]) -> dict[str, float]:
    """Extract LLM-generated dimension scores from synthesis_rationale.

    Priority order:
      1. Pre-extracted `llm_dimension_scores` field (written by dao_review.py)
      2. Full JSON parse of the rationale text
      3. Per-dimension regex extraction (handles truncated LLM output)
    """
    import re

    synthesis = categories.get("synthesis_rationale", {})

    pre_extracted = synthesis.get("llm_dimension_scores")
    if pre_extracted and isinstance(pre_extracted, dict):
        return {k: float(v) for k, v in pre_extracted.items() if _is_valid_score(v)}

    rationale_text = synthesis.get("rationale", "")
    if not rationale_text:
        return {}

    # Try full JSON parse
    try:
        parsed = json.loads(rationale_text)
        llm_scores: dict[str, float] = {}
        cats = parsed.get("categories", parsed)
        for dim_key, dim_data in cats.items():
            if isinstance(dim_data, dict) and "score" in dim_data:
                if _is_valid_score(dim_data["score"]):
                    llm_scores[dim_key] = float(dim_data["score"])
        if llm_scores:
            return llm_scores
    except json.JSONDecodeError:
        pass

    # Fallback: regex extraction of "dimension": { "score": X.XX patterns
    # Works even when the LLM output is truncated mid-JSON
    pattern = r'"(\w+)":\s*\{\s*"score":\s*([\d.]+)'
    matches = re.findall(pattern, rationale_text)
    return {k: float(v) for k, v in matches if _is_valid_score(v)}


def _is_valid_score(val: Any) -> bool:
    try:
        f = float(val)
        return 0.0 <= f <= 1.0
    except (ValueError, TypeError):
        return False


def _compute_blend_confidence(
    total_claims: int,
    min_claims: int = 10,
    llm_floor: float = 0.2,
    llm_ceiling: float = 0.8,
) -> tuple[float, float]:
    """Compute doc_confidence and llm_confidence based on claim density.

    With few claims, defer more to LLM. With many claims, trust the pipeline.
    Returns (doc_confidence, llm_confidence) that sum to 1.0.
    """
    if total_claims <= 0:
        return (1.0 - llm_ceiling, llm_ceiling)

    doc_confidence = min(1.0, total_claims / min_claims)
    doc_confidence = max(1.0 - llm_ceiling, min(1.0 - llm_floor, doc_confidence))
    llm_confidence = 1.0 - doc_confidence
    return (doc_confidence, llm_confidence)


def _clean_rationale(text: str) -> str:
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


def run_dao_score(
    dao_review: dict[str, Any],
    mappings_path: Path,
) -> dict[str, Any]:
    """Compute final DAO-level scores with custom dimension weights.

    Applies LLM-vs-pipeline confidence blending: dimensions with many claims
    trust the pipeline scores; dimensions with few claims blend toward the
    LLM synthesis assessment.

    Returns a complete dao_review.json structure with composite_score.
    """
    mappings = _load_json(mappings_path)
    dimension_weights = mappings.get("dimension_weights", {})
    rubrics = mappings.get("rubrics", {})
    blend_config = mappings.get("llm_blend", {})
    min_claims = blend_config.get("min_claims_for_full_doc_confidence", 10)
    llm_floor = blend_config.get("llm_floor", 0.2)
    llm_ceiling = blend_config.get("llm_ceiling", 0.8)

    categories = dao_review.get("categories", {})
    metadata = dao_review.get("structured_metadata", {})

    llm_scores = _extract_llm_scores(categories)

    scored_categories: dict[str, Any] = {}

    for dim_key, dim_data in categories.items():
        if not isinstance(dim_data, dict):
            continue
        if dim_key in ("cross_doc_consistency", "synthesis_rationale", "cross_cutting"):
            scored_categories[dim_key] = dim_data
            continue

        score = dim_data.get("score")
        if score is not None:
            scored_categories[dim_key] = {**dim_data, "score": round(float(score), 4)}
        elif dim_data.get("findings") and dim_key in rubrics:
            rubric = rubrics[dim_key]
            computed_score = _apply_rubric_score(dim_data["findings"], rubric)
            scored_categories[dim_key] = {
                **dim_data,
                "score": round(computed_score, 4),
                "score_method": "rubric_penalty",
            }
        elif dim_data.get("rationale"):
            scored_categories[dim_key] = {**dim_data, "score": 0.5}

    # Blend pipeline scores with LLM synthesis scores based on claim confidence
    for dim_key in list(scored_categories.keys()):
        if dim_key in ("cross_doc_consistency", "synthesis_rationale", "cross_cutting"):
            continue
        dim_data = scored_categories[dim_key]
        pipeline_score = dim_data.get("score")
        llm_score = llm_scores.get(dim_key)

        if pipeline_score is not None and llm_score is not None:
            total_claims = dim_data.get("total_claims", dim_data.get("claim_count", 0))
            doc_conf, llm_conf = _compute_blend_confidence(
                total_claims, min_claims, llm_floor, llm_ceiling,
            )
            blended = (pipeline_score * doc_conf) + (llm_score * llm_conf)
            dim_data["score"] = round(blended, 4)
            dim_data["blend_detail"] = {
                "pipeline_score": round(pipeline_score, 4),
                "llm_score": round(llm_score, 4),
                "doc_confidence": round(doc_conf, 3),
                "llm_confidence": round(llm_conf, 3),
                "total_claims": total_claims,
            }
        elif pipeline_score is None and llm_score is not None:
            dim_data["score"] = round(llm_score, 4)
            dim_data["score_method"] = "llm_only"

    token_score = _score_token_alignment(metadata)
    if token_score.get("score") is not None:
        if "token_alignment" in scored_categories and scored_categories["token_alignment"].get("score"):
            existing = scored_categories["token_alignment"]
            blended = (existing["score"] + token_score["score"]) / 2
            existing["score"] = round(blended, 4)
            existing["structured_findings"] = token_score.get("findings", [])
        else:
            scored_categories["token_alignment"] = token_score

    gov_score = _score_governance(metadata)
    if gov_score and "governance_accountability" not in scored_categories:
        scored_categories["governance_accountability"] = gov_score
    elif gov_score and "governance_accountability" in scored_categories:
        existing = scored_categories["governance_accountability"]
        if existing.get("score") is None:
            existing["score"] = gov_score["score"]
            existing["score_method"] = "structured_data"

    timeline_mod = _score_execution_timeline(metadata)
    if timeline_mod and "execution_credibility" in scored_categories:
        existing = scored_categories["execution_credibility"]
        if existing.get("score") is not None:
            modified = existing["score"] + timeline_mod["modifier"]
            existing["score"] = round(max(0.1, min(1.0, modified)), 4)
            existing.setdefault("timeline_findings", []).extend(timeline_mod["findings"])

    present_weights: dict[str, float] = {}
    for dim_key, weight in dimension_weights.items():
        if dim_key in scored_categories and scored_categories[dim_key].get("score") is not None:
            present_weights[dim_key] = weight

    composite_score = 0.0
    if present_weights:
        total_weight = sum(present_weights.values())
        for dim_key, weight in present_weights.items():
            normalized_weight = weight / total_weight
            dim_score = scored_categories[dim_key]["score"]
            composite_score += dim_score * normalized_weight
        composite_score = round(composite_score, 4)

    per_doc_reviews = dao_review.get("per_document_reviews", [])
    doc_summaries = [
        {
            "filename": d.get("filename", ""),
            "article_type": d.get("article_type", "unknown"),
            "composite_score": d.get("composite_score", 0.0),
        }
        for d in per_doc_reviews
    ]

    # --- Build clean categories: only score + rationale ---
    _NARRATIVE_KEYS = ("cross_doc_consistency", "synthesis_rationale", "cross_cutting")

    clean_categories: dict[str, Any] = {}
    for dim_key, dim_data in scored_categories.items():
        if dim_key in _NARRATIVE_KEYS:
            continue
        if not isinstance(dim_data, dict) or dim_data.get("score") is None:
            continue

        clean_categories[dim_key] = {
            "score": dim_data["score"],
            "rationale": _clean_rationale(dim_data.get("rationale", "")),
        }

    # --- Scale scores from 0-1 to 0-100 ---
    composite_score = round(composite_score * 100, 2)
    for dim_data in clean_categories.values():
        dim_data["score"] = round(dim_data["score"] * 100, 2)

    # --- Human-readable date ---
    _now = datetime.now(timezone.utc)
    review_date = f"{_now.strftime('%B')} {_now.day:02d}, {_now.year}"

    ipnft_name = metadata.get("ipnft_name", "")
    ipnft_symbol = metadata.get("ipnft_symbol", "")

    return {
        "research_name": ipnft_name or ipnft_symbol,
        "review_date": review_date,
        "composite_score": composite_score,
        "review_statement": dao_review.get("review_statement", ""),
        "categories": clean_categories,
        "dao_metadata": {
            "ipnft_symbol": ipnft_symbol,
            "ipnft_name": ipnft_name,
            "organization": metadata.get("organization", ""),
            "trl": metadata.get("trl", {}).get("value"),
            "funding_amount": metadata.get("funding", {}).get("amount"),
            "funding_currency": metadata.get("funding", {}).get("currency"),
            "holder_count": (
                metadata.get("tokenomics", {}).get("holder_count")
                if metadata.get("tokenomics") else None
            ),
            "market_cap_usd": (
                metadata.get("tokenomics", {}).get("primary_market_cap_usd")
                if metadata.get("tokenomics") else None
            ),
            "documents_processed": len(per_doc_reviews),
            "dimensions_scored": len(present_weights),
            "dimension_weights_used": present_weights,
            "llm_blend_config": blend_config if blend_config else None,
            "llm_dimensions_blended": [
                k for k, v in scored_categories.items()
                if isinstance(v, dict) and "blend_detail" in v
            ],
            "per_document_reviews": doc_summaries,
            "full_categories": scored_categories,
        },
    }


def main() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="DAO scoring with custom dimension weights")
    parser.add_argument("review", type=Path, help="Path to dao_review_raw.json")
    parser.add_argument("-o", "--output", type=Path, help="Output path")
    parser.add_argument("--mappings", type=Path, help="Path to dao_mappings.json")
    args = parser.parse_args()

    mappings_path = args.mappings or Path(__file__).resolve().parent / "dao_mappings.json"
    dao_review = json.loads(args.review.read_text(encoding="utf-8"))

    result = run_dao_score(dao_review=dao_review, mappings_path=mappings_path)

    output_json = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(output_json, encoding="utf-8")
        print(f"Scored -> {args.output} (composite: {result['composite_score']})")
    else:
        print(output_json)


if __name__ == "__main__":
    main()
