# VIGIL Record Lifecycle and Routing Model

VIGIL is an evidence-to-repair governance ledger. It preserves source evidence, classification/routing state, proposals, repairs, and source trail for observations, failure modes, proposals, and patch records.

This lifecycle is **conditional, not mandatory**. A record may begin as an observation, failure mode, proposal, or patch depending on the evidence and governance state. The arrows below describe common routing pathways and conditional transitions, not a compulsory sequence.

VIGIL records are not binding CAM doctrine. CAM adoption, amendment, and authoritative interpretation remain governed by CAM instruments and CAM amendment processes. Generated registry files are derived outputs from individual records and must not be manually edited.

## Observation records

Observation records preserve source evidence, early warning signals, platform behaviours, incidents, anomalies, public claims, research leads, or governance-relevant events.

They answer:

* What was observed?
* Where did the evidence come from?
* What system, platform, or product was involved?
* Why might this matter?
* Does this resemble a known failure mode?
* What is the next review action?

Observation records are source-data-first. They must not contain full failure classification, proposal logic, or patch implementation logic. They may include possible taxonomy mapping, related/similar CAM routing, or related/similar failure references where classification is not settled.

## Failure mode records

Failure mode records define a recurrent, structural, or governance-significant pattern of failure.

They answer:

* What is the failure pattern?
* What threshold makes it this failure mode?
* Which CAM taxonomy family does it route through?
* What harms, interests, or governance layers are implicated?
* What triage path is required?

Failure mode records must align with the CAM Runtime & Governance Failure Taxonomy in `CAM-EQ2026-OPERATIONS-003-SUP-01`.

If a failure does not fit a known canonical taxonomy family, it must not invent a new canonical group. It should either:

* route under the closest existing canonical group with a local or provisional subtype;
* use `provisional` only where justified; and
* create or link to a proposal for taxonomy extension when canonical coverage may need amendment.

Local concepts, harm vectors, and proposed subtypes may be recorded, but canonical-only fields must use canonical taxonomy values from the VIGIL schema-derived CAM taxonomy registry.

## Proposal records

Proposal records are for suggested governance, taxonomy, schema, validator, interface, workflow, or CAM corpus changes.

They answer:

* What should be changed?
* Why is a change needed?
* What instrument, schema, or workflow is affected?
* What decision or review is required?
* What would count as acceptance or next action?

A proposal is needed when:

* the taxonomy lacks an adequate family or subtype;
* the schema needs new fields or constraints;
* the validator needs new checks;
* a CAM instrument may need amendment;
* a UX/interface repair is needed but not yet implemented; or
* the repair pathway is not yet adopted or implemented.

Proposal records must not claim implementation as complete. Implemented work belongs in a patch or patch-note record.

## Patch / patch-note records

Patch records document implemented or recorded repair actions.

They answer:

* What changed?
* When was it implemented or recorded?
* What failure, proposal, or issue does it repair?
* What evidence verifies implementation?
* What impact does it have?
* What remains open?

A patch is appropriate when the corrective action is sufficiently defined and recorded, or where a placeholder patch is replaced with a substantive repair record.

Patch records must contain implementation evidence and the required fields:

* `date_implemented`
* `change_classification`
* `change_details`
* `implementation_verification`
* `impact_summary`
* `remaining_work`

A VIGIL patch can record a repair pathway without itself amending CAM doctrine. If CAM adoption or amendment is required, that remaining work must be preserved explicitly.

## Lifecycle examples

```text
Observation → Failure Mode → Proposal → Patch
Observation → Proposal → Patch
Failure Mode → Proposal
Failure Mode → Patch
Patch → Remaining Work / Future Proposal
Observation → Monitoring / Closed No Action
```

These examples are routing patterns. They do not require every observation to become a failure mode, every failure mode to become a proposal, or every proposal to become a patch.


## Linked standards and CAM routing

`linked_records.standards` is reserved for external standards, regulatory instruments, formal standards-body materials, and widely recognised external governance references such as ISO, IEEE, NIST, OECD, the EU AI Act, the Digital Services Act, W3C, or C2PA.

CAM instruments are internal CAM governance instruments, not external standards references. CAM instrument identifiers such as `CAM-BS...` or `CAM-EQ...` belong in `cam_internal` routing fields: related/similar routing for observations, affected routing for failure modes, target routing for proposals, and changed routing for patches.

## Registry and source-of-truth rule

Individual JSON files under `vigil/records/` are the source of truth. The generated registry indexes are derived outputs and should be rebuilt with the VIGIL build script after record changes. Do not manually edit generated registry files.
