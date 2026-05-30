# Proposal evidence audit trail

**Proposal:** Wim Hof Method Breathwork and Cold Exposure for Cancer-Related Inflammation: Feasibility Pilot  
**Review date:** May 22, 2026  
**Composite score:** 36/100  

*This file traces the screener findings, originality comparison, and funding assessment that produced the review. The review itself is in review.json.*

## Provenance

- **Generated (UTC):** 2026-05-22T06:30:33Z
- **Generator:** `proposals/pipeline/evidence_doc.py` v1.0 (no LLM)
- **VALIDATOR_MODEL:** `/model` *(model used by upstream proposal_pipe.py)*
- **Git revision:** `94ba61e`

| Input | SHA-256 (first 16 hex) |
|-------|-------------------------|
| review.json | `2b322f71ef6a51f3` |
| screener_findings.json | `c0bf77b743e75180` |
| originality.json | `e41107a299d868f2` |

### Composite score

The **composite score** is produced by `proposals/pipeline/proposal_pipe.py`, combining category scores using **`dimension_weights`** in `proposals/pipeline/proposal_mappings.json`.

Current `dimension_weights`: scientific_grounding=0.3; evidential_strength=0.25; funding_realism=0.25; originality=0.2.

## Category scores

| Dimension | Score |
|-----------|------:|
| evidential_strength | 30 |
| funding_realism | 35 |
| originality | 85 |
| scientific_grounding | 10 |

## Category rationales

### Evidential Strength (score: 30)

The proposal's evidential strength is currently limited by a reliance on popular science communicators rather than peer-reviewed literature to support key claims about measurement challenges. This approach weakens the foundational evidence for the intervention summary, as citations from figures like Dr. Andrew Huberman do not carry the same weight as academic studies. Furthermore, there is a notable tension in the analysis plan where the team proposes using causal machine learning to estimate effects, yet simultaneously admits that the small sample size will restrict results to an exploratory level. This creates a disconnect between the ambitious framing of establishing causal effects and the statistical reality of the proposed study design. Finally, the proposal correctly identifies the absence of a control group as a barrier to proving causality, yet the overall presentation suggests a definitive test of the Wim Hof Method's efficacy. This gap between the study's limitations and its stated goals raises questions about whether the preliminary evidence and design are sufficient to support the proposed research questions.

### Funding Realism (score: 35)

Funding snapshot: $100,000 requested, $18,505.40 raised (18.5% funded), 14 contributor(s), 8 of 229 days remaining, behind pace. The $100,000 budget is significantly misaligned with the scope of a feasibility pilot involving only 20 participants, particularly the $20,000 allocation for AI/ML development and $15,000 for blockchain infrastructure, which are disproportionate for such a small dataset. Critical gaps include the lack of a control group despite the study's inability to prove causality, and the acceptance of unstandardized wearable data as a covariate, which introduces high noise. The campaign is critically underfunded at 18.5% with only 8 days remaining and just 14 contributors, indicating a very low likelihood of reaching the goal and triggering potential refunds for backers. The team's institutional backing and methodological rigor appear insufficient to justify the heavy technical overhead relative to the limited clinical scope.

### Originality (score: 85)

The proposed study introduces a novel combination of the Wim Hof Method, a specific regimen involving controlled hyperventilation and cold exposure, within a feasibility framework for adults living with cancer. While the retrieved literature extensively covers exercise interventions like aerobic walking [2], yoga programs [3, 6], and mindfulness-based stress reduction [23] for cancer survivors, none of these works specifically investigate the safety and feasibility of the Wim Hof Method in this population. The unique pairing of cold exposure and specific breathing techniques with cancer patients, distinct from the purely physical or meditative approaches found in works such as [1] and [20], represents a genuine gap in the current research landscape. Furthermore, the inclusion of a healthy volunteer observational cohort alongside the patient group to compare adherence and safety profiles adds a comparative dimension not present in the single-arm pilot studies typical of the retrieved works.

The proposal builds upon well-established methodological foundations found in the related literature, particularly regarding study design and outcome measurement. The use of a pilot or feasibility study design to assess recruitment, retention, and adherence aligns closely with the approaches taken in CaRE @ Home [1] and the GO-EXCAP study [2]. Additionally, the plan to utilize consumer-grade wearables to measure heart rate variability mirrors the technological integration seen in research on wearable devices for biobehavioral data collection [7, 11]. The selection of inflammatory biomarkers such as hs-CRP and IL-6 is also consistent with existing studies examining systemic inflammation in cancer contexts [13, 14]. However, while these individual components are familiar, their specific application to the Wim Hof Method in a cancer population remains unexplored in the provided search results.

