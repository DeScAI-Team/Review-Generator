# Evidence audit trail

**Document:** De Novo Protein Binder Design for Advanced Glycation End Products A Computational Approach to Targeting Age-Related Glyc  
**Review date:** May 21, 2026  
**Composite score:** 0.4142  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T02:51:59Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `e5eff0ed57300361` |
| retrieve_compare_llm.json | `28c10f03e65171ee` |
| screener.json | `fe1379c9b490b155` |
| originality.json | `eec172fbbe4a63c0` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.2500 | evidence_grade_weighted | claim_count=10 |
| execution_credibility | 0.3179 | evidence_grade_weighted | claim_count=3 |
| financial_integrity | 0.5000 | evidence_grade_weighted | claim_count=0 |
| originality | 0.7704 | literature_similarity | compared_works=152 |
| real_world_traction | 0.3500 | evidence_grade_weighted | claim_count=2 |
| scientific_rigor | 0.3470 | evidence_grade_weighted | claim_count=46 |
| team_credibility | 0.3500 | evidence_grade_weighted | claim_count=1 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** self_reported: 1
- **evidential_strength:** self_reported_method: 5; unsupported: 3; self_reported: 2
- **execution_credibility:** unreferenced: 2; unsupported: 1
- **governance_accountability:** self_reported_method: 1
- **originality:** unsupported: 6; unreferenced: 4; moderate: 1; self_reported: 1; self_reported_method: 1; strong: 1
- **real_world_traction:** unreferenced: 2
- **scientific_rigor:** self_reported_method: 31; unsupported: 8; unreferenced: 4; weak: 2; moderate: 1; self_reported: 1
- **team_credibility:** unreferenced: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### team_credibility / aspirational · chunk 29 · Author Contributions

**Grade:** `unreferenced`  

> K.A.Y. conceived and designed the study, will perform all computational and experimental work, analyze the data, and write the manuscript.

### scientific_rigor / methodological · chunk 5 · Research Question: Background, Importance, and Relevance

**Grade:** `moderate`  

> Such binders would serve as research tools for detecting and quantifying specific AGE species, and as scaffolds for downstream enzyme design to actively degrade AGEs.

**References:**

- [6] 10.1038/s41586-023-06415-8 → partial support — This reference supports the claim regarding the use of AI for designing protein binders and scaffolds for enzyme active sites, as it explicitly mentions 'prote…
- [7] 10.1126/science.adl2528 → partial support — This reference supports the methodological claim of designing binders around small molecules (which could include AGEs) using RFdiffusionAA, but it does not ad…

### scientific_rigor / contextual · chunk 3 · Research Question: Background, Importance, and Relevance

**Grade:** `weak`  

> AGE cross-links increase tissue stiffness and reduce turnover in long-lived extracellular matrix proteins like collagen.

**References:**

- [1] 10.1007/s12551-024-01188-4 → partial support — The abstract confirms that AGEs form on long-life biomolecules and affect protein structure/function, but it does not explicitly state that this results in inc…
- [2] 10.3390/antiox14040492 → partial support — The abstract mentions that pathologies involve 'direct protein cross-linking,' which supports the mechanism, but it lacks specific evidence regarding the resul…

### scientific_rigor / contextual · chunk 5 · Research Question: Background, Importance, and Relevance

**Grade:** `weak`  

> Unlike small molecules, designed proteins can achieve high affinity and specificity through extensive complementary surfaces.

**References:**

- [6] 10.1038/s41586-023-06415-8 → partial support — The abstract confirms that RFdiffusion enables the design of protein binders with high accuracy (validated by cryo-EM), which implies the achievement of high a…
- [7] 10.1126/science.adl2528 → not relevant — This reference focuses on extending protein design to include small molecules, nucleic acids, and metals using an all-atom representation. It does not provide …

### scientific_rigor / aspirational · chunk 1 · ABSTRACT

**Grade:** `unreferenced`  

> The top 100 -200 computational designs will be validated experimentally through yeast surface display screening against CML-modified bovine serum albumin, and top candidates will undergo binding affinity characterization by biolayer interferometry.

### scientific_rigor / aspirational · chunk 4 · Research Question: Background, Importance, and Relevance

**Grade:** `unsupported`  

