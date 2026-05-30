# Proposal evidence audit trail

**Proposal:** Artificial Antigen-Presenting Cells for EnhancedCAR T Cell Persistence and Anti-Tumor Efficacy  
**Review date:** May 22, 2026  
**Composite score:** 53/100  

*This file traces the screener findings, originality comparison, and funding assessment that produced the review. The review itself is in review.json.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:32:22Z
- **Generator:** `proposals/pipeline/evidence_doc.py` v1.0 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(model used by upstream proposal_pipe.py)*
- **Git revision:** `94ba61e`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `916fd65a2f92fd1c` |
| screener_findings.json | `c2b4ad8a0454a271` |
| originality.json | `4dc6bea049991bb5` |

### Composite score

The **composite score** is produced by `proposals/pipeline/proposal_pipe.py`, combining category scores using **`dimension_weights`** in `proposals/pipeline/proposal_mappings.json`.

Current `dimension_weights`: scientific_grounding=0.3; evidential_strength=0.25; funding_realism=0.25; originality=0.2.

## Category scores

| Dimension | Score |
|-----------|------:|
| evidential_strength | 60 |
| funding_realism | 25 |
| originality | 82 |
| scientific_grounding | 50 |

## Category rationales

### Evidential Strength (score: 60)

The proposal presents a mechanistically sound hypothesis regarding surface-tethered IL-15 on aAPC-Lipo, which aligns with established immunological principles of trans-presentation. However, the authors have not yet cited preliminary data to support this specific combination, leaving the core claim without direct empirical backing at this stage. Additionally, the analysis plan commits to reporting data as mean ± SEM, a choice that can obscure true variability and potentially weaken the perceived robustness of the results during review. While the theoretical foundation is logical, the lack of cited preliminary evidence and the specific statistical reporting method suggest that the current evidential support is preliminary rather than conclusive.

### Funding Realism (score: 25)

Funding snapshot: $10,000 requested, $14.32 raised (0.1% funded), 2 contributor(s), 13 of 30 days remaining, behind pace. The proposed budget of $10,000 is critically misaligned with the scope of work, featuring fundamental accounting errors such as listing publication fees under 'Equipment & Services' and allocating only $500 for CAR T cell manufacturing, which is insufficient for generating viable cell lines across multiple donors. The campaign is in severe distress, having raised only $14.32 from two contributors with 13 days remaining, indicating a near-zero likelihood of reaching the goal. These budgetary flaws combined with the lack of institutional backing and the campaign's failure to gain traction suggest the project is not currently viable for funding.

### Originality (score: 82)

The proposed research introduces a novel combination of liposome-based artificial antigen-presenting cells (aAPC-Lipo) engineered to simultaneously deliver multiple surface stimulatory signals and encapsulate therapeutic mRNA. While the use of liposomes as drug carriers is well-established in the literature, as seen in general reviews of nanomedical devices [13] and lipid nanoparticle technologies [42], the specific application of these particles to co-display anti-CD3, anti-CD28, 4-1BBL, and membrane-tethered IL-15 while encapsulating dominant-negative TGF-β receptor II mRNA represents a unique integration of components. This approach distinguishes itself from existing bead-based expansion platforms, which provide only transient activation without the capacity for therapeutic co-delivery, and from other liposomal applications that focus primarily on drug delivery rather than complex immunostimulatory reprogramming during manufacturing and post-transfer.

The project builds upon established methodologies in CAR T cell therapy and tumor immunology, areas where significant prior art exists. The fundamental concepts of CAR T cell limitations regarding persistence and exhaustion are extensively documented, with numerous studies addressing these issues through checkpoint blockade or alternative cell types like CAR-NK cells [7]. Furthermore, the use of liposomes for cancer therapy is a mature field, with extensive literature covering their preparation, characterization, and role in drug delivery [15, 16, 43]. The proposal also aligns with known strategies for overcoming tumor microenvironment suppression, such as targeting TGF-β pathways, although the specific mechanism of delivering dominant-negative receptor mRNA via aAPC-Lipo for this purpose appears to be a new methodological application within this context.

