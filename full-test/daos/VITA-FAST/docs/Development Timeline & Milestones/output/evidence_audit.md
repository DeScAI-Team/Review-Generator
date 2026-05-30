# Evidence audit trail

**Document:** vitafast-202512updates  
**Review date:** May 22, 2026  
**Composite score:** 0.5117  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:21:00Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `111f8337f94ddb67` |
| retrieve_compare_llm.json | `41772bede479e316` |
| screener.json | `23e2c337034c355d` |
| originality.json | `f04f18b2cee7c6fe` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3608 | evidence_grade_weighted | claim_count=13 |
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=9 |
| financial_integrity | 0.5000 | evidence_grade_weighted | claim_count=0 |
| originality | 1.0000 | literature_similarity | compared_works=222 |
| real_world_traction | 0.3827 | evidence_grade_weighted | claim_count=2 |
| scientific_rigor | 0.3628 | evidence_grade_weighted | claim_count=57 |
| team_credibility | 0.5000 | evidence_grade_weighted | claim_count=0 |

## Evidence grade counts (retrieve_compare)

- **evidential_strength:** unreferenced: 7; self_reported: 2; self_reported_method: 2; unverifiable: 2
- **execution_credibility:** unreferenced: 8; self_reported: 1; self_reported_method: 1
- **governance_accountability:** self_reported_method: 2; unreferenced: 1
- **originality:** unreferenced: 13; unverifiable: 4; self_reported_method: 1
- **real_world_traction:** unreferenced: 1; unverifiable: 1
- **scientific_rigor:** unreferenced: 32; unverifiable: 11; self_reported_method: 9; self_reported: 6

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### scientific_rigor / empirical · chunk 2 · Project Overview & Scientific Foundation

**Grade:** `unreferenced`  

> Small molecules that activate autophagy and restore lysosomal function, rescuing cell survival in models with lysosomal dysfunction (Npc1-/-) but not in cells lacking autophagy initiation (Atg5-/-).

### scientific_rigor / empirical · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Pilot screening of FDA-approved drug library identified 12 previously unknown autophagy inducers

### scientific_rigor / empirical · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Multiple hit series with autophagy-activating signatures identified

### scientific_rigor / empirical · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> VitaFAST's approach targets downstream autophagy activation and lysosomal function rescue, distinct from mTOR inhibitors (rapamycin and rapalogs)

### scientific_rigor / empirical · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> Lead compounds exhibit 10-100x higher potency than earlier series.

### scientific_rigor / empirical · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> The mechanism directly addresses the autophagy-NAD axis identified by the Korolchuk lab.

### scientific_rigor / contextual · chunk 1 · Project Overview & Scientific Foundation

**Grade:** `unverifiable`  

> Lysosomal storage disorders (LSDs) collectively have an estimated frequency of approximately 1 in 5,000 live births.

**References:**

- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)
- [2025] ? → (no verdict — missing abstract)
- [2032] ? → (no verdict — missing abstract)
- [2033] ? → (no verdict — missing abstract)
- [2034] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 1 · Project Overview & Scientific Foundation

**Grade:** `unverifiable`  

> The entire aging population experiences autophagy decline, suggesting universal applicability for longevity interventions.

**References:**

- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)
- [2025] ? → (no verdict — missing abstract)
- [2032] ? → (no verdict — missing abstract)
- [2033] ? → (no verdict — missing abstract)
- [2034] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 1 · Project Overview & Scientific Foundation

**Grade:** `unverifiable`  

> Autophagy dysfunction plays a key pathological role in Alzheimer's disease and Parkinson's disease.

**References:**

- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)
- [2025] ? → (no verdict — missing abstract)
- [2032] ? → (no verdict — missing abstract)
- [2033] ? → (no verdict — missing abstract)
- [2034] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Commercially available compounds binding these targets validated as potent autophagy inducers

### scientific_rigor / contextual · chunk 15 · Experimental Evidence

**Grade:** `unreferenced`  

> Two lead repurposing molecules that have been through Phase 1 trials and are highly potent in lab assays of autophagy

### scientific_rigor / contextual · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> Autophagy has an evolutionarily conserved role in NAD preservation

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> Metabolic function of autophagy is essential for cell survival

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> There is a crosstalk of NAD, ROS and autophagy in cellular health and ageing

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 0 · Project Overview & Scientific Foundation

**Grade:** `unreferenced`  

