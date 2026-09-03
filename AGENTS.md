# VIGIL Agent Instructions

These instructions apply to the repository. `vigil/AGENTS.md` and `vigil/MAINTAINERS.md` add the detailed maintenance contract.

VIGIL is an Incident-centred public evidence and diagnosis corpus. INC is the sole active public record class. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired and must not be restored, published, resolved or reintroduced as runtime dependencies. The taxonomy, external-governance datasets and CAM assessment remain separate retained subsystems.

Before editing Incidents, inspect `vigil/VIGIL.Schema.json`, `vigil/templates/incident-record-template.json`, `vigil/scripts/validate-vigil-records.py` and comparable canonical records. Preserve stable IDs, evidence, uncertainty, occurrence-level diagnosis, severity and provenance.

Historical retired-class identifiers and payloads embedded in Incidents are provenance tokens only. Preserve them where they explain derivation, but never require them to resolve to live files.

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
