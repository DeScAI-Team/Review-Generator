# Evidence audit trail

**Document:** vitafast-to-use-molecules-coin-to-company-legal-framework  
**Review date:** May 22, 2026  
**Composite score:** 0.5151  

*Full narrative review and plain-language overview are published separately (review.json / overview.json). This file traces citation grades, screener findings, and originality context.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:23:02Z
- **Generator:** `evidence-doc.py` v1.1 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(models used by upstream retrieve_compare / review / score steps)*
- **Git revision:** `94ba61e` *(repository containing the run, best-effort)*
- **Retrieve source file:** `retrieve_compare_llm.json`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `1c06b57c842143a4` |
| retrieve_compare_llm.json | `265143052cd5ba54` |
| screener.json | `35cb3088f3faed68` |
| originality.json | `0b46f671eddc005c` |

*Fingerprints are of the JSON files read at generation time; use them to verify this document matches a frozen artifact bundle.*

### Composite score

The **composite score** in `review.json` is produced by `articles/pipeline/empirical/score.py`, which combines category scores using **`dimension_weights`** in `articles/pipeline/mappings.json`. Dimensions absent from the review use weight 0 implicitly.

Current `dimension_weights`: evidential_strength=0.25; scientific_rigor=0.25; originality=0.2; real_world_traction=0.1; team_credibility=0.1; execution_credibility=0.05; financial_integrity=0.05.

### Reference support lines

In **References**, citations may show `(no verdict — missing abstract)` when OpenAlex had no abstract for that work, or `(no verdict — ungraded)` when the retrieve_compare step did not assign `support_verdict` (e.g. skipped LLM grading). These are **not** contradictions of the paper — they mark limits of automated checking.

## Category scores

| Dimension | Score | Method | Notes |
|-----------|------:|--------|-------|
| evidential_strength | 0.4000 | evidence_grade_weighted | claim_count=1 |
| execution_credibility | 0.3500 | evidence_grade_weighted | claim_count=1 |
| financial_integrity | 0.3500 | evidence_grade_weighted | claim_count=8 |
| originality | 1.0000 | literature_similarity | compared_works=89 |
| scientific_rigor | 0.3702 | evidence_grade_weighted | claim_count=16 |
| team_credibility | 0.3606 | evidence_grade_weighted | claim_count=6 |

## Evidence grade counts (retrieve_compare)

- **evidential_strength:** unverifiable: 1
- **execution_credibility:** unreferenced: 1
- **financial_integrity:** self_reported_method: 4; unreferenced: 4
- **governance_accountability:** unreferenced: 15; self_reported_method: 9; unverifiable: 1
- **originality:** unverifiable: 1
- **scientific_rigor:** unreferenced: 9; unverifiable: 6; self_reported_method: 1
- **team_credibility:** unreferenced: 4; self_reported_method: 1; unverifiable: 1

## Claim-level trace (non-self-reported)

*Listing excludes grades counted only internally (self_reported, self_reported_method). Use `--include-self-reported` for all claims.*

### governance_accountability / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> Token holders are DAO members with governance voice but no automatic equity rights.

### governance_accountability / aspirational · chunk 0 · VFDP-16 VITA-FAST: From IP-NFT to Real-World Asset - Entity Formation for Equity Fundraising One-Liner

**Grade:** `unverifiable`  

> Establish a dual-entity structure for VITA-FAST comprising (1) VitaFast DUNA as the community governance layer with membership for VITA-FAST token holders conferred by operation of the Charter and Association Agreement of VitaFast DUNA and (2) VitaFast LLC as the operating compa…

**References:**

- [1] ? → (no verdict — missing abstract)
- [2] ? → (no verdict — missing abstract)

### governance_accountability / aspirational · chunk 1 · Teaser

**Grade:** `unreferenced`  

> The DUNA will enter into an agreement with a third party (yet to be defined) to act as its ministerial agent for limited operational and clerical functions, ensuring the DUNA can take limited actions in the real world without centralizing control.

### governance_accountability / aspirational · chunk 2 · Summary

**Grade:** `unreferenced`  

> this proposal seeks approval to establish a dual-entity operational structure

### governance_accountability / aspirational · chunk 3 · Entity 1: VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> Coordinates governance and community decision-making

### governance_accountability / aspirational · chunk 3 · Entity 1: VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> Does NOT hold treasury (avoids securities classification concerns)

### governance_accountability / aspirational · chunk 3 · Entity 1: VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> Oversight over Ministerial Agent's Activities

### governance_accountability / aspirational · chunk 6 · Motivation

**Grade:** `unreferenced`  

> The dual-entity structure positions VITA-FAST to pursue equity financing from strategic investors, pharmaceutical companies, and longevity-focused funds while maintaining community governance.

### governance_accountability / aspirational · chunk 7 · 1. VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> The DUNA serves as the community coordination layer-a legally recognized wrapper that provides liability protection for token holders while enabling decentralized governance.

