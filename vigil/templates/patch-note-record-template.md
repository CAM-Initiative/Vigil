# VIGIL Patch Note Record Template

Patch Note records capture CAM-specific changes that have actually been implemented.

## Boundary rules

* Use `record_type: "patch"` and IDs like `VIGIL-YYYY-PATCH-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Include `date_implemented`, `change_classification`, `change_details`, `implementation_verification`, `impact_summary`, and `remaining_work`.
* Include implemented-change evidence in `source_records` and/or `implementation_verification.evidence`.
* CAM routing must use changed CAM routing only: `cam_internal.changed_*` fields.

Required PATCH sections are identity, system context, implementation date, `change_classification`, `change_details`, `implementation_verification`, impact summary, remaining work, `source_records`, linked records, changed CAM routing, and migration notes where applicable.
