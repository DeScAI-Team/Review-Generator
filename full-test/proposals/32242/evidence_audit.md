# Proposal evidence audit trail

**Proposal:** Large-Scale Mapping of Human GPCR–Ligand Interactions Using Boltz-2  
**Review date:** May 22, 2026  
**Composite score:** 57/100  

*This file traces the screener findings, originality comparison, and funding assessment that produced the review. The review itself is in review.json.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:31:35Z
- **Generator:** `proposals/pipeline/evidence_doc.py` v1.0 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(model used by upstream proposal_pipe.py)*
- **Git revision:** `94ba61e`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `b521404ac2a8c6f7` |
| screener_findings.json | `8cae70902161b4de` |
| originality.json | `34bb1da9f2161c1a` |

### Composite score

The **composite score** is produced by `proposals/pipeline/proposal_pipe.py`, combining category scores using **`dimension_weights`** in `proposals/pipeline/proposal_mappings.json`.

Current `dimension_weights`: scientific_grounding=0.3; evidential_strength=0.25; funding_realism=0.25; originality=0.2.

## Category scores

| Dimension | Score |
|-----------|------:|
| evidential_strength | 60 |
| funding_realism | 35 |
| originality | 78 |
| scientific_grounding | 60 |

## Category rationales

### Evidential Strength (score: 60)

The proposal demonstrates a strong initial evidential base by citing specific pilot data, including the prediction of 44,574 GPCR–ligand pairs and a benchmark dataset of 89 pairs with a Pearson correlation coefficient of R = 0.78. While these results validate the method's utility for orphan GPCRs, the small sample size of the benchmark limits the statistical power to generalize performance across the entire diverse GPCR family required for the proposed large-scale application. To address this limitation, the project outlines a concrete validation strategy that includes comparing new predictions against experimental affinity data and structural benchmarks to evaluate ligand poses and affinity ranking. This combination of existing pilot metrics and a rigorous future validation plan provides a reasonable foundation for assessing the model's potential, though the current evidence remains preliminary regarding broad generalizability.

### Funding Realism (score: 35)

Funding snapshot: $5,000 requested, $15.96 raised (0.3% funded), 2 contributor(s), 2 of 30 days remaining, behind pace. The proposed scope of generating 200,000 GPCR-ligand predictions is computationally intensive and appears misaligned with the $5,000 budget, which allocates $4,900 to GPU compute at an unrealistically low rate of ~$3.57/hour for H200 instances. While the pilot data demonstrates methodological feasibility, the aggressive timeline of 6 months for this volume of work is highly questionable given the budget constraints and the lack of a dedicated personnel line item for project management. The campaign is critically underfunded at 0.3% with only two contributors and two days remaining, indicating a near-certain failure to meet the goal and a high risk of funders losing their money. Potential backers should be wary of the optimistic cost estimates and the lack of a clear path to completing such a large-scale computational study within the proposed financial limits.

### Originality (score: 78)

The proposed study introduces a novel combination of the Boltz-2 machine learning framework with a large-scale, systematic benchmarking protocol against classical docking methods like AutoDock Vina across the entire human GPCRome. While individual components such as deep learning for protein-ligand interaction prediction [1, 2] and classical molecular docking [7] are well-established, the specific application of Boltz-2 to screen 370 human GPCRs, including 93 orphan receptors, against a curated library of physiological ligands and therapeutics represents a unique methodological integration. This work distinguishes itself by generating a comprehensive dataset of approximately 200,000 predicted structures and affinities, which serves as a direct comparative resource for evaluating the trade-offs between the speed of traditional docking and the accuracy of modern AI models in a context where receptor flexibility is a known limitation [4].

The project builds directly upon existing literature that highlights the limitations of rigid docking models for GPCRs and the emerging potential of deep learning approaches [1, 2, 3]. It aligns with the conceptual frameworks presented in recent reviews discussing the shift from random screening to knowledge-driven design and the specific challenges of modeling conformational flexibility in membrane proteins [12, 22]. Furthermore, the study's focus on drug repurposing and deorphanization mirrors the goals of earlier large-scale pairing efforts, such as the discovery of human signaling systems [4], but updates the methodology by replacing older inference techniques with the more recent Boltz-2 architecture. The approach also resonates with broader discussions on the performance of machine-learning scoring functions in virtual screening, addressing concerns about overfitting and applicability to novel targets [5].

