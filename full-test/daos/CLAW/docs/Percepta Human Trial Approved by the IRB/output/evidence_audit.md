# Evidence audit trail

**Document:** percepta-human-trial-approved-by-the-irb  
**Review date:** May 22, 2026  
**Composite score:** 0.5083  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:26:58Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `70ed2212f51cbf94` |
| retrieve_compare_llm.json | `d20ed13c9e62bbec` |
| screener.json | `b7a1c585fe43600d` |
| originality.json | `b2abad1a2dffb280` |

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
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=2 |
| financial_integrity | 0.6000 | rubric_penalty | finding_count=1 |
| originality | 1.0000 | literature_similarity | compared_works=30 |
| real_world_traction | 0.3500 | evidence_grade_weighted | claim_count=1 |
| scientific_rigor | 0.3500 | evidence_grade_weighted | claim_count=4 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** unreferenced: 1
- **evidential_strength:** unreferenced: 1
- **execution_credibility:** unreferenced: 2
- **originality:** unreferenced: 1; unverifiable: 1
- **real_world_traction:** unreferenced: 1
- **scientific_rigor:** unreferenced: 3; self_reported_method: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### originality / aspirational · chunk 0 · Percepta Human Trial Approved by the IRB

**Grade:** `unverifiable`  

> This is the world's first tokenized brain health supplement to enter human trials.

**References:**

- [2024] ? → (no verdict — missing abstract)

### originality / aspirational · chunk 3 · The Journey So Far

**Grade:** `unreferenced`  

> The study represents the first community-funded clinical trial for a brain health supplement.

### scientific_rigor / empirical · chunk 2 · The Journey So Far

**Grade:** `unreferenced`  

> In-vitro studies demonstrated strong plaque- and tangle-reducing activity.

### scientific_rigor / empirical · chunk 2 · The Journey So Far

**Grade:** `unreferenced`  

> The demonstrated plaque- and tangle-reducing activity provided the foundation for a multi-year process of development, validation, patenting, and community-backed funding.

### scientific_rigor / aspirational · chunk 3 · The Journey So Far

**Grade:** `unreferenced`  

> The research addresses the plaque and tangle-reducing potential of cat's claw compounds.

### evidential_strength / empirical · chunk 3 · The Journey So Far

**Grade:** `unreferenced`  

> Percepta outperformed all competitors by substantial margins in a 2021 comparison study against 20+ major brain supplements.

### execution_credibility / empirical · chunk 3 · The Journey So Far

**Grade:** `unreferenced`  

> Percepta outperformed all competitors by substantial margins in a 2021 comparison study against 20+ major brain supplements.

### execution_credibility / aspirational · chunk 4 · Looking Ahead

**Grade:** `unreferenced`  

> first results expected later this year

### cross_cutting / aspirational · chunk 4 · Looking Ahead

**Grade:** `unreferenced`  

> safe, natural-product interventions can provide durable support for brain health throughout our lives and hopefully extend our brain health span

### real_world_traction / aspirational · chunk 4 · Looking Ahead

**Grade:** `unreferenced`  

> safe, natural-product interventions can provide durable support for brain health throughout our lives and hopefully extend our brain health span

## Document screener

- **financial_integrity** (concern) · *introduction*
  - Quote: crowd-funded over $500,000 ... from brain health enthusiasts through the CLAW Intellectual Property Token
  - Observation: The study is funded entirely by a community token sale targeting 'enthusiasts' rather than independent academic or pharmaceutical grants. This creates a potential conflict where the primary investors (token holders) may have a financial incentive to see positive results, comprom…

- **originality** (info) · *introduction*
  - Quote: This is the world's first tokenized brain health supplement to enter human trials
  - Observation: The claim of being the 'world's first' tokenized supplement in human trials is a novelty assertion that relies on the definition of 'tokenized.' While likely true in a specific niche, it frames the scientific contribution as a technological novelty (tokenization) rather than a p…

- **scientific_rigor** (concern) · *the trial*
  - Quote: P-tau 217 biomarker tracking – the leading blood-based biomarker for cognitive decline
  - Observation: The text asserts P-tau 217 is the 'leading' biomarker without citation or qualification. While widely used, its status as the definitive 'leading' marker is debated in the field, and using it as a primary endpoint without acknowledging its limitations or the specific assay used …

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 30 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2021 | Neuroprotective Herbs for the Management of Alzheimer’s Disease | 10.3390/biom11040543 |
| 2 | None | 2015 | Coumarins — An Important Class of Phytochemicals | 10.5772/59982 |
| 3 | None | 2021 | Curcumin Inhibits In Vitro SARS-CoV-2 Infection In Vero E6 Cells throug… | 10.3390/molecules26226900 |
| 4 | None | 2018 | Neuroprotection Against MPP+-Induced Cytotoxicity Through the Activatio… | 10.3389/fphar.2018.00768 |
| 5 | None | 2021 | Comparison of the chemical constituents and anti-Alzheimer’s disease ef… | 10.1186/s13020-021-00514-2 |
| 6 | None | 2020 | Dementia prevention, intervention, and care: 2020 report of the Lancet … | 10.1016/s0140-6736(20)30367-6 |
| 7 | None | 2017 | Ferroptosis: A Regulated Cell Death Nexus Linking Metabolism, Redox Bio… | 10.1016/j.cell.2017.09.021 |
| 8 | None | 2021 | 2021 ESC Guidelines for the diagnosis and treatment of acute and chroni… | 10.1093/eurheartj/ehab368 |
| 9 | None | 2012 | European Guidelines on cardiovascular disease prevention in clinical pr… | 10.1093/eurheartj/ehs092 |
| 10 | None | 2018 | Oxidative stress, aging, and diseases | 10.2147/cia.s158513 |
| 11 | None | 2018 | NIA‐AA Research Framework: Toward a biological definition of Alzheimer'… | 10.1016/j.jalz.2018.02.018 |
| 12 | None | 2018 | The Lancet Commission on global mental health and sustainable developme… | 10.1016/s0140-6736(18)31612-x |
| 13 | None | 2019 | Chronic inflammation in the etiology of disease across the life span | 10.1038/s41591-019-0675-0 |
| 14 | None | 2009 | Endocrine-Disrupting Chemicals: An Endocrine Society Scientific Stateme… | 10.1210/er.2009-0002 |
| 15 | None | 2020 | Effects of the Global Coronavirus Disease-2019 Pandemic on Early Childh… | 10.1016/j.jpeds.2020.05.020 |
