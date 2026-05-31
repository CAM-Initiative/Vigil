# VIGIL Failure Mode Record Template

Failure Mode records capture confirmed, strongly evidenced, recurring, or sufficiently clear failure patterns that require classification and triage.

## Boundary rules

* Use `record_type: "failure_mode"` and IDs like `VIGIL-YYYY-FM-0000`.
* Maintain source evidence only in `source_records`.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Include `failure_mode_definition`, `failure_threshold`, `failure_classification`, and `triage`.
* Do not include proposal implementation claims or patch-note fields.
* CAM routing may use `cam_internal.affected_*` fields because the record has triage-relevant failure classification.

Required FM sections are identity, summary, CAM relevance, failure definition, threshold, evidence confidence, `source_records`, system context, failure classification, triage, jurisdictional context, linked records, affected CAM routing, and migration notes where applicable.
