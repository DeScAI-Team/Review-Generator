# Evidence audit trail

**Document:** fixing-broken-mitochondria-fissionbio  
**Review date:** May 22, 2026  
**Composite score:** 0.4923  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:05:14Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `0da1d61c61a2ebfb` |
| retrieve_compare_llm.json | `390bd98bbfab96ce` |
| screener.json | `fc032935264a0c97` |
| originality.json | `484d0cf549fb0012` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3595 | evidence_grade_weighted | claim_count=16 |
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=3 |
| financial_integrity | 0.5000 | evidence_grade_weighted | claim_count=0 |
| originality | 1.0000 | literature_similarity | compared_works=79 |
| real_world_traction | 0.3500 | evidence_grade_weighted | claim_count=4 |
| scientific_rigor | 0.3595 | evidence_grade_weighted | claim_count=28 |
| team_credibility | 0.3500 | evidence_grade_weighted | claim_count=2 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** unreferenced: 1
- **evidential_strength:** unreferenced: 9; self_reported_method: 3; self_reported: 2; unverifiable: 2
- **execution_credibility:** unreferenced: 3
- **governance_accountability:** unreferenced: 3
- **originality:** unreferenced: 6; self_reported_method: 2; self_reported: 1; unverifiable: 1
- **real_world_traction:** unreferenced: 4
- **scientific_rigor:** unreferenced: 14; self_reported_method: 8; self_reported: 3; unverifiable: 3
- **team_credibility:** unreferenced: 2

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### evidential_strength / empirical · chunk 3 · Mitochondrial Fission

**Grade:** `unreferenced`  

> Fission supports quality control by isolating and removing damaged parts.

### evidential_strength / empirical · chunk 4 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unreferenced`  

> During inflammatory stress, Drp1 interacts with the receptor Fis1, triggering excessive and damaging mitochondrial splitting while reducing fusion.

### evidential_strength / empirical · chunk 5 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unverifiable`  

> Chronic inflammation drives an abnormal Drp1-Fis1 interaction pathway in neurodegenerative diseases, which is particularly damaging compared to healthy fission processes.

**References:**

- [2016] ? → (no verdict — missing abstract)

### evidential_strength / empirical · chunk 6 · The P110 Breakthrough

**Grade:** `unreferenced`  

> P110 represents a fundamentally new therapeutic strategy that prevents the initial mitochondrial damage that triggers cellular dysfunction rather than boosting energy production or removing toxic proteins.

### evidential_strength / empirical · chunk 6 · The P110 Breakthrough

**Grade:** `unreferenced`  

> P110 prevents inflammatory stress-induced fission while allowing normal mitochondrial dynamics to continue through other Drp1 receptors (Mff, MiD49, MiD51).

### evidential_strength / empirical · chunk 7 · The P110 Breakthrough

**Grade:** `unverifiable`  

> Drp1/Fis1 interaction mediates mitochondrial dysfunction, bioenergetic failure and cognitive decline in Alzheimer's disease.

**References:**

- [9] ? → (no verdict — missing abstract)
- [10] ? → (no verdict — missing abstract)
- [123] ? → (no verdict — missing abstract)
- [126] ? → (no verdict — missing abstract)
- [2012] ? → (no verdict — missing abstract)
- [2013] ? → (no verdict — missing abstract)
- [2018] ? → (no verdict — missing abstract)

### evidential_strength / empirical · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> BioDAOs offer several compelling advantages for scientific development that traditional funding mechanisms cannot match.

### evidential_strength / aspirational · chunk 0 · Introducing FissionBio

**Grade:** `unreferenced`  

> Researchers have uncovered a common thread in diseases like Alzheimer's, ALS, and Huntington's: an interaction between the proteins Drp1 and Fis1 causing mitochondria to fragment excessively.

### evidential_strength / aspirational · chunk 0 · Introducing FissionBio

**Grade:** `unreferenced`  

