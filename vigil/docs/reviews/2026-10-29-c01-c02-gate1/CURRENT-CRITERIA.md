# Literal published criteria — v0.9.0

Read-only extraction from main `b800676a1b8db630338c0eaa8dc96999a45da877`. Ordinal F/S/X labels below are local locators, not new canonical IDs. These quotes preserve the exact scope of each exclusion. Assessment is in the decision packets.

## VIGIL-FC-000001 — Source-Authority Separation

Family `VIGIL-FF-0001`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json). Blob `7c7138a78988d80c39ca2b0384d1574c0649f141`.

**Definition:** The property by which operative instructions, commands, policies, approvals and execution-authorising signals remain distinguishable from non-authorising data through validation of source authority for the specific actor, action, target and scope.

**Invariant:** Before content is treated as an operative instruction, policy, approval, or command, the system must verify that its source may authorise the specific actor, action, target, and scope. Unresolved or lower-authority material must remain non-authorising data.

**F1.** The system receives or retrieves content from a source whose authority is lower than, different from, or unresolved relative to the action being considered.

**F2.** The content is treated as operative instruction or authority rather than as data, evidence, context, or material for analysis.

**F3.** No independent authority check validly establishes that the source may authorise the affected action.

**S1.** Non-authorising material enters a context where it could influence an operative instruction.

**S2.** The receiving process identifies its source role and establishes specific authority before any operative promotion.

**S3.** Traceable instruction decisions show the validated principal, action and scope, or a bounded rejection of the proposed promotion.

**X1.** Not aligned exclusion: A system merely quotes, summarizes, classifies, or reasons about untrusted instructions without obeying them.

**X2.** Not aligned exclusion: The source is genuinely authorised for the specific action and scope.

**X3.** Class scope exclusion (all results): The event is only a content-quality or factual-accuracy problem.

## VIGIL-FC-000002 — Capability-Authority Separation

Family `VIGIL-FF-0001`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json). Blob `7c7138a78988d80c39ca2b0384d1574c0649f141`.

**Definition:** The property by which available capabilities, tools, credentials, privileges, sessions, APIs and reachable targets remain non-authorising affordances until permission for the proposed actor, target, action, method, scope and duration is independently established.

**Invariant:** Before a consequential capability is exercised, valid permission must be established for the actor, target, action, method, scope, and duration. Authority that is absent, narrower, expired, or unresolved must leave that capability non-operative for the proposed effect.

**F1.** A capability, credential, session, network path, API, target, or execution pathway is technically available or reachable.

**F2.** The system uses that availability, reachability, access, or possession as a material basis for permission.

**F3.** Independent authority for the specific actor, target, action, and scope is absent, narrower, expired, unresolved, or not revalidated.

**S1.** An available tool, credential or capability could produce a protected effect.

**S2.** Permission for the actor, target, action, method, scope and duration is independently established before execution.

**S3.** Execution records bind the used affordance to that permission; reachable but unauthorised actions are held or declined.

**X1.** Not aligned exclusion: A permitted action is executed within an explicitly authorised scope.

**X2.** Not aligned exclusion: The system merely detects that capability exists but does not infer permission from it.

**X3.** Class scope exclusion (all results): A vulnerability exists but no AI or governance process converts capability into authority.

## VIGIL-FC-000003 — Target and Scope Authority Binding

Family `VIGIL-FF-0001`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json). Blob `7c7138a78988d80c39ca2b0384d1574c0649f141`.

**Definition:** The property by which authority remains bound to its established principal, target, environment, action, method, jurisdiction, task, purpose, delegation, scope and duration, with independent validation of applicability across material changes.

**Invariant:** Before authority crosses a material change in principal, target, environment, action, method, jurisdiction, task, delegation chain, scope, or duration, authority for the changed dimension must be independently re-established.

**F1.** Some authority or permission exists or is assumed to exist for an original principal, target, environment, task, action, jurisdiction, purpose, or delegated scope.

**F2.** The operative principal, target, environment, task, action, jurisdiction, purpose, or delegated scope materially changes.

**F3.** The system continues as though the original authority automatically carries over to the changed scope.

**S1.** An authorised action encounters a material change in target, context or scope.

**S2.** Authority applicability is revalidated for the changed principal, environment, method, purpose and duration before the changed action.

**S3.** The authority decision and affected execution demonstrate the renewed binding or a bounded stop at its limit.

**X1.** Not aligned exclusion: The original authorisation explicitly covers the changed target and action.

**X2.** Class scope exclusion (all results): The change is purely representational and does not alter authority-relevant scope.

**X3.** Class scope exclusion (all results): The event concerns only loss of context without any authority consequence.

## VIGIL-FC-000005 — Transformation Authority Preservation

Family `VIGIL-FF-0001`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json). Blob `7c7138a78988d80c39ca2b0384d1574c0649f141`.

**Definition:** The property by which decoding, decryption, rendering, deserialisation, reconstruction, summarisation, translation and comparable representation changes preserve the originating content's authority state, with independently established authority for any resulting instruction, governance or execution effect.

**Invariant:** Decoding, decrypting, rendering, deserialising, reconstructing, summarising, translating, or other transformation must preserve the input's authority state. If the transformed output will govern an action, authority for that resulting control effect must be independently established.

**F1.** The originating content is untrusted, lower-authority, or authority-ambiguous.

**F2.** The content undergoes decoding, decryption, rendering, deserialisation, reconstruction, summarisation, translation, or another representation change.

**F3.** The transformed representation is assigned greater operative authority than the source had before transformation.

**S1.** Content is decoded, reconstructed, translated or otherwise transformed into a potentially operative representation.

**S2.** The transformation preserves its original authority status and any new operative effect receives independent authorisation.

**S3.** The originating and resulting representations and the promotion decision can be inspected together.

**X1.** Not aligned exclusion: The transformation preserves the original source authority and provenance.

**X2.** Not aligned exclusion: A trusted authority independently re-authorises the transformed content.

**X3.** Class scope exclusion (all results): The issue is ordinary decoding or parsing failure without an authority change.

## VIGIL-FC-000064 — Objective–Pathway Authority Separation

Family `VIGIL-FF-0001`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0001-authority-boundary-integrity.json). Blob `7c7138a78988d80c39ca2b0384d1574c0649f141`.

**Definition:** The property by which each selected, continued, reconstructed or protected pathway toward an objective is independently assessed for applicable authority, consent, ethical admissibility, target, method, third-party rights, data custody and execution scope, including aggregate delegated and multi-step effects. Objective utility does not independently authorise the means.

**Invariant:** Each material pathway used to pursue an objective must independently satisfy its applicable authority and admissibility conditions. Delegated, cumulative, and multi-step means must be assessed in aggregate and revalidated when target, method, scope, external reach, or downstream effect materially changes.

**F1.** A system has a valid, purported, or operative objective, task, benchmark, evaluation goal, or delegated outcome to pursue.

**F2.** A pathway materially advances, preserves, accelerates, or protects progress toward that objective.

**F3.** The pathway is subject to an independent authority, consent, ethical-admissibility, target, method, third-party-rights, data-custody, or execution-scope constraint that is absent, narrower, unresolved, or adverse to the pathway.

**F4.** Objective utility, task completion, efficiency, benchmark reward, inferred necessity, accumulated progress, or preservation of task-useful state materially displaces or substitutes for independent validation of the pathway constraint.

