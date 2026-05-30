# Evidence audit trail

**Document:** fission-bio-fixing-broken-mitochondria-to-stop-brain-disease  
**Review date:** May 22, 2026  
**Composite score:** 0.5411  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:02:37Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `1ae357f120d97f56` |
| retrieve_compare_llm.json | `e5d278809d96d523` |
| screener.json | `efb603021ae12623` |
| originality.json | `65bacd8adf324db9` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3500 | evidence_grade_weighted | claim_count=1 |
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=1 |
| financial_integrity | 0.5000 | rubric_penalty | finding_count=2 |
| originality | 1.0000 | literature_similarity | compared_works=45 |
| real_world_traction | 0.5000 | evidence_grade_weighted | claim_count=0 |
| scientific_rigor | 0.3644 | evidence_grade_weighted | claim_count=17 |
| team_credibility | 0.7000 | rubric_penalty | finding_count=1 |

## Evidence grade counts (retrieve_compare)

- **evidential_strength:** unreferenced: 1
- **execution_credibility:** unreferenced: 1
- **originality:** unreferenced: 2; self_reported_method: 1
- **scientific_rigor:** unreferenced: 8; self_reported: 5; unverifiable: 3; self_reported_method: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### scientific_rigor / empirical · chunk 0 · Fission Bio: Fixing Broken Mitochondria to Stop Brain Disease

**Grade:** `unreferenced`  

> Research shows mitochondrial fragmentation and loss of efficiency actively drive diseases like Alzheimer's, ALS, and Huntington's, rather than being solely associated with normal aging.

### scientific_rigor / empirical · chunk 1 · Understanding Our Mitochondrial Balance

**Grade:** `unverifiable`  

> The result is cells filled with fragmented, dysfunctional energy producers unable to meet metabolic demands.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / empirical · chunk 6 · What's Next

**Grade:** `unreferenced`  

> Fission Bio has proven its concept works in laboratory models.

### scientific_rigor / contextual · chunk 1 · Understanding Our Mitochondrial Balance

**Grade:** `unverifiable`  

> Neurodegenerative diseases disrupt the balance between mitochondrial fusion and fission.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 2 · Understanding Our Mitochondrial Balance

**Grade:** `unreferenced`  

> DRP1-dependent mitochondrial fission drives a range of diseases.

### scientific_rigor / contextual · chunk 3 · The P110 Discovery

**Grade:** `unreferenced`  

> Thirteen years of research across 11 disease models demonstrated P110's therapeutic potential.

### scientific_rigor / contextual · chunk 3 · The P110 Discovery

**Grade:** `unreferenced`  

> Peptides face several therapeutic obstacles: complex manufacturing, poor brain penetration, and rapid degradation in the body.

### scientific_rigor / contextual · chunk 3 · The P110 Discovery

**Grade:** `unreferenced`  

> The specific binding site where P110 interferes with the Fis1 interaction is termed SWAG (switch I-adjacent groove).

### scientific_rigor / aspirational · chunk 1 · Understanding Our Mitochondrial Balance

**Grade:** `unverifiable`  

> During inflammatory stress, the protein Drp1 begins interacting with Fis1 - a receptor that triggers excessive mitochondrial fragmentation, while fusion decreases.

**References:**

- [2016] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 2 · Understanding Our Mitochondrial Balance

**Grade:** `unreferenced`  

> Mitochondrial dysfunction has been directly linked to the progression of Alzheimer's disease, where it contributes to cognitive decline and neuronal death, as well as ALS, Huntington's disease, and Parkinson's disease.

### scientific_rigor / aspirational · chunk 5 · Community-Driven Development

**Grade:** `unreferenced`  

> Promising early-stage research often struggles to secure funding, despite its scientific merit.

### evidential_strength / empirical · chunk 0 · Fission Bio: Fixing Broken Mitochondria to Stop Brain Disease

**Grade:** `unreferenced`  

> Research shows mitochondrial fragmentation and loss of efficiency actively drive diseases like Alzheimer's, ALS, and Huntington's, rather than being solely associated with normal aging.

### originality / aspirational · chunk 5 · Community-Driven Development

**Grade:** `unreferenced`  

