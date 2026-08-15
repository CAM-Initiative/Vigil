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

`system_context` separates **scope** from **identity**.

Use `platform_or_vendor: "Multi Vendor"` only as a compatibility summary when structured evidence establishes more than one affected provider. It is not a substitute for naming the providers and systems VIGIL actually knows.

Failure-mode records must maintain the evidence-backed projection:

* `evidence_scope` — `single-provider`, `multi-provider`, `provider-unresolved`, `system-unresolved`, or `not-applicable`;
* `evidenced_vendors` — concrete providers/vendors established by structured evidence metadata;
* `evidenced_products_or_services` — concrete products/services established by structured evidence metadata;
* `evidenced_models_or_runtimes` — concrete model/runtime names established by structured evidence metadata;
* `evidenced_systems` — source-traceable per-evidence system identities; and
* `evidence_projection` — the derivation basis, method, reconciliation date, and inference boundary.

The maintained projection is derived from `source_records[].source_platform`, `source_records[].system_or_product`, and `source_records[].model_or_algorithm`. Do **not** mine narrative `source_context`, `relevance_note`, article titles, or publisher identity to manufacture a provider/model identity that the structured evidence does not establish.

For genuinely multi-provider records, keep the compatibility fields (`platform_or_vendor: "Multi Vendor"` and usually `product_or_service: "Other"`) for existing filters, but populate the evidence-backed arrays with the actual evidenced systems. Public interfaces should prefer those concrete arrays over placeholder compatibility values.

Example:

```json
"system_context": {
  "platform_or_vendor": "Multi Vendor",
  "product_or_service": "Other",
  "specific_model_or_runtime": "Claude; Claude Code; ChatGPT; Codex",
  "evidence_scope": "multi-provider",
  "evidenced_vendors": [
    "OpenAI",
    "Anthropic"
  ],
  "evidenced_products_or_services": [
    "ChatGPT",
    "Codex",
    "OpenAI API",
    "Claude",
    "Claude Code",
    "Claude API"
  ],
  "evidenced_models_or_runtimes": [
    "Claude",
    "Claude Code",
    "ChatGPT",
    "Codex"
  ],
  "evidenced_systems": [
    {
      "providers_or_vendors": ["OpenAI"],
      "products_or_services": ["ChatGPT", "Codex", "OpenAI API"],
      "models_or_runtimes": [],
      "source_title": "Official source title",
      "source_url": "https://example.invalid/source"
    }
  ]
}
```

If structured source metadata is insufficient, preserve `provider-unresolved` or `system-unresolved`. Do not silently fill gaps from narrative context.

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
