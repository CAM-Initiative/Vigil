# VIGIL Maintainer Guide

## Active architecture

VIGIL's active public record corpus is Incident-only:

```text
vigil/records/incidents/
```

INC records preserve bounded occurrences, source evidence, occurrence-level diagnosis, severity, taxonomy classification and provenance. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Their files, templates, generated indexes, routing rules, validators, lifecycle machinery and publication dependencies do not belong in the active tree.

Historical architecture remains recoverable through Git history and `stabilization/pre-fm-schema-migration`. Do not recreate an active-tree archive of retired records.

## Historical provenance

Migrated Incidents may contain `legacy_provenance`, `legacy_governance_state`, migration-source metadata and historical IDs. Preserve those payloads when they explain derivation or historical review. A retired-class ID is a provenance token, not a live link; validators, builders and public interfaces must not require a corresponding FM, OBS, RESEARCH, PROP, PATCH or LEARN file.

Do not falsify historical review dates, reconstruct deleted records or reinterpret historical payloads as current workflow state.

## Retained subsystem boundaries

- `vigil/records/incidents/` — sole active public record corpus.
- `vigil/taxonomy/` — canonical VIGIL Observatory failure taxonomy and generated publications.
- `vigil/external_governance/sources/` — external-source registry.
- `vigil/external_governance/requirements/` — external-governance requirements and projections.
- `vigil/cam_assessment/` — CAM applicability and coverage assessment.
- `vigil/docs/reviews/` — bounded reviews that remain operationally useful.
- `vigil/docs/audits/` — retained non-normative historical audit evidence.

The taxonomy migration assurance ledger at `vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json` remains live taxonomy validation evidence. It does not reactivate FM as a VIGIL record class.

## Schema and evidence authority

`vigil/VIGIL.Schema.json` is the sole active VIGIL record contract. It defines only Incident records. Subsystem schemas remain authoritative only for their named subsystem.

`source_records` is the only canonical evidence block. Preserve source identity, URLs, dates, evidence modality, access state, source residence, source role and claim-relative evidence status. Do not infer inaccessible facts or represent repository acceptance as human verification.

Structured Incident severity is substantive occurrence-level diagnosis. It is not source metadata, diagnostic provenance, taxonomy metadata or workflow priority. `severity_assessment_basis` may exist only as a deterministic generated compatibility projection.

## Generated outputs

The active public outputs are:

```text
vigil/VIGIL.Incidents.Index.json
vigil/VIGIL.Registry.Index.json
vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json
```

Build all three with:

```bash
python vigil/scripts/build-vigil-public-records.py
```

The master registry contains one registry, `incidents`. Do not manually edit generated outputs or recreate retired-class indexes.

## Maintenance and validation

Executable tests belong under `vigil/tests/`; current builders and validators belong under `vigil/scripts/`. Delete completed one-off migration, routing, reconciliation and seeding machinery when no retained subsystem depends on it.

For Incident/schema/runtime changes, run:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/tests/test_build_vigil_records.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py
python vigil/tests/test_validate_vigil_public_records.py
python vigil/tests/test_vigil_pipeline_state.py
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
python vigil/taxonomy/validate_taxonomy.py
```

Also run the validators owned by external governance or CAM assessment when those subsystems are touched.

Before closure, classify each touched supporting artefact as LIVE, GENERATED, REVIEW, AUDIT or RETIRE. Historical machinery must not masquerade as current authority. Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as cleanup.