Contextually, this proposal represents a meaningful methodological contribution by shifting the focus from efficacy to safety and feasibility for a specific, under-researched non-pharmacological intervention. Most existing studies in the field, such as those on yoga or general exercise, have moved beyond initial feasibility to examine physiological and psychological outcomes in established cohorts [3, 6, 23]. This project fills a critical niche by determining whether the unique physiological stressors of the Wim Hof Method can be safely managed by immunocompromised or treatment-recovering cancer patients before larger controlled trials are attempted. It advances the field by validating a distinct intervention modality that differs significantly from the somatic therapies and traditional exercise regimens currently documented in the literature [18, 39].

Based on comparison with 73 related works, this proposal receives an originality score of 0.8508 out of 1.00, reflecting a high degree of novelty due to the specific application of the Wim Hof Method in a cancer population, despite utilizing standard feasibility designs and outcome measures found in broader cancer rehabilitation literature.

### Scientific Grounding (score: 10)

The proposal demonstrates methodological awareness by selecting non-parametric statistical tests suitable for small sample sizes and detailing specific safety protocols for high-risk chemotherapy participants. However, significant concerns arise regarding the scientific rigor of the data collection and intervention claims. The authors explicitly accept substantial variability in wearable device measurements without mandating specific hardware, relying instead on documenting device type as a covariate, which may introduce unmanageable noise into heart rate variability data. Furthermore, the claim that cold water immersion protocols are 'empirically proven' to reach specific temperatures lacks citation support and uses imprecise scientific language. The study design is also limited by the absence of a formal control group, which restricts the ability to draw causal inferences from the primary outcomes. While the use of blockchain for data integrity is a notable technical feature, the overall grounding in established literature appears weak due to these methodological shortcuts and unsupported assertions.

## Document screener findings

**Windows scanned:** 5  
**Raw findings:** 18  
**After deduplication:** 18  

- **evidential_strength** (concern) · *intervention_summary*  Tags: SourceAttribution
  - Quote: Among others, Dr. Andrew Huberman and Dr. Susanna Soberg have expressed some of the key challenges that cold showers represent...
  - Observation: The proposal relies on citations to popular science communicators (Huberman, Soberg) rather than peer-reviewed literature to support claims about measurement challenges, weakening the evidential basis.

- **evidential_strength** (concern) · *analysis plan*  Tags: Causal
  - Quote: Causal machine learning to move beyond association and prediction... These approaches can help estimate whether adherence to the Wim Hof protocol has an identifiable causal effect... Given the small …
  - Observation: The proposal claims to use causal machine learning to estimate causal effects, yet simultaneously admits the results will be exploratory due to small sample size. This creates a tension between the ambitious causal framing and the limited statistical power to support such claims.

- **evidential_strength** (concern) · *limitations*  Tags: Causal, Benchmark
  - Quote: This study cannot prove WHM causes changes in biomarkers due to no control group.
  - Observation: The proposal correctly identifies that without a control group, the study cannot establish causality, yet the title and introduction likely imply testing the efficacy of Wim Hof Method, creating a gap between the study design and the ultimate research question.

- **funding_realism** (concern) · *milestones*  Tags: Feasibility
  - Quote: Recruitment begins with target of 15 to 20 participants over 4 to 6 weeks.
  - Observation: Recruiting 15-20 participants with required oncologist clearances and baseline ECGs within 4-6 weeks is an aggressive timeline that risks delaying the study or failing to reach the target, potentially compromising the power of the exploratory analyses.

- **funding_realism** (info) · *budget*  Tags: Budget
  - Quote: AI and ML model development: $20,000 for time-series analysis, causal inference, pattern discovery, and data engineering
  - Observation: The budget allocates $20,000 for AI/ML development on a dataset of only 20 participants over 4-6 weeks, which seems disproportionately high for the scope of data available.

- **funding_realism** (info) · *analysis plan*  Tags: Feasibility
  - Quote: Should HRV be made optional or exploratory given device variability?
  - Observation: The proposal acknowledges significant device variability for Heart Rate Variability (HRV) measurements and suggests making this metric optional or exploratory. This indicates a realistic assessment of technical limitations and a pragmatic approach to data quality in a pilot study.

- **originality** (info) · *intervention_summary*  Tags: GapStatement
  - Quote: Conversely it is currently scientifically unproven or complex to normalize a protocol to consistently measure impact of cold exposure in a shower...
  - Observation: The proposal identifies a gap in the literature regarding standardized measurement of cold shower effects, justifying the need for this study, though the gap statement is not fully supported by cited references.

