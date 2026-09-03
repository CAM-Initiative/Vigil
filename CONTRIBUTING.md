# Contributing to VIGIL

VIGIL accepts improvements to canonical Incident records, evidence quality, taxonomy classification, schema enforcement, generated publication, external-governance datasets and CAM applicability assessment.

FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Do not propose, restore or link to them as active records. Historical identifiers embedded in existing Incidents remain provenance tokens and do not require live targets.

## Incident contributions

Before adding or changing an Incident:

1. Read `vigil/VIGIL.Schema.json` and `vigil/templates/incident-record-template.json`.
2. Inspect comparable records under `vigil/records/incidents/`.
3. Preserve stable IDs and existing source evidence.
4. Keep `source_records` as the only canonical evidence block.
5. Separate source-supported facts, VIGIL diagnosis, structured severity and taxonomy classification.
6. Preserve uncertainty; do not invent URLs, dates, affected systems, causal claims, legal findings or verification.

External sources should identify title, publisher, date, URL, retrieval state, source type/platform, evidence modality, primary-artefact access, source residence, source role, claim-relative evidence status and relevance. Internal CAM/VIGIL material must not be represented as external evidence.

Use `platform_or_vendor: "Multi Vendor"` only where multiple vendors are evidenced and retain the required structured vendor arrays. Do not place comma-separated product lists in canonical enum fields.

## Build and validation

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```

Run the relevant taxonomy, external-governance or CAM-assessment validators when those subsystems change. Fix canonical sources rather than manually editing generated indexes.

A pull request should identify files and records changed, evidence added or still missing, generated outputs rebuilt, validation results and any remaining pre-existing warnings.

Do not modify CAM/Caelestis instruments through a VIGIL contribution unless explicitly requested.
