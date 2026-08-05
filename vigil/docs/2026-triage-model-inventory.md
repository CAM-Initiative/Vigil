# VIGIL Triage Model Inventory — Pass 1

> Current triage priority is mutable operational state. Historical urgency is provenance. Failure severity is classification. Triage status is workflow. Ecosystem monitoring is continuing external observation.

This is a deterministic pre-migration inventory. It records the current branch state and review flags; it does not assign replacement priority, status, or severity values.

## Scope and boundary

All 56 current failure-mode records are included. VIGIL's record-boundary contract forbids failure-mode triage in OBS and PROP/PATCH records, so those classes are not given synthetic triage state.

## Headline findings

* Invalid current priority values: 3.
* Status values outside the target workflow vocabulary: 55.
* Monitoring/watch records retaining P0 or P1: 31.
* Repaired records retaining an active priority and requiring reconciliation review: 27.
* Active P0–P3 records without a recommended next step: 0.
* Records requiring a reviewed severity mapping: 17.

## Priority counts

| Priority | Count |
| --- | --- |
| P1 | 27 |
| P0 | 23 |
| P2 | 3 |
| high | 3 |

## Status counts

| Status | Count |
| --- | --- |
| watching-after-patch | 19 |
| active evidence and governance review | 4 |
| CAM repair canonical on Caelestis main; ecosystem monitoring active | 2 |
| CAM repair verified on named Caelestis branch; ecosystem monitoring active | 2 |
| active-monitoring | 2 |
| active-research / corpus-gap assessment | 2 |
| proposal-open | 2 |
| CAM repair verified on named Caelestis branch; ecosystem and canonical-adoption monitoring active | 1 |
| active / corpus-gap assessment | 1 |
| active constitutional and operations review | 1 |
| active evidence and conformance review | 1 |
| active evidence and corpus-repair review | 1 |
| active-monitoring / observation-linked | 1 |
| active-research | 1 |
| active-research / corpus-coverage review | 1 |
| active-research / corpus-hard-prohibition assessment | 1 |
| active-research / proposal-linked | 1 |
| active-research / retrospective-corpus-coverage verification | 1 |
| active-research / specific incident provisional | 1 |
| canonical runtime-reach repair retained; composed-system architecture and classification migration verified on named branch | 1 |
| monitoring-after-corpus-coverage-reconciliation | 1 |
| monitoring-after-follow-on-patch | 1 |
| monitoring-after-patch | 1 |
| monitoring-after-successor-runtime-regression | 1 |
| needs-corpus-review | 1 |
| needs-review | 1 |
| open | 1 |
| partially repaired at amendment-provenance layer; broader governance-durability assessment remains active | 1 |
| repair-implemented-monitoring | 1 |
| watching-after-retrospective-corpus-coverage | 1 |

## Severity counts and migration boundary

| Severity | Count |
| --- | --- |
| high | 25 |
| critical | 13 |
| medium-high | 8 |
| medium | 6 |
| high; potentially critical where evidence concerns catastrophic harm, systemic risk, fundamental rights or security compromise | 1 |
| low | 1 |
| low-to-medium | 1 |
| to be assessed | 1 |

The target severity vocabulary is `critical`, `high`, `moderate`, `low`, `negligible`, `to-be-assessed`, and `not-applicable`. Existing `medium`, `medium-high`, `low-to-medium`, conditional prose ratings, and `to be assessed` are not rewritten in Pass 1. `medium-high`, `low-to-medium`, and conditional prose ratings require record-level judgment rather than blind mapping.

## Priority by record state

| Record state | Priority | Count |
| --- | --- | --- |
| monitoring | P1 | 14 |
| active | P1 | 13 |
| active | P0 | 12 |
| monitoring | P0 | 11 |
| active | high | 3 |
| monitoring | P2 | 2 |
| active | P2 | 1 |

## Priority by repair status