Within the broader landscape of computational drug discovery, this proposal represents a meaningful methodological contribution rather than a purely incremental advance. It addresses a specific gap identified in the literature regarding the lack of systematic, large-scale benchmarks comparing new AI-driven docking tools against established classical methods for the GPCR family [1, 2]. By producing an open database and a transparent pipeline, the project aims to provide a practical toolset that can accelerate the exploration of understudied targets, a goal consistent with initiatives like the Illuminating the Druggable Genome program [23]. The work positions itself as a critical validation step for the utility of Boltz-2 in real-world scenarios, moving beyond isolated case studies to a population-level assessment that could influence future adoption of these AI tools in pharmaceutical pipelines.

Based on comparison with 58 related works, this proposal receives an originality score of 0.7768 out of 1.00, reflecting a high degree of novelty derived from the specific combination of the Boltz-2 method with a comprehensive, large-scale benchmarking strategy for orphan GPCRs that is not currently present in the retrieved literature.

### Scientific Grounding (score: 60)

The proposal demonstrates strong scientific grounding by explicitly linking its methodological choices to established limitations in the field, such as the rigidity of classical docking methods. It justifies the use of Boltz-2 for structure prediction by referencing the need to capture GPCR conformational flexibility, a recognized challenge in current research. The methods section further supports this approach by specifying standard, appropriate tools like MMseqs for generating multiple sequence alignments and AutoDock Vina for docking simulations. To ensure reliability, the project includes a robust risk mitigation strategy that employs consensus scoring with AutoDock Vina for low-confidence predictions, addressing potential weaknesses in single-model outputs. Finally, the study plans to validate its machine learning predictions against specific experimental data points, comparing Boltz-2 pIC50 scores with experimentally derived pKi values to provide measurable outcomes.

## Document screener findings

**Windows scanned:** 3  
**Raw findings:** 15  
**After deduplication:** 15  

- **evidential_strength** (info) · *abstract*  Tags: Benchmark
  - Quote: As pilot work, we have already predicted 44,574 GPCR–ligand pairs using Boltz-2, demonstrating the feasibility of large-scale screening.
  - Observation: The proposal cites specific pilot data (44,574 pairs) to demonstrate technical feasibility, which strengthens the evidential basis for the proposed large-scale scope.

- **evidential_strength** (info) · *pilot_data*  Tags: Benchmark
  - Quote: This resulted in a benchmark dataset of 89 GPCR–ligand pairs. By comparing Boltz-2-predicted Ki values with experimentally measured values, we found that Boltz-2 predictions showed strong agreement w…
  - Observation: The pilot study provides a specific benchmark (R=0.78) on a small dataset (89 pairs) of non-PDB structures. While this validates the method's utility for the specific gap (orphan GPCRs), the small sample size limits the statistical power to generalize performance across the entire diverse GPCR family, which is a key concern for the proposed large-scale application.

- **evidential_strength** (info) · *analysis plan*  Tags: Benchmark
  - Quote: Compare Boltz-2 and AutoDock Vina predictions using structural benchmarks and experimental affinity data; evaluate agreement in ligand poses, affinity ranking, and orphan GPCR prioritization
  - Observation: The plan to benchmark new predictions against experimental affinity data and structural benchmarks provides a concrete strategy for validating the model's performance.

- **funding_realism** (concern) · *budget*  Tags: BudgetRedFlag
  - Quote: GPU costs Costs for ~1370 hours of GPU compute on Nebius NVIDIA HGX H200 $4900
  - Observation: The budget allocates $4,900 for 1,370 hours of high-end GPU compute (NVIDIA H200). This averages to ~$3.57/hour, which is significantly below current market rates for H200 instances on major cloud providers (typically $1.50-$2.50/hour for H100, with H200 often premium-priced). While Nebius may offer discounts, the sheer volume of compute required for 'all-against-all' screening of ~200k pairs see…

- **funding_realism** (concern) · *timeline*  Tags: TimelineFeasibility
  - Quote: The proposed project is designed for completion within a 6-month period... generate nearly 200,000 Boltz-2-predicted GPCR-ligand structures
  - Observation: The proposal aims to generate ~200,000 complex predictions and perform all-against-all docking within 6 months. Given the computational intensity of Boltz-2 and the scale of the 'all-against-all' approach, this timeline appears aggressive, especially if the budget constraints limit the ability to run instances in parallel at maximum capacity. The feasibility of completing this volume of work with…

