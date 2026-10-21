# Bounded source and relationship review

Date: 18 October 2026. Classification: REVIEW. AI-authored primary-text analysis under the maintainer handoff. Human review and verification remain not-reviewed / not-verified. This package does not certify any organisation or determine legal liability.

## Retained extraction

| Exact source | Primary text reviewed | Canonical selection | Force and boundary |
| --- | --- | --- | --- |
| NIST CSWP 29, CSF 2.0, 26 February 2024 | [Official PDF](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), introduction, function/category context and Appendix A printed pp. 19–23 | PR.AA-05, PR.IR-01, PR.PS-01, DE.CM-01, RS.MI-01, RC.RP-01, RC.RP-03, RC.RP-05 | Eight voluntary, desirable outcomes. Section 1 expressly says the framework does not prescribe outcomes or implementation. No mandatory checklist or adoption gate is introduced. |
| NIST SP 800-82 Rev. 3, September 2023; official publication page dated 28 September | [Official PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf), authority/scope, §§6.2.4.2, 6.2.10, 6.3.2.2 and 6.4.4 | Five bounded recommendations for approved configuration changes, justified/limited remote access, consideration of removing unneeded temporary access, actionable OT monitoring and conditional mitigation | Voluntary nongovernmental guidance. Performance, reliability, safety and physical-process effects remain material. The guide's CSF 1.1 labels are not relabelled as CSF 2.0 codes. |
| NIST SP 800-218, SSDF 1.1, February 2022 | [Official PDF](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf), framework scope and printed p.16 | PW.9.1 and PW.9.2 | Two software-producer tasks. Secure defaults and their implementation/documentation are distinct from operator response. Notional implementation examples remain examples. |

Exact requirement IDs, source-native locators, printed pages, carrier hashes, atomicity decisions and complete relationship dispositions are retained in the three source-specific JSON reviews. The extraction summary records 15 new requirements and 17 strong-supporting component relationships. All 1,102 baseline requirements remain equal as JSON values and retain their IDs. No baseline relationship is removed or rewritten. No direct or whole-invariant equivalence is claimed.

All three source scopes remain partial. Every admitted proposition received bounded field and atomicity review. Source-level provisional fidelity preserves the unreviewed remainder; it does not represent a resolved whole-instrument review. Known unreviewed material, next actions and maintainer actions remain explicit. The exact public PDF carrier digests are in the existing assurance sidecar; no human assurance is invented. Official NIST primary PDFs were processed; no copyrighted IEC normative text was processed or committed.

## Component fit and rejected overreach

PR.AA-05 supports independent permission enforcement and limited scope through access policy, least privilege and separation of duties. It does not identify the authentication protocol, prove every device-specific permission decision, or itself prescribe revalidation at every scope transition. PR.IR-01 is specifically protection against unauthorised logical access and usage. It is not a generic uptime or resilience guarantee.

PR.PS-01 supplies a high-level configuration-management component of Control-State Preservation. It does not establish every class recognition condition. The more specific OT configuration recommendation preserves an approved baseline and documents, tests and approves changes before deployment. A bad configuration alone cannot establish that an operative governance-control state was lost across a transition.

DE.CM-01 supports monitoring of network/service paths. OT §6.3.2.2 supports actionable monitoring across the OT system. Neither a temperature alarm nor an Internet-exposure scan alone establishes network security-monitor coverage or complete OT security monitoring. RS.MI-01 requires an actual containment outcome. Nominal activation, attempted hardening and loss incurred before containment are distinct facts.

The selected recovery outcomes separate triggered plan execution, integrity of restoration inputs before use, and validation of restored assets plus normal status. Reset, repair attendance or a recommendation to recover does not establish all three. RC.RP-03 remains irrelevant where no restoration assets are evidenced; unknown use of backups is not converted into a Boundary row.

Authentication remains separate. CSF PR.AA-03 says users, services and hardware are authenticated. It does not establish the specific device/action authority demanded by FC-002/003, nor authentication-state propagation under FC-031. This review retains it as contextual-only research and does not allocate a canonical EXTREQ from a weak class fit. Token validity, TLS or a password change cannot establish device-specific authorisation. The source-defined PR.AA-05 compound is retained with all policy, management, enforcement, review, least-privilege and separation-of-duties constituents.

