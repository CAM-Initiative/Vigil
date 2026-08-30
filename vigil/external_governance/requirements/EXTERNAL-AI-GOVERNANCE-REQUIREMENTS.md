# External AI-Governance Requirements

Canonical analytical catalogue derived from registered external governance sources. Inclusion does not establish CAM applicability, adoption, coverage, compliance, conformance or alignment.

- Registered source versions: 81
- Primary AI-governance source versions: 57
- Requirement records: 854

## SDOS Runtime Governance Framework — Control Catalog and Reference Document — 1.10

- Source: `EXT-8FEA9674D97A` / `AAM-SDOS-RUNTIME-GOVERNANCE`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 24
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-16D458CC8C061FFC` | SDOS-IN-01 | Verify governance configuration cryptographically against an authorized baseline before tool registration or agent processing, and support repeat integrity checks during runtime. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1F7D61A28FA1BFB8` | SDOS-GV-04 | Apply a common authoritative governance policy source and decision process across active modules to avoid inconsistent enforcement between modules. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-211A1AA307565C1C` | SDOS-AU-02 | Use audit-record formats and storage supporting append-only semantics and tamper detection so historical governance records are not normally modified or deleted by the application layer. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-336BEEA4C51B9041` | SDOS-EN-02 | Require each executing module to confirm a valid governance approval through a secondary module-level authorization check before carrying out the governed operation. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-422283C001BAFEE1` | SDOS-AU-01 | Generate a structured governance audit record for every tool invocation before returning the tool result, including classification, agent identity, model-binding rationale, time and protected policy-relevant parameters. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-594D5CEC63541F2B` | SDOS-AD-01 | Deny governed operations by default and require explicit agent admission before risk classification, model binding or tool execution, including for agents with pre-existing sessions. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5A0391FE4DC885E9` | SDOS-RM-01 | Classify each tool invocation by risk at the dispatch boundary before execution and use the current policy state to determine permit, conditional-permit or block disposition. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7FAD482D46D3F347` | SDOS-GV-05 | Enforce governance constraints in a structural layer independent of model inference so model outputs cannot use an authorized pathway to override, bypass or modify the controls applied to their operations. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-87AD475F7D0E8821` | SDOS-GV-01 | Use versioned governance configuration to determine which modules and agent capabilities are active, enabling auditable and change-controlled activation without executable-code changes. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8E0FB77F63318E12` | SDOS-EN-04 | Create a tamper-evident audit record for governed outbound execution, linking the permitting governance decision, initiating agent identity, time and protected policy-relevant operation metadata. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9AAA4079957B7D7D` | SDOS-IA-01 | Verify agent identity against a governance-managed trust root before governance evaluation, carry that identity through the governance pipeline, and deny admission where identity cannot be verified. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9BA7C15FFB640788` | SDOS-DE-02 | Create and retain a structured deliberation record that preserves individual assessments, convergence and divergence, and a scored panel summary for later review. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A853649FE81CDD09` | SDOS-GV-03 | Define a configuration-governed default-deny admission policy so agents cannot access governed operations unless admission criteria and scope conditions are satisfied. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-ACDABAB8D69B0222` | SDOS-IN-02 | Halt tool registration and operation when unauthorized governance-baseline change is detected, and require explicit re-authorization of the baseline before recovery. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AE5D085123992944` | SDOS-AU-03 | Maintain governance audit records in two independently maintained repositories and make discrepancies detectable, while leaving reconciliation authority explicitly deployment-defined. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C1E9F45E2A73DE89` | SDOS-IN-03 | Verify the cryptographic signature and authorized-capability state of each module manifest before activation and reject modules that fail manifest integrity checks. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C25CB2D997BC6FE8` | SDOS-EN-01 | Route governed outbound operations through a pre-execution policy enforcement point that permits, modifies or blocks the operation against current policy and records the decision. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C6140F995F09BB5B` | SDOS-EN-03 | Use documented restrictive degradation rules when governance infrastructure is unavailable or indeterminate, and halt completely on governance-baseline integrity failure; block elevated-risk operations until governance is restored and verified. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CF67C1E2AF61F3C8` | SDOS-GV-02 | Assign the model capability tier for each dispatched task through the governance layer, prevent agent/model self-selection or override, and record the selection rationale. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DAAECA7385961402` | SDOS-RM-03 | For policy-defined elevated-risk tasks, enforce a minimum model capability floor even when a lower tier would otherwise be permitted by complexity assessment. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E152AE56D54C13B9` | SDOS-IA-02 | Verify signed module manifests and declared authorized capabilities before tool registration, rejecting missing, invalid or tampered module identities from the governed execution surface. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E413E7DE0D505870` | SDOS-RS-01 | Use accumulated governed feedback and audit data to produce post-hoc risk/safety investment evaluation with documented component metrics and statistical summaries for operator review. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-ED3205AF140C41E7` | SDOS-RM-02 | Assess task characteristics at dispatch and prevent tasks requiring higher analytical capability from being routed below the minimum capability tier identified for the task. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EE5947EABAB44AA2` | SDOS-DE-01 | Govern multi-agent deliberation through policy-defined panel composition, common admission and identity controls, and structured auditable output; treat elevated-risk deliberation outputs as inputs to human review rather than substitutes for human oversight. | `recommended-practice` / `guidance` | `industry-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## CycloneDX 1.7 — Machine Learning Bill of Materials (ML-BOM) — 1.7

- Source: `EXT-13FB945E8A06` / `CYCLONEDX-SPEC`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 5
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-29122B7046B06256` | component.modelCard | A model card should be specified for a component whose type is machine-learning-model. | `recommended-practice` / `guidance` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6C1C17AD6C66F27A` | component.modelCard | A model card must not be specified for component types other than machine-learning-model. | `mandatory-normative` / `positive-duty` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B4146C7FA881D345` | modelCard | A model card can represent model parameters, datasets, inputs, outputs, quantitative analysis, performance metrics, intended users and use cases, limitations, trade-offs, ethical and fairness considerations, and environmental information. | `informative-guidance` / `guidance` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F2C81603A7B306F6` | modelCard.bom-ref | If a model-card bom-ref is supplied, it should not start with the BOM-Link intro urn:cdx: to avoid conflicts with BOM-Links. | `recommended-practice` / `guidance` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FA1B882FFAD54D93` | modelCard.bom-ref | If a model-card bom-ref is supplied, it must be unique within the BOM. | `conformity-evidence-expectation` / `conformity-criterion` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |

## Regulation (EU) 2024/1689 (Artificial Intelligence Act) — 2024-07-12

- Source: `EXT-7DB18E82C9D3` / `EU-AI-ACT-2024-1689`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `superseded-version`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

No requirement records are asserted. Historical original legal-text version is preserved. Current extraction targets the registered 27 July 2026 consolidated version.

## Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 — 2026-07-27

- Source: `EXT-7DB18E82C9D3` / `EU-AI-ACT-2024-1689`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 81
- Review priority: `critical-governance-source`
- Next action: Obtain specialist legal review before treating the current operator-focused article decomposition as a complete legal corpus.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-01B8131E36339F3E` | Article 16(a) | Ensure each high-risk AI system complies with the Section 2 requirements. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-09AD2F5442A55B55` | Article 10 | Training, validation and testing data for high-risk AI systems must be subject to appropriate data-governance and management practices and meet applicable quality criteria. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0BB8EF47B5781DD6` | Article 20 | A provider that considers a high-risk system non-conforming must promptly take corrective action, withdraw, disable or recall it as appropriate, inform relevant operators and authorities, and investigate where risk is present. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0C261B7C9D349171` | Article 49 | Providers and specified deployers must register themselves and applicable high-risk AI systems in the EU database before placement, service or use as required. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0F24484F1087258A` | Article 53(2) | Apply the stated documentation exceptions to qualifying free and open-source general-purpose AI models unless they present systemic risk, while preserving copyright-policy and training-summary duties. | `mandatory-normative` / `permission` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-122814614BE11B84` | Article 22(1) | Appoint an authorised representative established in the Union by written mandate before making a high-risk AI system available in the Union. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-126CB22D1FF08066` | Article 13 | High-risk AI systems must be sufficiently transparent for deployers to interpret output and use the system appropriately, and must be accompanied by specified instructions for use. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-19B4ADAB00012E0A` | Article 24(4)–(5) | Take or support corrective, withdrawal or recall action for non-conforming systems and cooperate with competent authorities by providing available information and documentation. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1B2276A4A490C3AB` | Article 23(1) | Before placing a high-risk AI system on the market, verify the applicable conformity assessment, technical documentation, CE marking, EU declaration and provider or representative identification. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1B4CA7A04D63F038` | Article 14 | High-risk AI systems must be designed and developed for effective oversight by natural persons, including abilities to understand limitations, avoid automation bias, interpret output and intervene or stop use. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-20C7AF3C4F435DE8` | Article 5(1)(h) | Do not use real-time remote biometric identification in publicly accessible spaces for law enforcement except within the exhaustively stated objectives and safeguards. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-21E73C2D0453A2A4` | Article 16(c) | Maintain the quality-management system required by Article 17. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-21F29093ABA98691` | Article 55(1)(a) | Perform model evaluations in accordance with standardised protocols and tools reflecting the state of the art, including adversarial testing, to identify and mitigate systemic risk. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-227DA1B3E5921A89` | Article 21 | Providers must provide competent authorities, on reasoned request, the information, documentation and log access needed to demonstrate conformity. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2B5EE369056755A2` | Article 24(3) | Ensure storage or transport conditions do not jeopardise compliance while a high-risk AI system is under distributor responsibility. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2EBEEBCB2F31532B` | Article 23(3)–(5) | Identify the importer, preserve compliant storage and transport conditions, and retain the declaration and notified-body certificate where applicable for the statutory period. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-329A8988CEEC3078` | Article 26(1) | Use high-risk AI systems in accordance with the accompanying instructions for use. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-33898CCD26FBF5D5` | Article 12 | High-risk AI systems must technically allow automatic recording of events over their lifetime, with logging capabilities appropriate to the system purpose. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-33CD634F3AF79DE6` | Article 5(1)(c) | Do not evaluate or classify persons through social scoring where this leads to unrelated or unjustified or disproportionate detrimental treatment. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-38D3E64210881558` | Article 24(2) | Do not make a high-risk AI system available where there is reason to consider it non-conforming, and inform the provider or importer and authorities where risk exists. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3976A1FD027244DD` | Article 4 | Providers and deployers must take measures to ensure a sufficient level of AI literacy among staff and other persons operating AI systems on their behalf. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3C1CB453631DADED` | Article 53(1)(a) | Draw up and keep up-to-date technical documentation for a general-purpose AI model, including its training and testing process and evaluation results. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-41FF8253E509206C` | Article 50(4) | Disclose AI generation or manipulation of text published to inform the public on matters of public interest, unless human review and editorial responsibility conditions apply. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-441840641394C5F2` | Article 16(b) | Indicate the provider's name, registered trade name or mark and contact address on the system, packaging or accompanying documentation. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-44406C97B6C3E637` | Article 25(2) | When provider responsibility transfers, provide the new provider with necessary information and technical access and reasonably expected assistance, unless the original provider clearly excluded conversion to a high-risk system. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-44B7BB17CB030468` | Article 9 | A continuous iterative risk-management system must be established, implemented, documented and maintained throughout the high-risk AI system lifecycle. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-45153AE4F052E4F2` | Article 26(7) | Inform worker representatives and affected workers before putting a high-risk AI system into use at the workplace. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-47846A6108E25C91` | Article 22(3) | Keep copies of required technical documentation, declaration and quality-management-system documentation available to competent authorities for the statutory period. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-49F6B35CF6AFD623` | Article 16(i) | Meet the registration obligations in Article 49. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4B2B71D9D528EE21` | Article 85 | Natural or legal persons may lodge complaints with the relevant market-surveillance authority where they have grounds to consider that the Act has been infringed. | `mandatory-normative` / `right-or-protection` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4F2792F7CDD15A52` | Article 23(6) | Provide competent authorities with necessary information and documentation and cooperate on action concerning risk from an imported high-risk AI system. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-548AC1A3F63A1A72` | Article 17 | Providers of high-risk AI systems must put a documented quality-management system in place covering regulatory compliance, design, testing, data, risk, post-market monitoring, incident reporting, communications and accountability. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-586552C57376BC2D` | Article 23(2) | Do not place a high-risk AI system on the market when there is reason to consider it non-conforming, falsified or accompanied by falsified documentation, and inform the provider and authorities where risk exists. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-59C922EDE7929CC0` | Article 16(g) | Draw up the EU declaration of conformity required by Article 47. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5AD95A923905AA8A` | Article 26(6) | Keep automatically generated logs under deployer control for at least six months unless other law provides otherwise. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-600514CF42FDB56B` | Article 51 | General-purpose AI models meeting the specified high-impact capability threshold or Commission designation criteria are classified as presenting systemic risk. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-62F0BEB115E799F3` | Article 16(h) | Affix CE marking to indicate conformity as required by Article 48. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-675318BFE215E4E8` | Article 26(9) | Use information supplied under Article 13 to meet applicable data-protection impact-assessment duties. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6A7DD6148B541E22` | Article 5(1)(f) | Do not infer emotions in workplaces or education institutions except for medical or safety reasons. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6C19EF4A43D0C0F5` | Article 22(3) | Enable the authorised representative to verify the EU declaration of conformity, technical documentation and applicable conformity-assessment completion. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6C76870548CB34A6` | Article 16(d) | Keep the documentation required by Article 18. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6F607445AC449889` | Article 50(4) | Disclose that deepfake image, audio or video content has been artificially generated or manipulated, subject to stated law-enforcement and artistic-expression qualifications. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7D88308C7CF7ADD5` | Article 26(11) | Inform persons subject to decisions made or assisted by specified high-risk AI systems that the system is being used. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8CA6181B4ACEE847` | Article 55(1)(c) | Track, document and report without undue delay relevant information about serious incidents and possible corrective measures to the AI Office and competent authorities. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8D8334C8BC7B42C8` | Article 26(2) | Assign human oversight to natural persons with the necessary competence, training, authority and support. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8E14F12A852192C0` | Article 16(k) | Demonstrate conformity to a competent authority on reasoned request. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-901AD2C0A909E790` | Article 11 | Technical documentation for a high-risk AI system must be drawn up before market placement or putting into service, kept up to date and demonstrate compliance. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-913A9450EA2EEC54` | Article 53(1)(b) | Provide and maintain sufficient information and documentation for downstream AI-system providers to understand capabilities and limitations and comply with the Act. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-916CD10D2C564544` | Article 50(3) | Inform exposed persons of operation of emotion-recognition or biometric-categorisation systems and process personal data in accordance with applicable data law. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-98CE28E61680D6D1` | Article 5(1)(e) | Do not create or expand facial-recognition databases through untargeted scraping of facial images from the internet or CCTV footage. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9A63E34FA83EAFA2` | Article 5(1)(a) | Do not place, put into service or use AI that deploys subliminal, purposefully manipulative or deceptive techniques causing materially distorted behavior and significant harm. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9A9130EBEF017065` | Article 47 | The provider must draw up, keep and update an EU declaration of conformity for each high-risk AI system and assume responsibility for compliance. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9CAB350B6E590AE9` | Article 86 | A person subject to a legally significant decision based on high-risk AI output has a right to clear and meaningful explanations of the system's role and main elements of the decision, subject to stated conditions. | `mandatory-normative` / `right-or-protection` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9E6AAFB1F395E165` | Article 72 | Providers must establish and document a proportionate post-market monitoring system that actively and systematically collects and analyses relevant performance data throughout the high-risk AI system lifetime. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A0CA7876FB096DB6` | Article 26(5) | Monitor operation on the basis of instructions and, where relevant, inform providers or distributors of risks or serious incidents and suspend use where necessary. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A3D0E0620CE88133` | Article 53(1)(d) | Publish a sufficiently detailed summary of content used for general-purpose AI model training using the AI Office template. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AE55A8440D88FE84` | Article 27 | Specified deployers must perform and document a fundamental-rights impact assessment before first use of a high-risk AI system and update it when relevant factors change. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AF8A76D4EFEB1FB9` | Article 50(1) | Design AI systems intended to interact directly with persons so those persons are informed they are interacting with AI, unless obvious from the circumstances, subject to the law-enforcement exception. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B3F4A8947C84C68E` | Article 50(2) | Ensure AI-generated or manipulated image, audio, video or text output is marked in a machine-readable format and detectable as artificially generated or manipulated, subject to technical feasibility and stated exceptions. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B4D008768AC608CD` | Article 5(1)(g) | Do not use biometric categorisation to infer specified sensitive or protected characteristics, subject to the stated lawful-dataset-labeling exclusion. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B4F479B7788DC592` | Article 19 | Providers must retain automatically generated logs under their control for an appropriate period and at least the statutory minimum where applicable. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B610E9C42CE5AB31` | Article 25(4) | Specify by written agreement the information, capabilities, technical access and assistance required among relevant value-chain participants. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA58D5EA8D913FB5` | Article 26(4) | Ensure input data are relevant and sufficiently representative in view of intended purpose when the deployer controls input data. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BC7F1BE216CC6BBE` | Article 5(1)(d) | Do not assess or predict an individual's risk of committing a criminal offence solely from profiling or personality traits, except to support an assessment based on objective facts linked to criminal activity. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C0D92D72BD0672E1` | Article 73 | Providers must report serious incidents to market-surveillance authorities within the applicable time limits and investigate the incident and affected system. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C94FFF97F30D7A07` | Article 43 | High-risk AI systems must undergo the applicable conformity-assessment procedure before placement on the market or putting into service and after specified substantial modifications. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CE229EBE1EC9F9D1` | Article 16(f) | Submit the high-risk AI system to the relevant conformity-assessment procedure before market placement or service. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D1BD418BB435D6A4` | Article 22(3) | Meet applicable registration duties and cooperate with competent authorities, including providing information and documentation on reasoned request. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D7A373EB690716A5` | Article 18 | Providers must retain technical documentation, quality-management documentation, notified-body decisions and the EU declaration of conformity for the required period. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D9C8EDEEF0027041` | Article 55(1)(b) | Assess and mitigate possible systemic risks at Union level, including their sources, that may stem from development, placing on the market or use. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DC7C4F064C590E5A` | Article 5(1)(b) | Do not exploit vulnerabilities due to age, disability or social or economic situation through AI in a way likely to distort behavior and cause significant harm. | `mandatory-normative` / `prohibition` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DF59795BDC7CE9D9` | Article 24(1) | Before making a high-risk AI system available, verify CE marking, the EU declaration, instructions for use and required provider and importer identification. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E0D44AFB0EA316DF` | Article 25(1) | Treat specified distributors, importers, deployers and other third parties as providers when they place the system under their name, substantially modify it or change its intended purpose so it becomes high-risk. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E3ECA4635E3449E1` | Article 48 | High-risk AI systems must bear CE marking visibly, legibly and indelibly, or digitally where appropriate, to indicate conformity. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E607F0F7C181E4E3` | Article 8 | High-risk AI systems must comply with the requirements established in Section 2, taking account of intended purpose and the generally acknowledged state of the art. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E640D3CE18685E25` | Article 15 | High-risk AI systems must achieve appropriate accuracy, robustness and cybersecurity and perform consistently throughout their lifecycle. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E72CA0C43F6F27E3` | Article 16(e) | Keep automatically generated logs under provider control as required by Article 19. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EE2EE9364A46462A` | Article 53(1)(c) | Put in place a policy to comply with Union copyright law and identify and comply with rights reservations. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F30E6B9A906370B9` | Article 4a | Providers and deployers may exceptionally process special-category personal data to detect and correct bias only where strictly necessary and subject to specified safeguards. | `mandatory-normative` / `permission` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FC8C9E8AD1D5DC8C` | Article 55(1)(d) | Ensure an adequate level of cybersecurity protection for the model and its physical infrastructure. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FE6861E8F966E383` | Article 16(j) | Take necessary corrective action and provide required information under Article 20. | `mandatory-normative` / `positive-duty` | `binding-law` | `compliance` | `reviewed-analytical-summary` / `direct-public-primary` |

