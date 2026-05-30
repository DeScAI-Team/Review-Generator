<img>ResearchHub JOURNAL</img>

**Pre-Processing**
Computational designs will be filtered by the following sequential pre-processing criteria prior to experimental testing: (1) pLDDT > 85 across the full design; (2) predicted TM-score to design model > 0.8; (3) no steric clashes with CML ligand as assessed by Rosetta fa_rep term < 5.0. Designs failing any criterion are excluded from experimental testing. BLI sensorgrams will be double-referenced (reference channel and buffer-only reference) prior to kinetic fitting using the Octet Analysis Studio software (Sartorius, v12).

**Primary Analysis**
The primary outcome is the fraction of designs showing a binding signal above background in yeast surface display (hit rate). Designs with a signal-to-background ratio > 3 relative to no-ligand controls will be classified as hits. The hit rate and its 95% Wilson confidence interval will be reported.

**Secondary Analyses**
(i) Correlation between in silico metrics (AlphaFold2 pLDDT, Rosetta binding energy) and experimental binding, assessed by Spearman rank correlation.
(ii) Structural diversity of successful binders, assessed by pairwise backbone RMSD clustering.
(iii) Affinity distribution of BLI-validated hits, reported as KD values with 95% confidence intervals from curve fitting.

**Variations from Intended Sample Size**
The primary anticipated challenge is a lower-than-expected number of designs passing in silico filtering thresholds, which could reduce the experimental sample below 100 designs. In this event, all designs passing filtering will still be tested and the hit rate reported with appropriate confidence intervals reflecting the smaller denominator. Gene synthesis failures (estimated < 5% of sequences) will be replaced with the next-ranked designs from the computational pipeline. No imputation will be applied to missing BLI measurements; any binder for which a reliable fit cannot be obtained will be reported as “fit failed” with the raw data provided.

**Pilot Data**
Preliminary computational experiments confirm feasibility. Test runs of RFdiffusion All-Atom with CML as the target ligand successfully generated diverse protein scaffolds with plausible binding pockets. AlphaFold2 predicts high confidence (pLDDT > 85) for 15–20% of designs after ProteinMPNN sequence assignment, consistent with published benchmarks for the method<sup>7</sup>. No wet laboratory pilot data has been generated, which is appropriate given the exploratory nature of this project and the absence of prior art applying RFdiffusion All-Atom to AGE targets.

**Statistical Methods**
Hit rates from yeast display will be reported as proportions with 95% Wilson score confidence intervals. Spearman rank correlation (scipy.stats, Python 3.11) will be used for secondary analysis (i) to avoid assumptions of normality given the expected right-skewed distribution of binding scores. BLI kinetic data will be fit to a 1:1 Langmuir model using nonlinear least squares

DOI: 10.55277/rhj.qm7p5g89.3
<page_number>5</page_number>