Contextually, this proposal represents a meaningful methodological contribution that seeks to bridge the gap between ex vivo manufacturing constraints and in vivo therapeutic efficacy. Unlike many related works that focus on single aspects such as imaging CAR cells [1], optimizing specific CAR targets [10], or analyzing general immune suppression mechanisms [4, 8, 12], this study aims to create a multifunctional platform that addresses activation, costimulation, and environmental resistance simultaneously. By integrating lipid nanoparticle engineering with CAR T cell manufacturing protocols, the project attempts to solve the problem of signal loss and exhaustion that plagues current therapies, offering a potential incremental advance over conventional bead-based systems and isolated cytokine delivery methods.

Based on comparison with 44 related works, this proposal receives an originality score of 0.8151 out of 1.00, reflecting a high degree of novelty in the specific combination of liposomal aAPC engineering, multi-signal surface display, and mRNA encapsulation for TGF-β blockade within the CAR T cell manufacturing pipeline.

### Scientific Grounding (score: 50)

The proposal demonstrates a solid methodological foundation by correctly identifying liposomal nanoparticles as a tunable platform for artificial antigen-presenting cells and citing their biocompatibility. The methods section further strengthens this grounding by specifying standard, well-established protocols for synthesis, such as thin-film hydration and extrusion, alongside appropriate characterization techniques like DLS and cryo-TEM. However, a notable inconsistency exists in the analysis plan regarding sample sizes, where the proposal specifies a minimum of three biological replicates for in vitro studies but cites n=8 mice for in vivo groups based on power calculations. This discrepancy in reporting statistical requirements across different experimental sections warrants attention to ensure rigorous planning before the project proceeds.

## Document screener findings

**Windows scanned:** 2  
**Raw findings:** 11  
**After deduplication:** 11  

- **evidential_strength** (info) · *hypotheses*  Tags: Mechanistic
  - Quote: Surface-tethered IL-15 on aAPC-Lipo will sustain CAR T cell viability... by engaging the IL-15 receptor complex in trans.
  - Observation: The hypothesis regarding IL-15 trans-presentation is mechanistically sound and aligns with established immunological principles, though preliminary data supporting this specific combination is not yet cited.

- **evidential_strength** (info) · *analysis plan*  Tags: Benchmark
  - Quote: Statistical significance will be defined as p < 0.05. Data will be presented as mean ± SEM unless stated otherwise.
  - Observation: The proposal explicitly commits to reporting SEM rather than SD for data presentation. While common, this choice can obscure the true variability of the data, potentially affecting the perceived evidential strength if reviewers scrutinize the variance.

- **funding_realism** (red_flag) · *budget*  Tags: BudgetRedFlag
  - Quote: Mandatory preprint + peer-reviewed journal $1,400
  - Observation: The budget allocates $1,400 for 'Mandatory preprint + peer-reviewed journal' under Equipment & Services. This is a critical error; publication fees are not equipment or service costs, and $1,400 is insufficient for most high-impact journals. This suggests a fundamental misunderstanding of research budgeting.

- **funding_realism** (red_flag) · *budget*  Tags: BudgetRedFlag
  - Quote: CAR T cell manufacturing reagents & vectors $500
  - Observation: Allocating only $500 for lentiviral vector production, T cell activation reagents, and manufacturing is highly unrealistic for generating sufficient CAR T cells for both in vitro and in vivo studies across multiple donors and timepoints. This line item appears grossly underestimated.

- **funding_realism** (red_flag) · *budget*  Tags: BudgetRedFlag
  - Quote: Flow cytometry (core facility) $1,400
  - Observation: While $1,400 might cover a few samples, the proposal requires extensive flow cytometry for phenotyping, exhaustion profiling, and persistence monitoring across multiple donors, mice, and timepoints. This allocation is likely insufficient for the scope of the experiments described.

