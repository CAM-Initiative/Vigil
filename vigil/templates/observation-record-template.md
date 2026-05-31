# VIGIL Observation Record Template

Observation records preserve observed source evidence, early warning signals, public reports, platform behavior, jurisdictional developments, or other inputs whose governance meaning is not yet final.

## Boundary rules

* Use `record_type: "observation"` and IDs like `VIGIL-YYYY-OBS-0000`.
* Maintain source evidence only in `source_records`.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Do **not** include failure classification, triage, proposal scope, change classification, implemented dates, or patch logic.
* CAM routing must use `cam_internal.related_or_similar_*` fields, not `affected_*`, `target_*`, or `changed_*`.

Required OBS sections are identity, summary, CAM relevance, evidence confidence, `source_records`, system context, jurisdictional context, linked records, OBS CAM routing, next action, and migration notes where applicable.
