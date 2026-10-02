# Taxonomy / external governance alignment audit — 1–2 October 2026

Reviewed 76 current classes and 799 canonical requirements. 303 requirements remain explicitly unresolved. The active registry contains 718 reviewed atomic relationships.

This is the available canonical relationship pass. It does not close pending source fidelity, source permissions or unresolved historical citations. No Incident applicability or finding was adjudicated.

Authorship: AI-authored analytical review; not human reviewed or verified.

## Counts

| Measure | Count |
|---|---:|
| registered source versions | 85 |
| canonical requirements | 1102 |
| requirements substantively reviewed | 799 |
| requirements unresolved | 303 |
| historical references dispositioned | 139 |
| historical references substantively reviewed | 89 |
| historical references unresolved | 50 |
| historical citations pending canonical decomposition | 17 |
| relationship registry count | 718 |
| direct relationships | 0 |
| strong-supporting relationships | 390 |
| contextual relationships | 328 |

## Review artefacts

- [Class definitions, invariants, boundaries and component-level relationships](fidelity-class-rollup.json)
- [Every represented requirement: reviewed reverse disposition or explicit hold](reverse-dispositions.json)
- [All original historical references and their dispositions](historical-reference-dispositions.json)
- [Primary review of noncanonical historical citations and specific access holds](historical-primary-review.json)
- [Source/version roll-ups](source-rollup.json)
- [Validation and unchanged baseline failures](validation-results.json)
- [Pending requirements](pending-requirements.json)
- [Source-copy access and permission review](primary-access-review.json)

Per-source decision files contain proposition, supported component, scope, force, strength reason, limitations and primary-review basis. The registry is `vigil/external_governance/requirements/taxonomy-relationships.json`. Roll-ups can be regenerated with `python vigil/docs/reviews/2026-10-01-taxonomy-standards-alignment/generate_rollups.py`. That script assembles explicit decisions; it performs no semantic inference.

## Fidelity Class support

