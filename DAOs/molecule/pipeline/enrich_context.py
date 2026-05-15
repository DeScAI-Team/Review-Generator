"""Enrich aggregated review data with structured IPNFT metadata and platform context.

Extracts structured fields from profile.json (funding, TRL, team, tokenomics,
governance, timeline) and selects relevant Molecule documentation slices based
on context_index.json topic triggers.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_funding(ipnft: dict) -> dict[str, Any]:
    """Extract funding information from IPNFT profile."""
    amount_raw = ipnft.get("fundingAmountValue")
    decimals = ipnft.get("fundingAmountDecimals", 0)
    currency = ipnft.get("fundingAmountCurrency", "")

    amount = None
    if amount_raw is not None:
        try:
            amount = int(amount_raw) / (10 ** decimals) if decimals else int(amount_raw)
        except (ValueError, TypeError):
            amount = None

    return {
        "amount": amount,
        "currency": currency,
        "currency_type": ipnft.get("fundingAmountCurrencyType", ""),
    }


def _extract_trl(ipnft: dict) -> dict[str, Any]:
    """Extract Technology Readiness Level data."""
    return {
        "value": ipnft.get("trlValue"),
        "rationale": ipnft.get("trlRationale"),
    }


def _extract_team(ipnft: dict) -> dict[str, Any]:
    """Extract team/research lead information."""
    lead = ipnft.get("researchLead", {}) or {}
    owner = ipnft.get("owner", {}) or {}
    return {
        "research_lead": {
            "name": lead.get("name"),
            "email": lead.get("email"),
        },
        "organization": ipnft.get("organization"),
        "owner_address": owner.get("address"),
    }


def _extract_tokenomics(ipnft: dict) -> dict[str, Any] | None:
    """Extract IPT market data. Returns None if no IPT exists."""
    ipt = ipnft.get("ipt")
    if not ipt:
        return None

    markets = ipt.get("markets", []) or []
    primary_market = markets[0] if markets else {}

    return {
        "symbol": ipt.get("symbol"),
        "holder_count": ipt.get("holderCount"),
        "total_issued": ipt.get("totalIssued"),
        "circulating_supply": ipt.get("circulatingSupply"),
        "markets": [
            {
                "pair": m.get("name"),
                "chain_id": m.get("chainId"),
                "usd_price": m.get("usdPrice"),
                "liquidity_usd": m.get("liquidityUsd"),
                "volume_24h": m.get("tradingVolume24hr"),
                "market_cap_usd": m.get("marketCapUsd"),
                "price_change_24h_pct": m.get("usdPrice24hrPercentageChange"),
            }
            for m in markets
        ],
        "primary_price_usd": primary_market.get("usdPrice"),
        "primary_liquidity_usd": primary_market.get("liquidityUsd"),
        "primary_market_cap_usd": primary_market.get("marketCapUsd"),
    }


def _extract_governance(ipnft: dict) -> dict[str, Any]:
    """Extract governance/legal agreement information."""
    agreements = ipnft.get("agreements", []) or []
    return {
        "agreement_count": len(agreements),
        "agreement_types": [a.get("type", "Unknown") for a in agreements],
        "has_assignment_agreement": any(
            "assignment" in (a.get("type", "")).lower() for a in agreements
        ),
        "has_development_agreement": any(
            "development" in (a.get("type", "")).lower() for a in agreements
        ),
    }


def _extract_timeline(ipnft: dict) -> dict[str, Any]:
    """Extract timeline information."""
    created = ipnft.get("createdAt")
    updated = ipnft.get("updatedAt")
    minted = ipnft.get("mintedAt")

    age_days = None
    if minted:
        try:
            mint_dt = datetime.fromisoformat(minted.replace("Z", "+00:00"))
            age_days = (datetime.now(timezone.utc) - mint_dt).days
        except (ValueError, TypeError):
            pass

    days_since_update = None
    if updated:
        try:
            update_dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            days_since_update = (datetime.now(timezone.utc) - update_dt).days
        except (ValueError, TypeError):
            pass

    return {
        "created_at": created,
        "updated_at": updated,
        "minted_at": minted,
        "age_days": age_days,
        "days_since_update": days_since_update,
    }


def _select_context_slices(
    profile: dict,
    molecule_docs: list[dict],
    context_index: dict,
) -> dict[str, str]:
    """Select relevant documentation slices based on profile fields present."""
    ipnft = profile.get("ipnft", {})
    selected_topics: set[str] = set()

    for topic_key, topic_config in context_index.items():
        triggers = topic_config.get("triggers", [])
        for trigger in triggers:
            if trigger == "always":
                selected_topics.add(topic_key)
                break
            if trigger == "ipt" and ipnft.get("ipt"):
                selected_topics.add(topic_key)
                break
            if trigger == "agreements" and ipnft.get("agreements"):
                selected_topics.add(topic_key)
                break
            if trigger == "dataroom":
                selected_topics.add(topic_key)
                break
            if trigger == "tokenUri" and ipnft.get("tokenUri"):
                selected_topics.add(topic_key)
                break

    needed_titles: set[str] = set()
    for topic_key in selected_topics:
        titles = context_index.get(topic_key, {}).get("doc_titles", [])
        needed_titles.update(titles)

    docs_by_title = {doc["title"]: doc for doc in molecule_docs}

    context_slices: dict[str, str] = {}
    for title in sorted(needed_titles):
        doc = docs_by_title.get(title)
        if doc:
            markdown = doc.get("markdown", "")
            if len(markdown) > 200:
                context_slices[title] = markdown

    return context_slices


def enrich_context(
    ipnft_dir: Path,
    aggregated: dict[str, Any],
    molecule_docs_path: Path,
    context_index_path: Path,
) -> dict[str, Any]:
    """Enrich aggregated review with structured metadata and platform context.

    Returns a merged structure combining:
      - All aggregated review data
      - Structured IPNFT metadata
      - Selected platform documentation context
    """
    profile = _load_json(ipnft_dir / "profile.json") or {}
    ipnft = profile.get("ipnft", {})
    molecule_docs = _load_json(molecule_docs_path) or []
    context_index = _load_json(context_index_path) or {}

    structured_metadata = {
        "ipnft_id": ipnft.get("id"),
        "ipnft_name": ipnft.get("name"),
        "ipnft_symbol": profile.get("symbol") or ipnft.get("initialSymbol"),
        "description": ipnft.get("description"),
        "organization": ipnft.get("organization"),
        "topic": ipnft.get("topic"),
        "chain_id": ipnft.get("chainId"),
        "schema_version": ipnft.get("schemaVersion"),
        "funding": _extract_funding(ipnft),
        "trl": _extract_trl(ipnft),
        "team": _extract_team(ipnft),
        "tokenomics": _extract_tokenomics(ipnft),
        "governance": _extract_governance(ipnft),
        "timeline": _extract_timeline(ipnft),
    }

    context_slices = _select_context_slices(profile, molecule_docs, context_index)

    return {
        **aggregated,
        "structured_metadata": structured_metadata,
        "platform_context": context_slices,
    }


def main() -> None:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Enrich aggregated review with IPNFT metadata")
    parser.add_argument("ipnft_dir", type=Path, help="IPNFT directory (with profile.json)")
    parser.add_argument("aggregated", type=Path, help="Path to aggregated.json")
    parser.add_argument("-o", "--output", type=Path, help="Output path (default: stdout)")
    parser.add_argument("--docs", type=Path, help="Path to molecule_docs.json")
    parser.add_argument("--context-index", type=Path, help="Path to context_index.json")
    args = parser.parse_args()

    pipeline_dir = Path(__file__).resolve().parent
    dao_root = pipeline_dir.parent.parent

    aggregated = json.loads(args.aggregated.read_text(encoding="utf-8"))
    docs_path = args.docs or (dao_root / "molecule_docs.json")
    idx_path = args.context_index or (pipeline_dir / "context_index.json")

    result = enrich_context(
        ipnft_dir=args.ipnft_dir.resolve(),
        aggregated=aggregated,
        molecule_docs_path=docs_path,
        context_index_path=idx_path,
    )

    output_json = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(output_json, encoding="utf-8")
        print(f"Enriched -> {args.output}")
    else:
        print(output_json)


if __name__ == "__main__":
    main()