> Compounds are identified via high-throughput phenotypic screening in autophagy-deficient cell models and optimized as first-in-class autophagy activators for aging and lysosomal storage disorders.

### scientific_rigor / aspirational · chunk 3 · Autophagy-lysosome pathway

**Grade:** `unreferenced`  

> Testing new chemical entities in vitro, also exploring the feasibility of a drug repurposing clinical trial

### scientific_rigor / aspirational · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Two novel targets identified - previously proposed longevity targets

### scientific_rigor / aspirational · chunk 7 · Team Information

**Grade:** `unreferenced`  

> The study focuses on autophagy and lysosomal biology, cellular homeostasis and neurodegeneration, high-throughput screening and assay development, organic and medicinal chemistry, SAR and drug discovery, computational chemistry, and translational longevity therapeutics.

### scientific_rigor / aspirational · chunk 10 · Filed IP

**Grade:** `unreferenced`  

> Repurposing claims for commercially available compounds as autophagy activators

### scientific_rigor / aspirational · chunk 10 · Filed IP

**Grade:** `unreferenced`  

> Methods of use for treating lysosomal storage disorders via autophagy activation

### scientific_rigor / aspirational · chunk 10 · Filed IP

**Grade:** `unreferenced`  

> Methods of use for longevity and age-related disease treatment

### scientific_rigor / aspirational · chunk 11 · Planned claims to cover:

**Grade:** `unreferenced`  

> The study addresses composition of matter for novel autophagy-activating small molecules.

### scientific_rigor / aspirational · chunk 11 · Planned claims to cover:

**Grade:** `unreferenced`  

> The study addresses methods of use for treating lysosomal storage disorders via autophagy activation.

### scientific_rigor / aspirational · chunk 11 · Planned claims to cover:

**Grade:** `unreferenced`  

> The study addresses methods of use for longevity and age-related disease treatment.

### scientific_rigor / aspirational · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> Key competitors (rapamycin, everolimus) work via mTOR inhibition - VitaFAST compounds work via distinct, newly identified targets

### scientific_rigor / aspirational · chunk 14 · Experimental Evidence

**Grade:** `unreferenced`  

> Mouse embryonic fibroblasts (MEFs) with Npc1 knockout (Npc1-/-) modelling lysosomal dysfunction associated with NPC and Parkinson's disease.

### scientific_rigor / aspirational · chunk 18 · IND Readiness

**Grade:** `unreferenced`  

> The study includes a demonstration of the synthesis approach and scale-up.

### scientific_rigor / aspirational · chunk 19 · For novel NCEs:

**Grade:** `unreferenced`  

> SAR-driven optimization yielding drug-like molecules

### scientific_rigor / aspirational · chunk 20 · For repurposed compounds:

**Grade:** `unreferenced`  

> Manufacturing timeline and cost identified as key risk factors

### scientific_rigor / aspirational · chunk 22 · Secondary indications - Longevity/aging:

**Grade:** `unverifiable`  

> Autophagy inducers represent emerging subsegment with significant growth potential

**References:**

- [2023] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 23 · Broader indications - Neurodegeneration:

**Grade:** `unverifiable`  

> Autophagy dysfunction is implicated in both Alzheimer's disease and Parkinson's disease.

**References:**

- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Rapamycin and rapalogs (sirolimus, everolimus, temsirolimus) are FDA-approved mTOR inhibitors with a well-established mechanism but significant side effects including immunosuppression, and they work by inhibiting mTOR upstream of autophagy.

### scientific_rigor / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Miglustat (Zavesca/Brazaves) is approved for Niemann-Pick disease type C in the EU and Japan (not the US) as a substrate reduction therapy with limited efficacy in clinical use.

### scientific_rigor / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Cyclodextrins (Trappsol Cyclo, Kleptose HPB) are used under compassionate use protocols for Niemann-Pick disease type C and target cholesterol clearance rather than autophagy directly.

### scientific_rigor / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Metformin is an AMPK activator whose autophagy-inducing effects are secondary to its metabolic mechanism.

### scientific_rigor / aspirational · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> No approved drugs currently exist that specifically target autophagy activation for longevity.

### scientific_rigor / aspirational · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> The autophagy-NAD axis has therapeutic implications for longevity and disease

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 28 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> Human neuronal validation of autophagy-NAD axis.

**References:**

- [2023] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 32 · Platform Potential:______________ Additional indications or broader technology applications

**Grade:** `unreferenced`  

