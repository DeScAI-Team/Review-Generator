# Evidence audit trail

**Document:** mity-fission-bio-labs-report  
**Review date:** May 22, 2026  
**Composite score:** 0.5083  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:01:06Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `b78c9299467855ae` |
| retrieve_compare_llm.json | `0758fd6b998d8652` |
| screener.json | `70a64bcf4a844d17` |
| originality.json | `3cffdfbffce54ca8` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3500 | evidence_grade_weighted | claim_count=11 |
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=4 |
| financial_integrity | 0.6000 | rubric_penalty | finding_count=1 |
| originality | 1.0000 | literature_similarity | compared_works=48 |
| scientific_rigor | 0.3500 | evidence_grade_weighted | claim_count=14 |
| team_credibility | 0.3500 | evidence_grade_weighted | claim_count=1 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** unreferenced: 1
- **evidential_strength:** unreferenced: 7; self_reported: 3; self_reported_method: 1
- **execution_credibility:** unreferenced: 4
- **governance_accountability:** unreferenced: 1
- **originality:** unreferenced: 6
- **scientific_rigor:** unreferenced: 8; self_reported_method: 4; self_reported: 2
- **team_credibility:** unreferenced: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### scientific_rigor / empirical · chunk 8 · The Opportunity

**Grade:** `unreferenced`  

> Fission Bio's DRP1-FIS1 inhibition targets mitochondrial dysfunction and chronic inflammation without long-term immunosuppression risks, while offering brain-penetrant pharmacology for CNS applications.

### scientific_rigor / contextual · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Mitochondrial dysfunction and fragmentation play central roles in neurodegenerative diseases and chronic inflammatory conditions.

### scientific_rigor / contextual · chunk 2 · The Science

**Grade:** `unreferenced`  

> The program originated from the P110 peptide platform developed at Stanford University, which has demonstrated efficacy across 11 disease models.

### scientific_rigor / contextual · chunk 3 · What Has Been Demonstrated

**Grade:** `unreferenced`  

> P110, the parent peptide compound, has shown efficacy in validated mouse models of ALS, Huntington's disease, Alzheimer's disease, Parkinson's disease, stroke, and cardiac ischemia

### scientific_rigor / aspirational · chunk 0 · Fission Bio Project Announcement

**Grade:** `unreferenced`  

> Targeting Mitochondrial Dysfunction to Treat Neurodegeneration and Chronic Inflammation

### scientific_rigor / aspirational · chunk 0 · Fission Bio Project Announcement

**Grade:** `unreferenced`  

> Fission Bio is developing a novel class of small molecule inhibitors that selectively block pathological mitochondrial fission, addressing a fundamental mechanism linking chronic inflammation to neurodegeneration and age-related disease.

### scientific_rigor / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Most current approaches either target downstream symptoms or broadly suppress immune function.

### scientific_rigor / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> The platform encompasses brain-penetrant, peripheral, and tissue-specific compounds, enabling broad clinical and commercial applications across multiple disease areas.

### originality / empirical · chunk 2 · The Science

**Grade:** `unreferenced`  

> This represents a fundamentally different approach compared to NLRP3 inflammasome inhibitors and other anti-inflammatory strategies that carry long-term immunosuppression risks.

### originality / aspirational · chunk 0 · Fission Bio Project Announcement

**Grade:** `unreferenced`  

> Targeting Mitochondrial Dysfunction to Treat Neurodegeneration and Chronic Inflammation

### originality / aspirational · chunk 0 · Fission Bio Project Announcement

**Grade:** `unreferenced`  

> Fission Bio is developing a novel class of small molecule inhibitors that selectively block pathological mitochondrial fission, addressing a fundamental mechanism linking chronic inflammation to neurodegeneration and age-related disease.

### originality / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Most current approaches either target downstream symptoms or broadly suppress immune function.

### originality / aspirational · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> The platform encompasses brain-penetrant, peripheral, and tissue-specific compounds, enabling broad clinical and commercial applications across multiple disease areas.

### originality / aspirational · chunk 5 · Current Status

**Grade:** `unreferenced`  

> This clean freedom-to-operate pathway is built on de novo chemical scaffolds with no background IP restrictions.

### evidential_strength / empirical · chunk 1 · The Core Idea

**Grade:** `unreferenced`  

> Fission Bio takes a different path by preserving mitochondrial integrity at its source, preventing the cascade of cellular damage without compromising normal immune signaling.

### evidential_strength / empirical · chunk 2 · The Science

**Grade:** `unreferenced`  

> The lead compounds inhibit the pathological interaction between dynamin-related protein 1 (DRP1) and mitochondrial receptor FIS1.

### evidential_strength / empirical · chunk 2 · The Science

**Grade:** `unreferenced`  

> Excessive DRP1-FIS1 interaction drives mitochondrial fragmentation, leading to increased reactive oxygen species (ROS) production, bioenergetic failure, and downstream cell death and inflammatory cascades.

### evidential_strength / empirical · chunk 2 · The Science

**Grade:** `unreferenced`  

> By selectively blocking this protein-protein interaction at the SWAG (switch I-adjacent groove) binding site on DRP1, Fission Bio's compounds preserve mitochondrial function and interrupt disease progression without inhibiting normal immune responses.

### evidential_strength / empirical · chunk 2 · The Science

**Grade:** `unreferenced`  

> This represents a fundamentally different approach compared to NLRP3 inflammasome inhibitors and other anti-inflammatory strategies that carry long-term immunosuppression risks.