- **funding_realism** (concern) · *timeline*  Tags: Timeline
  - Quote: The proposed project is designed for completion within a 6-month period and is supported by existing pilot data, established computational workflows, and available infrastructure.
  - Observation: A 6-month timeline for generating 150k structures, performing all-against-all docking, and publishing a manuscript is aggressive; while the team claims 'established workflows,' the feasibility of this scale within half a year warrants scrutiny.

- **funding_realism** (info) · *budget*  Tags: Budget
  - Quote: using Nebius NVIDIA HGX H200 resources, we estimate that the proposed budget will support the generation of nearly 150,000 new GPCR-ligand predicted structures
  - Observation: The proposal explicitly links the budget to specific high-end GPU resources (Nebius NVIDIA HGX H200) and a quantifiable output (150k structures), providing a clear justification for the requested funds.

- **originality** (info) · *innovation_and_novelty*  Tags: NoveltyAssertion, GapStatement
  - Quote: This project is innovative because it represents one of the first large-scale systematic comparisons of machine learning-based GPCR–ligand structure prediction using Boltz-2 with classical molecular …
  - Observation: The proposal clearly articulates the novelty of the work as a large-scale, systematic benchmarking study, distinguishing it from smaller, conventional docking studies.

- **originality** (info) · *background*  Tags: IncrementalContribution
  - Quote: Large-scale all-against-all GPCR–ligand screening will enable identification of novel ligands for orphan GPCRs, discovery of multi-target ligand activity... and repurposing of existing GPCR drugs
  - Observation: The novelty here lies in the scale (all-against-all) and the specific application to orphan GPCRs using a new model (Boltz-2), rather than a fundamentally new algorithmic approach. The value proposition is the creation of a massive, open-access resource for deorphanization, which is a significant incremental contribution to the field.

- **originality** (info) · *background*  Tags: IncrementalContribution
  - Quote: This scale of prediction will create one of the largest openly available GPCR–ligand structural interaction resources
  - Observation: The novelty claim rests on the scale of the dataset (200k structures) rather than a fundamentally new algorithm, positioning the work as a significant incremental contribution to the field's resources.

- **scientific_grounding** (info) · *introduction*  Tags: Methodological, Limitation
  - Quote: Classical molecular docking methods such as AutoDock Vina ... rely on predefined scoring functions and rigid or semi-flexible receptor models that often fail to capture GPCR conformational flexibility
  - Observation: The proposal correctly identifies the specific limitations of classical docking (rigidity, scoring functions) as the rationale for using Boltz-2, grounding the methodological choice in established field knowledge.

- **scientific_grounding** (info) · *methods*  Tags: Methodological
  - Quote: Generate protein multiple sequence alignments (MSAs) using MMseqs [8]; Predict monomeric GPCR structures for docking simulations using Boltz-2.
  - Observation: The methods section specifies the use of MMseqs for MSA generation, a standard and appropriate step for structure prediction methods like Boltz-2 that rely on co-evolutionary signals.

- **scientific_grounding** (info) · *methods*  Tags: Measurement
  - Quote: Compare Boltz-2 pIC 50 scores with experimentally derived pK i values
  - Observation: The proposal defines specific quantitative metrics (pIC50 vs pKi) for validating the machine learning predictions against experimental data, ensuring measurable outcomes.

- **scientific_grounding** (info) · *risk_mitigation*  Tags: Methodological
  - Quote: Low-confidence Boltz-2 predictions... will be prioritized using structural confidence metrics, while low-confidence cases will be evaluated using consensus scoring with AutoDock Vina.
  - Observation: The proposal outlines a robust risk mitigation strategy involving consensus scoring with AutoDock Vina for low-confidence predictions. This hybrid approach is methodologically sound and addresses the known limitations of single-model predictions, enhancing the reliability of the final output.

- **scientific_grounding** (info) · *methods*  Tags: Methodological
  - Quote: Perform all-against-all docking simulations using AutoDock Vina; analyze docking poses, docking scores, and ligand ranking results
  - Observation: The methods section specifies standard tools (AutoDock Vina, Boltz-2) and clear analytical steps, indicating a grounded approach to the computational pipeline.

## Originality (literature overlap)

