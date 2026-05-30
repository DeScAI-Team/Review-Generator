# Evidence audit trail

**Document:** vdp-16-fundingproposal  
**Review date:** May 22, 2026  
**Composite score:** 0.5020  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:13:45Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `6f344e3028a46f20` |
| retrieve_compare_llm.json | `9e339d5a2b984129` |
| screener.json | `58691c654e49d6e7` |
| originality.json | `9b5a842aeae7a5bd` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3565 | evidence_grade_weighted | claim_count=8 |
| execution_credibility | 0.3657 | evidence_grade_weighted | claim_count=8 |
| financial_integrity | 0.3836 | evidence_grade_weighted | claim_count=3 |
| originality | 1.0000 | literature_similarity | compared_works=87 |
| scientific_rigor | 0.3610 | evidence_grade_weighted | claim_count=26 |
| team_credibility | 0.3500 | evidence_grade_weighted | claim_count=2 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** unreferenced: 1; unverifiable: 1
- **evidential_strength:** unreferenced: 6; self_reported: 1; unverifiable: 1
- **execution_credibility:** unreferenced: 5; unverifiable: 2; self_reported_method: 1
- **financial_integrity:** unverifiable: 2; unreferenced: 1
- **originality:** unreferenced: 6
- **scientific_rigor:** unreferenced: 17; unverifiable: 6; self_reported: 2; self_reported_method: 2
- **team_credibility:** self_reported_method: 1; unreferenced: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### originality / aspirational · chunk 1 · Summary

**Grade:** `unreferenced`  

> Prof. Korolchuck lab proposes to initiate a drug discovery programme with the aim of identifying novel bioactive autophagy inducers.

### originality / aspirational · chunk 11 · Project Summary

**Grade:** `unreferenced`  

> Extensive work leading to this proposal identified a unique phenotype of cells with dysfunctional autophagy in tissue culture.

### originality / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> Targeting the processes downstream of autophagy dysfunction (mitochondrial dysfunction, hyperactivity of NADases, NAD boosting, mitochondrial re-polarisation) can rescue cell death in cells/organisms with both the genetic loss of Atg genes and Npc1.

### originality / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> This provides us with an opportunity for a unique and rapid high throughput cell death-based screening system.

### originality / aspirational · chunk 14 · Project Summary

**Grade:** `unreferenced`  

> We propose to initiate a drug discovery programme with the aim of identifying novel bioactive autophagy inducers.

### originality / aspirational · chunk 16 · Next Steps

**Grade:** `unreferenced`  

> This is a virgin collection that has never been tested for its effect on autophagy and, combined with the natural occurrence of these molecules and therefore bioavailability, it increases the chances of successful hit identification.

### scientific_rigor / empirical · chunk 12 · Project Summary

**Grade:** `unreferenced`  

> The mechanisms of cell death described in MEFs are evolutionarily conserved from yeast to humans.

### scientific_rigor / boilerplate_method · chunk 18 · Budget

**Grade:** `unverifiable`  

> Hit selection will be based on chemical diversity, chemical tractability, and physicochemical parameters.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 10 · VitaDAO

**Grade:** `unreferenced`  

> Lysosomal dysfunction is one of the prominent factors contributing to ageing and a driver of many age-related pathologies.

### scientific_rigor / contextual · chunk 10 · VitaDAO

**Grade:** `unreferenced`  

> In the presence of dysfunctional lysosomes, the autophagy pathway becomes blocked at the terminal stage.

### scientific_rigor / contextual · chunk 11 · Project Summary

**Grade:** `unreferenced`  

> This phenotype is common for Npc1 KO MEFs where autophagosome maturation is impaired as well as for cells with the loss of core autophagy genes (Atg5, Atg7 and FIP200/Rb1cc1).

### scientific_rigor / aspirational · chunk 1 · Summary

**Grade:** `unreferenced`  

> A large number of screens has been performed and published to date, these have identified a wide range of small molecules that stimulate initiation of autophagy.

### scientific_rigor / aspirational · chunk 2 · Problem

**Grade:** `unreferenced`  

> Lysosomal dysfunction is an important factor contributing to the reduction of autophagy during aging.

### scientific_rigor / aspirational · chunk 3 · VitaDAO

