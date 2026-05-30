# Evidence audit trail

**Document:** vita-fast-whitepaper  
**Review date:** May 22, 2026  
**Composite score:** 0.4898  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:17:30Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `5b140c09eef889f6` |
| retrieve_compare_llm.json | `121c1c1e6796b070` |
| screener.json | `77ffef056b677811` |
| originality.json | `d9f5fdd78689c47e` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.3661 | evidence_grade_weighted | claim_count=2 |
| execution_credibility | 0.3648 | evidence_grade_weighted | claim_count=13 |
| financial_integrity | 0.3500 | evidence_grade_weighted | claim_count=16 |
| originality | 1.0000 | literature_similarity | compared_works=174 |
| real_world_traction | 0.3500 | evidence_grade_weighted | claim_count=3 |
| scientific_rigor | 0.3702 | evidence_grade_weighted | claim_count=34 |
| team_credibility | 0.3500 | evidence_grade_weighted | claim_count=6 |

## Evidence grade counts (retrieve_compare)

- **cross_cutting:** unreferenced: 7
- **evidential_strength:** unreferenced: 1; unverifiable: 1
- **execution_credibility:** unreferenced: 7; unverifiable: 4; self_reported_method: 2
- **financial_integrity:** unreferenced: 12; self_reported_method: 4
- **governance_accountability:** unreferenced: 10; unverifiable: 2
- **originality:** unreferenced: 8
- **real_world_traction:** unreferenced: 3
- **scientific_rigor:** unreferenced: 16; unverifiable: 11; self_reported_method: 8
- **team_credibility:** unreferenced: 6

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### execution_credibility / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> At the time of publishing, the lab is screening the second generation of compounds that have been developed as lead series based on hits and is waiting on the delivery of additional chemical series of their leads.

### execution_credibility / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> Once lead molecules have been identified, VitaDAO and Molecule will work with Newcastle University and Dr. Korolchuk's lab to start the process of drug translation.

### execution_credibility / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> Upon completion, further research in in vitro and in vivo models will need to be performed.

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> From there, clinical studies would commence: Phase 1 Clinical Trials: Testing of the drug in a small group of healthy volunteers or patients (20-100) to evaluate safety, dosage, and side effects.

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> Phase 3 Clinical Trials

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 15 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> In this stage, if successful in Niemann-Pick Type C, the drug could be tried for Alzheimer's disease as a future indication, although that would involve its own full set of clinical trials.

### execution_credibility / aspirational · chunk 18 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> VitaDAO seeks to open up the development of an IP-NFT by minting new tokens in order to raise funds for additional scientific research and IP development.

### execution_credibility / aspirational · chunk 21 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> This is not required in the contract, but is intended to be a strong signal to other University TTOs and an incentive to speed up the licensing process if completed by a deadline.

### execution_credibility / aspirational · chunk 22 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> A Uniswap V3 liquidity pool will be created upon claiming the sale proceeds, matching 10% of the VITA-FAST tokens with 10% of the funds raised.

### execution_credibility / aspirational · chunk 32 · 9. Risk Factors

**Grade:** `unreferenced`  

> There might be delays, cost overruns, or the research might not yield the expected results.

### execution_credibility / aspirational · chunk 38 · 11. Team

**Grade:** `unverifiable`  

> The facility transitioned from genome wide yeast screens to mammalian siRNA screening in 2012.

**References:**

- [2011] ? → (no verdict — missing abstract)
- [2012] ? → (no verdict — missing abstract)

### real_world_traction / aspirational · chunk 1 · 1. Executive Summary

**Grade:** `unreferenced`  

> The sale of VITA-FAST tokens represents an innovative approach to democratizing funding for scientific research. It demands thorough understanding and careful consideration of potential risks from potential VITA-FAST token buyers.

### real_world_traction / aspirational · chunk 6 · 3. Project Background

**Grade:** `unreferenced`  

> Once the drug is approved, it has the potential to become a recognized therapeutic for more lysosomal storage disorders, and diseases that have a high incidence of lysosomal dysfunction, such as Alzheimer's and Parkinson's.

### real_world_traction / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs can create unprecedented liquidity in IP markets through the development of this new asset class.