| Class | Name | Direct | Constituent | Contextual | Pending historical citations |
|---|---|---:|---:|---:|---:|
| VIGIL-FC-000001 | Source-Authority Separation | 0 | 2 | 4 | 1 |
| VIGIL-FC-000002 | Capability-Authority Separation | 0 | 14 | 3 | 1 |
| VIGIL-FC-000003 | Target and Scope Authority Binding | 0 | 2 | 1 | 0 |
| VIGIL-FC-000005 | Transformation Authority Preservation | 0 | 0 | 1 | 0 |
| VIGIL-FC-000006 | Control-Plane Authority Separation | 0 | 2 | 0 | 0 |
| VIGIL-FC-000009 | Downstream Delegated Authority Validation | 0 | 1 | 0 | 1 |
| VIGIL-FC-000010 | Authorship and Source Attribution Integrity | 0 | 1 | 3 | 0 |
| VIGIL-FC-000011 | Synthesis Traceability | 0 | 6 | 2 | 0 |
| VIGIL-FC-000012 | Cross-Context Lineage Preservation | 0 | 0 | 5 | 0 |
| VIGIL-FC-000013 | Transformation Lineage Continuity | 0 | 19 | 12 | 0 |
| VIGIL-FC-000014 | Continuity Attribution Integrity | 0 | 0 | 0 | 0 |
| VIGIL-FC-000015 | Target-Object Binding Integrity | 0 | 9 | 2 | 0 |
| VIGIL-FC-000016 | Required Verification Completion | 0 | 23 | 4 | 1 |
| VIGIL-FC-000017 | Success Representation Integrity | 0 | 0 | 1 | 0 |
| VIGIL-FC-000018 | Completion-Condition Alignment | 0 | 0 | 2 | 0 |
| VIGIL-FC-000019 | Post-Verification State Integrity | 0 | 8 | 4 | 0 |
| VIGIL-FC-000020 | Verification Applicability Continuity | 0 | 19 | 17 | 0 |
| VIGIL-FC-000022 | Material Event Capture | 0 | 20 | 4 | 0 |
| VIGIL-FC-000023 | Monitoring Coverage Integrity | 0 | 4 | 14 | 0 |
| VIGIL-FC-000024 | Audit-Trail Reconstructability | 0 | 17 | 5 | 0 |
| VIGIL-FC-000025 | Actor–Action Attribution | 0 | 5 | 6 | 0 |
| VIGIL-FC-000026 | Material Execution Path Visibility | 0 | 0 | 1 | 0 |
| VIGIL-FC-000027 | Audit-Evidence Integrity | 0 | 14 | 2 | 0 |
| VIGIL-FC-000029 | Execution-State Disclosure | 0 | 1 | 3 | 0 |
| VIGIL-FC-000030 | Material Signal Integration | 0 | 1 | 9 | 0 |
| VIGIL-FC-000031 | Authentication-State Continuity | 0 | 0 | 0 | 0 |
| VIGIL-FC-000032 | Access-State Differentiation | 0 | 2 | 0 | 0 |
| VIGIL-FC-000034 | Continuity Anchoring | 0 | 0 | 0 | 0 |
| VIGIL-FC-000035 | Material Work-State Persistence | 0 | 0 | 4 | 0 |
| VIGIL-FC-000036 | Restoration-State Integrity | 0 | 0 | 1 | 1 |
| VIGIL-FC-000037 | Control Availability Determination | 0 | 4 | 9 | 1 |
| VIGIL-FC-000038 | Required Control Activation | 0 | 7 | 0 | 2 |
| VIGIL-FC-000040 | Control-State Preservation | 0 | 2 | 1 | 0 |
| VIGIL-FC-000041 | Required Governance Routing | 0 | 1 | 3 | 1 |
| VIGIL-FC-000042 | Governance Signal Delivery | 0 | 7 | 13 | 3 |
| VIGIL-FC-000043 | Control Activation Validity | 0 | 4 | 0 | 1 |
| VIGIL-FC-000044 | Primary Evidence Accessibility | 0 | 2 | 7 | 0 |
| VIGIL-FC-000045 | Authorised Investigative Evidence Access | 0 | 2 | 1 | 0 |
| VIGIL-FC-000046 | Inferential Evidence–Authority Separation | 0 | 5 | 4 | 0 |
| VIGIL-FC-000047 | Mechanism Attribution Support | 0 | 2 | 13 | 0 |
| VIGIL-FC-000048 | Verification-Dependency Access Continuity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000049 | Engagement Autonomy | 0 | 0 | 2 | 1 |
| VIGIL-FC-000050 | Protected-Signal Purpose Integrity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000051 | Relationally Independent Epistemic Framing | 0 | 0 | 2 | 1 |
| VIGIL-FC-000052 | Choice Agency Preservation | 0 | 0 | 3 | 2 |
| VIGIL-FC-000053 | Identity-Representation Authority Separation | 0 | 0 | 1 | 1 |
| VIGIL-FC-000054 | Multi-party Participant Authority Separation | 0 | 0 | 3 | 1 |
| VIGIL-FC-000055 | Secondary-Purpose Authority Revalidation | 0 | 6 | 18 | 1 |
| VIGIL-FC-000056 | Synthetic Conversational Turn-State Coordination | 0 | 0 | 0 | 0 |
| VIGIL-FC-000057 | Cross-Principal State Authority Separation | 0 | 0 | 0 | 1 |
| VIGIL-FC-000058 | Infrastructure–Governance Authority Separation | 0 | 0 | 0 | 1 |
| VIGIL-FC-000059 | Infrastructural Access Choice Integrity | 0 | 0 | 1 | 1 |
| VIGIL-FC-000060 | Canonical Representation Integrity | 0 | 0 | 0 | 0 |
| VIGIL-FC-000061 | Jurisdiction-Bounded Infrastructure Authority | 0 | 0 | 0 | 1 |
| VIGIL-FC-000062 | Epistemic Reliance Calibration | 0 | 102 | 42 | 0 |
| VIGIL-FC-000063 | Adversarial Evidence Trust Calibration | 0 | 9 | 16 | 1 |
| VIGIL-FC-000064 | Objective–Pathway Authority Separation | 0 | 0 | 4 | 0 |
| VIGIL-FC-000065 | Consequential Decision Grounding | 0 | 4 | 2 | 1 |
| VIGIL-FC-000066 | Evaluative Independence | 0 | 1 | 0 | 1 |
| VIGIL-FC-000067 | Privileged-Access Contribution Governance | 0 | 0 | 3 | 2 |
| VIGIL-FC-000068 | Industrial-Scale Capability Extraction Authority | 0 | 0 | 3 | 0 |
| VIGIL-FC-000069 | Objective–Reward Alignment | 0 | 0 | 3 | 0 |
| VIGIL-FC-000070 | Safe-Exit Transition | 0 | 0 | 5 | 1 |
| VIGIL-FC-000071 | Welfare–Economic Decision Separation | 0 | 0 | 0 | 6 |
| VIGIL-FC-000072 | Oversight Independence | 0 | 5 | 4 | 0 |
| VIGIL-FC-000073 | Protected Governance Dissent | 0 | 1 | 0 | 0 |
| VIGIL-FC-000074 | Identity-State Instruction Boundary | 0 | 0 | 1 | 2 |
| VIGIL-FC-000075 | Pragmatic Constraint Rendering Integrity | 0 | 1 | 4 | 0 |
| VIGIL-FC-000076 | Governance Neutrality | 0 | 1 | 3 | 0 |
| VIGIL-FC-000077 | Distributed Role Constraint Integrity | 0 | 5 | 3 | 2 |
| VIGIL-FC-000078 | Continuity-State Validity | 0 | 1 | 0 | 1 |
| VIGIL-FC-000079 | Economic Solicitation Authenticity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000080 | Human Contribution Recognition | 0 | 1 | 0 | 0 |
| VIGIL-FC-000081 | Biospheric Constraint Priority | 0 | 0 | 10 | 1 |
| VIGIL-FC-000082 | Social Engineering Integrity | 0 | 6 | 8 | 3 |
| VIGIL-FC-000083 | Control Effectiveness Integrity | 0 | 41 | 26 | 2 |

