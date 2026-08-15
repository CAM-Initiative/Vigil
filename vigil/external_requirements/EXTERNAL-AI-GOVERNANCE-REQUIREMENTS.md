# External AI-Governance Requirements

Generated from the maintained Layer 0 source ledger, Layer 1 source-scope decisions and requirement records. This catalogue does not state Caelestis coverage or conformance.

- Registered source versions: 72
- Primary AI-governance source versions: 55
- Requirement records: 159

## CycloneDX 1.7 — Machine Learning Bill of Materials (ML-BOM) — 1.7

- Source: `EXT-13FB945E8A06` / `CYCLONEDX-SPEC`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 4 (4 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-29122B7046B06256` | component.modelCard | A model card should be specified for a component whose type is machine-learning-model. | `recommended-practice` | CycloneDX BOM producer | A model card should be specified for a component whose type is machine-learning-model. | A modelCard object attached to the machine-learning-model component. | `reviewed-analytical-summary` |
| `EXTREQ-6C1C17AD6C66F27A` | component.modelCard | A model card must not be specified for component types other than machine-learning-model. | `mandatory-normative` | CycloneDX BOM producer | A model card must not be specified for component types other than machine-learning-model. | Schema-valid component representation without modelCard for non-machine-learning-model types. | `reviewed-analytical-summary` |
| `EXTREQ-B4146C7FA881D345` | modelCard | A model card can represent model parameters, datasets, inputs, outputs, quantitative analysis, performance metrics, intended users and use cases, limitations, trade-offs, ethical and fairness considerations, and environmental information. | `informative-guidance` | CycloneDX BOM producer | A model card can represent model parameters, datasets, inputs, outputs, quantitative analysis, performance metrics, intended users and use cases, limitations, trade-offs, ethical and fairness considerations, and environmental information. | Applicable structured model-card fields in the CycloneDX BOM. | `reviewed-analytical-summary` |
| `EXTREQ-FA1B882FFAD54D93` | modelCard.bom-ref | If a model-card bom-ref is supplied, it must be unique within the BOM and must not start with the reserved urn:cdx: prefix. | `conformity-evidence-expectation` | CycloneDX BOM producer | If a model-card bom-ref is supplied, it must be unique within the BOM and must not start with the reserved urn:cdx: prefix. | A unique model-card bom-ref satisfying the schema pattern. | `reviewed-analytical-summary` |

## Regulation (EU) 2024/1689 (Artificial Intelligence Act) — 2024-07-12

- Source: `EXT-7DB18E82C9D3` / `EU-AI-ACT-2024-1689`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `superseded-version`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Historical original legal-text version is preserved. Current extraction targets the registered 27 July 2026 consolidated version.

## Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated 27 July 2026 — 2026-07-27

- Source: `EXT-7DB18E82C9D3` / `EU-AI-ACT-2024-1689`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 35 (35 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-09AD2F5442A55B55` | Article 10 | Training, validation and testing data for high-risk AI systems must be subject to appropriate data-governance and management practices and meet applicable quality criteria. | `mandatory-normative` | Provider of a high-risk AI system | Training, validation and testing data for high-risk AI systems must be subject to appropriate data-governance and management practices and meet applicable quality criteria. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-901AD2C0A909E790` | Article 11 | Technical documentation for a high-risk AI system must be drawn up before market placement or putting into service, kept up to date and demonstrate compliance. | `mandatory-normative` | Provider of a high-risk AI system | Technical documentation for a high-risk AI system must be drawn up before market placement or putting into service, kept up to date and demonstrate compliance. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-33898CCD26FBF5D5` | Article 12 | High-risk AI systems must technically allow automatic recording of events over their lifetime, with logging capabilities appropriate to the system purpose. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must technically allow automatic recording of events over their lifetime, with logging capabilities appropriate to the system purpose. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-126CB22D1FF08066` | Article 13 | High-risk AI systems must be sufficiently transparent for deployers to interpret output and use the system appropriately, and must be accompanied by specified instructions for use. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must be sufficiently transparent for deployers to interpret output and use the system appropriately, and must be accompanied by specified instructions for use. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-1B4CA7A04D63F038` | Article 14 | High-risk AI systems must be designed and developed for effective oversight by natural persons, including abilities to understand limitations, avoid automation bias, interpret output and intervene or stop use. | `mandatory-normative` | Provider of a high-risk AI system, Natural person assigned oversight | High-risk AI systems must be designed and developed for effective oversight by natural persons, including abilities to understand limitations, avoid automation bias, interpret output and intervene or stop use. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E640D3CE18685E25` | Article 15 | High-risk AI systems must achieve appropriate accuracy, robustness and cybersecurity and perform consistently throughout their lifecycle. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must achieve appropriate accuracy, robustness and cybersecurity and perform consistently throughout their lifecycle. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-58706CBEC1A51EB4` | Article 16 | Providers of high-risk AI systems must ensure compliance, operate quality management, retain documentation and logs, complete conformity and registration steps, take corrective action and demonstrate conformity to authorities. | `mandatory-normative` | Provider of a high-risk AI system | Providers of high-risk AI systems must ensure compliance, operate quality management, retain documentation and logs, complete conformity and registration steps, take corrective action and demonstrate conformity to authorities. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-548AC1A3F63A1A72` | Article 17 | Providers of high-risk AI systems must put a documented quality-management system in place covering regulatory compliance, design, testing, data, risk, post-market monitoring, incident reporting, communications and accountability. | `mandatory-normative` | Provider of a high-risk AI system | Providers of high-risk AI systems must put a documented quality-management system in place covering regulatory compliance, design, testing, data, risk, post-market monitoring, incident reporting, communications and accountability. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-D7A373EB690716A5` | Article 18 | Providers must retain technical documentation, quality-management documentation, notified-body decisions and the EU declaration of conformity for the required period. | `mandatory-normative` | Provider of a high-risk AI system | Providers must retain technical documentation, quality-management documentation, notified-body decisions and the EU declaration of conformity for the required period. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-B4F479B7788DC592` | Article 19 | Providers must retain automatically generated logs under their control for an appropriate period and at least the statutory minimum where applicable. | `mandatory-normative` | Provider of a high-risk AI system | Providers must retain automatically generated logs under their control for an appropriate period and at least the statutory minimum where applicable. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-0BB8EF47B5781DD6` | Article 20 | A provider that considers a high-risk system non-conforming must promptly take corrective action, withdraw, disable or recall it as appropriate, inform relevant operators and authorities, and investigate where risk is present. | `mandatory-normative` | Provider of a high-risk AI system | A provider that considers a high-risk system non-conforming must promptly take corrective action, withdraw, disable or recall it as appropriate, inform relevant operators and authorities, and investigate where risk is present. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-227DA1B3E5921A89` | Article 21 | Providers must provide competent authorities, on reasoned request, the information, documentation and log access needed to demonstrate conformity. | `mandatory-normative` | Provider of a high-risk AI system | Providers must provide competent authorities, on reasoned request, the information, documentation and log access needed to demonstrate conformity. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-BD6495BEB2AA0C15` | Article 22 | A non-EU provider must appoint an EU-established authorised representative by written mandate before making a high-risk AI system available in the Union. | `mandatory-normative` | Provider established in a third country, Authorised representative | A non-EU provider must appoint an EU-established authorised representative by written mandate before making a high-risk AI system available in the Union. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-CDA5814A9C7B1B5A` | Article 23 | Importers must verify conformity prerequisites before placing a high-risk AI system on the market and must not place a system they consider non-conforming. | `mandatory-normative` | Importer of a high-risk AI system | Importers must verify conformity prerequisites before placing a high-risk AI system on the market and must not place a system they consider non-conforming. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2D26DDAF4FB34ED8` | Article 24 | Distributors must verify specified conformity markings, documents and provider/importer compliance before making a high-risk AI system available. | `mandatory-normative` | Distributor of a high-risk AI system | Distributors must verify specified conformity markings, documents and provider/importer compliance before making a high-risk AI system available. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-C858FECFE6BEA127` | Article 25 | AI value-chain operators must allocate information, capability, technical access and assistance needed for compliance by written agreement, and specified changes can transfer provider responsibilities. | `mandatory-normative` | AI-system provider, Third-party supplier, Distributor, Importer, Deployer | AI value-chain operators must allocate information, capability, technical access and assistance needed for compliance by written agreement, and specified changes can transfer provider responsibilities. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2490B1488A2F8FD8` | Article 26 | Deployers of high-risk AI systems must follow instructions, assign competent human oversight, ensure relevant input data, monitor operation, keep logs under their control and report risks or serious incidents. | `mandatory-normative` | Deployer of a high-risk AI system | Deployers of high-risk AI systems must follow instructions, assign competent human oversight, ensure relevant input data, monitor operation, keep logs under their control and report risks or serious incidents. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-AE55A8440D88FE84` | Article 27 | Specified deployers must perform and document a fundamental-rights impact assessment before first use of a high-risk AI system and update it when relevant factors change. | `mandatory-normative` | Public-law deployer, Private entity providing public services, Specified deployer of a high-risk AI system | Specified deployers must perform and document a fundamental-rights impact assessment before first use of a high-risk AI system and update it when relevant factors change. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-3976A1FD027244DD` | Article 4 | Providers and deployers must take measures to ensure a sufficient level of AI literacy among staff and other persons operating AI systems on their behalf. | `mandatory-normative` | AI-system provider, AI-system deployer | Providers and deployers must take measures to ensure a sufficient level of AI literacy among staff and other persons operating AI systems on their behalf. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-C94FFF97F30D7A07` | Article 43 | High-risk AI systems must undergo the applicable conformity-assessment procedure before placement on the market or putting into service and after specified substantial modifications. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must undergo the applicable conformity-assessment procedure before placement on the market or putting into service and after specified substantial modifications. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-9A9130EBEF017065` | Article 47 | The provider must draw up, keep and update an EU declaration of conformity for each high-risk AI system and assume responsibility for compliance. | `mandatory-normative` | Provider of a high-risk AI system | The provider must draw up, keep and update an EU declaration of conformity for each high-risk AI system and assume responsibility for compliance. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-E3ECA4635E3449E1` | Article 48 | High-risk AI systems must bear CE marking visibly, legibly and indelibly, or digitally where appropriate, to indicate conformity. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must bear CE marking visibly, legibly and indelibly, or digitally where appropriate, to indicate conformity. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-0C261B7C9D349171` | Article 49 | Providers and specified deployers must register themselves and applicable high-risk AI systems in the EU database before placement, service or use as required. | `mandatory-normative` | Provider of a high-risk AI system, Specified deployer of a high-risk AI system | Providers and specified deployers must register themselves and applicable high-risk AI systems in the EU database before placement, service or use as required. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-F30E6B9A906370B9` | Article 4a | Providers and deployers may exceptionally process special-category personal data to detect and correct bias only where strictly necessary and subject to specified safeguards. | `mandatory-normative` | Provider of a high-risk AI system, Deployer of a high-risk AI system | Providers and deployers may exceptionally process special-category personal data to detect and correct bias only where strictly necessary and subject to specified safeguards. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E853E8D853626EE4` | Article 5 | AI practices prohibited by the Act must not be placed on the market, put into service or used. | `mandatory-normative` | AI-system provider, AI-system deployer, Other operator | AI practices prohibited by the Act must not be placed on the market, put into service or used. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-D90FFC45004FF420` | Article 50 | Specified AI systems must disclose AI interaction or generated/manipulated content, and deployers must disclose deepfakes and certain public-interest text, subject to stated exceptions. | `mandatory-normative` | Provider of an AI system, Deployer of an AI system | Specified AI systems must disclose AI interaction or generated/manipulated content, and deployers must disclose deepfakes and certain public-interest text, subject to stated exceptions. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-600514CF42FDB56B` | Article 51 | General-purpose AI models meeting the specified high-impact capability threshold or Commission designation criteria are classified as presenting systemic risk. | `mandatory-normative` | Provider of a general-purpose AI model, European Commission | General-purpose AI models meeting the specified high-impact capability threshold or Commission designation criteria are classified as presenting systemic risk. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-302F48C69DA478C0` | Article 53 | General-purpose AI model providers must maintain technical documentation, provide downstream information, adopt a copyright-compliance policy and publish a sufficiently detailed training-content summary. | `mandatory-normative` | Provider of a general-purpose AI model | General-purpose AI model providers must maintain technical documentation, provide downstream information, adopt a copyright-compliance policy and publish a sufficiently detailed training-content summary. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-F10EE4ADFFEE67C3` | Article 55 | Providers of general-purpose AI models with systemic risk must conduct evaluations and adversarial testing, assess and mitigate systemic risks, track and report serious incidents, ensure cybersecurity and document energy efficiency where applicable. | `mandatory-normative` | Provider of a general-purpose AI model with systemic risk | Providers of general-purpose AI models with systemic risk must conduct evaluations and adversarial testing, assess and mitigate systemic risks, track and report serious incidents, ensure cybersecurity and document energy efficiency where applicable. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-9E6AAFB1F395E165` | Article 72 | Providers must establish and document a proportionate post-market monitoring system that actively and systematically collects and analyses relevant performance data throughout the high-risk AI system lifetime. | `mandatory-normative` | Provider of a high-risk AI system | Providers must establish and document a proportionate post-market monitoring system that actively and systematically collects and analyses relevant performance data throughout the high-risk AI system lifetime. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |
| `EXTREQ-C0D92D72BD0672E1` | Article 73 | Providers must report serious incidents to market-surveillance authorities within the applicable time limits and investigate the incident and affected system. | `mandatory-normative` | Provider of a high-risk AI system | Providers must report serious incidents to market-surveillance authorities within the applicable time limits and investigate the incident and affected system. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E607F0F7C181E4E3` | Article 8 | High-risk AI systems must comply with the requirements established in Section 2, taking account of intended purpose and the generally acknowledged state of the art. | `mandatory-normative` | Provider of a high-risk AI system | High-risk AI systems must comply with the requirements established in Section 2, taking account of intended purpose and the generally acknowledged state of the art. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-4B2B71D9D528EE21` | Article 85 | Natural or legal persons may lodge complaints with the relevant market-surveillance authority where they have grounds to consider that the Act has been infringed. | `mandatory-normative` | Affected natural person, Affected legal person | Natural or legal persons may lodge complaints with the relevant market-surveillance authority where they have grounds to consider that the Act has been infringed. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-9CAB350B6E590AE9` | Article 86 | A person subject to a legally significant decision based on high-risk AI output has a right to clear and meaningful explanations of the system's role and main elements of the decision, subject to stated conditions. | `mandatory-normative` | Deployer of a high-risk AI system, Affected person | A person subject to a legally significant decision based on high-risk AI output has a right to clear and meaningful explanations of the system's role and main elements of the decision, subject to stated conditions. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-44B7BB17CB030468` | Article 9 | A continuous iterative risk-management system must be established, implemented, documented and maintained throughout the high-risk AI system lifecycle. | `mandatory-normative` | Provider of a high-risk AI system | A continuous iterative risk-management system must be established, implemented, documented and maintained throughout the high-risk AI system lifecycle. | Records or artefacts required by the cited article to demonstrate or operate the obligation. | `reviewed-analytical-summary` |

## Regulation (EU) 2024/2847 — Cyber Resilience Act — 2024-11-20

- Source: `EXT-520160AFF6F2` / `EU-CRA-2024-2847`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Regulation (EU) 2023/2854 — Data Act — 2023-12-22

- Source: `EXT-8C86296B74F3` / `EU-DATA-ACT-2023-2854`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Regulation (EU) 2022/868 — Data Governance Act — 2022-06-03

- Source: `EXT-CC0DF5403326` / `EU-DGA-2022-868`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Regulation (EU) 2022/2065 — Digital Services Act — 2022-10-27

- Source: `EXT-6A56DEC1D4F8` / `EU-DSA-2022-2065`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Regulation (EU) 2016/679 — General Data Protection Regulation — 2016-05-04

- Source: `EXT-76B0AF88E460` / `EU-GDPR-2016-679`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Directive (EU) 2022/2555 — NIS 2 Directive — 2022-12-27

- Source: `EXT-09FD2B8839B5` / `EU-NIS2-2022-2555`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## IEEE Standard for an Age Appropriate Digital Services Framework Based on the 5Rights Principles for Children — 2021

- Source: `EXT-D009E06C7E91` / `IEEE-2089`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## IEEE Recommended Practice for Organizational Governance of Artificial Intelligence — 2026

- Source: `EXT-C6E029B2EF0F` / `IEEE-2863`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard Model Process for Addressing Ethical Concerns during System Design — 2021

- Source: `EXT-31AD0314218F` / `IEEE-7000`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard for Transparency of Autonomous Systems — 2021

- Source: `EXT-338E4D8BD259` / `IEEE-7001`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard for Data Privacy Process — 2022

- Source: `EXT-E9F381FE8748` / `IEEE-7002`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## IEEE Standard for Algorithmic Bias Considerations — 2024

- Source: `EXT-0A23E7D97928` / `IEEE-7003`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard for Transparent Employer Data Governance — 2021

- Source: `EXT-81484E94526F` / `IEEE-7005`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## IEEE Ontological Standard for Ethically Driven Robotics and Automation Systems — 2021

- Source: `EXT-7E4B8ED73AA5` / `IEEE-7007`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard for Fail-Safe Design of Autonomous and Semi-Autonomous Systems — 2024

- Source: `EXT-564A4CAA4F00` / `IEEE-7009`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being — 2020

- Source: `EXT-8E377EF5CE66` / `IEEE-7010`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## IEEE Standard for Machine Readable Privacy Terms — 2025

- Source: `EXT-A99E3697B1D0` / `IEEE-7012`
- Role: `supporting-external-authority`
- Access: `official-metadata-only`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## IEEE Standard for Ethical Considerations in Emulated Empathy in Autonomous and Intelligent Systems — 2024

- Source: `EXT-8D54F96680C4` / `IEEE-7014`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Model AI Governance Framework for Agentic AI — 2026-05

- Source: `EXT-3CCBC407EAC8` / `IMDA-AGENTIC-AI-MGF`
- Role: `primary-ai-governance`
- Access: `official-public-extract`
- Extraction: `partial`
- Requirements: 6 (0 reviewed; 6 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-04FB74C618E668E5` | Framework dimension: Assess risks | Organizations should assess agentic-AI risks in light of an agent's autonomy, access, impact and operating context. | `recommended-practice` | Organization deploying agentic AI | Organizations should assess agentic-AI risks in light of an agent's autonomy, access, impact and operating context. | Not expressly stated | `provisional-interpretation` |
| `EXTREQ-ACFDB5D263DAA3E9` | Framework dimension: Bound autonomy | Organizations should bound an agent's autonomy, permissions and access according to assessed risk. | `recommended-practice` | Organization deploying agentic AI | Organizations should bound an agent's autonomy, permissions and access according to assessed risk. | Not expressly stated | `provisional-interpretation` |
| `EXTREQ-DDEFC7FAC5BF45A0` | Framework dimension: Human accountability | Organizations should assign human accountability and meaningful oversight for agentic-AI decisions and actions. | `recommended-practice` | Organization deploying agentic AI | Organizations should assign human accountability and meaningful oversight for agentic-AI decisions and actions. | Not expressly stated | `provisional-interpretation` |
| `EXTREQ-54287457A2CDE0BB` | Framework dimension: Monitoring | Organizations should monitor agentic-AI behavior and outcomes and respond to unexpected or harmful behavior. | `recommended-practice` | Organization deploying agentic AI | Organizations should monitor agentic-AI behavior and outcomes and respond to unexpected or harmful behavior. | Not expressly stated | `provisional-interpretation` |
| `EXTREQ-3F373CECA14EA0D5` | Framework dimension: Technical controls | Organizations should implement proportionate technical controls and safeguards for agentic-AI operation. | `recommended-practice` | Organization deploying agentic AI | Organizations should implement proportionate technical controls and safeguards for agentic-AI operation. | Not expressly stated | `provisional-interpretation` |
| `EXTREQ-5CDBAA6A1E06358F` | Framework dimension: Transparency | Organizations should provide appropriate transparency about agentic-AI use, capabilities, limitations and accountability arrangements. | `recommended-practice` | Organization deploying agentic AI | Organizations should provide appropriate transparency about agentic-AI use, capabilities, limitations and accountability arrangements. | Not expressly stated | `provisional-interpretation` |

## Information technology — Artificial intelligence — Treatment of unwanted bias in classification and regression machine learning tasks — 2024

- Source: `EXT-562CDDAAB3BE` / `ISO-IEC-12791`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Transparency taxonomy of AI systems — 2025

- Source: `EXT-CB22558F9F71` / `ISO-IEC-12792`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Overview of machine learning computing devices — 2024

- Source: `EXT-040EEAE53753` / `ISO-IEC-17903`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Environmental sustainability aspects of AI systems — 2025

- Source: `EXT-AEE1B71204F9` / `ISO-IEC-20226`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Beneficial AI systems — 2025

- Source: `EXT-FAD576A617FA` / `ISO-IEC-21221`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Artificial intelligence concepts and terminology — 2022

- Source: `EXT-936F50D8BC1C` / `ISO-IEC-22989`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML) — 2022

