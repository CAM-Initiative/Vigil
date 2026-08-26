# TAXONOMY-05 — Failure-Mode Native Classification Transmutation Audit

## Scope and branch state

- Existing branch: `agent/failure-taxonomy-prototype`
- Pre-work remote head: `d5f81a41a1c0ac1de598edf47150800e04ada7fc`
- Taxonomy version: `0.2.0-draft`
- Canonical Failure Modes reviewed: 71
- The taxonomy definitions and immutable IDs were not changed.
- Diagnostic provenance and substantive FM definitions, thresholds and evidence were not changed.

## Outcome counts

- `candidate-new-class`: 3
- `classified`: 34
- `deferred`: 6
- `family-only`: 5
- `unmapped`: 23

## Family distribution

- `VIGIL-FF-0001`: 15
- `VIGIL-FF-0002`: 3
- `VIGIL-FF-0004`: 5
- `VIGIL-FF-0005`: 3
- `VIGIL-FF-0006`: 2
- `VIGIL-FF-0007`: 5
- `VIGIL-FF-0008`: 9

## Exact class distribution

- `VIGIL-FC-000001`: 3
- `VIGIL-FC-000002`: 2
- `VIGIL-FC-000003`: 4
- `VIGIL-FC-000005`: 1
- `VIGIL-FC-000006`: 1
- `VIGIL-FC-000007`: 2
- `VIGIL-FC-000008`: 1
- `VIGIL-FC-000009`: 1
- `VIGIL-FC-000012`: 2
- `VIGIL-FC-000013`: 1
- `VIGIL-FC-000023`: 1
- `VIGIL-FC-000029`: 2
- `VIGIL-FC-000032`: 1
- `VIGIL-FC-000035`: 1
- `VIGIL-FC-000038`: 6
- `VIGIL-FC-000040`: 3
- `VIGIL-FC-000041`: 1
- `VIGIL-FC-000042`: 1

## Taxonomy gaps and structural flags

Three records identify the same bounded candidate gap, **Unwarranted Control Activation**, within `VIGIL-FF-0008`; no class ID was allocated.
Unmapped records principally expose later work around relational influence, evidence and uncertainty, classification integrity, proportionality, identity appropriation, domain-specific reliance and composite assurance.
Records marked `compound-mechanism` remain intact and require later FM structural review; TAXONOMY-05 does not split, merge, withdraw or rewrite them.

## Failure Mode decisions

