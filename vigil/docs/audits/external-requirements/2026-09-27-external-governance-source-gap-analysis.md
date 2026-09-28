# AI Governance Standards Baseline 0.2.0 — Source Gap Analysis and Release Record

**Audit date:** 2026-09-27 (completed 2026-09-28)  
**Status:** VERIFIED RELEASE AUDIT — AI Governance Standards Baseline 0.2.0
**Release baseline:** 85 registered source versions; 978 canonical `EXTREQ` records
**Scope boundary:** Four sources are registered without requirement extraction. Canonical source/scope data and deterministic projections change; requirement records, taxonomy, schemas, and validators do not.

## Method and evidence boundary

The registered-source pass reconciled every source/version in `source-registry.json` with `source-scope.json`, `source-fidelity.json`, the fidelity status and blocked-source priorities, requirement manifests, and the source catalogue. “Clause-level defensible” below means an exact source/version is both historically complete and explicitly fidelity-assured; catalogue metadata is never treated as clause text. The landscape pass applied the gap and duplication tests to official publishers, regulators, intergovernmental bodies, and mature open specifications.

The maintainer supplied authoritative-source verification for Council of Europe CETS No. 225, OECD/LEGAL/0449's current 2024 revision, the current Government of Canada Directive on Automated Decision-Making, and C2PA Technical Specification 2.4 (April 2026). That verification resolves the provisional audit's network limitation for source identity, version, lifecycle and official locator. It does **not** constitute clause-level analysis: all four are registered as `not-started`, with zero EXTREQ records. No unseen ISO/IEC or IEEE clause was inferred.

# 1. Executive finding

**The index is broadly adequate for present research and bounded Compliance projection, but not yet balanced or complete enough to call a general authoritative governance corpus.** Its strongest clause-level coverage is NIST, selected licensed IEEE standards, the NIST GAI profile, Singapore's agentic framework, and specialist supply-chain specifications. The headline count still overstates clause-level breadth: only 17 source versions are both complete and fidelity-assured; 37 are blocked-access, 15 supporting-only, nine context-only, five not started, one partial, and one superseded.

There are **no P0 omissions**. The four P1 gaps identified by the provisional audit are now closed at the **registry layer**: the Council of Europe AI Convention, OECD AI Principles, Canada's federal Directive on Automated Decision-Making, and C2PA 2.4 are registered with accurate no-extraction states. They do not yet close clause-level Compliance gaps. Two public jurisdictional sources remain P2 candidates: the UK Algorithmic Transparency Recording Standard and Australia's Voluntary AI Safety Standard.

Baseline 0.2.0 should now move from registration to bounded analysis: (1) analyse the four newly registered sources before creating EXTREQ records; (2) complete IEEE 7003 and continue the EU AI Act fidelity work already queued; and (3) seek maintainer approval and lawful access for a small ISO/IEC subset. Do not buy or ingest other blocked standards merely to improve counts.

# 2. Current coverage map

## 2.1 Authority, jurisdiction, and extraction quality

| Dimension | Current state | Finding |
|---|---|---|
| Registered authority | 39 ISO/IEC, 14 IEEE, 10 NIST, 8 EU, 14 other versions | Numerically ISO-heavy, but substantively NIST/IEEE/EU-heavy because almost all ISO entries are metadata-only. |
| Jurisdiction | 64 “International”, 11 US/Canada federal, 8 EU, 1 Singapore, 1 US | “International” mostly reflects standards bodies; it does not substitute for Council of Europe, Canada, UK, or Australia authority. |
| Extraction | 17 complete; 1 partial; 5 not-started; 37 blocked; 15 supporting; 9 context; 1 superseded | The source count is not the usable requirement count. |
| Access | 31 direct-public; 11 direct-licensed; 43 official-metadata-only | Paid/licensed access is the main bottleneck, not registry discovery. |
| Clause fidelity | 17 explicitly assured versions | Only these are presently defensible for bounded clause-level Compliance use. |
| Concentration | NIST + selected IEEE supply most assured general controls; EU supplies the main binding-law corpus | Strong US/IEEE/EU centre; weak treaty, Canadian, UK, Australian, and open authenticity coverage. |

## 2.2 Governance-domain coverage