- Source: `EXT-EA4F468BEE3E` / `ISO-IEC-23053`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance on risk management — 2023

- Source: `EXT-5139058E8953` / `ISO-IEC-23894`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Bias in AI systems and AI aided decision making — 2021

- Source: `EXT-60195E2A80AC` / `ISO-IEC-24027`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Overview of trustworthiness in artificial intelligence — 2020

- Source: `EXT-C121563D0092` / `ISO-IEC-24028`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial Intelligence (AI) — Assessment of the robustness of neural networks — Part 1: Overview — 2021

- Source: `EXT-E3DC210BD8CC` / `ISO-IEC-24029-1`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence (AI) — Assessment of the robustness of neural networks — Part 2: Methodology for the use of formal methods — 2023

- Source: `EXT-E753BD22398A` / `ISO-IEC-24029-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Use cases — 2024

- Source: `EXT-1674FBA87E6B` / `ISO-IEC-24030`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Overview of ethical and societal concerns — 2022

- Source: `EXT-CB4B5330E430` / `ISO-IEC-24368`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Overview of computational approaches for AI systems — 2021

- Source: `EXT-BB1A2C1C7002` / `ISO-IEC-24372`
- Role: `context-or-discovery`
- Access: `official-metadata-only`
- Extraction: `context-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Information technology — Artificial intelligence — Process management framework for big data analytics — 2022

