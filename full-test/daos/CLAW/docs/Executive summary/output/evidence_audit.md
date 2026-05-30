# Evidence audit trail

**Document:** 2025-06-13-CLAW-update-IRB-protocol-executive-summary-1  
**Review date:** May 22, 2026  
**Composite score:** 0.5852  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:28:25Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `62597d64aafbc81f` |
| retrieve_compare_llm.json | `e801d299dc6c910e` |
| screener.json | `516f130f68a36938` |
| originality.json | `52ff8f256f8ed228` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| execution_credibility | 0.5000 | evidence_grade_weighted | claim_count=3 |
| financial_integrity | 0.6000 | rubric_penalty | finding_count=1 |
| originality | 1.0000 | literature_similarity | compared_works=43 |
| real_world_traction | 0.3500 | evidence_grade_weighted | claim_count=1 |
| scientific_rigor | 0.3555 | evidence_grade_weighted | claim_count=13 |
| team_credibility | 0.6000 | rubric_penalty | finding_count=1 |

## Evidence grade counts (retrieve_compare)

- **execution_credibility:** self_reported_method: 3
- **governance_accountability:** self_reported_method: 1; unreferenced: 1
- **originality:** unreferenced: 3; self_reported_method: 1
- **real_world_traction:** unreferenced: 1
- **scientific_rigor:** unreferenced: 8; self_reported_method: 5; unverifiable: 2

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### scientific_rigor / methodological · chunk 9 · Scientific Rationale

**Grade:** `unreferenced`  

> The randomized, double-blind, placebo-controlled design ensures a rigorous evaluation of Percepta's efficacy and safety.

### scientific_rigor / boilerplate_method · chunk 7 · Study Population

**Grade:** `unverifiable`  

> Participants must maintain stable lifestyles (diet, alcohol, substance use, physical activity, sleep) during the study.

**References:**

- [85] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 0 · Executive summary

**Grade:** `unreferenced`  

> The study investigates Percepta® for cognitive optimization in adults with mild cognitive impairment using a 6-month randomized controlled trial design incorporating neurocognitive, wearable, and participant-reported outcomes.

### scientific_rigor / aspirational · chunk 1 · Project Overview

**Grade:** `unreferenced`  

> The study aims to determine if Percepta can improve cognitive performance, wearable biomarker metrics, and participant-reported brain health in adults with self-reported Mild Cognitive Impairment (MCI).

### scientific_rigor / aspirational · chunk 2 · Key Details

**Grade:** `unreferenced`  

> Conduct a decentralized clinical trial for safety and efficacy of Percepta in adults with self-reported Mild Cognitive Impairment (MCI).

### scientific_rigor / aspirational · chunk 3 · Background

**Grade:** `unreferenced`  

> Percepta offers a novel, multi-faceted approach by leveraging the neuroprotective properties of its ingredients, which have shown promise in preclinical studies for reducing neuroinflammation, oxidative stress, and amyloid-beta plaque aggregation.

### scientific_rigor / aspirational · chunk 3 · Background

**Grade:** `unreferenced`  

> Existing treatments for MCI, such as lecanemab and donanemab, have limitations in accessibility, cost, and safety, making alternative interventions necessary.

### scientific_rigor / aspirational · chunk 7 · Study Population

**Grade:** `unverifiable`  

> Exclusion criteria include use of cognitive-affecting medications, neurological or psychiatric disorders, allergies to ingredients, pregnancy, and APOE-4 allele carrier status.

**References:**

- [85] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 9 · Scientific Rationale

**Grade:** `unreferenced`  

> The rationale for Percepta is based on the neuroprotective properties of cat's claw and oolong tea extract, which have shown potential in preclinical studies to mitigate neuroinflammation, oxidative stress, and protein aggregation.

### scientific_rigor / aspirational · chunk 10 · Expected Outcomes

**Grade:** `unreferenced`  

> This study aims to provide foundational data on Percepta's safety, tolerability, and potential cognitive benefits.

### originality / aspirational · chunk 1 · Project Overview

**Grade:** `unreferenced`  

> The study aims to determine if Percepta can improve cognitive performance, wearable biomarker metrics, and participant-reported brain health in adults with self-reported Mild Cognitive Impairment (MCI).

### originality / aspirational · chunk 3 · Background

