<img>ResearchHub JOURNAL</img>

Months 1–2: Computational design and in silico screening (backbone generation, sequence design, AlphaFold2/Rosetta filtering).

Months 3–4: Gene synthesis and yeast surface display library construction and expression.

Months 5–6: Binding validation by FACS screening, protein expression, purification, and affinity characterization by BLI.

A Stage 2 submission is anticipated approximately 8 months after Stage 1 acceptance, allowing time for data analysis and manuscript preparation.

**METHODS**
The Methods section provides sufficient detail to allow full replication of all computational and experimental procedures.

**Experimental Design**
*Target Selection and Structure Preparation*
Carboxymethyllysine (CML) will serve as the primary design target. CML is the most abundant AGE in human tissues, is chemically stable, has commercially available standards, and its structure is well characterized. The molecular structure of CML bound to a lysine backbone will be used as the design input. Coordinates will be generated from SMILES notation using RDKit (version 2023.09) and energy-minimized using the MMFF94 force field prior to diffusion design.

*Computational Design Pipeline*
Design will follow the RFdiffusion All-Atom workflow<sup>7</sup> in three sequential stages:

Stage 1 — Backbone generation: RFdiffusion All-Atom will generate protein scaffolds of 70–100 residues conditioned on the CML structure, producing diverse binding pocket geometries. A total of 10,000 backbone designs will be generated using the publicly available RFdiffusion All-Atom repository (github.com/baker-laboratory/rf_diffusion_all_atom).

Stage 2 — Sequence design: ProteinMPNN will assign amino acid sequences to each backbone, optimizing for the predicted binding interface. Five independent sequences will be generated per backbone.

Stage 3 — In silico filtering: Designs will be scored using AlphaFold2 (v2.3) for structural confidence (pLDDT) and Rosetta (REF2015 score function) for binding energy estimation. The top 100–200 designs ranked by a combined metric of pLDDT > 85 and Rosetta binding energy will advance to experimental testing.

*Yeast Surface Display Screening*
Designed binders will be displayed on yeast cell surfaces as Aga2p fusions. A pooled library of top designs will be constructed through oligonucleotide synthesis and Gibson assembly. The library will be sorted against biotinylated AGE-BSA (commercially available from R&D Systems) using fluorescence-activated cell sorting (FACS). Binding cells will be enriched over 2–3 rounds

DOI: 10.55277/rhj.qm7p5g89.3
<page_number>3</page_number>