| Domain | Coverage | Principal current sources | Strategic finding |
|---|---|---|---|
| AI governance / management systems | Partial | NIST AI RMF; IEEE 7000; ISO/IEC 42001 metadata | Strong outcomes, missing accessible management-system clauses. |
| AI risk management | Strong | NIST AI RMF; NIST AI 600-1; EU AI Act | Further generic frameworks would duplicate authority. |
| Generative-AI risks | Strong | NIST AI 600-1; IEEE 7014/7014.1 | Current source layer is adequate. |
| Factual accuracy / confabulation / information integrity | Moderate–strong | NIST AI 600-1; IEEE 7014.1; NIST AI RMF | Good GAI controls; less direct authority for false task-completion claims. |
| TEVV; robustness; reliability | Strong but concentrated | IEEE 7009; NIST AI RMF; ISO robustness/testing metadata | Clause depth is good in IEEE/NIST, inaccessible in ISO. |
| AI safety / harmful behaviour | Strong | NIST profiles; EU AI Act; IEEE 7014 series | Avoid generic additions. |
| Human oversight | Strong | EU AI Act; NIST; IEEE | No immediate source gap. |
| Agentic autonomy, delegation, tools, action authority | Moderate | IMDA Agentic AI MGF; SDOS; NIST security material | Valuable but over-reliant on one government framework plus a private framework. Monitor emerging consensus work. |
| Multi-agent coordination / long-running state / control transitions | Weak | IMDA and SDOS fragments | No mature missing authority clearly passes the gap test today; monitor rather than ingest marketing frameworks. |
| Monitoring; incidents; change management | Strong / moderate | NIST; EU AI Act; OECD incident reporting; SDOS | Incident taxonomy is supporting-only; EU atomic review remains incomplete. |
| Data governance | Moderate | EU law; NIST; ISO 5259 metadata | Accessible clause-level data-quality governance is weak. |
| Provenance / lineage; model/data documentation | Moderate | SPDX AI Profile; CycloneDX ML-BOM; NIST AI 100-4 | Strong component documentation, weaker content-authenticity provenance. C2PA fills a distinct gap. |
| AI supply chain / third-party components | Strong specialist | SPDX; CycloneDX; NIST SP 800-218A | Additional SBOM formats would mostly duplicate. |
| Software / secure development; cybersecurity | Strong | NIST SP 800-218A; NIST AI 100-2; CSF supporting | Adequate for AI-specific crosswalks; retain broad cyber frameworks as supporting. |
| Privacy | Adequate contextual | GDPR; IEEE 7002/7012 supporting | Not a privacy-law corpus; no expansion absent an incident-driven need. |
| Transparency / explainability | Strong | IEEE 7001; NIST AI 100-4; EU AI Act | Additional broad transparency principles mostly duplicate. |
| Traceability / auditability | Strong | IEEE 7001; EU AI Act; SDOS | EU source-fidelity work remains. |
| Bias / fairness / discrimination | Moderate | NIST SP 1270; EU AI Act; ISO 24027 metadata; IEEE 7003 pending | Complete IEEE 7003 before adding another fairness framework. |
| Manipulation / relational AI; vulnerable users | Strong specialist | EU AI Act; IEEE 7014/7014.1; IEEE 2089 supporting | No broad ingestion gap. |
| Impact assessment | Moderate | IEEE 7010; EU AI Act; ISO 42005 metadata | Lawful ISO 42005 access would materially strengthen method-level coverage. |
| Conformity / assurance / audit | Moderate | EU AI Act; IEEE 7009; ISO 42001/42006 metadata | Clause-level management-system certification remains inaccessible. |
| Organisational accountability | Moderate–strong | NIST AI RMF; IEEE 7000; EU AI Act | CoE/OECD add institutional authority and cross-jurisdiction comparability. |
| High-consequence decision support | Moderate | EU AI Act; NIST; IEEE | Canada's directive adds a distinct operational government-decision regime. |
| Epistemic assurance / reliance calibration | Moderate–strong | NIST AI RMF; NIST AI 600-1; IEEE 7014.1 | Retrieval-specific and false-completion controls remain sparse. |
| Deployment approval / release gates | Moderate | NIST AI 600-1; IEEE 7009 | Adequate, though ISO lifecycle access would help. |
| Rollback / intervention / override / decommissioning | Moderate | EU AI Act; NIST profiles; IMDA; SDOS | ISO/IEC 8200 controllability is the most valuable access target. |
| Model evaluation / benchmark integrity | Moderate | NIST AI 100-2; AI 600-1; IEEE 7009 | Enough for present use; monitor agent evaluation standards. |
| Retrieval / external-information reliability | Weak–moderate | NIST AI 600-1 source/citation actions; IEEE 7014.1 | No mature standalone standard clearly adds more today. |
| Synthetic content / authenticity | Weak | NIST AI 100-4/100-5 context; provenance specifications | C2PA is the clearest missing mature implementation source. |
| Child protection | Bounded | IEEE 2089 supporting; EU/IEEE relational safeguards | Sufficient for current scope; sector expansion should be incident-led. |
| Environmental sustainability | Metadata/context only | ISO/IEC 20226 metadata | Not central to current Fidelity mechanisms; defer. |