**Grade:** `unreferenced`  

> Percepta offers a novel, multi-faceted approach by leveraging the neuroprotective properties of its ingredients, which have shown promise in preclinical studies for reducing neuroinflammation, oxidative stress, and amyloid-beta plaque aggregation.

### originality / aspirational · chunk 3 · Background

**Grade:** `unreferenced`  

> Existing treatments for MCI, such as lecanemab and donanemab, have limitations in accessibility, cost, and safety, making alternative interventions necessary.

### governance_accountability / aspirational · chunk 2 · Key Details

**Grade:** `unreferenced`  

> Conduct a decentralized clinical trial for safety and efficacy of Percepta in adults with self-reported Mild Cognitive Impairment (MCI).

### real_world_traction / aspirational · chunk 10 · Expected Outcomes

**Grade:** `unreferenced`  

> If successful, findings could inform future research and contribute to the development of accessible, natural interventions for individuals experiencing cognitive decline.

## Document screener

- **financial_integrity** (concern) · *Safety and Monitoring*
  - Quote: Participants will be provided compensation for completing the study.
  - Observation: The protocol mentions compensation but fails to disclose the specific amount, the funding source, or the total budget. This lack of transparency regarding financial incentives is critical for assessing potential bias in participant reporting or dropout rates.

- **scientific_rigor** (concern) · *Study Population*
  - Quote: Inclusion criteria include adults aged 40 to 85, self-reported MCI (MoCA <25)...
  - Observation: The primary inclusion criterion for MCI is 'self-reported' status combined with a MoCA score, rather than a formal clinical diagnosis by a neurologist or neuropsychologist. This introduces significant selection bias and diagnostic uncertainty, weakening the internal validity of …

- **team_credibility** (concern) · *Project Overview*
  - Quote: Cerebrum DAO Lead Investigator: Dr. Mark Melnykowycz
  - Observation: The lead investigator is listed with a title ('Lead Investigator') but their specific academic credentials, prior publications in neurology or clinical trials, and institutional affiliation (other than the DAO) are not provided. This makes it difficult to assess their expertise …

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 43 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2018 | Nutritional patterns associated with the maintenance of neurocognitive … | 10.1016/j.phrs.2018.03.012 |
| 2 | None | 2020 | Dementia prevention, intervention, and care: 2020 report of the Lancet … | 10.1016/s0140-6736(20)30367-6 |
| 3 | None | 2013 | 2013 ESH/ESC Guidelines for the management of arterial hypertension | 10.1093/eurheartj/eht151 |
| 4 | None | 2024 | Two new Later Stone Age sites from the Final Pleistocene in the Falémé … | 10.3929/ethz-b-000667478 |
| 5 | None | 2021 | 2021 ESC Guidelines on cardiovascular disease prevention in clinical pr… | 10.1093/eurheartj/ehab484 |
| 6 | None | 2024 | The duality of amyloid-β: its role in normal and Alzheimer’s disease st… | 10.1186/s13041-024-01118-1 |
| 7 | None | 2024 | The Role of Diet and Gut Microbiota in Alzheimer’s Disease | 10.3390/nu16030412 |
| 8 | None | 2012 | NLRP3 is activated in Alzheimer’s disease and contributes to pathology … | 10.1038/nature11729 |
| 9 | None | 2020 | Comprehensive Review on Alzheimer’s Disease: Causes and Treatment | 10.3390/molecules25245789 |
| 10 | None | 2018 | Inflammation as a central mechanism in Alzheimer's disease | 10.1016/j.trci.2018.06.014 |
| 11 | None | 2022 | Lecanemab in Early Alzheimer’s Disease | 10.1056/nejmoa2212948 |
| 12 | None | 2024 | Dementia prevention, intervention, and care: 2024 report of the Lancet … | 10.1016/s0140-6736(24)01296-0 |
| 13 | None | 2024 | Alzheimer’s disease and its treatment–yesterday, today, and tomorrow | 10.3389/fphar.2024.1399121 |
| 14 | None | 2024 | Comparative Efficacy, Tolerability, and Acceptability of Donanemab, Lec… | 10.3233/jad-230911 |
| 15 | None | 2022 | Two Randomized Phase 3 Studies of Aducanumab in Early Alzheimer's Disea… | 10.14283/jpad.2022.30 |