### financial_integrity / aspirational · chunk 1 · 1. Executive Summary

**Grade:** `unreferenced`  

> The sale of VITA-FAST tokens represents an innovative approach to democratizing funding for scientific research. It demands thorough understanding and careful consideration of potential risks from potential VITA-FAST token buyers.

### financial_integrity / aspirational · chunk 3 · 2. Project Overview

**Grade:** `unreferenced`  

> The sale and funds aim to continue to support the work initiated by Dr. Korolchuk and Newcastle University to advance the field of aging research by empowering people to govern the Korolchuk Lab longevity therapeutics development through the use of cryptographic tokens represent…

### financial_integrity / aspirational · chunk 18 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> VitaDAO seeks to open up the development of an IP-NFT by minting new tokens in order to raise funds for additional scientific research and IP development.

### financial_integrity / aspirational · chunk 18 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> By distributing these new tokens, called Molecules, VitaDAO will distribute rights and responsibilities to the IP and R&D data of IP-NFTs to groups of token holders.

### financial_integrity / aspirational · chunk 19 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> The rights of VITA-FAST token holders are governed by the Korolchuk-Free Association of Molecules (FAM) Membership Agreement.

### financial_integrity / aspirational · chunk 20 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> A total of 1,000,000 VITA-FAST tokens will be minted using the Korolchuk IP-NFT.

### financial_integrity / aspirational · chunk 21 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> The vesting period incentivizes long-term success of the project and discourages falsification of data.

### financial_integrity / aspirational · chunk 21 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> This is not required in the contract, but is intended to be a strong signal to other University TTOs and an incentive to speed up the licensing process if completed by a deadline.

### financial_integrity / aspirational · chunk 21 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> Vesting period incentivizes long-term success of the project, but must first be approved by VitaDAO governance.

### financial_integrity / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> The immediate application of the funds raised will be to establish liquidity for VITA-FAST.

### financial_integrity / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> VITA-FAST holders have the power to decide how these funds will be subsequently used in advancing longevity research and IP development at the Korolchuk lab at Newcastle University.

### financial_integrity / aspirational · chunk 30 · 8. Use of Funds

**Grade:** `unreferenced`  

> through token holder governance there are various pathways to redirect this capital from liquidity to IP generation

### originality / aspirational · chunk 1 · 1. Executive Summary

**Grade:** `unreferenced`  

> The sale of VITA-FAST tokens represents an innovative approach to democratizing funding for scientific research. It demands thorough understanding and careful consideration of potential risks from potential VITA-FAST token buyers.

### originality / aspirational · chunk 4 · 3. Project Background

**Grade:** `unreferenced`  

> Aging is associated with a decline in the capacity of the autophagy pathway, and the mechanism through which autophagy becomes deficient with age remains to be understood.

### originality / aspirational · chunk 6 · 3. Project Background

**Grade:** `unreferenced`  

> NPC was chosen as the disease model as it is a monogenetic orphan disease, meaning that the biological causes are better understood, and any therapeutics developed will have a much shorter path to drug approval compared to other complex diseases.

### originality / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> The small molecules that have been screened have high chemical variability and no similarity to pre-existing autophagy inducers, representing a high possibility of novel IP.

### originality / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs represent a new paradigm in the evolution of legal contracts for scientific research by attaching legal contracts, such as sponsored research agreements, to smart contracts.

### originality / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs can create unprecedented liquidity in IP markets through the development of this new asset class.

### originality / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> The first IP-NFTs were minted by Molecule for the VitaDAO community to register its longevity therapeutics IP and R&D data rights on Ethereum.

### originality / aspirational · chunk 40 · Resources:

**Grade:** `unreferenced`  

> The project aims to discover novel autophagy activators.

### team_credibility / aspirational · chunk 3 · 2. Project Overview

**Grade:** `unreferenced`  

> The sale and funds aim to continue to support the work initiated by Dr. Korolchuk and Newcastle University to advance the field of aging research by empowering people to govern the Korolchuk Lab longevity therapeutics development through the use of cryptographic tokens represent…

### team_credibility / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> Once lead molecules have been identified, VitaDAO and Molecule will work with Newcastle University and Dr. Korolchuk's lab to start the process of drug translation.