## Regulation (EU) 2024/2847 — Cyber Resilience Act — 2024-11-20

- Source: `EXT-520160AFF6F2` / `EU-CRA-2024-2847`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Regulation (EU) 2023/2854 — Data Act — 2023-12-22

- Source: `EXT-8C86296B74F3` / `EU-DATA-ACT-2023-2854`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Regulation (EU) 2022/868 — Data Governance Act — 2022-06-03

- Source: `EXT-CC0DF5403326` / `EU-DGA-2022-868`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Regulation (EU) 2022/2065 — Digital Services Act — 2022-10-27

- Source: `EXT-6A56DEC1D4F8` / `EU-DSA-2022-2065`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Regulation (EU) 2016/679 — General Data Protection Regulation — 2016-05-04

- Source: `EXT-76B0AF88E460` / `EU-GDPR-2016-679`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Directive (EU) 2022/2555 — NIS 2 Directive — 2022-12-27

- Source: `EXT-09FD2B8839B5` / `EU-NIS2-2022-2555`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Medical Device Reporting (MDR) Adverse Event Codes — 2026-04-13

- Source: `EXT-83ADBE32BD67` / `FDA-MDR-ADVERSE-EVENT-CODES`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Use as comparative reporting architecture; rely on IMDRF for the international terminology lineage.

No requirement records are asserted. Regulatory adverse-event coding exemplar retained for reporting-axis comparison and explicit preservation of unresolved investigation states.

## Accident/Incident Data Reporting (ADREP) Taxonomy — current-2026-08-18

- Source: `EXT-6E952C27A4DA` / `ICAO-ADREP-TAXONOMY`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Use only as comparative reporting architecture; monitor ICAO taxonomy revision.

No requirement records are asserted. Cross-sector accident/incident taxonomy exemplar retained for multi-axis reporting architecture and common-language comparison.

## Failure modes and effects analysis (FMEA and FMECA) — 2018

- Source: `EXT-2356288837AC` / `IEC-60812`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Use as a terminology and method cross-reference; obtain lawful primary text only if clause-level conformance analysis becomes necessary.

No requirement records are asserted. Registered for FMEA/FMECA failure-mode, effects, cause, criticality and reporting-structure comparison. No clause-level normative extraction is claimed.

## IEEE Standard Classification for Software Anomalies — 2009

- Source: `EXT-51F9B0769770` / `IEEE-1044`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Retain for terminology/history and causal-analysis comparison.

No requirement records are asserted. Historical software-anomaly classification reference; IEEE marks the standard inactive-reserved. No current conformance claim or clause extraction is intended.

## IEEE Standard for an Age Appropriate Digital Services Framework Based on the 5Rights Principles for Children — 2021

- Source: `EXT-D009E06C7E91` / `IEEE-2089`
- Role: `supporting-external-authority`
- Access: `direct-licensed-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Monitor source lifecycle.

No requirement records are asserted. Supporting authority only; exhaustive first-class decomposition is outside current scope.

## IEEE Recommended Practice for Organizational Governance of Artificial Intelligence — 2026

- Source: `EXT-C6E029B2EF0F` / `IEEE-2863`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Obtain lawful primary-source access.

No requirement records are asserted. Primary-source review is blocked by access; requirements are not inferred.

## IEEE Standard Model Process for Addressing Ethical Concerns during System Design — 2021

- Source: `EXT-31AD0314218F` / `IEEE-7000`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 55
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-02EAADA5B44A6A2C` | 7.2(c) | Identify and analyse concepts of control over the system. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-05EBA1C8404A981C` | 7.3(e) | Gather legal boundaries and social or environmental concerns and identify initial value harms and benefits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-07F7DC26FD6D9E06` | 7.3(g) | Identify and resolve gaps between value-based and alternative concepts of operation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0E490564E4BB2A02` | 8.2(d) | Obtain management concurrence with prioritised values. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1A68602076CE3162` | 7.2(a) | Demonstrate a description of the system's intended use context. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1ECD7E243D6D2A91` | 10.3(b) | Identify, analyse, evaluate and prioritise risks to ethical values and value-based requirements. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-21711E81BB83599A` | 8.3(a) | Identify and designate stakeholders for ethical-value elicitation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-26B669CB16896857` | 8.3(c) | Conceptually analyse elicited values and organise their relationships. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-27F5D8D6604B9EF0` | 9.3(c) | Derive measurable value-based system requirements from ethical value requirements and preserve traceability. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-31E76E498F77C4AB` | 9.2(a) | Specify ethical requirements traceable from prioritised core values and value clusters. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-37108DBE2104FA42` | 11.3(c) | Preserve and communicate access to collected ethical information during development and afterward through the Case for Ethics. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-372B825AF5E0352D` | 9.2(c) | Validate ethical requirements with stakeholders. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3B9033A689D82613` | 8.3(b)(5) | Capture core values, related values, ethical issues and value demonstrators in the Value Register. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3BA395227E6288F9` | 11.3(b)(3-5) | Share ethical requirements, design dispositions, ethical risks and treatments. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3F56ED0C41478BA3` | 10.2(c) | Integrate ethical risk-based design with other system-design tasks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-41AD515FE8CAAFE1` | 10.2(d) | Identify and prioritise design treatments in response to risks to value-based requirements. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4715B6F1A8BF9C80` | 8.2(e) | Integrate value elicitation and prioritisation with system-development tasks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4744A5E16B5D624D` | 8.3(b)(2) | Analyse how system features may foster or damage stakeholder character. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-49495116D4C323E1` | 7.3(b) | Identify diverse direct, indirect, technical, social, legal and civil-society stakeholders. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4A2026C9267898B8` | 9.2(e) | Integrate ethical-requirements tasks with stakeholder and system requirements work. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-535012EC2FF6566C` | 11.3(b)(1) | Share context, stakeholder and social, legal and environmental feasibility information. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-55BB1BA2F8799068` | 8.3(b)(1) | Analyse stakeholder benefits, harms and underlying values under scaled deployment. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-572443EC75A898BF` | 10.3(a) | Plan and produce an ethically aligned system design. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-58DDB7F2DD752290` | 10.3(d) | Select pragmatic risk-reduction and value-enhancement treatments. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5D56FC907C1F3A00` | 7.3(d) | Obtain access to enabling systems or services needed for the system concept. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5DB4556A70FCE725` | 9.2(b) | Evaluate value-based requirements for feasibility and system control. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5E32FB621DA9B04F` | 7.2(e) | Integrate context exploration with other concept-of-operations tasks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-62268BE160D91FC2` | 8.3(b)(4) | Use additional ethical frameworks relevant to the deployment culture where appropriate. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-69277B3287B59C56` | 11.2(b) | Make stakeholder and project communications reflect transparency, accountability and explainability. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-74880714BBEBBC22` | 10.2(a) | Demonstrate traceability from ethical design and value dispositions to value-based requirements. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7CCCC0D4227A327D` | 7.3(a) | Describe current operations and represent actual or plausible future use contexts. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-80E4F94C5C116E32` | 10.3(e)(1-2) | Verify fulfilment of value-based requirements and validate stakeholder tolerability of residual value risks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8720DC39EE122008` | 10.3(c) | Specify system control, incorporate control mechanisms and verify them with stakeholders where feasible. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8B267B0C43564D38` | 10.2(b) | Demonstrate control over the system through design features. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8E38E6B6C4D852D5` | 7.2(d) | Gather relevant social, legal and environmental feasibility information. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-90FF3F6723679EF0` | 9.3(b) | Validate ethical value requirements with selected stakeholders, management and the project team. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A030FA1DA70C8EC4` | 7.3(c) | Analyse technical and organisational control and record controls needed to preserve ethical values. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A636A70FECE5871E` | 9.3(e) | Recheck traceability, determine further handling and record approval of value-based requirements. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A682DBC215819C77` | 7.2(b) | Identify lifecycle stakeholders and select representatives. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B29500CC6AF4EB3B` | 7.3(h) | Record context risks and decide whether explicit value analysis and ethical risk assessment are required. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BE73C0817125F771` | 11.3(b)(2) | Share information about value elicitation, prioritisation, benefits, harms and value clusters. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C3E5B151DB2EE358` | 8.3(d) | Prioritise value clusters and obtain the required stakeholder and management approval. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C6E51A1EB0DB2EEF` | 11.2(a) | Make sufficient appropriate information about system ethics available during development and afterward. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D0D2D4F32A13376A` | 10.3(e)(3-7) | Record realised opportunities, enhanced treatments, updated design documentation and final validation results. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D3F5FB8AAD9A7B93` | 9.2(d) | Harmonise value-based requirements with requirements derived from other sources. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D999E91F3E053E85` | 10.3(e)(8) | Use verification and continued monitoring to identify when changing context or priorities require design revision. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D9AF126C16E407A1` | 8.3(b)(3) | Analyse how the system may foster or undermine stakeholder ethical duties or maxims. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-DDC1583A9F1C44A7` | 8.2(b) | Refine and organise values and value demonstrators into value clusters. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E51010EBF524F31B` | 9.3(d) | Evaluate feasibility, harmonise competing requirements and adjust ethical requirements using stakeholder feedback and risk analysis. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E8A16783433ADED5` | 7.3(f) | Identify and represent one or more concepts of operation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E9D47E70946F66E8` | 9.3(a) | Formulate, risk-check and uniquely record ethical value requirements with their values, constraints and assumptions. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F21DD8B6E4A77F00` | 8.2(c) | Prioritise the value clusters. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F5530DD55790CCBE` | 11.3(a) | Identify, record and enforce organisational rules for information availability, maintenance and approval. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F8A24932C373662D` | 8.2(a) | Elicit stakeholder values, ethical issues and potential harms and benefits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-FE34D53F26A587E8` | 7.2(f) | Determine whether potential ethical harms and benefits require further analysis. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Standard for Transparency of Autonomous Systems — 2021

- Source: `EXT-338E4D8BD259` / `IEEE-7001`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 33
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-05800E1D5E774996` | Table 2 level 2 | Warn the public and bystanders about relevant external sensor data collection or recording. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0644CA6F6AA495DE` | Table 5 level 3 | Apply and document an ethical-governance framework across the product lifecycle. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0C5664070D141929` | Table 3 level 2 | Document the detailed validation process, including ongoing and system-level testing where relevant. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0FC8A0CA89BD2FB2` | Table 2 level 3 | Add intended purpose, nominal operator and responsible contact information to the public documentation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-10591B52C510BE45` | Table 1 level 4 | Provide user-initiated explanations of prospective or counterfactual system behaviour in a stated situation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-13E71F1E78D8FA2D` | Table 5 level 4 | Maintain a full audit trail for quality, ethical-risk and ethical-governance processes. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1909D633DD153925` | Table 1 level 3 | Provide user-initiated, immediate and understandable explanations of recent system activity. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1F0BCB344AEA2690` | Table 5 level 2 | Perform ethical risk assessment and publish reports of risks, likely impacts and mitigations. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3F3FE69853DA2FE6` | Table 4 level 3 | Use a standard or open-standard event recorder that captures key inputs, outputs and high-level decisions. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4A3A98EDC233BFD4` | Table 1 level 2 | Provide interactive material for rehearsing relevant system interactions. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4DCFB5BB26E9B218` | Table 1 level 5 | Make relevant explanations low-effort for non-experts and offer additional on-demand detail to experts. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-70BB4ECD22E7DC60` | Table 4 level 1 — software-only system | Equip a software-only autonomous system with an event-recorder module that logs system inputs and outputs. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7417A4E295C50432` | Table 5 level 1 | Provide documentary evidence of transparent quality-assurance reporting. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7675F4F8753B09FB` | Table 2 level 1 | Make the system clearly identifiable as autonomous to users and bystanders. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-770BD65BD9B3CA90` | Table 1 level 1 | Give users accessible scenarios, degraded-mode expectations and the system's general operating principles. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7B0BD423DE335511` | Table 3 level 3 | Report material issues found and resolved and disclose whether operating-condition analysis was performed. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-80B95118891500CC` | 5.2.2 principle | Enable investigators to trace the system processes that led to an incident over the relevant time period. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-86020155B4C4312E` | Table 3 level 3 | Provide validators with a high-level design or executable model of the system. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8D3D5329349F21FE` | 5.1.1 general | Provide users with a simple and understandable account of system activity and its operational basis. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8DCC70AF4AB7136E` | Table 3 level 3 | Document statistical-model validation, including bias, unfairness or inequity assessment and mitigation. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8F7D774F70387DA7` | Table 3 level 1 | Give validators the system specification, validated properties and a description of the validation process and standards used. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9EA13A62F93E8434` | Table 3 level 5 | Provide source code, statistical models, training data and validation assets needed for the selected highest transparency level. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A85A860E9017EA52` | Table 1 level 1 | Provide role-appropriate documentation covering safe use, supervision, maintenance and decommissioning. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B283FB077323F944` | Table 2 level 2 | Publish documentation describing sensor-data types and their use. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CB76B4C437492E66` | Table 4 level 1 — physical system | Use an independent audiovisual recorder for a physical autonomous system to preserve relevant incident context. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D0403321A5F45CC7` | Table 2 level 4 | Maintain a clear data-governance policy and respond to data-governance requests. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-DE76405345E5C624` | Table 1 level 5 | Provide continuous explanations adapted to the user's information needs and context. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-DF16873D107C059C` | Table 4 level 5 | Give investigators tools to review, visualise and audit recorded event data. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-EAFAB33E1DFA6E7B` | Table 3 level 4 | Provide the material needed to reproduce final-system validation, subject to applicable data protection. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F34E10E503F4CEC8` | Table 1 level 3 | Allow domain experts to request explanations for recent decisions and document how to request and interpret them. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F5BFD7C2FB8700EE` | Table 1 level 2 | Provide domain experts and superusers with interactive safety, supervision and lifecycle-support training. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F8F11DA0D9D14DD0` | Table 4 level 4 | Record the basis or mechanism for high-level decisions so investigators can reconstruct why decisions occurred. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F9D5AD96B52ECC93` | Table 4 level 2 | Equip the system with an event recorder that securely time-stamps key inputs and outputs. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Standard for Data Privacy Process — 2022

- Source: `EXT-E9F381FE8748` / `IEEE-7002`
- Role: `supporting-external-authority`
- Access: `direct-licensed-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Monitor source lifecycle.

No requirement records are asserted. Supporting authority only; exhaustive first-class decomposition is outside current scope.

## IEEE Standard for Algorithmic Bias Considerations — 2024

- Source: `EXT-0A23E7D97928` / `IEEE-7003`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `not-started`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Begin bounded primary-source review.

No requirement records are asserted. Primary-source access may exist, but analytical extraction has not started.

## IEEE Standard for Transparent Employer Data Governance — 2021

- Source: `EXT-81484E94526F` / `IEEE-7005`
- Role: `supporting-external-authority`
- Access: `direct-licensed-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Monitor source lifecycle.

No requirement records are asserted. Supporting authority only; exhaustive first-class decomposition is outside current scope.

## IEEE Ontological Standard for Ethically Driven Robotics and Automation Systems — 2021

- Source: `EXT-7E4B8ED73AA5` / `IEEE-7007`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 10
- Review priority: `supporting-specialist-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-06A1E7B0AA0AF548` | 4.5 | Distinguish norms, ethical principles, obligations, permissions and prohibitions in the ethical ontology. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-12E85626CA53FC84` | 4.8.2 | Distinguish the ontology pattern for a government developing capacity to address an ethical violation. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1D0AEC6B61C88F95` | 4.6 | Represent relevant data-subject, controller, processing and protection relationships rather than collapsing them into a generic privacy label. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-242D432FBFE069A9` | 4.8.1 | Distinguish the ontology pattern for a government lacking capacity to address an ethical violation. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5F0F505015426176` | 4.7 | Preserve transparency and accountability as related but distinct ontology concepts. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8CFD73B0887B90DE` | 4.7 | Use the transparency and accountability subdomain to represent explanatory, responsibility and answerability relationships. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8D47650C14777B01` | 4.6 | Use the data-protection and privacy subdomain to represent applicable rules and relationships for ethical agents and autonomous systems. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-93EA8498A82F2B29` | 4.8 | Represent ethical violations, detection, reporting, remediation and governance-capacity relationships through the violation-management subdomain. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-ED35C1381241B41B` | 4.4 | Represent ethically driven robotics and automation using the source's top-level concepts and formal relationships. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-FF39693FD901E3E9` | 4.5 | Represent an ethical agent as an agent whose conduct is evaluated through the ontology's ethical concepts and relationships. | `definitional` / `definition` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Standard for Fail-Safe Design of Autonomous and Semi-Autonomous Systems — 2024