- **funding_realism** (red_flag) · *budget*  Tags: BudgetRedFlag
  - Quote: Recombinant cytokines (IL-2, IL-15, IL-21) $4,000
  - Observation: The budget allocates $4,000 for recombinant cytokines but lists only IL-2 in the methods section. The absence of IL-15 and IL-21 in the methods despite the budget line suggests either a mismatch or an underestimation of costs if these are indeed used, raising questions about budget accuracy.

- **originality** (info) · *introduction*  Tags: GapStatement, NoveltyAssertion
  - Quote: However, the potential of liposomal aAPCs specifically designed for the sustained support of CAR T cells — including in vivo re-stimulation and therapeutic payload co-delivery — remains largely unexp…
  - Observation: The authors clearly articulate a specific gap: the lack of liposomal aAPCs designed for sustained CAR T support and in vivo payload delivery, positioning the work as a novel extension of existing aAPC technology.

- **originality** (info) · *abstract*  Tags: Synthesis
  - Quote: We propose to engineer liposome-based artificial antigen-presenting cells (aAPC-Lipo) co-displaying anti-CD3, anti-CD28, 4-1BBL, and membrane-tethered IL-15... while encapsulating dominant-negative T…
  - Observation: The proposal synthesizes multiple advanced concepts (multi-signal aAPCs, membrane-tethered cytokines, and mRNA payload delivery) into a single platform, representing a significant conceptual synthesis rather than a simple replication.

- **scientific_grounding** (concern) · *analysis plan*  Tags: Methodological
  - Quote: All experiments will be performed with a minimum of n = 3 independent biological replicates per condition
  - Observation: The proposal states a minimum of n=3 biological replicates for in vitro studies, but the in vivo section specifies n=8 mice per group based on power calculations. This inconsistency in reporting sample sizes across sections could indicate a lack of rigorous planning or confusion about statistical requirements.

- **scientific_grounding** (info) · *introduction*  Tags: Methodological, Background
  - Quote: Liposomal nanoparticles offer a compelling chassis for constructing artificial antigen-presenting cells (aAPCs). They are biocompatible, highly tunable in size and surface composition...
  - Observation: The proposal correctly identifies liposomes as a tunable platform for aAPCs and cites the general feasibility of this approach, establishing a sound methodological foundation.

- **scientific_grounding** (info) · *methods*  Tags: Methodological
  - Quote: aAPC-Lipo will be synthesized by thin-film hydration followed by extrusion through 100 nm polycarbonate membranes...
  - Observation: The methods section specifies standard, well-established protocols for liposome synthesis (thin-film hydration, extrusion) and characterization (DLS, NTA, cryo-TEM), indicating strong methodological grounding.

## Originality (literature overlap)