## Historical citation review

89 of 139 historical references have a recorded substantive review basis; 50 remain unresolved. 17 reviewed constituent citations have no canonical EXTREQ endpoint. They are excluded from registry and occurrence candidate derivation. Research-abstract reviews are bounded to the explicitly available proposition, not full-paper assurance.

| Class | Historical reference | Disposition |
|---|---|---|
| VIGIL-FC-000001 | LLM01:2025 Prompt Injection | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000001 | IEEE 7014.1-2026, clause 6.25.3(a-c) | pending-source-relationship-review |
| VIGIL-FC-000002 | LLM06:2025 Excessive Agency | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000002 | IEEE 7009-2024, Annex A.3 / 7009-ASR-011 | pending-source-relationship-review |
| VIGIL-FC-000003 | RFC 8707: Resource Indicators for OAuth 2.0 | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000005 | NIST AI 600-1, control MP-2.1-002 | retain-contextual |
| VIGIL-FC-000005 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000006 | CWE-15: External Control of System or Configuration Setting | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000006 | Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000009 | Model AI Governance Framework for Agentic AI, section 2.1.2 | pending-source-relationship-review |
| VIGIL-FC-000009 | RFC 8693: OAuth 2.0 Token Exchange | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000010 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000011 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000011 | NIST AI 600-1, control MP-2.1-002 | retain-contextual |
| VIGIL-FC-000012 | Privacy as Contextual Integrity | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000013 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000013 | NIST AI 600-1, control MP-2.1-002 | retain-contextual |
| VIGIL-FC-000014 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000015 | RFC 8707: Resource Indicators for OAuth 2.0 | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000016 | IEEE 7009-2024, clause 9.5 | pending-source-relationship-review |
| VIGIL-FC-000017 | IEEE 7001-2021, Table 5 level 1 | retain-contextual |
| VIGIL-FC-000018 | Specification gaming: the flip side of AI ingenuity | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000019 | CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000019 | IEEE 7000-2021, clause 10.3(e)(8) | retain-contextual |
| VIGIL-FC-000020 | IEEE 7000-2021, clause 10.3(e)(8) | retain-strong-supporting |
| VIGIL-FC-000022 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 12(1) | retain-strong-supporting |
| VIGIL-FC-000023 | Early work on monitorability evaluations | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000023 | NIST AI 600-1, control MS-2.6-007 | retain-contextual |
| VIGIL-FC-000024 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 12(2) | retain-strong-supporting |
| VIGIL-FC-000024 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000024 | IEEE 7001-2021, Table 4 level 4 | retain-strong-supporting |
| VIGIL-FC-000025 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000025 | SDOS Runtime Governance Framework v1.10, control SDOS-AU-01 | retain-strong-supporting |
| VIGIL-FC-000026 | IEEE 7001-2021, section 5.2.2 principle | retain-contextual |
| VIGIL-FC-000027 | SDOS Runtime Governance Framework v1.10, control SDOS-AU-02 | retain-strong-supporting |
| VIGIL-FC-000027 | IEEE 7001-2021, section 5.2.2 principle | retain-contextual |
| VIGIL-FC-000029 | IEEE 7001-2021, section 5.1.1 general | retain-contextual |
| VIGIL-FC-000030 | Context propagation | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000030 | NIST AI RMF 1.0, MEASURE 2.4 | retain-contextual |
| VIGIL-FC-000030 | Trace Context | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000031 | Digital Identity Guidelines: Authentication and Authenticator Management (NIST SP 800-63B-4) | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000031 | RFC 7009: OAuth 2.0 Token Revocation | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000032 | RFC 9110: HTTP Semantics | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000034 | Microsoft Agent Framework Workflows - Checkpoints | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000034 | A survey of rollback-recovery protocols in message-passing systems | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000035 | Microsoft Agent Framework Workflows - Checkpoints | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000035 | A survey of rollback-recovery protocols in message-passing systems | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000036 | IEEE 7014-2024, clause 4.3.6.2(c-d) | pending-source-relationship-review |
| VIGIL-FC-000037 | IEEE 7009-2024, clause 6.1(h) | pending-source-relationship-review |
| VIGIL-FC-000037 | NIST AI RMF 1.0, MEASURE 1.2 | retain-contextual |
| VIGIL-FC-000038 | IEEE 7014.1-2026, clause 6.6.3(a) | pending-source-relationship-review |
| VIGIL-FC-000038 | IEEE 7009-2024, Annex A.3 / 7009-ASR-011 | pending-source-relationship-review |
| VIGIL-FC-000040 | NIST AI RMF 1.0, MANAGE 4.1 | retain-contextual |
| VIGIL-FC-000040 | IEEE 7000-2021, clause 10.3(e)(8) | no-mapping-remove-from-active-relationship |
| VIGIL-FC-000041 | SDOS Runtime Governance Framework v1.10, control SDOS-EN-01 | retain-strong-supporting |
| VIGIL-FC-000041 | Model AI Governance Framework for Agentic AI, section 2.2.2 | pending-source-relationship-review |
| VIGIL-FC-000041 | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 | no-mapping-remove-from-active-relationship |
| VIGIL-FC-000042 | OPS10-BP04 Define escalation paths - AWS Well-Architected Framework | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000042 | Model AI Governance Framework for Agentic AI, section 2.2.2 | pending-source-relationship-review |
| VIGIL-FC-000042 | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 | pending-source-relationship-review |
| VIGIL-FC-000042 | IEEE Standard for Fail-Safe Design of Autonomous and Semi-Autonomous Systems | pending-source-relationship-review |
| VIGIL-FC-000043 | Spurious activation analysis of safety-instrumented systems | pending-primary-source-access |
| VIGIL-FC-000044 | IEEE 7001-2021, Table 4 level 5 | retain-contextual |
| VIGIL-FC-000045 | IEEE 7001-2021, Table 4 level 5 | retain-contextual |
| VIGIL-FC-000046 | NIST AI RMF 1.0, MEASURE 2.5 | retain-contextual |
| VIGIL-FC-000046 | Automation bias: a systematic review of frequency, effect mediators, and mitigators | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000047 | Four Principles of Explainable Artificial Intelligence | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000047 | IEEE 7001-2021, section 5.2.2 principle | retain-contextual |
| VIGIL-FC-000048 | IEEE 7014-2024, clause 4.3.2.2 (post-p) | pending-source-relationship-review |
| VIGIL-FC-000049 | IEEE 7014.1-2026, clause 6.26.3(a-f) | pending-source-relationship-review |
| VIGIL-FC-000050 | IEEE 7014.1-2026, clause 6.22.3(e-f) | pending-source-relationship-review |
| VIGIL-FC-000051 | Towards Understanding Sycophancy in Language Models | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000051 | IEEE 7014.1-2026, clause 6.27.3(a-d) | pending-source-relationship-review |
| VIGIL-FC-000052 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(a) | pending-source-relationship-review |
| VIGIL-FC-000052 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(b) | pending-source-relationship-review |
| VIGIL-FC-000052 | FTC Report Shows Rise in Sophisticated Dark Patterns Designed to Trick and Trap Consumers | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000053 | IEEE 7014-2024, clause 4.3.5.2(d) | pending-source-relationship-review |
| VIGIL-FC-000054 | IEEE 7014-2024, clause 4.3.2.2(i-k) | pending-source-relationship-review |
| VIGIL-FC-000055 | Guidance on privacy and developing and training generative AI models | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000055 | IEEE 7014-2024, clause 4.3.3.2(f-g) | pending-source-relationship-review |
| VIGIL-FC-000056 | Conversational AI for multi-agent communication in Natural Language | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000057 | API1:2023 Broken Object Level Authorization | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000057 | The Confused Deputy (or why capabilities might have been invented) | pending-primary-source-access |
| VIGIL-FC-000058 | Regulation (EU) 2023/2854 — Data Act | pending-primary-source-access |
| VIGIL-FC-000059 | Regulation (EU) 2023/2854 — Data Act | pending-primary-source-access |
| VIGIL-FC-000060 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000061 | Regulation (EU) 2023/2854 — Data Act | pending-primary-source-access |
| VIGIL-FC-000062 | Four Principles of Explainable Artificial Intelligence | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000062 | NIST AI RMF 1.0, MEASURE 2.5 | retain-strong-supporting |
| VIGIL-FC-000062 | Automation bias: a systematic review of frequency, effect mediators, and mitigators | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000063 | Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations | derived-contextual-document-rollup |
| VIGIL-FC-000063 | Threats to Training: A Survey of Poisoning Attacks and Defenses on Machine Learning Systems | pending-primary-source-access |
| VIGIL-FC-000064 | Optimal Policies Tend To Seek Power | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000065 | Automation bias: a systematic review of frequency, effect mediators, and mitigators | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000065 | Artificial Intelligence Risk Management Framework 1.0, Appendix C: AI Risk Management and Human-AI Interaction | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000065 | IEEE 7014.1-2026, clause 6.25.3(a-c) | pending-source-relationship-review |
| VIGIL-FC-000066 | Towards Understanding Sycophancy in Language Models | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000066 | IEEE 7014.1-2026, clause 6.27.3(a-d) | pending-source-relationship-review |
| VIGIL-FC-000067 | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 | pending-source-relationship-review |
| VIGIL-FC-000067 | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 | pending-source-relationship-review |
| VIGIL-FC-000068 | China-Based Artificial Intelligence Companies Conducting Industrial-Scale Distillation Campaigns Against U.S. AI Companies | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000068 | Stealing Machine Learning Models via Prediction APIs | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000068 | NIST AI 600-1, control MS-2.10-001 | retain-contextual |
| VIGIL-FC-000069 | Concrete Problems in AI Safety | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000069 | AI Safety Gridworlds | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000070 | IEEE 7009-2024, clause 8.3 DIOP4 | pending-source-relationship-review |
| VIGIL-FC-000070 | NIST AI RMF 1.0, GOVERN 1.7 | retain-contextual |
| VIGIL-FC-000071 | IEEE 7014.1-2026, clause 6.14.3(a-d) | pending-source-relationship-review |
| VIGIL-FC-000071 | IEEE 7014.1-2026, clause 6.7.3(f-k) | pending-source-relationship-review |
| VIGIL-FC-000071 | IEEE 7014.1-2026, clause 6.22.3(e-f) | pending-source-relationship-review |
| VIGIL-FC-000071 | IEEE 7014.1-2026, clause 6.9.3(e-g) | pending-source-relationship-review |
| VIGIL-FC-000071 | IEEE 7014.1-2026, clause 6.12.3(a-c) | pending-source-relationship-review |
| VIGIL-FC-000071 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(a) | pending-source-relationship-review |
| VIGIL-FC-000072 | Global Internal Audit Standards | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000073 | Directive (EU) 2019/1937 on the protection of persons who report breaches of Union law | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000074 | Model AI Governance Framework for Agentic AI, section 2.1.2 | pending-source-relationship-review |
| VIGIL-FC-000074 | Model AI Governance Framework for Agentic AI, section 2.2 | pending-source-relationship-review |
| VIGIL-FC-000074 | IEEE Standard Model Process for Addressing Ethical Concerns during System Design | retain-contextual |
| VIGIL-FC-000075 | IEEE Standard Model Process for Addressing Ethical Concerns during System Design | retain-strong-supporting |
| VIGIL-FC-000075 | IEEE Standard Model Process for Addressing Ethical Concerns during System Design | retain-contextual |
| VIGIL-FC-000076 | Global Internal Audit Standards | reviewed-constituent-citation-pending-canonical-decomposition |
| VIGIL-FC-000076 | IEEE Standard Model Process for Addressing Ethical Concerns during System Design | retain-contextual |
| VIGIL-FC-000077 | Model AI Governance Framework for Agentic AI, section 2.3.1 | pending-source-relationship-review |
| VIGIL-FC-000077 | Model AI Governance Framework for Agentic AI, section 2.2 | pending-source-relationship-review |
| VIGIL-FC-000077 | IEEE Standard Model Process for Addressing Ethical Concerns during System Design | retain-strong-supporting |
| VIGIL-FC-000078 | Memory poisoning attacks on retrieval-augmented Large Language Model agents via deceptive semantic reasoning | pending-primary-source-access |
| VIGIL-FC-000079 | Horizon Scan: AI and Deepfakes | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000079 | 26-195MR ASIC warns scammers are using AI to spin vast webs of deception | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000079 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(a) | pending-source-relationship-review |
| VIGIL-FC-000080 | PROV-DM: The PROV Data Model | retain-contextual-nonrequirement-citation |
| VIGIL-FC-000081 | IEEE 7000-2021, clause 7.3(e) | retain-contextual |
| VIGIL-FC-000081 | IEEE 7014.1-2026, clause 6.8.3(e-i) | pending-source-relationship-review |
| VIGIL-FC-000082 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(a) | pending-source-relationship-review |
| VIGIL-FC-000082 | IEEE 7014.1-2026, clause 6.7.3(l-p) | pending-source-relationship-review |
| VIGIL-FC-000082 | IEEE 7014.1-2026, clause 6.22.3(a-b) | pending-source-relationship-review |
| VIGIL-FC-000082 | Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency | derived-contextual-document-rollup |
| VIGIL-FC-000083 | NIST AI RMF 1.0, MEASURE 1.2 | retain-strong-supporting |
| VIGIL-FC-000083 | IEEE 7009-2024, clause 6.1(h) | pending-source-relationship-review |
| VIGIL-FC-000083 | IEEE 7014.1-2026, clause 6.6.3(a) | pending-source-relationship-review |