- **originality** (info) · *data, privacy, openness*  Tags: NoveltyAssertion
  - Quote: Blockchain-verified data provenance: To ensure data integrity we use decentralized data management infrastructure with blockchain verification.
  - Observation: The proposal introduces blockchain for data provenance and integrity. While technically novel for research data management, its scientific necessity for a small pilot study is debatable and may represent a distraction from core scientific goals.

- **scientific_grounding** (concern) · *measures*  Tags: Methodological, Limitation
  - Quote: We acknowledge measurement variability across devices but prioritize real-world feasibility over perfect standardization for this pilot.
  - Observation: The proposal explicitly accepts device-to-device variability in wearable data without specifying how this will be statistically controlled or if specific devices will be mandated, which threatens data comparability.

- **scientific_grounding** (concern) · *intervention_summary*  Tags: Methodological
  - Quote: Empirically it is proven that it is likely and practical with a simple CWI protocol to reach 4°C or colder with consistent full body exposure.
  - Observation: The use of the phrase 'empirically it is proven' is scientifically imprecise and lacks citation support for such a strong claim regarding cold water immersion protocols.

- **scientific_grounding** (concern) · *methods*  Tags: Methodological, Limitation
  - Quote: We acknowledge measurement variability across devices but prioritize real-world feasibility over perfect standardization for this pilot. Device type will be documented as a covariate.
  - Observation: The proposal explicitly accepts device variability without standardization, relying on it as a covariate. While pragmatic for a pilot, this introduces significant noise that may obscure true effects, and the justification for 'perfect standardization' being unfeasible is not elaborated with prior literature.

- **scientific_grounding** (concern) · *limitations*  Tags: Methodological, Limitation
  - Quote: Primary cancer cohort is uncontrolled, limiting causal inference. Healthy volunteer observational cohort serves as supplementary reference data only and is not used as a scientific control group.
  - Observation: The proposal explicitly acknowledges the lack of a control group and the inability to make causal claims, which is appropriate for a feasibility pilot but limits the scientific rigor of the primary outcomes.

- **scientific_grounding** (concern) · *analysis plan*  Tags: Methodological, Measurement
  - Quote: Wearable variability means different devices may measure HRV differently, documented as covariate.
  - Observation: Relying on participant-owned wearables with varying measurement standards introduces significant noise into HRV data; treating device type merely as a covariate may not adequately address systematic measurement differences.

- **scientific_grounding** (concern) · *methods*  Tags: Methodological, Limitation
  - Quote: Is the physician-gated observational approach with medical safety oversight sufficient or do you recommend additional ethics review procedures?
  - Observation: The proposal explicitly questions whether its own ethical safeguards (physician-gated approach) are sufficient, indicating uncertainty about the rigor of its ethical design. This self-doubt suggests the methodology may lack the robust ethical framework expected for human subject research.

- **scientific_grounding** (info) · *eligibility*  Tags: Methodological
  - Quote: Participants on active chemotherapy must have written oncologist approval in addition to GP clearance.
  - Observation: The inclusion of specific medical clearance requirements for high-risk subgroups (chemotherapy patients) demonstrates a thoughtful approach to safety and study design.

- **scientific_grounding** (info) · *analysis plan*  Tags: Methodological
  - Quote: Statistical approach: Paired comparisons from baseline versus week 16 using Wilcoxon signed-rank tests which are non-parametric and appropriate for small sample size.
  - Observation: The choice of non-parametric tests is methodologically sound given the anticipated small sample size and likely non-normal distribution of biomarker data, showing attention to statistical rigor.

- **scientific_grounding** (info) · *safety*  Tags: Methodological
  - Quote: Protocol hold criteria for active chemotherapy participants: Practice must be temporarily suspended if participant develops fever above 100.4°F (38°C), active infection, significant dehydration, acti…
  - Observation: The safety protocol for immunocompromised patients (chemotherapy) is detailed and aligns with standard clinical precautions, demonstrating appropriate risk management for this vulnerable population.

- **scientific_grounding** (info) · *methods*  Tags: Methodological
  - Quote: Blockchain-verified data provenance: To ensure data integrity we use decentralized data management infrastructure with blockchain verification.
  - Observation: The proposal details a specific technical approach using Ethereum and IPFS for data integrity, which is a notable methodological choice for ensuring transparency in an open-science context.

## Originality (literature overlap)

**Originality score:** 0.8508 · **Related works retrieved:** 98 · **Avg similarity:** 0.1492

