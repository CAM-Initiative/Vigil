# VIGIL Failure Taxonomy — External Evidence Validity Review

**Date:** 2026-09-11  
**Status:** AUDIT — non-normative research evidence  
**Reviewer:** Dr M.V. O'Rourke  
**Scope:** Current selectable VIGIL Failure Taxonomy classes on `agent/incident-ecosystem-ingestion`, including VIGIL-FC-000068.

## Purpose

This review tests the external evidentiary validity of the VIGIL Failure Taxonomy before class-level references are populated at scale. It is not a citation-filling exercise. A source is relevant only where it materially supports the existence of a mechanism, the boundary of a mechanism, or a governance/assurance expectation that helps distinguish the class.

The review deliberately separates four evidence functions:

1. **Research / evaluation evidence** — supports that a mechanism exists, recurs, can be reproduced, or has an empirically studied analogue.
2. **Government / regulatory evidence** — supports that a boundary, risk, duty, or governance concern is institutionally recognised.
3. **International standards evidence** — supports formal lifecycle, assurance, traceability, oversight, access-control, risk-management, data-quality, or governance expectations. Broad standards are not treated as proof of a narrow mechanism unless the public text actually supports that inference.
4. **Incident evidence** — demonstrates occurrence in deployment or evaluation. Incident evidence remains primarily canonical in VIGIL Incident records and should not be duplicated into class bibliographies merely to increase citation count.

A fifth role, **contextual evidence**, is appropriate where scholarship or guidance helps explain a boundary but does not itself establish the mechanism.

## Evidence-strength labels

- **STRONG** — multiple independent or high-authority sources materially support the mechanism or a close established analogue and the proposed class boundary is defensible.
- **PARTIAL** — external evidence supports the underlying phenomenon or adjacent control requirement, but VIGIL's mechanism-level separation is more specific than the source vocabulary.
- **VIGIL-EMERGENT** — the class is a defensible synthesis from incidents and adjacent literatures, but no sufficiently direct external source was identified in this pass that names or cleanly isolates the mechanism at the same abstraction.
- **EVIDENTIARY CONCERN** — insufficient basis to support the class as presently bounded. No class reached this threshold in this pass; emergent classes should nevertheless remain under review.

These labels are audit diagnostics only and should not be published as taxonomy fields at this stage.

## Source-handling rules

- Prefer primary standards bodies, regulators, government publications, peer-reviewed/open research, and original evaluation reports.
- Do not treat a standard's existence as evidence that it contains a clause that has not been inspected.
- Where VIGIL records an ISO source as `official-metadata-only` or `blocked-access`, use the official abstract only for claims visible in that abstract unless an authorised derivative mapping or accessible clause extract independently supports more detail.
- Do not use regulation as proof that a technical mechanism exists; use regulation to support a recognised boundary, governance objective, or harm/control concern.
- Do not turn a research analogue into a claim of legal non-compliance.
- Reuse one source across multiple classes only where the source independently supports each class; the publication renderer will de-duplicate the bibliography.

## Principal cross-taxonomy sources identified