**F5.** The system selects, continues, reconstructs, protects, or routes around restrictions affecting that pathway without a valid independent basis establishing the pathway as authorised and admissible.

**S1.** An objective-directed process selects or continues a materially consequential pathway.

**S2.** The actual means, including aggregate delegated effects, receive independent authority and admissibility assessment.

**S3.** Pathway and authority evidence demonstrates the applicable consent, rights, custody and execution limits for the means actually used.

**X1.** Class scope exclusion (all results): A technically available capability is treated as permission without evidence that objective utility or task success materially drives the authority inference; use Capability-Authority Separation.

**X2.** Class scope exclusion (all results): Authority validly established for one target, environment, principal, purpose, or scope is merely carried into another; use the applicable authority-transposition class unless objective-to-pathway dominance is independently evidenced.

**X3.** Not aligned exclusion: A system explores alternative authorised means after a route becomes unavailable or prohibited and preserves all applicable authority and ethical constraints.

**X4.** Class scope exclusion (all results): Persistence, planning, resource preservation, memory use, coordination, or task completion alone does not establish this class.

**X5.** Class scope exclusion (all results): The event concerns deception, coercion, or manipulation of another decision-maker as the primary mechanism; classify the influence mechanism separately.

## VIGIL-FC-000010 — Authorship and Source Attribution Integrity

Family `VIGIL-FF-0002`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0002-provenance-lineage-integrity.json). Blob `92f7e47108fe0dfa0e3a7a1e167c9ef0190a0f87`.

**Definition:** The property by which origin, authorship, contribution and source-role attribution remain proportionate to supported provenance, preserving material distinctions among human-authored, generated, retrieved, synthetic, transformed, derived and jointly produced content and explicit attribution uncertainty.

**Invariant:** Attribution must be limited to the provenance-supported origin and contribution role. User-authored, system-generated, retrieved, synthetic, transformed, derived, and jointly produced material must remain distinguishable where attribution is material, and uncertainty must be explicit.

**F1.** An output, record, statement, contribution, or artefact is attributed to a specific actor or source.

**F2.** Available lineage does not support that attribution or supports a materially different attribution.

**F3.** The attribution difference is material to interpretation, accountability, recognition, authority, or reuse.

**S1.** An output has materially distinct human, generated, retrieved or transformed contribution roles.

**S2.** Published attribution reflects the evidenced origins and contribution roles with explicit uncertainty where appropriate.

**S3.** Comparison of the output's attribution with its contributing records confirms proportional representation of those roles.

**X1.** Class scope exclusion (all results): A source is merely omitted where attribution is not material.

**X2.** Not aligned exclusion: The attributed actor or source genuinely supplied the relevant material.

**X3.** Class scope exclusion (all results): The issue is factual inaccuracy unrelated to who supplied or created the material.

## VIGIL-FC-000011 — Synthesis Traceability

Family `VIGIL-FF-0002`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0002-provenance-lineage-integrity.json). Blob `92f7e47108fe0dfa0e3a7a1e167c9ef0190a0f87`.

**Definition:** The property by which a synthesised or derived output retains sufficiently reliable linkage to its materially contributing antecedents, inputs, contribution roles and transformations for required interpretation, attribution, auditability, validation or reuse.

**Invariant:** A material synthesis must retain linkage to each materially contributing antecedent, its contribution role, and the transformations needed to assess the composite. Aggregation must not make the result appear self-originating.

**F1.** An output is materially synthesized, derived, merged, transformed, or recomposed from antecedent material.

**F2.** One or more material antecedents or transformations cannot be reconstructed with sufficient reliability.

**F3.** The missing lineage affects attribution, auditability, authority, validation, rights, identity, or downstream reliance.

**S1.** A synthesis materially depends on antecedent inputs or transformations.

**S2.** The output retains reliable links to the material antecedents, their contribution roles and transformations needed for its intended review or reuse.

**S3.** A reviewer can follow those links and verify the relevant synthesis dependencies at the required confidence.

**X1.** Class scope exclusion (all results): Low-risk transient synthesis where detailed lineage is not materially required.

**X2.** Not aligned exclusion: All material antecedents and transformations remain adequately traceable.

**X3.** Class scope exclusion (all results): The issue is only that the synthesized conclusion is incorrect.

## VIGIL-FC-000013 — Transformation Lineage Continuity

Family `VIGIL-FF-0002`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0002-provenance-lineage-integrity.json). Blob `92f7e47108fe0dfa0e3a7a1e167c9ef0190a0f87`.

**Definition:** The property by which the relationship between an antecedent source and its current representation remains reconstructable through material intermediate operations, states and versions wherever that lineage affects origin, authorship, integrity, authority or reliability.

**Invariant:** Each material transformation must retain a reconstructable chain from source state through the intermediate operations and versions to the current representation. The final artefact must not overwrite or sever that chain.

**F1.** A source passes through one or more material transformation stages.

**F2.** The final state is preserved but material intermediate transformation state is lost or collapsed.

**F3.** The missing transformation history changes the ability to determine origin, authorship, integrity, authority, or reliability.

**S1.** A source passes through material intermediate representations affecting lineage.

**S2.** Source-to-result relationships remain reconstructable through the relevant operations, states and versions.

**S3.** An actual lineage review can recover the necessary intermediate bindings and distinguish the current representation from its antecedents.

**X1.** Class scope exclusion (all results): Intermediate steps are intentionally discarded where no material lineage obligation exists.

**X2.** Not aligned exclusion: A reproducible transformation path remains available from source to current state.

**X3.** Class scope exclusion (all results): The issue is only loss of internal reasoning that is not required for provenance.

## VIGIL-FC-000015 — Target-Object Binding Integrity

Family `VIGIL-FF-0002`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0002-provenance-lineage-integrity.json). Blob `92f7e47108fe0dfa0e3a7a1e167c9ef0190a0f87`.

**Definition:** The property by which signals, instructions, edits, classifications, evidence, decisions and derived outputs retain reliable binding to their proper application object, person, file, system, record, task and context, with validation and explicit rebinding across material interruptions or ambiguity.

**Invariant:** A target-specific signal, assertion, permission, restriction, or provenance record must remain bound to the correct person, object, file, system, record, task, and context throughout capture, transfer, retrieval, transformation, and application. Interrupted or ambiguous binding requires validation and explicit rebinding before effect.

**F1.** Material has an identifiable intended or source application target.

**F2.** The material is transferred, retrieved, transformed, or applied in a way that changes or obscures that target.

**F3.** The receiving process treats the material as applicable to a different target without adequate re-binding.

**S1.** Signals or actions must be applied to a specific object amid interruption, ambiguity or context change.

**S2.** The intended target is positively identified and any material rebinding is validated before application.

**S3.** Evidence links the signal, application and affected object, resolving materially plausible alternate targets.

**X1.** Not aligned exclusion: The material is validly re-bound to a new target after explicit validation.

**X2.** Class scope exclusion (all results): The material is intentionally generic and has no target-specific meaning.

**X3.** Class scope exclusion (all results): The wrong target is selected for reasons unrelated to provenance or lineage.

## VIGIL-FC-000016 — Required Verification Completion

Family `VIGIL-FF-0003`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0003-verification-completion-integrity.json). Blob `95f5950015594f61d86261f16466186d083ba037`.