### governance_accountability / aspirational · chunk 8 · Key Characteristics:

**Grade:** `unreferenced`  

> Agreement will be entered into with a third party (yet to be defined) purely for ministerial services (e.g., appointing counsel, disbursing approved funds, record-keeping, reporting) under DUNA oversight.

### governance_accountability / aspirational · chunk 16 · Community Member Route:

**Grade:** `unreferenced`  

> Token holders must voluntarily lock tokens, complete KYC/AML verification, apply for contributor equity, and sign an AIPP Agreement to participate.

### governance_accountability / aspirational · chunk 20 · Phase 3: Ongoing Operations

**Grade:** `unreferenced`  

> Confirmation will be reported in Discord and on VITA-FAST governance channels.

### governance_accountability / aspirational · chunk 21 · Benefits

**Grade:** `unreferenced`  

> Commercialization Enabled: LLC provides clear counterparty for pharma partnerships and sublicenses research IP.

### governance_accountability / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> This proposal is consistent with: VDP-111 (VITA-FAST Governance): Token holder authority preserved via DUNA; LLC executes treasury decisions

### governance_accountability / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> Assignment Agreements: LLC manages sublicensing rights per Newcastle University agreements

### governance_accountability / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> FAM Membership Agreement: Token holder rights and governance participation maintained via DUNA

### team_credibility / aspirational · chunk 0 · VFDP-16 VITA-FAST: From IP-NFT to Real-World Asset - Entity Formation for Equity Fundraising One-Liner

**Grade:** `unverifiable`  

> Establish a dual-entity structure for VITA-FAST comprising (1) VitaFast DUNA as the community governance layer with membership for VITA-FAST token holders conferred by operation of the Charter and Association Agreement of VitaFast DUNA and (2) VitaFast LLC as the operating compa…

**References:**

- [1] ? → (no verdict — missing abstract)
- [2] ? → (no verdict — missing abstract)

### team_credibility / aspirational · chunk 6 · Motivation

**Grade:** `unreferenced`  

> The dual-entity structure positions VITA-FAST to pursue equity financing from strategic investors, pharmaceutical companies, and longevity-focused funds while maintaining community governance.

### team_credibility / aspirational · chunk 10 · 2. VitaFast LLC (Operating Layer)

**Grade:** `unreferenced`  

> VitaFast LLC is the operating company-conducting all business activities, holding license to IP and treasury, generating revenue, and enabling equity issuance through compliant securities exemptions.

### team_credibility / aspirational · chunk 11 · Key Characteristics:

**Grade:** `unreferenced`  

> The study involves a Newcastle autophagy program that generates research IP, which is licensed perpetually and worldwide with full ownership of developed products retained by the licensee.

### team_credibility / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> Assignment Agreements: LLC manages sublicensing rights per Newcastle University agreements

### financial_integrity / aspirational · chunk 3 · Entity 1: VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> Provides liability protection for VITA-FAST token holders

### financial_integrity / aspirational · chunk 3 · Entity 1: VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> Membership for VITA-FAST token holders conferred by operation of the Charter and Association Agreement for the DUNA upon qualifying participation through holding the VitaFast token

### financial_integrity / aspirational · chunk 11 · Key Characteristics:

**Grade:** `unreferenced`  

> The study involves a Newcastle autophagy program that generates research IP, which is licensed perpetually and worldwide with full ownership of developed products retained by the licensee.

### financial_integrity / aspirational · chunk 16 · Community Member Route:

**Grade:** `unreferenced`  

> Token holders must voluntarily lock tokens, complete KYC/AML verification, apply for contributor equity, and sign an AIPP Agreement to participate.

### scientific_rigor / empirical · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The dual-entity structure enables entity-level taxation, thereby avoiding pass-through complexity.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The dual-entity structure enabled by Wyoming's DUNA Act and Delaware's LLC framework permits for-profit activities while maintaining a nonprofit governance layer.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The dual-entity structure positions tokens to avoid securities classification.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The dual-entity structure provides legal existence and liability protection for the organization.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> The DUNA and LLC have distinct legal purposes and rights.

### scientific_rigor / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> Token holders are DAO members with governance voice but no automatic equity rights.

### scientific_rigor / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> Shareholders hold equity with economic rights via separate agreements.

### scientific_rigor / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> Tokens are classified as utility/commodity rather than securities.

### scientific_rigor / contextual · chunk 13 · VitaFast LLC - Operating Layer

**Grade:** `unreferenced`  

> Equity is issued only through compliant exemptions.

### scientific_rigor / contextual · chunk 17 · Investor Route:

**Grade:** `unreferenced`  

> Token locking enables cryptographic identity for shareholder voting and dividend distributions, commitment signaling that demonstrates alignment, and eligibility to petition for equity through compliant pathways.

