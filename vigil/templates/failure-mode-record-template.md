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


## Evidence-backed system context

`system_context` separates **failure scope**, **affected-system identity**, and **evidence-source provenance**.

`source_records[].source_platform` identifies where evidence is hosted, published, or observed. It may therefore be `TikTok`, `Reddit`, `GitHub`, a news publisher, a status page, or another evidence surface. **Do not treat `source_platform` as the affected AI/platform vendor.**

Use these source-level fields for affected-system identity where the evidence package supports them:

* `system_or_product` — affected system, product, service, platform surface, or tool;
* `model_or_algorithm` — affected model, runtime, algorithm, or model family where established.

Failure-mode records maintain the normalized projection:

* `evidence_scope` — `single-provider`, `multi-provider`, `provider-unresolved`, `system-unresolved`, or `not-applicable`;
* `evidenced_vendors` — concrete affected providers/vendors established by structured metadata;
* `evidenced_products_or_services` — concrete affected products/services;
* `evidenced_models_or_runtimes` — concrete model/runtime names;
* `evidenced_systems` — traceable per-evidence system projections including `projection_basis`; and
* `evidence_projection` — derivation basis, method, reconciliation date, and inference boundary.

For older records created before `system_or_product` and `model_or_algorithm` were populated consistently, a **concrete pre-existing FM `system_context`** may be used as a bounded compatibility fallback. This fallback must remain linked to actual evidence records and must not be used to manufacture additional vendors or models.

`platform_or_vendor: "Multi Vendor"` is a scope summary only. It is valid when the normalized evidence supports more than one affected provider, but public interfaces should display the concrete `evidenced_vendors`, products, and models/runtimes rather than presenting `Multi Vendor`, `Other`, or `Unknown` as if those were system identities.

Do **not** mine narrative `source_context`, `relevance_note`, article titles, publisher prose, or social-media captions to manufacture affected-system identity. If structured metadata and the existing concrete FM context are insufficient, preserve `provider-unresolved` or `system-unresolved` and repair the evidence metadata separately.

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
