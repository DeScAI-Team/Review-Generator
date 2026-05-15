"""DAO-level LLM review with platform context and cross-document synthesis.

Takes enriched data (aggregated per-doc scores + structured metadata + platform
context slices) and produces DAO-specific dimension evaluations via LLM calls.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI

VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
VLLM_API_KEY = os.environ.get("VLLM_API_KEY", "none")
MAX_RETRIES = 4
MAX_TOKENS = 4096


def _llm_call(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_content: str,
    max_tokens: int = MAX_TOKENS,
) -> str:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                temperature=0,
                extra_body={"chat_template_kwargs": {"enable_thinking": False}},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
            )
            raw = response.choices[0].message.content
            if raw is None:
                raise ValueError("LLM returned None content")
            text = raw.strip()
            text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
            text = re.sub(r"<think>.*", "", text, flags=re.DOTALL).strip()

            finish_reason = response.choices[0].finish_reason
            if finish_reason == "length" or (text and text[-1] not in ".!?"):
                last_period = max(text.rfind("."), text.rfind("!"), text.rfind("?"))
                if last_period > 0:
                    text = text[: last_period + 1].strip()

            return text
        except Exception as exc:
            err_str = str(exc).lower()
            if "context length" in err_str or "maximum context" in err_str:
                raise
            print(f"  [attempt {attempt}/{MAX_RETRIES}] LLM error: {exc}")
            if attempt == MAX_RETRIES:
                raise
    return ""


def _load_prompt(prompts_dir: Path, filename: str) -> str:
    path = prompts_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {path}")
    return path.read_text(encoding="utf-8")


def _format_metadata_block(metadata: dict[str, Any]) -> str:
    """Format structured metadata into a readable text block for prompts."""
    lines = []

    lines.append(f"## Project: {metadata.get('ipnft_name', 'Unknown')}")
    lines.append(f"Symbol: {metadata.get('ipnft_symbol', 'N/A')}")
    lines.append(f"Organization: {metadata.get('organization', 'N/A')}")
    lines.append(f"Topic: {metadata.get('topic', 'N/A')}")
    lines.append("")

    if metadata.get("description"):
        lines.append(f"### Description")
        lines.append(metadata["description"][:2000])
        lines.append("")

    funding = metadata.get("funding", {})
    if funding.get("amount"):
        lines.append(f"### Funding")
        lines.append(f"Amount: {funding['amount']:,.2f} {funding.get('currency', '')}")
        lines.append("")

    trl = metadata.get("trl", {})
    if trl.get("value"):
        lines.append(f"### Technology Readiness Level")
        lines.append(f"TRL: {trl['value']}")
        if trl.get("rationale"):
            lines.append(f"Rationale: {trl['rationale'][:1000]}")
        lines.append("")

    team = metadata.get("team", {})
    if team.get("research_lead", {}).get("name"):
        lines.append(f"### Team")
        lines.append(f"Research Lead: {team['research_lead']['name']}")
        lines.append(f"Organization: {team.get('organization', 'N/A')}")
        lines.append("")

    tokenomics = metadata.get("tokenomics")
    if tokenomics:
        lines.append(f"### Tokenomics (IPT)")
        lines.append(f"Symbol: {tokenomics.get('symbol', 'N/A')}")
        lines.append(f"Holders: {tokenomics.get('holder_count', 'N/A')}")
        if tokenomics.get("primary_price_usd"):
            lines.append(f"Price: ${tokenomics['primary_price_usd']:.6f}")
        if tokenomics.get("primary_liquidity_usd"):
            lines.append(f"Liquidity: ${tokenomics['primary_liquidity_usd']:,.2f}")
        if tokenomics.get("primary_market_cap_usd"):
            lines.append(f"Market Cap: ${tokenomics['primary_market_cap_usd']:,.2f}")
        lines.append("")

    gov = metadata.get("governance", {})
    if gov.get("agreement_count", 0) > 0:
        lines.append(f"### Governance & Legal")
        lines.append(f"Agreements: {', '.join(gov.get('agreement_types', []))}")
        lines.append(f"Has Assignment Agreement: {gov.get('has_assignment_agreement', False)}")
        lines.append(f"Has Development Agreement: {gov.get('has_development_agreement', False)}")
        lines.append("")

    timeline = metadata.get("timeline", {})
    if timeline.get("minted_at"):
        lines.append(f"### Timeline")
        lines.append(f"Minted: {timeline['minted_at']}")
        if timeline.get("age_days"):
            lines.append(f"Age: {timeline['age_days']} days")
        if timeline.get("days_since_update") is not None:
            lines.append(f"Days since last update: {timeline['days_since_update']}")
        lines.append("")

    return "\n".join(lines)


def _format_aggregated_scores(categories: dict[str, Any]) -> str:
    """Format aggregated per-document scores for the prompt."""
    lines = ["## Per-Document Science Scores"]
    for dim_key, dim_data in categories.items():
        if not isinstance(dim_data, dict):
            continue
        score = dim_data.get("score", "N/A")
        sources = dim_data.get("sources", [])
        source_str = ", ".join(f"{s['doc']}={s['score']:.2f}" for s in sources[:5])
        lines.append(f"- {dim_key}: {score:.4f} (from: {source_str})")
        if dim_data.get("rationale"):
            rationale_preview = dim_data["rationale"][:300]
            lines.append(f"  Rationale: {rationale_preview}")
    return "\n".join(lines)


def _format_platform_context(context_slices: dict[str, str]) -> str:
    """Format platform doc slices into a context block."""
    if not context_slices:
        return ""
    lines = ["## Molecule Platform Context"]
    for title, content in context_slices.items():
        trimmed = content[:3000]
        lines.append(f"\n### {title}\n{trimmed}")
    return "\n".join(lines)


def _run_dimension_review(
    client: OpenAI,
    model: str,
    dimension: str,
    prompt_template: str,
    user_context: str,
) -> dict[str, Any]:
    """Run a single dimension review and parse the JSON response."""
    response_text = _llm_call(client, model, prompt_template, user_context)

    json_match = re.search(r"\{[\s\S]*\}", response_text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError:
            pass

    return {
        "dimension": dimension,
        "rationale": response_text,
        "score": None,
        "findings": [],
    }


def run_dao_review(
    enriched: dict[str, Any],
    model: str,
    prompts_dir: Path,
) -> dict[str, Any]:
    """Run DAO-level LLM review across all DAO-specific dimensions.

    Returns the enriched dict updated with LLM-generated rationales and
    assessments for DAO-specific dimensions.
    """
    client = OpenAI(base_url=VLLM_BASE_URL, api_key=VLLM_API_KEY)

    metadata = enriched.get("structured_metadata", {})
    categories = enriched.get("categories", {})
    platform_context = enriched.get("platform_context", {})

    metadata_block = _format_metadata_block(metadata)
    scores_block = _format_aggregated_scores(categories)
    context_block = _format_platform_context(platform_context)

    dao_review_prompt = _load_prompt(prompts_dir, "dao_review_prompt.md")

    user_content = f"{metadata_block}\n\n{scores_block}\n\n{context_block}"

    print("  [dao_review] Running synthesis review...")
    synthesis_response = _llm_call(client, model, dao_review_prompt, user_content)

    dao_categories: dict[str, Any] = {}

    json_match = re.search(r"\{[\s\S]*\}", synthesis_response)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            if "categories" in parsed:
                dao_categories = parsed["categories"]
            elif any(k in parsed for k in ["governance_accountability", "token_alignment", "execution_credibility"]):
                dao_categories = parsed
        except json.JSONDecodeError:
            pass

    llm_dimension_scores: dict[str, float] = {}
    for dim_key, dim_data in dao_categories.items():
        if isinstance(dim_data, dict) and dim_data.get("score") is not None:
            try:
                llm_dimension_scores[dim_key] = float(dim_data["score"])
            except (ValueError, TypeError):
                pass

    if not dao_categories:
        dao_categories["synthesis_rationale"] = {
            "rationale": synthesis_response,
            "score": None,
            "score_method": "llm_narrative",
        }
    else:
        dao_categories["synthesis_rationale"] = {
            "rationale": synthesis_response,
            "llm_dimension_scores": llm_dimension_scores,
            "score": None,
            "score_method": "llm_narrative",
        }

    if metadata.get("tokenomics"):
        print("  [dao_review] Running token alignment review...")
        try:
            token_prompt = _load_prompt(prompts_dir, "token_alignment_prompt.md")
            token_context = f"{metadata_block}\n\n{context_block}"
            token_response = _llm_call(client, model, token_prompt, token_context)

            token_result = _run_dimension_review(
                client, model, "token_alignment", token_prompt, token_context
            )
            if token_result.get("rationale"):
                dao_categories["token_alignment"] = {
                    "rationale": token_result.get("rationale", token_response),
                    "score": token_result.get("score"),
                    "score_method": "llm_structured_data",
                    "findings": token_result.get("findings", []),
                }
        except FileNotFoundError:
            print("  [dao_review] token_alignment_prompt.md not found, skipping")

    if enriched.get("per_document_reviews") and len(enriched["per_document_reviews"]) > 1:
        print("  [dao_review] Running cross-document consistency check...")
        try:
            synthesis_prompt = _load_prompt(prompts_dir, "dao_synthesis_prompt.md")
            docs_summary = json.dumps(enriched["per_document_reviews"], indent=2)[:4000]
            consistency_response = _llm_call(
                client, model, synthesis_prompt,
                f"{metadata_block}\n\n## Documents Reviewed\n{docs_summary}\n\n{scores_block}"
            )
            dao_categories["cross_doc_consistency"] = {
                "rationale": consistency_response,
                "score_method": "llm_consistency_check",
            }
        except FileNotFoundError:
            print("  [dao_review] dao_synthesis_prompt.md not found, skipping")

    merged_categories = {**categories}
    for dim_key, dim_data in dao_categories.items():
        if dim_key in merged_categories and isinstance(dim_data, dict):
            existing = merged_categories[dim_key]
            if isinstance(existing, dict) and dim_data.get("rationale"):
                existing["dao_rationale"] = dim_data.get("rationale", "")
                if dim_data.get("findings"):
                    existing["dao_findings"] = dim_data["findings"]
        else:
            merged_categories[dim_key] = dim_data

    result = {**enriched}
    result["categories"] = merged_categories
    result["review_statement"] = synthesis_response[:2000] if not dao_categories.get("synthesis_rationale") else ""

    return result


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Run DAO-level LLM review")
    parser.add_argument("enriched", type=Path, help="Path to enriched.json")
    parser.add_argument("-o", "--output", type=Path, help="Output path")
    parser.add_argument("--model", type=str, default=os.environ.get("VALIDATOR_MODEL", "/model"))
    parser.add_argument("--prompts-dir", type=Path)
    args = parser.parse_args()

    enriched = json.loads(args.enriched.read_text(encoding="utf-8"))
    prompts_dir = args.prompts_dir or Path(__file__).resolve().parent / "prompts"

    result = run_dao_review(enriched=enriched, model=args.model, prompts_dir=prompts_dir)

    output_json = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(output_json, encoding="utf-8")
        print(f"DAO review -> {args.output}")
    else:
        print(output_json)


if __name__ == "__main__":
    main()