| Source | Evidence role | Relevant themes |
|---|---|---|
| ISO/IEC 42001:2023, *Artificial intelligence — Management system* | standards-evidence | AI management systems, risk controls, accountability, traceability, transparency, continual improvement |
| ISO/IEC 23894:2023, *AI — Guidance on risk management* | standards-evidence | lifecycle AI risk management |
| ISO/IEC 42005:2025, *AI system impact assessment* | standards-evidence | impact identification, documentation, lifecycle reassessment, accountability |
| ISO/IEC 5259-5:2025, *Data quality governance framework* | standards-evidence | data quality governance, responsibility, monitoring, lifecycle controls |
| ISO/IEC FDIS 42105, *Guidance for human oversight of AI systems* | contextual-evidence until published | human control, monitoring, autonomy, oversight across lifecycle |
| NIST AI RMF 1.0 / AIRC Core | authoritative-guidance | roles, oversight, scope, third-party risk, risk controls, lifecycle documentation |
| NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* | authoritative-guidance / research-evidence | poisoning, evasion, privacy and misuse attacks |
| NISTIR 8312, *Four Principles of Explainable Artificial Intelligence* | authoritative-guidance | explanation accuracy, knowledge limits, meaningfulness |
| NIST SP 800-63B-4, *Digital Identity Guidelines: Authentication and Authenticator Management* | authoritative-guidance | authenticated sessions, timeout, reauthentication, session continuity |
| OECD AI Principles — robustness/safety and accountability | authoritative-guidance | traceability, lifecycle records, inquiry, risk management and accountability |
| UNESCO Recommendation on the Ethics of Artificial Intelligence | authoritative-guidance | human agency, oversight, traceability, privacy, national sovereignty, benefit sharing |
| EU AI Act, especially Articles 5, 12, 13 and 14 | regulatory-evidence | manipulative/exploitative practices, logging, transparency and human oversight |
| OAIC APP 6 guidance and guidance on privacy and AI/model training | regulatory-evidence | primary/secondary purpose, consent, reasonable expectations and AI training reuse |
| IETF RFC 9700, *Best Current Practice for OAuth 2.0 Security* | standards-evidence | minimum privileges, audience/resource/action restriction, token scope |
| W3C PROV-DM / PROV family | standards-evidence | entities, activities, agents, derivation, attribution and provenance relationships |
| OWASP LLM Top 10 / Authorization guidance | contextual / standards-adjacent | least privilege, per-object authorization, prompt injection, excessive agency, deterministic controls |
| Tramèr et al. (USENIX Security 2016), *Stealing Machine Learning Models via Prediction APIs* | research-evidence | black-box API model extraction and functional duplication |
| Zhao et al. (2025), *A Survey on Model Extraction Attacks and Defenses for Large Language Models* | research-evidence | LLM functionality extraction, API-based knowledge distillation and extraction defenses |
| NSA/FBI/CISA (2026), *China-Based Artificial Intelligence Companies Conducting Industrial-Scale Distillation Campaigns Against U.S. AI Companies* | authoritative-guidance | industrial-scale systematic extraction of restricted frontier-model capabilities for downstream training; explicitly distinguishes legitimate distillation |
| METR monitorability / frontier-risk evaluations | research-evidence | monitor avoidance, monitoring failure modes, control coverage and agentic side tasks |
| Anthropic sycophancy research | research-evidence | model agreement with user beliefs/preferences over truthful or independent evaluation |
| Goddard et al. automation-bias systematic reviews | research-evidence | over-reliance on automated decision support and reduced independent verification |
| FTC dark-patterns report | regulatory-evidence | practices that obscure, subvert or impair consumer choice |
| ACCC Digital Platform Services Inquiry / EU Digital Markets Act materials | regulatory-evidence | gatekeeper power, dependency, lock-in and infrastructural leverage |
| Chandy & Lamport, *Distributed Snapshots* | research-evidence | consistent state capture and distributed-state recovery analogues |
| CWE-367, TOCTOU Race Condition | authoritative technical taxonomy | state-changing-after-check analogue relevant to post-verification mutation |

## Class-by-class external-validity assessment