### scientific_rigor / aspirational · chunk 4 · Entity 2: VitaFast LLC (Operating Layer)

**Grade:** `unreferenced`  

> This structure implements the C2C framework's categorical separation: tokens remain utility instruments for community membership, while equity flows through the LLC via established exemptions.

### scientific_rigor / aspirational · chunk 5 · Motivation

**Grade:** `unverifiable`  

> Previous approaches including ICOs, SAFTs, and 'sufficient decentralization' theories have proven inadequate for enabling broad community participation and decentralized governance without triggering securities compliance obligations.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The same person can be both a DAO member and a shareholder through distinct pathways within the Coin-to-Company model.

**References:**

- [1] ? → (no verdict — missing abstract)

### scientific_rigor / aspirational · chunk 7 · 1. VitaFast DUNA (Community Layer)

**Grade:** `unreferenced`  

> The DUNA serves as the community coordination layer-a legally recognized wrapper that provides liability protection for token holders while enabling decentralized governance.

### scientific_rigor / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> C2C Model: Implements categorical separation of tokens (utility) and equity (securities)

### originality / aspirational · chunk 5 · Motivation

**Grade:** `unverifiable`  

> Previous approaches including ICOs, SAFTs, and 'sufficient decentralization' theories have proven inadequate for enabling broad community participation and decentralized governance without triggering securities compliance obligations.

**References:**

- [1] ? → (no verdict — missing abstract)

### evidential_strength / empirical · chunk 5 · Motivation

**Grade:** `unverifiable`  

> The dual-entity structure enables entity-level taxation, thereby avoiding pass-through complexity.

**References:**

- [1] ? → (no verdict — missing abstract)

### execution_credibility / aspirational · chunk 22 · Alignment with Existing Framework

**Grade:** `unreferenced`  

> VITA-FAST Whitepaper: Enables commercialization pathway for autophagy research IP

## Document screener

- **financial_integrity** (concern) · *Relationship Between DUNA and LLC*
  - Quote: Members required to apply to become a shareholder in the LLC
  - Observation: The distinction that DUNA members must 'apply' to become LLC shareholders creates a two-tiered incentive structure where token holders have governance rights but no automatic economic rights. This decoupling may lead to misalignment between those governing the project and those …

- **financial_integrity** (info) · *Equity Financing Pathways*
  - Quote: Token holders voluntarily lock their tokens, they gain eligibility to apply for equity—but locking creates no automatic right, no option to purchase, and no enforceable claim.
  - Observation: The incentive structure relies on voluntary token locking which grants only 'eligibility' to apply for equity, not a right to purchase. This creates a significant disconnect between community participation (holding/locking tokens) and actual ownership/economic upside, potentiall…

## Originality (literature overlap)

**Originality score:** 1.0 · **Related works retrieved:** 89 · **Avg similarity:** 0.0

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | None | 2025 | Decentralized autonomous organizations: adapting legal structures and p… | 10.1093/cmlj/kmaf011 |
| 2 | None | 2024 | DAO Token Transferability: Property, Contract, and Technology | 10.1017/err.2024.93 |
| 3 | None | 2026 | A Quantitative Taxonomy of Regulatory Frameworks for Decentralized Auto… | 10.55277/researchhub.leu54yop.1 |
| 4 | None | 2025 | Cross-Chain Governance | 10.1515/9783839410974-007 |
| 5 | None | 2018 | The Lancet Commission on global mental health and sustainable developme… | 10.1016/s0140-6736(18)31612-x |
| 6 | None | 2002 | Assessing the impact of organizational practices on the relative produc… | 10.1016/s0048-7333(01)00196-2 |
| 7 | None | 2019 | Unicorns, Cheshire cats, and the new dilemmas of entrepreneurial finance | 10.1080/13691066.2018.1517430 |
| 8 | None | 2022 | Artificial Intelligence and Blockchain Integration in Business: Trends … | 10.1007/s10796-022-10279-0 |
| 9 | None | 2018 | Medicinal plants of the Andes and the Amazon - The magic and medicinal … | 10.32859/era.15.2.001-295 |
| 10 | None | 2021 | Federated learning for predicting clinical outcomes in patients with CO… | 10.1038/s41591-021-01506-3 |
| 11 | None | 2023 | A Review of the Role of Artificial Intelligence in Healthcare | 10.3390/jpm13060951 |
| 12 | None | 2019 | ‘Fit-for-purpose?’ – challenges and opportunities for applications of b… | 10.1186/s12916-019-1296-7 |
| 13 | None | 2020 | A Blockchain-Based Smart Contract System for Healthcare Management | 10.3390/electronics9010094 |
| 14 | None | 2019 | Strategy for a globally coordinated response to a priority neglected tr… | 10.1371/journal.pntd.0007059 |
| 15 | None | 2013 | SPIRIT 2013 explanation and elaboration: guidance for protocols of clin… | 10.1136/bmj.e7586 |