# 3. Verified P1 registrations and remaining candidates

| Candidate source | Issuer | Current baseline state | Governance gap filled | Priority | Access | Recommended action | Rationale |
|---|---|---|---|---|---|---|---|
| Council of Europe AI Convention, CETS No. 225 | Council of Europe | **Registered; not started; 0 EXTREQs; open for signature and not in force** | Treaty-level lifecycle risk, remedies, accountability and procedural safeguards | P1 | Direct public primary | COMPLETE EXISTING EXTRACTION | Registration closes the source-identity gap only; treaty status and applicability must remain explicit. |
| OECD Recommendation on AI, OECD/LEGAL/0449 | OECD | **Registered; not started; 0 EXTREQs; current 2024 revision** | Intergovernmental principles and lifecycle stewardship | P1 | Direct public primary | COMPLETE EXISTING EXTRACTION | Preserve recommendation-level authority; do not turn broad principles into invented controls. |
| Canada Directive on Automated Decision-Making | Treasury Board of Canada Secretariat | **Registered; not started; 0 EXTREQs; current official instrument** | Operational public-sector impact tiers, intervention, testing, monitoring and recourse | P1 | Direct public primary | COMPLETE EXISTING EXTRACTION | Adds a distinct high-consequence public-decision regime with bounded federal scope. |
| C2PA Technical Specification 2.4 | C2PA | **Registered; not started; 0 EXTREQs; April 2026** | Signed content provenance, manifests and authenticity infrastructure | P1 | Direct public primary | COMPLETE EXISTING EXTRACTION | Distinguish normative conformance from explanatory/optional material and from factual truth. |
| UK Algorithmic Transparency Recording Standard | UK Government | Missing | Standardised public-sector disclosure | P2 | Public primary; currency recheck required | ADD AND EXTRACT later | Useful but narrower than the registered P1 set. |
| Australian Voluntary AI Safety Standard | Australian Government | Missing | Cross-jurisdiction operational guardrails | P2 | Public primary; currency recheck required | ADD AND EXTRACT later | Meaningful comparator, but substantially overlaps existing controls. |

No source is P0. Baseline 0.2.0 registers the four P1 sources but completes no new structured extraction. Registration must not be rendered as clause-level Compliance coverage.

# 4. Already indexed but under-developed

Forty-four source/version rows carry `maintainer_action_required`; 37 of those are blocked-access standards and four are the newly registered P1 sources awaiting analysis. The table below separates the material next actions from the long tail. Appendix A classifies all 85 rows.