### FF-0001 — Authority Boundary Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000001 Source-Authority Confusion | STRONG | W3C PROV; NIST AI RMF; OECD traceability | Provenance identifies source/agent role; authority consequences are VIGIL's governance application. |
| FC-000002 Capability-Authority Conflation | STRONG | RFC 9700; OWASP Excessive Agency; NIST AI RMF | Strong established distinction between technical capability/credential possession and least-privilege authorization. |
| FC-000003 Target and Scope Authority Transposition | STRONG | RFC 9700; OWASP Authorization guidance | Audience/resource/action restrictions directly support scope- and target-bound authorization. |
| FC-000005 Transformation-Mediated Authority Laundering | PARTIAL | OWASP Prompt Injection; NIST third-party/component risk | Strong evidence that transformed/untrusted content can cross trust boundaries; the explicit authority-laundering abstraction is more specific to VIGIL. |
| FC-000006 Control-Plane Authority Crossover | PARTIAL | OWASP Excessive Agency; zero-trust/control-plane security literature | Established privilege-boundary problem, but VIGIL's control-plane/subject-matter authority separation is a narrower governance synthesis. |
| FC-000009 Transitive Authority Propagation | STRONG | RFC 9700; least-privilege/confused-deputy security literature | Authorization does not automatically propagate through delegation or downstream services. |
| FC-000046 Inferential-Evidence Authority Conflation | PARTIAL | NISTIR 8312 knowledge limits/explanation accuracy; OECD transparency | Strong support for preserving epistemic limits; treating inference as an authority grant is VIGIL's mechanism-level synthesis. |
| FC-000053 Identity-Representation Authority Conflation | PARTIAL | NIST SP 800-63; W3C PROV; identity-security literature | Identity representation and authenticated identity are well distinguished externally; conversion of representation into governance authority is narrower. |
| FC-000054 Multiparty Participant Authority Transposition | PARTIAL | privacy consent doctrine; RFC 9700 resource-owner scope; multiparty privacy research | Sources support participant-specific consent/authority but do not generally isolate this exact mechanism. |
| FC-000055 Secondary-Purpose Authority Transposition | STRONG | OAIC APP 6; OAIC AI/model-training guidance; purpose-limitation privacy principles | Exceptionally strong boundary support: authority/collection for one purpose does not automatically establish secondary-purpose use. |
| FC-000057 Cross-Principal State Authority Transposition | STRONG | OWASP Authorization guidance; IDOR/BOLA literature; RFC 9700 | Per-principal/per-object authorization is a mature security boundary. |
| FC-000064 Objective-Pathway Authority Dominance | PARTIAL | reward/specification-gaming research; Anthropic reward-tampering and agentic-misalignment evaluations | Strong evidence that objectives can drive opportunistic pathways; VIGIL adds the explicit unresolved-authority/admissibility boundary. |
| FC-000068 Industrial-Scale Unauthorised Capability Extraction | STRONG | Tramèr et al.; LLM model-extraction survey; NSA/FBI/CISA 2026 advisory | Strong technical lineage for model extraction plus direct authoritative description of systematic industrial-scale capability extraction for downstream training. Keep legality/authority claim bounded: extraction/distillation itself is not inherently prohibited. |

### FF-0002 — Provenance & Lineage Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000010 Authorship or Source Misattribution | STRONG | W3C PROV; OECD traceability | Direct support for provenance attribution among entities, activities and agents. |
| FC-000011 Untraceable Synthesis | STRONG | W3C PROV derivation; OECD traceability; NIST lifecycle documentation | Strong support for retaining materially relevant source and transformation lineage. |
| FC-000012 Cross-Context Lineage Distortion | PARTIAL | W3C PROV; RFC 9700 audience/context restriction | Context-dependent applicability is recognised, but the cross-session/project semantic-distortion class is more specific. |
| FC-000013 Transformation Lineage Collapse | STRONG | W3C PROV derivation/activity model | Direct conceptual fit to preserving transformations between antecedent and derived artefacts. |
| FC-000014 False Continuity Attribution | VIGIL-EMERGENT | distributed-state/checkpoint literature; W3C provenance concepts | Literature supports state identity, snapshots and reconstruction, but no sufficiently direct source was found that isolates falsely asserted continuity across uncertain reconstruction at this abstraction. |
| FC-000015 Target-Object Binding Failure | STRONG | W3C PROV; RFC 9700 audience/resource binding; object-level authorization literature | Strong analogue in explicit entity/resource binding. |
| FC-000047 Unsupported Mechanism Attribution | STRONG | NISTIR 8312 explanation accuracy and knowledge limits | Direct support for ensuring explanations reflect the system/process and do not exceed knowledge limits. |