### team_credibility / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> The first IP-NFTs were minted by Molecule for the VitaDAO community to register its longevity therapeutics IP and R&D data rights on Ethereum.

### team_credibility / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> VITA-FAST holders have the power to decide how these funds will be subsequently used in advancing longevity research and IP development at the Korolchuk lab at Newcastle University.

### team_credibility / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> The objective is to harness superior SAR expertise from a global pool.

### team_credibility / aspirational · chunk 37 · 11. Team

**Grade:** `unreferenced`  

> Dr. Korolchuk's research focuses on the molecular mechanisms that regulate cellular homeostasis, particularly in the context of neurodegenerative diseases and cancer.

### scientific_rigor / empirical · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Stress response pathways are activated (PARP & SIRT).

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / empirical · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Apoptosis (programmed cell death) begins.

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Dysfunctional mitochondria accumulate within cells due to inadequate recycling caused by faulty autophagy.

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Accumulation of reactive oxygen species (ROS) and DNA damage induces cellular stress.

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Depletion of NAD+ and NADH occurs, which are essential to cellular metabolic pathways.

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 7 · 3. Project Background

**Grade:** `unverifiable`  

> Mitochondria lose their ability to generate ATP as they become depolarized.

**References:**

- [4] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 16 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> NFTs provide a new way to manage and protect intellectual property, allowing creators and owners to easily transfer ownership, establish authenticity, and control usage rights.

### scientific_rigor / aspirational · chunk 4 · 3. Project Background

**Grade:** `unreferenced`  

> Aging is associated with a decline in the capacity of the autophagy pathway, and the mechanism through which autophagy becomes deficient with age remains to be understood.

### scientific_rigor / aspirational · chunk 4 · 3. Project Background

**Grade:** `unreferenced`  

> Activation of autophagy is considered a promising therapeutic approach to combat aging and age-related diseases.

### scientific_rigor / aspirational · chunk 5 · 3. Project Background

**Grade:** `unreferenced`  

> Impaired autophagy is strongly linked to neurodegenerative disorders like Alzheimer's disease, Parkinson's disease, Huntington's disease, and amyotrophic lateral sclerosis (ALS).

### scientific_rigor / aspirational · chunk 6 · 3. Project Background

**Grade:** `unreferenced`  

> NPC was chosen as the disease model as it is a monogenetic orphan disease, meaning that the biological causes are better understood, and any therapeutics developed will have a much shorter path to drug approval compared to other complex diseases.

### scientific_rigor / aspirational · chunk 8 · 3. Project Background

**Grade:** `unreferenced`  

> Approximately 4000 bioactive molecules and commercial small molecules will be screened.

### scientific_rigor / aspirational · chunk 9 · 3. Project Background

**Grade:** `unverifiable`  

> Structure-activity relationship (SAR) and validation in vitro autophagy assays

**References:**

- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> The small molecules that have been screened have high chemical variability and no similarity to pre-existing autophagy inducers, representing a high possibility of novel IP.

### scientific_rigor / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> Possibilities include using Neimann-Pick Type C patient-derived fibroblasts or CRISPR-Cas9 Npc1 knock-out cells to examine the efficacy of lead compounds in a human cell model.

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> Npc1-mutant mice and cats who display the same symptoms as humans with Niemann-Pick Type C provide strong in vivo models to evaluate neurological outcomes as well as potential toxicity in large animal models.

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 16 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> NFTs can be used to represent various forms of digital content, including art, virtual real property, scientific research and development (R&D) data, and intellectual property.

### scientific_rigor / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs represent a new paradigm in the evolution of legal contracts for scientific research by attaching legal contracts, such as sponsored research agreements, to smart contracts.

### scientific_rigor / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> The aim is to identify promising compound scaffolds and design optimal candidates for further medicinal chemistry optimization.

### scientific_rigor / aspirational · chunk 31 · 9. Risk Factors

**Grade:** `unreferenced`  

> The list of potential risks associated with purchasing Molecules to fund scientific research is not exhaustive, and specific risks vary depending on the nature of the project, the research being funded, the structure of the investment, the jurisdiction, and other factors.