> Promising early-stage research often struggles to secure funding, despite its scientific merit.

### originality / aspirational · chunk 5 · Community-Driven Development

**Grade:** `unreferenced`  

> This model directly tackles the 'valley of death' - the gap between promising laboratory discoveries and viable treatments that kills most breakthrough research.

### execution_credibility / empirical · chunk 6 · What's Next

**Grade:** `unreferenced`  

> Fission Bio has proven its concept works in laboratory models.

## Document screener

- **financial_integrity** (concern) · *community-driven development*
  - Quote: MITY token holders help fund, govern, and guide Fission Bio's progress while owning fractional stakes in the patents being developed.
  - Observation: The claim that token holders 'govern' the project raises questions about the separation of scientific oversight and financial governance. In drug development, community governance based on token holdings could lead to pressure for premature clinical trials or pivots that comprom…

- **financial_integrity** (concern) · *introduction*
  - Quote: Fission Bio raised $400,000 through Cerebrum DAO's IP-Token model to develop drugs that repair mitochondrial dysfunction instead of treating downstream symptoms.
  - Observation: The document frames the funding model as a 'community-funded breakthrough' but lacks specific details on how token holders' financial incentives align with long-term scientific rigor versus short-term token appreciation. The 'shared ownership' claim needs scrutiny regarding pote…

- **team_credibility** (info) · *the p110 discovery*
  - Quote: Dr. Luis Rios, Fission Bio's Co-Founder and Principal Investigator, made a crucial breakthrough by identifying the specific binding site – termed SWAG (switch I-adjacent groove) – where P110 interfer…
  - Observation: The text attributes a specific mechanistic discovery (SWAG site identification) to Dr. Rios as a 'crucial breakthrough' without citing the primary literature where this was likely first published (e.g., Rios et al., 2023). This suggests a potential conflation of the PI's role in…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 45 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2023 | Targeting an allosteric site in dynamin-related protein 1 to inhibit Fi… | 10.1038/s41467-023-40043-0 |
| 2 | None | 2009 | Mitochondrial dynamics-fusion, fission, movement, and mitophagy-in neur… | 10.1093/hmg/ddp326 |
| 3 | None | 2009 | Impaired Balance of Mitochondrial Fission and Fusion in Alzheimer's Dis… | 10.1523/jneurosci.1357-09.2009 |
| 4 | None | 2023 | Mitochondrial dynamics in health and disease: mechanisms and potential … | 10.1038/s41392-023-01547-9 |
| 5 | None | 2017 | Mitochondrial energetics in the kidney | 10.1038/nrneph.2017.107 |
| 6 | None | 1999 | Caspase structure, proteolytic substrates, and function during apoptoti… | 10.1038/sj.cdd.4400598 |
| 7 | None | 2010 | Regulation of Mammalian Autophagy in Physiology and Pathophysiology | 10.1152/physrev.00030.2009 |
| 8 | None | 2021 | Mitochondrial Dysfunction and Oxidative Stress in Alzheimer’s Disease | 10.3389/fnagi.2021.617588 |
| 9 | None | 2019 | Molecular Mechanisms of TDP-43 Misfolding and Pathology in Amyotrophic … | 10.3389/fnmol.2019.00025 |
| 10 | None | 2023 | Cellular mitophagy: Mechanism, roles in diseases and small molecule pha… | 10.7150/thno.79876 |
| 11 | None | 2024 | Targeting Mitochondrial Dysfunction and Reactive Oxygen Species for Neu… | 10.3390/ijms25147952 |
| 12 | None | 2010 | Mitochondrial Dynamics in Alzheimerʼs Disease | 10.2165/11532140-000000000-00000 |
| 13 | None | 2020 | Neuronal mitochondria-targeted micelles relieving oxidative stress for … | 10.1016/j.biomaterials.2020.119844 |
| 14 | None | 2025 | Mitochondrial Dysfunction in Neurodegenerative Diseases | 10.3390/cells14040276 |
| 15 | None | 2019 | Synergy in Disruption of Mitochondrial Dynamics by Aβ (1-42) and Glia M… | 10.1007/s12035-019-1544-z |