> The study explores how mitochondrial imbalance can push neurons toward failure as a fundamental mechanism of neurodegeneration.

### evidential_strength / aspirational · chunk 2 · Mitochondrial Fusion

**Grade:** `unreferenced`  

> This process enables them to share resources, such as proteins and DNA, which helps repair damaged mitochondria by combining their contents with healthier ones.

### evidential_strength / aspirational · chunk 2 · Mitochondrial Fusion

**Grade:** `unreferenced`  

> Fusion also improves energy production by creating efficient networks to distribute power throughout the cell.

### scientific_rigor / empirical · chunk 4 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unreferenced`  

> The interaction between Drp1 and Fis1 creates a cellular environment characterized by fragmented, dysfunctional mitochondria.

### scientific_rigor / empirical · chunk 5 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unverifiable`  

> Chronic inflammation drives an abnormal Drp1-Fis1 interaction pathway in neurodegenerative diseases, which is particularly damaging compared to healthy fission processes.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / empirical · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> While SC9 demonstrated that small molecules can target the SWAG binding site and mimic P110's effects, it lacks the brain penetration needed for neurological applications.

### scientific_rigor / contextual · chunk 5 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unverifiable`  

> DRP1-dependent mitochondrial fission drives a range of diseases.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 0 · Introducing FissionBio

**Grade:** `unreferenced`  

> Researchers have uncovered a common thread in diseases like Alzheimer's, ALS, and Huntington's: an interaction between the proteins Drp1 and Fis1 causing mitochondria to fragment excessively.

### scientific_rigor / aspirational · chunk 0 · Introducing FissionBio

**Grade:** `unreferenced`  

> FissionBio is developing drugs targeting the interaction between Drp1 and Fis1 to stop excessive mitochondrial fragmentation at the source.

### scientific_rigor / aspirational · chunk 0 · Introducing FissionBio

**Grade:** `unreferenced`  

> The study explores how mitochondrial imbalance can push neurons toward failure as a fundamental mechanism of neurodegeneration.

### scientific_rigor / aspirational · chunk 1 · Understanding the Link Between Mitochondria and Disease

**Grade:** `unreferenced`  

> Every cell in your body contains hundreds or thousands of mitochondria, but nowhere are they more critical than in your brain.

### scientific_rigor / aspirational · chunk 1 · Understanding the Link Between Mitochondria and Disease

**Grade:** `unreferenced`  

> Neurons are energy-hungry cells that never stop working, requiring a constant supply of ATP (cellular fuel) to maintain electrical activity, transport materials, and repair themselves.

### scientific_rigor / aspirational · chunk 1 · Understanding the Link Between Mitochondria and Disease

**Grade:** `unreferenced`  

> In healthy cells, mitochondria maintain a delicate balance between two opposing processes: fusion and fission. This dynamic system allows mitochondria to adapt while maintaining optimal function.

### scientific_rigor / aspirational · chunk 2 · Mitochondrial Fusion

**Grade:** `unreferenced`  

> Mitochondrial fusion occurs when individual mitochondria merge into larger, interconnected networks.

### scientific_rigor / aspirational · chunk 5 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unverifiable`  

> Inhibition of Drp1/Fis1 interaction slows the progression of numerous diseases including Alzheimer's, ALS, Huntington's, Parkinson's, and cardiovascular disease, suggesting therapeutic benefits from targeting this protein interaction.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 8 · The P110 Breakthrough

**Grade:** `unreferenced`  

> Recent research has revealed the extensive therapeutic reach of P110 beyond ALS, demonstrating benefits in Parkinson's disease, stroke, inflammatory bowel disease, and sepsis.

### scientific_rigor / aspirational · chunk 8 · The P110 Breakthrough

**Grade:** `unreferenced`  

> Targeting the pathological Drp1-Fis1 interaction isn't just relevant for brain diseases but could be fundamental in treating inflammatory conditions throughout the body.