**Grade:** `unreferenced`  

> autophagy are rather unreliable, slow, and with complicated readouts, making the screening of compounds that promote autophagy less efficient.

### scientific_rigor / aspirational · chunk 4 · Opportunity

**Grade:** `unreferenced`  

> If funded by VitaDAO, Prof. Korolchuk lab will use this innovative method to screen an unique library of natural compounds, synthesize derivatives based on hits and identify their biological target.

### scientific_rigor / aspirational · chunk 10 · VitaDAO

**Grade:** `unreferenced`  

> We model this situation using cells with a mutation in a lysosomal protein Npc1, which leads to the block in autophagosome degradation.

### scientific_rigor / aspirational · chunk 11 · Project Summary

**Grade:** `unreferenced`  

> Extensive work leading to this proposal identified a unique phenotype of cells with dysfunctional autophagy in tissue culture.

### scientific_rigor / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> Autophagy inducers can rescue autophagy block and cell survival in Npc1 cells, whilst in Atg5 KO cells true autophagy inducers are not able to rescue autophagy or cell death.

### scientific_rigor / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> This provides us with an opportunity for a unique and rapid high throughput cell death-based screening system.

### scientific_rigor / aspirational · chunk 16 · Next Steps

**Grade:** `unreferenced`  

> Lead molecules will be identified by testing structurally similar derivatives of the hits identified in the KVP collection by our long-term collaborator JR and synthesised by KVP staff for structural verification, followed by validation of their effect on autophagy in several st…

### scientific_rigor / aspirational · chunk 16 · Next Steps

**Grade:** `unreferenced`  

> This is a virgin collection that has never been tested for its effect on autophagy and, combined with the natural occurrence of these molecules and therefore bioavailability, it increases the chances of successful hit identification.

### scientific_rigor / aspirational · chunk 17 · Next Steps

**Grade:** `unreferenced`  

> The study aims to establish the specificity of small molecules from screens, identify their cellular targets using the Samsara platform, and characterize their mechanism of action in autophagy.

### scientific_rigor / aspirational · chunk 17 · Next Steps

**Grade:** `unreferenced`  

> The study will investigate the potential of small molecules to alleviate cellular defects caused by lysosomal dysfunction, including mitochondrial deficit, DNA damage, increased sensitivity to stress, and cell death, using human fibroblasts and neurons.

### scientific_rigor / aspirational · chunk 17 · Next Steps

**Grade:** `unreferenced`  

> The study plans to test a focused collection of small molecules based on the structure of lead compounds to establish a robust structure-activity relationship (SAR) for future translation into preclinical models.

### scientific_rigor / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> The study aims to identify lead compounds by screening a diverse library of approximately 200 naturally occurring bioactive compounds in cell survival assays comparing Atg5 and Npc1 knockout models.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> Hit verification will utilize orthogonal assays including Luc-p62 clearance and traffic light LC3 assays.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> The study plans to synthesize derivatives for 3-5 hit series (approximately 12 derivatives each) and perform additional autophagy assays such as cargo degradation, flux assays, imaging-based induction determination, and testing involvement of known signaling pathways.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> Lead series will be determined through screening, followed by a second round of synthesis generating approximately 12 derivatives based on the lead series.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 19 · Budget

**Grade:** `unverifiable`  

> Future work subject to successful screening includes determining ADMET and DMPK profiles in mouse models, assessing pharmacokinetics and tissue distribution, evaluating routes of administration (PO, IV), and conducting preliminary toxicology studies including dose-range finding …

**References:**

- [7] ? → (no verdict — missing abstract)
- [9] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 1 · Summary

**Grade:** `unreferenced`  

> Prof. Korolchuck lab proposes to initiate a drug discovery programme with the aim of identifying novel bioactive autophagy inducers.

### execution_credibility / aspirational · chunk 5 · Highlights

**Grade:** `unreferenced`  

> There is solid evidence supporting their approach

### execution_credibility / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> This provides us with an opportunity for a unique and rapid high throughput cell death-based screening system.

### execution_credibility / aspirational · chunk 14 · Project Summary

**Grade:** `unreferenced`  

