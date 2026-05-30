<img>ResearchHub JOURNAL</img>

# De Novo Protein Binder Design for Advanced Glycation End Products: A Computational Approach to Targeting Age-Related Glycative Damage (Stage 1 Registered Report)

Kejun (Albert) Ying<sup>1,2,*</sup>

Published: March 25, 2026

<sup>1</sup> Stanford University, Department of Neurology (Tony Wyss-Coray Lab).
<sup>2</sup> University of Washington, Institute for Protein Design (David Baker Lab).

*Corresponding author: albert.k.ying@gmail.com

## ABSTRACT
Advanced glycation end products (AGEs) accumulate with age and contribute to cardiovascular disease, neurodegeneration, and diabetic complications through receptor for advanced glycation end products (RAGE) activation and direct protein cross-linking. Despite decades of research, no approved therapies specifically target AGEs. This project applies deep learning-based protein design to create de novo protein binders that sequester carboxymethyllysine (CML), the most abundant and well-characterized AGE species. Using RFdiffusion All-Atom, we will generate 10,000 protein scaffold designs conditioned on the CML molecular structure, followed by sequence optimization with ProteinMPNN and in silico filtering using AlphaFold2 and Rosetta. The top 100–200 computational designs will be validated experimentally through yeast surface display screening against CML-modified bovine serum albumin, and top candidates will undergo binding affinity characterization by biolayer interferometry. We hypothesize that this pipeline will yield at least one binder with measurable binding to CML-modified protein and sub-micromolar affinity. All computational designs, experimental protocols, and raw data will be made openly available. This work represents the first application of RFdiffusion All-Atom to AGE targeting and will establish whether computationally designed protein binders can serve as a new class of anti-glycation therapeutics.

## INTRODUCTION
**Research Question: Background, Importance, and Relevance**
AGEs form through non-enzymatic glycation when reducing sugars react with amino groups on proteins, lipids, and nucleic acids. The Maillard reaction produces early glycation intermediates that undergo oxidation and rearrangement to form stable AGE adducts. The most abundant and best-characterized AGEs include carboxymethyllysine (CML), carboxyethyllysine (CEL), and pentosidine. These modifications accumulate in nearly all mammalian tissues with age and are accelerated by hyperglycemia, oxidative stress, and metabolic dysfunction<sup>1,2</sup>.

AGEs cause pathology through two primary mechanisms. First, they directly modify proteins, causing cross-linking that impairs function. This is particularly damaging in long-lived extracellular matrix proteins like collagen, where AGE cross-links increase tissue stiffness and reduce turnover. Second, AGEs bind to the receptor for advanced glycation end products

DOI: 10.55277/rhj.qm7p5g89.3
<page_number>1</page_number>