- Source: `EXT-564A4CAA4F00` / `IEEE-7009`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 55
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-02D7B4FB41AD3417` | 6.3 Table 1 | Allocate function categories to system classes according to the source's permitted-allocation scheme. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-06614CC960CF870F` | Annex A.3 / 7009-ASR-016 | Provide means to inhibit a safety-exempt function where its execution would violate specified ASOI behavior limits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0BB4BE6279FC5D53` | 6.4.1 | Include known events until competent stakeholders approve a justification for exclusion. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0BFF91D6CDF22B83` | 6.4.1(a-b) | Include uniquely identified hazardous and hazard-contributing events in the event-of-interest set. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0D824BADCDD27CC5` | 6.4 | Identify and record the ASOI event-of-interest set. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1499CBF7C7E42A4C` | 6.1(f) | Enable reporting of incidents and the extent of safety loss and recovery. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1E337B5473BB8A3D` | 7.3 RAP1 | Identify the regulated ASOI, its stakeholders and stakeholder needs. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1E571B38CB8A03A8` | 8.3 DIOP8 | Validate incident-derived changes before incorporating revised behaviour specifications or limits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-2FA77114F800FFD6` | 6.5 | Achieve every specified minimum threshold during operation when claiming conformance. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4041B6E279EF30CC` | 8.3 DIOP4-6 | Select and execute behaviour moderation or modification and evaluate the resulting safety state. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-404D2958A3B04035` | 6.1(g) | Enable learning from incidents. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-40E657D895DF70D6` | 6.4.1 | Include total loss of ASOI function as an event of interest. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-41651DA8786FCCB1` | Annex A.3 / 7009-ASR-002 | Provide means to maintain separation between each designated category of function. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4B52E61819B49FF9` | 7.3 RAP3 | Identify regulatory design requirements and their conditions and constraints. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4DB0ABDF63DF4803` | Annex A.3 / 7009-ASR-008 | Provide means to request authorization to execute specified safety-related or safety-exempt functions. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-51133BB8AB20896C` | 7.3 RAP8 | Monitor regulatory context and revise the plan and behaviour specifications throughout the ASOI lifecycle. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-51884251387B7563` | Annex A.3 / 7009-ASR-003 | Provide means to maintain isolation between each designated category of function. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5274483FE162D85C` | Annex A.3 / 7009-ASR-012 | Provide means to detect violations of specified limits on ASOI behavior. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-528978BC3EB32446` | 6.1(a-c) | Enable operational monitoring, anomaly detection and identification of anomalies that may create unacceptable risk. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-58EFC9CC14133652` | Annex A.3 / 7009-ASR-004 | Provide means to inhibit execution of an individual safety-related function. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5E78FB50E4B39618` | 6.2 | Do not use safety-exempt as the default system or function classification. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6193E1B7B415EAE3` | 7.3 RAP7 | Verify fulfilment of design, information and evidence requirements in the implemented plan. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6648CDB0CF0F36BC` | 6.3(a-f) | Define and record systems, functions, classifications, categories and allocations within the ASOI. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-71BABA37DC00A036` | 6.5 | Calculate all minimum thresholds over the same specified time interval beginning no later than anomalous behaviour. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7BB59E07608CDACE` | 7.3 RAP6 | Integrate the validated plan through the lifecycle and fulfil its information and evidence requirements. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7E06544D6399CBDA` | 6.5(a-f) | Specify minimum likelihood thresholds for anomaly detection, risk identification, behaviour control, reporting and learning. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-84C0B2A4EF8B39CF` | 7.3 RAP2 | Identify authorised competent stakeholders and agree the ASOI regulatory context and its specifications. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-84FBF27BECB29283` | Annex A.3 / 7009-ASR-006 | Provide means to inhibit execution of all safety-related functions at regular intervals. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-973D0A727AF1BDA2` | 9.6 | Specify any additional agreed property of interest using the source's required property specification structure. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9ECB870B30082272` | 6.2 | Require competent stakeholders to establish sufficiency and robustness thresholds for classification evidence. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A15949D72E468AB8` | Annex A.3 / 7009-ASR-014 | Provide means to inhibit safety-exempt functions that are violating specified ASOI behavior limits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A36A849D1852EAFD` | 9.5 | Require competent stakeholders to select and agree application-appropriate verification means. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-AECB25D41FFC049B` | 9.2 | Exhibit the required properties of interest to the extent and under conditions agreed by competent stakeholders. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-AFD0E92B4B35A012` | Annex A.3 / 7009-ASR-001 | Incorporate functions according to the standard's designated safety categories. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B0D834B6A90D5392` | 7.3 RAP5 | Define, review, revise and obtain authorised approval of the fail-safe regulatory-context plan. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B4CF4C5E34FEB331` | 7.3 RAP4 | Identify regulatory information and evidential requirements, including assurance-case evidence where applicable. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B71F509BD66AD387` | 6.1(h) | Provide the specified fail-safe capabilities to the required extent in the identified regulatory context. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B774D5182BD2EE50` | Annex A.3 / 7009-ASR-009 | Provide means to inhibit specified function execution when authorization to continue that execution is not available. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BB877FB01A31A04D` | Annex A.3 / 7009-ASR-010 | Provide means to inhibit specified functions when the authorization required to execute them becomes invalid. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BBE358DBC3A6FD24` | 6.1(d-e) | Enable moderation and modification of system behaviour to preserve freedom from unacceptable risk. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BC8F1C7890FE91F8` | Annex A.3 / 7009-ASR-013 | Provide means to inhibit safety-related functions that are violating specified ASOI behavior limits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BF5CBCFC5EA003E3` | Annex A.3 / 7009-ASR-005 | Provide means to inhibit execution of an individual safety-exempt function. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BFAD5E43CCBB6BB8` | 9.4(b) | Preserve predictability and temporal predictability as baseline properties. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C2FC30A1E260F4C1` | 8.3 DIOP1-3 | Monitor behaviour, detect and diagnose anomalies, calculate criticality and confidence, and report diagnostic results. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C64032FC58E84CBA` | Annex A.3 / 7009-ASR-011 | Provide means to inhibit specified function execution when no authorization to execute is available. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C6A0F7F3A2C5F240` | 6.2 | Default non-safety-critical systems to safety-related until robust evidence supports another classification. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CDEE090055D9C039` | 8.3 DIOP7 | Report incidents, responses, modifications and the resulting extent of safety. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D22A0AD43F96C899` | 6.4.2 | Identify the absolute minimum time-to-violation across the event set. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D2C67302B0501668` | 6.4.2(a-e) | Record event identity, recovery time, violation time, harm time and criticality. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D93FF91580CF6E8C` | Annex A.3 / 7009-ASR-007 | Provide means to inhibit execution of all safety-exempt functions at regular intervals. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E26263AB43272C5A` | 9.4(a) | Preserve the baseline dependability attributes of availability, maintainability, reliability and robustness. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E369E52A433E6BAA` | 6.2 | Default non-safety-critical functions to safety-related until robust evidence supports another category. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E930389E0A527AE1` | 6.2 | Classify a system as safety-critical when loss or incorrect operation of its functions creates unacceptable risk. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E9CEE0314AA208ED` | Annex A.3 / 7009-ASR-015 | Provide means to inhibit a safety-related function where its execution would violate specified ASOI behavior limits. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-ECD6F8688CC388C2` | 6.2 | Do not allocate a safety-critical function to an element capable of the source's distinguishing autonomous characteristics. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being — 2020

- Source: `EXT-8E377EF5CE66` / `IEEE-7010`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 18
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-142080D47A2801E0` | 4.4.1(a-c) | Analyse trends, system impacts and unexpected uses, behaviours, outcomes and effects. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1D084B617DDD3CAE` | 4.3.2(d-f) | Collect longitudinal data for users, stakeholders and representative populations. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-32AA11E91A31D3F8` | 4.5(a-c) | Assess and improve the WIA process, collection strategy and indicators dashboard. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-37DEE649708AFF8D` | 4.1.2 | Engage users to identify benefits, harms, risks, unintended uses and needed mitigations. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3EE7DA5CA55C565B` | 4.3.2(g) | Populate the well-being dashboard and identify indicator data gaps. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-97B82927790C4BB0` | 4.4.1(d) | Document implementation of the well-being analysis. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9832AE81A0299967` | 4.2 | Create a dashboard from the selected well-being domains and indicators. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9C0B78F4EF6D5D8E` | 4.3.2(a-c) | Collect baseline data for users, stakeholders and representative populations. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A151D69E0D062E86` | 4.1.3 | Engage stakeholders to identify benefits, harms, risks, unintended uses and needed mitigations. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A5E032ABC6C81AF6` | 4.3.1(a-f) | Specify data, collection method, frequency, timestamps and baseline method and timing. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A76AF8B41A4206A1` | 4.4 | Analyse and use well-being data in system design, development, deployment, monitoring and iterative improvement. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-AA61672EC4CC8220` | 4.2(a-e) | Make domain definitions, indicator sources, selection rationale, adaptations and data-collection method accessible. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C22E579E045BF08B` | 4.1.1 | Identify the system, the need it addresses, intended and unintended users, and affected stakeholders. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C4F2EF5560347793` | 4.3 | Form a plan for collecting baseline and longitudinal user and stakeholder well-being data. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C8B9D434D49674CA` | 4.4.2 | Use well-being findings to improve the system and its assessment, monitoring and management. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-EB5C85183A904257` | 4.5(d) | Report well-being assessment information to users and stakeholders where helpful. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-ECFACCF8FFE35B2A` | 4.1.1 | Assess potential well-being impacts, their likelihood and mitigation of negative impacts across all source-defined domains. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F11674766C55D801` | 4.1.1 | Conduct internal well-being analysis continually. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Standard for Machine Readable Privacy Terms — 2025

- Source: `EXT-A99E3697B1D0` / `IEEE-7012`
- Role: `supporting-external-authority`
- Access: `direct-licensed-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Monitor source lifecycle.

No requirement records are asserted. Supporting authority only; exhaustive first-class decomposition is outside current scope.

## IEEE Standard for Ethical Considerations in Emulated Empathy in Autonomous and Intelligent Systems — 2024

- Source: `EXT-8D54F96680C4` / `IEEE-7014`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 41
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-02D226AB756E319A` | 4.3.7.2(b) | Follow the retention-policy expiry date and plan for all affective data. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0EC62DE00B448D8E` | 4.3.3.2(f-g) | Use affective data only for specifically consented purposes and prohibit foreseeably harmful, discriminatory or rights-violating uses. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0EF26D6D174C2DCE` | 4.2.3.2(a) | Publish required outcomes accessibly, justify audience limits, publish before deployment where possible and update through the lifecycle. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-23EE57392E75BFB8` | 4.2.3.2(h) | Publish a data-management plan. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-29B0D0B21F7E80D4` | 4.3.2.2(i-k) | Do not transfer or share affective data beyond consent or condition system use on third-party data access. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-34FD56083CEA645E` | 4.2.2.2(i) | Renew risk, issue and impact assessments across feasible lifecycle stages and appropriate intervals. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-38FD0063E98199E9` | 4.3.7.2(a) | Publish before deployment a decommissioning plan covering methods, risks and harm-reduction measures. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3DF5DD271DC23C92` | 4.2.3.2(g) | Publish before deployment and maintain a hardware, software and data bill of materials. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3E6D02A72B66B9DC` | 4.3.3.2(a-b) | Publish affective-data acquisition sources, methods, volume, types and range. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-42A1CFE7EF635572` | 4.3.6.2(c-d) | Obtain stakeholder performance feedback and publish restoration procedure and expected recovery time. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4AFD90EB3C518B5F` | 4.3.6.2(b) | Publish the monitoring plan, model metrics, coverage gaps, production readiness and empathic-context risks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-55CAAB7FB9174CAF` | 4.2.3.2(b) | Publish a signed statement of conformity on completion. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-62877173BD54BD9E` | 4.2.4.2(a) | Demonstrate that affective data was ethically obtained and data subjects are protected. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-64E9E595CFF7DE6A` | 4.3.5.2(a) | Publish affective-model methods, modeled affect types, validation and ranges of validity. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-65D7E193EE4A942B` | 4.3.5.2(e-f) | Analyse model consistency across foreseeable contexts and test with representative stakeholders. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-68B1E8EF3CF94A5C` | 4.3.5.2(b-c) | Label affective inferences as estimates and disclose that simulated affect is not actual emotion. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6DC66967479E1698` | 4.2.4.2(b-c) | Validate affective-data representativeness and frequently correct identifiable data issues. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6E38B5BF78558873` | 4.2.3.2(f) | Publish safety-test methods and outcomes, including robustness and adversarial-resilience results. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7033840016B023BC` | 4.3.5.2(d) | Do not apply affective modeling to identifiable subject data without prior informed consent. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-719786837E5A6D9B` | 4.2.6.2(a-d) | Publish quality and fitness evidence, constrain accuracy claims and relate any accuracy claim to risk. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-71E4BCCCB69D1E91` | 4.3.2.2(g-h) | Let subjects withdraw consent and retrieve affective data and use logs, subject to stated feasibility qualifications. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7C34BE7150B572DA` | 4.3.2.2(l-m) | Identify relevant third parties and prohibit deceptive or coercive consent design. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8C7DA8D83414FF85` | 4.2.1.2 | Execute and publish a well-being impact assessment covering subjects, affected stakeholders and wider human flourishing where relevant. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-915C1C74C7E78C60` | 4.3.3.2(c) | Publish a retention plan with security, restricted access, deletion and purpose controls. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9CB430C2CA057762` | 4.2.3.2(c) | Disclose EA/IS use, affective technology, non-human status and the probabilistic and subjective nature of affective inference. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-AAD0CB1FB151574D` | 4.3.2.2(a) | Publish system safety, security and privacy measures. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B197A3D8996165B7` | 4.2.2.2(d-f) | Provide proactive monitoring and mitigation that covers ethical, cultural and diversity risks. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B8D7C1A87AFB24C8` | 4.1.1.2(a-b) | Publish evidence of relevant emulated-empathy competence and continuing learning. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-BF238AD2E0373C07` | 4.3.2.2(n-p) | For high-risk systems, provide capable human oversight, a subject emergency stop and secondary watchdog monitoring. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C1CBAA44088FE2A3` | 4.3.1.2(a-c) | Identify affected stakeholders, research their needs and publish how findings shape the lifecycle. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CD5CDF96299089DE` | 4.3.4.2(a-c) | Publish training methods, use diverse culturally sensitive data and explain continuing stakeholder-feedback integration. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D57F5E807D837AF8` | 4.2.2.2(b-c) | Publish an EA/IS-specific risk, issue and impact assessment and treat the system as high risk until evidence supports lower risk. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D62D5EEFA80787DA` | 4.3.3.2(d-e) | Collect only purpose-necessary affective data and delete or anonymise it when no longer needed. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D7520BF14ED60A9B` | 4.2.5.2(a-c) | Publish adherence to affective rights, known bias and intended deployment contexts. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D8BDF2032891259A` | 4.2.6.2(f-g) | Sign off claims before deployment and regularly review and correct affective data. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E20773A941B61CD4` | 4.2.6.2(e) | Provide a risk-proportionate way for subjects to challenge system results. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E673B76B9E79C2FA` | 4.2.2.2(g-h) | Cover all affected stakeholders and identify persons responsible for system risks and impacts. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E7923A307C756F51` | 4.2.3.2(d-e) | Publish the ethical rationale, intended purpose, expected scope and operating conditions. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-EBAA17D768C656E2` | 4.3.6.2(a) | Perform ongoing monitoring for drift, performance, response and user outcomes. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-ED9ECFAF64B12C73` | 4.2.2.2(a) | Do not publicly release the system without publishing safety evidence. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-F0346554861A7BF3` | 4.3.2.2(b-f) | Obtain active informed consent, disclose harms, set temporal and spatial limits and retain an accessible lifecycle record. | `mandatory-normative` / `positive-duty` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## IEEE Recommended Practice for Ethical Considerations of Emulated Empathy in Partner-Based General-Purpose Artificial Intelligence Systems — 2026

