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
