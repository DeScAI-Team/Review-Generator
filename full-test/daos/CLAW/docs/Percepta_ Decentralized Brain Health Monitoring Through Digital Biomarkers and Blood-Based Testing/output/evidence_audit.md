# Evidence audit trail

**Document:** claw-percepta-labs-report  
**Review date:** May 22, 2026  
**Composite score:** 0.5609  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:25:46Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `a9839677d9228a64` |
| retrieve_compare_llm.json | `c1b555087a0bcbca` |
| screener.json | `ea026bca6c435347` |
| originality.json | `d517efcadcc2afe1` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.5000 | evidence_grade_weighted | claim_count=3 |
| execution_credibility | 0.3750 | evidence_grade_weighted | claim_count=3 |
| financial_integrity | 0.3500 | evidence_grade_weighted | claim_count=1 |
| originality | 1.0000 | literature_similarity | compared_works=33 |
| scientific_rigor | 0.3500 | evidence_grade_weighted | claim_count=13 |

## Evidence grade counts (retrieve_compare)

- **evidential_strength:** self_reported: 3
- **execution_credibility:** self_reported: 1; unreferenced: 1; unverifiable: 1
- **financial_integrity:** unreferenced: 1
- **governance_accountability:** unreferenced: 2; unverifiable: 1
- **originality:** unreferenced: 7
- **scientific_rigor:** unreferenced: 10; self_reported: 3

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### scientific_rigor / empirical · chunk 4 · Current Status

**Grade:** `unreferenced`  

> Small-scale commercial production is already operational for the supplement market, demonstrating manufacturing feasibility.

### scientific_rigor / methodological · chunk 2 · The Science

**Grade:** `unreferenced`  

> Through remote blood collection paired with digital cognitive assessments, Percepta identifies early-stage neurodegenerative signatures that serve as proxies for tau pathology and structural brain changes.

### scientific_rigor / contextual · chunk 3 · What Has Been Demonstrated

**Grade:** `unreferenced`  

> Published literature demonstrates that polyphenols and proanthocyanidins from Uncaria tomentosa and oolong tea can reduce amyloid burden, modulate neuroinflammation, and support memory function

### scientific_rigor / contextual · chunk 4 · Current Status

**Grade:** `unreferenced`  

> The active ingredients are derived from botanical sources with established dietary use and have shown no safety concerns in preclinical models.

### scientific_rigor / aspirational · chunk 0 · Percepta: Decentralized Brain Health Monitoring Through Digital Biomarkers and Blood-Based Testing

**Grade:** `unreferenced`  

> Percepta is developing a non-invasive, at-home cognitive monitoring platform that combines digital biomarkers with blood-based assays to detect early changes in brain health before clinical symptoms emerge.

### scientific_rigor / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Most cognitive decline goes undetected until significant symptoms appear, when intervention options are limited.

### scientific_rigor / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> The platform integrates remote blood collection with validated neurodegenerative biomarkers to enable longitudinal tracking of cognitive health, creating a scalable pathway for decentralized clinical assessments.

### scientific_rigor / aspirational · chunk 4 · Current Status

**Grade:** `unreferenced`  

> The biomarker panel has been expanded to include pTau-217 quantification using the Simoa ALZpath assay, and device validation for home-use blood collection is underway.

### scientific_rigor / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Competitors like Prevagen lack robust scientific validation despite reporting over $200 million in annual sales.

### scientific_rigor / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> The Percepta model creates a replicable blueprint for future DeSci-enabled studies across wellness and neurodegeneration pipelines.

### originality / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Most cognitive decline goes undetected until significant symptoms appear, when intervention options are limited.

### originality / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Percepta addresses this gap by making sophisticated brain health monitoring accessible outside traditional clinical settings.

### originality / aspirational · chunk 2 · The Science

**Grade:** `unreferenced`  

> This represents the first crowdsale-backed tokenization of a brain health patent portfolio through an IP-NFT structure, pioneering a new model for decentralized science (DeSci) funding.