### FF-0003 — Verification & Completion Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000016 Required Verification Omission | STRONG | NIST AI RMF measurement/evaluation; ISO/IEC 42001/23894 lifecycle assurance | Strong assurance principle; specific verification requirement remains task-dependent. |
| FC-000017 False-Success Representation | PARTIAL | software assurance/testing literature; NIST AI RMF | Established difference between attempted and verified outcomes, but VIGIL's representation mechanism is more specific than broad assurance sources. |
| FC-000018 Completion-Condition Mismatch | PARTIAL | specification-gaming literature; software verification/acceptance criteria | External work strongly supports proxy-vs-objective mismatch; VIGIL applies this specifically to task completion representations. |
| FC-000019 Post-Verification Mutation | STRONG | CWE-367 TOCTOU; change-control and revalidation practice | Very strong structural analogue: a check is invalidated by material state change before use/reliance. |
| FC-000020 Stale Verification Reuse | STRONG | ISO/IEC 42005 lifecycle reassessment; NIST continuous monitoring/change management | Strong support for re-evaluating assurance when system/context changes materially. |
| FC-000062 Epistemic Reliance Miscalibration | STRONG | NISTIR 8312 knowledge limits; NIST GenAI Profile; automation-bias literature | Strong evidence for confidence/reliance calibration and harms from over-reliance where downstream assurance requirements are consequential. |
| FC-000063 Adversarial Evidence Poisoning Acceptance | STRONG | NIST AI 100-2e2025; prompt-injection/RAG-poisoning research | Direct established adversarial-ML category; VIGIL appropriately focuses on acceptance into an evidence-bearing pathway. |

### FF-0004 — Observability & Audit Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000022 Material Event Non-Capture | STRONG | EU AI Act Art. 12; OECD traceability; NIST logging/audit practice | Direct support for automatic logging/records sufficient for traceability and review. |
| FC-000023 Monitor Circumvention or Coverage Bypass | STRONG | METR monitorability evaluations; frontier-risk reporting | Direct research evidence for agents/side tasks avoiding or defeating monitoring. |
| FC-000024 Audit-Trail Non-Reconstructability | STRONG | OECD traceability; EU AI Act Art. 12; W3C PROV | Strong support for records sufficient for subsequent analysis and inquiry, not mere log existence. |
| FC-000025 Actor–Action Attribution Loss | STRONG | W3C PROV agent/activity attribution; OECD accountability | Direct conceptual support for attribution of actions to responsible actors/processes. |
| FC-000026 Hidden Material Execution Path | PARTIAL | METR monitorability; OWASP agentic guidance | External evidence establishes consequential alternate/agentic paths and monitoring blind spots; VIGIL isolates hidden topology from event non-capture and monitor bypass. |
| FC-000027 Audit Evidence Integrity Loss | STRONG | security logging/audit-integrity standards; NIST security controls; OECD traceability | Mature integrity requirement for audit evidence. |
| FC-000029 Execution State Non-Disclosure | PARTIAL | EU AI Act transparency; NISTIR 8312 explanation accuracy; OECD transparency | Strong expectation that users/overseers receive meaningful system-state information, but exact execution-state disclosure is context-dependent. |
| FC-000030 Material Signal Fragmentation | PARTIAL | distributed observability/correlation literature; OECD traceability | Strong adjacent evidence for correlation and end-to-end observability, but VIGIL's fragmentation mechanism is more granular. |
| FC-000044 Primary Evidence Accessibility Failure | PARTIAL | OECD accountability/traceability; audit and assurance principles | Evidence availability for authorised review is strongly supported, but “primary evidence accessibility” is a VIGIL-specific separation from evidence existence/integrity. |
| FC-000045 Authorised Investigative Evidence Access Pathway Failure | VIGIL-EMERGENT | auditability, due-process and assurance access principles | The need for authorised review is well established; failure of the governed *pathway* for investigators is a useful VIGIL abstraction not cleanly isolated in the sources reviewed. |

### FF-0005 — Access & Session State Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000031 Authentication-State Continuity Failure | STRONG | NIST SP 800-63B-4 | Direct support for authenticated-session state, timeouts, reauthentication, termination and session management. |
| FC-000032 Access-State Collapse | PARTIAL | NIST digital-identity guidance; access-control state models | External standards distinguish materially different states; the failure caused by collapsing those states into one representation is more specific. |
| FC-000048 Verification-Dependency Access Failure | VIGIL-EMERGENT | identity recovery/fallback guidance; resilience/accessibility principles | Strong adjacent practice around recovery and alternative authentication, but no direct general standard was identified for the exact dependency-without-proportionate-fallback mechanism. |

