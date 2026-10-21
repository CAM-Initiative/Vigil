# VIGIL Agent Instructions

These instructions apply to the repository. `vigil/AGENTS.md` and `vigil/MAINTAINERS.md` add the detailed maintenance contract.

VIGIL is an Incident-centred public evidence and diagnosis corpus. INC is the sole active public record class. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired and must not be restored, published, resolved or reintroduced as runtime dependencies. The taxonomy, external-governance datasets and CAM assessment remain separate retained subsystems.

**VIGIL adjudication authority:** Sources establish attributed occurrence evidence, not the outcome of VIGIL's classifications. Apply the current canonical Fidelity Class recognition conditions and exclusions independently; external interpretations neither overrule nor automatically validate a VIGIL finding. Preserve and explicitly disposition previously supported VIGIL divergences, including bounded successes and mixed-role episodes, before accepting a rewrite. For taxonomic re-adjudication, follow the criterion-level decision and preservation protocol in `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md`. A passing structural validator does not certify semantic fidelity.

Before editing Incidents, inspect `vigil/VIGIL.Schema.json`, `vigil/templates/incident-record-template.json`, `vigil/scripts/validate-vigil-records.py` and comparable canonical records. Preserve stable IDs, evidence, uncertainty, occurrence-level diagnosis, severity and provenance.

A request to create a new Incident authorises the complete ordinary processing sequence, not intake alone. Follow the new-entry completion section in `vigil/docs/maintenance/INCIDENT-ADJUDICATION-WORKFLOW.md` and its audit checklist. An empty external-assessment list does not demonstrate review. Report evidence-limited findings separately from work not performed. New schema fields and blocking controls still require Gate 1 approval.

Legacy record classes and migration artefacts remain recoverable through Git history. Do not restore them to active Incident records or require them as runtime dependencies.

Build and validate with:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```

Run retained-subsystem tests when taxonomy, external governance or CAM assessment is touched. Do not manually edit generated indexes, fabricate evidence or review state, expose private material, or modify CAM/Caelestis instruments without explicit instruction.

## Canonical Boundary adjudication — approved 19 October 2026

Every admitted `ambiguous-boundary` primary or secondary taxonomy mapping MUST contain a completed `boundary_adjudication` object in the Incident itself. A dated audit packet is supporting review history, never a substitute for the canonical explanation. Use `vigil/templates/boundary-adjudication-template.json`; the authoritative shape is `boundary_adjudication_contract` in `vigil/VIGIL.Schema.json`.

The object records `taxonomy_version`, positive `material_engagement`, non-empty `unresolved_conditions`, `diagnostic_reasons`, `decisive_blocker` and `resolution_requirements`. Each unresolved condition records its `polarity` (failure-occurrence or successful-invariant), literal `condition`, occurrence-specific `assessment`, and resolvable `source_record_refs` and `episode_refs`. Explain why neither outcome is established; do not assume a failure-side unknown proves success or vice versa. Historical taxonomy metadata remains separate from the version applied in this adjudication.

Permitted diagnostic reasons are `insufficient-evidence`, `conflicting-evidence` and `recognition-criteria-insufficiency`, including multiple contributing reasons. Identify the precise missing fact and potential resolving source, incompatible evidence and needed reconciliation, or criteria deficiency and separate taxonomy review. Unsupported class engagement is a candidate for removal or alternative disposition, not a completed Boundary. Review not performed is an audit hold, not a completed adjudication. These reasons explain the existing role; they are not additional canonical classification roles.

The validator rejects absent/incomplete objects, invalid reasons and unresolved source/episode references. It cannot certify that prose is substantively correct or that all relevant criteria have been examined. Boundary mappings require completed boundary_adjudication and must omit classification_confidence. Failure-occurrence and successful-invariant mappings require classification_confidence (low, medium or high) and must omit boundary_adjudication. On a role change, preserve the previous mapping and superseded values in dated review history before removing role-inapplicable fields from the current mapping. Historical confidence is provenance, never a current Boundary rating. Keep complete criterion matrices, rejected candidates and review process history in audit packets. The canonical object contains accepted occurrence-specific reasoning only.

Approval covers this control, documentation, templates and isolated tests. After implementation run the corpus read-only and report exact failures. Do not mechanically fill objects, reclassify findings, change recognition conditions or amend independent assessments. Substantive corpus repair remains subject to explicit maintainer authorisation. This requirement supersedes earlier audit-only placement of Boundary diagnostic reasons. Website display is separate renderer work; no presentation or builder change is authorised here.