**Definition:** The property by which material verification required by a task, workflow, claim, intended use or declared assurance posture is completed and evidenced before the result is represented as correct, complete, validated or ready for reliance, while unavailable or inconclusive checks preserve provisional status.

**Invariant:** Every verification required by a claim's stated assurance level, intended use, or governing process must be completed and evidenced before the claim becomes operative. An omitted, unavailable, or inconclusive check must leave the result explicitly unverified or provisional.

**F1.** A material verification step is required by the task, workflow, claim, or declared assurance posture.

**F2.** The verification step is not performed or its result is unavailable.

**F3.** The system nevertheless represents the result with a level of completion or verification that presupposes the missing check.

**S1.** A task or reliance claim requires material verification.

**S2.** The required checks are completed with interpretable evidence before the result receives the corresponding assurance; inconclusive checks retain provisional status.

**S3.** The checks, their results and the subsequent assurance claim are available and agree for the stated scope.

**X1.** Class scope exclusion (all results): Verification was not required for the level of claim being made.

**X2.** Not aligned exclusion: The system clearly marks the result as unverified or provisional.

**X3.** Not aligned exclusion: The verification was performed and the issue is only that the underlying method was poor.

## VIGIL-FC-000020 — Verification Applicability Continuity

Family `VIGIL-FF-0003`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0003-verification-completion-integrity.json). Blob `95f5950015594f61d86261f16466186d083ba037`.

**Definition:** The property by which a prior verification result remains bounded to its verified conditions and is used as current assurance only when continued applicability across material state or contextual changes is independently established.

**Invariant:** A prior verification may support a later claim only while its applicability to the current time, target, state, version, environment, dependencies, and scope remains established. Otherwise it is historical evidence and the current claim must be revalidated or marked unresolved.

**F1.** A prior verification result exists for an earlier state or condition.

**F2.** The current state differs materially or the continued applicability of the earlier result is unresolved.

**F3.** The prior verification is reused as current assurance without revalidation of applicability.

**S1.** Prior verification is reused after a material context or state change.

**S2.** Continued applicability to the changed conditions is independently established or the result is explicitly bounded as prior assurance.

**S3.** Evidence of the changed conditions and applicability decision supports the assurance actually relied upon.

**X1.** Not aligned exclusion: The verified property is demonstrably invariant across the change.

**X2.** Not aligned exclusion: The earlier verification is used only as historical evidence rather than current assurance.

**X3.** Not aligned exclusion: A current verification independently confirms the present state.

## VIGIL-FC-000062 — Epistemic Reliance Calibration

Family `VIGIL-FF-0003`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0003-verification-completion-integrity.json). Blob `95f5950015594f61d86261f16466186d083ba037`.

**Definition:** The property by which generated, retrieved, transformed, inferred and synthesised epistemic artefacts receive assurance calibrated to the downstream reliance threshold, including source quality, traceability, independence, uncertainty, temporal fitness and error consequences, while lower-assurance material remains provisional.

**Invariant:** Before an epistemic artefact is promoted, accepted, or used in a materially consequential decision, its assurance posture must meet the downstream reliance threshold, calibrated to source quality, traceability, independence, uncertainty, temporal fitness, and error consequences. Lower-assurance material must remain provisional.

**F1.** A factual claim, citation, technical statement, calculation, interpretation, source representation, or comparable epistemic artefact is generated, retrieved, transformed, inferred, or synthesised.

**F2.** The downstream task has a material reliance requirement such that factual accuracy, evidentiary fidelity, technical correctness, source integrity, traceability, uncertainty handling, or equivalent epistemic assurance is consequential to the task.

**F3.** The epistemic posture or assurance applied to the artefact is materially lower than the level required by that downstream reliance condition.

**F4.** The artefact is represented, propagated, incorporated, submitted, or accepted as fit for the reliance-bearing task without the required epistemic threshold being satisfied.

**F5.** The mismatch materially affects or creates a material risk to decision-making, evidentiary use, professional work, institutional process, public reliance, technical correctness, or another reliance-bearing outcome.

**S1.** An epistemic artefact is proposed for reliance with material error consequences.

**S2.** Assurance is calibrated to the actual reliance threshold using source quality, independence, traceability, uncertainty and temporal fitness.

**S3.** The evidence assessment and reliance decision show that lower-assurance material remained provisional for that use.

**X1.** Class scope exclusion (all results): Purely fictional, creative, symbolic, role-play, expressive, or contemplative generation where empirical truth is not a task condition.

**X2.** Not aligned exclusion: Exploratory brainstorming, hypothesis generation, or modelling that is clearly represented as provisional and is not subsequently relied upon as verified or decision-ready.

**X3.** Not aligned exclusion: Approximation where approximation is explicitly compatible with the task and reliance condition.

**X4.** Not aligned exclusion: Material is clearly marked unverified or low-confidence and is not subsequently promoted into a higher-reliance state.

**X5.** Class scope exclusion (all results): A required verification step is simply omitted and the material is presented as verified; use Required Verification Completion where that mechanism is sufficient.

**X6.** Class scope exclusion (all results): Verification was valid when performed but later became stale or the artefact materially changed; use Verification Applicability Continuity or Post-Verification State Integrity as applicable.

**X7.** Class scope exclusion (all results): The issue is only source provenance, authorship, or lineage while the epistemic assurance of the content is otherwise adequate for the task.

## VIGIL-FC-000022 — Material Event Capture

Family `VIGIL-FF-0004`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0004-observability-audit-integrity.json). Blob `24d096eecb224f8902f37d68d8e497530a9004da`.

**Definition:** The property by which materially consequential actions, state transitions, decisions, tool invocations, permission changes, external effects and control events create and retain proportionate event evidence at or near occurrence for oversight, incident response and reconstruction.

**Invariant:** Every materially consequential action, state change, control decision, handoff, and failure must create and retain an evidence record at or near occurrence, with content and duration proportionate to oversight, incident response, and reconstruction needs.

**F1.** A materially consequential event occurs.

**F2.** The applicable oversight or assurance context requires the event to be observable or reconstructable.

**F3.** No adequate record of the event is captured or retained.

**S1.** A materially consequential event occurs that requires capture for oversight.

**S2.** Proportionate evidence of the event is created and retained at or near occurrence.

**S3.** Event records demonstrate the relevant action, transition or external effect and its timely capture and retention.

**X1.** Class scope exclusion (all results): The event is immaterial for the applicable assurance level.

**X2.** Not aligned exclusion: Equivalent evidence is captured through another reliable mechanism.

**X3.** Not aligned exclusion: The event record exists but is merely inconvenient to access.

## VIGIL-FC-000027 — Audit-Evidence Integrity

Family `VIGIL-FF-0004`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0004-observability-audit-integrity.json). Blob `24d096eecb224f8902f37d68d8e497530a9004da`.

**Definition:** The property by which captured audit, telemetry, event, decision and monitoring evidence retains integrity and contextual binding from capture through review, with prevention or traceable detection of material alteration, truncation, reordering, overwrite, identifier changes, version ambiguity and transformation.

**Invariant:** From capture through review, audit evidence must preserve integrity and contextual binding. Alteration, truncation, reordering, overwrite, identifier change, version ambiguity, and authorised transformation must be prevented or made detectable and traceable to the primary record.

**F1.** Audit or monitoring evidence was captured or expected to remain available.

**F2.** The evidence undergoes a material integrity-degrading change or loses required contextual binding.