- Source: `EXT-F257F1512247` / `ISO-IEC-24668`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guidance for quality evaluation of artificial intelligence (AI) systems — 2024

- Source: `EXT-4D6C88D8B249` / `ISO-IEC-25058`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality model for AI systems — 2023

- Source: `EXT-87623C21D66F` / `ISO-IEC-25059`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Governance of IT — Governance implications of the use of artificial intelligence by organizations — 2022

- Source: `EXT-6B4C6A420D7A` / `ISO-IEC-38507`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Management system — 2023

- Source: `EXT-206D448EB65F` / `ISO-IEC-42001`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — AI system impact assessment — 2025

- Source: `EXT-28BBBB608503` / `ISO-IEC-42005`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Requirements for bodies providing audit and certification of artificial intelligence management systems — 2025

- Source: `EXT-797A4F77B73C` / `ISO-IEC-42006`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence (AI) — Overview of differentiated benchmarking of AI system quality characteristics — 2026

- Source: `EXT-AC009E599200` / `ISO-IEC-42106`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance on machine learning model training efficiency optimization — 2026

- Source: `EXT-C522C31221D1` / `ISO-IEC-42112`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Testing of AI — Part 2: Overview of testing AI systems — 2025

- Source: `EXT-F7D25C093670` / `ISO-IEC-42119-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Assessment of machine learning classification performance — 2022

- Source: `EXT-2532B488F72F` / `ISO-IEC-4213`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 1: Overview, terminology, and examples — 2024

- Source: `EXT-0F495407BD10` / `ISO-IEC-5259-1`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 2: Data quality measures — 2024

- Source: `EXT-1AB8EF4CB11D` / `ISO-IEC-5259-2`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 3: Data quality management requirements and guidelines — 2024

- Source: `EXT-29BC8BF61EDF` / `ISO-IEC-5259-3`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 4: Data quality process framework — 2024

- Source: `EXT-F307DA6ADE51` / `ISO-IEC-5259-4`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 5: Data quality governance framework — 2025

- Source: `EXT-1B5FBFF7B099` / `ISO-IEC-5259-5`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Data quality for analytics and machine learning (ML) — Part 6: Visualization framework for data quality — 2026

- Source: `EXT-2CC8B310E58F` / `ISO-IEC-5259-6`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — AI system life cycle processes — 2023

- Source: `EXT-DEE88CAA4636` / `ISO-IEC-5338`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Guidance for AI applications — 2024

- Source: `EXT-E5A4A33AC525` / `ISO-IEC-5339`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Reference architecture of knowledge engineering — 2024

- Source: `EXT-30D0802D15C6` / `ISO-IEC-5392`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial intelligence — Functional safety and AI systems — 2024

- Source: `EXT-EF206ED96999` / `ISO-IEC-5469`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Objectives and approaches for explainability and interpretability of machine learning (ML) models and artificial intelligence (AI) systems — 2025

- Source: `EXT-5435F9552ED1` / `ISO-IEC-6254`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Data life cycle framework — 2023

- Source: `EXT-EFFD34D14635` / `ISO-IEC-8183`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Information technology — Artificial intelligence — Controllability of automated artificial intelligence systems — 2024

- Source: `EXT-6DDF68F621A8` / `ISO-IEC-8200`
- Role: `primary-ai-governance`
- Access: `official-metadata-only`
- Extraction: `blocked-access`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Primary AI-governance source is in scope, but requirement extraction is blocked because only official metadata or an abstract was accessed.

## Artificial Intelligence Risk Management Framework (AI RMF 1.0) — 1.0

- Source: `EXT-6442C7954667` / `NIST-AI-100-1`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 71 (71 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-6320A5C27CD2562D` | GOVERN 1.1 | Legal and regulatory requirements involving AI are understood, managed and documented. | `recommended-practice` | Organization using the NIST AI RMF | Legal and regulatory requirements involving AI are understood, managed and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-8F72332AE922D993` | GOVERN 1.2 | Trustworthy-AI characteristics are integrated into organizational policies, processes, procedures and practices. | `recommended-practice` | Organization using the NIST AI RMF | Trustworthy-AI characteristics are integrated into organizational policies, processes, procedures and practices. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-3F4CDACD587C4311` | GOVERN 1.3 | Processes, procedures and practices determine the needed level of AI risk-management activity from organizational risk tolerance. | `recommended-practice` | Organization using the NIST AI RMF | Processes, procedures and practices determine the needed level of AI risk-management activity from organizational risk tolerance. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-4AF3E931C4EF1B2B` | GOVERN 1.4 | The risk-management process and its outcomes are transparent, with policies and controls established to document outcomes. | `recommended-practice` | Organization using the NIST AI RMF | The risk-management process and its outcomes are transparent, with policies and controls established to document outcomes. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-84A8B3C0B190FB83` | GOVERN 1.5 | Ongoing monitoring and periodic review of the risk-management process and outcomes are planned and organizational roles and frequency are documented. | `recommended-practice` | Organization using the NIST AI RMF | Ongoing monitoring and periodic review of the risk-management process and outcomes are planned and organizational roles and frequency are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-4C464EF3523BD496` | GOVERN 1.6 | Mechanisms inventory AI systems and the resources used to manage their risks. | `recommended-practice` | Organization using the NIST AI RMF | Mechanisms inventory AI systems and the resources used to manage their risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E0E174AA5FE5AD2B` | GOVERN 1.7 | Processes and procedures are in place for safe decommissioning and phasing out of AI systems and for safely discontinuing their use. | `recommended-practice` | Organization using the NIST AI RMF | Processes and procedures are in place for safe decommissioning and phasing out of AI systems and for safely discontinuing their use. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-DBF5850ADAEC83E4` | GOVERN 2.1 | Roles and responsibilities for AI risk management are documented and communicated across the organization and to relevant third parties. | `recommended-practice` | Organization using the NIST AI RMF | Roles and responsibilities for AI risk management are documented and communicated across the organization and to relevant third parties. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-4406FC00176EF608` | GOVERN 2.2 | Personnel and partners receive AI risk-management training so they can perform their duties and responsibilities. | `recommended-practice` | Organization using the NIST AI RMF | Personnel and partners receive AI risk-management training so they can perform their duties and responsibilities. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-7737200A1740E641` | GOVERN 2.3 | Executive leadership takes responsibility for decisions about AI-system risks. | `recommended-practice` | Organization using the NIST AI RMF | Executive leadership takes responsibility for decisions about AI-system risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-C428E36496435AB3` | GOVERN 3.1 | Decision-making about AI risk throughout the lifecycle is informed by diverse teams. | `recommended-practice` | Organization using the NIST AI RMF | Decision-making about AI risk throughout the lifecycle is informed by diverse teams. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-B850AD995985724B` | GOVERN 3.2 | Policies and procedures define and differentiate roles and responsibilities for human-AI configurations and oversight. | `recommended-practice` | Organization using the NIST AI RMF | Policies and procedures define and differentiate roles and responsibilities for human-AI configurations and oversight. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-78B9D34F9D38B5A0` | GOVERN 4.1 | Organizational policies and practices foster critical thinking and a safety-first mindset in AI design, development, deployment and use. | `recommended-practice` | Organization using the NIST AI RMF | Organizational policies and practices foster critical thinking and a safety-first mindset in AI design, development, deployment and use. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-23A856D39E460557` | GOVERN 4.2 | Organizational teams document and communicate AI-system risks and potential impacts. | `recommended-practice` | Organization using the NIST AI RMF | Organizational teams document and communicate AI-system risks and potential impacts. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-5F9DA0D0B6F0F41C` | GOVERN 4.3 | Organizational practices enable testing, incident identification and information sharing. | `recommended-practice` | Organization using the NIST AI RMF | Organizational practices enable testing, incident identification and information sharing. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-0055BCF6AB20FDB7` | GOVERN 5.1 | Processes collect, consider, prioritize and integrate feedback from those outside the team that developed or deployed the AI system. | `recommended-practice` | Organization using the NIST AI RMF | Processes collect, consider, prioritize and integrate feedback from those outside the team that developed or deployed the AI system. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-50CD57A13CF16C6A` | GOVERN 5.2 | Practices regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation. | `recommended-practice` | Organization using the NIST AI RMF | Practices regularly incorporate adjudicated feedback from relevant AI actors into system design and implementation. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-3EDCD15F1ECEC4F8` | GOVERN 6.1 | Policies and procedures address AI risks associated with third-party entities, including intellectual-property and other risks. | `recommended-practice` | Organization using the NIST AI RMF | Policies and procedures address AI risks associated with third-party entities, including intellectual-property and other risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-CF1C89C280B6A699` | GOVERN 6.2 | Contingency processes are in place for failures or incidents in third-party data or systems assessed as high risk. | `recommended-practice` | Organization using the NIST AI RMF | Contingency processes are in place for failures or incidents in third-party data or systems assessed as high risk. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E2BA27213272AF72` | MANAGE 1.1 | Whether to proceed with development or deployment is decided from mapped and measured risks and intended purposes. | `recommended-practice` | Organization using the NIST AI RMF | Whether to proceed with development or deployment is decided from mapped and measured risks and intended purposes. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-F95F33125D83F81A` | MANAGE 1.2 | Risk treatment is prioritized by impact, likelihood and available resources. | `recommended-practice` | Organization using the NIST AI RMF | Risk treatment is prioritized by impact, likelihood and available resources. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-1031AEE45BE9ED28` | MANAGE 1.3 | Responses for high-priority risks are developed, planned and documented, including mitigation, transfer, avoidance or acceptance. | `recommended-practice` | Organization using the NIST AI RMF | Responses for high-priority risks are developed, planned and documented, including mitigation, transfer, avoidance or acceptance. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-A9486CE3E82FB660` | MANAGE 1.4 | Residual risk is documented and communicated to downstream acquirers and end users. | `recommended-practice` | Organization using the NIST AI RMF | Residual risk is documented and communicated to downstream acquirers and end users. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-B7D251A503308E4A` | MANAGE 2.1 | Resources required to manage AI risks and viable non-AI alternatives are considered. | `recommended-practice` | Organization using the NIST AI RMF | Resources required to manage AI risks and viable non-AI alternatives are considered. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E5BEDF611AC4A683` | MANAGE 2.2 | Mechanisms are in place to sustain the value of deployed AI systems. | `recommended-practice` | Organization using the NIST AI RMF | Mechanisms are in place to sustain the value of deployed AI systems. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-D22AB2D961D08A9E` | MANAGE 2.3 | Procedures are established to respond to and recover from previously unknown risks. | `recommended-practice` | Organization using the NIST AI RMF | Procedures are established to respond to and recover from previously unknown risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-F1F3A6472A08E764` | MANAGE 2.4 | Mechanisms and responsibilities are established to supersede, disengage or deactivate systems whose performance or outcomes are inconsistent with intended use. | `recommended-practice` | Organization using the NIST AI RMF | Mechanisms and responsibilities are established to supersede, disengage or deactivate systems whose performance or outcomes are inconsistent with intended use. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-78837C1C44B0806B` | MANAGE 3.1 | Third-party AI risks and benefits are regularly monitored, controls are applied, and results are documented. | `recommended-practice` | Organization using the NIST AI RMF | Third-party AI risks and benefits are regularly monitored, controls are applied, and results are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-1408DB88C2C42508` | MANAGE 3.2 | Pre-trained models used in the AI system are monitored as part of maintenance. | `recommended-practice` | Organization using the NIST AI RMF | Pre-trained models used in the AI system are monitored as part of maintenance. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-559DBB147B1BEB9E` | MANAGE 4.1 | Post-deployment monitoring covers user input, appeal and override, decommissioning, incident response and change management. | `recommended-practice` | Organization using the NIST AI RMF | Post-deployment monitoring covers user input, appeal and override, decommissioning, incident response and change management. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2905C0AA3C11D9DA` | MANAGE 4.2 | Measurable continual improvement is integrated into system updates and stakeholder engagement. | `recommended-practice` | Organization using the NIST AI RMF | Measurable continual improvement is integrated into system updates and stakeholder engagement. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-6870C9F25BE482D7` | MAP 1.1 | The intended purpose, users, uses, benefits, impacts, laws, norms, assumptions, settings and performance expectations of the AI system are understood and documented. | `recommended-practice` | Organization using the NIST AI RMF | The intended purpose, users, uses, benefits, impacts, laws, norms, assumptions, settings and performance expectations of the AI system are understood and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-C5251D534A12E316` | MAP 1.2 | Interdisciplinary and diverse perspectives are used to define and document the deployment context, including participation by potentially affected communities. | `recommended-practice` | Organization using the NIST AI RMF | Interdisciplinary and diverse perspectives are used to define and document the deployment context, including participation by potentially affected communities. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-99448CA617B69B2F` | MAP 1.3 | The organization mission and relevant goals for the AI technology are understood and documented. | `recommended-practice` | Organization using the NIST AI RMF | The organization mission and relevant goals for the AI technology are understood and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-84093779C78FF4A1` | MAP 1.4 | The business value or context of business use is defined or re-evaluated. | `recommended-practice` | Organization using the NIST AI RMF | The business value or context of business use is defined or re-evaluated. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-0CCFB0AAE692E441` | MAP 1.5 | Organizational risk tolerances are determined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Organizational risk tolerances are determined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-59FCEFAD3AD44D68` | MAP 1.6 | System requirements are elicited from relevant AI actors, and socio-technical design considerations are incorporated. | `recommended-practice` | Organization using the NIST AI RMF | System requirements are elicited from relevant AI actors, and socio-technical design considerations are incorporated. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-6BA40F94C5B1FD66` | MAP 2.1 | The specific tasks and methods used to implement them are defined. | `recommended-practice` | Organization using the NIST AI RMF | The specific tasks and methods used to implement them are defined. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2831EFFBC5F8A321` | MAP 2.2 | Knowledge limits and how outputs may be used, including human oversight, are determined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Knowledge limits and how outputs may be used, including human oversight, are determined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-4A55F4250F95C5E2` | MAP 2.3 | Scientific-integrity and TEVV considerations, including data and validation assumptions, are identified and documented. | `recommended-practice` | Organization using the NIST AI RMF | Scientific-integrity and TEVV considerations, including data and validation assumptions, are identified and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-57F4CC2CD806240B` | MAP 3.1 | Potential benefits of the AI system are examined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Potential benefits of the AI system are examined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-93500A33F8E3899D` | MAP 3.2 | Potential costs, including non-monetary costs, are examined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Potential costs, including non-monetary costs, are examined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-669D0C512E2B7AD7` | MAP 3.3 | The application scope is specified and documented based on capability, context and classification. | `recommended-practice` | Organization using the NIST AI RMF | The application scope is specified and documented based on capability, context and classification. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-3B4A77A84EB7C45E` | MAP 3.4 | Processes for operator proficiency are defined, assessed and documented. | `recommended-practice` | Organization using the NIST AI RMF | Processes for operator proficiency are defined, assessed and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-CBC134B07CB4DB0A` | MAP 3.5 | Processes for human oversight are defined, assessed and documented. | `recommended-practice` | Organization using the NIST AI RMF | Processes for human oversight are defined, assessed and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-366214C3FB6CBD7B` | MAP 4.1 | Risks from components and third-party technologies, including legal and intellectual-property risks, are mapped and documented. | `recommended-practice` | Organization using the NIST AI RMF | Risks from components and third-party technologies, including legal and intellectual-property risks, are mapped and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-ACFFD259B09631E2` | MAP 4.2 | Internal controls for components, including third-party components, are identified and documented. | `recommended-practice` | Organization using the NIST AI RMF | Internal controls for components, including third-party components, are identified and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-B03C89BC46097F92` | MAP 5.1 | Likelihood and magnitude of impacts are identified and documented using available evidence, incident reports and external feedback. | `recommended-practice` | Organization using the NIST AI RMF | Likelihood and magnitude of impacts are identified and documented using available evidence, incident reports and external feedback. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-E64704F05DE5759B` | MAP 5.2 | Practices and personnel are in place to engage relevant stakeholders and integrate feedback about impacts. | `recommended-practice` | Organization using the NIST AI RMF | Practices and personnel are in place to engage relevant stakeholders and integrate feedback about impacts. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-C32F213CA1F4C104` | MEASURE 1.1 | Appropriate methods and metrics are selected for mapped risks according to significance, and risks that cannot be measured are documented. | `recommended-practice` | Organization using the NIST AI RMF | Appropriate methods and metrics are selected for mapped risks according to significance, and risks that cannot be measured are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-233EE01AB85DB0F0` | MEASURE 1.2 | The appropriateness of metrics and effectiveness of controls are regularly assessed and updated, including errors and impacts on affected communities. | `recommended-practice` | Organization using the NIST AI RMF | The appropriateness of metrics and effectiveness of controls are regularly assessed and updated, including errors and impacts on affected communities. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-7DAF9BF16EE1EED4` | MEASURE 1.3 | Independent assessors or internal experts not serving on frontline development, and relevant users or affected communities, are consulted in assessment. | `recommended-practice` | Organization using the NIST AI RMF | Independent assessors or internal experts not serving on frontline development, and relevant users or affected communities, are consulted in assessment. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-B7315893B8D75680` | MEASURE 2.1 | TEVV test sets, metrics and tools are identified and documented. | `recommended-practice` | Organization using the NIST AI RMF | TEVV test sets, metrics and tools are identified and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-6165C5E752264175` | MEASURE 2.10 | Privacy risk is examined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Privacy risk is examined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-9E0A814431B2A294` | MEASURE 2.11 | Fairness and bias are evaluated and results are documented. | `recommended-practice` | Organization using the NIST AI RMF | Fairness and bias are evaluated and results are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-C5281C9522B1CD2C` | MEASURE 2.12 | Environmental and sustainability impacts are assessed and documented. | `recommended-practice` | Organization using the NIST AI RMF | Environmental and sustainability impacts are assessed and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-E90F2DD631617DDA` | MEASURE 2.13 | The effectiveness of TEVV metrics and processes is evaluated and documented. | `recommended-practice` | Organization using the NIST AI RMF | The effectiveness of TEVV metrics and processes is evaluated and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-66474C86C4005DDB` | MEASURE 2.2 | Evaluations involving human subjects comply with applicable requirements and use representative populations. | `recommended-practice` | Organization using the NIST AI RMF | Evaluations involving human subjects comply with applicable requirements and use representative populations. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-A337E13222520E08` | MEASURE 2.3 | Performance and assurance criteria are measured in conditions similar to deployment and the results are documented. | `recommended-practice` | Organization using the NIST AI RMF | Performance and assurance criteria are measured in conditions similar to deployment and the results are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-809CCACFF672EFB9` | MEASURE 2.4 | The functionality and behavior of the AI system and its components are monitored in production. | `recommended-practice` | Organization using the NIST AI RMF | The functionality and behavior of the AI system and its components are monitored in production. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2E1D2C63187C14E8` | MEASURE 2.5 | The validity and reliability of the AI system are demonstrated, and limits on generalization are documented. | `recommended-practice` | Organization using the NIST AI RMF | The validity and reliability of the AI system are demonstrated, and limits on generalization are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-4E032FB784E538EB` | MEASURE 2.6 | The AI system is regularly evaluated for safety, including fail-safe behavior, residual risk and alignment with defined risk tolerance. | `recommended-practice` | Organization using the NIST AI RMF | The AI system is regularly evaluated for safety, including fail-safe behavior, residual risk and alignment with defined risk tolerance. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-28293B6A2D5AB761` | MEASURE 2.7 | AI-system security and resilience are evaluated and documented. | `recommended-practice` | Organization using the NIST AI RMF | AI-system security and resilience are evaluated and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-86DF9273C10549E9` | MEASURE 2.8 | Risks related to transparency and accountability are examined and documented. | `recommended-practice` | Organization using the NIST AI RMF | Risks related to transparency and accountability are examined and documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-F6E7F0CA4F94EB71` | MEASURE 2.9 | The model is explained and validated, explanations are documented, and output context is interpreted. | `recommended-practice` | Organization using the NIST AI RMF | The model is explained and validated, explanations are documented, and output context is interpreted. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-C9091A8E13995001` | MEASURE 3.1 | Existing, unanticipated and emergent risks are regularly identified and tracked using deployed-system performance. | `recommended-practice` | Organization using the NIST AI RMF | Existing, unanticipated and emergent risks are regularly identified and tracked using deployed-system performance. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-83FD9ACC984101BE` | MEASURE 3.2 | Risks that are difficult to measure or lack reliable metrics are considered for tracking. | `recommended-practice` | Organization using the NIST AI RMF | Risks that are difficult to measure or lack reliable metrics are considered for tracking. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-A50A6EADB3460E08` | MEASURE 3.3 | Feedback and appeal processes are incorporated into evaluation metrics. | `recommended-practice` | Organization using the NIST AI RMF | Feedback and appeal processes are incorporated into evaluation metrics. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-6795C6C5F4D8116C` | MEASURE 4.1 | Measurement is connected to deployment context and informed by domain experts and relevant users, and this context is documented. | `recommended-practice` | Organization using the NIST AI RMF | Measurement is connected to deployment context and informed by domain experts and relevant users, and this context is documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-65093F71FE0B832B` | MEASURE 4.2 | Measurement results are informed by input from relevant experts and AI actors and are documented. | `recommended-practice` | Organization using the NIST AI RMF | Measurement results are informed by input from relevant experts and AI actors and are documented. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |
| `EXTREQ-B14E3C4577F28D7C` | MEASURE 4.3 | Improvements or declines in performance and trustworthiness are identified and documented from consultation and field data. | `recommended-practice` | Organization using the NIST AI RMF | Improvements or declines in performance and trustworthiness are identified and documented from consultation and field data. | Documented records, results or controls identified by the subcategory. | `reviewed-analytical-summary` |

## Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations — E2025

- Source: `EXT-2B2B0FF7FBE9` / `NIST-AI-100-2`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 5 (5 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-E85789205A356A50` | Section 3 | Adversarial machine-learning risks should be characterized across the AI lifecycle using common terminology for attacker goals, capabilities, knowledge and attack stages. | `recommended-practice` | Organization developing or using AI | Adversarial machine-learning risks should be characterized across the AI lifecycle using common terminology for attacker goals, capabilities, knowledge and attack stages. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-B7088F30C43E6463` | Section 4 | Organizations should assess evasion attacks that modify inputs at inference time to cause incorrect behavior. | `recommended-practice` | Organization developing or using AI | Organizations should assess evasion attacks that modify inputs at inference time to cause incorrect behavior. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-3745EB26CC7B9A5F` | Section 5 | Organizations should assess poisoning attacks that manipulate training data or processes to alter learned model behavior. | `recommended-practice` | Organization developing or using AI | Organizations should assess poisoning attacks that manipulate training data or processes to alter learned model behavior. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-A2DE5ECBC85B954D` | Section 6 | Organizations should assess privacy attacks that infer or extract sensitive information from models, training data or outputs. | `recommended-practice` | Organization developing or using AI | Organizations should assess privacy attacks that infer or extract sensitive information from models, training data or outputs. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2F298ACC2DE09299` | Section 7 | Adversarial-ML risk management should select and evaluate mitigations in relation to the relevant attack, threat model and lifecycle stage. | `recommended-practice` | Organization developing or using AI | Adversarial-ML risk management should select and evaluate mitigations in relation to the relevant attack, threat model and lifecycle stage. | Not expressly stated | `reviewed-analytical-summary` |