> We propose to initiate a drug discovery programme with the aim of identifying novel bioactive autophagy inducers.

### execution_credibility / aspirational · chunk 17 · Next Steps

**Grade:** `unreferenced`  

> The study plans to test a focused collection of small molecules based on the structure of lead compounds to establish a robust structure-activity relationship (SAR) for future translation into preclinical models.

### execution_credibility / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> Lead series will be determined through screening, followed by a second round of synthesis generating approximately 12 derivatives based on the lead series.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 19 · Budget

**Grade:** `unverifiable`  

> Future work subject to successful screening includes determining ADMET and DMPK profiles in mouse models, assessing pharmacokinetics and tissue distribution, evaluating routes of administration (PO, IV), and conducting preliminary toxicology studies including dose-range finding …

**References:**

- [7] ? → (no verdict — missing abstract)
- [9] ? → (no verdict — missing abstract)

### evidential_strength / empirical · chunk 2 · Problem

**Grade:** `unreferenced`  

> Stimulation of autophagy initiation can be ineffective to rescue autophagy when dysfunctional lysosomes interfere with autophagy at the terminal stage.

### evidential_strength / empirical · chunk 11 · Project Summary

**Grade:** `unreferenced`  

> The sequence of events leading to cell death of autophagy deficient cells involves accumulation of dysfunctional mitochondria followed by stress.

### evidential_strength / empirical · chunk 12 · Project Summary

**Grade:** `unreferenced`  

> The mechanisms of cell death described in MEFs are evolutionarily conserved from yeast to humans.

### evidential_strength / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> Targeting the processes downstream of autophagy dysfunction (mitochondrial dysfunction, hyperactivity of NADases, NAD boosting, mitochondrial re-polarisation) can rescue cell death in cells/organisms with both the genetic loss of Atg genes and Npc1.

### evidential_strength / aspirational · chunk 13 · Project Summary

**Grade:** `unreferenced`  

> Autophagy inducers can rescue autophagy block and cell survival in Npc1 cells, whilst in Atg5 KO cells true autophagy inducers are not able to rescue autophagy or cell death.

### evidential_strength / aspirational · chunk 17 · Next Steps

**Grade:** `unreferenced`  

> The study aims to establish the specificity of small molecules from screens, identify their cellular targets using the Samsara platform, and characterize their mechanism of action in autophagy.

### evidential_strength / aspirational · chunk 18 · Budget

**Grade:** `unverifiable`  

> The study aims to identify lead compounds by screening a diverse library of approximately 200 naturally occurring bioactive compounds in cell survival assays comparing Atg5 and Npc1 knockout models.

**References:**

- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### financial_integrity / aspirational · chunk 4 · Opportunity

**Grade:** `unreferenced`  

> If funded by VitaDAO, Prof. Korolchuk lab will use this innovative method to screen an unique library of natural compounds, synthesize derivatives based on hits and identify their biological target.

### financial_integrity / aspirational · chunk 7 · Outcome of the evaluation and recommendation

**Grade:** `unverifiable`  

> All the evaluators consider the project worth funding by the VitaDAO community.

**References:**

- [1] ? → (no verdict — missing abstract)
- [2] ? → (no verdict — missing abstract)
- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [5] ? → (no verdict — missing abstract)

### financial_integrity / aspirational · chunk 19 · Budget

**Grade:** `unverifiable`  

> The project budget may increase to $250,000 to account for TTO overheads of 20-60%.

**References:**

- [7] ? → (no verdict — missing abstract)
- [9] ? → (no verdict — missing abstract)

### team_credibility / aspirational · chunk 15 · VitaDAO

**Grade:** `unreferenced`  

> The study involves contributions from experts in cell biology, drug discovery, and organic and medicinal chemistry.

### cross_cutting / contextual · chunk 10 · VitaDAO

**Grade:** `unreferenced`  

> Stimulation of autophagy initiation may not always be an effective approach to induce the flux through the system.

### cross_cutting / aspirational · chunk 19 · Budget

**Grade:** `unverifiable`  

> Intellectual property is sought for the identified drug candidate(s).

**References:**

- [7] ? → (no verdict — missing abstract)
- [9] ? → (no verdict — missing abstract)

## Document screener

