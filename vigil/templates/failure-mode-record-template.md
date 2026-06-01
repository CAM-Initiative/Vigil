# VIGIL Failure Mode Record Template

Failure Mode records capture confirmed, strongly evidenced, recurring, or sufficiently clear failure patterns that require classification and triage.

## Boundary rules

* Use `record_type: "failure_mode"` and IDs like `VIGIL-YYYY-FM-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Include `failure_mode_definition`, `failure_threshold`, `failure_classification`, and `triage`; `failure_classification` must include `failure_family`, `canonical_failure_group`, `taxonomy_reference`, `related_failure_groups`, `persistence`, `reproducibility`, and `visibility`.
* Do not include proposal implementation claims or patch-note fields.
* CAM routing must use affected CAM routing only: `cam_internal.affected_*` fields because the record has triage-relevant failure classification.

Required FM sections are identity, summary, CAM relevance, failure definition, threshold, evidence confidence, `source_records`, system context (including `product_family`, `product_or_service`, `specific_model`, and `interface_surface`), failure classification, triage, jurisdictional context, linked records, affected CAM routing, and migration notes where applicable.