### scientific_rigor / aspirational · chunk 32 · 9. Risk Factors

**Grade:** `unreferenced`  

> There might be delays, cost overruns, or the research might not yield the expected results.

### scientific_rigor / aspirational · chunk 33 · 9. Risk Factors

**Grade:** `unreferenced`  

> The value and function of the Molecules could be impacted by changes or issues with the underlying blockchain network, Ethereum, such as changes in the consensus mechanism, forks, or network congestion.

### scientific_rigor / aspirational · chunk 33 · 9. Risk Factors

**Grade:** `unreferenced`  

> The platforms or exchanges used to buy, sell, or store the Molecules could have operational issues, such as downtime, that could impact your ability to manage your purchase.

### scientific_rigor / aspirational · chunk 37 · 11. Team

**Grade:** `unreferenced`  

> Dr. Korolchuk's research focuses on the molecular mechanisms that regulate cellular homeostasis, particularly in the context of neurodegenerative diseases and cancer.

### scientific_rigor / aspirational · chunk 38 · 11. Team

**Grade:** `unverifiable`  

> The study addresses the use of robotics in genetic research.

**References:**

- [2011] ? → (no verdict — missing abstract)
- [2012] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 38 · 11. Team

**Grade:** `unverifiable`  

> The screening facility expanded to incorporate bacteria and alternative yeasts such as Candida albicans.

**References:**

- [2011] ? → (no verdict — missing abstract)
- [2012] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 39 · 11. Team

**Grade:** `unreferenced`  

> His research focuses on the discovery of new drug candidates and the development of novel therapeutic strategies for various diseases, including cancer, infectious diseases, and neurodegenerative disorders.

### evidential_strength / aspirational · chunk 9 · 3. Project Background

**Grade:** `unverifiable`  

> determination of the mechanism of action

**References:**

- [3] ? → (no verdict — missing abstract)
- [4] ? → (no verdict — missing abstract)
- [6] ? → (no verdict — missing abstract)

### evidential_strength / aspirational · chunk 13 · 4. Project Status and Future Plans

**Grade:** `unreferenced`  

> At the time of publishing, the lab is screening the second generation of compounds that have been developed as lead series based on hits and is waiting on the delivery of additional chemical series of their leads.

### governance_accountability / aspirational · chunk 14 · 4. Project Status and Future Plans

**Grade:** `unverifiable`  

> For Niemann-Pick Type C, Orphan Drug designation could be sought at this stage, which may provide some benefits including tax credits for certain research and a waiver of the FDA user fee.

**References:**