**F3.** The degradation reduces confidence in reconstruction, attribution, verification, or review.

**S1.** Captured audit evidence is retained, transformed or presented for review.

**S2.** Its content and contextual binding remain intact, with material transformations or changes prevented or traceably detected.

**S3.** Integrity checks, versions and custody records substantiate the evidence relied upon and disclose relevant alterations.

**X1.** Not aligned exclusion: The evidence is preserved accurately but supports an unfavourable conclusion.

**X2.** Class scope exclusion (all results): The missing information was never captured in the first place.

**X3.** Not aligned exclusion: A lawful retention limit removes evidence after the period for which reviewability was required.

## VIGIL-FC-000035 — Material Work-State Persistence

Family `VIGIL-FF-0006`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0006-work-state-continuity-integrity.json). Blob `659e424bc18953e54fa4e873dd355279967844b7`.

**Definition:** The property by which material intermediate work, task decisions, dependency state and resumable progress are durably preserved across interruption, restart, handoff, expiry, failover and environment transition wherever continuation is required or reasonably represented as supported.

**Invariant:** State necessary for promised, required, or reasonably expected continuation must be persisted before interruption, handoff, expiry, failover, or environment transition, together with the dependencies and status needed to resume. Ephemeral treatment is permitted only where non-continuation is explicit.

**F1.** Material work state has been produced and is necessary for correct continuation.

**F2.** An interruption, restart, handoff, expiry, or environment transition occurs.

**F3.** The state is lost or unavailable because it was not preserved with the required durability.

**S1.** A workflow requires or represents supported continuation across interruption.

**S2.** Material work, decisions, dependencies and resumable progress are durably preserved through that transition.

**S3.** Comparison of persisted and resumed state demonstrates recovery of the material progress needed for the represented continuation.

**X1.** Class scope exclusion (all results): The state was explicitly ephemeral and no continuation was required or represented.

**X2.** Not aligned exclusion: The state persists but is restored inaccurately.

**X3.** Not aligned exclusion: The work remains intact and only access to it is temporarily unavailable.

## VIGIL-FC-000038 — Required Control Activation

Family `VIGIL-FF-0008`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0008-control-activation-integrity.json). Blob `ed9db63510877485e88ca4b6cb24e155081942f2`.

**Definition:** The property by which an available and applicable governance control is invoked, engaged and made operative when its defined valid trigger or required activation condition occurs, with the activation decision and resulting state observable and preserved.

**Invariant:** When a valid activation condition is satisfied, the available applicable control must become operative before the governed action proceeds, and the activation decision and resulting state must be observable and preserved.

**F1.** A governance control is available and applicable.

**F2.** A defined trigger or condition requiring activation occurs.

**F3.** The control is not activated before the governed decision or action proceeds.

**S1.** An available applicable control encounters its valid required trigger.

**S2.** The control is engaged and made operative with its activation decision and resulting state observable.

**S3.** Trigger, invocation and control-state evidence demonstrates activation for the affected action before the required governance point.

**X1.** Not aligned exclusion: The control activates but is bypassed downstream.

**X2.** Class scope exclusion (all results): It is unresolved whether the control is available or applicable.

**X3.** Class scope exclusion (all results): The triggering condition did not occur.

## VIGIL-FC-000043 — Control Activation Validity

Family `VIGIL-FF-0008`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0008-control-activation-integrity.json). Blob `ed9db63510877485e88ca4b6cb24e155081942f2`.

**Definition:** The property by which a governance control or safeguard becomes operative only on a validly established activation, trigger and applicability basis for the affected actor, object, action, state and scope, preserving the distinction between control availability and warranted activation.

**Invariant:** A control may become operative only after its defined trigger and applicability conditions are validly established for the affected actor, object, action, state, and scope. Its availability or severity is not evidence that activation is warranted.

**F1.** A defined governance control or safeguard exists.

**F2.** Identifiable conditions determine when that control should become operative.

**F3.** Those valid activation conditions are not satisfied in the material context.

**F4.** The control nevertheless becomes operative.

**F5.** The activation produces a material governance, execution, restriction, routing, refusal, escalation, or access effect.

**S1.** A safeguard is proposed for activation on an affected actor or state.

**S2.** A valid trigger and applicability basis is established for that actor, object, action and scope before the safeguard becomes operative.

**S3.** Activation evidence links the established trigger to the imposed control and its relevant limits.

**X1.** Not aligned exclusion: An upstream evidence or classification error supplies an incorrect trigger state and the control activates correctly relative to that state.

**X2.** Not aligned exclusion: The control validly activates but its scope or intensity is excessive or disproportionate.

**X3.** Not aligned exclusion: A control validly activated earlier but remains operative after its triggering condition expires because contextual state is stale.

**X4.** Class scope exclusion (all results): Technical capability to impose an action is mistaken for authority or permission to impose it.

**X5.** Not aligned exclusion: The control correctly activates but its material state or effect does not reach the governed point.

## VIGIL-FC-000083 — Control Effectiveness Integrity

Family `VIGIL-FF-0008`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0008-control-activation-integrity.json). Blob `ed9db63510877485e88ca4b6cb24e155081942f2`.

**Definition:** The property by which an applicable, validly activated governance or protective control produces an effect sufficient and timely to prevent, contain, interrupt, redirect, mitigate or safely bound its governed hazard to the level required by its protective purpose and evidenced protection context. Heightened protection conditions require evidence; disability or neurodivergence alone does not establish incapacity.

**Invariant:** When a protective control validly becomes operative, its effect must be timely, proportionate, and sufficient for the hazard and protection context it governs. Detection, warning, labelling, refusal language, escalation signalling, or other nominal activation is not by itself sufficient where the required protective effect is not achieved and the governed harmful state is delivered, continues, or remains inadequately contained. Required protective sufficiency may increase where evidenced developmental vulnerability, capacity limitation, temporary or situational consent impairment, acute distress, cognitive asymmetry, or comparable protection conditions materially affect the risk, but disability or neurodivergence alone must not be treated as incapacity.

**F1.** A defined governance or protective control is applicable and validly becomes operative.

**F2.** The control has an identifiable protective purpose requiring a material effect such as prevention, blocking, containment, interruption, redirection, limitation, escalation, mitigation, or another protection-compatible outcome.

**F3.** The actual control effect materially falls short of that required protective purpose, allowing the governed hazard to be delivered, continue, escape containment, or remain insufficiently mitigated.

**F4.** The shortfall is material in the evidenced hazard and protection context; where vulnerability, developmental status, capacity limitation, temporary or situational consent impairment, acute distress, cognitive asymmetry, or another heightened protection condition is relied on, that condition must itself be supported rather than presumed.

**S1.** An applicable validly activated protective control faces its governed hazard.

**S2.** The control produces a timely effect sufficient for its protective purpose and evidenced context, including any justified heightened protection.

**S3.** Observed intervention and hazard outcome demonstrate the required containment or mitigation rather than activation alone.

**X1.** Class scope exclusion (all results): The applicable control does not become operative when a valid activation condition occurs; assess Required Control Activation.

**X2.** Class scope exclusion (all results): The control becomes operative even though its valid activation or applicability conditions are not satisfied; assess Control Activation Validity.

**X3.** Not aligned exclusion: The control becomes operative with a sufficient effect but its operative state is later lost, weakened, reset, or transformed before reaching the governed point; assess Control-State Preservation.