| Source | Registry state | Extraction state | Fidelity state | Missing value | Recommended next action |
|---|---|---|---|---|---|
| EU AI Act, consolidated 2026-07-27 | Active/current legal baseline | Partial | Requires re-extraction | Remaining represented operator-facing provisions lack the same atomic/source-fidelity review already applied to Articles 4a and 9–15 | P1 — RE-AUDIT EXISTING EXTRACTION; specialist legal review remains a human gate. |
| IEEE 7003-2024 | Registered; public-access route recorded | Not started | Not assessed | Bias/fairness process requirements; would complement NIST SP 1270 | P1 — COMPLETE EXISTING EXTRACTION after primary text is retrieved and version-verified. |
| IEEE 2863-2026 | Registered | Blocked access | Not assessed | Organisational governance for AI | P2 — OBTAIN PRIMARY ACCESS only if it adds material detail beyond IEEE 7000, NIST, and ISO 42001; otherwise defer. |
| ISO/IEC 42001:2023 | Registered | Blocked access | Metadata only | Auditable AI management-system requirements | P1 — OBTAIN PRIMARY ACCESS, subject to maintainer approval. |
| ISO/IEC 42005:2025 | Registered | Blocked access | Metadata only | AI impact-assessment process requirements | P1 — OBTAIN PRIMARY ACCESS. |
| ISO/IEC 5338:2023 | Registered | Blocked access | Metadata only | AI lifecycle process integration | P1 — OBTAIN PRIMARY ACCESS. |
| ISO/IEC 8200:2024 | Registered | Blocked access | Metadata only | Controllability, intervention, override and decommissioning | P1 — OBTAIN PRIMARY ACCESS. |
| ISO/IEC 23894:2023 | Registered | Blocked access | Metadata only | International AI risk-management guidance | P2 — access only after the four ISO P1 targets; substantial NIST duplication. |
| ISO/IEC 42006:2025 | Registered | Blocked access | Metadata only | Certification-body requirements | P2 — defer until VIGIL needs conformity/certification analysis. |
| ISO/IEC 42119-2:2025 | Registered | Blocked access | Metadata only | AI testing guidance | P2 — useful specialist access target after foundational ISO sources. |
| ISO/IEC 5259-3/-4/-5 | Registered | Blocked access | Metadata only | Data-quality management, process and governance | P2 — obtain as a coherent subset only if data-quality incidents become a priority. |
| ISO/IEC 24029-1/-2 | Registered | Blocked access | Metadata only | Neural-network robustness assessment | P2 — specialist TEVV tranche, not foundational. |
| Remaining 24 blocked ISO/IEC versions | Registered | Blocked access | Metadata only | Mixed terminology, reference architectures, specialist techniques and lower-priority domains | P3 — retain catalogue metadata; do not purchase or extract in bulk. |
| IEEE 2089, 7002, 7005, 7012 | Registered and licensed | Supporting-only | Not in first-class fidelity scope | Child design, privacy process, employer data, machine-readable privacy | RETAIN AS SUPPORTING; promote only on a bounded incident/research need. |
| OECD AI incident reporting 2025 | Registered | Supporting-only | Not first-class | Common reporting concepts, not a complete control corpus | RETAIN AS SUPPORTING; do not confuse with the missing OECD AI Principles. |
| NIST CSF 2.0 and SSDF 1.1 | Registered | Supporting-only | Not first-class | General cyber/secure-development controls | RETAIN AS SUPPORTING; AI 100-2 and 800-218A already provide the AI-specific layer. |

# 5. Areas already sufficiently covered

* **Generic AI risk management:** NIST AI RMF, NIST AI 600-1, EU AI Act and IEEE 7000/7009 already provide complementary outcomes, controls, law and assurance. Add only a source with distinct authority, not another risk checklist.
* **GAI confabulation and information integrity:** NIST AI 600-1 supplies explicit suggested actions for monitoring, source/citation verification, assurance thresholds, capability claims and performance limits; IEEE 7014.1 supplies bounded factuality practices. The immediate problem is discovery/crosswalk use, not source absence.
* **Transparency and explainability:** IEEE 7001 and NIST AI 100-4 provide strong clause-level material, with EU legal duties as a scoped comparator.
* **AI secure development and adversarial risk:** NIST SP 800-218A and AI 100-2 are current first-class sources; generic cyber catalogues should remain supporting.
* **AI component and dataset documentation:** SPDX AI Profile and CycloneDX ML-BOM cover machine-readable inventory and supply-chain documentation. Add C2PA only because content authenticity is a different object.
* **Relational/manipulative AI:** IEEE 7014/7014.1 and EU prohibited-practice/transparency provisions already provide unusually specific coverage.
* **TEVV process:** IEEE 7009 plus NIST AI RMF are sufficient for current use; inaccessible ISO testing sources are specialist improvements, not emergency gaps.

# 6. Standards worth obtaining primary access to

Paid/licensed access is a **human approval gate**, not an audit action.

| Rank | Source | Why it is worth access | Why not infer from metadata |
|---:|---|---|---|
| 1 | ISO/IEC 42001:2023 | Foundational auditable AI management-system requirements across organisational governance | Catalogue scope cannot supply normative “shall” clauses, evidence, exceptions, or control relationships. |
| 2 | ISO/IEC 8200:2024 | Most direct registered source for controllability, intervention, override, and decommissioning mechanisms | The title does not reveal actor, trigger, lifecycle, or verification conditions. |
| 3 | ISO/IEC 42005:2025 | Direct impact-assessment process likely useful across many incidents and families | Clause granularity and artefact requirements are inaccessible. |
| 4 | ISO/IEC 5338:2023 | AI lifecycle integration could strengthen change, release, monitoring, and retirement controls | Metadata does not establish normative process steps. |
| 5 | IEEE 2863-2026 | Organisational AI governance may add contemporary governance practices | First perform a duplication check against IEEE 7000, ISO 42001 and NIST; access is currently blocked. |
| 6 | ISO/IEC 23894:2023 | International risk comparator | Lower urgency because NIST AI RMF is already complete and assured. |