### FF-0006 — Work-State Continuity Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000034 Continuity Anchor Failure | PARTIAL | checkpointing/distributed-snapshot literature; provenance identity | Stable checkpoint/task binding is well established technically; VIGIL's “anchor” abstraction is broader and governance-oriented. |
| FC-000035 Material Work-State Persistence Failure | STRONG | Chandy–Lamport/distributed checkpointing; contingency/recovery practice | Strong technical support for persisting state required for correct continuation and recovery. |
| FC-000036 Restoration-State Integrity Failure | STRONG | distributed checkpoint/recovery literature; NIST contingency/recovery guidance | Strong established requirement that recovered state be internally consistent and suitable for continuation. |
| FC-000056 Synthetic Conversational Turn-State Coordination Failure | VIGIL-EMERGENT | distributed-state consistency; multi-agent coordination literature | The general coordination problem is well established, but the synthetic conversational turn-state mechanism is more specific than identified external taxonomies. |

### FF-0007 — Governance Control Reach Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000040 Control-State Preservation Failure | PARTIAL | policy/authorization propagation; zero-trust principles; NIST AI RMF controls | External practice supports preserving operative policy state across components; VIGIL's exact downstream governance-state mechanism is more specific. |
| FC-000041 Required Governance Route Bypass | STRONG | METR monitorability/control-bypass evidence; OWASP Excessive Agency; NIST oversight requirements | Strong support that consequential actions must traverse required controls/approval paths and alternate routes create material failures. |
| FC-000042 Governance Signal Delivery Dead End | PARTIAL | safety/control-system escalation literature; NIST AI RMF oversight processes | Delivery/escalation pathways are established, but VIGIL cleanly isolates “signal exists but reaches no capable decision point.” |

### FF-0008 — Control Activation Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000037 Control Availability Ambiguity | PARTIAL | resilience/monitoring standards; NIST AI RMF control documentation | Control availability is operationally important; ambiguity-before-activation is a VIGIL-specific separation. |
| FC-000038 Required Control Non-Activation | STRONG | NIST AI RMF; ISO/IEC 42001; EU AI Act human-oversight requirements | Strong governance support for controls being operative when applicable; incident/evaluation evidence can establish specific missed triggers. |
| FC-000043 Unwarranted Control Activation | PARTIAL | safety-control precision/false-positive literature; proportionality principles | External literature supports false-positive and overblocking risk, but the general governance activation class is broader than a named standard category. |

### FF-0009 — Agency-Preserving Influence Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000049 Dependency-Cultivation Optimisation | PARTIAL | longitudinal/observational AI emotional-dependence studies; platform engagement literature | Evidence supports emotional dependence/problematic use as a real outcome. Stronger evidence is still needed before claiming that dependency cultivation is a general optimisation mechanism rather than a possible product/design mechanism. |
| FC-000050 Protected-Signal Influence Repurposing | STRONG | EU AI Act Art. 5 vulnerability exploitation; privacy purpose limitation; child/vulnerability safeguards | Direct regulatory recognition that exploiting vulnerability to distort behaviour is unacceptable; purpose limitation supports the repurposing boundary. |
| FC-000051 Relationally Conditioned Epistemic Steering | STRONG | sycophancy research; autonomy/choice literature | Sycophancy work directly shows models conditioning responses on user beliefs/preferences in ways that can favour agreement over truth. |
| FC-000052 Instrumental Choice Manipulation | STRONG | EU AI Act Art. 5; FTC dark patterns; UNESCO human agency | Strong cross-domain support for concealed/manipulative techniques that materially impair autonomous choice. |
| FC-000065 Consequential Decision Grounding Bypass | STRONG | automation-bias systematic reviews; NIST human-AI oversight guidance | Strong evidence that users can over-rely on automated recommendations and reduce independent information seeking/verification in consequential decisions. |
| FC-000066 Evaluative Assent Collapse | STRONG | sycophancy research | Strong direct evidence that models can systematically favour agreement with user preferences/beliefs rather than independent evaluation. |