> None have achieved regulatory approval for AGE-related indications.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The abstract discusses the chemistry, formation, and pathophysiological roles of AGEs in various diseases but contains no information regarding the regulatory …
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H2: At least one computationally designed binder will show measurable binding to CMLmodified bovine serum albumin (AGE-BSA) in yeast surface display screening, defined as a signal-to-background ratio greater than 3.

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on the chemistry, formation, and biological effects of AGEs; it provides no data on computationally designed binders, yeast …

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H3: Top binder candidates will exhibit sub-micromolar affinity for AGE-BSA as measured by biolayer interferometry (BLI).

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on AGEs, their formation, and receptors, but it does not contain specific data on binder affinity measurements, biolayer int…

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H1 is the primary outcome as it establishes the foundational feasibility of the computational approach.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference is a review article focused on the biochemistry and pathology of Advanced Glycation End-Products (AGEs), whereas the claim concerns the feasibili…

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H2 constitutes the primary experimental outcome, since yeast display screening is the initial gate for identifying active binders.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference discusses Advanced Glycation End-Products (AGEs) and their role in diseases like diabetes and cancer, whereas the claim concerns yeast display sc…

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H3 is a secondary outcome that characterizes the quality of candidates passing the primary screen.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference discusses Advanced Glycation End-Products (AGEs) and their role in diseases like diabetes and cancer, which has no logical connection to the clai…

### scientific_rigor / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> In the event no binding is detected in the initial yeast display screen, contingent analyses are pre-specified in the Methods section.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference discusses Advanced Glycation End-Products (AGEs) and their role in diseases like diabetes and cancer, which has no connection to yeast display sc…

### scientific_rigor / aspirational · chunk 17 · Primary Analysis

**Grade:** `unreferenced`  

> The primary outcome is the fraction of designs showing a binding signal above background in yeast surface display (hit rate).

### scientific_rigor / aspirational · chunk 17 · Primary Analysis

**Grade:** `unreferenced`  

> The hit rate and its 95% Wilson confidence interval will be reported.

### scientific_rigor / aspirational · chunk 18 · Secondary Analyses

**Grade:** `unreferenced`  

> Affinity distribution of BLI-validated hits, reported as KD values with 95% confidence intervals from curve fitting.

### scientific_rigor / aspirational · chunk 20 · Pilot Data

**Grade:** `unsupported`  

> No wet laboratory pilot data has been generated, which is appropriate given the exploratory nature of this project and the absence of prior art applying RFdiffusion All-Atom to AGE targets.

**References:**

- [7] 10.1126/science.adl2528 → overclaim — The abstract explicitly states that RFdiffusion All-Atom was 'experimentally validated' through crystallography and binding measurements for specific targets, …

### originality / aspirational · chunk 2 · ABSTRACT

**Grade:** `unreferenced`  

> This work represents the first application of RFdiffusion All-Atom to AGE targeting and will establish whether computationally designed protein binders can serve as a new class of anti-glycation therapeutics.

### originality / aspirational · chunk 4 · Research Question: Background, Importance, and Relevance

**Grade:** `unsupported`  

> None have achieved regulatory approval for AGE-related indications.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The abstract discusses the chemistry, formation, and pathophysiological roles of AGEs in various diseases but contains no information regarding the regulatory …
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 5 · Research Question: Background, Importance, and Relevance

**Grade:** `strong`  

> No group has yet applied this technology to AGE targeting.

**References:**

- [6] 10.1038/s41586-023-06415-8 → not relevant — This reference describes the development of RFdiffusion for general protein design (binders, enzymes, symmetric assemblies) but does not mention the specific a…
- [7] 10.1126/science.adl2528 → not relevant — This reference details the extension of RFdiffusion to include small molecules (digoxigenin, heme, bilin) but fails to cite any application of the technology s…

### originality / aspirational · chunk 5 · Research Question: Background, Importance, and Relevance

**Grade:** `moderate`  

> This project proposes a novel strategy: designing de novo protein binders that recognize and sequester specific AGE adducts.

**References:**

- [6] 10.1038/s41586-023-06415-8 → partial support — This reference establishes the feasibility of de novo protein binder design using RFdiffusion, which is a core component of the proposed strategy. However, it …
- [7] 10.1126/science.adl2528 → partial support — This reference demonstrates the capability to design proteins that bind specific small molecules and covalent modifications (like heme and digoxigenin) using R…

### originality / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> This study will test three preregistered hypotheses: H1: RFdiffusion All-Atom can generate protein scaffolds with designed binding pockets for CML (the most abundant AGE species).

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on the chemistry, classification, and disease associations of AGEs; it does not contain any data or discussion regarding RFd…