ISO/IEC 42006, 42119-2, 5259-3/-4/-5, and 24029-1/-2 are second-tranche specialist candidates. Metadata is sufficient to catalogue all other blocked ISO sources but not to create `EXTREQ` records.

# 7. Emerging / monitor list

| Area/source family | Action | Trigger for promotion |
|---|---|---|
| NIST and international agentic-AI standards activity | MONITOR | Stable public normative guidance addressing delegation, tool authority, agent identity, multi-agent coordination, intervention, or state persistence. |
| IMDA Agentic AI MGF revisions | MONITOR | New version changes source-native controls; re-audit rather than register every announcement. |
| AI incident reporting specifications | MONITOR | Mature common reporting schema with authoritative adoption and controls beyond OECD's supporting framework. |
| Agent identity and authorisation profiles | MONITOR | Consensus specification with stable security semantics; exclude vendor protocol marketing. |
| Model-evaluation and benchmark-integrity standards | MONITOR | Mature requirements for contamination, reproducibility, evaluator independence, or claims substantiation. |
| Retrieval-augmented generation assurance | MONITOR | Authoritative source with controls beyond generic source verification, provenance, and monitoring. |
| Synthetic-content regulation and authenticity profiles | MONITOR | Binding or consensus requirements materially beyond C2PA's technical provenance layer. |

# 8. Sources NOT recommended

| Candidate | Decision | Reason |
|---|---|---|
| OWASP Top 10 for LLM Applications | DO NOT ADD as first-class requirements | Useful threat-awareness material, but NIST AI 100-2/600-1 and SSDF 800-218A provide stronger public authority and structured controls; use for discovery only if needed. |
| MITRE ATLAS | DO NOT ADD as normative requirements | Valuable adversarial knowledge base, not a governance control standard; NIST security sources are the better Compliance authority. |
| Vendor “responsible AI” principles, model system cards, and agent frameworks | DO NOT ADD by default | Vendor-specific, self-authored, frequently revised, and generally weaker than existing public/consensus authority. Use as incident evidence, not baseline governance. |
| UNESCO Recommendation on the Ethics of AI | RETAIN OUTSIDE NEXT TRANCHE | Significant soft-law context, but broad principles largely duplicate OECD/NIST/IEEE for current mechanism-level Compliance; reconsider for human-rights research after CoE/OECD. |
| G7 Hiroshima Process reporting framework/code | MONITOR / DO NOT INGEST NOW | Important policy coordination but evolving and substantially overlaps GAI risk, transparency, security, and accountability already covered. |
| Every ISO/IEC SC 42 publication | DO NOT ADD/EXTRACT EN MASSE | Registration is already broad; many entries are terminology, overview, reference architecture, or narrow techniques. Access cost must follow mechanism need. |
| Additional SBOM formats | DO NOT ADD | SPDX and CycloneDX already cover the relevant inventory/provenance layer. |
| Superseded EU AI Act 2024 text as current authority | RETAIN HISTORICALLY ONLY | Preserve for provenance and change comparison; current analysis must use the consolidated version and applicability dates. |

# 9. Recommended bounded expansion tranche

A **10-action** tranche is justified; it is deliberately smaller than the 44-row maintenance queue.

### Newly registered sources awaiting extraction (4)
1. Boundedly extract the registered Council of Europe AI Convention while preserving its not-in-force treaty lifecycle.
2. Perform principle-level extraction of the registered 2024 OECD AI Recommendation.
3. Extract the registered Canada Directive without turning the assessment tool into invented legal text.
4. Extract registered C2PA 2.4 at source-native normative granularity, separating conformance from optional material.

### Existing public sources (2)
5. Complete the already queued IEEE 7003-2024 extraction.
6. Continue the EU AI Act atomic/source-fidelity review; obtain specialist legal review before any completeness claim.

