"""Aggregate per-document review.json files into a unified DAO-level review.

Merges claims, scores, and rationales across multiple article pipeline runs,
preserving provenance (which PDF contributed each dimension score).

Supports type-aware weighting: each document's article_type (empirical, protocol,
theoretical_narrative) determines how much weight its dimension scores carry in
the final aggregate via type_dimension_weights from dao_mappings.json.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _doc_name_from_path(review_path: Path) -> str:
    """Derive a human-readable doc identifier from the review.json path."""
    run_dir = review_path.parent.parent
    return run_dir.name


def _detect_article_type(review_path: Path) -> str:
    """Find the article_type for a review by searching nearby directories."""
    run_dir = review_path.parent.parent
    steps_dir = run_dir / "steps"

    for search_dir in [run_dir, steps_dir, run_dir.parent]:
        at_path = search_dir / "article_type.json"
        if at_path.exists():
            data = _load_json(at_path)
            if data and isinstance(data, dict):
                return data.get("article_type", "empirical")

    docs_parent = run_dir.parent
    for sibling in docs_parent.iterdir():
        if sibling.is_dir():
            at_path = sibling / "article_type.json"
            if at_path.exists():
                doc_name = _doc_name_from_path(review_path).lower().replace(" ", "").replace("-", "")
                sibling_name = sibling.name.lower().replace(" ", "").replace("-", "")
                if doc_name.startswith(sibling_name[:10]) or sibling_name.startswith(doc_name[:10]):
                    data = _load_json(at_path)
                    if data and isinstance(data, dict):
                        return data.get("article_type", "empirical")

    return "empirical"


def _weighted_mean(scores: list[tuple[float, float]]) -> float:
    """Compute weighted mean from (score, weight) pairs."""
    total_weight = sum(w for _, w in scores)
    if total_weight == 0:
        return 0.0
    return sum(s * w for s, w in scores) / total_weight


def aggregate_reviews(
    review_paths: list[Path],
    type_dimension_weights: dict[str, dict[str, float]] | None = None,
) -> dict[str, Any]:
    """Merge multiple review.json files into an aggregated structure.

    Args:
        review_paths: Paths to per-document review.json files.
        type_dimension_weights: Optional per-type weight maps from dao_mappings.json.
            When provided, each document's contribution to a dimension is weighted
            by how important that dimension is for its article type.

    Returns a dict with:
      - per_document_reviews: list of per-doc summaries with article_type
      - categories: merged dimension data with provenance and type-aware weights
      - aggregated_scores: per-dimension weighted-mean scores
    """
    if not review_paths:
        return {
            "per_document_reviews": [],
            "categories": {},
            "aggregated_scores": {},
        }

    per_doc_reviews: list[dict[str, Any]] = []
    dimension_contributions: dict[str, list[dict[str, Any]]] = {}

    for review_path in review_paths:
        try:
            review = json.loads(review_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, FileNotFoundError) as exc:
            print(f"  [aggregate] Skipping unreadable review: {review_path} ({exc})")
            continue

        doc_name = _doc_name_from_path(review_path)
        article_type = _detect_article_type(review_path)
        categories = review.get("categories", {})
        composite = review.get("composite_score", 0.0)

        per_doc_reviews.append({
            "filename": doc_name,
            "research_name": review.get("research_name", doc_name),
            "article_type": article_type,
            "composite_score": composite,
            "review_date": review.get("review_date", ""),
            "dimensions_scored": list(categories.keys()),
            "review_path": str(review_path),
        })

        type_weights = {}
        if type_dimension_weights and article_type in type_dimension_weights:
            type_weights = type_dimension_weights[article_type]

        for dim_key, dim_data in categories.items():
            if not isinstance(dim_data, dict):
                continue
            score = dim_data.get("score")
            if score is None:
                continue

            if dim_key not in dimension_contributions:
                dimension_contributions[dim_key] = []

            dimension_contributions[dim_key].append({
                "source_doc": doc_name,
                "article_type": article_type,
                "score": score,
                "score_method": dim_data.get("score_method", "unknown"),
                "rationale": dim_data.get("rationale", ""),
                "claim_count": dim_data.get("claim_count", 0),
                "finding_count": dim_data.get("finding_count", 0),
                "type_weight_for_dim": type_weights.get(dim_key, 0.1),
            })

    aggregated_scores: dict[str, dict[str, Any]] = {}
    for dim_key, contributions in dimension_contributions.items():
        weights = []
        for c in contributions:
            claim_weight = max(c.get("claim_count", 0), c.get("finding_count", 0), 1)
            type_multiplier = c.get("type_weight_for_dim", 0.1)
            combined_weight = claim_weight * type_multiplier
            weights.append((c["score"], combined_weight))

        mean_score = _weighted_mean(weights)
        best_rationale = max(contributions, key=lambda c: len(c.get("rationale", "")))

        aggregated_scores[dim_key] = {
            "score": round(mean_score, 4),
            "score_method": "type_aware_weighted_mean",
            "source_count": len(contributions),
            "total_claims": sum(c.get("claim_count", 0) for c in contributions),
            "rationale": best_rationale.get("rationale", ""),
            "sources": [
                {
                    "doc": c["source_doc"],
                    "score": c["score"],
                    "method": c["score_method"],
                    "article_type": c["article_type"],
                    "type_weight": c["type_weight_for_dim"],
                }
                for c in contributions
            ],
        }

    return {
        "per_document_reviews": per_doc_reviews,
        "categories": aggregated_scores,
        "aggregated_scores": {k: v["score"] for k, v in aggregated_scores.items()},
    }


def main() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Aggregate article pipeline reviews")
    parser.add_argument("docs_dir", type=Path, help="Directory containing per-doc pipeline outputs")
    parser.add_argument("-o", "--output", type=Path, help="Output path (default: stdout)")
    parser.add_argument("--mappings", type=Path, help="Path to dao_mappings.json for type weights")
    args = parser.parse_args()

    docs_dir = args.docs_dir.resolve()
    review_paths = sorted(docs_dir.rglob("output/review.json"))

    if not review_paths:
        print(f"No review.json found under {docs_dir}", file=sys.stderr)
        sys.exit(1)

    type_dimension_weights = None
    mappings_path = args.mappings or Path(__file__).resolve().parent / "dao_mappings.json"
    if mappings_path.exists():
        mappings = json.loads(mappings_path.read_text(encoding="utf-8"))
        type_dimension_weights = mappings.get("type_dimension_weights")

    result = aggregate_reviews(review_paths, type_dimension_weights=type_dimension_weights)

    output_json = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(output_json, encoding="utf-8")
        print(f"Aggregated {len(review_paths)} reviews -> {args.output}")
    else:
        print(output_json)


if __name__ == "__main__":
    main()