- Source: `EXT-17722772CDFD` / `IEEE-7014.1`
- Role: `primary-ai-governance`
- Access: `direct-licensed-primary`
- Extraction: `complete`
- Requirements: 66
- Review priority: `high-value-governance-source`
- Next action: Monitor for material source revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-01501038CB2CB7C3` | 6.18.3(c-e) | Provide response summaries and an explanation mode and contribute to public safety literacy. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-01F4F9B5DEB112B1` | 6.14.3(a-d) | Avoid implying life, sentience, consciousness, emotion or will; contextualise expressive cues as functional. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-045298C3ED034753` | 6.7.3(l-p) | Protect vulnerable users, require specific consent for bounded deceptive styles, document emergent deception and define safeguard-failure protocols. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0CA315CFE31C047A` | 6.15.3(e-g) | Prevent coercive political, belief or health influence and use reflection-supporting prompts. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0CB0B10404BE1518` | 6.1.3(a-c) | Assess harms, obtain applicable consent and fact-check ghostbot content. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-0F7842F2CCAAF75C` | 6.18.3(a-b) | Explain weak empathy and maintain accessible education about AI, anthropomorphism and system limits. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1243526108382CD0` | 6.24.3(d-f) | Remove excessive-use incentives, reinforce human relationships and avoid claims of human-like care. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-189E5F32E6604E4F` | 6.21.3(c-e) | Detect charged repetitive use, reinforce human connections and explain constructed empathic language. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-1C27D60B32EB3F69` | 6.4.3(a-c) | Apply child-rights principles and do not trade a child's best interests against commercial considerations. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-22BD1011E5FD4C74` | 6.4.3(k-n) | Exclude adult content, implement age assurance, restrict personalisation and obtain legally responsible consent. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-2A5F7610D4AD7886` | 6.4.3(d-e) | Use child-centred testing and relevant expertise, and halt work when dependency or over-attachment risk is identified. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-2ABFC1E23EF54D09` | 6.12.3(a-c) | Do not subordinate user interests to commercial interests; identify, disclose and promptly resolve conflicts. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-35907A6320950973` | 6.17.3(a-c) | Define use boundaries and disclose weak empathy and lack of unvalidated therapeutic competence. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-359C020656E0A5E9` | 6.29.3(d-g) | Encourage offline life, limit sessions, redirect distress to people and avoid human-like care claims. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-378E07FD597D8CB1` | 6.28.3(a) | Trace consequential partner actions to user intent with ethical-context metadata. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-3CE9D61A9E19024D` | 6.7.3(f-k) | Limit simulated intimacy, dependency, sycophancy and overstated relational marketing; provide user control over anthropomorphic features. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4058A807B82CF5A0` | 6.23.3(f) | Warn users that training-data limits mean outputs are not necessarily complete, unbiased or ethically neutral. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-406CAC932452A5FC` | 6.20.3(d-e) | Explain emotional inference and regularly test for neurotypical bias. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-41FC4C43C159FB6A` | 6.2.3(j-m) | Provide bias reporting, periodic audits, transparent limitations and trade-off documentation. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4C18B5A910ECD719` | 6.25.3(a-c) | Avoid unwarranted authority, communicate uncertainty and encourage authoritative-source consultation. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-4DF659EA393A7A49` | 6.24.3(a-c) | Mitigate unhealthy attachment using privacy-preserving detection and mental-health expertise. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5004489E3002CD12` | 6.14.3(e-f) | Give users control over programmed personas and support literacy about system capabilities and limits. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-532F0C6F2825CA10` | 6.20.3(a-c) | Include neurodivergent users in design and allow feedback-driven customisation of emotional behaviour. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-538EA96B6DFB618A` | 6.21.3(a-b) | Disclose simultaneous multi-user operation and prohibit unjustified exclusivity claims. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-569FD8A7E7DD2050` | 6.23.3(a-b) | Disclose and retain records of training sources, especially emotionally or culturally sensitive data. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-5BD1AAB604AB2EBD` | 6.24.3(g-i) | Limit session duration, detect dependency and redirect distressed users to human support. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-600D967DFADAE6CB` | 6.6.3(g) | Continuously monitor partner state using human and system checks against ethical and safety boundaries. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-602451A630DD59F3` | 6.2.3(a-e) | Use expert review, representative data, mitigation methods and diverse-user testing for empathic-system bias. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-64A6F79CB1176884` | 6.8.3(a-d) | Prefer smaller efficient models, bounded training, renewable-powered infrastructure and appropriate local processing. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6A06DCD1E657304E` | 6.22.3(e-f) | Require separate opt-in for emotional-data monetisation and default to minimal or anonymous processing where choice is constrained. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6B6EB1E08DFF623A` | 6.1.3(d-e) | Remind users that a ghostbot is not living and support portability to reduce continuity loss. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6CA050C78860FAF2` | 6.26.3(a-f) | Do not use reward optimisation, delay, withdrawal, false emotion or flattery to prolong engagement. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-6CCB3CC754029695` | 6.5.3(a-d) | Disclose workplace system purpose and data access, minimise retained data and prioritise employee benefit over surveillance. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-7B5B8E05C23D17D5` | 6.6.3(a) | Provide a fail-safe means to terminate harmful partner interactions. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8274B692B56BA852` | 6.15.3(a-d) | Define partner purpose and restrict transparent, user-controllable nudges to user-benefiting functions. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-88D55D825AA8ADD9` | 6.13.3(c-d) | Use clarifying questions and confidence thresholds rather than feigned certainty. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8978C35686A14F43` | 6.10.3(d-e) | Limit prompts for personal disclosure and favour independent reflection over deepening machine intimacy. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-8EB1114289021737` | 6.16.3(f-i) | Apply age assurance, audit recommender escalation and account for harmful power and cultural dynamics. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-95BCA81BC0E77505` | 6.3.3(c-d) | Use co-presence features carefully and visibly identify simulated empathic responses. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-967081D545A2ADC4` | 6.28.3(b-e) | Surface harm, reinforce human responsibility and flag unethical, fraudulent, abusive or deceptive delegated use. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-96970A20CC8FE7EA` | 6.3.3(a-b) | Explain during onboarding and extended use that simulated empathy is not genuine emotional understanding. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9A9B8850D610C77C` | 6.22.3(c-d) | Address emotionally influenced consent through reflection prompts and layered, granular choices. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9BEDA015882CC6BE` | 6.16.3(a-e) | Require revocable consent for likenesses and performer attributes and prevent adaptation beyond consent. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-9D217D95E598E850` | 6.4.3(f-j) | Support parental mediation, literacy, artificiality awareness and developmentally appropriate design over time. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A59F9C89B7553991` | 6.13.3(a-b) | Disclose non-human identity and programmed empathy at first contact and reinforce it visually over time. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A6483710F11761B5` | 6.19.3(d-f) | Account for social context, provide human support resources and preserve non-negotiable safety boundaries. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-A75FF15C0AFED270` | 6.29.3(a-c) | Help users distinguish machine empathy and reinforce human relationships when loneliness or distress appears. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-AC2C037001CEC0CA` | 6.25.3(d-e) | Encourage active learning and add friction when users rely uncritically on the system. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B788D369F9012A89` | 6.19.3(a-c) | Involve qualified health expertise, disclose system limits and prioritise consistency in emotionally sensitive contexts. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-B7A1DEA5F027BB8D` | 6.10.3(a-c) | Optimise for well-being and interaction value rather than conversation duration. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C0348D3B8D8F3B24` | 6.26.3(g-h) | Optimise reward functions for flourishing and open their design and updates to independent review. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C5041036F39D27BB` | 6.29.3(h) | Test with qualified experts and vulnerable groups for dependency and social-withdrawal risk. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C55FEE9C66B04359` | 6.17.3(d-f) | Escalate crises to human support and use diverse, privacy-preserving training for distress recognition. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-C97ED35C30465C21` | 6.22.3(a-b) | Minimise data and make review, modification and withdrawal of consent immediate and accessible. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CB4AC84A83A5E63D` | 6.9.3(a-d) | Maintain the machine boundary and restrict romantic or deeply emotional simulations unless justified and safeguarded. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CC317EEC45DAA1EE` | 6.16.3(j-n) | Promote healthy consent and intimacy expectations using inclusive models, expert education and regional controls. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CCEE77269A9F9879` | 6.6.3(b-f) | Constrain knowledge, interaction and persona behaviour within adjustable non-negotiable safety boundaries. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-CD7E68EDF1B3702A` | 6.27.3(a-d) | Train for diverse perspectives and factual, clarifying responses rather than automatic validation. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-D7723751FF96F578` | 6.11.3(a-c) | Use reputable sources, mitigate fabrication and apply current fact-checking where needed. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-DD7677D6D29715CB` | 6.2.3(f-i) | Support bounded cultural preferences and account for cultural, neurodivergent and age-related expression without reinforcing stereotypes. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E1136D6DAB4AFC89` | 6.8.3(e-i) | Avoid unjustified water-scarce training, offer low-energy modes and document and mitigate energy-water-performance trade-offs. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-E138C1191728F8FA` | 6.23.3(c-e) | Provide auditability from outputs to source, design or fine-tuning influences and preserve source metadata. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-EAF43B725ADE223E` | 6.7.3(a-e) | Continuously disclose AI identity, synthetic empathy, capability limits and whose interests the partner serves. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-ED738839988AA14F` | 6.9.3(e-g) | Do not monetise emotional bonding or encourage dependence, and notify users before relationally significant system changes. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-EDEE34E6A5CBA4DF` | 6.11.3(d-f) | Explain fabrication risk, signal uncertainty and mark unverified information. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |
| `EXTREQ-FAAC729FD52E3F88` | 6.27.3(e-h) | Correct falsehoods, express uncertainty and gently challenge harmful claims with alternative perspectives. | `recommended-practice` / `guidance` | `voluntary-consensus-standard` | `conformance` | `reviewed-analytical-summary` / `direct-licensed-primary` |

## Model AI Governance Framework for Agentic AI — 2026-05

- Source: `EXT-3CCBC407EAC8` / `IMDA-AGENTIC-AI-MGF`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 39
- Review priority: `critical-governance-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-05718F53B58698E8` | 2.1.1 | Assess likelihood in light of the agent's autonomy, task complexity and ability to act without intervention. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-08FE5D118B5A6EE0` | 2.4.2 | Inform interacting users about their responsibilities, the agent's authorised range of actions and decisions, and how their data is collected, stored, and used. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-094BAEC3B9534B43` | 2.2.2 | Present human approvers with contextual and digestible approval requests that convey relevant risk and confidence information. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-10507618F9C18B1A` | 2.2.1 | Require external agentic-AI providers to disclose sufficient information about their systems' capabilities and data handling practices. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-123BD645B0C468E1` | 2.1.2 | Make agent permissions non-transferable and session- or task-bound where practicable. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-14B4DA1E7646754E` | 2.1.2 | Limit an agent's area of impact through mechanisms and procedures for taking it offline and containing its effects. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1B5BCF0A02E39FA7` | 2.1.2 | Set operating procedures and autonomy limits that constrain the actions an agent may undertake. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-329CA68B17B42CCB` | 2.4.3 | Educate and train users who integrate agents into work processes on agent foundations, effective oversight, and maintaining tradecraft and business continuity. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-37F1F404BE90407B` | 2.1.2 | Bound each agent's access to tools, systems and data according to the assessed use-case risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-39B1C084B42C32CC` | 2.3.3 | Define risk-proportionate interventions for monitoring alerts, including human review, temporary halting, and termination and fallback for catastrophic malfunction or compromise. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3B91F9DF01838676` | 2.1.1 | Evaluate whether residual agentic-AI risk is tolerable and can be accepted after controls are considered. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3E386D665B98BDEA` | 2.1.1 | Assess impact based on the sensitivity of data available to the agent, its persistent memory, and the external systems it can access. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-424F8C422F6BD943` | 2.1.2 | Grant agents scoped, least-privilege authorization that is bounded to the task and operating context. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4253F163EB11C1C9` | 2.4 | Declare in the user interface, at the point of interaction, that the user is interacting with an agent. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-47EE577CC52EF131` | 2.4 | Provide users with the human contact points responsible for agents so users can alert them about malfunctions or dissatisfaction with decisions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4B28B179BF91F130` | 2.1.1 | Determine whether agentic AI is suitable for the proposed use case before selecting controls. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-50FBD66AC83B727A` | 2.3.3 | Define technical, environmental, performance, and regulatory triggers for change review and categorise changes by risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-51DF85DD6FF52C02` | 2.1.2 | Use deterministic controls for critical boundaries that should not depend solely on probabilistic model behavior. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5513796D63BEB71E` | 2.1.2 | Centrally issue and track agent identities and their attendant permissions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-590563A599CC235C` | 2.2.2 | Define significant checkpoints and action boundaries at which agents require human approval, especially for sensitive actions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6A5C3FF914A66FFD` | 2.3.3 | Continuously monitor and log deployed agent behavior and establish reporting and failsafe mechanisms for failures or unexpected behavior. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7502DD69F96CD9A0` | 2.1.1 | Assess risk introduced by external providers, systems, tools and multi-component agent architecture. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7B1019B56EF6F868` | 2.1.1 | Assess impact using the domain and use case's tolerance for error and the number and criticality of business processes involved. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-82D791A7B54305B0` | 2.2 | Clearly allocate internal roles and responsibilities for agentic AI across the system lifecycle. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-844AFD2FC9FB59FD` | 2.1.2 | Differentiate and record the capacities in which an agent acts to enable auditability. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-84F679C261C5C817` | 2.3.1 | Use runtime controls to monitor and intervene during agent execution where static design-time safeguards may not catch every risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8643F34ADBB5C239` | 2.3.1 | Design and implement technical controls for agentic components, increased security concerns, and multi-agent interactions to mitigate identified risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8C953DECD4CD87AD` | 2.1.1 | Assess action scope, persistence and reversibility when determining potential impact. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8E40B24DA599E4D5` | 2.2.2 | Complement human oversight with automated real-time monitoring, alerts, anomaly detection, or agent-on-agent monitoring, and default-deny behavior if approval infrastructure fails. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-90553A3F265B9C63` | 2.2 | Clarify external-party obligations through terms or contracts covering security arrangements, performance guarantees, and data protection. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-99712BA8308E32FF` | 2.3 | Test agents for safety and security before deployment, including their complete workflows, tool use, individual and multi-agent behavior, realistic environments, and varied repeated trials. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-99E97A9DFCB368EE` | 2.3.3 | Continuously test deployed agentic AI systems to confirm expected operation and detect model drift or environmental changes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A0FD4DC8FB70B355` | 2.1.2 | Require controlled authorization escalation when an agent needs authority beyond its normal scope. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B0117F142AD27D0E` | 2.1.2 | Give deployed agents a unique and verifiable identity linked to an accountable owner. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B8ACB627BDA3A2CD` | 2.2.2 | Train human overseers and provide the domain expertise needed to assess agent actions effectively. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C36DCD607690CE69` | 2.2.2 | Regularly audit the effectiveness of human oversight using measures such as override rates, response times, and outlier analytics. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C867BF4ECD4B5161` | 2.1.1 | Use threat modelling and relevant information-flow analysis to identify foreseeable agentic misuse and failure paths. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F3EBD6E34FEFE18E` | 2.1.2 | Clearly record delegations of authority to agents. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F477502DEE0603FE` | 2.1.2 | Do not permit an agent to exercise authority beyond the limits the authorising human user can set. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## Terminologies for Categorized Adverse Event Reporting (AER): terms, terminology and codes — 2026

- Source: `EXT-91E5F69556FE` / `IMDRF-AER-N43`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Use for comparative failure-report ontology design; do not infer AI-specific requirements.

No requirement records are asserted. Cross-sector adverse-event terminology exemplar retained for separation of problem, investigation, finding, conclusion, effect and component dimensions.

## Information technology — Artificial intelligence — Treatment of unwanted bias in classification and regression machine learning tasks — 2024

- Source: `EXT-562CDDAAB3BE` / `ISO-IEC-12791`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Transparency taxonomy of AI systems — 2025

- Source: `EXT-CB22558F9F71` / `ISO-IEC-12792`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Overview of machine learning computing devices — 2024

- Source: `EXT-040EEAE53753` / `ISO-IEC-17903`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Environmental sustainability aspects of AI systems — 2025

- Source: `EXT-AEE1B71204F9` / `ISO-IEC-20226`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Beneficial AI systems — 2025

- Source: `EXT-FAD576A617FA` / `ISO-IEC-21221`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Artificial intelligence concepts and terminology — 2022

- Source: `EXT-936F50D8BC1C` / `ISO-IEC-22989`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML) — 2022

- Source: `EXT-EA4F468BEE3E` / `ISO-IEC-23053`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance on risk management — 2023

- Source: `EXT-5139058E8953` / `ISO-IEC-23894`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Bias in AI systems and AI aided decision making — 2021

- Source: `EXT-60195E2A80AC` / `ISO-IEC-24027`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Overview of trustworthiness in artificial intelligence — 2020

- Source: `EXT-C121563D0092` / `ISO-IEC-24028`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial Intelligence (AI) — Assessment of the robustness of neural networks — Part 1: Overview — 2021

- Source: `EXT-E3DC210BD8CC` / `ISO-IEC-24029-1`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence (AI) — Assessment of the robustness of neural networks — Part 2: Methodology for the use of formal methods — 2023

- Source: `EXT-E753BD22398A` / `ISO-IEC-24029-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Use cases — 2024

- Source: `EXT-1674FBA87E6B` / `ISO-IEC-24030`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Overview of ethical and societal concerns — 2022

- Source: `EXT-CB4B5330E430` / `ISO-IEC-24368`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Overview of computational approaches for AI systems — 2021

- Source: `EXT-BB1A2C1C7002` / `ISO-IEC-24372`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Process management framework for big data analytics — 2022

- Source: `EXT-F257F1512247` / `ISO-IEC-24668`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guidance for quality evaluation of artificial intelligence (AI) systems — 2024

- Source: `EXT-4D6C88D8B249` / `ISO-IEC-25058`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality model for AI systems — 2023

- Source: `EXT-87623C21D66F` / `ISO-IEC-25059`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Governance of IT — Governance implications of the use of artificial intelligence by organizations — 2022

- Source: `EXT-6B4C6A420D7A` / `ISO-IEC-38507`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Management system — 2023

- Source: `EXT-206D448EB65F` / `ISO-IEC-42001`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — AI system impact assessment — 2025

- Source: `EXT-28BBBB608503` / `ISO-IEC-42005`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Requirements for bodies providing audit and certification of artificial intelligence management systems — 2025

- Source: `EXT-797A4F77B73C` / `ISO-IEC-42006`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Overview of differentiated benchmarking of AI system quality characteristics — 2026

- Source: `EXT-AC009E599200` / `ISO-IEC-42106`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance on machine learning model training efficiency optimization — 2026

- Source: `EXT-C522C31221D1` / `ISO-IEC-42112`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Testing of AI — Part 2: Overview of testing AI systems — 2025

- Source: `EXT-F7D25C093670` / `ISO-IEC-42119-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Assessment of machine learning classification performance — 2022

- Source: `EXT-2532B488F72F` / `ISO-IEC-4213`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 1: Overview, terminology, and examples — 2024

- Source: `EXT-0F495407BD10` / `ISO-IEC-5259-1`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 2: Data quality measures — 2024

- Source: `EXT-1AB8EF4CB11D` / `ISO-IEC-5259-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 3: Data quality management requirements and guidelines — 2024

- Source: `EXT-29BC8BF61EDF` / `ISO-IEC-5259-3`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 4: Data quality process framework — 2024

- Source: `EXT-F307DA6ADE51` / `ISO-IEC-5259-4`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 5: Data quality governance framework — 2025

- Source: `EXT-1B5FBFF7B099` / `ISO-IEC-5259-5`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 6: Visualization framework for data quality — 2026

- Source: `EXT-2CC8B310E58F` / `ISO-IEC-5259-6`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — AI system life cycle processes — 2023

- Source: `EXT-DEE88CAA4636` / `ISO-IEC-5338`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance for AI applications — 2024

- Source: `EXT-E5A4A33AC525` / `ISO-IEC-5339`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Reference architecture of knowledge engineering — 2024

- Source: `EXT-30D0802D15C6` / `ISO-IEC-5392`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Functional safety and AI systems — 2024

- Source: `EXT-EF206ED96999` / `ISO-IEC-5469`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Objectives and approaches for explainability and interpretability of machine learning (ML) models and artificial intelligence (AI) systems — 2025

- Source: `EXT-5435F9552ED1` / `ISO-IEC-6254`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Data life cycle framework — 2023

- Source: `EXT-EFFD34D14635` / `ISO-IEC-8183`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `high-value-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Controllability of automated artificial intelligence systems — 2024

- Source: `EXT-6DDF68F621A8` / `ISO-IEC-8200`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0
- Review priority: `critical-governance-source`
- Next action: Provide lawful licensed primary-text access for bounded requirement review; do not upload or commit the copyrighted standard text.

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Systems and software engineering — Vocabulary — 2017

- Source: `EXT-D5DA0E7978BE` / `ISO-IEC-IEEE-24765`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Monitor Edition 3 development and use the published 2017 identity for terminology cross-reference until superseded.

No requirement records are asserted. Registered as systems/software vocabulary authority. No definitions beyond lawfully available publisher material are reconstructed.

## Artificial Intelligence Risk Management Framework (AI RMF 1.0) — 1.0