**Originality score:** 0.7768 · **Related works retrieved:** 69 · **Avg similarity:** 0.2232

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | 0.7500 | 2025 | Deep learning in GPCR drug discovery: benchmarking the path to accurate… | 10.1093/bib/bbaf186 |
| 2 | 0.7200 | 2025 | Beyond rigid docking: deep learning approaches for fully flexible prote… | 10.1093/bib/bbaf454 |
| 3 | 0.6800 | 2025 | AI meets physics in computational structure-based drug discovery for GP… | 10.1038/s44386-025-00019-0 |
| 4 | 0.5500 | 2019 | Discovery of Human Signaling Systems: Pairing Peptides to G Protein-Cou… | 10.1016/j.cell.2019.10.010 |
| 5 | 0.4200 | 2017 | Performance of machine-learning scoring functions in structure-based vi… | 10.1038/srep46710 |
| 6 | 0.4200 | 2012 | Prediction of Drug-Target Interactions and Drug Repositioning via Netwo… | 10.1371/journal.pcbi.1002503 |
| 7 | 0.3800 | 2018 | Binding Affinity via Docking: Fact and Fiction | 10.3390/molecules23081899 |
| 8 | 0.3500 | 2023 | Computational approaches streamlining drug discovery | 10.1038/s41586-023-05905-z |
| 9 | 0.3500 | 2020 | QSAR without borders | 10.1039/d0cs00098a |
| 10 | 0.3200 | 2018 | Recent applications of deep learning and machine intelligence on in sil… | 10.1093/bib/bby061 |
| 11 | 0.3200 | 2020 | Haloperidol bound D2 dopamine receptor structure inspired the discovery… | 10.1038/s41467-020-14884-y |
| 12 | 0.2800 | 2018 | Bridging Molecular Docking to Molecular Dynamics in Exploring Ligand-Pr… | 10.3389/fphar.2018.00923 |
| 13 | 0.2800 | 2021 | Accurate prediction of protein structures and interactions using a thre… | 10.1126/science.abj8754 |
| 14 | 0.2700 | 2015 | Drug–target interaction prediction: databases, web servers and computat… | 10.1093/bib/bbv066 |
| 15 | 0.2600 | 2017 | Metabolite-Sensing G Protein–Coupled Receptors—Facilitators of Diet-Rel… | 10.1146/annurev-immunol-051116-052235 |
| 16 | 0.2600 | 2021 | Highly accurate protein structure prediction for the human proteome | 10.1038/s41586-021-03828-1 |
| 17 | 0.2600 | 2017 | The IUPHAR/BPS Guide to PHARMACOLOGY in 2018: updates and expansion to … | 10.1093/nar/gkx1121 |
| 18 | 0.2600 | 2015 | The IUPHAR/BPS Guide to PHARMACOLOGY in 2016: towards curated quantitat… | 10.1093/nar/gkv1037 |
| 19 | 0.2600 | 2014 | Structure-Based Virtual Screening for Drug Discovery: Principles, Appli… | 10.2174/1568026614666140929124445 |
| 20 | 0.2500 | 2021 | ProLIF: a library to encode molecular interactions as fingerprints | 10.1186/s13321-021-00548-6 |
| 21 | 0.2500 | 2015 | STITCH 5: augmenting protein–chemical interaction networks with tissue … | 10.1093/nar/gkv1277 |
| 22 | 0.2500 | 2021 | G protein-coupled receptors: structure- and function-based drug discove… | 10.1038/s41392-020-00435-w |
| 23 | 0.2400 | 2018 | Unexplored therapeutic opportunities in the human genome | 10.1038/nrd.2018.14 |
| 24 | 0.2400 | 2020 | Molecular Dynamics Simulations in Drug Discovery and Pharmaceutical Dev… | 10.3390/pr9010071 |
| 25 | 0.2400 | 2017 | A Critical Review of Validation, Blind Testing, and Real- World Use of … | 10.2174/1568026617666170414142131 |

*… and 44 additional related work(s) not shown.*

## Funding snapshot

Funding snapshot: $5,000 requested, $15.96 raised (0.3% funded), 2 contributor(s), 2 of 30 days remaining, behind pace. The proposed scope of generating 200,000 GPCR-ligand predictions is computationally intensive and appears misaligned with the $5,000 budget, which allocates $4,900 to GPU compute at an unrealistically low rate of ~$3.57/hour for H200 instances. While the pilot data demonstrates methodological feasibility, the aggressive timeline of 6 months for this volume of work is highly questionable given the budget constraints and the lack of a dedicated personnel line item for project management. The campaign is critically underfunded at 0.3% with only two contributors and two days remaining, indicating a near-certain failure to meet the goal and a high risk of funders losing their money. Potential backers should be wary of the optimistic cost estimates and the lack of a clear path to completing such a large-scale computational study within the proposed financial limits.