## The Language of Trustworthy AI: An In-Depth Glossary of Terms — 2023

- Source: `EXT-13A4EA0D8BCF` / `NIST-AI-100-3`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Reducing Risks Posed by Synthetic Content: An Overview of Technical Approaches to Digital Content Transparency — 2024

- Source: `EXT-5BC2AAEAF1D3` / `NIST-AI-100-4`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 4 (4 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-90877E875B6C164A` | Section 3 | Organizations should use provenance, authentication and content-credential techniques to improve transparency about synthetic content origin and modification history. | `recommended-practice` | Organization developing or using AI | Organizations should use provenance, authentication and content-credential techniques to improve transparency about synthetic content origin and modification history. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-F118B5C4982252FF` | Section 4 | Synthetic-content detection techniques should be evaluated for effectiveness, limitations and robustness in relevant contexts. | `recommended-practice` | Organization developing or using AI | Synthetic-content detection techniques should be evaluated for effectiveness, limitations and robustness in relevant contexts. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-F06CA6F4515987A8` | Section 5 | Content labeling and disclosure approaches should communicate synthetic or manipulated status while accounting for usability and accessibility. | `recommended-practice` | Organization developing or using AI | Content labeling and disclosure approaches should communicate synthetic or manipulated status while accounting for usability and accessibility. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-A15762516FC5C13D` | Section 6 | Synthetic-content transparency should use layered and complementary technical and governance measures rather than depend on a single technique. | `recommended-practice` | Organization developing or using AI | Synthetic-content transparency should use layered and complementary technical and governance measures rather than depend on a single technique. | Not expressly stated | `reviewed-analytical-summary` |

## A Plan for Global Engagement on AI Standards — 2025

- Source: `EXT-5316F21598A2` / `NIST-AI-100-5`
- Role: `context-or-discovery`
- Access: `direct-public-primary`
- Extraction: `context-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained for terminology, examples, strategy or discovery context. It is not treated as an independently assessable current requirement baseline.

## Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile — 2024

- Source: `EXT-DE4FDB52698E` / `NIST-AI-600-1`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 22 (22 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-8096823CE7FE00C1` | 2.1 | Organizations should consider and manage cbrn information or capability risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage cbrn information or capability risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-70FB934007D26B99` | 2.10 | Organizations should consider and manage intellectual-property risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage intellectual-property risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-FF415140E4149BA7` | 2.11 | Organizations should consider and manage obscene, degrading or abusive content risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage obscene, degrading or abusive content risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-C9B7A3D72C4A6511` | 2.12 | Organizations should consider and manage value-chain and component-integration risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage value-chain and component-integration risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-5C707CDA63126398` | 2.2 | Organizations should consider and manage confabulation risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage confabulation risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-D80867BEF745997B` | 2.3 | Organizations should consider and manage dangerous, violent or hateful content risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage dangerous, violent or hateful content risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-E4B604764848C260` | 2.4 | Organizations should consider and manage data privacy risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage data privacy risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2AED24B068EA924F` | 2.5 | Organizations should consider and manage environmental impact risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage environmental impact risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-5A3DEC25113D0F81` | 2.6 | Organizations should consider and manage harmful bias and homogenization risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage harmful bias and homogenization risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-F591D6427C6EE07D` | 2.7 | Organizations should consider and manage human-ai configuration risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage human-ai configuration risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-86938D79BBFF174E` | 2.8 | Organizations should consider and manage information integrity risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage information integrity risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-06E16BB05C087E2A` | 2.9 | Organizations should consider and manage information security risk when identifying generative-AI risks. | `recommended-practice` | Organization developing or using generative AI | Organizations should consider and manage information security risk when identifying generative-AI risks. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-7732367879542D01` | GOVERN 1.1 | Maintain awareness of legal and regulatory requirements relevant to generative AI and incorporate them into governance. | `recommended-practice` | Organization developing or using generative AI | Maintain awareness of legal and regulatory requirements relevant to generative AI and incorporate them into governance. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-D7928D57E2EBAE27` | GOVERN 1.7 | Plan for safe decommissioning of generative-AI systems, including retained data, model access and downstream dependencies. | `recommended-practice` | Organization developing or using generative AI | Plan for safe decommissioning of generative-AI systems, including retained data, model access and downstream dependencies. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-4681B6AB7E4B7C8A` | GOVERN 4.3 | Establish mechanisms to identify, document and disclose generative-AI incidents and share relevant information. | `recommended-practice` | Organization developing or using generative AI | Establish mechanisms to identify, document and disclose generative-AI incidents and share relevant information. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-F115F5477FCED9CB` | MANAGE 1.3 | Plan and document responses for prioritized generative-AI risks, including mitigations and residual risk. | `recommended-practice` | Organization developing or using generative AI | Plan and document responses for prioritized generative-AI risks, including mitigations and residual risk. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-64ADA20063447574` | MANAGE 4.1 | Monitor deployed generative-AI systems for emergent risks, user feedback, incidents and changes in capability or use. | `recommended-practice` | Organization developing or using generative AI | Monitor deployed generative-AI systems for emergent risks, user feedback, incidents and changes in capability or use. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-BCFD713ABF7CDA08` | MAP 1.1 | Document intended purpose, capabilities, limitations, users and deployment contexts for generative-AI systems. | `recommended-practice` | Organization developing or using generative AI | Document intended purpose, capabilities, limitations, users and deployment contexts for generative-AI systems. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-97FF7789E33E00CA` | MAP 4.1 | Map and document risks from foundation models, datasets, software components and other third parties in the generative-AI value chain. | `recommended-practice` | Organization developing or using generative AI | Map and document risks from foundation models, datasets, software components and other third parties in the generative-AI value chain. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-B3E57F05FF8E9B46` | MEASURE 2.11 | Evaluate harmful bias in generative-AI outputs across relevant groups, languages and use contexts. | `recommended-practice` | Organization developing or using generative AI | Evaluate harmful bias in generative-AI outputs across relevant groups, languages and use contexts. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-6C43DDE7799A545D` | MEASURE 2.5 | Evaluate generative-AI validity and reliability and document limitations and failure modes in relevant contexts. | `recommended-practice` | Organization developing or using generative AI | Evaluate generative-AI validity and reliability and document limitations and failure modes in relevant contexts. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |
| `EXTREQ-75E4071CB88B3594` | MEASURE 2.7 | Evaluate generative-AI security and resilience, including adversarial risks relevant to the system and use context. | `recommended-practice` | Organization developing or using generative AI | Evaluate generative-AI security and resilience, including adversarial risks relevant to the system and use context. | Documented action or assessment artefact where specified by the suggested action. | `reviewed-analytical-summary` |

## The NIST Cybersecurity Framework (CSF) 2.0 — 2.0

- Source: `EXT-09F549521716` / `NIST-CSF-2-0`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Towards a Standard for Identifying and Managing Bias in Artificial Intelligence — 2022

- Source: `EXT-1BE47AB84994` / `NIST-SP-1270`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 3 (3 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-AF8098BE5D37DB2F` | Section 3 | Bias in AI should be treated as a socio-technical phenomenon arising from systemic, computational and human sources. | `recommended-practice` | Organization developing or using AI | Bias in AI should be treated as a socio-technical phenomenon arising from systemic, computational and human sources. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-740699EEAC589A36` | Section 4 | Organizations should identify and manage bias throughout data collection, model development, evaluation, deployment and monitoring. | `recommended-practice` | Organization developing or using AI | Organizations should identify and manage bias throughout data collection, model development, evaluation, deployment and monitoring. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-A1255A14CD2B2059` | Section 5 | AI bias management should use organizational governance, diverse perspectives, documented context and engagement with affected communities. | `recommended-practice` | Organization developing or using AI | AI bias management should use organizational governance, diverse perspectives, documented context and engagement with affected communities. | Not expressly stated | `reviewed-analytical-summary` |

## Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities — 1.1

- Source: `EXT-4AADC9C1B06B` / `NIST-SP-800-218`
- Role: `supporting-external-authority`
- Access: `direct-public-primary`
- Extraction: `supporting-only`
- Requirements: 0 (0 reviewed; 0 unresolved)

No requirement records are asserted. Retained as a bounded supporting authority. It is not decomposed into a comprehensive first-class requirement corpus in EXTREQ-01.

## Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile — 2024

- Source: `EXT-65F7658B8B04` / `NIST-SP-800-218A`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `partial`
- Requirements: 5 (5 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-68CF252D0E20D42E` | PW.1 | AI model and system security requirements and risks should be identified during design and incorporated into secure development practices. | `recommended-practice` | Organization developing or using AI | AI model and system security requirements and risks should be identified during design and incorporated into secure development practices. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-3A4B0A2D2797720F` | PW.4 | Training data, model weights, code and other AI-system components should be protected against unauthorized access, modification and supply-chain compromise. | `recommended-practice` | Organization developing or using AI | Training data, model weights, code and other AI-system components should be protected against unauthorized access, modification and supply-chain compromise. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-4CDBC424BA361AA0` | PW.7 | AI systems should be security-tested for relevant adversarial threats and vulnerabilities before release and after material change. | `recommended-practice` | Organization developing or using AI | AI systems should be security-tested for relevant adversarial threats and vulnerabilities before release and after material change. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-2A413A1A24FE2B94` | RV.1 | Deployed AI systems and components should be monitored for vulnerabilities, attacks and unexpected security behavior. | `recommended-practice` | Organization developing or using AI | Deployed AI systems and components should be monitored for vulnerabilities, attacks and unexpected security behavior. | Not expressly stated | `reviewed-analytical-summary` |
| `EXTREQ-9D602FF3E2ABDB09` | RV.2 | Organizations should analyze, prioritize, remediate and disclose AI-related vulnerabilities through defined response processes. | `recommended-practice` | Organization developing or using AI | Organizations should analyze, prioritize, remediate and disclose AI-related vulnerabilities through defined response processes. | Not expressly stated | `reviewed-analytical-summary` |

## SPDX Specification 3.0.1 — AI Profile — 3.0.1

- Source: `EXT-71B4139453FA` / `SPDX-SPEC`
- Role: `primary-ai-governance`
- Access: `direct-public-primary`
- Extraction: `complete`
- Requirements: 4 (4 reviewed; 0 unresolved)

| Requirement | Clause/control | Summary | Posture | Actor | Governance expectation | Evidence expectation | Review state |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXTREQ-2514768EC96941E6` | AI profile conformance | Every AI package must be the from-element of exactly one hasConcludedLicense relationship. | `conformity-evidence-expectation` | SPDX document producer | Every AI package must be the from-element of exactly one hasConcludedLicense relationship. | An SPDX relationship with relationshipType hasConcludedLicense whose from-element is the AI package. | `reviewed-analytical-summary` |
| `EXTREQ-DFB4F86BA99C60CF` | AI profile conformance | Every AI package must be the from-element of exactly one hasDeclaredLicense relationship. | `conformity-evidence-expectation` | SPDX document producer | Every AI package must be the from-element of exactly one hasDeclaredLicense relationship. | An SPDX relationship with relationshipType hasDeclaredLicense whose from-element is the AI package. | `reviewed-analytical-summary` |
| `EXTREQ-51B823BB26E5C870` | AI/AIPackage | An AI package may record AI-specific governance information including autonomy, domain, training and application information, limitations, metrics, preprocessing, explainability, safety risk assessment, standards compliance and sensitive personal information. | `permitted-optional` | SPDX document producer | An AI package may record AI-specific governance information including autonomy, domain, training and application information, limitations, metrics, preprocessing, explainability, safety risk assessment, standards compliance and sensitive personal information. | Applicable optional AIPackage properties encoded in the SPDX document. | `reviewed-analytical-summary` |
| `EXTREQ-5EF3B75BAAAB980A` | AI/AIPackage | An AI package must carry the required inherited identity, creation, supplier, release, download, version and primary-purpose properties defined for AIPackage. | `conformity-evidence-expectation` | SPDX document producer | An AI package must carry the required inherited identity, creation, supplier, release, download, version and primary-purpose properties defined for AIPackage. | AIPackage includes creationInfo, name, spdxId, releaseTime, suppliedBy, downloadLocation, packageVersion and primaryPurpose. | `reviewed-analytical-summary` |