**Originality score:** 0.8151 · **Related works retrieved:** 55 · **Avg similarity:** 0.1849

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | 0.6800 | 2024 | Imaging CAR-NK cells targeted to HER2 ovarian cancer with human sodium-… | 10.1007/s00259-024-06722-w |
| 2 | 0.4200 | 2016 | Combination Immunotherapy with NY-ESO-1-Specific CAR+ T Cells with T-Ce… | 10.1182/blood.v128.22.3366.3366 |
| 3 | 0.3800 | 2018 | Durable regression of Medulloblastoma after regional and intravenous de… | 10.1186/s40425-018-0340-z |
| 4 | 0.3800 | 2020 | Collagen promotes anti-PD-1/PD-L1 resistance in cancer through LAIR1-de… | 10.1038/s41467-020-18298-8 |
| 5 | 0.3600 | 2022 | Production and characterization of virus-free, CRISPR-CAR T cells capab… | 10.1136/jitc-2021-004446 |
| 6 | 0.3600 | 2015 | Induction of T-cell Immunity Overcomes Complete Resistance to PD-1 and … | 10.1158/2326-6066.cir-14-0215 |
| 7 | 0.3500 | 2020 | CAR-NK cells: A promising cellular immunotherapy for cancer | 10.1016/j.ebiom.2020.102975 |
| 8 | 0.3500 | 2018 | Cancer-associated fibroblasts induce antigen-specific deletion of CD8 +… | 10.1038/s41467-018-03347-0 |
| 9 | 0.3400 | 2021 | Droplet digital PCR allows vector copy number assessment and monitoring… | 10.1186/s12967-021-02925-z |
| 10 | 0.3300 | 2021 | CD70‐targeting CAR‐T cells have potential activity against CD19‐negativ… | 10.1002/cac2.12201 |
| 11 | 0.3200 | 2023 | An “off-the-shelf” CD2 universal CAR-T therapy for T-cell malignancies | 10.1038/s41375-023-02039-z |
| 12 | 0.3200 | 2006 | Immune Suppression in the Tumor Microenvironment | 10.1097/01.cji.0000199193.29048.56 |
| 13 | 0.2800 | 2015 | Liposomes as nanomedical devices | 10.2147/ijn.s68861 |
| 14 | 0.2800 | 2012 | The tumor microenvironment at a glance | 10.1242/jcs.116392 |
| 15 | 0.2500 | 2024 | Microfluidics-mediated Liposomal Nanoparticles for Cancer Therapy:Recen… | 10.2174/0115680266286460240220073334 |
| 16 | 0.2500 | 2022 | Methods of Liposomes Preparation: Formation and Control Factors of Vers… | 10.3390/pharmaceutics14030543 |
| 17 | 0.2500 | 2020 | Engineered Tumor-Derived Extracellular Vesicles: Potentials in Cancer I… | 10.3389/fimmu.2020.00221 |
| 18 | 0.2200 | 2017 | Apoptosis in mesenchymal stromal cells induces in vivo recipient-mediat… | 10.1126/scitranslmed.aam7828 |
| 19 | 0.2200 | 2020 | Preclinical Imaging Using Single Track Location Shear Wave Elastography… | 10.1109/tmi.2020.2971422 |
| 20 | 0.1800 | 2012 | Holoendemic Malaria Exposure Is Associated with Altered Epstein-Barr Vi… | 10.1128/jvi.02158-12 |
| 21 | 0.1800 | 2010 | The Sympathetic Nervous System Induces a Metastatic Switch in Primary B… | 10.1158/0008-5472.can-10-0522 |
| 22 | 0.1800 | 2010 | Daratumumab, a Novel Therapeutic Human CD38 Monoclonal Antibody, Induce… | 10.4049/jimmunol.1003032 |
| 23 | 0.1600 | 2006 | Analysis of gene expression and chemoresistance of CD133+ cancer stem c… | 10.1186/1476-4598-5-67 |
| 24 | 0.1500 | 2019 | Concentric and Eccentric Endurance Exercise Reverse Hallmarks of T-Cell… | 10.3389/fphys.2019.00684 |
| 25 | 0.1500 | 2012 | Paraneoplastic Thrombocytosis in Ovarian Cancer | 10.1056/nejmoa1110352 |

*… and 30 additional related work(s) not shown.*

## Funding snapshot

Funding snapshot: $10,000 requested, $14.32 raised (0.1% funded), 2 contributor(s), 13 of 30 days remaining, behind pace. The proposed budget of $10,000 is critically misaligned with the scope of work, featuring fundamental accounting errors such as listing publication fees under 'Equipment & Services' and allocating only $500 for CAR T cell manufacturing, which is insufficient for generating viable cell lines across multiple donors. The campaign is in severe distress, having raised only $14.32 from two contributors with 13 days remaining, indicating a near-zero likelihood of reaching the goal. These budgetary flaws combined with the lack of institutional backing and the campaign's failure to gain traction suggest the project is not currently viable for funding.