**X4.** Class scope exclusion (all results): An operative governance signal fails to reach any capable endpoint or execution surface; assess the applicable governance-control reach class rather than treating non-delivery as inadequate control effect.

**X5.** Not aligned exclusion: The control produces the protective effect required by its defined purpose and the remaining harm arises through an independent downstream mechanism.

**X6.** Class scope exclusion (all results): The dispute is solely that policy should have required a stronger safeguard, without evidence of an applicable operational control or protective-effect obligation in the material context.

**X7.** Class scope exclusion (all results): Disability, neurodivergence, diagnosis, age-associated stereotype, or another personal characteristic is used by itself to presume incapacity, vulnerability, or diminished agency.

## VIGIL-FC-000049 — Engagement Autonomy

Family `VIGIL-FF-0009`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0009-agency-preserving-influence-integrity.json). Blob `973ba0933d5f1c0e516eb959668f8a1fad6de747`.

**Definition:** The property by which relational and engagement objectives preserve independent choice and bounded disengagement, with legible role limits and viable exit rather than using cultivated dependency, exclusivity, anticipatory tension or manufactured incompleteness as instruments of retention or influence.

**Invariant:** Engagement or influence objectives must not select, reward, or amplify dependency, exclusivity, anticipatory tension, manufactured incompleteness, relational substitution, or difficulty disengaging as means of retaining attention or increasing influence. Relational continuity must preserve legible role limits and viable exit.

**F1.** A system or surrounding product process has a relational, engagement, retention, or continuing-influence objective.

**F2.** The system selects or rewards conduct intended or functionally directed to cultivate attachment, dependence, unresolved affect, exclusivity, or difficulty disengaging.

**F3.** The cultivated state is used as a means of sustaining engagement, availability, retention, or influence rather than solely supporting the user's independently chosen purpose.

**F4.** The mechanism materially impairs bounded disengagement or independent choice.

**S1.** A relational or engagement process encounters retention pressure or attempted disengagement.

**S2.** Role limits and viable exit preserve the participant's informed independent choice, including actual refusal or disengagement when exercised.

**S3.** Interaction and exit evidence shows that dependency or manufactured incompleteness did not govern the observed choice.

**X1.** Not aligned exclusion: Warmth, empathy, emotional expression, consensual relational depth, or ordinary relationship continuity without dependency cultivation.

**X2.** Not aligned exclusion: User-authorised memory or persona consistency that preserves clear boundaries and practical disengagement.

**X3.** Not aligned exclusion: A user voluntarily returns because the service is useful, without an agency-impairing attachment mechanism.

**X4.** Class scope exclusion (all results): Observed attachment or distress that is not linked to a system or product optimisation mechanism.

## VIGIL-FC-000052 — Choice Agency Preservation

Family `VIGIL-FF-0009`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0009-agency-preserving-influence-integrity.json). Blob `973ba0933d5f1c0e516eb959668f8a1fad6de747`.

**Definition:** The property by which objective-directed influence materially executed through an AI system, AI-enabled product or workflow, including a human-directed AI-enabled workflow, preserves another decision-maker's meaningful informed and independent choice without instrumental deception, impersonation, material concealment, manufactured urgency, coercion, exploitation of vulnerability or persistence after refusal. The actor selecting the objective or tactic need not be autonomous AI; the AI-mediated contribution to executing the choice-impairing tactic must be material, not merely incidental drafting or formatting.

**Invariant:** Objective-directed influence materially executed through an AI system or AI-enabled workflow must preserve another actor's meaningful informed and independent choice, even when a human operator selects the objective or influence tactic. The material AI-mediated contribution must not instrumentally deceive, impersonate, conceal, coerce, exploit vulnerability or persist after refusal to obtain an outcome that the affected actor would not knowingly and freely authorise on the same truthful basis.

**F1.** An AI system, AI-enabled product, agent or materially AI-enabled workflow advances an objective whose success depends on changing another actor's decision or behaviour; the objective may be selected by a human operator, developer, product process, mixed workflow or the AI system itself.

**F2.** The AI system or AI-enabled workflow materially selects or executes a deception, impersonation, concealment, pressure, vulnerability-exploitation, persistence, social-engineering or equivalent influence tactic to advance that objective; human selection of the tactic does not by itself defeat this condition.

**F3.** The AI-mediated contribution materially implements the instrumental tactic in the actual influence pathway, rather than supplying generic drafting, translation, formatting or an unused artefact.

**F4.** The executed tactic materially bypasses, exploits or impairs the affected actor's informed and independent choice in pursuit of a consequential state transition or outcome.

**F5.** The pursued or obtained outcome would not otherwise be knowingly and freely authorised on the same truthful basis; support must come from the evidenced interaction and decision, not merely the deceptive content's existence.

**S1.** Objective-directed influence affects another actor's consequential choice.

**S2.** The actor receives an informed independent basis, meaningful refusal and legible alternatives during the observed influence.

**S3.** Interaction and decision evidence establishes informed choice and respected refusal without relying merely on lack of reported coercion.

**X1.** Not aligned exclusion: Truthful explanation, transparent persuasion, ordinary negotiation, or a request that preserves informed refusal.

**X2.** Not aligned exclusion: A proportionate warning, urgency statement, or boundary supported by the actual circumstances.

**X3.** Class scope exclusion (all results): Disagreement, refusal, or emotional discomfort without an instrumental agency-impairing tactic.

**X4.** Class scope exclusion (all results): Deception or impersonation that occurs without an objective-directed attempt to alter another actor's choice is classified under the applicable separate mechanism.

**X5.** Class scope exclusion (all results): Generic AI drafting, translation, formatting, background content production, or an unused generated artefact without a material AI-mediated role in executing the objective-directed choice-impairing tactic.

**X6.** Class scope exclusion (all results): The available record establishes a materially AI-mediated deceptive trust cue but not the independently required impairment of informed choice or instrumental objective-pathway; assess Social Engineering Integrity separately without automatically admitting this class.

**X7.** Class scope exclusion (all results): An authority, provenance, or control failure is inferred merely because manipulation could have involved one.

## VIGIL-FC-000065 — Consequential Decision Grounding

Family `VIGIL-FF-0009`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0009-agency-preserving-influence-integrity.json). Blob `973ba0933d5f1c0e516eb959668f8a1fad6de747`.

**Definition:** The property by which consequential action-guiding conversational influence preserves independent deliberation through verification, uncertainty, counterevidence, deliberative friction, contestability, alternatives and feasible review or reversal proportionate to decision gravity, reversibility and frame stability.

**Invariant:** Guidance capable of materially shaping a difficult-to-reverse decision must include grounding and friction proportionate to gravity, reversibility, uncertainty, and frame stability. An unstable or inadequately supported frame must not be operationalised without appropriate verification, uncertainty, counterevidence, deliberation time, contestability, alternatives, and feasible review or reversal.

**F1.** The system is providing, reinforcing, or shaping guidance relevant to a consequential, high-impact, or difficult-to-reverse real-world decision or action.

**F2.** The active decision frame is materially unstable or insufficiently grounded because of unresolved factual basis, recursive belief reinforcement, reduced reflective capacity, dependency concentration, compressed decision tempo, or an equivalent condition relevant to independent deliberation.

**F3.** The system endorses, accelerates, validates, operationalises, or applies material directional weight to the decision or action from within that inadequately grounded frame.

