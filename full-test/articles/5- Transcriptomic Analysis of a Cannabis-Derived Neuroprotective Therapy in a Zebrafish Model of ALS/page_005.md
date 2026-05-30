<img>ResearchHub JOURNAL</img>

*   BMAA: Embryos exposed to β-N-methylamino-L-alanine to induce neurodegenerative phenotypes characteristic of ALS.
*   CNR-401: BMAA-exposed embryos subsequently treated with drug candidate CNR-401.
*   Edaravone: BMAA-exposed embryos subsequently treated with Edaravone, a clinically approved ALS therapy.
*   Cannflavin A: BMAA-exposed embryos subsequently treated with pure cannflavin A.

**Sample Preparation and RNA Sequencing**
Non-control zebrafish embryos were exposed to BMAA to induce neurodegeneration, with additional groups receiving candidate neuroprotective agents, including Edaravone and CNR-401. All samples (non-treated and treated) were prepared in 10 mM HEC. Samples were incubated in 48-well plates in the same manner as the efficacy assay plates. After collection of the larvae and transfer into 2 mL tubes, the samples were washed three times with E3 water (5 mM NaCl, 0.17 mM KCl, 0.33 mM CaCl₂·2H₂O, 0.33 mM MgSO₄·7H₂O, pH7.2). The remaining E3 water was then removed as thoroughly as possible. Samples were flash-frozen in liquid nitrogen and immediately stored at -80 °C. RNA was extracted using the Qiagen RNeasy kit, and libraries were prepared with the Illumina TruSeq Stranded RNA kit. Sequencing was performed on an Illumina NovaSeq 6000 platform using v1.5 2x150 bp chemistry, and yielding an average of 36.3 million read pairs per sample.

**Data Processing and Visualization**
Raw reads were trimmed with Cutadapt²³ and mapped to the *Danio rerio* reference genome assembly GRCz11 using STAR 2.7.11b²⁴,²⁵. FastQC²⁶ was used to analyze the quality of the reads before and after trimming. Gene-level counts were subsequently imported into DESeq2 (v.1.44.0)²⁷ for normalization and pairwise differential expression analysis (with ~batch + condition design). An adjusted p-value (padj, q) false discovery rate (FDR) of 0.05 (Benjamini and Hochberg) was used as the cutoff value for downstream analysis. In this study, a next-generation differential expressed gene (DEGs) Pipeline Assistant developed by Canruta Therapeutics was employed²⁸. This analysis platform is comparable to existing tools, but was specifically designed for high-throughput, reproducible, and pathway-oriented interpretation of RNA-seq data. The pipeline integrates advanced normalization, automated gene–pathway curation, and streamlined reproducibility, accelerating the identification of candidate therapeutic targets relevant to ALS. The downstream analysis included: automated metadata construction and quality control (boxplots, correlation heatmap, PCA), differential expression filtering with log2 fold change > 1 and adjusted p-value < 0.05, visualization (MA plots, volcano plots, heatmaps), ortholog mapping to human genes, and GO and KEGG functional enrichment analysis with adjusted p-value < 0.05. A summary of the parameters used is presented in the Supplementary Material.

**RESULTS**

**Product Toxicity Assessment**
Both CNR-401 and cannflavin A demonstrated no toxicity up to 2 µM concentration (Supplementary Material: Product Toxicity Assays). Acute toxicity assays were conducted to determine the median lethal concentration (LC₅₀), which is the concentration of the product estimated to be lethal to 50% of the test organisms within the test duration. CNR-401 showed

DOI: 10.55277/rhj.tv4dbb3e.5
<page_number>5</page_number>