| Rank | Similarity | Year | Title | DOI |
|-----:|-----------:|------|-------|-----|
| 1 | 0.6500 | 2020 | CaRE @ Home: Pilot Study of an Online Multidimensional Cancer Rehabilit… | 10.3390/jcm9103092 |
| 2 | 0.6200 | 2022 | A single-arm pilot study of a mobile health exercise intervention (GO-E… | 10.1182/bloodadvances.2022007056 |
| 3 | 0.5800 | 2013 | Effect of an office worksite-based yoga program on heart rate variabili… | 10.1186/1472-6882-13-82 |
| 4 | 0.4200 | 2018 | Impact of supportive therapy modalities on heart rate variability in ca… | 10.1080/09638288.2018.1514664 |
| 5 | 0.4200 | 2018 | Novel mHealth App to Deliver Geriatric Assessment-Driven Interventions … | 10.2196/10296 |
| 6 | 0.4200 | 2020 | Yoga Research: A Narrative Review | 10.19080/jyp.2020.08.555742 |
| 7 | 0.3800 | 2021 | Use of Physiological Data From a Wearable Device to Identify SARS-CoV-2… | 10.2196/26107 |
| 8 | 0.3500 | 2024 | Non-pharmacological immunomodulation | 10.54195/9789465150017 |
| 9 | 0.3500 | 2022 | A Scalable Risk-Scoring System Based on Consumer-Grade Wearables for In… | 10.2196/35717 |
| 10 | 0.3500 | 2021 | The Efficacy of Somatic Therapies in Trauma Recovery | ? |
| 11 | 0.3200 | 2020 | Guidelines for wrist-worn consumer wearable assessment of heart rate in… | 10.1038/s41746-020-0297-4 |
| 12 | 0.2800 | 2010 | Outcomes for Implementation Research: Conceptual Distinctions, Measurem… | 10.1007/s10488-010-0319-7 |
| 13 | 0.2800 | 2008 | Rosuvastatin to Prevent Vascular Events in Men and Women with Elevated … | 10.1056/nejmoa0807646 |
| 14 | 0.2800 | 2015 | Inflammatory biomarkers, cerebral microbleeds, and small vessel disease | 10.1212/wnl.0000000000001279 |
| 15 | 0.2500 | 2015 | The Internet of Things for Health Care: A Comprehensive Survey | 10.1109/access.2015.2437951 |
| 16 | 0.2500 | 2021 | Dietary patterns and biomarkers of oxidative stress and inflammation: A… | 10.1016/j.redox.2021.101869 |
| 17 | 0.2200 | 2022 | Breathing: a Powerfull Tool for Physical &amp; Neuropsychological Regul… | 10.47577/tssj.v28i1.5922 |
| 18 | 0.2200 | 2023 | Multimodal non-invasive non-pharmacological therapies for chronic pain:… | 10.1186/s12916-023-03076-2 |
| 19 | 0.2200 | 1996 | A Pilot Study for a Randomized Controlled Trial to Prevent Gastric Canc… | 10.1111/j.1349-7006.1996.tb00276.x |
| 20 | 0.2200 | 2021 | Mindfulness-Based Compassion Training for Health Professionals Providin… | 10.1089/jpm.2020.0358 |
| 21 | 0.2200 | 2023 | Exploring causal correlations between inflammatory cytokines and system… | 10.3389/fimmu.2022.985729 |
| 22 | 0.1800 | 2016 | Creating Live Interactions to Mitigate Barriers (CLIMB): A Mobile Inter… | 10.2196/mental.6671 |
| 23 | 0.1500 | 2019 | Mindfulness-based stress reduction for women diagnosed with breast canc… | 10.1002/14651858.cd011518.pub2 |
| 24 | 0.1500 | 2021 | Exoskeleton-Assisted Anthropomorphic Movement Training (EAMT) for Posts… | 10.1016/j.apmr.2021.06.001 |
| 25 | 0.1500 | 2017 | Resveratrol regulates neuro-inflammation and induces adaptive immunity … | 10.1186/s12974-016-0779-0 |

*… and 73 additional related work(s) not shown.*

## Funding snapshot

Funding snapshot: $100,000 requested, $18,505.40 raised (18.5% funded), 14 contributor(s), 8 of 229 days remaining, behind pace. The $100,000 budget is significantly misaligned with the scope of a feasibility pilot involving only 20 participants, particularly the $20,000 allocation for AI/ML development and $15,000 for blockchain infrastructure, which are disproportionate for such a small dataset. Critical gaps include the lack of a control group despite the study's inability to prove causality, and the acceptance of unstandardized wearable data as a covariate, which introduces high noise. The campaign is critically underfunded at 18.5% with only 8 days remaining and just 14 contributors, indicating a very low likelihood of reaching the goal and triggering potential refunds for backers. The team's institutional backing and methodological rigor appear insufficient to justify the heavy technical overhead relative to the limited clinical scope.