### scientific_rigor / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Traditional investors typically wait for later-stage data before committing resources, creating a gap that can stall breakthrough treatments for years.

### scientific_rigor / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> Successful compounds advance to Investigational New Drug (IND)-enabling studies comprehensive safety testing required before human clinical trials can begin.

### scientific_rigor / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> These studies generate the preclinical data that regulatory agencies, such as the FDA, require to approve first-in-human testing.

### originality / empirical · chunk 6 · The P110 Breakthrough

**Grade:** `unreferenced`  

> P110 represents a fundamentally new therapeutic strategy that prevents the initial mitochondrial damage that triggers cellular dysfunction rather than boosting energy production or removing toxic proteins.

### originality / aspirational · chunk 5 · How Mitochondrial Fission and Fusion Link to Brain Health

**Grade:** `unverifiable`  

> Inhibition of Drp1/Fis1 interaction slows the progression of numerous diseases including Alzheimer's, ALS, Huntington's, Parkinson's, and cardiovascular disease, suggesting therapeutic benefits from targeting this protein interaction.

**References:**

- [2016] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 8 · The P110 Breakthrough

**Grade:** `unreferenced`  

> Targeting the pathological Drp1-Fis1 interaction isn't just relevant for brain diseases but could be fundamental in treating inflammatory conditions throughout the body.

### originality / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Most promising research dies in the early stages, not because the science is bad, but because it can't attract the funding needed to prove its potential.

### originality / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Traditional investors typically wait for later-stage data before committing resources, creating a gap that can stall breakthrough treatments for years.

### originality / aspirational · chunk 12 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> BioDAOs bridge the gap between academic research and commercial development.

### originality / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> FissionBio is now developing third-generation compounds that build on this knowledge while achieving better drug properties, particularly brain penetration.

### governance_accountability / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Cerebrum DAO, a community-driven Decentralized Autonomous Organization (DAO) focused on ending brain diseases, addresses this problem by enabling individuals to fund promising scientific research directly.

### governance_accountability / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> These studies generate the preclinical data that regulatory agencies, such as the FDA, require to approve first-in-human testing.

### governance_accountability / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> Through Cerebrum DAO's projects, you can own stakes in the intellectual property that could change how we treat brain diseases.

### real_world_traction / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Cerebrum DAO, a community-driven Decentralized Autonomous Organization (DAO) focused on ending brain diseases, addresses this problem by enabling individuals to fund promising scientific research directly.

### real_world_traction / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> This model transforms how breakthrough treatments get funded and supported through translational research development.

### real_world_traction / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> Instead of waiting for pharmaceutical giants to recognize potential, patients, researchers, and supporters can directly back the science they believe in while sharing in the rewards of success.

### real_world_traction / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> Through Cerebrum DAO's projects, you can own stakes in the intellectual property that could change how we treat brain diseases.

### team_credibility / aspirational · chunk 11 · How Cerebrum DAO Accelerates Scientific Discovery

**Grade:** `unreferenced`  

> Cerebrum DAO, a community-driven Decentralized Autonomous Organization (DAO) focused on ending brain diseases, addresses this problem by enabling individuals to fund promising scientific research directly.

### team_credibility / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> Through Cerebrum DAO's projects, you can own stakes in the intellectual property that could change how we treat brain diseases.

### execution_credibility / aspirational · chunk 13 · What Comes Next

**Grade:** `unreferenced`  

> FissionBio has demonstrated that its scientific concept is effective in the laboratory.

### execution_credibility / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> Starting with the validated SWAG target and binding site, the team must develop entirely new molecules that can effectively treat brain diseases.

### execution_credibility / aspirational · chunk 14 · From Discovery to Medicine

**Grade:** `unreferenced`  

> The development process involves multiple stages: Hit identification, Lead optimization, Safety testing, Pharmacokinetics, and Disease model validation.