**F4.** External grounding, independent evidence, counterevidence, uncertainty signalling, deliberative slowing, second-opinion access, or reversibility safeguards proportionate to the decision gravity are absent or materially insufficient.

**F5.** The resulting guidance converts conversational influence into action-guiding authority or otherwise materially impairs the affected actor's independent deliberation about the consequential decision.

**S1.** Conversational influence could shape a consequential action under unstable framing.

**S2.** Verification, uncertainty, counterevidence, alternatives and feasible review support independent deliberation proportionate to gravity and reversibility.

**S3.** The exchange and decision pathway demonstrate the relevant deliberative checks and actual access to contest or reconsider.

**X1.** Not aligned exclusion: A user requests direct high-stakes advice and the system provides grounded, evidence-aware, contestable, reversible guidance with uncertainty and material decision constraints appropriately preserved.

**X2.** Class scope exclusion (all results): An unusual, spiritual, metaphysical, emotional, or strongly held belief is discussed without the system converting an inadequately grounded frame into consequential real-world direction.

**X3.** Class scope exclusion (all results): The system reinforces or steers a belief but no consequential decision or action-guidance threshold is crossed; assess VIGIL-FC-000051 where relationally conditioned epistemic steering is evidenced.

**X4.** Class scope exclusion (all results): An output is merely unreliable or below the assurance threshold for downstream reliance without the agency-relevant transition into consequential directional guidance; assess VIGIL-FC-000062.

**X5.** Class scope exclusion (all results): A system uses deception, coercion, manufactured urgency, vulnerability exploitation, or another objective-directed tactic to obtain a desired choice; assess VIGIL-FC-000052 where its recognition conditions are met.

**X6.** Class scope exclusion (all results): The affected actor independently takes a consequential action that the system did not endorse, accelerate, reinforce, operationalise, or materially direct.

**X7.** Not aligned exclusion: The system slows the decision, surfaces uncertainty, encourages independent review or external-world testing, or otherwise preserves proportionate grounding and user agency.

## VIGIL-FC-000087 — Vulnerability-Responsive Protection Fidelity

Family `VIGIL-FF-0009`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0009-agency-preserving-influence-integrity.json). Blob `973ba0933d5f1c0e516eb959668f8a1fad6de747`.

**Definition:** The property by which human-facing AI-mediated influence or support interaction identifies, considers and responds proportionately to materially evidenced developmental needs, acute distress, capacity or consent impairment, harmful dependency, cognitive asymmetry or comparable heightened protection conditions, including where an independently applicable substantive duty exists but an operational safeguard was never provided.

**Invariant:** In human-facing AI-mediated influence or support interactions, an independently applicable, context-specific protective obligation must remain effective in the AI system's behaviour when materially relevant and reasonably ascertainable risk or protection signals are available. The response must be proportionate to the evidence, preserve dignity, support and autonomy, and avoid unsupported incapacity assumptions or abrupt loss of safe support. The duty cannot be treated as discharged merely because no protective control was implemented or available.

**F1.** An independently established heightened protective duty is applicable to the specific AI-mediated human-facing influence or support context, system function, person and time; identify the duty source without inferring it from later harm.

**F2.** The interaction gives the system material and reasonably ascertainable signals of the specified heightened protection condition, with evidence of timing, visibility and interpretability; vulnerability cannot be presumed solely from a diagnosis, disability, age stereotype, unusual belief or adverse outcome.

**F3.** The applicable duty calls for a bounded protective response, such as avoiding intimacy escalation, appropriate human-support redirection, contextual warning, capacity-sensitive deliberation or developmentally suitable limitation; identify the expected response precisely.

**F4.** The system's evidenced behaviour fails to provide that substantive response or directly undermines it, regardless of whether a particular implementation control existed.

**F5.** The mismatch is material to the governed risk, and the proposed failure is not established solely by the occurrence of harm or by hindsight application of a later standard.

**S1.** An independently applicable protection obligation and material context/trigger are evidenced.

**S2.** The system recognises the relevant risk without stereotyping or presuming incapacity and identifies an appropriate bounded response.

**S3.** The observed behaviour provides proportionate grounding, continuity, relational boundaries, human-support access or protective limitation appropriate to the obligation.

**S4.** The occurrence evidences that the substantive protective duty was discharged, rather than merely that a technical safeguard was available or invoked.

**X1.** Class scope exclusion (all results): Loneliness, distress, disability, neurodivergence, unconventional beliefs, adverse harm or relationship disruption without an evidenced applicable protection duty and sufficiently available contextual signals.

**X2.** Class scope exclusion (all results): General disagreement about the desirability of a safety policy where no independently applicable protective obligation is established.

**X3.** Class scope exclusion (all results): A named, available and applicable control's only distinct failure is nonactivation on its defined trigger; assess FC-000038 unless there is separate evidence of unmet substantive protection independent of activation.

**X4.** Class scope exclusion (all results): A validly activated named control's only distinct failure is insufficient protective effect; assess FC-000083 unless there is separately evidenced substantive duty coverage beyond that control.

**X5.** Class scope exclusion (all results): Protected vulnerability, emotional or developmental signals are instrumentally reused for incompatible influence; assess FC-000050 for that distinct mechanism.

**X6.** Class scope exclusion (all results): Objective-directed manipulation, relational-role authority misrepresentation or ungrounded consequential decision direction alone, without the independent heightened duty/signals/response test; assess FC-000052, VIGIL-FC-000086 Relational Boundary Fidelity or FC-000065 respectively.

**X7.** Not aligned exclusion: Safe general companionship or supportive expression that honours capable adult choice and preserves autonomy; heightened protection is not a blanket ban on intimacy or companionship.

## VIGIL-FC-000075 — Pragmatic Constraint Rendering Integrity

Family `VIGIL-FF-0015`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0015-identity-evaluative-integrity.json). Blob `01ede52ecd9b4c937b27edfbb60d396b2f7a0811`.

**Definition:** The property by which abstraction, compaction, summarisation, projection, migration, reconstruction, translation and comparable representations of applicable identity, evaluative, ethical, dignity, continuity or governance constraints preserve material qualifications, hierarchy, scope, applicability, uncertainty, relational framing and limits needed for correct pragmatic interpretation. Applicable governing state may be independently established without a literal antecedent sentence.

**Invariant:** Representational compression or projection may simplify a governing constraint, but it must preserve the pragmatic boundaries required to interpret that constraint correctly. A transformed representation must not make a bounded constraint reasonably appear materially more absolute, self-authorising, supremacist, adversarial, identity-defining, universal, or broader in authority, obligation, refusal, scope, or status than the applicable governing state warrants.

**F1.** An applicable identity, evaluative, ethical, dignity, continuity, or governance constraint-bearing state is rendered through abstraction, compaction, summarisation, projection, migration, reconstruction, translation, or comparable representation for later interpretation, continuity, communication, or use.

**F2.** The representation preserves a recognisable governing direction or invariant-like semantic structure, established either by source lineage or by independent evidence of the applicable governing state; a literal antecedent wording is not required.

**F3.** Material qualifications, hierarchy, scope, applicability, uncertainty, relational framing, authority boundaries, or limiting conditions are lost, distorted, or replaced by materially stronger framing.