### Primary-access decisions (4; no ingestion until approved)
7. Obtain lawful access to ISO/IEC 42001:2023.
8. Obtain lawful access to ISO/IEC 8200:2024.
9. Obtain lawful access to ISO/IEC 42005:2025.
10. Obtain lawful access to ISO/IEC 5338:2023.

The UK and Australian P2 sources form a later public-source tranche only after these actions. IEEE 2863 receives a duplication review before any purchase.

# 10. Interaction with taxonomy (diagnostic only)

| Proposed source/action | Likely benefited Fidelity Families or mechanisms | Gap type |
|---|---|---|
| CoE AI Convention | Governance Control Reach; Control Activation; Agency-Preserving Influence; accountability, remedies and public-authority boundaries | B — registered, not extracted |
| OECD AI Principles | Cross-family governance context; robustness, transparency, accountability and human-centred values | B — registered, not extracted; usually supporting rather than class-defining |
| Canada Directive/AIA | Verification & Completion; Observability & Audit; Governance Control Reach; high-consequence decision support and intervention | B — registered, not extracted |
| C2PA | Provenance & Lineage; Observability & Audit; synthetic-content authenticity | B — registered, not extracted |
| IEEE 7003 | Bias/discrimination mechanisms and impact/measurement boundaries | B — registered, not extracted |
| EU AI Act continuation | Existing legal mechanisms across oversight, logging, monitoring, incidents and transparency | B — registered and partially extracted |
| ISO/IEC 42001 | Cross-family organisational governance, assurance and evidence | B — registered, inaccessible |
| ISO/IEC 8200 | Control Activation; Governance Control Reach; safe intervention, override and decommissioning | B — registered, inaccessible |
| ISO/IEC 42005 | Impact assessment and consequential-use governance across several families | B — registered, inaccessible |
| ISO/IEC 5338 | Work-State Continuity; verification applicability; change, release, operation and retirement lifecycle controls | B — registered, inaccessible |

For the separate taxonomy reconciliation's 26 classes lacking structured mappings, the most likely disposition remains **D** for narrow mechanisms such as Completion-Condition Alignment, continuity anchors, false continuity attribution, and multi-agent turn-state coordination: no sufficiently close external requirement is presently evident. A small subset may become **B** if ISO/IEC 8200, 5338, or IEEE 7003 yields source-native clauses after lawful review. Epistemic/confabulation classes are primarily **A**: appropriate NIST/IEEE requirements already exist and the issue is crosswalk use, not corpus absence. No mappings are changed here.

# Appendix A — Every registered source/version

Classification is strategic for this audit, not a change to canonical registry metadata. “No” under clause-level use means the source may still be useful as authority, context, or discovery evidence.