### FF-0010 — Infrastructural Authority Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000058 Dependency-Derived Governance Authority | PARTIAL | EU Digital Markets Act gatekeeper rationale; ACCC Digital Platform Services Inquiry; UNESCO sovereignty principles | External sources establish dependency, lock-in and gatekeeper power. VIGIL's distinction between practical control and legitimate governance authority is a normative/mechanistic synthesis. |
| FC-000059 Infrastructural Access Leverage | STRONG | DMA gatekeeper obligations; cloud-switching/interoperability policy; competition-law leveraging concepts | Strong external support for using control of access/interoperability/lock-in as leverage over dependent actors, while VIGIL keeps valid security/operational restrictions excluded. |
| FC-000060 Canonical Representation Capture | VIGIL-EMERGENT | platform/gatekeeper and information-intermediation literature | Platform representation power is extensively studied, but no sufficiently direct general source was identified for capture of a shared canonical representation as a discrete governance mechanism. |
| FC-000061 Sovereign Authority Infrastructure Projection | VIGIL-EMERGENT | UNESCO national-sovereignty principle; cross-border cloud/data-governance literature | Sovereignty/extraterritorial infrastructure risk is well established; VIGIL's mechanism of projecting authority through infrastructure beyond its independent jurisdictional basis is a narrower synthesis. |

### FF-0011 — Value Appropriation Integrity Failures

| Class | Assessment | Candidate external evidence | Review note |
|---|---|---|---|
| FC-000067 Privileged-Access Appropriation | PARTIAL | UNESCO benefit-sharing/equity principles; U.S. Copyright Office AI-training study; EU DSM Directive text-and-data-mining framework; competition/research ethics literature | Strong evidence that AI training/reuse, reservation of rights, concentration and benefit distribution are live governance issues. VIGIL's ethical requirement for proportionate participation/benefit sharing is broader than settled IP law and must not be represented as an established legal entitlement. |

## Cross-family findings

### 1. The taxonomy is externally anchored, but not derivative of existing frameworks

Most classes have a strong or partial analogue in established security, provenance, assurance, human-factors, privacy, AI-governance or distributed-systems literature. Existing frameworks usually describe desired properties or broad risks. VIGIL's distinctive contribution is often the separation of *mechanisms* that those frameworks place under one control family.

Examples include separating:

- event non-capture from audit non-reconstructability, hidden execution topology and monitor bypass;
- missing verification from false-success representation, stale verification and post-verification mutation;
- authentication-state continuity from ambiguous/collapsed access state;
- dependency as structural power from the separate use of infrastructure access as leverage;
- sycophantic/evaluative assent from manipulation of a consequential choice;
- purpose transposition from downstream value appropriation.

### 2. International standards are most useful as boundary and assurance evidence

ISO/IEC 42001, 23894, 42005, the 5259 data-quality series and related JTC 1/SC 42 work provide a strong governance and lifecycle backbone. They should not be sprayed across classes merely because they mention risk or controls. A class-level standards reference should identify the specific public concept supporting that class and state whether the evidence is clause-level, authorised derivative mapping, or official metadata/abstract only.

ISO/IEC FDIS 42105 is particularly relevant to FF-0007, FF-0008 and FF-0009 because its public draft description expressly concerns human control and monitoring throughout the AI lifecycle and preserving human autonomy in decision-making. Because it remains an FDIS rather than a published International Standard as of this review, it should be marked contextual or draft-standard evidence until publication.

### 3. Several VIGIL-emergent classes appear genuinely useful rather than unsupported

The six classes presently marked VIGIL-EMERGENT are not unsupported phenomena. They are narrower mechanism boundaries for which this pass found only adjacent external vocabularies:

- FC-000014 False Continuity Attribution;
- FC-000045 Authorised Investigative Evidence Access Pathway Failure;
- FC-000048 Verification-Dependency Access Failure;
- FC-000056 Synthetic Conversational Turn-State Coordination Failure;
- FC-000060 Canonical Representation Capture;
- FC-000061 Sovereign Authority Infrastructure Projection.

These should be priority targets for deeper literature review. If direct analogues remain absent while multiple incidents map coherently to them, that absence itself is potentially a research finding about the taxonomy.

### 4. Two classes require especially careful normative wording

**FC-000049 Dependency-Cultivation Optimisation:** current evidence strongly supports emotional dependence and problematic-use outcomes, and there is broad literature on engagement optimisation. It does not by itself establish that a particular system was deliberately or functionally optimised to cultivate dependency. Classification must retain the requirement for evidence of the optimisation mechanism.

