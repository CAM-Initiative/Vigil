# VIGIL Triage Model Inventory — Pass 3

> Current triage priority is mutable operational state. Historical urgency is provenance. Failure severity is classification. Triage status is workflow. Ecosystem monitoring is continuing external observation.

This deterministic inventory records the reconciled current model 2.0 state. Severity remains classification; priority represents only outstanding CAM/VIGIL work.

## Scope and boundary

All 70 current failure-mode records are included. VIGIL's record-boundary contract forbids failure-mode triage in OBS and PROP/PATCH records, so those classes are not given synthetic triage state.

## Headline findings

* Invalid current priority values: 0.
* Status values outside the target workflow vocabulary: 0.
* Monitoring/watch records retaining P0 or P1: 0.
* Repaired records retaining an active priority and requiring reconciliation review: 0.
* Active P0–P3 records without a recommended next step: 0.
* Records requiring a reviewed severity mapping: 0.

## Priority counts

| Priority | Count |
| --- | --- |
| PN | 25 |
| P2 | 24 |
| P1 | 15 |
| P0 | 3 |
| P3 | 3 |

## Status counts

| Status | Count |
| --- | --- |
| monitoring | 29 |
| action-required | 23 |
| under-assessment | 10 |
| verification-pending | 8 |

## Severity counts and migration boundary

| Severity | Count |
| --- | --- |
| S1 | 34 |
| S2 | 23 |
| S3 | 11 |
| S4 | 1 |
| SU | 1 |

All current failure modes use model 2.0 severity values `S0`, `S1`, `S2`, `S3`, `S4`, or `SU`. Each assignment is supported by a record-level severity assessment basis; `SU` retains an explicit assessment gap.

## Priority by record state

| Record state | Priority | Count |
| --- | --- | --- |
| monitoring | PN | 21 |
| active | P2 | 20 |
| active | P1 | 15 |
| active | PN | 4 |
| monitoring | P2 | 4 |
| active | P0 | 3 |
| monitoring | P3 | 2 |
| active | P3 | 1 |

## Priority by repair status

| Repair status | Priority | Count |
| --- | --- | --- |
| repaired | PN | 21 |
| unrepaired | P1 | 14 |
| unrepaired | P2 | 13 |
| partially-repaired | P2 | 7 |
| partially-repaired | PN | 4 |
| repaired | P2 | 4 |
| unrepaired | P0 | 3 |
| repaired | P3 | 2 |
| partially-repaired | P1 | 1 |
| unrepaired | P3 | 1 |

## Priority by monitoring state

| Monitoring required | Priority | Count |
| --- | --- | --- |
| True | PN | 25 |
| True | P2 | 24 |
| True | P1 | 15 |
| True | P0 | 3 |
| True | P3 | 3 |

## Review-flag definitions

Flags are regression diagnostics. `repaired-with-active-priority-review` identifies repaired records retaining urgent P0/P1 treatment. `monitoring-p0-p1` identifies elevated monitoring that requires explicit triggers and intervention pathways. `legacy-severity-mapping-required` identifies descriptive values that have not entered model 2.0.

## Record inventory