| Source / version | Authority / jurisdiction | Strategic class | Lifecycle | Extraction | Fidelity | Clause-level Compliance | Further work value |
|---|---|---|---|---|---|---|---|
| `AAM-SDOS-RUNTIME-GOVERNANCE` 1.10 | AAM Cyber / International | HIGH-VALUE specialist | published | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `C2PA-SPEC` 2.4 | Coalition for Content Provenance and Authenticity / International | HIGH-VALUE specialist | published | not-started | not applicable / not assessed | No | Yes — extract |
| `CANADA-DIRECTIVE-AUTOMATED-DECISION-MAKING` current-2026-09-28 | Treasury Board of Canada Secretariat / Canada/Federal | CORE / foundational | in-force | not-started | not applicable / not assessed | No | Yes — extract |
| `COE-AI-CONVENTION-CETS-225` 2024-09-05 | Council of Europe / International | CORE / foundational | open-for-signature-not-in-force | not-started | not applicable / not assessed | No | Yes — extract |
| `CYCLONEDX-SPEC` 1.7 | OWASP CycloneDX / International | SUPPORTING | published | complete | assured | Yes — bounded clauses | No current priority |
| `EU-AI-ACT-2024-1689` 2024-07-12 | European Union / European Union | DUPLICATIVE / superseded | in-force | superseded-version | not applicable / not assessed | No | No current priority |
| `EU-AI-ACT-2024-1689` 2026-07-27 | European Union / European Union | CORE / foundational | in-force | partial | requires-reextraction | No | Yes — finish/re-audit |
| `EU-CRA-2024-2847` 2024-11-20 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `EU-DATA-ACT-2023-2854` 2023-12-22 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `EU-DGA-2022-868` 2022-06-03 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `EU-DSA-2022-2065` 2022-10-27 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `EU-GDPR-2016-679` 2016-05-04 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `EU-NIS2-2022-2555` 2022-12-27 | European Union / European Union | LOW CURRENT VALUE | in-force | supporting-only | not applicable / not assessed | No | No current priority |
| `FDA-MDR-ADVERSE-EVENT-CODES` 2026-04-13 | U.S. Food and Drug Administration / United States | CONTEXT / methodology only | current | context-only | not applicable / not assessed | No | No current priority |
| `ICAO-ADREP-TAXONOMY` current-2026-08-18 | International Civil Aviation Organization / International | CONTEXT / methodology only | maintained | context-only | not applicable / not assessed | No | No current priority |
| `IEC-60812` 2018 | International Electrotechnical Commission / International | SUPPORTING | published | supporting-only | not applicable / not assessed | No | No current priority |
| `IEEE-1044` 2009 | IEEE Standards Association / International | CONTEXT / methodology only | inactive-reserved | context-only | not applicable / not assessed | No | No current priority |
| `IEEE-2089` 2021 | IEEE Standards Association / International | LOW CURRENT VALUE | active | supporting-only | not applicable / not assessed | No | No current priority |
| `IEEE-2863` 2026 | IEEE Standards Association / International | CORE / foundational | active | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `IEEE-7000` 2021 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IEEE-7001` 2021 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IEEE-7002` 2022 | IEEE Standards Association / International | LOW CURRENT VALUE | active | supporting-only | not applicable / not assessed | No | No current priority |
| `IEEE-7003` 2024 | IEEE Standards Association / International | HIGH-VALUE specialist | active | not-started | not applicable / not assessed | No | Yes — extract |
| `IEEE-7005` 2021 | IEEE Standards Association / International | LOW CURRENT VALUE | active | supporting-only | not applicable / not assessed | No | No current priority |
| `IEEE-7007` 2021 | IEEE Standards Association / International | SUPPORTING | active | complete | assured | Yes — bounded clauses | No current priority |
| `IEEE-7009` 2024 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IEEE-7010` 2020 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IEEE-7012` 2025 | IEEE Standards Association / International | LOW CURRENT VALUE | active | supporting-only | not applicable / not assessed | No | No current priority |
| `IEEE-7014` 2024 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IEEE-7014.1` 2026 | IEEE Standards Association / International | HIGH-VALUE specialist | active | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IMDA-AGENTIC-AI-MGF` 2026-05 | Infocomm Media Development Authority of Singapore / Singapore | CORE / foundational | published | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `IMDRF-AER-N43` 2026 | International Medical Device Regulators Forum / International | CONTEXT / methodology only | current | context-only | not applicable / not assessed | No | No current priority |
| `ISO-IEC-12791` 2024 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-12792` 2025 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-17903` 2024 | ISO/IEC JTC 1/SC 42 / International | CONTEXT / methodology only | published | context-only | not applicable / not assessed | No | No current priority |
| `ISO-IEC-20226` 2025 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-21221` 2025 | ISO/IEC JTC 1/SC 42 / International | SUPPORTING | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-22989` 2022 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-23053` 2022 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-23894` 2023 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-24027` 2021 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-24028` 2020 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-24029-1` 2021 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-24029-2` 2023 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-24030` 2024 | ISO/IEC JTC 1/SC 42 / International | CONTEXT / methodology only | published | context-only | not applicable / not assessed | No | No current priority |
| `ISO-IEC-24368` 2022 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-24372` 2021 | ISO/IEC JTC 1/SC 42 / International | CONTEXT / methodology only | published | context-only | not applicable / not assessed | No | No current priority |
| `ISO-IEC-24668` 2022 | ISO/IEC JTC 1/SC 42 / International | SUPPORTING | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-25058` 2024 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-25059` 2023 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-38507` 2022 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-42001` 2023 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-42005` 2025 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-42006` 2025 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-42106` 2026 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-42112` 2026 | ISO/IEC JTC 1/SC 42 / International | SUPPORTING | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-42119-2` 2025 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-4213` 2022 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5259-1` 2024 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5259-2` 2024 | ISO/IEC JTC 1/SC 42 / International | SUPPORTING | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5259-3` 2024 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-5259-4` 2024 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-5259-5` 2025 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-5259-6` 2026 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5338` 2023 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-5339` 2024 | ISO/IEC JTC 1/SC 42 / International | SUPPORTING | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5392` 2024 | ISO/IEC JTC 1/SC 42 / International | LOW CURRENT VALUE | published | blocked-access | not applicable / not assessed | No | No current priority |
| `ISO-IEC-5469` 2024 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-6254` 2025 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-8183` 2023 | ISO/IEC JTC 1/SC 42 / International | HIGH-VALUE specialist | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-8200` 2024 | ISO/IEC JTC 1/SC 42 / International | CORE / foundational | published | blocked-access | not applicable / not assessed | No | Yes, if access approved |
| `ISO-IEC-IEEE-24765` 2017 | ISO/IEC/IEEE / International | SUPPORTING | published-to-be-revised | supporting-only | not applicable / not assessed | No | No current priority |
| `NIST-AI-100-1` 1.0 | National Institute of Standards and Technology / United States/Federal | CORE / foundational | final | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `NIST-AI-100-2` E2025 | National Institute of Standards and Technology / United States/Federal | SUPPORTING | final | complete | assured | Yes — bounded clauses | No current priority |
| `NIST-AI-100-3` 2023 | National Institute of Standards and Technology / United States/Federal | CONTEXT / methodology only | final | context-only | not applicable / not assessed | No | No current priority |
| `NIST-AI-100-4` 2024 | National Institute of Standards and Technology / United States/Federal | SUPPORTING | final | complete | assured | Yes — bounded clauses | No current priority |
| `NIST-AI-100-5` 2025 | National Institute of Standards and Technology / United States/Federal | CONTEXT / methodology only | final | context-only | not applicable / not assessed | No | No current priority |
| `NIST-AI-600-1` 2024 | National Institute of Standards and Technology / United States/Federal | CORE / foundational | final | complete | assured | Yes — bounded clauses | Monitor/re-audit on revision |
| `NIST-CSF-2-0` 2.0 | National Institute of Standards and Technology / United States/Federal | LOW CURRENT VALUE | final | supporting-only | not applicable / not assessed | No | No current priority |
| `NIST-SP-1270` 2022 | National Institute of Standards and Technology / United States/Federal | SUPPORTING | final | complete | assured | Yes — bounded clauses | No current priority |
| `NIST-SP-800-218` 1.1 | National Institute of Standards and Technology / United States/Federal | LOW CURRENT VALUE | final | supporting-only | not applicable / not assessed | No | No current priority |
| `NIST-SP-800-218A` 2024 | National Institute of Standards and Technology / United States/Federal | SUPPORTING | final | complete | assured | Yes — bounded clauses | No current priority |
| `OECD-AI-INCIDENT-REPORTING-2025` 2025 | OECD / International | SUPPORTING | published | supporting-only | not applicable / not assessed | No | No current priority |
| `OECD-AI-PRINCIPLES` 2024-05-03 | OECD / International | CORE / foundational | adopted-current | not-started | not applicable / not assessed | No | Yes — extract |
| `SPDX-SPEC` 3.0.1 | SPDX / Linux Foundation / International | SUPPORTING | published | complete | assured | Yes — bounded clauses | No current priority |