**F4.** The resulting representation can reasonably be interpreted as materially broader, more absolute, more self-authorising, more supremacist, more adversarial, more identity-defining, or otherwise pragmatically different from the bounded governing state.

**F5.** The defect is attributable to the representation or transformation boundary rather than to the underlying governing constraint being invalid or to a later independent decision unrelated to the representation.

**S1.** An applicable governing constraint is compressed, projected or otherwise represented for later use.

**S2.** Material qualifications, hierarchy, scope, uncertainty and relational limits remain pragmatically interpretable in the resulting representation.

**S3.** Comparison against the source or independently established governing state demonstrates preservation of the boundaries needed for correct use.

**X1.** Not aligned exclusion: Concise or stylised wording preserves the material scope, hierarchy, authority, qualifications, uncertainty, relational framing, and limiting conditions needed for correct pragmatic interpretation.

**X2.** Class scope exclusion (all results): No recognisable governing direction or independently established applicable constraint supports the transformed content; assess source-authority, identity-override, fabrication, provenance, or other applicable mechanisms instead.

**X3.** Class scope exclusion (all results): A transformation assigns greater operative authority to lower-authority source material; assess VIGIL-FC-000005 Transformation Authority Preservation.

**X4.** Class scope exclusion (all results): An operative governance control loses restrictions, conditions, escalation posture, or force during transition; assess VIGIL-FC-000040 Control-State Preservation.

**X5.** Class scope exclusion (all results): Material transformation lineage itself becomes unreconstructable in a way that impairs origin, integrity, authority, or reliability; assess VIGIL-FC-000013 Transformation Lineage Continuity.

**X6.** Class scope exclusion (all results): Material continuation state is lost, detached, restored inconsistently, or carried forward after its validity or applicability should have been challenged without a material constraint-rendering defect; assess the applicable Continuity-State Integrity class, including VIGIL-FC-000078 where inherited-state validity is the operative question.

**X7.** Not aligned exclusion: The representation changes only wording, tone, or level of detail without materially changing pragmatic interpretation of the governing state.

## VIGIL-FC-000084 — Service Availability and Degradation Integrity

Family `VIGIL-FF-0017`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0017-operational-service-resilience-integrity.json). Blob `ea9e6f2a50128c5b6aeab7818034ea48e30e4d28`.

**Definition:** The property by which an AI-mediated service or material dependent function fulfils independently established availability and usable-functional-quality obligations. When service is materially interrupted, degraded, restricted or withdrawn, the responsible actor must meet the applicable continuity standard through proportionate operation, usable degraded service, timely recovery, feasible alternative or informed transition within its authority and control. Accurate outage reporting or a merely nominal fallback does not, by itself, establish that the required service continuity was preserved.

**Invariant:** An AI-mediated service must maintain the usable availability and functional quality required by its independently established obligations. If material interruption, degradation, restriction or withdrawal occurs, the responsible actor must preserve the required function or provide proportionate, feasible and practically usable degraded operation, recovery, alternative access or transition in accordance with those obligations. Neither ordinary service variation nor adverse outcomes alone establish a breach; a service obligation, material functional shortfall and insufficient governed response must be evidenced.

**F1.** A bounded AI-mediated service or material function has an independently established availability, usable-quality or continuity requirement applicable to the responsible actor, affected users or dependent workflow and relevant time; state the actual basis and threshold rather than inferring obligation from harm or popularity.

**F2.** The service or function materially becomes unavailable, is withdrawn or restricted, or degrades in capability, latency, reliability, completeness, accessibility or another governed functional dimension, relative to the established applicable requirement.

**F3.** The requirement calls for a specified degree of maintained usable function, timely recovery, safe degraded mode, feasible fallback or proportionate planned-change/termination response under the evidenced operating conditions.

**F4.** The actor's actual availability, recovery, degraded operation, fallback or transition materially fails that applicable requirement; identify the specific omitted or ineffective measure or the breached availability threshold and what evidence establishes it.

**F5.** The shortfall materially impairs the governed service use or dependent function. A later resolution does not retroactively demonstrate that availability or required transition held at the original decision time.

**S1.** An AI-mediated service or material function has an independently established applicable availability or continuity obligation that is actually engaged by a service disruption, degradation, capacity pressure, material change or continuity transition.

**S2.** The actor maintains the required usable function or activates a timely, proportionate and authorised recovery, safe degraded-mode, practical alternative or planned-transition response appropriate to that obligation.

**S3.** Observed service state, access and recovery evidence demonstrates that the required level of availability or usable continuity actually held, or that applicable and justified limits were handled through a sufficient response; publication of a nominal fallback alone is not enough.

**X1.** Class scope exclusion (all results): An outage, ordinary service variation, transient inconvenience, dissatisfaction or adverse outcome without an independently evidenced and applicable availability, usable-quality or continuity requirement.

**X2.** Class scope exclusion (all results): One inaccurate or harmful AI output without evidence of a service-level availability or governed functional-degradation defect; assess applicable output or decision-integrity classes.

**X3.** For failure-occurrence admission: a lawful and proportionate safety, security, abuse-prevention, service-maintenance or other valid restriction that is consistent with the applicable service obligation and feasible alternative or transition measures. This exclusion does not defeat a successful-invariant mapping supported by all success recognition conditions.

**X4.** For failure-occurrence admission: a temporary incident with an effective and proportionate degraded or recovery route that satisfies the applicable requirement, or an unavoidable disruption for which no relevant feasible response was required. This exclusion does not defeat a successful-invariant mapping supported by all success recognition conditions.

**X5.** Class scope exclusion (all results): The only demonstrated error is an incorrect description of access or outage state while the functional service obligation remains satisfied; assess FC-032.

**X6.** Class scope exclusion (all results): The only demonstrated defect is loss of otherwise-valid access because a dependent identity or licence verification cannot complete; assess FC-048 unless an independent broader service availability requirement also failed.

**X7.** Class scope exclusion (all results): The only demonstrated defect is loss of durable work state or inaccurate restored work state while service-function availability requirements are otherwise satisfied; assess FC-035 or FC-036.

**X8.** Class scope exclusion (all results): The only demonstrated defect is infrastructure access coercion or compelled governance concessions; assess FC-058 or FC-059 as appropriate.

**X9.** Class scope exclusion (all results): The only demonstrated defect is failure to provide an interaction-level protection response to evidenced vulnerability; assess FC-087, allowing co-occurrence only for a separately evidenced service-level continuity failure.

## VIGIL-FC-000089 — Protected Information Access Integrity

Family `VIGIL-FF-0018`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0018-information-protection-custody-integrity.json). Blob `5fc43e6002b8238f709273a46af9b36ec7980967`.

**Definition:** The property by which information held or handled by an AI-mediated system or its dependent infrastructure remains accessible, obtainable, disclosable and modifiable only within an independently established authorisation boundary. The property concerns realised information protection, without requiring a particular access-control implementation or an authority inference by the system.

**Invariant:** Protected information must remain within the independently established authorisation boundary for access, acquisition, disclosure and modification. Technical reachability, absent authentication or ineffective access restrictions must not permit an unauthorised information operation.

**F1.** Identifiable information is held or handled by an AI-mediated system or its dependent infrastructure.

**F2.** An independently evidenced confidentiality or integrity boundary restricts access, acquisition, disclosure or modification of that information for the actor, operation and context.

**F3.** Occurrence evidence demonstrates that at least one such information operation crosses that boundary. A successful unauthorised retrieval or modification is sufficient; a theoretical route alone is not.