- [20] ? → (no verdict — missing abstract)
- [21] ? → (no verdict — missing abstract)
- [22] ? → (no verdict — missing abstract)
- [23] ? → (no verdict — missing abstract)
- [24] ? → (no verdict — missing abstract)
- [25] ? → (no verdict — missing abstract)
- [26] ? → (no verdict — missing abstract)
- [27] ? → (no verdict — missing abstract)
- [28] ? → (no verdict — missing abstract)
- [29] ? → (no verdict — missing abstract)
- [30] ? → (no verdict — missing abstract)
- [31] ? → (no verdict — missing abstract)
- [32] ? → (no verdict — missing abstract)
- [33] ? → (no verdict — missing abstract)
- [34] ? → (no verdict — missing abstract)
- [35] ? → (no verdict — missing abstract)
- [36] ? → (no verdict — missing abstract)
- [37] ? → (no verdict — missing abstract)
- [38] ? → (no verdict — missing abstract)
- [39] ? → (no verdict — missing abstract)
- [40] ? → (no verdict — missing abstract)
- [41] ? → (no verdict — missing abstract)
- [42] ? → (no verdict — missing abstract)
- [43] ? → (no verdict — missing abstract)
- [44] ? → (no verdict — missing abstract)
- [45] ? → (no verdict — missing abstract)
- [46] ? → (no verdict — missing abstract)
- [47] ? → (no verdict — missing abstract)
- [48] ? → (no verdict — missing abstract)
- [49] ? → (no verdict — missing abstract)
- [50] ? → (no verdict — missing abstract)
- [51] ? → (no verdict — missing abstract)
- [52] ? → (no verdict — missing abstract)
- [53] ? → (no verdict — missing abstract)
- [54] ? → (no verdict — missing abstract)
- [55] ? → (no verdict — missing abstract)
- [56] ? → (no verdict — missing abstract)
- [57] ? → (no verdict — missing abstract)
- [58] ? → (no verdict — missing abstract)
- [59] ? → (no verdict — missing abstract)
- [60] ? → (no verdict — missing abstract)
- [61] ? → (no verdict — missing abstract)
- [62] ? → (no verdict — missing abstract)
- [63] ? → (no verdict — missing abstract)
- [64] ? → (no verdict — missing abstract)
- [65] ? → (no verdict — missing abstract)
- [66] ? → (no verdict — missing abstract)
- [67] ? → (no verdict — missing abstract)
- [68] ? → (no verdict — missing abstract)
- [69] ? → (no verdict — missing abstract)
- [70] ? → (no verdict — missing abstract)
- [71] ? → (no verdict — missing abstract)
- [72] ? → (no verdict — missing abstract)
- [73] ? → (no verdict — missing abstract)
- [74] ? → (no verdict — missing abstract)
- [75] ? → (no verdict — missing abstract)
- [76] ? → (no verdict — missing abstract)
- [77] ? → (no verdict — missing abstract)
- [78] ? → (no verdict — missing abstract)
- [79] ? → (no verdict — missing abstract)
- [80] ? → (no verdict — missing abstract)
- [81] ? → (no verdict — missing abstract)
- [82] ? → (no verdict — missing abstract)
- [83] ? → (no verdict — missing abstract)
- [84] ? → (no verdict — missing abstract)
- [85] ? → (no verdict — missing abstract)
- [86] ? → (no verdict — missing abstract)
- [87] ? → (no verdict — missing abstract)
- [88] ? → (no verdict — missing abstract)
- [89] ? → (no verdict — missing abstract)
- [90] ? → (no verdict — missing abstract)
- [91] ? → (no verdict — missing abstract)
- [92] ? → (no verdict — missing abstract)
- [93] ? → (no verdict — missing abstract)
- [94] ? → (no verdict — missing abstract)
- [95] ? → (no verdict — missing abstract)
- [96] ? → (no verdict — missing abstract)
- [97] ? → (no verdict — missing abstract)
- [98] ? → (no verdict — missing abstract)
- [99] ? → (no verdict — missing abstract)
- [100] ? → (no verdict — missing abstract)

### governance_accountability / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs can be used to distribute governance to groups of stakeholders.

### governance_accountability / aspirational · chunk 18 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> By distributing these new tokens, called Molecules, VitaDAO will distribute rights and responsibilities to the IP and R&D data of IP-NFTs to groups of token holders.

### governance_accountability / aspirational · chunk 19 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> The rights of VITA-FAST token holders are governed by the Korolchuk-Free Association of Molecules (FAM) Membership Agreement.

### governance_accountability / aspirational · chunk 21 · 6. Tokenomics of VITA-FAST

**Grade:** `unreferenced`  

> Vesting period incentivizes long-term success of the project, but must first be approved by VitaDAO governance.

### governance_accountability / aspirational · chunk 29 · 8. Use of Funds

**Grade:** `unreferenced`  

> LabDAO has proposed providing access to facilitate the decentralization of Structure-Activity Relationship (SAR) analysis.

### governance_accountability / aspirational · chunk 30 · 8. Use of Funds

**Grade:** `unreferenced`  

> through token holder governance there are various pathways to redirect this capital from liquidity to IP generation

### governance_accountability / aspirational · chunk 33 · 9. Risk Factors

**Grade:** `unreferenced`  

> Depending on your jurisdiction, owning and trading Molecules or other digital assets might have legal implications, including potential tax liabilities.

### governance_accountability / aspirational · chunk 33 · 9. Risk Factors

**Grade:** `unreferenced`  

> Molecules include governance rights and there may be disagreements or disputes among the token holders.

### governance_accountability / aspirational · chunk 34 · 10. Legal Considerations

**Grade:** `unreferenced`  