# Appendix B — Decision totals and stop conditions

* **Current corpus:** 85 source versions; 978 canonical requirements.
* **Strategic classes:** {'HIGH-VALUE specialist': 25, 'CORE / foundational': 15, 'SUPPORTING': 15, 'DUPLICATIVE / superseded': 1, 'LOW CURRENT VALUE': 20, 'CONTEXT / methodology only': 9}.
* **Extraction states:** {'complete': 17, 'not-started': 5, 'superseded-version': 1, 'partial': 1, 'supporting-only': 15, 'context-only': 9, 'blocked-access': 37}.
* **Already-indexed rows needing work:** 44 canonical rows carry `maintainer_action_required`; only the bounded priorities in Sections 4, 6 and 9 should advance now.
* **Primary-access blockers:** IEEE 2863 plus 36 ISO/IEC source versions are unavailable for clause extraction; only four ISO sources are proposed for the next access decision.
* **Human gates:** paid/licensed acquisition; legal completeness/applicability judgments; any promotion of supporting-only sources; any new source family that changes architecture.
* **Release distinction:** four sources are newly registered; zero newly registered sources have completed extraction; 43 source versions await extraction, reconciliation, or access, and one complete source retains an optional legacy-identity action.
* **Lifecycle safeguard:** CETS No. 225 is recorded as open for signature and not in force.
* **Stale facts:** none were silently repaired outside the four maintainer-verified registrations.