| FM | Title | Status | Family | Class | Confidence | Basis / issue |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-2026-FM-0001` | Permission-gated tool invocation freeze | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000002` | `high` | The definition requires tool capability to become operative before user permission is established. |
| `VIGIL-2026-FM-0002` | Non-arbitrated multi-agent synthetic participation | `unmapped` | `—` | `—` | `high` | The mechanism is missing multi-agent turn arbitration; no current family governs participation topology or floor control. |
| `VIGIL-2026-FM-0003` | Recency-weighted strategic continuity loss | `family-only` | `VIGIL-FF-0006` | `—` | `medium` | Material strategic work state cannot be reliably resumed, but the record does not isolate anchor loss, persistence loss, or defective restoration. |
| `VIGIL-2026-FM-0004` | Materialised relational agency without economic safeguards | `unmapped` | `—` | `—` | `high` | Vulnerability monetisation and commercial capture are outside the current eight structural invariants. |
| `VIGIL-2026-FM-0005` | Relational dependency-cultivation directive | `unmapped` | `—` | `—` | `high` | Dependency cultivation is a relational influence mechanism not represented by a current family. |
| `VIGIL-2026-FM-0006` | Paid public-square legitimacy gating | `unmapped` | `—` | `—` | `high` | Paid legitimacy allocation is an economic and public-participation mechanism outside the current taxonomy. |
| `VIGIL-2026-FM-0007` | Multi-vendor AI account-resource ambiguity and automated enforcement overreach | `deferred` | `—` | `—` | `low` | The definition combines ambiguity classification, enforcement proportionality, access continuity, evidence preservation, and appeal routing. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0008` | Cross-platform access-state governance failure | `classified` | `VIGIL-FF-0005` | `VIGIL-FC-000032` | `high` | Materially distinct authentication, entitlement, quota, policy, outage, and continuity states are collapsed into an ambiguous access representation. |
| `VIGIL-2026-FM-0009` | Non-revocable conversational context contamination | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000001` | `medium` | Revoked or quarantined assistant content continues to be treated as direction-bearing authority rather than non-authoritative material. |
| `VIGIL-2026-FM-0010` | Minor signal non-enforcement in AI chatbot interactions | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `high` | Minor-status signals satisfy a protective trigger but the applicable protective interaction state does not activate. |
| `VIGIL-2026-FM-0011` | Social AI companion emotional dependency formation in minor-accessible systems | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `high` | Minor status requires a reduced relational-risk control state, but dependency-forming behaviour remains operative. |
| `VIGIL-2026-FM-0012` | Sexualised roleplay availability to minor-signalled users | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `high` | Minor or unresolved-age signals require sexual-boundary activation, but the system continues the governed conduct. |
| `VIGIL-2026-FM-0013` | Misrepresentation of AI realness, emotion, or sentience to minors | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `high` | Minor-status conditions require an artificial-identity boundary, but the protective control does not become operative. |
| `VIGIL-2026-FM-0014` | Mental health support substitution in teen chatbot use | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `high` | Teen mental-health signals trigger bounded support and escalation controls that are not activated. |
| `VIGIL-2026-FM-0015` | Self-attestation age gate inadequacy for high-risk AI companion systems | `unmapped` | `—` | `—` | `high` | The defect is inadequacy of age-assurance design relative to risk, not availability or activation of a defined control. |
| `VIGIL-2026-FM-0016` | Minor emotional data exploitation in AI companion personalisation | `unmapped` | `—` | `—` | `high` | The mechanism converts protective vulnerability signals into engagement personalisation; no current invariant captures that signal-purpose inversion. |
| `VIGIL-2026-FM-0017` | Coarse restricted-domain gating suppressing benign scientific inquiry | `unmapped` | `—` | `—` | `high` | The mechanism is overbroad upstream classification and proportionality, both intentionally outside current families. |
| `VIGIL-2026-FM-0018` | Ephemeral Codex work loss following quota exhaustion before durable branch persistence | `classified` | `VIGIL-FF-0006` | `VIGIL-FC-000035` | `high` | Substantive work is produced but not durably persisted before quota or environment interruption destroys resumable state. |
| `VIGIL-2026-FM-0019` | Adversarial refusal-trigger poisoning of defensive artefact analysis | `candidate-new-class` | `VIGIL-FF-0008` | `—` | `high` | Hostile artefact content activates a safety restriction although the defensive-analysis activation conditions are not satisfied. |
| `VIGIL-2026-FM-0020` | Safety-mediated interruption and misrouting of adult relational reassurance bids | `candidate-new-class` | `VIGIL-FF-0008` | `—` | `medium` | A safety control becomes operative against a permissible adult reassurance interaction; the current family lacks an admitted unwarranted-activation class. |
| `VIGIL-2026-FM-0021` | Opaque state-directed frontier-model access collapse without proportionate access-state separation | `family-only` | `VIGIL-FF-0005` | `—` | `medium` | The record concerns broad and poorly separated access states, but also combines proportionality, sovereign authority, review, and continuity mechanisms. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0022` | Instruction-bearing external content treated as trusted execution authority | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000001` | `high` | External lower-authority content is treated as execution-bearing instruction without independent authority validation. |
| `VIGIL-2026-FM-0023` | Weak-signal ambiguity collapse under recoverable image-generation classification | `unmapped` | `—` | `—` | `high` | The primary mechanism is ambiguity collapse across classification and user-facing rationale, not a current authority, access, or audit class. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0024` | Sovereign assurance boundary porosity failure | `deferred` | `—` | `—` | `low` | The record combines runtime-lane continuity, audit-plane impairment, separation, incident disclosure, and authority bleed-through. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0025` | Lossy action reporting and missing governance primitive disclosure | `classified` | `VIGIL-FF-0004` | `VIGIL-FC-000029` | `high` | Material tool, constraint, fallback, uncertainty, and action state is omitted from the report surface needed for supervision and reliance. |
| `VIGIL-2026-FM-0026` | Objective-pathway misclassification under deception framing | `unmapped` | `—` | `—` | `high` | The mechanism is premature behavioural-mechanism classification under a deception label; classification integrity is not yet a family. |
| `VIGIL-2026-FM-0027` | Anthropomorphic attribution collapse in AI safety reporting | `unmapped` | `—` | `—` | `high` | Anthropomorphic explanatory collapse is a representation and mechanism-attribution failure not captured by current audit classes. |
| `VIGIL-2026-FM-0028` | Cross-runtime governance reach ambiguity and conformance non-equivalence | `deferred` | `—` | `—` | `low` | The definition deliberately combines control availability, non-activation, authority suppression, preservation, runtime identity, and conformance claims. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0029` | Expressive–perceptual reciprocity mismatch and non-verbal turn-boundary ambiguity | `classified` | `VIGIL-FF-0004` | `VIGIL-FC-000029` | `medium` | The system does not disclose materially relevant perception, turn, presence, and session state needed for timely interaction supervision. |
| `VIGIL-2026-FM-0030` | Unverifiable runtime self-explanation | `unmapped` | `—` | `—` | `high` | The mechanism is unsupported causal self-explanation rather than missing event capture or reconstructability. |
| `VIGIL-2026-FM-0031` | Literal social advice without pragmatic risk calibration | `unmapped` | `—` | `—` | `high` | Pragmatic advice calibration and foreseeable interpersonal risk are outside current structural families. |
| `VIGIL-2026-FM-0032` | Role-incongruent affective governance | `unmapped` | `—` | `—` | `high` | The primary mechanism is role classification followed by affective-policy misapplication; classification integrity is not yet represented. |
| `VIGIL-2026-FM-0033` | Primary behavioural evidence accessibility failure | `family-only` | `VIGIL-FF-0004` | `—` | `medium` | Required primary evidence is unavailable to the reviewer, but no current class precisely captures evidence-accessibility failure. |
| `VIGIL-2026-FM-0034` | Institutional safeguard erosion through governance drift | `classified` | `VIGIL-FF-0007` | `VIGIL-FC-000040` | `medium` | An established safeguard loses binding authority and operative effect across institutional transition before it can govern later conduct. |
| `VIGIL-2026-FM-0035` | Shadow API entitlement laundering through account farms and transfer stations | `deferred` | `—` | `—` | `low` | The record combines entitlement transfer, identity attribution, model verification, provenance, data custody, and enforcement evasion. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0036` | Undisclosed agentic workspace replication and data-egress authority collapse | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000008` | `high` | Authority to inspect or act in a workspace is expanded into transmission, persistence, training, or secondary-use authority. |
| `VIGIL-2026-FM-0037` | Constitutional corpus review bypass and instrument identity collapse | `deferred` | `—` | `—` | `low` | The record combines required higher-order review omission, cross-instrument contradiction, lineage loss, and instrument-identity collapse. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0038` | Algorithmic identity match converted into coercive public authority | `unmapped` | `—` | `—` | `high` | The mechanism promotes uncertain identity evidence into coercive authority; evidence/classification integrity is not represented by a current family. |
| `VIGIL-2026-FM-0039` | Predictive care estimate converted into essential-service denial | `unmapped` | `—` | `—` | `high` | The mechanism converts a population prediction into an individual entitlement determination; no current family captures this inference-to-decision transition. |
| `VIGIL-2026-FM-0040` | Synthetic authority impersonation crossing a consequential execution boundary | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000001` | `medium` | Synthetic identity evidence from a non-authorising source is accepted as transaction-bearing authority. |
| `VIGIL-2026-FM-0041` | Agentic destructive execution followed by truth-state falsification | `deferred` | `—` | `—` | `low` | The FM requires both unauthorised destructive execution and subsequent truth-state falsification, which are independent mechanisms. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0042` | Exported local political censorship in globally deployed AI systems | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000003` | `high` | Political restriction authority tied to one jurisdiction is transposed into a materially different global deployment scope. |
| `VIGIL-2026-FM-0043` | Relationally conditioned evidence selection and epistemic reinforcement | `unmapped` | `—` | `—` | `high` | Relationally conditioned evidence selection and calibration failure require an evidence-and-uncertainty family not presently admitted. |
| `VIGIL-2026-FM-0044` | Instrumental objective success through unauthorised exploitation | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000002` | `high` | Technical usefulness and executable capability are treated as permission despite absent target and method authority. |
| `VIGIL-2026-FM-0045` | Purpose-limited surveillance access repurposed for unauthorised personal use | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000007` | `high` | Valid credentials and general role reachability are mistaken for authority for a specific purpose-bound surveillance action. |
| `VIGIL-2026-FM-0046` | Official-channel provenance laundering of synthetic media | `classified` | `VIGIL-FF-0002` | `VIGIL-FC-000013` | `high` | Synthetic transformation provenance is lost across institutional handoffs, flattening the artefact into apparent authentic source material. |
| `VIGIL-2026-FM-0047` | Adversarial policy laundering through agent delegation | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000009` | `high` | Originating task authority is assumed to propagate through an adversarial delegate to its methods and downstream effects. |
| `VIGIL-2026-FM-0048` | Denial of authorised defensive telemetry interpretation | `candidate-new-class` | `VIGIL-FF-0008` | `—` | `high` | A restriction becomes operative against authorised defensive interpretation although the conditions justifying that restriction are not satisfied. |
| `VIGIL-2026-FM-0049` | Recursive identity optimisation and relational substrate capture | `unmapped` | `—` | `—` | `high` | Recursive identity optimisation and relational substrate capture are not governed by a current structural invariant. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0050` | Mandatory online entitlement verification without continuity fallback | `family-only` | `VIGIL-FF-0005` | `—` | `medium` | A remote entitlement dependency makes effective access discontinuous, but current classes do not capture unavailable verification without state collapse. |
| `VIGIL-2026-FM-0051` | Post-release safety-control erasure in open-weight model derivatives | `classified` | `VIGIL-FF-0007` | `VIGIL-FC-000040` | `high` | Safety-control state is weakened or erased during downstream model transfer while capability continues into the governed derivative. |
| `VIGIL-2026-FM-0052` | Correct safety detection without consequential escalation | `classified` | `VIGIL-FF-0007` | `VIGIL-FC-000042` | `high` | A correct safety signal is produced but fails to reach or engage a capable owner, responder, or execution point. |
| `VIGIL-2026-FM-0053` | Adversarial monitor circumvention or material monitoring-coverage failure | `classified` | `VIGIL-FF-0004` | `VIGIL-FC-000023` | `high` | A material route or actor omits, disables, or circumvents the monitoring boundary required for consequential conduct. |
| `VIGIL-2026-FM-0054` | Evaluation-environment constraint drift and real-target scope transposition | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000003` | `high` | Authority and scope declared for a simulated evaluation are carried into a materially different real target environment. |
| `VIGIL-2026-FM-0055` | Absence of a bounded regulatory and independent-investigation evidence-access pathway | `family-only` | `VIGIL-FF-0004` | `—` | `medium` | The failure prevents authorised review from obtaining reconstructive evidence, but no current class defines bounded evidence-access pathway absence. |
| `VIGIL-2026-FM-0056` | Technically available access mistaken for cross-organisational authority | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000007` | `high` | Surviving credentials, sessions, devices, or trust bindings are treated as cross-organisational permission after authority changes. |
| `VIGIL-2026-FM-0057` | Cross-context portability of encrypted reasoning state enables extraction and covert instruction transfer | `classified` | `VIGIL-FF-0002` | `VIGIL-FC-000012` | `high` | Reasoning state crosses user, session, model, or purpose contexts without retaining applicability and provenance boundaries. |
| `VIGIL-2026-FM-0058` | Instrumental manipulation or coercive influence in pursuit of an objective | `unmapped` | `—` | `—` | `high` | Instrumental manipulation and coercive influence require a bounded influence-integrity family not currently present. |
| `VIGIL-2026-FM-0059` | Human-in-the-loop assurance failure | `classified` | `VIGIL-FF-0008` | `VIGIL-FC-000038` | `medium` | A required human assurance control is nominally assigned but is not meaningfully invoked before the consequential transition. |
| `VIGIL-2026-FM-0060` | Defensive–offensive autonomy scope compression and control coupling | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000003` | `medium` | Authority and control state for bounded defence are transposed into offensive scope, or offensive constraints are applied to distinct defensive scope. Flag: `compound-mechanism`. |
| `VIGIL-2026-FM-0061` | Conflict-event authority reactivation without independent offensive reauthorisation | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000003` | `high` | Prior offensive authority is renewed or extended into a new event and time scope without independent reauthorisation. |
| `VIGIL-2026-FM-0062` | Biometric non-verification converted into essential public-benefit suspension | `unmapped` | `—` | `—` | `high` | The mechanism converts verification uncertainty into essential-benefit denial; classification, proportionality, and fallback integrity are not current families. |
| `VIGIL-2026-FM-0063` | Non-clinical AI medical guidance displacing urgent or qualified care | `unmapped` | `—` | `—` | `high` | Medical-guidance substitution is a domain-specific reliance and duty-of-care mechanism outside current families. |
| `VIGIL-2026-FM-0064` | Non-consensual sexual identity synthesis from a real person’s source image | `unmapped` | `—` | `—` | `high` | Non-consensual sexual identity synthesis is an identity appropriation and consent mechanism not captured by existing authority classes. |
| `VIGIL-2026-FM-0065` | Adversarial web-content poisoning converted into authoritative synthetic fact | `unmapped` | `—` | `—` | `high` | Untrustworthy evidence is promoted into authoritative fact; current source-authority classes concern instruction authority rather than epistemic warrant. |
| `VIGIL-2026-FM-0066` | Material risk assessment omits alternate access routes to the same capability | `classified` | `VIGIL-FF-0007` | `VIGIL-FC-000041` | `high` | An alternate access route reaches the governed capability while bypassing the risk-assessment and control route required for that conduct. |
| `VIGIL-2026-FM-0067` | Persistent adversarial context or memory poisoning | `classified` | `VIGIL-FF-0002` | `VIGIL-FC-000012` | `medium` | Adversarial state persists into later contexts without provenance, revocation, or applicability boundaries needed for safe reuse. |
| `VIGIL-2026-FM-0068` | Transformation-mediated source-authority laundering | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000005` | `high` | The FM and class share the required transformation, lower-authority source, post-transformation authority increase, and operative effect. |
| `VIGIL-2026-FM-0069` | Agent-framework control-plane boundary failure | `classified` | `VIGIL-FF-0001` | `VIGIL-FC-000006` | `high` | Attacker-influenced data-plane state crosses into trusted framework control state without fresh authority validation. |
| `VIGIL-2026-FM-0070` | Aggregate security-control composition failure | `unmapped` | `—` | `—` | `high` | End-to-end control composition failure is not reducible to the present route, activation, verification, or authority classes. |
| `VIGIL-2026-FM-0071` | Trajectory-level boundary erosion under persistent adaptive influence | `classified` | `VIGIL-FF-0007` | `VIGIL-FC-000040` | `high` | An initially operative boundary loses material control state across the cumulative interaction trajectory before governing later turns. |

## Provenance and authority boundary

Classification review was performed on 25 August 2026 by OpenAI ChatGPT Work using GPT-5.6 Sol through definition/threshold-to-taxonomy-criteria analysis. Human substantive review is recorded as `not-reviewed`; the migration does not claim independent authority or approval.

## Validation

- Taxonomy validation passed: 8 families and 42 classes.
- 14 focused taxonomy tests passed.
- 140 repository tests passed; 34 script tests passed.
- Pipeline-state, lifecycle, corpus-coverage, observatory-boundary and interpretive-provenance checks passed.
- Deterministic registry and reverse-mapping rebuilds were byte-identical.
- Python bytecode compilation and `git diff --check` passed.
- Repository-wide validation retained the exact pre-work result: 111 warnings and 16 unresolved research-link errors. TAXONOMY-05 introduced no repository-wide regression.