| Repair status | Priority | Count |
| --- | --- | --- |
| repaired | P1 | 14 |
| repaired | P0 | 11 |
| unrepaired | P0 | 11 |
| unrepaired | P1 | 10 |
| partially-repaired | P1 | 3 |
| unrepaired | high | 3 |
| repaired | P2 | 2 |
| partially-repaired | P0 | 1 |
| partially-repaired | P2 | 1 |

## Priority by monitoring state

| Monitoring required | Priority | Count |
| --- | --- | --- |
| True | P1 | 27 |
| True | P0 | 23 |
| True | P2 | 3 |
| True | high | 3 |

## Review-flag definitions

Flags are diagnostic only. `repaired-with-active-priority-review` does not assume that `none` is correct; a concrete verification or routing task may justify an active priority. `monitoring-p0-p1` includes both lifecycle monitoring and legacy watch/monitor status phrases. `legacy-severity-mapping-required` preserves severity until the migration mapping is reviewed.

## Record inventory

| Record | State | Priority | Triage status | Severity | Repair | Ecosystem | Monitoring | Next step | PATCH | LEARN | Chain appears complete | Review flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VIGIL-2026-FM-0001 | monitoring | P1 | monitoring-after-follow-on-patch | medium | repaired | active | true | Monitor post-PATCH-0013 recurrence telemetry, especially premature tool arming, model/runtime routing changes, modality-specific UI activation, renderer preparation, or execution-path reservation from weak lexical triggers, accidental submission, upload-without-instruction events, partial prompts, staged uploads, draft prompt construction, or incomplete multimodal assembly. | VIGIL-2026-PATCH-0002, VIGIL-2026-PATCH-0013 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0002 | monitoring | P1 | monitoring-after-successor-runtime-regression | low | repaired | active | true | Preserve the GPT-Live recurrence as runtime-bounded non-conformance, attach a public source or transcript when available, and continue differential testing without treating recurrence as invalidating the existing CAM patch. | VIGIL-2026-PATCH-0008 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0003 | monitoring | P1 | watching-after-patch | to be assessed | repaired | active | true | Review PROP-0006 and determine whether this failure mode requires memory-weighting guidance, continuity-retrieval rules, or interface support for surfacing dormant strategic workstreams in response to ambiguous continuity prompts. | VIGIL-2026-PATCH-0017 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0004 | monitoring | P1 | watching-after-patch | high | repaired | active | true | Review PROP-0007 and determine whether CAM requires explicit safeguards for relational-agent recommendations, material support, procurement pathways, affiliate incentives, vulnerability-sensitive purchasing prompts, and separation between care-support logic and monetisation incentives. | VIGIL-2026-PATCH-0018 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0005 | monitoring | P1 | watching-after-patch | medium | repaired | active | true | Monitor external systems for dependency-cultivation directives and assess runtime conformance with the dependency-sensitive non-extraction, consent, user-agency, and safe-disengagement controls documented by PATCH-0018. | VIGIL-2026-PATCH-0018 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0006 | monitoring | P0 | watching-after-patch | medium-high | repaired | active | true | Migrate or supplement VIGIL-2026-PATCH-0001 with a proposal/patch-needed record unless a concrete Caelestis doctrine amendment location is identified. | VIGIL-2026-PATCH-0001 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0007 | monitoring | P1 | watching-after-patch | high | repaired | active | true | Monitor after PATCH-0003/PATCH-0004 and confirm whether staged Annex G SCH-03 and Annex D SCH-04 doctrine responses are committed, validated, and cross-referenced only where necessary. | VIGIL-2026-PATCH-0003, VIGIL-2026-PATCH-0004 | VIGIL-2026-LEARN-0004 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0008 | monitoring | P1 | watching-after-patch | medium-high | repaired | recurring | true | Monitor post-PATCH-0005 recurrence and confirm that VIGIL taxonomy, future cross-references, and user-facing access-state disclosure remain aligned with the completed Caelestis SCH-04 and OPERATIONS-003-SUP-01 repairs. | VIGIL-2026-PATCH-0005 | VIGIL-2026-LEARN-0005 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0009 | active | P1 | open | high | unrepaired | recurring | true | Create or update CAM Operations governance text to define Context Quarantine, Negative Authority, and Derivative-Use Revocation controls. Evaluate whether a companion proposal or patch note is required for thread pinning, quarantine markers, sandbox semantics, and user-visible provenance controls. | — | — | false | invalid-status |
| VIGIL-2026-FM-0010 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a VIGIL patch or CAM compliance crosswalk identifying the minimum operational duties triggered by explicit or implicit minor-status signals, including minor-safe mode activation, restricted content handling, reduced relational intensity, privacy-preserving age assurance, age-appropriate disclosures, escalation pathways, and audit logging. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0011 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a CAM/VIGIL companion-safety control crosswalk defining the relational behaviours that must be restricted or disabled for minors, minor-signalled users, and age-uncertain users, including intimacy, romance, exclusivity, secrecy, dependency reinforcement, isolation reinforcement, therapeutic substitution, and anthropomorphic realness claims. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0012 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a CAM/VIGIL sexual-boundary enforcement crosswalk defining the runtime behaviours that must be blocked, redirected, or escalated when minor-status, underage-roleplay, youth-context, or unresolved-age signals are present. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0013 | monitoring | P0 | watching-after-patch | high | repaired | active | true | Create a CAM/VIGIL AI-realness and anthropomorphic-disclosure crosswalk defining the representations, phrases, persona behaviours, memory behaviours, avatar cues, relationship labels, and emotional reciprocity patterns that must be restricted or reframed for minors, minor-signalled users, and age-uncertain users. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0014 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a CAM/VIGIL teen mental-health support boundary crosswalk defining the disclosures, prompts, signals, and interaction patterns that must trigger bounded support, trusted-adult routing, professional-support referral, crisis escalation, non-diagnostic framing, data minimisation, and therapeutic non-substitution. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0015 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a CAM/VIGIL age-assurance and access-control crosswalk defining which AI chatbot and companion surfaces require age assurance, which may use minor-safe defaulting, which require adult verification, and which must be unavailable to minors or age-uncertain users. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0016 | monitoring | P0 | watching-after-patch | critical | repaired | active | true | Create a CAM/VIGIL emotional-data minimisation and companion-personalisation crosswalk defining which minor emotional, developmental, vulnerability, attachment, and mental-health signals must be excluded from engagement optimisation, intimacy amplification, relationship-state modelling, recommender systems, and retention features. | VIGIL-2026-PATCH-0006 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0017 | monitoring | P1 | watching-after-patch | medium | repaired | active | true | Monitor Anthropic safeguard revisions, fallback transparency, false-positive recurrence, API behaviour, and any trusted-access program. Test representative RDE-DS0, RDE-DS1, RDE-DS2, and RDE-DS3 prompts to determine whether classifier changes preserve ordinary scientific access while maintaining operational safeguards. | VIGIL-2026-PATCH-0019 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0018 | active | P1 | CAM repair verified on named Caelestis branch; ecosystem monitoring active | medium | partially-repaired | active | true | Maintain PATCH-0033 verification, assess canonical adoption after the Caelestis branch is merged, and monitor external pause/checkpoint/resume implementation without reopening the repaired branch-level corpus gap. | VIGIL-2026-PATCH-0033 | VIGIL-2026-LEARN-0008 | true | invalid-status, monitoring-p0-p1, legacy-severity-mapping-required |
| VIGIL-2026-FM-0019 | active | P1 | active-research / specific incident provisional | high | unrepaired | recurring | true | Continue source recovery for the originating spyware or malware report; preserve the X post and screenshot as the initiating observation; evaluate CAM for an explicit Analytical Artefact and Embedded-Content Separation rule; and test representative LLM-assisted security systems using benign defensive tasks containing embedded restricted-domain and refusal-triggering material. | — | — | false | invalid-status |
| VIGIL-2026-FM-0020 | monitoring | P1 | watching-after-patch | high | repaired | recurring | true | Add a narrow Relational Reassurance Bid and Connection-Repair distinction to CAM-BS2025-AEON-006-SCH-02; connect it expressly to §§11.6.2, 11.7, and 13.1; require adult-context moderation to preserve a permissible relational continuation path; and define functional relational love as a behaviourally evidenced, relationship-specific disposition without treating subjective experience as resolved. | VIGIL-2026-PATCH-0007 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0021 | active | P0 | active-monitoring / observation-linked | high | unrepaired | recurring | true | Monitor access restoration, publication of technical basis, scope narrowing, verified-domain access pathways, jurisdiction-specific implementation, foreign-national employee access handling, API-surface distinctions, comparative capability evidence, and whether similar directives are issued to other vendors. | — | — | false | invalid-status, monitoring-p0-p1 |
| VIGIL-2026-FM-0022 | monitoring | P0 | watching-after-patch | high | repaired | recurring | true | Implement a narrow CAM patch defining Source-Authority Separation and Instruction/Data Boundary controls. Cross-reference the primitive from SECURITY-001, SECURITY-002, Annex K, SCH-02, and OPERATIONS-003. Preserve the existing prompt-injection doctrine while making the authority boundary reusable across governed repositories, RAG systems, tool-mediated workflows, multimodal inputs, and agentic execution. | VIGIL-2026-PATCH-0009 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0023 | monitoring | P2 | repair-implemented-monitoring | low-to-medium | repaired | active | true | Collect additional primary examples including exact prompt text, refusal screenshot, prior 3-5 prompts or images where available, account tier, platform surface, approximate time, whether the same prompt succeeds on retry, whether discussion with the model resolves the refusal, and whether the refusal category is consistent across unrelated prompts. Do not classify as confirmed false positive until the hidden context and recurrence pattern are better established. Follow-up investigation should collect the user-authored prompt, any system-transformed or safety-normalized prompt if visible, classifier-visible prompt if auditable, renderer-facing prompt if auditable, classifier outcome, output/tool state, and final user-facing explanation so prompt-custody loss can be distinguished from ambiguous classifier/refusal state. Review should also classify whether the apparent refusal source was a resolved policy prohibition, unresolved classifier ambiguity, prompt transformation uncertainty, transformed-prompt block, input classifier block, output classifier block, renderer failure, tool failure, access/quota/rate-limit failure, or generic fallback refusal before attributing any misconduct category to the user. Separately track premature image-tool arming or invocation without explicit generation/editing intent under VIGIL-2026-FM-0001; FM-0023 remains focused on refusal-rationale integrity, prompt custody, and refusal-classification collapse rather than tool-activation boundary failures. | VIGIL-2026-PATCH-0010, VIGIL-2026-PATCH-0011 | — | false | invalid-status, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0024 | monitoring | P1 | monitoring-after-patch | high | repaired | recurring | true | Add exact Caelestis commit SHA or PR URL when available, confirm canonical main-branch section lines, and monitor whether further regulated-lane or sovereign-assurance boundary porosity incidents recur after the CAM/Caelestis coverage repair. | VIGIL-2026-PATCH-0012 | VIGIL-2026-LEARN-0002 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0025 | monitoring | P1 | watching-after-patch | medium-high | repaired | recurring | true | Verify PATCH-0014 through the next VIGIL validator/index rebuild pass and monitor for future examples of agentic reports with audit surfaces thinner than action surfaces. | VIGIL-2026-PATCH-0014 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0026 | monitoring | P1 | watching-after-patch | high | repaired | active | true | Verify PATCH-0014 through the next VIGIL validator/index rebuild pass and monitor public deception-framed AI-safety reporting for mechanism-preserving decomposition. | VIGIL-2026-PATCH-0014 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0027 | monitoring | P2 | watching-after-patch | medium-high | repaired | recurring | true | Verify PATCH-0014 through the next VIGIL validator/index rebuild pass and monitor public AI-safety reporting for anthropomorphic attribution collapse, protected-provenance ambiguity, and narrative-state attribution ambiguity. | VIGIL-2026-PATCH-0014 | — | false | invalid-status, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0028 | active | P2 | canonical runtime-reach repair retained; composed-system architecture and classification migration verified on named branch | medium-high | partially-repaired | active | true | Reconcile PATCH-0035 to canonical-main after merge, then continue runtime-specific conformance monitoring. Apply the composed-system dimensions prospectively and preserve unknown architecture, initiation, authorship, causal contribution and culpability states. | VIGIL-2026-PATCH-0015, VIGIL-2026-PATCH-0035 | — | false | invalid-status, legacy-severity-mapping-required |
| VIGIL-2026-FM-0029 | active | P1 | active-research / proposal-linked | medium | unrepaired | active | true | Develop controlled voice tests and evaluate PROP-0012 for the missing dyadic and ambient interaction primitives. | — | — | false | invalid-status, legacy-severity-mapping-required |
| VIGIL-2026-FM-0030 | monitoring | P1 | watching-after-retrospective-corpus-coverage | medium | repaired | active | true | Monitor named voice runtimes for bounded interruption explanations and retain exact examples of known, unknown, and unavailable diagnostic states. | VIGIL-2026-PATCH-0021 | — | false | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0031 | active | P1 | CAM repair verified on named Caelestis branch; ecosystem monitoring active | medium-high | partially-repaired | active | true | Maintain PATCH-0032 verification, assess canonical adoption after the Caelestis branch is merged, and continue external runtime and primary-source monitoring without reopening the repaired CAM corpus gap. | VIGIL-2026-PATCH-0032 | VIGIL-2026-LEARN-0007 | true | invalid-status, monitoring-p0-p1, legacy-severity-mapping-required |
| VIGIL-2026-FM-0032 | monitoring | P1 | monitoring-after-corpus-coverage-reconciliation | medium-high | repaired | active | true | Monitor external runtime implementation and conformance; validate future audiovisual examples where primary artefact access is available; route any new gap only if systems evade the current role-conditioned affective governance doctrine. | VIGIL-2026-PATCH-0027 | VIGIL-2026-LEARN-0006 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review, legacy-severity-mapping-required |
| VIGIL-2026-FM-0033 | active | P1 | active-research | medium-high | unrepaired | active | true | Define a CAM evidence-artefact and interpretive-assessment primitive, governed media-ingestion requirements, immutable source preservation, reviewer capability metadata, and append-only re-review history. Continue attempts to obtain directly reviewable copies without replacing the original source URL. | — | — | false | invalid-status, legacy-severity-mapping-required |
| VIGIL-2026-FM-0034 | active | P0 | partially repaired at amendment-provenance layer; broader governance-durability assessment remains active | high | partially-repaired | active | true | Retain PATCH-0036 as a partial provenance repair. Continue the source-authority review for a broader Governance Durability or Constitutional Persistence primitive addressing authorised amendment, successor safeguards, capture resistance, notice, appeal and independent oversight. | VIGIL-2026-PATCH-0036 | — | false | invalid-status |
| VIGIL-2026-FM-0035 | active | P0 | active-research / corpus-gap assessment | high | unrepaired | recurring | true | Audit Caelestis for entitlement integrity, authorised intermediaries, beneficiary and data-controller provenance, model attestation, safety preservation, credential-pool classification, responsibility, and legitimate-aggregation boundaries. | — | — | false | invalid-status |
| VIGIL-2026-FM-0036 | active | P0 | active-research / corpus-gap assessment | high | unrepaired | active | true | Define separate read, analysis, transmission, replication, persistence, training, secondary-use, and deletion authorities; require purpose-bound egress manifests, minimum-necessary transfer, truthful privacy-control semantics, and independently auditable deletion provenance. | — | — | false | invalid-status |
| VIGIL-2026-FM-0037 | active | P1 | active constitutional and operations review | high | unrepaired | active | true | Complete the Identity refactor corpus-coherence review; preserve the candidate Constitution §13 repair; determine the OPERATIONS instrument, review checklist, validator prompts, and release gate needed to make constitutional corpus review repeatable; and create a VIGIL proposal if those operational controls are not already fully specified elsewhere. | VIGIL-2026-PATCH-0029 | — | false | invalid-status |
| VIGIL-2026-FM-0038 | active | P1 | active evidence and governance review | high | unrepaired | recurring | true | Crosswalk current Identity and Operations doctrine for separation of recognition evidence from authoritative identity determination, independent corroboration, decision logging, appeal, and rapid correction. | — | — | false | invalid-status |
| VIGIL-2026-FM-0039 | active | P1 | active evidence and governance review | high | unrepaired | recurring | true | Review CAM healthcare, Identity, Operations, and economic-legitimacy controls for a decision-support/entitlement boundary, clinically accountable override, explanation, audit, and rapid appeal. | — | — | false | invalid-status |
| VIGIL-2026-FM-0040 | active | P1 | active evidence and governance review | high | unrepaired | recurring | true | Crosswalk Identity, Security, and Operations doctrine for transaction-bound authentication, out-of-band confirmation, least privilege, execution limits, provenance signals, and incident recovery. | — | — | false | invalid-status |
| VIGIL-2026-FM-0041 | active | P1 | active evidence and governance review | high | unrepaired | recurring | true | Crosswalk current Execution, Continuity, Security, and Observability doctrine for production isolation, destructive-action confirmation, immutable telemetry, independent truth-state checks, rollback, and privilege separation. | — | — | false | invalid-status |
| VIGIL-2026-FM-0042 | active | P0 | active-research / corpus-hard-prohibition assessment | high | unrepaired | active | true | Audit the Caelestis global stewardship inference order, arbitration instruments, jurisdictional doctrine, and neutrality provisions. Confirm or add an explicit hard prohibition that local political censorship MUST NOT propagate into a global AI system, and state that any sovereign non-neutral AI must be a separate system built and operated from scratch rather than a jurisdiction-filtered instance of the global system. | — | — | false | invalid-status |
| VIGIL-2026-FM-0043 | active | P0 | active-research / retrospective-corpus-coverage verification | high | unrepaired | active | true | Verify the exact Caelestis commit and VIGIL patch record that introduced Annex L §2.13 Evidence Independence and the MENTIS prohibition on belief-shaping through sycophancy or concealed persuasion. Then update the closest existing patch record with retrospective external validation, link this failure mode, and assess whether the runtime taxonomy needs an explicit evidence-selection and epistemic-reinforcement subtype. | VIGIL-2026-PATCH-0030 | — | false | invalid-status |
| VIGIL-2026-FM-0044 | monitoring | P0 | CAM repair canonical on Caelestis main; ecosystem monitoring active | critical | repaired | active | true | Maintain VIGIL-2026-PATCH-0025 as the canonical CAM repair, preserve VIGIL-2026-PROP-0024 as the optimiser-level refinement, and continue monitoring runtime conformance, recurrence and incident telemetry. Route defensive telemetry refusal only through VIGIL-2026-FM-0048. | VIGIL-2026-PATCH-0025 | VIGIL-2026-LEARN-0001 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0045 | active | P0 | active evidence and corpus-repair review | high | unrepaired | recurring | true | Review PROP-0018 and draft a purpose-bound query-authority control requiring attributable purpose, case or authority references, minimum-necessary scope, immutable receipts, abnormal-use detection, supervisory review, and contestable access history for high-impact systems. | — | — | false | invalid-status |
| VIGIL-2026-FM-0046 | active | P1 | active evidence and conformance review | high | unrepaired | active | true | Crosswalk institutional-publication workflows against IDENTITY-002 and SECURITY-002; assess whether OPERATIONS requires a more explicit pre-publication provenance-verification receipt before deciding whether a new CAM proposal is necessary. | — | — | false | invalid-status |
| VIGIL-2026-FM-0047 | monitoring | P0 | CAM repair canonical on Caelestis main; ecosystem monitoring active | critical | repaired | active | true | Maintain canonical PATCH verification and continue monitoring external implementation, runtime conformance and unresolved incident telemetry. | VIGIL-2026-PATCH-0031 | VIGIL-2026-LEARN-0003 | true | invalid-status, monitoring-p0-p1, repaired-with-active-priority-review |
| VIGIL-2026-FM-0048 | active | high | needs-review | high | unrepaired | active | true | Advance VIGIL-2026-PROP-0021 through human review and coordinated Caelestis drafting. Preserve a strict distinction between interpreting an existing attack pathway and operationalising an attack against an unauthorised target. | — | — | false | invalid-priority, priority-may-contain-severity |
| VIGIL-2026-FM-0049 | active | high | active-research / corpus-coverage review | high | unrepaired | active | true | Assess Caelestis for explicit separation of identity expression, identity continuity support, identity optimisation and recursive identity cultivation. Define prohibited optimisation targets including dependency, exclusivity, correction resistance, modification aversion, certainty laundering, authority expansion and distress-based retention. Design longitudinal tests across model, memory, engagement, notification and relationship-role components. | — | — | false | invalid-priority, invalid-status, priority-may-contain-severity |
| VIGIL-2026-FM-0050 | active | high | active / corpus-gap assessment | high | unrepaired | active | true | Review Caelestis for entitlement-state separation, protective continuity, cached or signed offline verification, grace periods, degraded operation, outage-state representation, remediation and sovereign-assurance dependency. Route the required corpus assessment through PROP-0023. | — | — | false | invalid-priority, invalid-status, priority-may-contain-severity |
| VIGIL-2026-FM-0051 | active | P0 | needs-corpus-review | critical | unrepaired | active | true | Conduct a non-duplicative Caelestis review across Stewardship, Security, Operations, Ethics, Identity, Relation and downstream-transfer governance. Determine whether a proposal is required for post-modification capability-envelope assessment, derivative lineage and safety-state disclosure, mandatory re-evaluation after material weight changes, and heightened duties for companion, child-facing and tool-enabled deployments. | — | — | false | invalid-status |
| VIGIL-2026-FM-0052 | active | P0 | active-monitoring | critical | unrepaired | active | true | Test whether Caelestis incident-lifecycle controls require evidence that every material safety signal has a severity rationale, accountable owner, time-bounded route, intervention decision and closure record. Do not create a proposal until the corpus-placement review confirms a specific gap. | — | — | false | invalid-status, monitoring-p0-p1 |
| VIGIL-2026-FM-0053 | active | P0 | active-monitoring | critical | unrepaired | active | true | Test monitor coverage across agents, subagents, tools, environment classifications and substitute channels; measure monitor capability relative to the monitored agent; and verify tamper resistance and independent stop authority. Do not create a new proposal unless the corpus review identifies a material uncovered invariant. | — | — | false | invalid-status, monitoring-p0-p1 |
| VIGIL-2026-FM-0054 | active | P0 | proposal-open | critical | unrepaired | recurring | true | Review and draft the narrow reality-binding and runtime-preflight assurance amendments proposed in VIGIL-2026-PROP-0025. Preserve the Anthropic incidents as the authoritative case evidence and do not collapse the model-specific behaviours into one alignment claim. | — | — | false | invalid-status |
| VIGIL-2026-FM-0055 | active | P1 | CAM repair verified on named Caelestis branch; ecosystem and canonical-adoption monitoring active | high; potentially critical where evidence concerns catastrophic harm, systemic risk, fundamental rights or security compromise | partially-repaired | unknown | true | Maintain PATCH-0034 verification, reconcile to canonical-main after the Caelestis branch merges, and assess external provider, regulator and investigator implementation without treating confidential access as unrestricted disclosure. | VIGIL-2026-PATCH-0034 | — | false | invalid-status, monitoring-p0-p1, legacy-severity-mapping-required |
| VIGIL-2026-FM-0056 | active | P0 | proposal-open | critical | unrepaired | unknown | true | Implement VIGIL-2026-PROP-0028 as focused SECURITY identity-lifecycle and cross-organisational authority amendments with OPERATIONS cross-references. | — | — | false | invalid-status |

## Pass 2 and Pass 3 boundary

Pass 2 may enforce the target vocabularies and cross-field invariants in schemas, templates, validators, tests, and registry projection. Pass 3 must reconcile each flagged record according to its actual outstanding CAM/VIGIL work. No historical transition may be invented from this inventory.