### evidential_strength / empirical · chunk 8 · The Opportunity

**Grade:** `unreferenced`  

> Fission Bio's DRP1-FIS1 inhibition targets mitochondrial dysfunction and chronic inflammation without long-term immunosuppression risks, while offering brain-penetrant pharmacology for CNS applications.

### evidential_strength / aspirational · chunk 7 · The Opportunity

**Grade:** `unreferenced`  

> Fission Bio's DRP1-FIS1 inhibition targets mitochondrial dysfunction and chronic inflammation without long-term immunosuppression risks, while offering brain-penetrant

### team_credibility / contextual · chunk 2 · The Science

**Grade:** `unreferenced`  

> The program originated from the P110 peptide platform developed at Stanford University, which has demonstrated efficacy across 11 disease models.

### execution_credibility / aspirational · chunk 5 · Current Status

**Grade:** `unreferenced`  

> composition of matter patents are planned for novel DRP1FIS1 inhibitor scaffolds following hit-to-lead optimization.

### execution_credibility / aspirational · chunk 5 · Current Status

**Grade:** `unreferenced`  

> The IP strategy will cover three distinct classes: brain-penetrant inhibitors for CNS indications, peripheral inhibitors for systemic applications, and tissue-restricted compounds for localized use in organs such as the eye and gut.

### execution_credibility / aspirational · chunk 6 · Next Steps

**Grade:** `unreferenced`  

> The program is advancing through critical development milestones including completion of new compound synthesis and secondary screening by November 2025, hit-to-lead optimization and IP filings for novel scaffolds in Q1 2026, and in vivo validation in ALS, Huntington's disease, …

### execution_credibility / aspirational · chunk 6 · Next Steps

**Grade:** `unreferenced`  

> The initial regulatory strategy targets ALS as the lead indication, enabling potential orphan drug designation, with plans to follow the standard FDA IND pathway after completion of lead optimization, in vivo efficacy studies, and safety profiling.

### cross_cutting / aspirational · chunk 5 · Current Status

**Grade:** `unreferenced`  

> The IP strategy will cover three distinct classes: brain-penetrant inhibitors for CNS indications, peripheral inhibitors for systemic applications, and tissue-restricted compounds for localized use in organs such as the eye and gut.

### governance_accountability / aspirational · chunk 6 · Next Steps

**Grade:** `unreferenced`  

> The initial regulatory strategy targets ALS as the lead indication, enabling potential orphan drug designation, with plans to follow the standard FDA IND pathway after completion of lead optimization, in vivo efficacy studies, and safety profiling.

## Document screener

- **execution_credibility** (concern) · *current status*
  - Quote: Virtual screening of 48 billion compounds from the Enamine REAL library
  - Observation: While the scale of the virtual screen is impressive, the passage lacks details on the filtering criteria, false positive rates, or the specific computational methods used to prioritize the 90 hits. This omission makes it difficult to assess the feasibility of the hit-to-lead tra…

- **financial_integrity** (concern) · *current status*
  - Quote: sponsored by Cerebrum DAO, which serves as IP custodian. An IP-NFT has been minted
  - Observation: The project relies on a DAO and IP-NFT structure for funding and IP custody, which introduces significant uncertainty regarding the stability of funding, legal enforceability of IP rights, and potential conflicts between decentralized governance and traditional pharmaceutical de…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 48 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2023 | Targeting an allosteric site in dynamin-related protein 1 to inhibit Fi… | 10.1038/s41467-023-40043-0 |
| 2 | None | 2009 | Mitochondrial dynamics-fusion, fission, movement, and mitophagy-in neur… | 10.1093/hmg/ddp326 |
| 3 | None | 2009 | Impaired Balance of Mitochondrial Fission and Fusion in Alzheimer's Dis… | 10.1523/jneurosci.1357-09.2009 |
| 4 | None | 2023 | Mitochondrial dynamics in health and disease: mechanisms and potential … | 10.1038/s41392-023-01547-9 |
| 5 | None | 2017 | Mitochondrial energetics in the kidney | 10.1038/nrneph.2017.107 |
| 6 | None | 2017 | The hallmarks of mitochondrial dysfunction in chronic kidney disease | 10.1016/j.kint.2017.05.034 |
| 7 | None | 2018 | Molecular mechanisms of cell death: recommendations of the Nomenclature… | 10.1038/s41418-017-0012-4 |
| 8 | None | 2015 | Biological properties of extracellular vesicles and their physiological… | 10.3402/jev.v4.27066 |
| 9 | None | 2018 | Reactive Oxygen Species in Metabolic and Inflammatory Signaling | 10.1161/circresaha.117.311401 |
| 10 | None | 2019 | Cellular Senescence: Defining a Path Forward | 10.1016/j.cell.2019.10.005 |
| 11 | None | 2023 | Unveiling the potential of mitochondrial dynamics as a therapeutic stra… | 10.3389/fcell.2023.1244313 |
| 12 | None | 2021 | DRP1-Mediated Mitochondrial Fission Regulates Lung Epithelial Response … | 10.3390/ijms222011125 |
| 13 | None | 2023 | Mechanisms of Modulation of Mitochondrial Architecture | 10.3390/biom13081225 |
| 14 | None | 2010 | Regulation of Mammalian Autophagy in Physiology and Pathophysiology | 10.1152/physrev.00030.2009 |
| 15 | None | 2019 | Molecular Mechanisms of TDP-43 Misfolding and Pathology in Amyotrophic … | 10.3389/fnmol.2019.00025 |