- **financial_integrity** (concern) · *budget*
  - Quote: IP sought for drug candidate(s) patent TTO overhead (20-60%) is not included in the current budget and might increase the ticket size up to $2500000
  - Observation: The budget explicitly excludes significant overhead costs (20-60%) associated with Intellectual Property (IP) transfer and technology transfer offices. This suggests the budget is likely underfunded for the full lifecycle of the project or that the funding model relies on extern…

- **financial_integrity** (concern) · *budget*
  - Quote: Total: 12-month postdoc + running costs - £80,000
  - Observation: The total budget of £80,000 covers only a 12-month postdoc and running costs, yet the project involves synthesizing derivatives, extensive screening, and future plans for in vivo testing and pharmacokinetics. The budget appears tight for the scope of work described, particularly…

- **financial_integrity** (concern) · *highlights*
  - Quote: The platform would allow collaboration with other projects targeting autophagy/mitophagy * Potential for generation of IP/NFT for compounds coming out of their screening platform
  - Observation: The proposal highlights 'IP/NFT' generation and 'company formation' as key outcomes. This suggests a potential misalignment between the VitaDAO community's likely interest in scientific output and the lab's potential financial incentive to prioritize patentable compounds over op…

- **team_credibility** (info) · *next steps*
  - Quote: KVP lab collected 1000+ compounds initially isolated from rare plant and animal species from northern Russia and have a unique expertise in the synthesis of these compounds
  - Observation: The proposal highlights a 'virgin collection' of 1000+ natural compounds from a specific geographic region (northern Russia) that has never been tested for autophagy effects. While this represents a unique resource, the lack of prior testing data means the quality and bioavailab…

- **team_credibility** (info) · *summary*
  - Quote: Prof. Korolchuck lab proposes to initiate a drug discovery programme...
  - Observation: The proposal explicitly names 'Prof. Korolchuk lab' as the executing entity. While the team is described as 'strong and productive' by evaluators, the specific institutional affiliation (e.g., University of Edinburgh) and the professor's specific credentials are not stated in th…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 87 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2016 | Ultrastructural Characterization of the Lower Motor System in a Mouse M… | 10.1038/s41598-016-0001-8 |
| 2 | None | 2011 | Acid β‐glucosidase mutants linked to gaucher disease, parkinson disease… | 10.1002/ana.22400 |
| 3 | None | 2015 | Lysosomal‐associated membrane protein 2 isoforms are differentially aff… | 10.1002/mds.26141 |
| 4 | None | 2007 | Linking of Autophagy to Ubiquitin-Proteasome System Is Important for th… | 10.2353/ajpath.2007.070188 |
| 5 | None | 2017 | Mitochondrial Dynamics: Coupling Mitochondrial Fitness with Healthy Agi… | 10.1016/j.molmed.2017.01.003 |
| 6 | None | 2010 | Regulation of Mammalian Autophagy in Physiology and Pathophysiology | 10.1152/physrev.00030.2009 |
| 7 | None | 2021 | Targeting oxidative stress in disease: promise and limitations of antio… | 10.1038/s41573-021-00233-1 |
| 8 | None | 2007 | Autophagy inhibition enhances therapy-induced apoptosis in a Myc-induce… | 10.1172/jci28833 |
| 9 | None | 2016 | Pancreatic cancer | 10.1038/nrdp.2016.22 |
| 10 | None | 2019 | Tumor-associated macrophages: an accomplice in solid tumor progression | 10.1186/s12929-019-0568-z |
| 11 | None | 2016 | Guidelines for the use and interpretation of assays for monitoring auto… | 10.1080/15548627.2015.1100356 |
| 12 | None | 2020 | Multidisciplinary research priorities for the COVID-19 pandemic: a call… | 10.1016/s2215-0366(20)30168-1 |
| 13 | None | 2019 | Molecular Docking: Shifting Paradigms in Drug Discovery | 10.3390/ijms20184331 |
| 14 | None | 2019 | Role of hypoxia in cancer therapy by regulating the tumor microenvironm… | 10.1186/s12943-019-1089-9 |
| 15 | None | 2012 | The role of surface charge in cellular uptake and cytotoxicity of medic… | 10.2147/ijn.s36111 |
