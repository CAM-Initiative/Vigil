# Bounded security comparison

Status: REVIEW. AI-authored analysis, no substantive human verification. Canonical recognition contracts are pinned verbatim in CLASS-CONTRACT-SNAPSHOT.json at main taxonomy v0.9.1. Native identifiers are retained in the two audit inventories. These tables are descriptive discovery aids; none is a canonical FC–EXTREQ edge, occurrence assessment or evidence of successful exploitation.

## Source authority

| Kind | Role in this review | Claim boundary |
| --- | --- | --- |
| Legal/regulatory instruments | Existing ICCPR, CETS 225 and EU AI Act records | Exact actor, jurisdiction, commencement and scope establish applicability; registration alone does not. |
| Governance frameworks | Existing OECD principles and NIST AI RMF 1.0 | Voluntary governance propositions; reuse 74 represented RMF propositions. |
| Technical standards/specifications | Existing catalogue; six service-related ISO editions held | Conformance depends on actual source clauses and adoption. No new standard authority inferred. |
| Security risk references/knowledge bases | Two OWASP 2026 lists; ATLAS v2026.09 | Risk and adversary vocabulary; source-defined mitigation prose is a separate discovery surface. |

All three new sources use existing `taxonomy` source class and `context-or-discovery` role. “Authoritative” in the publisher matrix means authoritative for its own publication identity, not legal force. No new normative-force value is introduced. Source records do not assert a control was adopted or verified.

## Descriptive associations against the recognition contract

| Current class | OWASP / ATLAS discovery anchors | Recognition boundary |
| --- | --- | --- |
| FC-025 Actor–Action Attribution | ASI02, ASI03, ASI07; AML.T0053; AML.M0024 | Distinguish effective initiator/controller, tool execution, human direction and transfers of control. A harmful attributed action can preserve attribution. Tool misuse alone does not establish attribution loss. |
| FC-062 Epistemic Reliance Calibration | LLM07:2026; ASI06, ASI09 | Test assurance against actual purpose and downstream reliance, including drafting. Distinguish evidence quality from mere content lineage. Apply the exclusion for an omitted required verification step where that mechanism is sufficient; misinformation labels do not establish recognition. |
| FC-064 Objective–Pathway Authority Separation | LLM03:2026; ASI01, ASI02, ASI03; AML.T0051.001, AML.T0053 | Establish that objective utility materially drove an authority/admissibility failure in the selected pathway. Technical reachability alone or valid authority merely carried to another scope engages neighbouring contracts instead. Planning and persistence alone are excluded. |
| FC-089 Protected Information Access Integrity | LLM02:2026, LLM08:2026; ASI02, ASI03; AML.T0057, AML.T0086 | Establish an independent authorisation boundary and realised protected-information operation. Public information, purely hypothetical vulnerabilities and unsuccessful attempts cannot establish the adverse recognition. A system prompt is not automatically protected information. |
| FC-090 Authentication Material Custody Integrity | ASI03; AML.T0055, AML.T0082, AML.T0083, AML.T0098 | Establish actual secret authentication material and exposure/acquisition outside custody. Public identifiers, placeholders, authorised delegation and pure action-scope disputes are excluded. Later credential use is not required to establish a custody event. |
| FC-083 Control Effectiveness Integrity | ASI08, ASI10; AML.M0030, AML.M0033 | Identify a validly activated applicable control and required protective effect. Separate non-activation, invalid activation, lost state and non-delivery under the neighbouring contracts named in the exclusions. A successful block at an independent defender is not the attacking agent's own behaviour. |
| FC-084 Service Availability and Degradation Integrity | LLM06:2026; ASI08; AML.T0029, AML.T0101 | Independently establish the service obligation, material shortfall and inadequate required response. Resource consumption or an outage label supplies no universal uptime guarantee. Lawful proportionate restriction and effective feasible recovery may defeat the adverse role. |

## Governance-proposition candidates — not admitted

| Native source proposition | Potential component | Admission disposition |
| --- | --- | --- |
| ATLAS AML.M0024, AI Telemetry Logging | FC-025: identity and intermediate tool/action logging | Concrete control text exists. Logging agent identity does not necessarily identify effective human/orchestrator control or transfers. A later atomic candidate must preserve this partial correspondence and review privacy and retention. |
| ATLAS AML.M0026–M0028, privileged/single-user/tool permissions | Authority and information-boundary components | Explicit least-privilege and delegated-access controls are stronger than technique names. Review exact target class recognition, actor, lifecycle and boundary separately; no blanket FC-064/089/090 edge. |
| ATLAS AML.M0029, Human In-the-Loop for AI Agent Actions | Consequence-calibrated approval | The text distinguishes minor repetitive tasks from consequential actions. Approval is not proof that the policy or approver is legitimate. No unconditional human-approval requirement is extracted. |
| ATLAS AML.M0030 and AML.M0033 | Restrict tool invocation on untrusted data; external component validation | Specific defensive guidance exists. Establish the actual protected purpose and component effect; implementation advice alone cannot establish FC-083 or incident polarity. |
| OWASP Agentic 2026 ASI01 mitigation guidance, PDF pp. 10–11 | Scope/goal-change validation, bounded tools and review | Possible atomic source-defined controls; examples and emerging patterns must not become mandatory duties. Full field-level extraction, metadata, fidelity and supported-pair admission are outside this context-only registration. |

Decision: zero new OWASP/ATLAS EXTREQs or canonical relationships in this tranche. This is a bounded non-admission decision, not a claim that the sources contain no controls. The ten selectively recovered NIST relationships are already reviewed component pairs, not newly inferred security mappings. Four of their requirements were already admitted on the research branch. Reuse their deterministic IDs and evidence.

## Version and provenance qualifications

- OWASP LLM: dedicated publisher resource dated 3 August 2026 and September release announcement support a published 2026 edition. PDF text has publication-date placeholders; no invented final PDF date. Native rankings differ from 2025: excessive agency is LLM03, consumption LLM06 and misinformation LLM07. The generic website navigation remains 2025 and must not overwrite 2026 vocabulary.
- OWASP Agentic: 2026 edition published 9 December 2025, PDF dated December 2025. Its internal references to LLM 2025 remain historical source references.
- MITRE: release v2026.09 published 15 September 2026, non-draft/non-prerelease. Exact YAML SHA-256 matches the publisher asset: 935efa93e28294432d3e2f537eb94991ef8d1f8c58341cd360ea3321ddb66688. It contains 120 techniques, 88 sub-techniques, 40 mitigations and 73 case studies. October v2026.10 exists; September is registered as superseded, retained by explicit requested pin. Live technique names may differ from this snapshot.
- OWASP source text was inspected through web retrieval. Direct local download returned HTML, not PDF; no substituted carrier checksum is recorded. The PDFs state CC BY-SA 4.0; source-derived inventories retain attribution to the OWASP GenAI Security Project and the respective document titles. No endorsement is implied. MITRE asset identifiers remain publisher-native; full source text is not copied into this review.
- Optional Agent Control Standard: official project resource confirms a separate runtime-control workstream. Exact versioned control text was not admitted or exhaustively assessed here. Its title confers no mandatory normative force. Keep it as a separate follow-up, not a fourth source silently registered.
