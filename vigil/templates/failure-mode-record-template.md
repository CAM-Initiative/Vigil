# VIGIL Failure Mode Record Template

Failure Mode records capture confirmed, strongly evidenced, recurring, or sufficiently clear failure patterns that require classification and triage.

## Boundary rules

* Use `record_type: "failure_mode"` and IDs like `VIGIL-YYYY-FM-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Use authoritative proposal and PATCH arrays only for this failure's own repair chain.
* Put adjacent failures, shared controls, contrasts, and precedents in `linked_records.contextual_relations` with `chain_inclusion: false`.
* Include `failure_mode_definition`, `failure_threshold`, `failure_classification`, and `triage`; `failure_classification` must include `failure_family`, `canonical_failure_group`, `taxonomy_reference`, `related_failure_groups`, `persistence`, `reproducibility`, and `visibility`.
* Do not include proposal implementation claims or patch-note fields.
* CAM routing must use affected CAM routing only: `cam_internal.affected_*` fields because the record has triage-relevant failure classification.

Required FM sections are identity, summary, CAM relevance, failure definition, threshold, evidence confidence, `source_records`, system context (including `platform_or_vendor`, `product_or_service`, `specific_model_or_runtime`, and `interface_surface`), failure classification, triage, jurisdictional context, linked records, and affected CAM routing.


## Multi Vendor authoring

Use `platform_or_vendor: "Multi Vendor"` only when the record is genuinely supported by source evidence from more than one vendor or platform.

Multi Vendor records must include non-empty `vendor_cluster` and `primary_evidenced_vendors` arrays. `product_or_service` must remain a single canonical value, not a comma-separated product or surface list. For genuinely multi-product / multi-vendor records, use `product_or_service: "Other"` unless a single canonical product clearly controls the record. Put detailed product, model, surface, deployment, and incident facts in `interface_surface`, `model_or_product`, `deployment_context`, and `source_records`.

Example:

```json
"system_context": {
  "platform_or_vendor": "Multi Vendor",
  "vendor_cluster": [
    "OpenAI",
    "Anthropic"
  ],
  "primary_evidenced_vendors": [
    "OpenAI",
    "Anthropic"
  ],
  "product_or_service": "Other",
  "interface_surface": "Multiple evidenced access surfaces; specify details in source_records and deployment_context."
}
```

Rationale: Multi-vendor records require separated vendor evidence because top-level database fields are controlled values for indexing, filtering, validation, and UI routing. Detailed vendor, product, surface, and source claims belong in evidence metadata, not comma-combined canonical fields.

## Severity and triage model 2.0

New failure-mode records must declare `triage.model_version: "2.0"`.

Severity and priority are independent:

* Severity uses `S0` catastrophic, `S1` critical, `S2` high, `S3` moderate, `S4` low, or `SU` unassessed.
* `SU` requires `failure_classification.severity_assessment_gap` and a concrete assessment next step.
* Priority uses `P0` immediate, `P1` urgent, `P2` planned, `P3` routine, `PN` no active priority, or `PU` priority unassessed.
* P0–P3 require a concrete action. P0 and P1 also require a named owner, action basis, and review horizon.
* `PN` does not mean low severity or no ecosystem monitoring. `PU` is temporary and requires `triage_assessment_gap`.
* `triage.triage_status` is the workflow-status field. Use only `intake`, `under-assessment`, `action-required`, `repair-in-progress`, `verification-pending`, `monitoring`, `blocked`, `closed-actioned`, `closed-no-action`, or `superseded`.
* Append evidenced priority transitions to top-level `triage_history`. Do not reconstruct or backdate a legacy transition.