> The VitaFAST autophagy activation platform has broad applicability across neurodegeneration, lysosomal storage disorders, metabolic diseases, aging, and cancer.

### scientific_rigor / aspirational · chunk 32 · Platform Potential:______________ Additional indications or broader technology applications

**Grade:** `unreferenced`  

> In cancer, the VitaFAST platform may have context-dependent application involving autophagy-dependent cell death.

### scientific_rigor / aspirational · chunk 32 · Platform Potential:______________ Additional indications or broader technology applications

**Grade:** `unreferenced`  

> Combination approaches with NAD+ precursors, sirtuin activators, or other geroprotectors show potential synergy with the VitaFAST platform.

### scientific_rigor / aspirational · chunk 34 · Team publications:

**Grade:** `unverifiable`  

> The autophagy-NAD axis in longevity and disease

**References:**

- [56] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 36 · Planned publications:

**Grade:** `unreferenced`  

> The study focuses on novel autophagy-activating compounds and target identification.

### originality / empirical · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Pilot screening of FDA-approved drug library identified 12 previously unknown autophagy inducers

### originality / empirical · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> Two newly identified targets represent novel mechanism of action for autophagy activation

### originality / aspirational · chunk 0 · Project Overview & Scientific Foundation

**Grade:** `unreferenced`  

> Compounds are identified via high-throughput phenotypic screening in autophagy-deficient cell models and optimized as first-in-class autophagy activators for aging and lysosomal storage disorders.

### originality / aspirational · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Two novel targets identified - previously proposed longevity targets

### originality / aspirational · chunk 10 · Filed IP

**Grade:** `unreferenced`  

> Repurposing claims for commercially available compounds as autophagy activators

### originality / aspirational · chunk 11 · Planned claims to cover:

**Grade:** `unreferenced`  

> The study addresses novel target applications for autophagy induction.

### originality / aspirational · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> Key competitors (rapamycin, everolimus) work via mTOR inhibition - VitaFAST compounds work via distinct, newly identified targets

### originality / aspirational · chunk 21 · Commercial Viability

**Grade:** `unverifiable`  

> Strong unmet need for therapies that restore lysosomal function at the cellular level

**References:**

- [2024] ? → (no verdict — missing abstract)
- [2025] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 22 · Secondary indications - Longevity/aging:

**Grade:** `unverifiable`  

> Autophagy inducers represent emerging subsegment with significant growth potential

**References:**

- [2023] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Miglustat (Zavesca/Brazaves) is approved for Niemann-Pick disease type C in the EU and Japan (not the US) as a substrate reduction therapy with limited efficacy in clinical use.

### originality / aspirational · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> Direct autophagy activation occurs via newly identified targets distinct from mTOR inhibition.

### originality / aspirational · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> No approved drugs currently exist that specifically target autophagy activation for longevity.

### originality / aspirational · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> NAD preservation via autophagy protects against cell death in Niemann-Pick type C1 disease models

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 32 · Platform Potential:______________ Additional indications or broader technology applications

**Grade:** `unreferenced`  

> The VitaFAST autophagy activation platform has broad applicability across neurodegeneration, lysosomal storage disorders, metabolic diseases, aging, and cancer.

### originality / aspirational · chunk 34 · Team publications:

**Grade:** `unverifiable`  

> Targeting the autophagy-NAD axis protects against cell death in Niemann-Pick type C1 disease models

**References:**

- [56] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 35 · Conference presentations:

**Grade:** `unreferenced`  

> The study addresses gaps in community-driven scientific engagement through VitaDAO community calls and scientific presentations.

### originality / aspirational · chunk 36 · Planned publications:

**Grade:** `unreferenced`  

> The study focuses on novel autophagy-activating compounds and target identification.

### real_world_traction / contextual · chunk 1 · Project Overview & Scientific Foundation

**Grade:** `unverifiable`  

> The entire aging population experiences autophagy decline, suggesting universal applicability for longevity interventions.

**References:**

- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)
- [2025] ? → (no verdict — missing abstract)
- [2032] ? → (no verdict — missing abstract)
- [2033] ? → (no verdict — missing abstract)
- [2034] ? → (no verdict — missing abstract)

### real_world_traction / aspirational · chunk 35 · Conference presentations:

**Grade:** `unreferenced`  

> The study addresses gaps in community-driven scientific engagement through VitaDAO community calls and scientific presentations.

