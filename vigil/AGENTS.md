# VIGIL Agent Instructions

VIGIL is an Incident-centred public observatory. Its sole active public record class is:

```text
INC — bounded occurrence-level Incident record
```

Canonical records are stored only under `vigil/records/incidents/`. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Do not create, restore, load, publish, validate or resolve them as active records. Their historical content remains available through Git history and `stabilization/pre-fm-schema-migration`.

The taxonomy, external-governance datasets and CAM assessment are separate retained subsystems. VIGIL does not amend CAM/Caelestis doctrine, determine liability or establish final factual truth.

## Incident authority and provenance

- Preserve `source_records` as the only canonical source-evidence block.
- Preserve source URLs, evidence status, evidence modality, source residence, source role, access limitations and uncertainty.
- Do not invent sources, dates, affected systems, causal claims, legal findings, severity or taxonomy mappings.
- Keep occurrence-level facts in `summary` and `vigil_assessment.factual_basis`; keep governed diagnosis in `vigil_assessment.governance_interpretation`.
- Keep structured `severity_assessment` as substantive occurrence-level diagnosis, independent of taxonomy classification, source prestige, workflow priority and hypothetical worst-case harm.
- Keep taxonomy classification separately governed and allow an Incident to remain unclassified.
- Preserve append-only interpretive provenance and do not represent AI review as human review or verification.

Historical FM/OBS/RESEARCH/PROP/PATCH/LEARN identifiers embedded in `legacy_provenance`, `legacy_governance_state`, migration-source provenance, source metadata or links are historical provenance tokens only. Do not remove or rewrite those payloads merely because the retired files are absent, and do not require the tokens to resolve to active records.

## Schema and publication

The sole VIGIL record-rules contract is `vigil/VIGIL.Schema.json`. Subsystem schemas remain scoped to taxonomy, external governance and CAM assessment.

Generated public record outputs are:

```text
vigil/VIGIL.Incidents.Index.json
vigil/VIGIL.Registry.Index.json
vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json
```

Build them only with:

```bash
python vigil/scripts/build-vigil-public-records.py
```

Do not manually edit generated indexes. The public master registry must expose only the Incident registry.

## Required workflow

Before editing an Incident, inspect `vigil/VIGIL.Schema.json`, the Incident template, the validator and comparable Incident records. Preserve stable IDs and substantive evidence.

Run at least:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```

Run taxonomy, external-governance and CAM-assessment validators when those retained subsystems are touched.

Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as maintenance. Do not restore retired records from main, migration inputs or generated artefacts.