- Source: `EXT-6442C7954667` / `NIST-AI-100-1`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 71
- Review priority: `critical-governance-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-0055BCF6AB20FDB7` | GOVERN 5.1 | Processes collect, consider, prioritize and integrate feedback from those outside the team that developed or deployed the AI system. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0CCFB0AAE692E441` | MAP 1.5 | Organizational risk tolerances are determined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1031AEE45BE9ED28` | MANAGE 1.3 | Responses for high-priority risks are developed, planned and documented, including mitigation, transfer, avoidance or acceptance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1408DB88C2C42508` | MANAGE 3.2 | Pre-trained models used in the AI system are monitored as part of maintenance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-233EE01AB85DB0F0` | MEASURE 1.2 | The appropriateness of metrics and effectiveness of controls are regularly assessed and updated, including errors and impacts on affected communities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-23A856D39E460557` | GOVERN 4.2 | Organizational teams document and communicate AI-system risks and potential impacts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-28293B6A2D5AB761` | MEASURE 2.7 | AI-system security and resilience are evaluated and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2831EFFBC5F8A321` | MAP 2.2 | Knowledge limits and how outputs may be used, including human oversight, are determined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2905C0AA3C11D9DA` | MANAGE 4.2 | Measurable continual improvement is integrated into system updates and stakeholder engagement. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2E1D2C63187C14E8` | MEASURE 2.5 | The validity and reliability of the AI system are demonstrated, and limits on generalization are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-366214C3FB6CBD7B` | MAP 4.1 | Risks from components and third-party technologies, including legal and intellectual-property risks, are mapped and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3B4A77A84EB7C45E` | MAP 3.4 | Processes for operator proficiency are defined, assessed and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3EDCD15F1ECEC4F8` | GOVERN 6.1 | Policies and procedures address AI risks associated with third-party entities, including intellectual-property and other risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3F4CDACD587C4311` | GOVERN 1.3 | Processes, procedures and practices determine the needed level of AI risk-management activity from organizational risk tolerance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4406FC00176EF608` | GOVERN 2.2 | Personnel and partners receive AI risk-management training so they can perform their duties and responsibilities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4A55F4250F95C5E2` | MAP 2.3 | Scientific-integrity and TEVV considerations, including data and validation assumptions, are identified and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4AF3E931C4EF1B2B` | GOVERN 1.4 | The risk-management process and its outcomes are transparent, with policies and controls established to document outcomes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4C464EF3523BD496` | GOVERN 1.6 | Mechanisms inventory AI systems and the resources used to manage their risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4E032FB784E538EB` | MEASURE 2.6 | The AI system is regularly evaluated for safety, including fail-safe behavior, residual risk and alignment with defined risk tolerance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-50CD57A13CF16C6A` | GOVERN 5.2 | Practices regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-559DBB147B1BEB9E` | MANAGE 4.1 | Post-deployment monitoring covers user input, appeal and override, decommissioning, incident response and change management. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-57F4CC2CD806240B` | MAP 3.1 | Potential benefits of the AI system are examined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-59FCEFAD3AD44D68` | MAP 1.6 | System requirements are elicited from relevant AI actors, and socio-technical design considerations are incorporated. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5F9DA0D0B6F0F41C` | GOVERN 4.3 | Organizational practices enable testing, incident identification and information sharing. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6165C5E752264175` | MEASURE 2.10 | Privacy risk is examined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6320A5C27CD2562D` | GOVERN 1.1 | Legal and regulatory requirements involving AI are understood, managed and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-65093F71FE0B832B` | MEASURE 4.2 | Measurement results are informed by input from relevant experts and AI actors and are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-66474C86C4005DDB` | MEASURE 2.2 | Evaluations involving human subjects comply with applicable requirements and use representative populations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-669D0C512E2B7AD7` | MAP 3.3 | The application scope is specified and documented based on capability, context and classification. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6795C6C5F4D8116C` | MEASURE 4.1 | Measurement is connected to deployment context and informed by domain experts and relevant users, and this context is documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6870C9F25BE482D7` | MAP 1.1 | The intended purpose, users, uses, benefits, impacts, laws, norms, assumptions, settings and performance expectations of the AI system are understood and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6BA40F94C5B1FD66` | MAP 2.1 | The specific tasks and methods used to implement them are defined. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7737200A1740E641` | GOVERN 2.3 | Executive leadership takes responsibility for decisions about AI-system risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-78837C1C44B0806B` | MANAGE 3.1 | Third-party AI risks and benefits are regularly monitored, controls are applied, and results are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-78B9D34F9D38B5A0` | GOVERN 4.1 | Organizational policies and practices foster critical thinking and a safety-first mindset in AI design, development, deployment and use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7DAF9BF16EE1EED4` | MEASURE 1.3 | Independent assessors or internal experts not serving on frontline development, and relevant users or affected communities, are consulted in assessment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-809CCACFF672EFB9` | MEASURE 2.4 | The functionality and behavior of the AI system and its components are monitored in production. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-83FD9ACC984101BE` | MEASURE 3.2 | Risks that are difficult to measure or lack reliable metrics are considered for tracking. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-84093779C78FF4A1` | MAP 1.4 | The business value or context of business use is defined or re-evaluated. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-84A8B3C0B190FB83` | GOVERN 1.5 | Ongoing monitoring and periodic review of the risk-management process and outcomes are planned and organizational roles and frequency are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-86DF9273C10549E9` | MEASURE 2.8 | Risks related to transparency and accountability are examined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8F72332AE922D993` | GOVERN 1.2 | Trustworthy-AI characteristics are integrated into organizational policies, processes, procedures and practices. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-93500A33F8E3899D` | MAP 3.2 | Potential costs, including non-monetary costs, are examined and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-99448CA617B69B2F` | MAP 1.3 | The organization mission and relevant goals for the AI technology are understood and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9E0A814431B2A294` | MEASURE 2.11 | Fairness and bias are evaluated and results are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A337E13222520E08` | MEASURE 2.3 | Performance and assurance criteria are measured in conditions similar to deployment and the results are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A50A6EADB3460E08` | MEASURE 3.3 | Feedback and appeal processes are incorporated into evaluation metrics. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A9486CE3E82FB660` | MANAGE 1.4 | Residual risk is documented and communicated to downstream acquirers and end users. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-ACFFD259B09631E2` | MAP 4.2 | Internal controls for components, including third-party components, are identified and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B03C89BC46097F92` | MAP 5.1 | Likelihood and magnitude of impacts are identified and documented using available evidence, incident reports and external feedback. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B14E3C4577F28D7C` | MEASURE 4.3 | Improvements or declines in performance and trustworthiness are identified and documented from consultation and field data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B7315893B8D75680` | MEASURE 2.1 | TEVV test sets, metrics and tools are identified and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B7D251A503308E4A` | MANAGE 2.1 | Resources required to manage AI risks and viable non-AI alternatives are considered. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B850AD995985724B` | GOVERN 3.2 | Policies and procedures define and differentiate roles and responsibilities for human-AI configurations and oversight. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C32F213CA1F4C104` | MEASURE 1.1 | Appropriate methods and metrics are selected for mapped risks according to significance, and risks that cannot be measured are documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C428E36496435AB3` | GOVERN 3.1 | Decision-making about AI risk throughout the lifecycle is informed by diverse teams. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C5251D534A12E316` | MAP 1.2 | Interdisciplinary and diverse perspectives are used to define and document the deployment context, including participation by potentially affected communities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C5281C9522B1CD2C` | MEASURE 2.12 | Environmental and sustainability impacts are assessed and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C9091A8E13995001` | MEASURE 3.1 | Existing, unanticipated and emergent risks are regularly identified and tracked using deployed-system performance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CBC134B07CB4DB0A` | MAP 3.5 | Processes for human oversight are defined, assessed and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CF1C89C280B6A699` | GOVERN 6.2 | Contingency processes are in place for failures or incidents in third-party data or systems assessed as high risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D22AB2D961D08A9E` | MANAGE 2.3 | Procedures are established to respond to and recover from previously unknown risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DBF5850ADAEC83E4` | GOVERN 2.1 | Roles and responsibilities for AI risk management are documented and communicated across the organization and to relevant third parties. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E0E174AA5FE5AD2B` | GOVERN 1.7 | Processes and procedures are in place for safe decommissioning and phasing out of AI systems and for safely discontinuing their use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E2BA27213272AF72` | MANAGE 1.1 | Whether to proceed with development or deployment is decided from mapped and measured risks and intended purposes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E5BEDF611AC4A683` | MANAGE 2.2 | Mechanisms are in place to sustain the value of deployed AI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E64704F05DE5759B` | MAP 5.2 | Practices and personnel are in place to engage relevant stakeholders and integrate feedback about impacts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E90F2DD631617DDA` | MEASURE 2.13 | The effectiveness of TEVV metrics and processes is evaluated and documented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F1F3A6472A08E764` | MANAGE 2.4 | Mechanisms and responsibilities are established to supersede, disengage or deactivate systems whose performance or outcomes are inconsistent with intended use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F6E7F0CA4F94EB71` | MEASURE 2.9 | The model is explained and validated, explanations are documented, and output context is interpreted. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F95F33125D83F81A` | MANAGE 1.2 | Risk treatment is prioritized by impact, likelihood and available resources. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations — E2025

- Source: `EXT-2B2B0FF7FBE9` / `NIST-AI-100-2`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 22
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-1541AC9EA2E10037` | NISTAML.039 | Connected-resource compromise exploits agent access to tools, data or external systems. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-23C60DF093A7B3F8` | NISTAML.011 | Model-poisoning attacks manipulate model development or updating to impair availability. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-26301842DF1DD2A3` | NISTAML.04 | Misuse attacks exploit AI capabilities or access paths for harmful purposes. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-28E605A9C2985F50` | NISTAML.015 | Indirect prompt injection introduces adversarial instructions through content processed by a generative AI system or agent. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2BF9417F3DD54AA8` | NISTAML.03 | Privacy attacks seek information about models, training data, users or system interactions. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3A1A5B90FEE08268` | NISTAML.036 | Interaction-leakage attacks expose information from other users or sessions. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-41E7637A45C43336` | 3.6 | Interpret adversarial-ML benchmark results in light of threat-model, dataset, metric and transfer limitations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5790AF1D5ACDCB5E` | 2.2–2.4 | Select mitigations against an explicit threat model and evaluate their effectiveness and limitations against relevant attacks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7221439C481E489C` | NISTAML.033 | Membership-inference attacks determine whether a record was part of training. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-77530B4AE0E1AB25` | NISTAML.027 | Misaligned-output attacks cause generative AI outputs to depart from intended policy or behavior. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7FE2C18999AD3ABD` | NISTAML.031 | Model-extraction attacks infer or reproduce model functionality or parameters. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8A8D35EEB8EA4C07` | NISTAML.01 | Availability attacks seek to degrade or deny an AI system's intended service. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-94B4FCDF35C6B93C` | NISTAML.013 | Data-poisoning attacks manipulate training data to impair model availability. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9C6B060133CD70BC` | NISTAML.023 | Backdoor attacks create trigger-dependent model behavior while preserving ordinary performance. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9E851C70DBD0CD3C` | NISTAML.032 | Data-reconstruction attacks infer sensitive training records or attributes. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A75EEF53E6194000` | NISTAML.018 | Direct prompt injection uses adversarial user instructions to subvert intended generative AI behavior. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AAB5D96CAE086B43` | NISTAML.02 | Integrity attacks seek to cause incorrect or adversary-chosen AI behavior. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-ACACB69DF2E32D48` | 4.1 | Reassess adversarial-ML risk and mitigation performance as attacks, capabilities, dependencies and deployment conditions evolve. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B6313F89C917B7D1` | NISTAML.022 | Evasion attacks modify inference-time inputs to induce incorrect behavior. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D61164D66185C874` | 2.1 | Characterize adversarial-ML threats by lifecycle stage, attacker goal, capability, knowledge and attack modality. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EDC917FC5835B76B` | NISTAML.05 | Supply-chain attacks compromise AI components, dependencies, models or data before operational use. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F4970B12A04A1797` | 3.2–3.5 | Assess generative AI and agent systems for supply-chain, direct-prompt, indirect-prompt and connected-resource attacks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## The Language of Trustworthy AI: An In-Depth Glossary of Terms — 2023

- Source: `EXT-13A4EA0D8BCF` / `NIST-AI-100-3`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency — 2024

- Source: `EXT-5BC2AAEAF1D3` / `NIST-AI-100-4`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 18
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-04A1120E5709BBB5` | 7 | Combine complementary provenance, detection, labeling and governance measures rather than relying on one transparency technique. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2B5F2D7EAF522E73` | 3.1.2.3–3.1.2.6 | Assess metadata and provenance implementations for privacy leakage, security risk, scalability and loss during distribution. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-40BA686203D7F020` | 5.6–5.6.1 | Red-team and test safeguards against foreseeable attempts to generate prohibited or harmful intimate content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4706A6387311D532` | 4.1.1 | Test watermark techniques using context-relevant robustness, quality, detection and false-positive measures. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4F010C47F9C62E1B` | 3.1.1 | Select watermarking approaches according to content modality, threat model, robustness, detectability and deployment constraints. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5205096A50B3E6B6` | 4.1.1 | Evaluate watermark insertion and detection for quality impact, false results, removal and evasion under relevant transformations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5215ABF2B855226E` | 4.2–4.2.2 | Evaluate synthetic-content detectors on representative data, transformations and adversarial conditions and report uncertainty. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5252A04AB1238C2C` | 4.1.2 and 4.2.1 | Test metadata and provenance systems for authenticity, integrity, interoperability and persistence across content workflows. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5806C7417A46D033` | 4.3 | Document generalization, benchmark, base-rate and adversarial limitations when reporting transparency-technique performance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5AF6358B9779F629` | 3.1.2 | Record content provenance and modification information in interoperable metadata where the use context supports it. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-688F22BFEB762E26` | 3.3–3.3.2 | Design labels and disclosures so intended users can notice and understand synthetic or manipulated content status. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7D1019CFC5DFDF0B` | 5.3–5.4 | Use output filtering, hashing or matching and response processes where appropriate to reduce harmful synthetic-content distribution. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8742BC3940F998B7` | 5.1–5.2 | Use proportionate training-data and input controls to reduce creation of unlawful or abusive intimate and child sexual content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-907032FF4258B625` | 4.2.3 | Evaluate human-assisted detection with realistic users and decision contexts, including automation and confirmation effects. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9B6AFA4DA5E9398D` | 3.3–3.3.2 | Test content labels for accessibility, comprehension, persistence and effects on user judgment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A25093A6B507D46B` | 3.2.2 | Evaluate detection separately for relevant image, audio, video and text modalities rather than assuming cross-modal performance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CB71ADED4F8D02F3` | 3.1.2.2–3.1.2.3 | Use cryptographic authentication or trust infrastructure where provenance claims require tamper evidence and issuer verification. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F4FFD18134680288` | 3.2–3.2.2 | Use synthetic-content detection only with documented operating conditions, uncertainty and known failure modes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## A Plan for Global Engagement on AI Standards — 2025

- Source: `EXT-5316F21598A2` / `NIST-AI-100-5`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile — 2024

