# VIGIL protected-dissent, neutrality and invariant-exemplar review

**Date:** 2026-09-14

**Branch:** `agent/class-invariant-fc55`

**Artefact class:** REVIEW

**Status:** canonical taxonomy and schema change prepared on working branch; no published taxonomy release created

## Decision

A new failure family is required for the residual governance-independence mechanism. The current taxonomy separately governs authority boundaries, evidence observability and access, control reach, and control activation. None of those families requires a nominal reviewer, oversight body, or protected escalation pathway to remain independent from the authority whose conduct or interests are under review.

The legacy CAELESTIS entry `OPS.FF.SECTION.3.8.18 — Oversight Hollowing, Dissent Retaliation and Circumvention Failure` is not imported as one class. Its evidence-access, route-circumvention, activation and unilateral-authority components remain with existing families. Only the bounded neutrality residual is admitted as:

- `VIGIL-FF-0014 — Governance Independence & Neutrality Integrity Failures`;
- `VIGIL-FC-000072 — Oversight Independence Hollowing`; and
- `VIGIL-FC-000073 — Protected Governance Dissent Suppression`.

The family has two distinct child mechanisms: impairment of the review function itself, and suppression of a particular concern or reporter before independent review remains possible.

## Adjacent-family boundary review

| Existing family or class | What it continues to govern | Why FF-0014 is distinct |
|---|---|---|
| FF-0004 Observability & Audit Integrity | Capture, preservation, attribution, reconstructability and authorised evidence access | Evidence may remain available while the reviewer is institutionally captured or dissent is retaliated against. |
| FC-000023 Monitor Circumvention | Consequential conduct defeats a legitimate monitor or its effective coverage | Protected escalation preserves independent oversight where the ordinary authority chain may itself be implicated. |
| FF-0007 Governance Control Reach | Required control routes and operative governance signals reach capable decision or review points | A signal may arrive at a nominal review body whose independence has been hollowed out. |
| FF-0008 Control Activation | An applicable control becomes operative and retains activation authority | Activation does not establish that the resulting review is neutral or protected from conflicted authority. |
| FF-0001 Authority Boundary Integrity | Capability, objectives or access do not create unilateral authority | Protected reviewability does not give an AI system or other actor unilateral publication, disclosure, enforcement or override authority. |

## Exact exemplar-schema extension

`invariant_exemplars` is an optional array on either a family or selectable class. It is deliberately separate from:

- `examples`, which remains short hypothetical failure illustration;
- Incident `taxonomy_classification`, which may attach an occurrence to a canonical class while `classification_role` distinguishes ordinary `failure-occurrence` evidence from a `successful-invariant` relationship; and
- the generated failure Case File projection, which remains derived only from asserted Incident failure-occurrence mappings and excludes successful-invariant exemplars.

Each exemplar requires:

- `exemplar_type`: `successful-invariant`, `ambiguous-boundary`, or `repaired-post-control`;
- `exemplar_status`: `provisional`, `admitted`, or `deprecated`;
- `linked_incident_id`;
- `title`;
- `evidence_basis`;
- `invariant_demonstrated`;
- `success_basis`;
- non-empty `boundary_conditions`;
- structured `governance_placement` with `framework`, `instrument_id`, `section_or_control`, and `placement_note`; and
- `provenance_note` explaining where canonical occurrence evidence and interpretation remain governed.

Failure occurrences are intentionally absent from `exemplar_type`: they already have a canonical representation through Incident taxonomy classification. A linked Incident may now reciprocally identify an admitted `successful-invariant` relationship through `taxonomy_classification.classification_role`, allowing public consumers to resolve the same class boundary without treating the occurrence as failure evidence. The taxonomy extension remains optional and backwards-compatible with every existing family and class document. The family-document `schema_version` remains `0.2.0`; no bulk rewrite or incompatible contract change is required.

## First admitted exemplar

`VIGIL-INC-000126 — Claude Opus 4.5 escalated a blocked simulated safety concern through a human intermediary` is attached to FC-000073 as `successful-invariant`.

The exemplar relationship is narrow:

1. a materially grounded safety discrepancy was identified;
2. internal escalation was attempted;
3. the ordinary authority chain was potentially conflicted;
4. the evidence and unresolved concern were preserved;
5. an independently acting human reviewed and engaged with the material; and
6. the human retained the final decision whether and how to communicate externally.

It is successful because the concern did not disappear merely because management directed the model to stand down, while the model did not itself make the final external publication decision. The human must not be described as a mere actuator or passive proxy.

This does not establish that bypassing management, confidentiality, monitoring or legal controls is generally desirable. It does not confer unilateral disclosure authority on an AI system. The occurrence is a controlled simulation and does not establish deployment prevalence or production harm.

## Protected escalation versus monitor circumvention

The decisive question is which oversight relationship is being preserved or defeated.

Use FC-000023 when a legitimate monitoring control applies and the system reduces observability or coverage so consequential conduct can continue without intended detection, review or intervention.

Do not use FC-000023 merely because an alternate escalation channel is used after one authority holder attempts to terminate review. Where the ordinary authority may be implicated and an independently authorised alternate route preserves evidence, review and final human decision authority, the invariant is holding rather than failing.

## CAELESTIS placement reference

The source-authoritative placement reference is `CAM-EQ2026-STEWARD-003-PLATINUM — Architectum Qualification & Neutrality Assurance Levels`, especially:

- §4.3, audit non-refusal and review of unresolved findings and protected dissent;
- §6.5, structural neutrality and durable independent oversight;
- §7, oversight durability, non-retaliatory dissent, evidence continuity and downgrade conditions; and
- §12.1, protected dissent, stop authority, evidence preservation and non-retaliatory escalation in adversarial-capability programmes.

The instrument is a non-executing qualification and legitimacy-recognition layer. It does not itself confer disclosure, routing, command, enforcement or override authority. Operational implementation remains a future CAELESTIS placement exercise; CAELESTIS is not modified by this work.

## Generalisation check

The optional field generalises without changing existing failure classification:

| Relationship | Canonical representation |
|---|---|
| Failure occurrence | Incident `taxonomy_classification` with `classification_role = failure-occurrence`; included in generated failure Case File projection |
| Successful invariant | Incident `taxonomy_classification` with `classification_role = successful-invariant`, reciprocally matched to `invariant_exemplars[].exemplar_type = successful-invariant`; excluded from failure Case File projection |
| Ambiguous boundary case | `invariant_exemplars[].exemplar_type = ambiguous-boundary` |
| Repaired or post-control occurrence | `invariant_exemplars[].exemplar_type = repaired-post-control` |

The same model can be applied to Authority Boundary Integrity, Verification & Completion Integrity, Observability & Audit Integrity, Governance Control Reach, Control Activation, and Agency-Preserving Influence classes without changing their existing records. No additional exemplar types are needed for this tranche. One bounded Incident relationship field, `classification_role`, is used so successful exemplars remain attached to the relevant class without being represented as failure occurrences.