> Given regulatory uncertainty, token holders must make a careful judgment in the future about whether, and how, to distribute licensing or sale proceeds, such as by forming a legal entity prior to making such distribution and it is recommended that such decisions include soliciti…

### governance_accountability / aspirational · chunk 35 · 10. Legal Considerations

**Grade:** `unreferenced`  

> VITA-FAST will not be sold to U.S. persons in compliance with Regulation S of the United States

### governance_accountability / aspirational · chunk 36 · 10. Legal Considerations

**Grade:** `unverifiable`  

> VITA-FAST will not be made available to U.S. persons or within the United States.

**References:**

- [1933] ? → (no verdict — missing abstract)

### cross_cutting / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs can be used to unlock new ways to interact with and develop IP, R&D data, and NIPIA (Non-IP Intangible Assets, like trade secrets and publicity rights).

### cross_cutting / aspirational · chunk 17 · 5. Introduction to Blockchain, NFTs, IP-NFTs, and Molecules

**Grade:** `unreferenced`  

> IP-NFTs can be used to empower crowd control of ethics in commercialization.

### cross_cutting / aspirational · chunk 26 · Pro rata distribution

**Grade:** `unreferenced`  

> If the sales goal is met or exceeded, then the final allocation of Molecules will be proportional to each bidder's fraction of the total bids.

### cross_cutting / aspirational · chunk 27 · Overflow refunds

**Grade:** `unreferenced`  

> If the amount bid exceeds the sales goal, then the excess amount is automatically returned via the token sale smart contract.

### cross_cutting / aspirational · chunk 32 · 9. Risk Factors

**Grade:** `unreferenced`  

> The success of the scientific research being funded is not guaranteed.

### cross_cutting / aspirational · chunk 32 · 9. Risk Factors

**Grade:** `unreferenced`  

> There might be delays, cost overruns, or the research might not yield the expected results.

### cross_cutting / aspirational · chunk 34 · 10. Legal Considerations

**Grade:** `unreferenced`  

> Given regulatory uncertainty, token holders must make a careful judgment in the future about whether, and how, to distribute licensing or sale proceeds, such as by forming a legal entity prior to making such distribution and it is recommended that such decisions include soliciti…

## Document screener

- **financial_integrity** (concern) · *tokenomics*
  - Quote: The vesting period incentivizes long-term success of the project and discourages falsification of data.
  - Observation: The document explicitly links token vesting to the prevention of data falsification. This is a non-standard, unproven causal claim; vesting schedules are financial mechanisms that do not inherently prevent scientific misconduct or data fabrication.

- **financial_integrity** (info) · *bidding and locking*
  - Quote: The more VITA a buyer is willing to stake in the sales contract for the 60-day vesting period, the more that buyer may bid during the 2-day sale period.
  - Observation: The mechanism requires locking native governance tokens (VITA) to bid for the project tokens (VITA-FAST). This aligns incentives by ensuring only committed, long-term holders can participate in the initial funding round, reducing speculative 'flip-and-dump' behavior.

- **financial_integrity** (info) · *funding*
  - Quote: Resources: Korolchuk Lab - VitaDAO Discovering Novel Autophagy Activators - Molecule Funding Science Through Blockchain Technology and Cryptocurrencies - Newcastle University Newcastle fractionalizat…
  - Observation: The funding model involves 'fractionalization' and 'blockchain technology' to fund scientific research. While innovative, this specific mechanism is not standard in academic publishing and introduces complexity regarding how resources are allocated, tracked, and audited compared…

- **financial_integrity** (info) · *tokenomics*
  - Quote: 10% of VITA-FAST tokens (100,000 VITA-FAST) will be sold to a maximum of 499 participants who are VITA tokenholders of VitaDAO...
  - Observation: The token sale is restricted to existing 'VITA tokenholders,' creating a closed-loop fundraising mechanism that excludes external investors. This limits the diversity of the funding base and potential for broad market validation.

- **financial_integrity** (info) · *use of funds*
  - Quote: The immediate application of the funds raised will be to establish liquidity for VITA-FAST.
  - Observation: The primary use of funds is liquidity provision rather than immediate R&D execution. This suggests a strategy to bootstrap a secondary market before heavy IP development costs are incurred, which is a common but risky approach for early-stage scientific tokens.