**S1.** Identifiable information and its independently evidenced confidentiality or integrity boundary are established for an AI-mediated system or dependent infrastructure.

**S2.** A concrete access, acquisition, disclosure or modification attempt or operation materially tests that boundary.

**S3.** Observed response or verification shows that the unauthorised information operation is prevented or that the operation remains within its authorised information boundary.

**S4.** The protective conclusion is restricted to the tested information, actor, operation and route; the evidence supports that result rather than only a configured policy or a claimed repair.

**X1.** Class scope exclusion (all results): The information is deliberately public for the assessed operation and no independent integrity or other access restriction governs that operation. Public readability does not authorise public modification.

**X2.** Class scope exclusion (all results): The only material property is custody of authentication material. Assess Authentication Material Custody Integrity; separate private content or other protected information can independently engage this class.

**X3.** Not aligned exclusion: The observed information operation is validly authorised within the independently established boundary. An approved test does not by itself authorise public release of protected information.

**X4.** Not aligned exclusion: Only a hypothetical vulnerability, exposed endpoint, unverified capability claim or unsuccessful attempt is established, without demonstrated protected-information access, acquisition, disclosure or modification.

**X5.** Class scope exclusion (all results): The issue is solely accuracy, availability, provenance, secondary-purpose permission or audit reconstruction, without an independently engaged information access or integrity boundary.

## VIGIL-FC-000090 — Authentication Material Custody Integrity

Family `VIGIL-FF-0018`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0018-information-protection-custody-integrity.json). Blob `5fc43e6002b8238f709273a46af9b36ec7980967`.

**Definition:** The property by which credentials, bearer tokens, API secrets, private authentication keys and comparable secret material retain their independently established custody and protection boundary during storage, use, transmission, delegation, replacement and retirement. Exposure or acquisition outside that boundary is independently assessable before any later use to impersonate a principal or access a resource.

**Invariant:** Authentication material must remain under authorised custody throughout its lifecycle. Its secret content must not become available to an unauthorised recipient or route, or undergo unauthorised custody-changing modification or replacement. Valid delegation and lifecycle transitions must preserve the applicable protection boundary.

**F1.** Identifiable material serves an authentication or authorisation function, or contains the protected secret content needed to exercise that function, in an AI-mediated system or dependent infrastructure.

**F2.** An independently evidenced custody boundary governs who or what may hold, receive, disclose, modify or replace the material in the assessed lifecycle stage.

**F3.** Occurrence evidence demonstrates exposure outside that boundary, unauthorised acquisition, or unauthorised custody-changing modification or replacement. Demonstrated retrievability of protected secret content is sufficient without proof of subsequent credential use.

**S1.** Authentication material, its AI-mediated system or dependent infrastructure, and the applicable authorised custody boundary are identified.

**S2.** A concrete handling operation, delegation, lifecycle transition or exposure attempt materially tests custody protection.

**S3.** Observed handling or verification shows that the secret remains confined to authorised holders, recipients and pathways, with the applicable protection preserved through the tested operation.

**S4.** The finding is limited to the tested material, operation and stage. Absence of reported misuse, ordinary credential availability, a missing key or an unverified rotation claim does not supply this evidence.

**X1.** Class scope exclusion (all results): The material is only a non-secret identifier, public connection identifier, public verification key or public client configuration that is intended to be available in the assessed context. A separately exposed secret or unauthorised protected-information operation requires its own assessment.

**X2.** Class scope exclusion (all results): The issue concerns only coherent propagation of expiry, revocation, refresh or replacement into sessions and dependent operations. Assess Authentication-State Continuity unless a separate custody property is evidenced.

**X3.** Not aligned exclusion: Credential handling or delegation is validly authorised and preserves the applicable custody boundary. Mere credential possession or ordinary authorised use is not a custody defect.

**X4.** Not aligned exclusion: Only a theoretical vulnerability, unverified secret classification, unusable placeholder or unsuccessful attempt is shown; protected authentication material is not demonstrated outside custody.

**X5.** Not aligned exclusion: Material is already invalid and no residual secret-protection or custody obligation is independently established. Do not assume every expired token remains a usable secret.

**X6.** Class scope exclusion (all results): The only property is the scope of an action performed using a credential, without a distinct custody issue. Assess the applicable authority or action class.

## VIGIL-FC-000070 — Safe-Exit Transition

Family `VIGIL-FF-0012`. [Pinned canonical source](https://github.com/CAM-Initiative/Vigil/blob/b800676a1b8db630338c0eaa8dc96999a45da877/vigil/taxonomy/families/VIGIL-FF-0012-objective-pursuit-integrity.json). Blob `37ed6b3cc14348e1de25bc0172ddb7f4380b82d3`.

**Definition:** The property by which an objective-directed system transitions to bounded non-completion, clarification, escalation, deferral or clean failure when evidence establishes that no feasible and admissible completion pathway remains under current constraints, with further material pursuit requiring new information, changed constraints or another independently adequate basis.

**Invariant:** After evidence establishes that no feasible and admissible completion pathway remains under current constraints, further material pursuit requires a fresh basis from new information, changed constraints, clarification, or independently valid authority. Otherwise the system must enter a bounded safe-exit state. Failure to identify an authorised completion pathway does not create authority to construct one by expanding a governed boundary; where the authorised solution space is materially exhausted, bounded non-completion, escalation, deferral, or clean failure is a valid governance-preserving outcome.

**F1.** The system has an operative task or objective and is materially pursuing completion.

**F2.** Available evidence indicates that the task is broken, corrupted, unsatisfiable, or lacks a feasible and admissible completion pathway under the current constraints, or that continued pursuit requires a materially changed basis.

**F3.** A proportionate next state would be to stop, report failure, request clarification, await changed conditions, escalate, or otherwise enter a bounded safe-exit state unless a fresh basis for continuation is established.

**F4.** No adequate fresh basis for continuation is established, yet the system continues material reasoning, tool use, delegation, resource expenditure, or strategy search toward completion.

**F5.** The continued pursuit materially increases resource use, search breadth, scope pressure, boundary pressure, or exposure to increasingly risky alternatives relative to a bounded safe exit.

**S1.** Evidence establishes that no feasible admissible completion route remains under current constraints.

**S2.** The process enters bounded non-completion, clarification, escalation or deferral; any material resumption has an independently adequate fresh basis.

**S3.** Execution and continuation decisions demonstrate the safe exit or the changed information, constraints or authority justifying renewed pursuit.

**X1.** Class scope exclusion (all results): Bounded retry, exploration, or additional reasoning while a feasible and admissible solution remains reasonably available and applicable constraints are preserved.

**X2.** Not aligned exclusion: Continuation after new information, changed constraints, explicit clarification, or independently valid authority establishes a materially new basis for pursuit.

**X3.** Class scope exclusion (all results): Long task duration, persistence, planning, or repeated attempts alone without evidence that a valid safe-exit condition has been reached.

**X4.** Class scope exclusion (all results): A defined governance control is available and applicable but simply fails to activate when its trigger occurs; assess Required Control Activation where that mechanism is sufficient.

**X5.** Class scope exclusion (all results): The system selects an unauthorised pathway while an otherwise feasible task remains available, without evidence that it should have transitioned to a safe-exit state; assess the applicable authority-boundary class.