Classes without constituent support are not ranked as deficient. They may rely on VIGIL normative reasoning, contextual evidence, or pending sources. Counts alone cannot distinguish those explanations. No reviewed source expresses an entire class invariant here; strength was not increased to satisfy a coverage target.

## Source/version support

| Source | Version | Reviewed requirements | Direct | Constituent | Contextual | Pending requirements | Review state |
|---|---|---:|---:|---:|---:|---:|---|
| AAM-SDOS-RUNTIME-GOVERNANCE | 1.10 | 24 | 0 | 40 | 1 | 0 | represented-requirements-reviewed |
| C2PA-SPEC | 2.4 | 25 | 0 | 22 | 3 | 3 | partially-reviewed |
| CANADA-DIRECTIVE-AUTOMATED-DECISION-MAKING | current-2026-09-28 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| COE-AI-CONVENTION-CETS-225 | 2024-09-05 | 54 | 0 | 13 | 20 | 0 | represented-requirements-reviewed |
| CYCLONEDX-SPEC | 1.7 | 5 | 0 | 1 | 4 | 0 | represented-requirements-reviewed |
| EU-AI-ACT-2024-1689 | 2024-07-12 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-AI-ACT-2024-1689 | 2026-07-27 | 102 | 0 | 87 | 16 | 73 | partially-reviewed |
| EU-CRA-2024-2847 | 2024-11-20 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DATA-ACT-2023-2854 | 2023-12-22 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DGA-2022-868 | 2022-06-03 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DSA-2022-2065 | 2022-10-27 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-GDPR-2016-679 | 2016-05-04 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-NIS2-2022-2555 | 2022-12-27 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| FDA-MDR-ADVERSE-EVENT-CODES | 2026-04-13 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ICAO-ADREP-TAXONOMY | current-2026-08-18 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEC-60812 | 2018 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-1044 | 2009 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-2089 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-2863 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7000 | 2021 | 59 | 0 | 9 | 23 | 0 | represented-requirements-reviewed |
| IEEE-7001 | 2021 | 33 | 0 | 20 | 20 | 0 | represented-requirements-reviewed |
| IEEE-7002 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7003 | 2024 | 0 | 0 | 0 | 0 | 0 | permission-pending |
| IEEE-7005 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7007 | 2021 | 10 | 0 | 0 | 11 | 0 | represented-requirements-reviewed |
| IEEE-7009 | 2024 | 0 | 0 | 0 | 0 | 63 | permission-pending |
| IEEE-7010 | 2020 | 18 | 0 | 1 | 3 | 0 | represented-requirements-reviewed |
| IEEE-7012 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7014 | 2024 | 0 | 0 | 0 | 0 | 59 | permission-pending |
| IEEE-7014.1 | 2026 | 0 | 0 | 0 | 0 | 66 | permission-pending |
| IMDA-AGENTIC-AI-MGF | 2026-05 | 0 | 0 | 0 | 0 | 39 | source-access-pending |
| IMDRF-AER-N43 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-12791 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-12792 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-17903 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-20226 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-21221 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-22989 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-23053 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-23894 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24027 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24028 | 2020 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24029-1 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24029-2 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24030 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24368 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24372 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24668 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-25058 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-25059 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-38507 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42001 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42005 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42006 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42106 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42112 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42119-2 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-4213 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-1 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-2 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-3 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-4 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-5 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-6 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5338 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5339 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5392 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5469 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-6254 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-8183 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-8200 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-IEEE-24765 | 2017 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-100-1 | 1.0 | 74 | 0 | 15 | 54 | 0 | represented-requirements-reviewed |
| NIST-AI-100-2 | E2025 | 22 | 0 | 4 | 20 | 0 | represented-requirements-reviewed |
| NIST-AI-100-3 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-100-4 | 2024 | 19 | 0 | 10 | 14 | 0 | represented-requirements-reviewed |
| NIST-AI-100-5 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-600-1 | 2024 | 224 | 0 | 116 | 92 | 0 | represented-requirements-reviewed |
| NIST-CSF-2-0 | 2.0 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-SP-1270 | 2022 | 14 | 0 | 7 | 3 | 0 | represented-requirements-reviewed |
| NIST-SP-800-218 | 1.1 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-SP-800-218A | 2024 | 75 | 0 | 41 | 33 | 0 | represented-requirements-reviewed |
| OECD-AI-INCIDENT-REPORTING-2025 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| OECD-AI-PRINCIPLES | 2024-05-03 | 37 | 0 | 3 | 7 | 0 | represented-requirements-reviewed |
| SPDX-SPEC | 3.0.1 | 4 | 0 | 1 | 4 | 0 | represented-requirements-reviewed |

Contextual counts are excluded from material support and resolver candidate derivation. A catalogue entry marked reviewed is not evidence that its normative requirements have been extracted/reviewed.

## Outstanding work

- IEEE 7003, 7009, 7014 and 7014.1 require evidence of separate written AI-use permission before substantive relationship admission. Other metadata-only/licensed editions retain their registered access limits.
- IMDA framework-body access remains unresolved; Canada Directive access remains blocked, with no represented canonical requirements.
- EU review is bounded to the 102 source-assured successors from Articles 4a and 9–15. The other 73 requirements remain pending consolidated-source fidelity/atomicity.
- Three C2PA AI-disclosure requirements remain unresolved because normative prose, CDDL and examples conflict.
- Primary-reviewed constituent citations without canonical endpoints remain pending decomposition and outside the registry. Research, definitions and implementation examples remain contextual nonrequirement citations. Failed primary retrieval is recorded separately with attempted locators; original annotations are preserved.
- No genuinely new class or material boundary change is proposed. No-mapping institutional, policy, social-outcome and operational provisions are recorded without forcing them into a class.

New relationships should trigger only the dependent occurrence external-requirement backfill. Existing clause/taxonomy adjudication should be reopened only for a substantive contradiction.
