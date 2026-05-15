#!/usr/bin/env python3
"""Build a Markdown evidence audit for the pump-science (compounds) pipeline.

No LLM.

**Single compound:** reads ``grouped_by_stance.json``, optional ``*-review.json``,
optional ``units_tagged.jsonl``; writes ``evidence_audit.md`` next to the grouped file.

**Combination:** pass ``--combination-bundle`` (output of ``interactions.py``); optionally
``--combo-review`` (defaults to the same path ``review-multiple.py`` uses). Writes
``evidence_audit.md`` beside the combo review under ``reviews/compounds/<slug>/``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_PIPELINE = Path(__file__).resolve().parent
_COMPOUNDS = _PIPELINE.parent
_REPO_ROOT = _COMPOUNDS.parent

GENERATOR_VERSION = "1.1"
DEFAULT_MAX_BYTES = 120 * 1024

KNOWN_STANCES: tuple[str, ...] = (
    "supports_exploration",
    "raises_caution",
    "risk_information",
    "mixed_or_unclear",
    "context_only",
    "unmapped",
)


@dataclass
class BuildParams:
    excerpt_max_chars: int
    rationale_max_chars: int
    drop_context_only: bool
    provenance_compact: bool


@dataclass
class ComboParams:
    snippet_max_chars: int
    spl_excerpt_max_chars: int
    rationale_max_chars: int
    omit_mechanism_units: bool
    provenance_compact: bool


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_review_slug(compound_name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", compound_name).strip()


def default_review_path(compound_name: str) -> Path:
    """Match ``review.default_output_path`` (``reviews/compounds/<slug>/`` under repo root)."""
    safe = _safe_review_slug(compound_name)
    return _REPO_ROOT / "reviews" / "compounds" / safe / f"{safe}-review.json"


def combo_dir_slug(combination_name: str) -> str:
    """Same slug rule as ``review-multiple._default_output_path``."""
    return re.sub(r'[<>:"/\\|?*]', "_", combination_name).strip().replace(" ", "-")[:80]


def default_combo_review_path(combination_name: str) -> Path:
    safe = combo_dir_slug(combination_name)
    return _REPO_ROOT / "reviews" / "compounds" / safe / f"{safe}-combo-review.json"


def default_combo_evidence_audit_path(combination_name: str) -> Path:
    return default_combo_review_path(combination_name).parent / "evidence_audit.md"


def _sha256_file_short(path: Path, *, nbytes: int = 16) -> str | None:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:nbytes]


def _git_revision(cwd: Path) -> str | None:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def _trunc(s: str, max_len: int) -> str:
    s = s.replace("\n", " ").strip()
    if len(s) <= max_len:
        return s
    return s[: max_len - 1] + "…"


def _payload_excerpt(payload: Any, max_chars: int) -> str:
    if payload is None:
        return ""
    if isinstance(payload, str):
        return _trunc(payload, max_chars)
    try:
        raw = json.dumps(payload, ensure_ascii=False)
    except (TypeError, ValueError):
        raw = str(payload)
    return _trunc(raw, max_chars)


def _build_provenance_block(
    *,
    cwd: Path,
    grouped_path: Path,
    review_path: Path | None,
    tagged_path: Path | None,
    output_path: Path,
    compact: bool,
) -> list[str]:
    lines: list[str] = []
    lines.append("## Provenance")
    lines.append("")
    gen_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    git_rev = _git_revision(cwd) or _git_revision(output_path.parent)
    model = (
        os.environ.get("REVIEWER_MODEL", "").strip()
        or os.environ.get("TAGGER_MODEL", "").strip()
        or "(unset)"
    )

    lines.append(f"- **Generated (UTC):** {gen_ts}")
    lines.append(f"- **Generator:** `compounds/pipeline/evidence-doc.py` v{GENERATOR_VERSION} (no LLM)")
    lines.append(
        f"- **REVIEWER_MODEL / TAGGER_MODEL:** `{model}` "
        "*(models used by upstream tag / review steps, when set)*",
    )
    lines.append(
        f"- **Git revision:** `{git_rev}` *(repository containing the run, best-effort)*"
        if git_rev
        else "- **Git revision:** *(unavailable — not a git checkout or git not on PATH)*",
    )

    if not compact:
        lines.append("")
        lines.append("| Input | SHA-256 (first 16 hex) |")
        lines.append("|-------|-------------------------|")
        rows = [
            ("grouped_by_stance.json", grouped_path),
            ("review.json", review_path),
            ("units_tagged.jsonl", tagged_path),
        ]
        for label, pth in rows:
            if pth is None or not pth.is_file():
                lines.append(f"| {label} | — |")
            else:
                fp = _sha256_file_short(pth)
                lines.append(f"| {label} | `{fp or '?'}` |")
        lines.append("")
        lines.append(
            "*Fingerprints are of the files read at generation time; use them to verify this "
            "document matches a frozen artifact bundle.*",
        )
    else:
        g = _sha256_file_short(grouped_path)
        r = _sha256_file_short(review_path) if review_path else None
        lines.append(
            f"- **Fingerprints (short):** grouped=`{g or '?'}` review=`{r or '?'}`",
        )

    lines.append("")
    lines.append("### Scores in this audit")
    lines.append("")
    lines.append(
        "**Scientific grounding** (stance ratio) and **aggregate risk** (severity-weighted) "
        "are computed in ``compounds/pipeline/single/group_by_stance.py`` from tagged units. "
        "Narrative **rationales** in ``review.json`` come from ``review.py`` (LLM upstream of this tool).",
    )
    lines.append("")
    return lines


def _iter_members(grouped: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    by_stance = grouped.get("by_stance")
    if not isinstance(by_stance, dict):
        return out
    for stance in KNOWN_STANCES:
        bucket = by_stance.get(stance)
        if not isinstance(bucket, dict):
            continue
        members = bucket.get("members")
        if not isinstance(members, list):
            continue
        for m in members:
            if isinstance(m, dict):
                out.append((stance, m))
    return out


def _stance_counts(grouped: dict[str, Any]) -> dict[str, int]:
    counts: dict[str, int] = {}
    by_stance = grouped.get("by_stance")
    if not isinstance(by_stance, dict):
        return counts
    for stance in KNOWN_STANCES:
        b = by_stance.get(stance)
        if isinstance(b, dict):
            counts[stance] = int(b.get("count", 0))
    return counts


def _risk_severity_counts(grouped: dict[str, Any]) -> dict[str, int]:
    scores = grouped.get("scores")
    if not isinstance(scores, dict):
        return {}
    ar = scores.get("aggregate_risk")
    if not isinstance(ar, dict):
        return {}
    sc = ar.get("severity_counts")
    return {str(k): int(v) for k, v in sc.items()} if isinstance(sc, dict) else {}


def build_audit_markdown(
    grouped: dict[str, Any],
    review: dict[str, Any] | None,
    params: BuildParams,
    *,
    provenance_lines: list[str] | None = None,
) -> str:
    lines: list[str] = []
    name = grouped.get("compound_name")
    if not name and review:
        name = review.get("research_name") or review.get("compound_name")
    if not name:
        name = "?"

    review_date = review.get("review_date", "?") if review else "?"

    scores = grouped.get("scores") if isinstance(grouped.get("scores"), dict) else {}
    sg = scores.get("scientific_grounding") if isinstance(scores.get("scientific_grounding"), dict) else {}
    ar = scores.get("aggregate_risk") if isinstance(scores.get("aggregate_risk"), dict) else {}
    sg_s = f"{float(sg['score']):.4f}" if isinstance(sg.get("score"), (int, float)) else str(sg.get("score"))
    ar_s = f"{float(ar['score']):.4f}" if isinstance(ar.get("score"), (int, float)) else str(ar.get("score"))

    lines.append("# Evidence audit trail")
    lines.append("")
    lines.append(f"**Compound:** {name}  ")
    lines.append(f"**Review date:** {review_date}  ")
    lines.append(f"**Scientific grounding score (stance ratio):** {sg_s}  ")
    lines.append(f"**Aggregate risk score (severity-weighted):** {ar_s}  ")
    lines.append("")
    lines.append(
        "*Narrative review text lives in ``*-review.json`` (``review_statement`` and category "
        "rationales). This file traces tagged units, stance distribution, and risk labels.*",
    )
    lines.append("")
    if provenance_lines:
        lines.extend(provenance_lines)

    lines.append("## Pipeline scores (from grouped_by_stance.json)")
    lines.append("")
    lines.append("| Metric | Value | Detail |")
    lines.append("|--------|------:|--------|")
    lines.append(
        f"| scientific_grounding | {sg_s} | "
        f"supports={sg.get('supports_exploration_count', '?')}; "
        f"caution={sg.get('raises_caution_count', '?')}; "
        f"denom={sg.get('support_and_caution_total', '?')} |",
    )
    lines.append(
        f"| aggregate_risk | {ar_s} | "
        f"scored_units={ar.get('scored_unit_count', '?')}; "
        f"skipped_na={ar.get('skipped_na_count', '?')}; "
        f"skipped_null={ar.get('skipped_null_count', '?')} |",
    )
    lines.append("")

    if review and isinstance(review.get("categories"), dict):
        lines.append("## Category scores (from review.json)")
        lines.append("")
        lines.append("| Category | Score |")
        lines.append("|----------|------:|")
        for cat_key, data in sorted(review["categories"].items()):
            if not isinstance(data, dict):
                continue
            sc = data.get("score")
            sc_s = f"{float(sc):.4f}" if isinstance(sc, (int, float)) else str(sc)
            lines.append(f"| {cat_key} | {sc_s} |")
        lines.append("")

    lines.append("## Stance counts (tagging)")
    lines.append("")
    scounts = _stance_counts(grouped)
    for stance in KNOWN_STANCES:
        if stance in scounts:
            lines.append(f"- **{stance}:** {scounts[stance]}")
    lines.append(f"- **total_units:** {grouped.get('total_units', '?')}")
    lines.append("")

    lines.append("## Risk severity counts (tagged units)")
    lines.append("")
    rc = _risk_severity_counts(grouped)
    if rc:
        parts = [f"{k}: {v}" for k, v in sorted(rc.items(), key=lambda x: (-x[1], x[0]))]
        lines.append("- " + "; ".join(parts))
    else:
        lines.append("*No aggregate_risk.severity_counts in grouped file.*")
    lines.append("")

    lines.append("## Unit-level trace")
    lines.append("")
    if params.drop_context_only:
        lines.append(
            "*Omitting ``context_only`` stance rows under current size budget "
            "(re-run with a higher ``--max-bytes`` or adjust trimming).*",
        )
        lines.append("")

    shown = 0
    for stance, unit in sorted(_iter_members(grouped), key=lambda x: (x[0], str(x[1].get("unit_id", "")))):
        if params.drop_context_only and stance == "context_only":
            continue
        shown += 1
        uid = unit.get("unit_id", "?")
        ut = unit.get("unit_type", "?")
        sec = unit.get("report_section") or "?"
        sev = unit.get("risk_severity")
        sev_s = str(sev) if sev is not None else "—"
        lines.append(f"### {stance} · unit {uid} · {ut}")
        lines.append("")
        lines.append(f"**Section:** {sec}  ")
        lines.append(f"**Risk severity:** `{sev_s}`  ")
        lines.append("")
        excerpt = _payload_excerpt(unit.get("payload"), params.excerpt_max_chars)
        lines.append(f"> {excerpt or '*(empty payload)*'}")
        lines.append("")

    if shown == 0:
        lines.append("*No units in grouped file.*")
        lines.append("")

    if review:
        lines.append("## Review rationales (verbatim from review.json)")
        lines.append("")
        cats = review.get("categories")
        if isinstance(cats, dict):
            for key in ("scientific_grounding", "risk_assessment"):
                block = cats.get(key)
                if not isinstance(block, dict):
                    continue
                rat = block.get("rationale")
                if not rat:
                    continue
                lines.append(f"### {key}")
                lines.append("")
                lines.append(_trunc(str(rat), params.rationale_max_chars))
                lines.append("")
        stmt = review.get("review_statement")
        if stmt:
            lines.append("### review_statement")
            lines.append("")
            lines.append(_trunc(str(stmt), params.rationale_max_chars))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def shrink_params(p: BuildParams) -> BuildParams:
    return BuildParams(
        excerpt_max_chars=max(120, p.excerpt_max_chars - 80),
        rationale_max_chars=max(400, p.rationale_max_chars - 200),
        drop_context_only=True,
        provenance_compact=True,
    )


def build_under_budget(
    grouped: dict[str, Any],
    review: dict[str, Any] | None,
    max_bytes: int,
    initial: BuildParams,
    *,
    provenance_full_lines: list[str],
    provenance_compact_lines: list[str],
) -> tuple[str, BuildParams]:
    def _prov(p: BuildParams) -> list[str] | None:
        if not provenance_full_lines:
            return None
        return provenance_compact_lines if p.provenance_compact else provenance_full_lines

    p = initial
    for _ in range(16):
        text = build_audit_markdown(grouped, review, p, provenance_lines=_prov(p))
        if len(text.encode("utf-8")) <= max_bytes:
            return text, p
        p = shrink_params(p)
    text = build_audit_markdown(grouped, review, p, provenance_lines=_prov(p))
    return text, p


def _build_combo_provenance_block(
    *,
    cwd: Path,
    bundle_path: Path,
    combo_review_path: Path | None,
    grouped_paths: list[tuple[str, Path]],
    output_path: Path,
    compact: bool,
) -> list[str]:
    lines: list[str] = []
    lines.append("## Provenance")
    lines.append("")
    gen_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    git_rev = _git_revision(cwd) or _git_revision(output_path.parent)
    model = (
        os.environ.get("REVIEWER_MODEL", "").strip()
        or os.environ.get("TAGGER_MODEL", "").strip()
        or "(unset)"
    )
    lines.append(f"- **Generated (UTC):** {gen_ts}")
    lines.append(f"- **Generator:** `compounds/pipeline/evidence-doc.py` v{GENERATOR_VERSION} (no LLM)")
    lines.append(f"- **Mode:** combination (interactions bundle + combo review)")
    lines.append(
        f"- **REVIEWER_MODEL / TAGGER_MODEL:** `{model}` "
        "*(models used by upstream review-multiple.py, when set)*",
    )
    lines.append(
        f"- **Git revision:** `{git_rev}` *(best-effort)*"
        if git_rev
        else "- **Git revision:** *(unavailable)*",
    )
    if not compact:
        lines.append("")
        lines.append("| Input | SHA-256 (first 16 hex) |")
        lines.append("|-------|-------------------------|")
        rows: list[tuple[str, Path | None]] = [
            ("interactions bundle", bundle_path),
            ("combo-review.json", combo_review_path),
        ]
        for compound_label, gp in grouped_paths:
            rows.append((f"grouped_by_stance ({compound_label})", gp))
        for label, pth in rows:
            if pth is None or not pth.is_file():
                lines.append(f"| {label} | — |")
            else:
                fp = _sha256_file_short(pth)
                lines.append(f"| {label} | `{fp or '?'}` |")
        lines.append("")
        lines.append(
            "*Fingerprints are of the files read at generation time; use them to verify this "
            "document matches a frozen artifact bundle.*",
        )
    else:
        b = _sha256_file_short(bundle_path)
        c = _sha256_file_short(combo_review_path) if combo_review_path else None
        lines.append(f"- **Fingerprints (short):** bundle=`{b or '?'}` combo_review=`{c or '?'}`")
    lines.append("")
    lines.append("### What this audit contains")
    lines.append("")
    lines.append(
        "Structured fields come from ``interactions.py`` (no LLM). Narrative paragraphs come "
        "from ``review-multiple.py`` (LLM). Per-compound stance/unit detail remains in each "
        "compound’s ``compounds/data/<compound>/evidence_audit.md`` when present.",
    )
    lines.append("")
    return lines


def _coverage_rows(coverage: Any) -> list[str]:
    if not isinstance(coverage, dict):
        return ["*No coverage object.*"]
    rows: list[str] = []
    for key in sorted(coverage.keys()):
        info = coverage[key]
        if not isinstance(info, dict):
            continue
        present = info.get("present")
        reason = info.get("reason")
        rows.append(f"- **{key}:** present={present}" + (f"; reason={reason}" if reason else ""))
    return rows or ["*Empty coverage.*"]


def build_combo_audit_markdown(
    bundle: dict[str, Any],
    combo_review: dict[str, Any] | None,
    params: ComboParams,
    *,
    provenance_lines: list[str] | None = None,
) -> str:
    lines: list[str] = []
    name = str(bundle.get("combination_name") or "?")
    gen_at = bundle.get("generated_at", "?")
    review_date = combo_review.get("review_date", "?") if combo_review else "?"

    lines.append("# Evidence audit trail (combination)")
    lines.append("")
    lines.append(f"**Combination:** {name}  ")
    lines.append(f"**Bundle generated:** {gen_at}  ")
    lines.append(f"**Combo review date:** {review_date}  ")
    lines.append(f"**Compounds:** {bundle.get('compound_count', '?')}  ")
    lines.append("")
    lines.append(
        "*This file is the non-LLM audit for the **pairing** (bundle + cross-references + SPL/KEGG excerpts). "
        "Per-compound unit/stance traces are in each compound’s data-directory ``evidence_audit.md``.*",
    )
    lines.append("")
    if provenance_lines:
        lines.extend(provenance_lines)

    xr = bundle.get("cross_reference")
    lines.append("## Cross-reference (interactions.py)")
    lines.append("")
    if isinstance(xr, dict):
        note = xr.get("note")
        if note:
            lines.append(f"*{note}*")
            lines.append("")
        sp = xr.get("shared_pathways")
        if isinstance(sp, list) and sp:
            lines.append("**Shared KEGG longevity flags:** " + ", ".join(str(x) for x in sp))
        else:
            lines.append("**Shared KEGG longevity flags:** *(none)*")
        lines.append("")
        em = xr.get("explicit_mentions")
        n_em = len(em) if isinstance(em, list) else 0
        lines.append(f"**Explicit cross-mentions (token match):** {n_em}")
        lines.append("")
        sm = xr.get("spl_coverage_summary")
        if sm:
            lines.append(f"**SPL coverage:** {sm}")
            lines.append("")
    else:
        lines.append("*No cross_reference in bundle.*")
        lines.append("")

    compounds_map = bundle.get("compounds")
    if not isinstance(compounds_map, dict):
        compounds_map = {}

    lines.append("## Per-compound bundle trace")
    lines.append("")
    for cname in sorted(compounds_map.keys()):
        ev = compounds_map[cname]
        if not isinstance(ev, dict):
            continue
        lines.append(f"### {cname}")
        lines.append("")
        lines.append(f"- **data_dir:** `{ev.get('data_dir', '?')}`")
        lines.append(f"- **found:** {ev.get('found')}")
        warns = ev.get("warnings")
        if isinstance(warns, list) and warns:
            lines.append("- **warnings:**")
            for w in warns:
                lines.append(f"  - {w}")
        lines.append(
            f"- **scores (from single-compound reviews, embedded in bundle):** "
            f"scientific_grounding={ev.get('scientific_grounding_score')!s} · "
            f"risk={ev.get('risk_score')!s}",
        )
        lines.append("")
        lines.append("#### Coverage")
        lines.append("")
        lines.extend(_coverage_rows(ev.get("coverage")))
        lines.append("")

        kegg = ev.get("kegg")
        if isinstance(kegg, dict):
            flags = kegg.get("flags_present")
            if isinstance(flags, list) and flags:
                lines.append("**KEGG longevity flags present:** " + ", ".join(str(x) for x in flags))
            else:
                lines.append("**KEGG longevity flags present:** *(none)*")
            lines.append("")
        spl = ev.get("spl")
        if isinstance(spl, dict):
            lines.append("#### SPL (extracted text)")
            lines.append("")
            lines.append(f"- label_matched: `{spl.get('label_matched')}` — {spl.get('match_note', '')}")
            excerpts = spl.get("interaction_excerpts")
            if isinstance(excerpts, list) and excerpts:
                lines.append("- **interaction_excerpts** (truncated):")
                lines.append("")
                for i, ex in enumerate(excerpts[:5], start=1):
                    lines.append(f"  {i}. {_trunc(str(ex), params.spl_excerpt_max_chars)}")
                if len(excerpts) > 5:
                    lines.append(f"  *… {len(excerpts) - 5} more excerpt(s) omitted here.*")
                lines.append("")
            mech = spl.get("mechanism_excerpt")
            if mech:
                lines.append("- **mechanism_excerpt** (truncated):")
                lines.append("")
                lines.append(_trunc(str(mech), params.spl_excerpt_max_chars))
                lines.append("")

        if not params.omit_mechanism_units:
            mus = ev.get("mechanism_units")
            if isinstance(mus, list) and mus:
                lines.append("#### Mechanism / pathway units (from bundle)")
                lines.append("")
                for u in mus:
                    if not isinstance(u, dict):
                        continue
                    uid = u.get("unit_id", "?")
                    ut = u.get("unit_type", "?")
                    st = u.get("decision_relevance", "?")
                    sn = u.get("snippet")
                    sn_s = _trunc(str(sn), params.snippet_max_chars) if sn else "*(no snippet)*"
                    lines.append(f"- **{uid}** ({ut}) · stance `{st}` — {sn_s}")
                lines.append("")
        lines.append("---")
        lines.append("")

    if combo_review:
        lines.append("## Combo review (verbatim excerpts from combo-review.json)")
        lines.append("")
        cats = combo_review.get("categories")
        if isinstance(cats, dict):
            lines.append("| Category | Score / metric |")
            lines.append("|----------|------------------|")
            for cat_key in sorted(cats.keys()):
                block = cats[cat_key]
                if not isinstance(block, dict):
                    continue
                sc = block.get("score")
                if isinstance(sc, (int, float)):
                    metric = f"{float(sc):.2f}"
                else:
                    metric = str(sc) if sc is not None else "—"
                lines.append(f"| {cat_key} | {metric} |")
            lines.append("")
            for key in ("scientific_grounding", "risk_assessment", "compatibility"):
                block = cats.get(key)
                if not isinstance(block, dict):
                    continue
                rat = block.get("rationale")
                if not rat:
                    continue
                lines.append(f"### {key}")
                lines.append("")
                lines.append(_trunc(str(rat), params.rationale_max_chars))
                lines.append("")
        stmt = combo_review.get("review_statement")
        if stmt:
            lines.append("### review_statement")
            lines.append("")
            lines.append(_trunc(str(stmt), params.rationale_max_chars))
            lines.append("")
    else:
        lines.append("## Combo review")
        lines.append("")
        lines.append("*combo-review.json not found — run review-multiple.py or pass ``--combo-review``.*")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def shrink_combo_params(p: ComboParams) -> ComboParams:
    return ComboParams(
        snippet_max_chars=max(80, p.snippet_max_chars - 60),
        spl_excerpt_max_chars=max(200, p.spl_excerpt_max_chars - 150),
        rationale_max_chars=max(800, p.rationale_max_chars - 800),
        omit_mechanism_units=True,
        provenance_compact=True,
    )


def build_combo_under_budget(
    bundle: dict[str, Any],
    combo_review: dict[str, Any] | None,
    max_bytes: int,
    initial: ComboParams,
    *,
    provenance_full_lines: list[str],
    provenance_compact_lines: list[str],
) -> tuple[str, ComboParams]:
    def _prov(p: ComboParams) -> list[str] | None:
        if not provenance_full_lines:
            return None
        return provenance_compact_lines if p.provenance_compact else provenance_full_lines

    p = initial
    for _ in range(18):
        text = build_combo_audit_markdown(bundle, combo_review, p, provenance_lines=_prov(p))
        if len(text.encode("utf-8")) <= max_bytes:
            return text, p
        p = shrink_combo_params(p)
    text = build_combo_audit_markdown(bundle, combo_review, p, provenance_lines=_prov(p))
    return text, p


def main_combination(args: argparse.Namespace) -> int:
    bundle_path = args.combination_bundle.expanduser().resolve()
    if not bundle_path.is_file():
        print(f"error: missing bundle {bundle_path}", file=sys.stderr)
        return 1

    bundle = _load_json(bundle_path)
    combo_name = str(bundle.get("combination_name") or "?")

    combo_review_path = (
        args.combo_review.expanduser().resolve()
        if args.combo_review
        else default_combo_review_path(combo_name)
    )
    combo_review: dict[str, Any] | None = (
        _load_json(combo_review_path) if combo_review_path.is_file() else None
    )

    combo_out_dir = default_combo_review_path(combo_name).parent
    out_path = (
        args.output.expanduser().resolve()
        if args.output
        else combo_out_dir / "evidence_audit.md"
    )

    compounds_map = bundle.get("compounds")
    grouped_paths: list[tuple[str, Path]] = []
    if isinstance(compounds_map, dict):
        for cname in sorted(compounds_map.keys()):
            ev = compounds_map[cname]
            if not isinstance(ev, dict):
                continue
            dd = ev.get("data_dir")
            if isinstance(dd, str):
                gp = Path(dd) / "grouped_by_stance.json"
                grouped_paths.append((cname, gp.resolve() if gp.is_absolute() else Path(dd).resolve()))

    cwd = bundle_path.parent
    prov_full: list[str] = []
    prov_compact: list[str] = []
    if not args.skip_provenance:
        prov_full = _build_combo_provenance_block(
            cwd=cwd,
            bundle_path=bundle_path,
            combo_review_path=combo_review_path if combo_review_path.is_file() else None,
            grouped_paths=grouped_paths,
            output_path=out_path,
            compact=False,
        )
        prov_compact = _build_combo_provenance_block(
            cwd=cwd,
            bundle_path=bundle_path,
            combo_review_path=combo_review_path if combo_review_path.is_file() else None,
            grouped_paths=grouped_paths,
            output_path=out_path,
            compact=True,
        )

    initial = ComboParams(
        snippet_max_chars=args.excerpt_max_chars,
        spl_excerpt_max_chars=min(2000, max(400, args.excerpt_max_chars * 3)),
        rationale_max_chars=args.rationale_max_chars,
        omit_mechanism_units=False,
        provenance_compact=False,
    )

    text, used = build_combo_under_budget(
        bundle,
        combo_review,
        args.max_bytes,
        initial,
        provenance_full_lines=prov_full,
        provenance_compact_lines=prov_compact,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    nbytes = len(text.encode("utf-8"))
    print(f"  Wrote {out_path} ({nbytes} bytes, max {args.max_bytes})")
    if used.omit_mechanism_units or used.provenance_compact:
        print(
            "  Note: budget trimming applied "
            f"(omit_mechanism_units={used.omit_mechanism_units}, "
            f"provenance_compact={used.provenance_compact})",
        )
    if combo_review is None:
        print(
            f"  Note: combo review not found at {combo_review_path}; audit is bundle-only.",
            file=sys.stderr,
        )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--combination-bundle",
        type=Path,
        default=None,
        metavar="BUNDLE.json",
        help=(
            "Interactions evidence bundle (interactions.py output). Writes combination "
            "``evidence_audit.md`` next to the combo review under ``reviews/compounds/<slug>/``."
        ),
    )
    ap.add_argument(
        "--combo-review",
        type=Path,
        default=None,
        help="Path to *-combo-review.json (default: inferred from bundle ``combination_name``).",
    )
    ap.add_argument(
        "--directory",
        "-d",
        type=Path,
        default=None,
        help="Compound data directory (contains grouped_by_stance.json)",
    )
    ap.add_argument(
        "--grouped",
        type=Path,
        default=None,
        help="Path to grouped_by_stance.json (default: <directory>/grouped_by_stance.json)",
    )
    ap.add_argument(
        "--review",
        type=Path,
        default=None,
        help="Path to *-review.json (default: infer from compound_name → ``reviews/compounds/<slug>/``).",
    )
    ap.add_argument(
        "--tagged",
        type=Path,
        default=None,
        help="Path to units_tagged.jsonl (default: <directory>/units_tagged.jsonl if present)",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output Markdown (default: <directory>/evidence_audit.md)",
    )
    ap.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES)
    ap.add_argument("--excerpt-max-chars", type=int, default=400)
    ap.add_argument("--rationale-max-chars", type=int, default=8000)
    ap.add_argument("--skip-provenance", action="store_true")
    args = ap.parse_args()

    if args.combination_bundle is not None:
        return main_combination(args)

    directory = (args.directory or Path.cwd()).expanduser().resolve()
    grouped_path = (args.grouped or directory / "grouped_by_stance.json").expanduser().resolve()
    if not grouped_path.is_file():
        print(f"error: missing {grouped_path}", file=sys.stderr)
        return 1

    grouped = _load_json(grouped_path)
    compound_name = str(grouped.get("compound_name") or directory.name)

    review_path = args.review.expanduser().resolve() if args.review else default_review_path(compound_name)
    review: dict[str, Any] | None = _load_json(review_path) if review_path.is_file() else None

    tagged_path = (args.tagged or directory / "units_tagged.jsonl").expanduser().resolve()
    if not tagged_path.is_file():
        tagged_path_t: Path | None = None
    else:
        tagged_path_t = tagged_path

    out_path = (args.output or directory / "evidence_audit.md").expanduser().resolve()

    initial = BuildParams(
        excerpt_max_chars=args.excerpt_max_chars,
        rationale_max_chars=args.rationale_max_chars,
        drop_context_only=False,
        provenance_compact=False,
    )

    prov_full: list[str] = []
    prov_compact: list[str] = []
    if not args.skip_provenance:
        prov_full = _build_provenance_block(
            cwd=directory,
            grouped_path=grouped_path,
            review_path=review_path if review_path.is_file() else None,
            tagged_path=tagged_path_t,
            output_path=out_path,
            compact=False,
        )
        prov_compact = _build_provenance_block(
            cwd=directory,
            grouped_path=grouped_path,
            review_path=review_path if review_path.is_file() else None,
            tagged_path=tagged_path_t,
            output_path=out_path,
            compact=True,
        )

    text, used = build_under_budget(
        grouped,
        review,
        args.max_bytes,
        initial,
        provenance_full_lines=prov_full,
        provenance_compact_lines=prov_compact,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    nbytes = len(text.encode("utf-8"))
    print(f"  Wrote {out_path} ({nbytes} bytes, max {args.max_bytes})")
    if used.drop_context_only or used.provenance_compact:
        print(
            "  Note: budget trimming applied "
            f"(drop_context_only={used.drop_context_only}, "
            f"provenance_compact={used.provenance_compact})",
        )
    if review is None:
        print(
            f"  Note: review.json not found at {review_path}; audit omits review categories and rationales.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