### originality / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H2: At least one computationally designed binder will show measurable binding to CMLmodified bovine serum albumin (AGE-BSA) in yeast surface display screening, defined as a signal-to-background ratio greater than 3.

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on the chemistry, formation, and biological effects of AGEs; it provides no data on computationally designed binders, yeast …

### originality / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H3: Top binder candidates will exhibit sub-micromolar affinity for AGE-BSA as measured by biolayer interferometry (BLI).

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on AGEs, their formation, and receptors, but it does not contain specific data on binder affinity measurements, biolayer int…

### originality / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H1 is the primary outcome as it establishes the foundational feasibility of the computational approach.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference is a review article focused on the biochemistry and pathology of Advanced Glycation End-Products (AGEs), whereas the claim concerns the feasibili…

### originality / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H3 is a secondary outcome that characterizes the quality of candidates passing the primary screen.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference discusses Advanced Glycation End-Products (AGEs) and their role in diseases like diabetes and cancer, which has no logical connection to the clai…

### originality / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> If H2 and H3 are supported (binding detected with sub-micromolar affinity), this will establish proof-of-concept for a new class of AGE-targeting protein therapeutics and produce binder sequences that can be optimized through directed evolution.

### originality / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> This would represent the first demonstration that computationally designed proteins can specifically engage a posttranslational glycation modification, advancing both the therapeutic and research tool landscape for aging biology.

### originality / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> If binding is not achieved (H2 not supported), the negative results will inform the field about the challenges of designing binders for post-translationally modified amino acids and guide future computational approaches.

### evidential_strength / empirical · chunk 5 · Research Question: Background, Importance, and Relevance

**Grade:** `unsupported`  

> A designed AGE binder could function therapeutically by intercepting circulating AGEs before they engage RAGE or cross-link tissue proteins.

**References:**

- [6] 10.1038/s41586-023-06415-8 → tangential — This reference demonstrates the capability to design protein binders using RFdiffusion but does not provide evidence regarding the therapeutic mechanism of int…
- [7] 10.1126/science.adl2528 → tangential — While this reference shows the ability to design proteins around small molecules, it focuses on non-AGE targets (digoxigenin, heme, bilin) and lacks any discus…

### evidential_strength / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H2: At least one computationally designed binder will show measurable binding to CMLmodified bovine serum albumin (AGE-BSA) in yeast surface display screening, defined as a signal-to-background ratio greater than 3.

**References:**

- [3] 10.3390/cells11081312 → not relevant — This reference is a general review on the chemistry, formation, and biological effects of AGEs; it provides no data on computationally designed binders, yeast …

### evidential_strength / aspirational · chunk 20 · Pilot Data

**Grade:** `unsupported`  

> No wet laboratory pilot data has been generated, which is appropriate given the exploratory nature of this project and the absence of prior art applying RFdiffusion All-Atom to AGE targets.

**References:**

- [7] 10.1126/science.adl2528 → overclaim — The abstract explicitly states that RFdiffusion All-Atom was 'experimentally validated' through crystallography and binding measurements for specific targets, …

### execution_credibility / aspirational · chunk 6 · Hypotheses

**Grade:** `unsupported`  

> H1 is the primary outcome as it establishes the foundational feasibility of the computational approach.

**References:**

- [3] 10.3390/cells11081312 → not relevant — The reference is a review article focused on the biochemistry and pathology of Advanced Glycation End-Products (AGEs), whereas the claim concerns the feasibili…

### execution_credibility / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> Either outcome has direct implications for the feasibility of protein-based anti-AGE interventions.

### execution_credibility / aspirational · chunk 26 · Study Status

**Grade:** `unreferenced`  

> The full design generation campaign and all experimental work described in this protocol will commence following Stage 1 peer review approval.

### real_world_traction / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> These findings will contribute to the literature on de novo protein design benchmarks and to the aging intervention field.

### real_world_traction / aspirational · chunk 24 · Interpreting Results

**Grade:** `unreferenced`  

> Successful development of anti-AGE biologics could eventually inform therapeutic strategies for diabetes complications and age-related diseases.

## Document screener

- **financial_integrity** (concern) · *abstract*
  - Quote: All computational designs, experimental protocols, and raw data will be made openly available.
  - Observation: While the paper promises open data, there is no explicit statement regarding funding sources, grants, or financial support in this window. For a project involving gene synthesis, yeast display, and BLI assays, the absence of a funding disclosure is notable.