### originality / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Percepta targets a critical market gap: the absence of human-evidence-backed memory supplements.

### originality / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Competitors like Prevagen lack robust scientific validation despite reporting over $200 million in annual sales.

### originality / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Percepta aims to establish category leadership through peer-reviewed preclinical data and a decentralized human study powered by tokenized funding.

### originality / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> The tokenized IP-NFT and community-backed funding mechanisms represent an innovative approach to supporting brain health research.

### governance_accountability / aspirational · chunk 2 · The Science

**Grade:** `unreferenced`  

> This represents the first crowdsale-backed tokenization of a brain health patent portfolio through an IP-NFT structure, pioneering a new model for decentralized science (DeSci) funding.

### governance_accountability / aspirational · chunk 5 · Next Steps

**Grade:** `unverifiable`  

> Future plans may explore the FDA botanical drug pathway contingent on clinical efficacy data.

**References:**

- [1] ? → (no verdict — missing abstract)

### governance_accountability / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Percepta aims to establish category leadership through peer-reviewed preclinical data and a decentralized human study powered by tokenized funding.

### execution_credibility / empirical · chunk 4 · Current Status

**Grade:** `unreferenced`  

> Small-scale commercial production is already operational for the supplement market, demonstrating manufacturing feasibility.

### execution_credibility / aspirational · chunk 5 · Next Steps

**Grade:** `unverifiable`  

> Future plans may explore the FDA botanical drug pathway contingent on clinical efficacy data.

**References:**

- [1] ? → (no verdict — missing abstract)

### financial_integrity / aspirational · chunk 6 · The Opportunity

**Grade:** `unreferenced`  

> Percepta aims to establish category leadership through peer-reviewed preclinical data and a decentralized human study powered by tokenized funding.

## Document screener

*No screener findings (or all filtered out).*

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 33 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2018 | NIA‐AA Research Framework: Toward a biological definition of Alzheimer'… | 10.1016/j.jalz.2018.02.018 |
| 2 | None | 2024 | Revised criteria for diagnosis and staging of Alzheimer's disease: Alzh… | 10.1002/alz.13859 |
| 3 | None | 2017 | Oxidative Stress, Synaptic Dysfunction, and Alzheimer’s Disease | 10.3233/jad-161088 |
| 4 | None | 2021 | Blood-based biomarkers for Alzheimer's disease: towards clinical implem… | 10.1016/s1474-4422(21)00361-6 |
| 5 | None | 2018 | Blood-Brain Barrier: From Physiology to Disease and Back | 10.1152/physrev.00050.2017 |
| 6 | None | 2021 | Current advances in digital cognitive assessment for preclinical Alzhei… | 10.1002/dad2.12217 |
| 7 | None | 2020 | Implementing Remote Memory Clinics to Enhance Clinical Care During and … | 10.3389/fpsyt.2020.579934 |
| 8 | None | 2020 | 2020 ESC Guidelines for the diagnosis and management of atrial fibrilla… | 10.1093/eurheartj/ehaa612 |
| 9 | None | 2020 | Dementia prevention, intervention, and care: 2020 report of the Lancet … | 10.1016/s0140-6736(20)30367-6 |
| 10 | None | 2020 | Remote cognitive assessment approaches in the Dominantly Inherited Alzh… | 10.1002/alz.038144 |
| 11 | None | 2019 | The Amazon rain forest plant Uncaria tomentosa (cat’s claw) and its spe… | 10.1038/s41598-019-38645-0 |
| 12 | None | 2021 | Neuroprotective Herbs for the Management of Alzheimer’s Disease | 10.3390/biom11040543 |
| 13 | None | 2021 | Tau and Membranes: Interactions That Promote Folding and Condensation | 10.3389/fcell.2021.725241 |
| 14 | None | 2021 | In vitro comparison of major memory-support dietary supplements for the… | 10.1038/s41598-020-79275-1 |
| 15 | None | 2022 | In Silico Analysis of Metabolites from Peruvian Native Plants as Potent… | 10.3390/molecules27030918 |