### execution_credibility / aspirational · chunk 3 · Autophagy-lysosome pathway

**Grade:** `unreferenced`  

> Testing new chemical entities in vitro, also exploring the feasibility of a drug repurposing clinical trial

### execution_credibility / aspirational · chunk 6 · Upcoming milestones:

**Grade:** `unreferenced`  

> The study outlines a future direction involving drug repurposing trial scoping, regulatory pre-submission, CMC planning, and clinical protocol drafting between Q4 2025 and Q1 2026.

### execution_credibility / aspirational · chunk 6 · Upcoming milestones:

**Grade:** `unreferenced`  

> A future direction includes conducting IND-enabling studies, specifically murine safety experiments, for novel lead compounds in 2026.

### execution_credibility / aspirational · chunk 6 · Upcoming milestones:

**Grade:** `unreferenced`  

> A potential future direction is the initiation of a Phase 2 clinical trial for a repurposed compound pathway between 2026 and 2027.

### execution_credibility / aspirational · chunk 8 · Patent Application Status:______________

**Grade:** `unreferenced`  

> New patent applications planned for novel compounds developed through SAR optimization targeting H2 2025.

### execution_credibility / aspirational · chunk 8 · Patent Application Status:______________

**Grade:** `unreferenced`  

> Application IP filed 2nd Dec 2025 for repurposed compounds for autophagy induction and longevity use.

### execution_credibility / aspirational · chunk 20 · For repurposed compounds:

**Grade:** `unreferenced`  

> Manufacturing timeline and cost identified as key risk factors

### execution_credibility / aspirational · chunk 30 · Pharmacodynamic biomarkers:

**Grade:** `unreferenced`  

> Blood autophagy/mitophagy biomarkers are planned for clinical pathway in UAE

### evidential_strength / empirical · chunk 5 · Completed milestones:

**Grade:** `unreferenced`  

> Three lead compounds identified with 10-100x higher potency than previous series

### evidential_strength / empirical · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> VitaFAST's approach targets downstream autophagy activation and lysosomal function rescue, distinct from mTOR inhibitors (rapamycin and rapalogs)

### evidential_strength / empirical · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> Two newly identified targets represent novel mechanism of action for autophagy activation

### evidential_strength / empirical · chunk 13 · Favorable FTO position with key considerations:

**Grade:** `unreferenced`  

> Strong differentiation from existing therapeutic approaches for NPC (miglustat, cyclodextrins)

### evidential_strength / empirical · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> Compounds rescue lysosomal dysfunction specifically rather than merely initiating autophagy.

### evidential_strength / empirical · chunk 25 · VitaFAST differentiation:

**Grade:** `unreferenced`  

> The mechanism directly addresses the autophagy-NAD axis identified by the Korolchuk lab.

### evidential_strength / empirical · chunk 27 · Key foundational publications from Korolchuk Lab:

**Grade:** `unverifiable`  

> Autophagy promotes cell survival by maintaining NAD levels

**References:**

- [2020] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### evidential_strength / empirical · chunk 34 · Team publications:

**Grade:** `unverifiable`  

> Autophagy promotes cell survival by maintaining NAD levels

**References:**

- [56] ? → (no verdict — missing abstract)
- [2022] ? → (no verdict — missing abstract)
- [2023] ? → (no verdict — missing abstract)
- [2024] ? → (no verdict — missing abstract)

### evidential_strength / aspirational · chunk 24 · Key competitors in autophagy modulation:

**Grade:** `unreferenced`  

> Metformin is an AMPK activator whose autophagy-inducing effects are secondary to its metabolic mechanism.

### governance_accountability / aspirational · chunk 6 · Upcoming milestones:

**Grade:** `unreferenced`  

> A future direction includes conducting IND-enabling studies, specifically murine safety experiments, for novel lead compounds in 2026.

## Document screener

- **financial_integrity** (concern) · *funding status*
  - Quote: VITA-FAST Token crowdsale: 1700%+ oversubscribed, ~$620K in bids, ~$32K target sale
  - Observation: Funding is derived from a token crowdsale with a massive oversubscription (1700%) and a specific 'target sale' mechanism. This suggests a community-driven incentive structure where early adopters may be financially incentivized to support the project's success, potentially intro…

