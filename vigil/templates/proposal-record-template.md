# VIGIL Proposal Record Template

Proposal records capture CAM-specific governance development, amendment logic, template/schema/validator/automation/interface repair, or operational design proposals.

## Boundary rules

* Use `record_type: "proposal"` and IDs like `VIGIL-YYYY-PROP-0000`.
* Maintain source evidence only in `source_records`; `source_data` is forbidden anywhere in an individual record.
* Do **not** add `source_data`.
* Do **not** duplicate the primary source in `linked_records.external_references`; use that array only for genuinely additional references.
* Include `proposal_rationale`, `proposal_scope`, `implementation_notes`, `external_relevance`, and `next_action`.
* A proposal must not claim that a patch has already been implemented; `patch_status` is forbidden. Implemented work belongs in a PATCH record.
* CAM routing must use target CAM routing only: `cam_internal.target_*` fields.

Required PROP sections are identity, summary, proposal rationale, proposal type, proposal scope, evidence confidence, `source_records`, linked records, target CAM routing, implementation notes, external relevance, next action, and migration notes where applicable.