Other recovery outcomes were inspected: RC.RP-02 addresses selection/prioritisation, RC.RP-04 operational norms and RC.RP-06 recovery closure/documentation. None supplied an additional necessary proposition for these bounded incident proposals. They remain outside extraction rather than becoming speculative occurrence rows. No FC-038/040/083 outcome is inferred merely because a refrigeration parameter changed. No FC definition, recognition criterion or exclusion changes.

## Industrial-control standard access hold

[IEC's official catalogue](https://webstore.iec.ch/en/publication/7033) verifies IEC 62443-3-3:2013, Edition 1.0, publication 7 August 2013. It identifies system security requirements and security levels and states that the supplied copy includes the April 2014 corrigendum. Catalogue metadata supports this precise part/version identity. It does not supply normative provisions or authority to process the standard for this task.

The canonical registration is therefore supporting-external-authority / official-metadata-only / blocked-access, with zero requirements and no FC relationship. The actionable hold requires authorised text and permission for the intended processing, then edition-specific provision and fidelity review. No SR number, security-level claim or compliance result is reconstructed from an abstract, a NIST reference or another part of the series. Other parts, such as asset-owner management-system or component-security standards, would need their own exact editions and access decisions. They are not registered as one undifferentiated series or needed to duplicate the accessible OT recommendations in this package.

The [official NIST SP 800-82 Rev.3 page](https://csrc.nist.gov/pubs/sp/800/82/r3/final) still identifies Rev.3 as final. Its 21 September 2026 planning note points to the initial public draft of Rev.4, with comments due 30 November. A draft does not silently replace the final source version used here.

## Other registered supporting authorities

| Source | Authoritative bounded review | Disposition |
| --- | --- | --- |
| [NIS2 Directive, original OJ 27 December 2022](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555) | Article 21(1)–(4), Article 41, Article 46, Annex II point 4, with entity scope in Articles 2–3 | Retain registered supporting-only state. Article 21 measures include incident handling, continuity, effectiveness review, access policies and conditional authentication. They bind the Member-State implementation route for essential/important entities, with proportionality and sector/entity conditions. Annex II food coverage concerns wholesale distribution and industrial production/processing; supermarket retail alone does not establish it. Actual French transposition, entity designation/size and responsible operator scope were not established for these stores. Accessible voluntary sources already supply the relevant technical propositions. Do not fabricate a direct legal-breach row or use unknown entity scope as a speculative Boundary result. |
| [Cyber Resilience Act, original OJ Regulation (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R2847) | Articles 69 and 71, read with Article 14 and Annex I secure-default/access-control themes | Retain supporting-only state. Article 71(2) makes general application 11 December 2027; Article 14 reporting applies from 11 September 2026 and Chapter IV from 11 June 2026. Article 69 preserves separate transitional conditions and does not defer all Article 14 duties on older products. Do not retrospectively apply future Annex I product-security duties to February/October 2026. No evidence establishes producer knowledge, triggering product scope or reporting conduct for a separate Article 14 finding. Those questions remain outside these occurrence rows. |
| Base SSDF 1.1 | PW.9 task text and notional examples reviewed independently of SP 800-218A | Admit the two bounded source-faithful tasks above. Other SSDF tasks are not expanded merely to increase coverage. A deployment defect does not automatically prove a producer's default-setting or development-process defect. |

These are original-version reviews, not an assertion of complete consolidated-law currency. Official HTML carrier hashes are retained in research-access.json. No secondary summary is substituted for inaccessible legal text. These decisions do not alter the 11 October source package, its historical review records, or the 16 October EN 18286 / decision access holds.

## Publication boundary

Only independently justified canonical occurrence rows may reach Section 04. The source-specific relationship reviews do not publish occurrence results. Dated proposals for INC-199/200/203 use the exact ingestion baseline, retain per-site distinctions and require integration on that branch separately. No website file is changed, no PR is opened and no merge or publication is performed.
