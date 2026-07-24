# VIGIL Patch Note Record Template

Patch Note records capture CAM-specific corpus changes that have actually been implemented, or pre-existing Caelestis controls that a retrospective repair decision explicitly relied upon. VIGIL maintenance is not a corpus PATCH.

## Boundary rules

* Use `record_type: "patch"` and IDs like `VIGIL-YYYY-PATCH-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Set `repair_scope.primary_failure_mode` to the one failure repaired by this PATCH by default.
* A multi-failure PATCH is exceptional: explain why one indivisible repair closes every listed failure and provide one `verification_by_failure_mode` result for each.
* Put adjacent failures, precedents, contrasts, and consequential benefits in `linked_records.contextual_relations` with `chain_inclusion: false`.
* Put `decision_trace` and `corpus_implementation` before the longer narrative and provenance fields in the JSON record.
* Include `date_implemented`, `decision_trace`, `corpus_implementation`, `record_reconstruction`, `change_classification`, `change_details`, `implementation_verification`, `impact_summary`, and `remaining_work`.
* Set `record_reconstruction.reconstructed` to `true` only when an earlier PATCH was rebuilt; native trace-first records use `false` and disclose that lineage explicitly.
* Every `corpus_implementation.entries[]` item must name one Caelestis instrument, its canonical repository path, exact section and heading, change kind, literal resulting wording, source commit, direct commit-addressed link, and verification state.
* Capture literal prior wording when it is materially relevant. Otherwise explain the absence with `prior_text_status`.
* A retrospective coverage record must use `implementation_type: "pre-existing-control"` and `change_kind: "relied-upon"`; it must never imply that the quoted clause originated on the VIGIL record date.
* A branch-only implementation remains `record_state: "active"` until the cited text reaches canonical main or the work is abandoned.
* Include implemented-change evidence in `source_records` and `implementation_verification.evidence`, but do not use either as a substitute for literal `corpus_implementation` text.
* CAM routing must use changed CAM routing only: `cam_internal.changed_*` fields.
* Schema, template, validator, automation, registry, interface, or documentation maintenance inside VIGIL is observatory maintenance and must never be recorded as a corpus PATCH.

Required PATCH sections are identity, decision trace, literal corpus implementation, system context, implementation date, `change_classification`, `change_details`, `implementation_verification`, impact summary, remaining work, `source_records`, linked records, changed CAM routing, reconstruction disclosure, interpretive provenance, and migration notes where applicable.