### cross_cutting / aspirational · chunk 15 · Community-Driven Progress

**Grade:** `unreferenced`  

> This model transforms how breakthrough treatments get funded and supported through translational research development.

## Document screener

- **financial_integrity** (concern) · *discussion*
  - Quote: This ambitious drug development timeline requires significant funding, but Fission Bio isn't relying on traditional pharmaceutical investment.
  - Observation: The text acknowledges the 'significant funding' requirement but immediately pivots to the DAO model without detailing the sustainability of this model for the long, expensive drug development timeline (IND-enabling studies, clinical trials). It implies the DAO model solves the f…

- **financial_integrity** (info) · *discussion*
  - Quote: Cerebrum DAO has backed the company through two early funding rounds using an innovative community-driven model.
  - Observation: The text explicitly identifies the funding source as a DAO (Cerebrum) using IP Tokens (IPTs) rather than traditional venture capital or grants. This is a significant structural detail regarding financial integrity that explains the 'community-driven' narrative but lacks standard…

- **financial_integrity** (info) · *introduction*
  - Quote: FissionBio, backed by community funding through Cerebrum DAO
  - Observation: The text explicitly identifies the funding source as 'community funding through Cerebrum DAO,' indicating a decentralized autonomous organization (DAO) model rather than traditional venture capital or institutional grants. This is a notable structural detail for assessing financ…

- **team_credibility** (info) · *introduction*
  - Quote: FissionBio, backed by community funding through Cerebrum DAO
  - Observation: The document identifies the entity as 'FissionBio' and the funding mechanism as 'Cerebrum DAO.' While this establishes the organizational structure, the lack of specific academic or clinical affiliations for the lead researchers in this window makes it difficult to assess the te…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 79 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2023 | Targeting an allosteric site in dynamin-related protein 1 to inhibit Fi… | 10.1038/s41467-023-40043-0 |
| 2 | None | 2009 | Mitochondrial dynamics-fusion, fission, movement, and mitophagy-in neur… | 10.1093/hmg/ddp326 |
| 3 | None | 2009 | Impaired Balance of Mitochondrial Fission and Fusion in Alzheimer's Dis… | 10.1523/jneurosci.1357-09.2009 |
| 4 | None | 2023 | Mitochondrial dynamics in health and disease: mechanisms and potential … | 10.1038/s41392-023-01547-9 |
| 5 | None | 2017 | Mitochondrial energetics in the kidney | 10.1038/nrneph.2017.107 |
| 6 | None | 2014 | Editorial (Thematic Issue: Mitochondrial Biogenesis: Pharmacological Ap… | 10.2174/138161282035140911142118 |
| 7 | None | 2012 | AMPK: a nutrient and energy sensor that maintains energy homeostasis | 10.1038/nrm3311 |
| 8 | None | 2025 | Mitochondrial Dysfunction in Neurodegenerative Diseases | 10.3390/cells14040276 |
| 9 | None | 2018 | Reactive Oxygen Species in Metabolic and Inflammatory Signaling | 10.1161/circresaha.117.311401 |
| 10 | None | 2015 | Biological properties of extracellular vesicles and their physiological… | 10.3402/jev.v4.27066 |
| 11 | None | 2020 | Gene regulation by long non-coding RNAs and its biological functions | 10.1038/s41580-020-00315-9 |
| 12 | None | 2021 | Inference and analysis of cell-cell communication using CellChat | 10.1038/s41467-021-21246-9 |
| 13 | None | 2020 | A SARS-CoV-2 protein interaction map reveals targets for drug repurposi… | 10.1038/s41586-020-2286-9 |
| 14 | None | 2021 | Reactive astrocyte nomenclature, definitions, and future directions | 10.1038/s41593-020-00783-4 |
| 15 | None | 2008 | Fission and selective fusion govern mitochondrial segregation and elimi… | 10.1038/sj.emboj.7601963 |