- **financial_integrity** (concern) · *intellectual property status*
  - Quote: IP-NFT registered on Molecule protocol, tokenized as VITA-FAST IP Tokens (first DeSci fractionalized IPT)
  - Observation: The project utilizes a 'DeSci' model where IP is tokenized as NFTs. This introduces a novel incentive structure where ownership and potentially value are tied to tokens rather than traditional equity or grant funding. The lack of detail on how these tokens are distributed, trade…

- **financial_integrity** (info) · *funding status*
  - Quote: VFDP-14 ($30K repurposing scoping), VFDP-15 (modified H2 2025 plan)
  - Observation: The budget breakdown shows specific line items for 'repurposing scoping' and 'modified' future plans, indicating an adaptive, iterative funding approach. While not a red flag, it suggests the project scope is fluid and dependent on ongoing governance approvals rather than a fixe…

- **originality** (info) · *intellectual property status*
  - Quote: IP-NFT registered on Molecule protocol, tokenized as VITA-FAST IP Tokens (first DeSci fractionalized IPT)
  - Observation: The project claims to be the 'first DeSci fractionalized IPT'. While this is a novelty assertion regarding the *business model* of IP management, it does not necessarily reflect scientific novelty in the therapeutic mechanism itself, which is described as targeting known pathway…

- **scientific_rigor** (info) · *mechanism of action*
  - Quote: Small molecules that activate autophagy and restore lysosomal function, rescuing cell survival in models with lysosomal dysfunction (Npc1-/-) but not in cells lacking autophagy initiation (Atg5-/-).
  - Observation: The mechanism description explicitly uses negative controls (Atg5-/-) to validate specificity. This is a strong methodological signal, but the brevity of the description in this overview document suggests the full experimental design and statistical power analysis are absent fro…

- **team_credibility** (info) · *author affiliations*
  - Quote: Dr. Jóhannes Reynisson (Keele University) providing drug discovery and SAR analysis
  - Observation: The document explicitly lists a second key scientist (Dr. Reynisson) with a specific role in drug discovery and SAR analysis, alongside the primary PI. This signals a multi-expert team structure rather than a single-lab effort, which strengthens the technical feasibility of the …

- **team_credibility** (info) · *team information*
  - Quote: VitaDAO (decentralized longevity research collective)
  - Observation: The team includes a 'decentralized longevity research collective' (VitaDAO) alongside traditional academic institutions. While potentially a source of diverse input, this non-traditional affiliation structure lacks the standard oversight and track record verification of establis…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 222 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2016 | Mitochondrial Dynamics and Metabolic Regulation | 10.1016/j.tem.2015.12.001 |
| 2 | None | 2015 | Lysosomal storage and impaired autophagy lead to inflammasome activatio… | 10.1111/acel.12409 |
| 3 | None | 2021 | Hypoxia‐stimulated ATM activation regulates autophagy‐associated exosom… | 10.1002/jev2.12146 |
| 4 | None | 2007 | Linking of Autophagy to Ubiquitin-Proteasome System Is Important for th… | 10.2353/ajpath.2007.070188 |
| 5 | None | 2022 | Celastrol enhances transcription factor EB (TFEB)-mediated autophagy an… | 10.1016/j.apsb.2022.01.017 |
| 6 | None | 2019 | New insights into the interplay between autophagy, gut microbiota and i… | 10.1080/15548627.2019.1635384 |
| 7 | None | 2018 | Lysosomal membrane permeabilization and cell death | 10.1111/tra.12613 |
| 8 | None | 2019 | Lysosomes as a therapeutic target | 10.1038/s41573-019-0036-1 |
| 9 | None | 2016 | Autophagy, lipophagy and lysosomal lipid storage disorders | 10.1016/j.bbalip.2016.01.006 |
| 10 | None | 2023 | New insights into the autophagy-NAD axis in brain disease | 10.1016/j.celrep.2023.112420 |
| 11 | None | 2017 | Ferroptosis: A Regulated Cell Death Nexus Linking Metabolism, Redox Bio… | 10.1016/j.cell.2017.09.021 |
| 12 | None | 2020 | Interaction between microbiota and immunity in health and disease | 10.1038/s41422-020-0332-7 |
| 13 | None | 2021 | The cGAS–STING pathway as a therapeutic target in inflammatory diseases | 10.1038/s41577-021-00524-z |
| 14 | None | 2023 | Macrophages in immunoregulation and therapeutics | 10.1038/s41392-023-01452-1 |
| 15 | None | 2018 | Hallmarks of Cellular Senescence | 10.1016/j.tcb.2018.02.001 |