- **financial_integrity** (concern) · *funding*
  - Quote: Cloud GPU computing costs (≈1,000 USD) will be funded from discretionary postdoctoral research funds. This work is also supported by a ResearchHub Foundation grant.
  - Observation: The project relies on 'discretionary postdoctoral research funds' for significant computational costs (~$1k) rather than dedicated grant funding. This suggests the work may be under-resourced or dependent on the PI's personal lab budget, which could limit the scale of the experi…

- **originality** (info) · *abstract*
  - Quote: This work represents the first application of RFdiffusion All-Atom to AGE targeting and will establish whether computationally designed protein binders can serve as a new class of anti-glycation ther…
  - Observation: The authors explicitly claim this is the first application of a specific deep learning tool (RFdiffusion All-Atom) to a specific target class (AGEs), positioning the work as a novel proof-of-concept rather than incremental optimization.

- **scientific_rigor** (concern) · *sample and statistical power*
  - Quote: No covariates or regressors are anticipated for primary analyses.
  - Observation: The plan to perform no covariate adjustment in primary analyses is risky. In yeast display and BLI experiments, batch effects, instrument drift, or operator differences are common confounders. Failing to plan for these statistically could lead to false positives or inflated effe…

- **scientific_rigor** (info) · *pilot data*
  - Quote: No wet laboratory pilot data has been generated, which is appropriate given the exploratory nature of this project
  - Observation: The authors admit to a lack of wet-lab pilot data, justifying it only by the 'exploratory nature' of the project. This is a significant methodological gap for a study claiming to validate a new computational pipeline against a specific target (AGEs), as wet-lab feasibility (e.g.…

- **team_credibility** (info) · *author affiliations*
  - Quote: Stanford University, Department of Neurology (Tony Wyss-Coray Lab). University of Washington, Institute for Protein Design (David Baker Lab)
  - Observation: The authors are affiliated with two of the most prominent labs in protein design and neurodegeneration research (Baker and Wyss-Coray). This signals high technical capability for the proposed computational pipeline and relevant domain expertise for the target disease area.

## Originality (literature overlap)

**Originality score:** 0.7704 · **Related works retrieved:** 152 · **Avg similarity:** 0.2296

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | 0.9800 | 2026 | De Novo Protein Binder Design for Advanced Glycation End Products: A Co… | 10.55277/rhj.qm7p5g89.2 |
| 2 | 0.9800 | 2026 | De Novo Protein Binder Design for Advanced Glycation End Products: A Co… | 10.55277/researchhub.5r1a915k.1 |
| 3 | 0.9800 | 2026 | De Novo Protein Binder Design for Advanced Glycation End Products: A Co… | 10.55277/researchhub.a1qgt240.1 |
| 4 | 0.7800 | 2024 | Atomically accurate de novo design of antibodies with RFdiffusion | 10.1101/2024.03.14.585103 |
| 5 | 0.7800 | 2023 | De novo design of protein structure and function with RFdiffusion | 10.1038/s41586-023-06415-8 |
| 6 | 0.7200 | 2025 | Atom level enzyme active site scaffolding using RFdiffusion2 | 10.1101/2025.04.09.648075 |
| 7 | 0.6800 | 2023 | Generalized Biomolecular Modeling and Design with RoseTTAFold All-Atom | 10.1101/2023.10.09.561603 |
| 8 | 0.6800 | 2024 | Generalized biomolecular modeling and design with RoseTTAFold All-Atom | 10.1126/science.adl2528 |
| 9 | 0.6600 | 2024 | Accurate structure prediction of biomolecular interactions with AlphaFo… | 10.1038/s41586-024-07487-w |
| 10 | 0.6500 | 2024 | Target-Specific <i>De Novo</i> Peptide Binder Design with DiffPepBuilder | 10.1021/acs.jcim.4c00975 |
| 11 | 0.6200 | 2023 | De novo design of high-affinity binders of bioactive helical peptides | 10.1038/s41586-023-06953-1 |
| 12 | 0.5800 | 2025 | Atomic context-conditioned protein sequence design using LigandMPNN | 10.1038/s41592-025-02626-1 |
| 13 | 0.5500 | 1994 | Cellular receptors for advanced glycation end products. Implications fo… | 10.1161/01.atv.14.10.1521 |
| 14 | 0.5200 | 2023 | In silico evolution of autoinhibitory domains for a PD-L1 antagonist us… | 10.1073/pnas.2307371120 |
| 15 | 0.5200 | 1992 | Maillard Reaction-Mediated Molecular Damage to Extracellular Matrix and… | 10.2337/diab.41.2.s36 |