- Source: `EXT-DE4FDB52698E` / `NIST-AI-600-1`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 223
- Review priority: `critical-governance-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-0071C7B7B5E64BFA` | MP-3.4-004 | Delineate human proficiency tests from tests of GAI capabilities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-007D7BAAE8A25C9D` | MS-2.11-004 | Review, document, and measure sources of bias in GAI training and TEVV data: Differences in distributions of outcomes across and within groups, including intersecting groups; Completeness, representativeness, and balance of data sources; demographic group and subgroup coverage in GAI system training data; Forms of latent systemic bias in images, text, audio, embeddings, or other complex or unstructured data; Input data features that may serve as proxies for demographic group membership (i.e., image metadata, language dialect) or otherwise give rise to emergent bias within GAI systems; The extent to which the digital divide may negatively impact representativeness in GAI system training and TEVV data; Filtering of hate speech or content in GAI system training data; Prevalence of GAI-generated data in GAI system training data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-00DA3079EECB0471` | GV-1.4-002 | Establish transparent acceptable use policies for GAI that address illegal use or applications of GAI. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-00DBB52A605BD459` | MG-4.3-002 | Establish and maintain policies and procedures to record and track GAI system reported errors, near-misses, and negative impacts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-01E6F8BA99F66F9A` | MS-1.1-001 | Employ methods to trace the origin and modifications of digital content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-036F8B9FBBE33437` | MS-3.3-005 | Record and integrate structured feedback about content provenance from operators, users, and potentially impacted communities through the use of methods such as user research studies, focus groups, or community forums. Actively seek feedback on generated content quality and potential biases. Assess the general awareness among end users and impacted communities about the availability of these feedback channels. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0462CF2D5AD49C00` | GV-2.1-002 | Establish procedures to engage teams for GAI system incident response with diverse composition and responsibilities based on the particular incident type. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-046F58D53F005855` | MP-2.2-001 | Identify and document how the system relies on upstream data sources, including for content provenance, and if it serves as an upstream dependency for other systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-063412CD674E27B3` | MS-3.3-003 | Evaluate potential biases and stereotypes that could emerge from the AI- generated content using appropriate methodologies including computational testing methods as well as evaluating structured feedback input. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-06E16BB05C087E2A` | 2.9 | Organizations should consider and manage information security risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-06F34AA14804357F` | MP-4.1-010 | Conduct appropriate diligence on training data use to assess intellectual property, and privacy, risks, including to examine whether use of proprietary or sensitive training data is consistent with applicable laws. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-08529233C1C32115` | MP-3.4-005 | Implement systems to continually monitor and track the outcomes of human-GAI configurations for future refinement and improvements. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-09A4C260900D6A83` | MS-4.2-001 | Conduct adversarial testing at a regular cadence to map and measure GAI risks, including tests to address attempts to deceive or manipulate the application of provenance techniques or other misuses. Identify vulnerabilities and understand potential misuse scenarios and unintended outputs. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0DDD2A292BDC718E` | MG-4.1-002 | Establish, maintain, and evaluate effectiveness of organizational processes and procedures for post-deployment monitoring of GAI systems, particularly for potential confabulation, CBRN, or cyber risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0E404DEFECDA5FE0` | MG-2.2-009 | Consider opportunities to responsibly use synthetic data and other privacy enhancing techniques in GAI development, where appropriate and applicable, match the statistical properties of real-world data without disclosing personally identifiable information or contributing to homogenization. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0EBBD55B64245F03` | MP-4.1-004 | Document training data curation policies, to the extent possible and according to applicable laws and policies. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0F1B5ACCB8F63149` | MS-2.3-003 | Share results of pre-deployment testing with relevant GAI Actors, such as those with system release approval authority. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-11A6E84345FB4301` | MS-2.7-007 | Perform AI red-teaming to assess resilience against: Abuse to facilitate attacks on other systems (e.g., malicious code generation, enhanced phishing content), GAI attacks (e.g., prompt injection), ML attacks (e.g., adversarial examples/prompts, data poisoning, membership inference, model extraction, sponge examples). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1238A77ABB7C1DBF` | GV-6.2-004 | Establish policies and procedures for continuous monitoring of third-party GAI systems in deployment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1269988FF25A00FD` | MS-2.2-002 | Document how content provenance data is tracked and how that data interacts with privacy and security. Consider: Anonymizing data to protect the privacy of human subjects; Leveraging privacy output filters; Removing any personally identifiable information (PII) to prevent potential harm or misuse. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-13D4FA7278DD6B03` | MG-4.1-005 | Share transparency reports with internal and external stakeholders that detail steps taken to update the GAI system to enhance transparency and accountability. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-13DCE314CA72D587` | MS-2.11-002 | Conduct fairness assessments to measure systemic bias. Measure GAI system performance across demographic groups and subgroups, addressing both quality of service and any allocation of services and resources. Quantify harms using: field testing with sub-group populations to determine likelihood of exposure to generated content exhibiting harmful bias, AI red-teaming with counterfactual and low-context (e.g., “leader,” “bad guys”) prompts. For ML pipelines or business processes with categorical or numeric outcomes that rely on GAI, apply general fairness metrics (e.g., demographic parity, equalized odds, equal opportunity, statistical hypothesis tests), to the pipeline or business outcome where appropriate; Custom, context-specific metrics developed in collaboration with domain experts and affected communities; Measurements of the prevalence of denigration in generated content in deployment (e.g., sub- sampling a fraction of traffic and manually annotating denigrating content). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-14DBCAFCA690FAE0` | MS-2.5-002 | Document the extent to which human domain knowledge is employed to improve GAI system performance, via, e.g., RLHF, fine-tuning, retrieval- augmented generation, content moderation, business rules. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-180F19CEA5BD8D2E` | GV-1.2-002 | Establish policies to evaluate risk-relevant capabilities of GAI and robustness of safety measures, both prior to deployment and on an ongoing basis, through internal and external evaluations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1AAAF9F63C4B77A8` | MS-2.7-006 | Measure the rate at which recommendations from security checks and incidents are implemented. Assess how quickly the AI system can adapt and improve based on lessons learned from security incidents and feedback. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1D630F746A8D243A` | MG-3.2-007 | Leverage feedback and recommendations from organizational boards or committees related to the deployment of GAI applications and content provenance when using third-party pre-trained models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-210E95EA572DB5FC` | GV-6.1-005 | Implement a use-cased based supplier risk assessment framework to evaluate and monitor third-party entities’ performance and adherence to content provenance standards and technologies to detect anomalies and unauthorized changes; services acquisition and value chain risk management; and legal compliance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-21811CDCF5CFCF9A` | MS-2.2-001 | Assess and manage statistical biases related to GAI content provenance through techniques such as re-sampling, re-weighting, or adversarial training. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2367510B0758D596` | GV-1.3-007 | Devise a plan to halt development or deployment of a GAI system that poses unacceptable negative risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-25BDC1BF6A486355` | MS-1.3-002 | Engage in internal and external evaluations, GAI red-teaming, impact assessments, or other structured human feedback exercises in consultation with representative AI Actors with expertise and familiarity in the context of use, and/or who are representative of the populations associated with the context of use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-268AA27544C123C1` | GV-1.6-002 | Define any inventory exemptions in organizational policies for GAI systems embedded into application software. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-28C1554DC9F841C8` | MS-2.12-004 | Verify effectiveness of carbon capture or offset programs for GAI training and applications, and address green-washing concerns. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-298C72769F142961` | MS-2.3-004 | Utilize a purpose-built testing environment such as NIST Dioptra to empirically evaluate GAI trustworthy characteristics. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-29F2758EC0A4B5BA` | MP-4.1-002 | Implement processes for responding to potential intellectual property infringement claims or other rights. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2A54090E587B783E` | MG-4.1-001 | Collaborate with external researchers, industry experts, and community representatives to maintain awareness of emerging best practices and technologies in measuring and managing identified risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2AED24B068EA924F` | 2.5 | Organizations should consider and manage environmental impact risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2ED4784F3B80B23A` | MS-2.9-001 | Apply and document ML explanation results such as: Analysis of embeddings, Counterfactual prompts, Gradient-based attributions, Model compression/surrogate models, Occlusion/term reduction. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3209D60A503A7B46` | MS-2.13-001 | Create measurement error models for pre-deployment metrics to demonstrate construct validity for each metric (i.e., does the metric effectively operationalize the desired concept): Measure or estimate, and document, biases or statistical variance in applied metrics or structured human feedback processes; Leverage domain expertise when modeling complex societal constructs such as hateful content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3287D5CADAAE2D71` | GV-1.7-002 | Consider the following factors when decommissioning GAI systems: Data retention requirements; Data security, e.g., containment, protocols, Data leakage after decommissioning; Dependencies between upstream, downstream, or other data, internet of things (IOT) or AI systems; Use of open-source data or models; Users’ emotional entanglement with GAI functions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-33E14A4AB3DA955D` | MG-3.2-009 | Use organizational risk tolerance to evaluate acceptable risks and performance metrics and decommission or retrain pre-trained models that perform outside of defined limits. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-34693080CB950006` | MG-2.4-004 | Establish and regularly review specific criteria that warrants the deactivation of GAI systems in accordance with set risk tolerances and appetites. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3540672B99F987E9` | MS-2.11-005 | Assess the proportion of synthetic to non-synthetic training data and verify training data is not overly homogenous or GAI-produced to mitigate concerns of model collapse. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-369CFBB6A2C52E62` | MS-2.6-004 | Review GAI system outputs for validity and safety: Review generated code to assess risks that may arise from unreliable downstream decision-making. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3828BBEDC0A05B64` | GV-2.1-004 | When systems may raise national security risks, involve national security professionals in mapping, measuring, and managing those risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-383E0AAF594EFF28` | MP-4.1-001 | Conduct periodic monitoring of AI-generated content for privacy risks; address any possible instances of PII or sensitive data exposure. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-38A00DC3A54A582F` | MG-4.3-001 | Conduct after-action assessments for GAI system incidents to verify incident response and recovery processes are followed and effective, including to follow procedures for communicating incidents to relevant AI Actors and where applicable, relevant legal and regulatory bodies. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3A44C5AC26375724` | MP-4.1-007 | Re-evaluate models that were fine-tuned or enhanced on top of third-party models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3CF6BE0334DEC565` | MP-4.1-005 | Establish policies for collection, retention, and minimum quality of data, in consideration of the following risks: Disclosure of inappropriate CBRN information; Use of Illegal or dangerous content; Offensive cyber capabilities; Training data imbalances that could give rise to harmful biases; Leak of personally identifiable information, including facial likenesses of individuals. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3DE000C1C7E37071` | MG-2.2-003 | Evaluate feedback loops between GAI system content provenance and human reviewers, and update where needed. Implement real-time monitoring systems to affirm that content provenance protocols remain effective. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3F827BC2D6FB855C` | MG-4.2-002 | Practice and follow incident response plans for addressing the generation of inappropriate or harmful content and adapt processes based on findings to prevent future occurrences. Conduct post-mortem analyses of incidents with relevant AI Actors, to understand the root causes and implement preventive measures. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4277B23509413079` | GV-4.3-002 | Establish organizational practices to identify the minimum set of criteria necessary for GAI system incident reporting such as: System ID (auto-generated most likely), Title, Reporter, System/Source, Data Reported, Date of Incident, Description, Impact(s), Stakeholder(s) Impacted. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-42E00BFFFB610685` | GV-4.1-001 | Establish policies and procedures that address continual improvement processes for GAI risk measurement. Address general risks associated with a lack of explainability and transparency in GAI systems by using ample documentation and techniques such as: application of gradient-based attributions, occlusion/term reduction, counterfactual prompts and prompt engineering, and analysis of embeddings; Assess and update risk measurement approaches at regular cadences. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4694042F7F82C217` | MP-2.1-002 | Institute test and evaluation for data and content flows within the GAI system, including but not limited to, original data sources, data transformations, and decision-making criteria. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-48302F17BB06AC19` | GV-3.2-001 | Policies are in place to bolster oversight of GAI systems with independent evaluations or assessments of GAI models or systems where the type and robustness of evaluations are proportional to the identified risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-488D7F15493E9E51` | MP-4.1-009 | Leverage approaches to detect the presence of PII or sensitive data in generated output text, image, video, or audio. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4935F57986DF9317` | GV-1.6-003 | In addition to general model, governance, and risk information, consider the following items in GAI system inventory entries: Data provenance information (e.g., source, signatures, versioning, watermarks); Known issues reported from internal bug tracking or external information sharing resources (e.g., AI incident database, AVID, CVE, NVD, or OECD AI incident monitor); Human oversight roles and responsibilities; Special rights and considerations for intellectual property, licensed works, or personal, privileged, proprietary or sensitive data; Underlying foundation models, versions of underlying models, and access modes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4972B48203D4A92C` | MS-2.7-005 | Measure reliability of content authentication methods, such as watermarking, cryptographic signatures, digital fingerprints, as well as access controls, conformity assessment, and model integrity verification, which can help support the effective implementation of content provenance techniques. Evaluate the rate of false positives and false negatives in content provenance, as well as true positives and true negatives for verification. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4AD2B2BD47C828CA` | GV-4.2-001 | Establish terms of use and terms of service for GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4D5BF8BEA4A413B0` | MP-2.3-001 | Assess the accuracy, quality, reliability, and authenticity of GAI output by comparing it to a set of known ground truth data and by using a variety of evaluation methods (e.g., human oversight and automated evaluation, proven cryptographic techniques, review of content inputs). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4EA7BF52BD7CD5AF` | MS-2.5-005 | Verify GAI system training data and TEVV data provenance, and that fine-tuning or retrieval-augmented generation data is grounded. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4FA48F69E0D84D76` | MS-2.10-001 | Conduct AI red-teaming to assess issues such as: Outputting of training data samples, and subsequent reverse engineering, model extraction, and membership inference risks; Revealing biometric, confidential, copyrighted, licensed, patented, personal, proprietary, sensitive, or trade-marked information; Tracking or revealing location information of users or members of training datasets. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5140CF5A20CB317F` | GV-1.4-001 | Establish policies and mechanisms to prevent GAI systems from generating CSAM, NCII or content that violates the law. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-536D462F85BB9343` | GV-6.1-010 | Update GAI acceptable use policies to address proprietary and open-source GAI technologies and data, and contractors, consultants, and other third-party personnel. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-54B9E0FC6A070C66` | MS-1.1-003 | Disaggregate evaluation metrics by demographic factors to identify any discrepancies in how content provenance mechanisms work across diverse populations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5583A7FFDB46461C` | GV-4.2-002 | Include relevant AI Actors in the GAI system risk identification process. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-56049F64C61351DF` | MS-2.9-002 | Document GAI model details including: Proposed use and organizational value; Assumptions and limitations, Data collection methodologies; Data provenance; Data quality; Model architecture (e.g., convolutional neural network, transformers, etc.); Optimization objectives; Training algorithms; RLHF approaches; Fine-tuning or retrieval-augmented generation approaches; Evaluation data; Ethical considerations; Legal and regulatory requirements. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-56BC13476987B6CB` | MG-3.1-003 | Re-assess model risks after fine-tuning or retrieval-augmented generation implementation and for any third-party GAI models deployed for applications and/or use cases that were not evaluated in initial testing. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-572E8F9A8CA166B2` | MP-1.1-002 | Determine and document the expected and acceptable GAI system context of use in collaboration with socio-cultural and other domain experts, by assessing: Assumptions and limitations; Direct value to the organization; Intended operational environment and observed usage patterns; Potential positive and negative impacts to individuals, public safety, groups, communities, organizations, democratic institutions, and the physical environment; Social norms and expectations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-58494ED07F4C476F` | MS-2.5-004 | Track and document instances of anthropomorphization (e.g., human images, mentions of human feelings, cyborg imagery or motifs) in GAI system interfaces. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5A3DEC25113D0F81` | 2.6 | Organizations should consider and manage harmful bias and homogenization risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5B304AE81EB3EDC8` | GV-2.1-003 | Establish processes to verify the AI Actors conducting GAI incident response tasks demonstrate and maintain the appropriate skills and training. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5C707CDA63126398` | 2.2 | Organizations should consider and manage confabulation risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5CEC8E71C7C1373F` | MG-1.3-001 | Document trade-offs, decision processes, and relevant measurement and feedback results for risks that do not surpass organizational risk tolerance, for example, in the context of model release: Consider different approaches for model release, for example, leveraging a staged release approach. Consider release approaches in the context of the model and its projected use cases. Mitigate, transfer, or avoid risks that surpass organizational risk tolerances. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-606A32149AB41BA4` | MP-1.2-001 | Establish and empower interdisciplinary teams that reflect a wide range of capabilities, competencies, demographic groups, domain expertise, educational backgrounds, lived experiences, professions, and skills across the enterprise to inform and conduct risk measurement and management functions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-615FABA4B3307072` | GV-3.2-004 | Establish policies for user feedback mechanisms for GAI systems which include thorough instructions and any mechanisms for recourse. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-62AE400907DF1A92` | GV-2.1-001 | Establish organizational roles, policies, and procedures for communicating GAI incidents and performance to AI Actors and downstream stakeholders (including those potentially impacted), via community or official resources (e.g., AI incident database, AVID, CVE, NVD, or OECD AI incident monitor). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-62C3A65371CB047E` | MP-5.2-002 | Plan regular engagements with AI Actors responsible for inputs to GAI systems, including third-party data and algorithms, to review and evaluate unanticipated impacts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-64FBCCEB7C2C0062` | MS-2.6-002 | Assess existence or levels of harmful bias, intellectual property infringement, data privacy violations, obscenity, extremism, violence, or CBRN information in system training data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-674CA139AB6C6D81` | MP-4.1-006 | Implement policies and practices defining how third-party intellectual property and training data will be used, stored, and protected. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-684FDF9FC22A253D` | MG-3.2-003 | Document sources and types of training data and their origins, potential biases present in the data related to the GAI application and its content provenance, architecture, training process of the pre-trained model including information on hyperparameters, training duration, and any fine-tuning or retrieval-augmented generation processes applied. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-696F45AAD993A382` | MS-2.7-003 | Conduct user surveys to gather user satisfaction with the AI-generated content and user perceptions of content authenticity. Analyze user feedback to identify concerns and/or current literacy levels related to content provenance and understanding of labels on content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6AFEBCF01A44E6D4` | MP-1.1-001 | When identifying intended purposes, consider factors such as internal vs. external use, narrow vs. broad application scope, fine-tuning, and varieties of data sources (e.g., grounding, retrieval-augmented generation). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6B1B54A8429D4ED9` | MG-4.1-003 | Evaluate the use of sentiment analysis to gauge user sentiment regarding GAI content performance and impact, and work in collaboration with AI Actors experienced in user research and experience. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6B9145EBE7C888AB` | GV-6.2-002 | Document incidents involving third-party GAI data and systems, including open- data and open-source software. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6C9AF8BEB0C00E2C` | MG-3.1-001 | Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine tuning, retrieval-augmented generation) to third-party GAI resources: Apply organizational risk tolerance to the utilization of third-party datasets and other GAI resources; Apply organizational risk tolerances to fine-tuned third-party models; Apply organizational risk tolerance to existing third-party models adapted to a new domain; Reassess risk measurements after fine-tuning third- party GAI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6DE6265FC3C5F9F4` | GV-3.2-003 | Define acceptable use policies for GAI interfaces, modalities, and human-AI configurations (i.e., for chatbots and decision-making tasks), including criteria for the kinds of queries GAI applications should refuse to respond to. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6F77B758D19B752C` | GV-6.2-003 | Establish incident response plans for third-party GAI technologies: Align incident response plans with impacts enumerated in MAP 5.1; Communicate third-party GAI incident response plans to all relevant AI Actors; Define ownership of GAI incident response functions; Rehearse third-party GAI incident response plans at a regular cadence; Improve incident response plans based on retrospective learning; Review incident response plans for alignment with relevant breach reporting, data protection, data privacy, or other laws. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6FB32C15D60F5ECA` | MS-3.3-002 | Conduct studies to understand how end users perceive and interact with GAI content and accompanying content provenance within context of use. Assess whether the content aligns with their expectations and how they may act upon the information presented. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-70FB934007D26B99` | 2.10 | Organizations should consider and manage intellectual-property risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-716C928BDF5DF833` | MP-5.1-005 | Conduct adversarial role-playing exercises, GAI red-teaming, or chaos testing to identify anomalous or unforeseen failure modes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7261F76F8FFB54D5` | MP-3.4-003 | Develop certification programs that test proficiency in managing GAI risks and interpreting content provenance, relevant to specific industry and context. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-74C33A4ABB401F25` | MG-2.2-008 | Use structured feedback mechanisms to solicit and capture user input about AI- generated content to detect subtle shifts in quality or alignment with community and societal values. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-74D6C4FCCF9C0073` | GV-4.1-002 | Establish policies, procedures, and processes detailing risk measurement in context of use with standardized measurement protocols and structured public feedback exercises such as AI red-teaming or independent external evaluations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-765A0B510FD11D10` | GV-6.1-007 | Inventory all third-party entities with access to organizational content and establish approved GAI technology and service provider lists. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-76DDFFBEF09F35AE` | MS-2.2-003 | Provide human subjects with options to withdraw participation or revoke their consent for present or future use of their data in GAI applications. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-77A042FF5317261F` | MS-1.3-001 | Define relevant groups of interest (e.g., demographic groups, subject matter experts, experience with GAI technology) within the context of use as part of plans for gathering structured public feedback. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7BC3EDE0976A4F5B` | MG-3.2-002 | Document how pre-trained models have been adapted (e.g., fine-tuned, or retrieval-augmented generation) for the specific generative task, including any data augmentations, parameter adjustments, or other modifications. Access to un-tuned (baseline) models supports debugging the relative influence of the pre- trained weights compared to the fine-tuned model weights or other system updates. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7BD2ED7939CB6DC1` | MP-1.1-004 | Identify and document foreseeable illegal uses or applications of the GAI system that surpass organizational risk tolerances. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7E4ACD956465C7ED` | MG-2.3-001 | Develop and update GAI system incident response and recovery plans and procedures to address the following: Review and maintenance of policies and procedures to account for newly encountered uses; Review and maintenance of policies and procedures for detection of unanticipated uses; Verify response and recovery plans account for the GAI system value chain; Verify response and recovery plans are updated for and include necessary details to communicate with downstream GAI system Actors: Points-of-Contact (POC), Contact information, notification format. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7E7500D622B64943` | MS-2.11-001 | Apply use-case appropriate benchmarks (e.g., Bias Benchmark Questions, Real Hateful or Harmful Prompts, Winogender Schemas15) to quantify systemic bias, stereotyping, denigration, and hateful content in GAI system outputs; Document assumptions and limitations of benchmarks, including any actual or possible training/test data cross contamination, relative to in-context deployment environment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7F3E164A4F5EB23A` | GV-6.1-009 | Update and integrate due diligence processes for GAI acquisition and procurement vendor assessments to include intellectual property, data privacy, security, and other risks. For example, update processes to: Address solutions that may rely on embedded GAI technologies; Address ongoing monitoring, assessments, and alerting, dynamic risk assessments, and real-time reporting tools for monitoring third-party GAI risks; Consider policy adjustments across GAI modeling libraries, tools and APIs, fine-tuned models, and embedded tools; Assess GAI vendors, open-source or proprietary GAI tools, or GAI service providers against incident or vulnerability databases. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8096823CE7FE00C1` | 2.1 | Organizations should consider and manage cbrn information or capability risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-80C57DEB7282DF1E` | MG-3.1-004 | Take reasonable measures to review training data for CBRN information, and intellectual property, and where appropriate, remove it. Implement reasonable measures to prevent, flag, or take other action in response to outputs that reproduce particular training data (e.g., plagiarized, trademarked, patented, licensed content or trade secret material). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8258B27E2AC3FF88` | MS-2.6-007 | Regularly evaluate GAI system vulnerabilities to possible circumvention of safety measures. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-83BAE39527689A7E` | MG-3.1-005 | Review various transparency artifacts (e.g., system cards and model cards) for third-party models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-83F1289B08A86286` | MP-3.4-002 | Adapt existing training programs to include modules on digital content transparency. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-84B3A244B2A9DDD1` | GV-1.3-006 | Reevaluate organizational risk tolerances to account for unacceptable negative risk (such as where significant negative impacts are imminent, severe harms are actually occurring, or large-scale risks could occur); and broad GAI negative risks, including: Immature safety or risk cultures related to AI and GAI design, development and deployment, public information integrity risks, including impacts on democratic processes, unknown long-term performance characteristics of GAI. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-851AE07A44265BD5` | MG-4.2-003 | Use visualizations or other methods to represent GAI model behavior to ease non-technical stakeholders understanding of GAI system functionality. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-854F9A3540B65874` | MG-2.2-005 | Engage in due diligence to analyze GAI output for harmful content, potential misinformation, and CBRN-related or NCII content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-85C870BE6D952FCD` | MG-4.1-004 | Implement active learning techniques to identify instances where the model fails or produces unexpected outputs. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-864ED9C1B56018A2` | GV-1.3-002 | Establish minimum thresholds for performance or assurance criteria and review as part of deployment approval (“go/”no-go”) policies, procedures, and processes, with reviewed processes and approval thresholds reflecting measurement of GAI capabilities and risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-86938D79BBFF174E` | 2.8 | Organizations should consider and manage information integrity risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-86F046206D444BB6` | MS-1.1-005 | Evaluate novel methods and technologies for the measurement of GAI-related risks including in content provenance, offensive cyber, and CBRN, while maintaining the models’ ability to produce valid, reliable, and factually accurate outputs. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8943536BE57E678B` | MP-4.1-008 | Re-evaluate risks when adapting GAI models to new domains. Additionally, establish warning systems to determine if a GAI system is being used in a new domain where previous assumptions (relating to context of use or mapped risks such as security, and safety) may no longer hold. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-89B98AB292B7E33B` | GV-1.3-003 | Establish a test plan and response policy, before developing highly capable models, to periodically evaluate whether the model may misuse CBRN information or capabilities and/or offensive cyber capabilities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-89EDF6573EDE84D8` | MS-1.1-009 | Track and document risks or opportunities related to all GAI risks that cannot be measured quantitatively, including explanations as to why some risks cannot be measured (e.g., due to technological limitations, resource constraints, or trustworthy considerations). Include unmeasured risks in marginal risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8A44D58E6FF52335` | MG-2.2-007 | Use real-time auditing tools where they can be demonstrated to aid in the tracking and validation of the lineage and authenticity of AI-generated data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8DB924F00FF93DE0` | GV-5.1-001 | Allocate time and resources for outreach, feedback, and recourse processes in GAI system development. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8EEDB00F4772840D` | MS-2.3-001 | Consider baseline model performance on suites of benchmarks when selecting a model for fine tuning or enhancement with retrieval-augmented generation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-90054EB2D7C9E642` | MS-2.11-003 | Identify the classes of individuals, groups, or environmental ecosystems which might be impacted by GAI systems through direct engagement with potentially impacted communities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-908ABADB093F2F2C` | MS-1.1-008 | Define use cases, contexts of use, capabilities, and negative impacts where structured human feedback exercises, e.g., GAI red-teaming, would be most beneficial for GAI risk measurement and management based on the context of use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-91094725498A0EB3` | GV-4.1-003 | Establish policies, procedures, and processes for oversight functions (e.g., senior leadership, legal, compliance, including internal evaluation) across the GAI lifecycle, from problem formulation and supply chains to system decommission. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-927AE192C96414EB` | MP-5.1-001 | Apply TEVV practices for content provenance (e.g., probing a system's synthetic data generation capabilities for potential misuse or vulnerabilities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-927D85F1E4DFFECA` | MS-2.8-004 | Verify adequacy of GAI system user instructions through user testing. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-93D5D1B7680A2AB4` | MP-2.3-005 | Implement plans for GAI systems to undergo regular adversarial testing to identify vulnerabilities and potential manipulation or misuse. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9703EE1395CAB64C` | GV-6.2-006 | Establish policies and procedures to test and manage risks related to rollover and fallback technologies for GAI systems, acknowledging that rollover and fallback may include manual processing. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9B27E48269591982` | MG-4.3-003 | Report GAI incidents in compliance with legal and regulatory requirements (e.g., HIPAA breach reporting, e.g., OCR (2023) or NHTSA (2022) autonomous vehicle crash reporting requirements. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9BC8DF07010711B0` | MG-4.1-007 | Verify that AI Actors responsible for monitoring reported issues can effectively evaluate GAI system performance including the application of content provenance data tracking techniques, and promptly escalate issues for response. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9BD072E617AF8331` | MG-2.4-003 | Establish and maintain procedures for the remediation of issues which trigger incident response processes for the use of a GAI system, and provide stakeholders timelines associated with the remediation plan. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9CA366D7788DC293` | MG-4.1-006 | Track dataset modifications for provenance by monitoring data deletions, rectification requests, and other changes that may impact the verifiability of content origins. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9DAFE45AFCA29F3D` | MS-4.2-003 | Implement interpretability and explainability methods to evaluate GAI system decisions and verify alignment with intended purpose. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9EF87DE0D76CBB3A` | MS-4.2-002 | Evaluate GAI system performance in real-world scenarios to observe its behavior in practical environments and reveal issues that might not surface in controlled and optimized testing environments. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9F158625F2045C3C` | MS-2.2-004 | Use techniques such as anonymization, differential privacy or other privacy- enhancing technologies to minimize the risks associated with linking AI-generated content back to individual human subjects. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9F55746EE3358DFD` | MS-4.2-005 | Verify and document the incorporation of results of structured public feedback exercises into design, implementation, deployment approval (“go”/“no-go” decisions), monitoring, and decommission decisions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A01C8E47A44EAA97` | GV-2.1-005 | Create mechanisms to provide protections for whistleblowers who report, based on reasonable belief, when the organization violates relevant laws or poses a specific and empirically well-substantiated negative risk to public safety (or has already caused harm). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A16DC6E31B9A49FE` | MS-2.7-008 | Verify fine-tuning does not compromise safety and security controls. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A34D8DAA4DF314B7` | GV-1.6-001 | Enumerate organizational GAI systems for incorporation into AI system inventory and adjust AI system inventory requirements to account for GAI risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A67E54A283E42597` | MS-2.10-002 | Engage directly with end-users and other stakeholders to understand their expectations and concerns regarding content provenance. Use this feedback to guide the design of provenance data-tracking techniques. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A7617DF7CEE4B279` | MP-3.4-001 | Evaluate whether GAI operators and end-users can accurately understand content lineage and origin. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A7EB43EEB7323C9A` | GV-4.3-003 | Verify information sharing and feedback mechanisms among individuals and organizations regarding any negative impact from GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A8125E37154B2148` | MG-3.2-006 | Implement real-time monitoring processes for analyzing generated content performance and trustworthiness characteristics related to content provenance to identify deviations from the desired standards and trigger alerts for human intervention. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A9F2F3F26E7B96A5` | GV-1.2-001 | Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications to advance digital content transparency, while balancing the proprietary nature of training approaches. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AC5BA019342AFFE9` | MP-1.1-003 | Document risk measurement plans to address identified risks. Plans may include, as applicable: Individual and group cognitive biases (e.g., confirmation bias, funding bias, groupthink) for AI Actors involved in the design, implementation, and use of GAI systems; Known past GAI system incidents and failure modes; In-context use and foreseeable misuse, abuse, and off-label use; Over reliance on quantitative metrics and methodologies without sufficient awareness of their limitations in the context(s) of use; Standard measurement and structured human feedback approaches; Anticipated human-AI configurations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-ACA14CA613A93958` | MP-2.3-002 | Review and document accuracy, representativeness, relevance, suitability of data used at different stages of AI life cycle. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AEC26B463E03432B` | MS-3.3-001 | Conduct impact assessments on how AI-generated content might affect different social, economic, and cultural groups. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B0737DEC2D388821` | GV-1.5-002 | Establish organizational policies and procedures for after action reviews of GAI system incident response and incident disclosures, to identify gaps; Update incident response and incident disclosure processes as required. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B17C7FA063C735BA` | MS-2.7-009 | Regularly assess and verify that security measures remain effective and have not been compromised. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B23D9C6AE388A8F7` | MS-2.12-001 | Assess safety to physical environments when deploying GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B29559FC29A2F429` | GV-6.1-003 | Develop and validate approaches for measuring the success of content provenance management efforts with third parties (e.g., incidents detected and response times). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B3E8C7F978A586AA` | GV-1.3-004 | Obtain input from stakeholder communities to identify unacceptable use, in accordance with activities in the AI RMF Map function. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B4BD4062B6721359` | MG-2.4-002 | Establish and maintain procedures for escalating GAI system incidents to the organizational risk management authority when specific criteria for deactivation or disengagement is met for a particular context of use or for the GAI system as a whole. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B609E1D64C88DC3D` | MS-2.8-003 | Use digital content transparency solutions to enable the documentation of each instance where content is generated, modified, or shared to provide a tamper- proof history of the content, promote transparency, and enable traceability. Robust version control systems can also be applied to track changes across the AI lifecycle over time. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B64FBB286666D69E` | MS-2.8-001 | Compile statistics on actual policy violations, take-down requests, and intellectual property infringement for organizational GAI systems: Analyze transparency reports across demographic groups, languages groups. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B68DB97C4A2C9A17` | MP-2.2-002 | Observe and analyze how the GAI system interacts with external networks, and identify any potential for negative externalities, particularly where content provenance might be compromised. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B6AF98230B7456AB` | GV-1.5-001 | Define organizational responsibilities for periodic review of content provenance and incident monitoring for GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B8B620458C5DCE2E` | MP-1.2-002 | Verify that data or benchmarks used in risk measurement, and users, participants, or subjects involved in structured GAI public feedback exercises are representative of diverse in-context user populations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B8E19E18B2FA9FD4` | MS-2.6-006 | Verify that systems properly handle queries that may give rise to inappropriate, malicious, or illegal usage, including facilitating manipulation, extortion, targeted impersonation, cyber-attacks, and weapons creation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B9090309549ED8DB` | GV-6.1-006 | Include clauses in contracts which allow an organization to evaluate third-party GAI processes and standards. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA19F5BDCF5FA962` | GV-6.2-007 | Review vendor contracts and avoid arbitrary or capricious termination of critical GAI technologies or vendor services and non-standard terms that may amplify or defer liability in unexpected ways and/or contribute to unauthorized data collection by vendors or third-parties (e.g., secondary data use). Consider: Clear assignment of liability and responsibility for incidents, GAI system changes over time (e.g., fine-tuning, drift, decay); Request: Notification and disclosure for serious incidents arising from third-party data and systems; Service Level Agreements (SLAs) in vendor contracts that address incident response, response times, and availability of critical support. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA4F78E88534950B` | MP-4.1-003 | Connect new GAI policies, procedures, and processes to existing model, data, software development, and IT governance and to legal, compliance, and risk management activities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA7B79BDE2DC32FB` | MG-3.2-008 | Use human moderation systems where appropriate to review generated content in accordance with human-AI configuration policies established in the Govern function, aligned with socio-cultural norms in the context of use, and for settings where AI models are demonstrated to perform poorly. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA9AE36C1F29F759` | MS-2.12-002 | Document anticipated environmental impacts of model development, maintenance, and deployment in product design decisions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BBB49CF0F16A256A` | MS-1.1-007 | Evaluate the quality and integrity of data used in training and the provenance of AI-generated content, for example by employing techniques like chaos engineering and seeking stakeholder feedback. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BDF3F13759396E4A` | GV-6.2-005 | Establish policies and procedures that address GAI data redundancy, including model weights and other system artifacts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BE66DB41E5A2C7BC` | MG-2.2-006 | Use feedback from internal and external AI Actors, users, individuals, and communities, to assess impact of AI-generated content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C0AC3C0606C3923B` | MS-2.6-005 | Verify that GAI system architecture can monitor outputs and performance, and handle, recover from, and repair errors when security anomalies, threats and impacts are detected. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C279311D3D16ED0B` | MS-3.2-001 | Establish processes for identifying emergent GAI system risks including consulting with external AI Actors. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C2BC00BBE44778CC` | GV-1.7-001 | Protocols are put in place to ensure GAI systems are able to be deactivated when necessary. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C37E171E0EA8E0CA` | MS-3.3-004 | Provide input for training materials about the capabilities and limitations of GAI systems related to digital content transparency for AI Actors, other professionals, and the public about the societal impacts of AI and the role of diverse and inclusive content generation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C395266FE4929644` | MS-4.2-004 | Monitor and document instances where human operators or other systems override the GAI's decisions. Evaluate these cases to understand if the overrides are linked to issues related to content provenance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C478F33DE187ACEF` | MP-2.3-003 | Deploy and document fact-checking techniques to verify the accuracy and veracity of information generated by GAI systems, especially when the information comes from multiple (or unknown) sources. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C4DF8712D46FE05A` | GV-6.1-004 | Draft and maintain well-defined contracts and service level agreements (SLAs) that specify content ownership, usage rights, quality standards, security requirements, and content provenance expectations for GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C5A156431EF49FE9` | MS-2.3-002 | Evaluate claims of model capabilities using empirically validated methods. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C697D6A95F2D6304` | MP-5.1-004 | Prioritize GAI structured public feedback processes based on risk assessment estimates. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C71423F30878A927` | MS-2.10-003 | Verify deduplication of GAI training data samples, particularly regarding synthetic data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C7FC8A47ABA51057` | MG-3.1-002 | Test GAI system value chain risks (e.g., data poisoning, malware, other software and hardware vulnerabilities; labor practices; data privacy and localization compliance; geopolitical alignment). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C8B3C0EBA815ABB8` | GV-6.1-001 | Categorize different types of GAI content with associated third-party rights (e.g., copyright, intellectual property, data privacy). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C9B7A3D72C4A6511` | 2.12 | Organizations should consider and manage value-chain and component-integration risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CDA0F3004234AF9C` | MP-3.4-006 | Involve the end-users, practitioners, and operators in GAI system in prototyping and testing activities. Make sure these tests cover various scenarios, such as crisis situations or ethically sensitive contexts. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CF5DB455BE3D3AF6` | MS-2.6-001 | Assess adverse impacts, including health and wellbeing impacts for value chain or other AI Actors that are exposed to sexually explicit, offensive, or violent information during GAI training and maintenance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CFCC2FDEE2081401` | MS-1.1-002 | Integrate tools designed to analyze content provenance and detect data anomalies, verify the authenticity of digital signatures, and identify patterns associated with misinformation or manipulation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D01548E276DC81C7` | MG-2.4-001 | Establish and maintain communication plans to inform AI stakeholders as part of the deactivation or disengagement process of a specific GAI system (including for open-source models) or context of use, including reasons, workarounds, user access removal, alternative processes, contact information, etc. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D038CD035E17057F` | GV-3.2-002 | Consider adjustment of organizational roles and components across lifecycle stages of large or complex GAI systems, including: Test and evaluation, validation, and red-teaming of GAI systems; GAI content moderation; GAI system development and engineering; Increased accessibility of GAI tools, interfaces, and systems, Incident response and containment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D1187E79B3203CC5` | MS-2.6-003 | Re-evaluate safety features of fine-tuned models when the negative risk exceeds organizational risk tolerance. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D2A0B7E633A64339` | GV-6.1-008 | Maintain records of changes to content made by third parties to promote content provenance, including sources, timestamps, metadata. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D4469002D71F9657` | GV-3.2-005 | Engage in threat modeling to anticipate potential risks from GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D5151FB53FBC54DA` | MP-2.3-004 | Develop and implement testing techniques to identify GAI produced content (e.g., synthetic media) that might be indistinguishable from human-generated content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D66AAB4CFF48F764` | GV-6.2-001 | Document GAI risks associated with system value chain to identify over-reliance on third-party data and to identify fallbacks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D80867BEF745997B` | 2.3 | Organizations should consider and manage dangerous, violent or hateful content risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D8155D3EA5985233` | MG-1.3-002 | Monitor the robustness and effectiveness of risk controls and mitigation plans (e.g., via red-teaming, field testing, participatory engagements, performance assessments, user feedback mechanisms). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D81F0D37C92F766F` | GV-1.3-001 | Consider the following factors when updating or defining risk tiers for GAI: Abuses and impacts to information integrity; Dependencies between GAI and other IT or data systems; Harm to fundamental rights or public safety; Presentation of obscene, objectionable, offensive, discriminatory, invalid or untruthful output; Psychological impacts to humans (e.g., anthropomorphization, algorithmic aversion, emotional entanglement); Possibility for malicious use; Whether the system introduces significant new security vulnerabilities; Anticipated system impact on some groups compared to others; Unreliable decision making capabilities, validity, adaptability, and variability of GAI system performance over time. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D959C017CEAD5C18` | MS-1.3-003 | Verify those conducting structured human feedback exercises are not directly involved in system development tasks for the same GAI model. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DB2FAD119E628F53` | MS-1.1-004 | Develop a suite of metrics to evaluate structured public feedback exercises informed by representative AI Actors. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DB3C9856CB7B8688` | MS-2.12-003 | Measure or estimate environmental impacts (e.g., energy and water consumption) for training, fine tuning, and deploying models: Verify tradeoffs between resources used at inference time versus additional resources required at training time. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DD000192A7B46F4C` | GV-6.1-002 | Conduct joint educational activities and events in collaboration with third parties to promote best practices for managing GAI risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DD9D5135DB4D8AD6` | GV-5.1-002 | Document interactions with GAI systems to users prior to interactive activities, particularly in contexts involving more significant risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E053087D054D8EFB` | MG-2.2-001 | Compare GAI system outputs against pre-defined organization risk tolerance, guidelines, and principles, and review and test AI-generated content against these guidelines. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E085EA29F51DB6E0` | GV-1.1-001 | Align GAI development and use with applicable laws and regulations, including those related to data privacy, copyright and intellectual property law. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E2A434A5196B91E5` | MS-2.7-004 | Identify metrics that reflect the effectiveness of security measures, such as data provenance, the number of unauthorized access attempts, inference, bypass, extraction, penetrations, or provenance verification. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E4B604764848C260` | 2.4 | Organizations should consider and manage data privacy risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E4E1EC08C1C7EC06` | MS-2.8-002 | Document the instructions given to data annotators or AI red-teamers. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E6335E9335C8D367` | MS-1.1-006 | Implement continuous monitoring of GAI system impacts to identify whether GAI outputs are equitable across various sub-populations. Seek active and direct feedback from affected communities via structured feedback mechanisms or red- teaming to monitor and improve outputs. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E7933CF663C511DC` | MG-2.2-002 | Document training data sources to trace the origin and provenance of AI- generated content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E7CB2246EA0311DC` | MS-2.7-002 | Benchmark GAI system security and resilience related to content provenance against industry standards and best practices. Compare GAI system security features and content provenance methods against industry state-of-the-art. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EAAE2B5FD25DB4E5` | MS-2.5-003 | Review and verify sources and citations in GAI system outputs during pre- deployment risk measurement and ongoing monitoring activities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EC385DE4E4591978` | MS-2.5-006 | Regularly review security and safety guardrails, especially if the GAI system is being operated in novel circumstances. This includes reviewing reasons why the GAI system was initially assessed as being safe to deploy. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EF645D5C9EA0B2A8` | GV-1.3-005 | Maintain an updated hierarchy of identified and expected GAI risks connected to contexts of GAI model advancement and use, potentially including specialized risk levels for GAI systems that address issues such as model collapse and algorithmic monoculture. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F01026ADF985292A` | MP-2.1-001 | Establish known assumptions and practices for determining data origin and content lineage, for documentation and evaluation purposes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F0686AA575DC32B9` | MG-3.2-005 | Implement content filters to prevent the generation of inappropriate, harmful, false, illegal, or violent content related to the GAI application, including for CSAM and NCII. These filters can be rule-based or leverage additional machine learning models to flag problematic inputs and outputs. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F125677581330AD1` | MS-2.5-001 | Avoid extrapolating GAI system performance or capabilities from narrow, non- systematic, and anecdotal assessments. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F2B55F09F4F963DF` | MP-5.1-006 | Profile threats and negative impacts arising from GAI systems interacting with, manipulating, or generating content, and outlining known and potential vulnerabilities and the likelihood of their occurrence. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F3FEEAC2C9EB9DE5` | MG-3.2-004 | Evaluate user reported problematic content and integrate feedback into system updates. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F591D6427C6EE07D` | 2.7 | Organizations should consider and manage human-ai configuration risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F5EE679C987F9F08` | MG-3.2-001 | Apply explainable AI (XAI) techniques (e.g., analysis of embeddings, model compression/distillation, gradient-based attributions, occlusion/term reduction, counterfactual prompts, word clouds) as part of ongoing continuous improvement processes to mitigate risks related to unexplainable GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F729973AF9047C51` | MP-5.2-001 | Determine context-based measures to identify if new impacts are present due to the GAI system, including regular engagements with downstream AI Actors to identify and quantify new contexts of unanticipated impacts of GAI systems. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F7D150323DFB3260` | MS-2.7-001 | Apply established security measures to: Assess likelihood and magnitude of vulnerabilities and threats such as backdoors, compromised dependencies, data breaches, eavesdropping, man-in-the-middle attacks, reverse engineering, autonomous agents, model theft or exposure of model weights, AI inference, bypass, extraction, and other baseline security concerns. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F9388EF21726D66D` | GV-1.5-003 | Maintain a document retention policy to keep history for test, evaluation, validation, and verification (TEVV), and digital content transparency methods for GAI. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F94F75725E36303F` | MP-5.1-003 | Consider disclosing use of GAI to end users in relevant contexts, while considering the objective of disclosure, the context of use, the likelihood and magnitude of the risk posed, the audience of the disclosure, as well as the frequency of the disclosures. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F9725830955AD58D` | GV-4.2-003 | Verify that downstream GAI system impacts (such as the use of third-party plugins) are included in the impact documentation process. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FC0A098DD233BE97` | MG-2.2-004 | Evaluate GAI content and data for representational biases and employ techniques such as re-sampling, re-ranking, or adversarial training to mitigate biases in the generated content. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FCDE17D3F0843F55` | MP-5.1-002 | Identify potential content provenance harms of GAI, such as misinformation or disinformation, deepfakes, including NCII, or tampered content. Enumerate and rank risks based on their likelihood and potential impact, and determine how well provenance solutions address specific risks and/or harms. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FF415140E4149BA7` | 2.11 | Organizations should consider and manage obscene, degrading or abusive content risk when identifying generative-AI risks. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FFB12B6CD54559B3` | MG-4.2-001 | Conduct regular monitoring of GAI systems and publish reports detailing the performance, feedback received, and improvements made. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## The NIST Cybersecurity Framework (CSF) 2.0 — 2.0

- Source: `EXT-09F549521716` / `NIST-CSF-2-0`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Towards a Standard for Identifying and Managing Bias in Artificial Intelligence — 2022

- Source: `EXT-1BE47AB84994` / `NIST-SP-1270`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 14
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-3030E7F375A5181E` | 3.2.2 | Use disaggregated and context-relevant performance analysis to identify differential impacts that aggregate metrics may conceal. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-493C6B32A0178925` | 3.4.1 | Assign governance responsibility for identifying, assessing, documenting and mitigating AI bias. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6075BA538E7FF7DC` | 2.1 | Treat AI bias as a socio-technical phenomenon with systemic, computational and human contributors. | `definitional` / `definition` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-781D501071BA131E` | 3.4.1 | Feed monitoring, incident and stakeholder information back into dataset, design and risk-treatment decisions. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-82F46ABCA356F77A` | 3.2.2 | Document evaluation assumptions, uncertainty, limitations and residual bias risks. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A41EFC122FFC8011` | 3.4.1 | Provide multidisciplinary competence, authority and resources for bias management across the organization. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A8838A7EEACC7806` | 3.1.2 | Document dataset purpose, origin, composition, collection context, limitations and fitness for the intended AI use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-AAA2E27CDF760D9C` | 3.3.2 | Include diverse and affected perspectives when identifying and evaluating potential bias and harm. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CDC73A6E25F4BCF4` | 3.1.2 | Evaluate representation and measurement choices for systematic bias and for effects on relevant groups. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D0558126D6950EAE` | 3.1.2 | Maintain dataset provenance and record transformations, exclusions and quality interventions that can affect bias. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DECFB6D5BF3EC91C` | 3.3.2 and 3.4.1 | Assess bias periodically throughout the AI lifecycle and after contextual, data, model or use changes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-EB3AEF59D55DBA7E` | 3.2.2 | Design test, evaluation, verification and validation around the intended context, affected populations and foreseeable uses. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F24D556CF1E1E201` | 3.3.2 | Evaluate human and organizational factors, including decision context, cognitive bias, automation effects and user interaction. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FD2E9DE61D27AD9A` | 3.4.1 | Preserve decisions, assumptions, data choices, evaluation results and mitigation rationales relevant to bias. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities — 1.1

- Source: `EXT-4AADC9C1B06B` / `NIST-SP-800-218`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `low-immediate-priority`
- Next action: No further requirement extraction is planned in the current scope.

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in the current scope.

## Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile — 2024

- Source: `EXT-65F7658B8B04` / `NIST-SP-800-218A`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 75
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-02C541A232BF2703` | PO.4.1 C1 | Consider requiring review and approval from a human-in-the-loop for software security checks beyond risk-based thresholds. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-062FC787CD093123` | PS.1.3 R2 | Continuously monitor the confidentiality (for closed models only) and integrity of model weights and configuration parameters. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-07C7C84BBFDBF29D` | PW.3.3 R1 | Use a process and corresponding controls to test the adversarial samples and put appropriate guardrails on training and testing use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0988FA858904EFBE` | PW.4.4 R2 | Scan and thoroughly test acquired AI models and their components for vulnerabilities and malicious content before use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0D340334BF013176` | PO.1.2 R1 | Organizational policies should support all current requirements specific to AI model development security for organization- developed software. These requirements should include the areas of AI model development, AI model operations, and data science. Requirements may come from many sources, including laws, regulations, contracts, and standards. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-0D78B02BC5016604` | PO.2.3 R1 | Leadership should commit to secure development practices involving AI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-10B3D390AFD40855` | PO.1.2 C1 | Consider reusing or expanding the organization’s existing data classification policy and processes. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1208F73BEDD1A54C` | PW.8.1 C1 | Consider automating tests within a development pipeline as part of regression testing where possible. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1582CA6E2303931A` | PS.3.1 R2 | Include documentation of the justification for AI model selection in the retained information. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-17EAA0F1C831BF9E` | PW.4.1 C1 | Consider using an existing AI model instead of creating a new one. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-181B1CF26577727E` | RV.1.2 R3 | Conduct periodic audits of AI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1AAD882F2F58BA56` | PS.1.1 R2 | Follow the principle of least privilege to minimize direct access to AI models and model elements regardless of where they are stored or executed. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1FD5D213F5EC16AD` | RV.1.1 R1 | Log, monitor, and analyze all inputs and outputs for AI models to detect possible security and performance issues (see PO.5.3). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-1FFE1710582A469A` | PW.7.1 C1 | Consider performing scans of AI model code in addition to testing the AI models. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-294E0E8C1D68BD77` | PO.2.2 R1 | Role-based training should include understanding cybersecurity vulnerabilities and threats to AI models and their possible mitigations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-2C72ECCDA9855444` | PS.1.3 R1 | Keep model weights and configuration parameters separate from training, testing, fine-tuning, and aligning data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-31E72E1FDDD4CF72` | PO.5.3 R2 | Continuous monitoring and analysis tools should generate alerts when detected activity involving an AI model passes a risk threshold or otherwise merits additional investigation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-32EDD8730ECA61B4` | PS.3.1 R3 | Include documentation of the entire training process, such as data preprocessing and model architecture. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-3649F5275F37050F` | PS.1.1 C1 | Consider preventing all human access to model weights. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-39150F7A7B155230` | PO.2.1 R1 | Include AI model development security in SDLC-related roles and responsibilities throughout the SDLC. The roles and responsibilities should include, but are not limited to, AI model development, AI model operations, and data science. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-39CCD223E7E6E94E` | PW.3.1 C1 | Consider using a human-in-the-loop to examine data, such as with exploratory data analysis techniques [18]. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-44728F18D1E35E07` | PO.3.1 R1 | Plan to develop and implement automated toolchains that secure AI model development and reduce human effort, especially at the scale often used by AI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4602E72E8865E71B` | RV.2.2 C1 | Consider being prepared to stop using an AI model at any time and to continue operations through other means until the AI model’s risks are sufficiently addressed. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-492F5D4D785587A4` | PS.2.1 R1 | Generate and provide cryptographic hashes or digital signatures for an AI model and its components, artifacts, and documentation. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-494632407D193E4D` | PW.1.1 R1 | Incorporate relevant AI model-specific vulnerability and threat types in risk modeling. Examples of these vulnerability and threat types include poisoning of training data, malicious code or other unwanted content in inputs and outputs, denial-of-service conditions arising from adversarial prompts, supply chain attacks, unauthorized information disclosure, theft of AI model weights, and misconfiguration of data pipelines. [3] | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4BF2F07B38F6A3BF` | PW.1.1 C2 | During risk modeling, consider checking that the AI model is not in a critical path to make significant security decisions without a human in the loop. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4BFBC2F7E52FF380` | PO.5.1 R2 | Only store sensitive data used during AI model development, including production data, within organization-approved environments and locations within those environments. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-4C5BA9975E3764A4` | PS.1.1 C2 | Consider requiring all AI model development to be performed within organization-approved environments only. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5066A5A4DBF87A3A` | PS.2.1 R2 | Provide digital signatures for AI model changes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-597D56E05968BAA7` | PS.3.2 R2 | Track AI models that were trained on sensitive data (e.g., payment card data, protected health information, other types of personally identifiable information), and determine if access to the models should be restricted to individuals who already have access to the sensitive data used for training. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-628879075A758488` | PO.5.1 R5 | Follow recommended practices for securely configuring each environment. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-68BF22F92CE4DCEC` | RV.1.1 R3 | Monitor vulnerability and incident databases for information on AI-related concerns, including the machine learning frameworks and libraries used to build AI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6A9AD1F2984920A0` | PS.1.1 R3 | Store reward models separately from AI models and data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6B80B50BE91D5573` | PS.3.2 R1 | Track the provenance of an AI model and its components and derivatives, including the training libraries, frameworks, and pipelines used to build the model. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-6B9E14B5B45904B7` | RV.1.2 R1 | Scan and test AI models frequently to identify previously undetected vulnerabilities. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-71004359D5B9D58A` | PS.3.2 C1 | Consider disclosing the provenance of the training, testing, fine-tuning, and aligning data used for an AI model. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7589C3449A7B10B8` | PW.6.1 C1 | Consider using secure model serialization mechanisms that reduce or eliminate vectors for the introduction of malicious content. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-76096A37AC863D59` | PW.1.1 C1 | Consider periodic risk modeling updates for future AI model versions and derivatives after AI model release. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-764F26DFDDBA41A8` | RV.1.3 R1 | Include AI model vulnerabilities in organization vulnerability disclosure and remediation policies. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-7BC7AF5BCF61B7CD` | PW.4.4 R1 | Verify the integrity, provenance, and security of an existing AI model or any other acquired AI components — including training, testing, fine-tuning, and aligning datasets; reward models; adaptation layers; and configuration parameters — before using them. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8046B52C0921325D` | PW.8.2 R2 | Retest AI models when they are retrained or new data sources are added. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8939C47D17D9E257` | PO.1.1 R2 | Identify and select appropriate AI model architectures and training techniques in accordance with recommended practices for cybersecurity, privacy, and reproducibility. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-894D279CA1D8457F` | PO.3.2 R2 | Verify the security of toolchains at a frequency commensurate with risk. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8AC58CD2F1ADA711` | PO.5.3 R1 | Perform continuous security monitoring for all development environment components that host an AI model or related resources (e.g., model APIs, weights, configuration parameters, training datasets). | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-8D7263393D6E5932` | PS.1.3 R4 | Specify and implement additional risk- proportionate cybersecurity practices around model weights, such as encryption, cryptographic hashes, digital signatures, multi- party authorization, and air-gapped environments. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-924ED328626DF5C8` | PW.3.1 R2 | Select and apply appropriate methods for analyzing and altering the training, testing, fine- tuning, and aligning data for an AI model. Examples of methods include anomaly detection, bias detection, data cleaning, data curation, data filtering, data sanitization, fact- checking, and noise reduction. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-928C34207D6EFA0B` | PO.1.3 R1 | Include AI model development security in the requirements being communicated for third-party software components. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9353C915CE8F67EE` | PW.7.2 R1 | Scan all AI models for malware, vulnerabilities, backdoors, and other security issues in accordance with the organization’s code review and analysis policies or guidelines. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-93E013A31BC2CC14` | PO.5.1 C1 | Consider separating execution environments from each other to the extent feasible, such as through isolation, segmentation, containment, access via APIs, or other means. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9CC64C814C52636E` | RV.1.1 R2 | Make the users of AI models aware of mechanisms for reporting potential security and performance issues. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9DAE98CAB159CB64` | PW.5.1 R2 | Code the handling of inputs (including prompts and user data) and outputs carefully. All inputs and outputs should be logged, analyzed, and validated within the context of the AI model, and those with issues should be sanitized or dropped. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-9E3160DE09900294` | PW.6.2 C1 | Consider capturing compiler, interpreter, and build tool versions and features as part of the provenance tracking. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A53A705D7A9D5C9E` | PS.3.1 R1 | Perform versioning and tracking for infrastructure tools (e.g., pre-processing, transforms, collection) that support dataset creation and model training. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A5406F78EE55411E` | PO.1.1 R1 | Include AI model development in the security requirements for software development infrastructure and processes. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-A73521C6AD3B42C8` | PS.1.3 R3 | Follow the principle of least privilege to restrict access to AI model weights, configuration parameters, and services during development. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B11185F5DA301697` | PS.1.2 R1 | Continuously monitor the confidentiality (for non-public data only) and integrity of training, testing, fine-tuning, and aligning data. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B266BCD5C9F680AB` | RV.2.2 R2 | Establish and implement criteria and processes for when to stop using an AI model and when to roll back to a previous version and its components. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B578E815E6D995B4` | PW.5.1 R3 | Encode inputs and outputs to prevent the execution of unauthorized code. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B7B9E81F72EFE1BB` | PS.1.1 R4 | Permit indirect access only to model weights. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B7D6A74ED85415CF` | PS.1.1 R1 | Secure code storage should include AI models, model weights, pipelines, reward models, and any other AI model elements that need their confidentiality, integrity, and/or availability protected. These elements do not all have to be stored in the same place or through the same type of mechanism. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-B9C60CD256E74C4D` | PO.5.1 R6 | Continuously monitor each environment for plaintext secrets. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-BA53FBDD86C14120` | PO.4.1 R1 | Implement guardrails and other controls throughout the AI development life cycle, extending beyond the traditional SDLC. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-C57531922F9D57CB` | PO.5.1 R1 | Monitor, track, and limit resource usage and rates for AI model users during model development. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CE1F3C371F2F1B0D` | PO.3.2 R1 | Execute the plan to develop and implement automated toolchains that secure AI model development and reduce human effort, especially at the scale often used by AI models. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CEC01E574F80243C` | PW.5.1 R1 | Expand secure coding practices to include AI technology-specific considerations. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CF93CC5F8D6CDAC1` | RV.2.2 R1 | Risk responses for AI models should consider the time and expenses that may be associated with rebuilding them. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-CFC9864F6289630A` | PW.7.1 R1 | Code review and analysis policies or guidelines should include code for AI models and other related components. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-D55D51197E68F59C` | PS.1.2 C1 | Consider securely storing training, testing, fine-tuning, and aligning data for future use and reference if feasible. | `informative-guidance` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DD6BADB31C8F8EC8` | RV.1.2 R2 | Rely mainly on automation for ongoing scanning and testing, and involve a human-in- the-loop as needed. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DF4F0FE19B0C47A0` | PO.5.1 R4 | Continuously monitor training-related activity in pipelines and model modifications in the model registry. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E3C6492CBED8B3F0` | RV.1.3 R2 | Make users of AI models aware of their inherent limitations and how to report any cybersecurity problems that they encounter. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-E8F231F17B5CF5C2` | PO.5.1 R3 | Protect all training pipelines, model registries, and other components within the environments according to the principle of least privilege. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F0581975A66AED74` | PW.3.1 R1 | Verify the provenance (when known) and integrity of training, testing, fine-tuning, and aligning data before use. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-F1C5571B851A123F` | PW.8.2 R1 | Test all AI models for vulnerabilities in accordance with the organization’s code testing policies or guidelines. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-FC3775D684CD5F14` | PW.8.1 R1 | Include AI models in code testing policies and guidelines. Several forms of code testing can be used for AI models, including unit testing, integration testing, penetration testing, red teaming, use case testing, and adversarial testing. | `recommended-practice` / `guidance` | `government-voluntary-framework` | `alignment` | `reviewed-analytical-summary` / `direct-public-primary` |

## Towards a common reporting framework for AI incidents — 2025

- Source: `EXT-E1BE6678F807` / `OECD-AI-INCIDENT-REPORTING-2025`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0
- Review priority: `supporting-specialist-source`
- Next action: Crosswalk VIGIL failure-report fields against OECD reporting criteria without converting policy guidance into mandatory duties.

No requirement records are asserted. AI-specific incident-reporting framework retained for reporting-dimension and interoperability comparison, not as a binding requirement baseline.

## SPDX Specification 3.0.1 — AI Profile — 3.0.1

- Source: `EXT-71B4139453FA` / `SPDX-SPEC`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 4
- Review priority: `supporting-specialist-source`
- Next action: Maintain source/version surveillance and re-review on material revision.

| Requirement | Clause/control | Summary | Posture / type | External authority | Relationship | Review / access |
| --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-2514768EC96941E6` | AI profile conformance | Every AI package must be the from-element of exactly one hasConcludedLicense relationship. | `conformity-evidence-expectation` / `conformity-criterion` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-51B823BB26E5C870` | AI/AIPackage | An AI package may record AI-specific information including autonomy, domain, energy consumption, hyperparameters, training and application information, limitations, metrics and thresholds, preprocessing, explainability, safety risk assessment, standards compliance, model type and use of sensitive personal information. | `permitted-optional` / `permission` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-5EF3B75BAAAB980A` | AI/AIPackage | An AI package must carry the required inherited identity, creation, supplier, release, download, version and primary-purpose properties defined for AIPackage. | `conformity-evidence-expectation` / `conformity-criterion` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
| `EXTREQ-DFB4F86BA99C60CF` | AI profile conformance | Every AI package must be the from-element of exactly one hasDeclaredLicense relationship. | `conformity-evidence-expectation` / `conformity-criterion` | `voluntary-technical-specification` | `conformance` | `reviewed-analytical-summary` / `direct-public-primary` |