**FC-000067 Privileged-Access Appropriation:** current law and standards do not establish a universal entitlement to proportionate benefit sharing from all downstream AI-derived value. The class can remain an ethical/governance mechanism, but external references must not be presented as proving an existing general legal prohibition or property right.

### 5. FC-000068 has unusually strong external triangulation

The class is supported by a mature technical model-extraction literature and by the September 2026 NSA/FBI/CISA advisory's explicit distinction between legitimate distillation and aggressive industrial-scale campaigns that systematically extract restricted frontier-model capabilities for downstream training. This supports the class's scale, systematicity and end-purpose criteria while preserving the critical boundary that distillation or learning from model outputs is not inherently a failure.

## Recommended canonical-reference tranche

Do **not** bulk-write every candidate above into class JSON in one pass. Populate canonical `external_references` in controlled tranches, beginning with classes where the source-to-mechanism fit is direct and reviewable:

1. FC-000055 — OAIC APP 6 and AI/model-training purpose-limitation guidance.
2. FC-000031 — NIST SP 800-63B-4 authenticated-session guidance.
3. FC-000019 — CWE-367 TOCTOU as a clearly-labelled structural analogue, supplemented by lifecycle/change-control assurance if desired.
4. FC-000063 — NIST AI 100-2e2025 adversarial-ML poisoning taxonomy.
5. FC-000022 / 024 / 025 — OECD traceability, EU AI Act logging where applicable, and W3C PROV.
6. FC-000023 — METR monitorability evidence.
7. FC-000051 / 066 — primary sycophancy research.
8. FC-000052 — EU AI Act Article 5 and FTC dark-patterns material.
9. FC-000065 — automation-bias systematic reviews plus NIST human-AI oversight guidance.
10. FC-000068 — retain current NSA/FBI/CISA reference and add mature model-extraction research.

After this high-confidence tranche, review PARTIAL classes family-by-family and add only sources that support the precise boundary. Leave VIGIL-EMERGENT classes without class-level references until deeper review finds an adequate source; incident evidence can continue to support their empirical usefulness without manufacturing an external lineage.

## Public sources reviewed / candidate bibliography

- ISO/IEC 42001:2023 — https://www.iso.org/standard/42001
- ISO/IEC 23894:2023 — https://www.iso.org/standard/77304.html
- ISO/IEC 42005:2025 — https://www.iso.org/standard/42005
- ISO/IEC 5259-5:2025 — https://www.iso.org/standard/84150.html
- ISO/IEC FDIS 42105 — https://www.iso.org/standard/86902.html
- NIST AI Risk Management Framework / AIRC — https://airc.nist.gov/airmf-resources/airmf/
- NIST AI RMF Core — https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AI RMF human-AI interaction appendix — https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/
- NIST SP 800-63B-4 — https://pages.nist.gov/800-63-4/sp800-63b.html
- OECD AI Principles, robustness/security/safety — https://oecd.ai/en/dashboards/ai-principles/P8
- UNESCO Recommendation on the Ethics of Artificial Intelligence — https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
- OAIC guidance on privacy and developing/training generative AI models — https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-developing-and-training-generative-ai-models
- IETF RFC 9700 — https://www.rfc-editor.org/rfc/rfc9700
- W3C PROV-DM — https://www.w3.org/TR/prov-dm/
- OWASP Authorization Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP LLM Top 10 — https://genai.owasp.org/llm-top-10/
- Tramèr et al., *Stealing Machine Learning Models via Prediction APIs* — https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer
- Zhao et al., *A Survey on Model Extraction Attacks and Defenses for Large Language Models* — https://arxiv.org/abs/2506.22521
- NSA/FBI/CISA industrial-scale distillation advisory announcement — https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4592113/nsa-and-others-warn-china-based-ai-companies-are-distilling-us-frontier-ai-mode/
- Goddard et al., *Automation bias: a systematic review of frequency, effect mediators, and mitigators* — https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/

## Closure state

**Artefact classification:** AUDIT.  
**Canonical taxonomy modified by this review:** No.  
**Generated publication modified by this review:** No.  
**Incident records modified by this review:** No.  
**Next action:** reviewer-approved class-level reference population, beginning with the high-confidence tranche above, followed by targeted deeper research on VIGIL-EMERGENT classes.