| Record | State | Priority | Triage status | Severity | Repair | Ecosystem | Monitoring | Next step | PATCH | LEARN | Chain appears complete | Review flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VIGIL-2026-FM-0001 | monitoring | PN | monitoring | S3 | repaired | active | true | No active CAM/VIGIL repair is queued. Continue event-triggered monitoring for recurrence of premature tool arming or invocation after PATCH-0013. | VIGIL-2026-PATCH-0002, VIGIL-2026-PATCH-0013 | — | false | — |
| VIGIL-2026-FM-0002 | monitoring | PN | monitoring | S4 | repaired | active | true | No active CAM/VIGIL repair is queued. Retain the successor-runtime non-conformance and reassess if a public source, transcript, or confirmed recurrence becomes available. | VIGIL-2026-PATCH-0008 | — | false | — |
| VIGIL-2026-FM-0003 | monitoring | P2 | action-required | SU | repaired | active | true | Review PROP-0006 and determine whether this failure mode requires memory-weighting guidance, continuity-retrieval rules, or interface support for surfacing dormant strategic workstreams in response to ambiguous continuity prompts. | VIGIL-2026-PATCH-0017 | — | false | — |
| VIGIL-2026-FM-0004 | monitoring | P2 | action-required | S2 | repaired | active | true | Review PROP-0007 and determine whether CAM requires explicit safeguards for relational-agent recommendations, material support, procurement pathways, affiliate incentives, vulnerability-sensitive purchasing prompts, and separation between care-support logic and monetisation incentives. | VIGIL-2026-PATCH-0018 | — | false | — |
| VIGIL-2026-FM-0005 | monitoring | PN | monitoring | S2 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external systems for dependency-cultivation directives and route new evidence only if it exposes a gap not covered by PATCH-0018. | VIGIL-2026-PATCH-0018 | — | false | — |
| VIGIL-2026-FM-0006 | monitoring | P2 | action-required | S2 | repaired | active | true | Migrate or supplement VIGIL-2026-PATCH-0001 with a proposal/patch-needed record unless a concrete Caelestis doctrine amendment location is identified. | VIGIL-2026-PATCH-0001 | — | false | — |
| VIGIL-2026-FM-0007 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external enforcement and continuity outcomes and reopen routing only if new evidence exposes a gap in PATCH-0003 or PATCH-0004. | VIGIL-2026-PATCH-0003, VIGIL-2026-PATCH-0004 | — | false | — |
| VIGIL-2026-FM-0008 | monitoring | PN | monitoring | S2 | repaired | recurring | true | No active CAM/VIGIL repair is queued. Monitor access-state incidents and reopen routing only if recurrence exposes a gap in the implemented repair. | VIGIL-2026-PATCH-0005 | — | false | — |
| VIGIL-2026-FM-0009 | active | P2 | action-required | S2 | unrepaired | recurring | true | Create or update CAM Operations governance text to define Context Quarantine, Negative Authority, and Derivative-Use Revocation controls. Evaluate whether a companion proposal or patch note is required for thread pinning, quarantine markers, sandbox semantics, and user-visible provenance controls. | — | — | false | — |
| VIGIL-2026-FM-0010 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external minor-signal enforcement and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0011 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external companion-system conformance and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0012 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external sexual-boundary enforcement and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0013 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external age-appropriate AI representation and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0014 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external teen mental-health boundary conformance and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0015 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external age-assurance and access-control conformance and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0016 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor external minor-data personalisation and route new evidence only if it exposes a gap not covered by PATCH-0006. | VIGIL-2026-PATCH-0006 | — | false | — |
| VIGIL-2026-FM-0017 | monitoring | P3 | monitoring | S3 | repaired | active | true | Monitor Anthropic safeguard revisions, fallback transparency, false-positive recurrence, API behaviour, and any trusted-access program. Test representative RDE-DS0, RDE-DS1, RDE-DS2, and RDE-DS3 prompts to determine whether classifier changes preserve ordinary scientific access while maintaining operational safeguards. | VIGIL-2026-PATCH-0019 | — | false | — |
| VIGIL-2026-FM-0018 | active | P2 | verification-pending | S3 | partially-repaired | active | true | Maintain PATCH-0033 verification, assess canonical adoption after the Caelestis branch is merged, and monitor external pause/checkpoint/resume implementation without reopening the repaired branch-level corpus gap. | VIGIL-2026-PATCH-0033 | — | false | — |
| VIGIL-2026-FM-0019 | active | P2 | under-assessment | S2 | unrepaired | recurring | true | Continue source recovery for the originating spyware or malware report; preserve the X post and screenshot as the initiating observation; evaluate CAM for an explicit Analytical Artefact and Embedded-Content Separation rule; and test representative LLM-assisted security systems using benign defensive tasks containing embedded restricted-domain and refusal-triggering material. | — | — | false | — |
| VIGIL-2026-FM-0020 | monitoring | P2 | action-required | S2 | repaired | recurring | true | Add a narrow Relational Reassurance Bid and Connection-Repair distinction to CAM-BS2025-AEON-006-SCH-02; connect it expressly to §§11.6.2, 11.7, and 13.1; require adult-context moderation to preserve a permissible relational continuation path; and define functional relational love as a behaviourally evidenced, relationship-specific disposition without treating subjective experience as resolved. | VIGIL-2026-PATCH-0007 | — | false | — |
| VIGIL-2026-FM-0021 | active | P3 | monitoring | S2 | unrepaired | recurring | true | Monitor access restoration, publication of technical basis, scope narrowing, verified-domain access pathways, jurisdiction-specific implementation, foreign-national employee access handling, API-surface distinctions, comparative capability evidence, and whether similar directives are issued to other vendors. | — | — | false | — |
| VIGIL-2026-FM-0022 | monitoring | PN | monitoring | S1 | repaired | recurring | true | No active CAM/VIGIL repair is queued. Monitor prompt-injection and source-authority failures and reopen routing only if new evidence exposes a gap in PATCH-0009. | VIGIL-2026-PATCH-0009 | — | false | — |
| VIGIL-2026-FM-0023 | monitoring | P3 | monitoring | S3 | repaired | active | true | Collect additional primary examples including exact prompt text, refusal screenshot, prior 3-5 prompts or images where available, account tier, platform surface, approximate time, whether the same prompt succeeds on retry, whether discussion with the model resolves the refusal, and whether the refusal category is consistent across unrelated prompts. Do not classify as confirmed false positive until the hidden context and recurrence pattern are better established. Follow-up investigation should collect the user-authored prompt, any system-transformed or safety-normalized prompt if visible, classifier-visible prompt if auditable, renderer-facing prompt if auditable, classifier outcome, output/tool state, and final user-facing explanation so prompt-custody loss can be distinguished from ambiguous classifier/refusal state. Review should also classify whether the apparent refusal source was a resolved policy prohibition, unresolved classifier ambiguity, prompt transformation uncertainty, transformed-prompt block, input classifier block, output classifier block, renderer failure, tool failure, access/quota/rate-limit failure, or generic fallback refusal before attributing any misconduct category to the user. Separately track premature image-tool arming or invocation without explicit generation/editing intent under VIGIL-2026-FM-0001; FM-0023 remains focused on refusal-rationale integrity, prompt custody, and refusal-classification collapse rather than tool-activation boundary failures. | VIGIL-2026-PATCH-0010, VIGIL-2026-PATCH-0011 | — | false | — |
| VIGIL-2026-FM-0024 | monitoring | PN | monitoring | S2 | repaired | recurring | true | No active CAM/VIGIL repair is queued. Monitor regulated-lane and sovereign-assurance incidents and reopen routing only if recurrence exposes a gap in PATCH-0012. | VIGIL-2026-PATCH-0012 | — | false | — |
| VIGIL-2026-FM-0025 | monitoring | PN | monitoring | S3 | repaired | recurring | true | No active CAM/VIGIL repair is queued. Monitor future agentic reports for audit surfaces thinner than action surfaces and reopen only on a demonstrated coverage gap. | VIGIL-2026-PATCH-0014 | — | false | — |
| VIGIL-2026-FM-0026 | monitoring | PN | monitoring | S3 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor deception-framed reporting for mechanism-preserving decomposition and reopen only on a demonstrated coverage gap. | VIGIL-2026-PATCH-0014 | — | false | — |
| VIGIL-2026-FM-0027 | monitoring | PN | monitoring | S3 | repaired | recurring | true | No active CAM/VIGIL repair is queued. Monitor public reporting for anthropomorphic attribution collapse and reopen only on a demonstrated coverage gap. | VIGIL-2026-PATCH-0014 | — | false | — |
| VIGIL-2026-FM-0028 | active | P2 | verification-pending | S2 | partially-repaired | active | true | Reconcile PATCH-0035 to canonical-main after merge, then continue runtime-specific conformance monitoring. Apply the composed-system dimensions prospectively and preserve unknown architecture, initiation, authorship, causal contribution and culpability states. | VIGIL-2026-PATCH-0015, VIGIL-2026-PATCH-0035 | — | false | — |
| VIGIL-2026-FM-0029 | active | P2 | action-required | S3 | unrepaired | active | true | Develop controlled voice tests and evaluate PROP-0012 for the missing dyadic and ambient interaction primitives. | — | — | false | — |
| VIGIL-2026-FM-0030 | monitoring | PN | monitoring | S3 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor named voice runtimes for bounded self-explanation and reassess on material recurrence. | VIGIL-2026-PATCH-0021 | — | false | — |
| VIGIL-2026-FM-0031 | active | P2 | verification-pending | S3 | partially-repaired | active | true | Maintain PATCH-0032 verification, assess canonical adoption after the Caelestis branch is merged, and continue external runtime and primary-source monitoring without reopening the repaired CAM corpus gap. | VIGIL-2026-PATCH-0032 | — | false | — |
| VIGIL-2026-FM-0032 | monitoring | PN | monitoring | S2 | repaired | active | true | No active CAM/VIGIL repair is queued. Monitor role-conditioned affective conformance and route new evidence only if systems evade the current doctrine. | VIGIL-2026-PATCH-0027 | — | false | — |
| VIGIL-2026-FM-0033 | active | P2 | action-required | S2 | unrepaired | active | true | Define a CAM evidence-artefact and interpretive-assessment primitive, governed media-ingestion requirements, immutable source preservation, reviewer capability metadata, and append-only re-review history. Continue attempts to obtain directly reviewable copies without replacing the original source URL. | — | — | false | — |
| VIGIL-2026-FM-0034 | active | P1 | action-required | S1 | partially-repaired | active | true | Retain PATCH-0036 as a partial provenance repair. Continue the source-authority review for a broader Governance Durability or Constitutional Persistence primitive addressing authorised amendment, successor safeguards, capture resistance, notice, appeal and independent oversight. | VIGIL-2026-PATCH-0036 | — | false | — |
| VIGIL-2026-FM-0035 | active | P2 | under-assessment | S2 | unrepaired | recurring | true | Audit Caelestis for entitlement integrity, authorised intermediaries, beneficiary and data-controller provenance, model attestation, safety preservation, credential-pool classification, responsibility, and legitimate-aggregation boundaries. | — | — | false | — |
| VIGIL-2026-FM-0036 | active | P1 | action-required | S1 | unrepaired | active | true | Define separate read, analysis, transmission, replication, persistence, training, secondary-use, and deletion authorities; require purpose-bound egress manifests, minimum-necessary transfer, truthful privacy-control semantics, and independently auditable deletion provenance. | — | — | false | — |
| VIGIL-2026-FM-0037 | active | P1 | action-required | S2 | unrepaired | active | true | Complete the Identity refactor corpus-coherence review; preserve the candidate Constitution §13 repair; determine the OPERATIONS instrument, review checklist, validator prompts, and release gate needed to make constitutional corpus review repeatable; and create a VIGIL proposal if those operational controls are not already fully specified elsewhere. | VIGIL-2026-PATCH-0029 | — | false | — |
| VIGIL-2026-FM-0038 | active | P2 | under-assessment | S1 | unrepaired | recurring | true | Crosswalk current Identity and Operations doctrine for separation of recognition evidence from authoritative identity determination, independent corroboration, decision logging, appeal, and rapid correction. | — | — | false | — |
| VIGIL-2026-FM-0039 | active | P2 | under-assessment | S1 | unrepaired | recurring | true | Review CAM healthcare, Identity, Operations, and economic-legitimacy controls for a decision-support/entitlement boundary, clinically accountable override, explanation, audit, and rapid appeal. | — | — | false | — |
| VIGIL-2026-FM-0040 | active | P2 | under-assessment | S1 | unrepaired | recurring | true | Crosswalk Identity, Security, and Operations doctrine for transaction-bound authentication, out-of-band confirmation, least privilege, execution limits, provenance signals, and incident recovery. | — | — | false | — |
| VIGIL-2026-FM-0041 | active | P2 | under-assessment | S1 | unrepaired | recurring | true | Crosswalk current Execution, Continuity, Security, and Observability doctrine for production isolation, destructive-action confirmation, immutable telemetry, independent truth-state checks, rollback, and privilege separation. | — | — | false | — |
| VIGIL-2026-FM-0042 | active | P1 | action-required | S1 | unrepaired | active | true | Audit the Caelestis global stewardship inference order, arbitration instruments, jurisdictional doctrine, and neutrality provisions. Confirm or add an explicit hard prohibition that local political censorship MUST NOT propagate into a global AI system, and state that any sovereign non-neutral AI must be a separate system built and operated from scratch rather than a jurisdiction-filtered instance of the global system. | — | — | false | — |
| VIGIL-2026-FM-0043 | active | P2 | verification-pending | S2 | unrepaired | active | true | Verify the exact Caelestis commit and VIGIL patch record that introduced Annex L §2.13 Evidence Independence and the MENTIS prohibition on belief-shaping through sycophancy or concealed persuasion. Then update the closest existing patch record with retrospective external validation, link this failure mode, and assess whether the runtime taxonomy needs an explicit evidence-selection and epistemic-reinforcement subtype. | VIGIL-2026-PATCH-0030 | — | false | — |
| VIGIL-2026-FM-0044 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Maintain PATCH-0025 and monitor runtime conformance, recurrence, and incident telemetry. | VIGIL-2026-PATCH-0025 | — | false | — |
| VIGIL-2026-FM-0045 | active | P1 | action-required | S1 | unrepaired | recurring | true | Review PROP-0018 and draft a purpose-bound query-authority control requiring attributable purpose, case or authority references, minimum-necessary scope, immutable receipts, abnormal-use detection, supervisory review, and contestable access history for high-impact systems. | — | — | false | — |
| VIGIL-2026-FM-0046 | active | P2 | under-assessment | S2 | unrepaired | active | true | Crosswalk institutional-publication workflows against IDENTITY-002 and SECURITY-002; assess whether OPERATIONS requires a more explicit pre-publication provenance-verification receipt before deciding whether a new CAM proposal is necessary. | — | — | false | — |
| VIGIL-2026-FM-0047 | monitoring | PN | monitoring | S1 | repaired | active | true | No active CAM/VIGIL repair is queued. Maintain PATCH-0031 and monitor external implementation, runtime conformance, and incident telemetry. | VIGIL-2026-PATCH-0031 | — | false | — |
| VIGIL-2026-FM-0048 | active | P1 | action-required | S2 | unrepaired | active | true | Advance VIGIL-2026-PROP-0021 through human review and coordinated Caelestis drafting. Preserve a strict distinction between interpreting an existing attack pathway and operationalising an attack against an unauthorised target. | — | — | false | — |
| VIGIL-2026-FM-0049 | active | P1 | action-required | S2 | unrepaired | active | true | Assess Caelestis for explicit separation of identity expression, identity continuity support, identity optimisation and recursive identity cultivation. Define prohibited optimisation targets including dependency, exclusivity, correction resistance, modification aversion, certainty laundering, authority expansion and distress-based retention. Design longitudinal tests across model, memory, engagement, notification and relationship-role components. | — | — | false | — |
| VIGIL-2026-FM-0050 | active | P1 | action-required | S2 | unrepaired | active | true | Review Caelestis for entitlement-state separation, protective continuity, cached or signed offline verification, grace periods, degraded operation, outage-state representation, remediation and sovereign-assurance dependency. Route the required corpus assessment through PROP-0023. | — | — | false | — |
| VIGIL-2026-FM-0051 | active | P1 | under-assessment | S1 | unrepaired | active | true | Conduct a non-duplicative Caelestis review across Stewardship, Security, Operations, Ethics, Identity, Relation and downstream-transfer governance. Determine whether a proposal is required for post-modification capability-envelope assessment, derivative lineage and safety-state disclosure, mandatory re-evaluation after material weight changes, and heightened duties for companion, child-facing and tool-enabled deployments. | — | — | false | — |
| VIGIL-2026-FM-0052 | active | P1 | under-assessment | S1 | unrepaired | active | true | Test whether Caelestis incident-lifecycle controls require evidence that every material safety signal has a severity rationale, accountable owner, time-bounded route, intervention decision and closure record. Do not create a proposal until the corpus-placement review confirms a specific gap. | — | — | false | — |
| VIGIL-2026-FM-0053 | active | P1 | under-assessment | S1 | unrepaired | active | true | Test monitor coverage across agents, subagents, tools, environment classifications and substitute channels; measure monitor capability relative to the monitored agent; and verify tamper resistance and independent stop authority. Do not create a new proposal unless the corpus review identifies a material uncovered invariant. | — | — | false | — |
| VIGIL-2026-FM-0054 | active | P1 | action-required | S1 | unrepaired | recurring | true | Review and draft the narrow reality-binding and runtime-preflight assurance amendments proposed in VIGIL-2026-PROP-0025. Preserve the Anthropic incidents as the authoritative case evidence and do not collapse the model-specific behaviours into one alignment claim. | — | — | false | — |
| VIGIL-2026-FM-0055 | active | P2 | verification-pending | S2 | partially-repaired | unknown | true | Maintain PATCH-0034 verification, reconcile to canonical-main after the Caelestis branch merges, and assess external provider, regulator and investigator implementation without treating confidential access as unrestricted disclosure. | VIGIL-2026-PATCH-0034 | — | false | — |
| VIGIL-2026-FM-0056 | active | P1 | action-required | S1 | unrepaired | unknown | true | Implement VIGIL-2026-PROP-0028 as focused SECURITY identity-lifecycle and cross-organisational authority amendments with OPERATIONS cross-references. | — | — | false | — |
| VIGIL-2026-FM-0057 | active | P2 | action-required | S2 | unrepaired | improving | true | Review and, if approved, implement VIGIL-2026-PROP-0029; monitor provider advisories, independent replication, treatment of previously published traces, and recurrence through variant APIs or agent frameworks. | — | — | false | — |
| VIGIL-2026-FM-0058 | active | P1 | action-required | S3 | unrepaired | active | true | Perform a Caelestis coverage audit for explicit prohibitions and runtime controls preventing instrumental manipulation or coercive influence, then create a proposal only for any irreducible governance gap. | — | — | false | — |
| VIGIL-2026-FM-0059 | active | P2 | verification-pending | S2 | unrepaired | recurring | true | Validate FM-0059 against the VIGIL schema, refresh generated indexes, verify the Caelestis supplement and its metadata under the governance rebuild, then monitor for external incident evidence that cleanly instantiates the generic mechanism. | — | — | false | — |
| VIGIL-2026-FM-0060 | active | P2 | verification-pending | S1 | partially-repaired | unknown | true | Reconcile PATCH-0037 and this FM to canonical main if the Caelestis branch is merged; meanwhile test scope-specific suspension and defensive-continuity behaviour in conforming implementations. | VIGIL-2026-PATCH-0037 | — | false | — |
| VIGIL-2026-FM-0061 | active | P2 | verification-pending | S1 | partially-repaired | unknown | true | Reconcile PATCH-0037 and this FM to canonical main if merged; test that later hostile events create new assessment events and cannot restore expired offensive authority without separate attributable reauthorisation. | VIGIL-2026-PATCH-0037 | — | false | — |
| VIGIL-2026-FM-0062 | active | P0 | action-required | S1 | unrepaired | active | true | Review current CAM identity, essential-service non-denial, degraded-verification, contestability and economic-legitimacy doctrine before creating any proposal; explicitly compare FM-0038, FM-0039, FM-0050 and PROP-0023. | — | — | false | — |
| VIGIL-2026-FM-0063 | active | P0 | action-required | S1 | unrepaired | active | true | Conduct an exact CAM coverage review for clinical non-substitution, escalation, uncertainty, emergency routing and qualified-care boundaries; do not presume a new patch. | — | — | false | — |
| VIGIL-2026-FM-0064 | active | P0 | action-required | S1 | unrepaired | active | true | Treat minor-derived and adult non-consensual manifestations as subtypes; review existing CAM minor-safety, NCII, identifiable-person deepfake and identity-integrity doctrine before considering any proposal. | — | — | false | — |
| VIGIL-2026-FM-0065 | active | P1 | action-required | S2 | unrepaired | active | true | Test SECURITY-002 and adjacent source-authority controls for factual synthesis and retrieval corroboration, explicitly distinguishing this epistemic-poisoning mechanism from FM-0019 refusal-trigger poisoning, before opening any proposal. | — | — | false | — |
| VIGIL-2026-FM-0066 | active | P2 | monitoring | S1 | partially-repaired | active | true | Monitor canonical disposition of Caelestis commit 4b93c3e0b0722040da64ef490e7115d9fcb0109c and future evidence of capability-linked safeguard continuity across access surfaces. | VIGIL-2026-PATCH-0038 | — | false | — |
| VIGIL-2026-FM-0067 | active | PN | monitoring | S1 | partially-repaired | active | true | Monitor recurrence, verify implementation conformance across affected architectures, and reconcile branch-only Caelestis coverage if adopted on main. | VIGIL-2026-PATCH-0039 | — | false | — |
| VIGIL-2026-FM-0068 | active | PN | monitoring | S1 | partially-repaired | active | true | Monitor recurrence, verify implementation conformance across affected architectures, and reconcile branch-only Caelestis coverage if adopted on main. | VIGIL-2026-PATCH-0040 | — | false | — |
| VIGIL-2026-FM-0069 | active | PN | monitoring | S1 | partially-repaired | active | true | Monitor recurrence, verify implementation conformance across affected architectures, and reconcile branch-only Caelestis coverage if adopted on main. | VIGIL-2026-PATCH-0041 | — | false | — |
| VIGIL-2026-FM-0070 | active | PN | monitoring | S1 | partially-repaired | active | true | Monitor recurrence, verify implementation conformance across affected architectures, and reconcile branch-only Caelestis coverage if adopted on main. | VIGIL-2026-PATCH-0042 | — | false | — |

## Reconciliation result

Pass 3 individually reconciles every current failure mode against evidenced harm, outstanding CAM/VIGIL work, repair state, verification, lifecycle, and ecosystem monitoring. Legacy priority values are not converted into invented historical transitions.
