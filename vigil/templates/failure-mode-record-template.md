# VIGIL Failure Mode Record Template

Failure Mode records capture confirmed, strongly evidenced, recurring, or sufficiently clear failure patterns that require classification and triage.

## Boundary rules

* Use `record_type: "failure_mode"` and IDs like `VIGIL-YYYY-FM-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Use authoritative proposal and PATCH arrays only for this failure's own repair chain.
* Do not add `linked_records.related_failure_modes` or convert peer-FM similarity into contextual relations. Similarity and class membership belong to the taxonomy layer.
* Include `failure_mode_definition`, `failure_threshold`, `failure_classification`, and `triage`; during the taxonomy-free transition, `failure_classification` preserves substantive fields such as severity, harm, scope, recurrence, persistence, reproducibility and visibility but contains no formal taxonomy fields.
* `failure_classification.faceted_analysis` is additive. Existing records do not require retrospective facet population. New or materially reassessed records SHOULD use it when evidence permits.
* Do not include proposal implementation claims or patch-note fields.
* CAM routing must use affected CAM routing only: `cam_internal.affected_*` fields because the record has triage-relevant failure classification.

Required FM sections are identity, summary, CAM relevance, failure definition, threshold, evidence confidence, `source_records`, system context (including `platform_or_vendor`, `product_or_service`, `specific_model_or_runtime`, and `interface_surface`), failure classification, triage, jurisdictional context, linked records, and affected CAM routing.

## Faceted failure reporting

The faceted analysis records independent incident-reporting dimensions without assigning a formal failure-taxonomy class.

Where evidence permits, use `failure_classification.faceted_analysis` to keep the following questions separate:

* `event_state` — whether the record concerns an anomaly, hazard, near miss, incident, confirmed failure, or an unresolved state;
* `manifestation` — what was actually observed or represented at the interaction/system surface;
* `mechanism_or_cause` and `cause_status` — the candidate mechanism and how strongly causation is established;
* `failure_locus` — the component or interface at which the failure arose or became observable;
* `repair_side` — where remediation responsibility currently belongs; this may differ from the failure locus;
* `execution_phase` — where in the execution trajectory the failure occurred;
* `observability` — overt, latent, silent, differentially observable, externally detected, user reported, or unknown;
* `evidence_state` — reported, observed, corroborated, reproduced, root-cause confirmed, provisional, or unknown;
* `effect_or_harm` — the resulting or evidenced consequence, kept separate from severity;
* `propagation` — local, downstream, cascading, cross-provider, systemic, or unknown;
* `completion_state` — including premature termination, non-termination, and false completion;
* `verification_state` — whether verification was absent, incomplete, incorrect, passed, failed, or unresolved; and
* `execution_pattern` — including repeated-step, looping, retry amplification, and degraded-but-functional execution.

Do not infer a root cause because the schema offers a field. Use `unknown`, `hypothesised`, or `provisional` states where the available evidence does not support a stronger conclusion. A user-visible symptom may arise at one locus while remediation belongs at a different component or governance layer.

The faceted block is intentionally optional for legacy records. Absence means the facets have not been recorded; it does not imply a negative finding.

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