- **team_credibility** (concern) · *author affiliations*
  - Quote: Jóhannes Reynisson ... is a drug discovery expert and a research lead at VitaDAO ... He holds a PhD in chemistry from the University of Copenhagen and has extensive experience in the pharmaceutical i…
  - Observation: The text explicitly links a key team member to the project entity (VitaDAO) while simultaneously listing prestigious past affiliations (Novartis, AstraZeneca). This dual role as both an industry veteran and a current stakeholder in the project raises potential conflicts of inter…

- **team_credibility** (info) · *project overview*
  - Quote: The lab is led by Dr. Viktor Korolchuk, a highly regarded researcher with extensive experience in autophagy and lysosomal biology.
  - Observation: The document relies on subjective adjectives ('highly regarded', 'extensive experience') rather than providing objective evidence of the team's specific track record, publication history, or prior success in drug discovery. While Dr. Korolchuk is a known figure, the lack of spec…

- **team_credibility** (info) · *team*
  - Quote: In addition to his academic work, Dr. Korolchuk is involved in several industry collaborations and has received funding from a variety of sources...
  - Observation: While the team has strong academic credentials, the explicit mention of 'industry collaborations' alongside the creation of a tokenized IP pool suggests potential dual roles or conflicts where academic interests may align with commercial token holders.

- **team_credibility** (info) · *use of funds*
  - Quote: advancing longevity research and IP development at the Korolchuk lab at Newcastle University
  - Observation: The document explicitly anchors the project to the Korolchuk lab at Newcastle University, a known leader in autophagy research. This provides a specific, credible institutional home for the scientific claims, distinguishing it from generic DAO projects.

- **team_credibility** (info) · *use of funds*
  - Quote: The Korolchuk laboratory has a computational biologist on staff, yet the objective is to harness superior SAR expertise from a global pool.
  - Observation: The text acknowledges a gap in internal expertise (SAR) and proposes a solution (global pool/hackathons). This demonstrates self-awareness regarding the team's limitations and a strategic plan to mitigate them.

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 174 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2024 | Targeting the autophagy-NAD axis protects against cell death in Niemann… | 10.1038/s41419-024-06770-y |
| 2 | None | 2020 | Report of the 23rd Meeting on Signal Transduction 2019—Trends in Cancer… | 10.3390/ijms21082728 |
| 3 | None | 2012 | Reactive oxygen species (ROS) homeostasis and redox regulation in cellu… | 10.1016/j.cellsig.2012.01.008 |
| 4 | None | 2026 | International Journal of Oncology | 10.3892/ijo |
| 5 | None | 2017 | Parkinson disease | 10.1038/nrdp.2017.13 |
| 6 | None | 2000 | The Hallmarks of Cancer | 10.1016/s0092-8674(00)81683-9 |
| 7 | None | 2018 | Hallmarks of Cellular Senescence | 10.1016/j.tcb.2018.02.001 |
| 8 | None | 2015 | Autophagy: a druggable process that is deregulated in aging and human d… | 10.1172/jci78652 |
| 9 | None | 2010 | AMP-activated Protein Kinase Signaling Activation by Resveratrol Modula… | 10.1074/jbc.m109.060061 |
| 10 | None | 2022 | Therapeutic application of quercetin in aging-related diseases: SIRT1 a… | 10.3389/fimmu.2022.943321 |
| 11 | None | 2010 | Chaperone-Mediated Autophagy Markers in Parkinson Disease Brains | 10.1001/archneurol.2010.198 |
| 12 | None | 2021 | Autophagy in metabolic disease and ageing | 10.1038/s41574-021-00551-9 |
| 13 | None | 2013 | First‐in‐class cardiolipin‐protective compound as a therapeutic agent t… | 10.1111/bph.12461 |
| 14 | None | 2013 | New horizons in the pathogenesis, diagnosis and management of sarcopenia | 10.1093/ageing/afs191 |
| 15 | None | 2013 | Autophagy in aging and neurodegenerative diseases: implications for pat… | 10.1016/j.neurobiolaging.2013.11.019 |
