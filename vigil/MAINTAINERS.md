# VIGIL Maintainer Guide

## Active architecture

VIGIL's active public record corpus is Incident-only:

```text
vigil/records/incidents/
```

INC records preserve bounded occurrences, source evidence, occurrence-level diagnosis, severity, taxonomy classification and provenance. FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Their files, templates, generated indexes, routing rules, validators, lifecycle machinery and publication dependencies do not belong in the active tree.

Historical architecture remains recoverable through Git history and `stabilization/pre-fm-schema-migration`. Do not recreate an active-tree archive of retired records.

## Canonical Incident allocation and ingestion branch

`agent/incident-ecosystem-ingestion` is the single canonical allocation branch for new `VIGIL-INC-*` identifiers.

- Every newly allocated canonical Incident MUST originate on `agent/incident-ecosystem-ingestion`, regardless of whether the candidate was discovered by scheduled ecosystem ingestion, manual research, taxonomy work, feature development or another maintenance activity.
- Other branches MUST NOT independently allocate new `VIGIL-INC-*` identifiers. If work on another branch identifies a new Incident candidate, create the canonical Incident on `agent/incident-ecosystem-ingestion` first, then consume or reference that canonical ID from later work as appropriate.
- Existing Incidents may be amended on other branches where the maintenance task requires it, provided their stable IDs are preserved and ordinary schema, evidence and provenance requirements are followed.
- While `agent/incident-ecosystem-ingestion` exists, preserve its accumulated Incident work and continue appending bounded ingestion changes there. Do not recreate the branch from `main` merely because it is ahead of or behind `main`.
- When an ingestion tranche has been merged and the branch has been consumed/deleted, recreate `agent/incident-ecosystem-ingestion` from the exact current `main` head before allocating the next Incident.
- Incident-ID allocation should therefore check current `main` plus `agent/incident-ecosystem-ingestion`; scanning unrelated feature branches for speculative Incident reservations is not required under this contract. If a branch is found to contain an independently allocated new Incident, treat that as a maintenance-contract violation and reconcile it before further allocation rather than silently creating competing IDs.

Before opening a pull request from `agent/incident-ecosystem-ingestion`, synchronize it with the current `main` so the PR is based on the current canonical repository state. A deliberate pre-PR rebase of this dedicated ingestion branch onto current `main` is permitted for that synchronization step when no concurrent ingestion work is in flight and the branch is not already under review. Because rebasing rewrites branch history, use it only at this bounded pre-PR boundary and update the remote with lease-protected force semantics rather than an unconditional force push. Do not use rebasing, resetting or force-pushing as routine cleanup while the ingestion branch is accumulating work.

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

Structured Incident severity is derived through `harm_impact_assessment` and VIGIL-HIM. Overall severity is the highest supported assessed materialised-harm band; dimensions are never averaged or summed. `unreported` is not S1, and SU applies when no dimension can be defensibly banded. Severity remains independent of source metadata, diagnostic provenance, taxonomy classification and workflow priority.

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

The master registry contains one registry, `incidents`. It is a registry-of-registries manifest and must not duplicate Incident entries. `VIGIL.Incidents.Index.json` is intentionally a lightweight catalogue/search/routing projection; canonical evidence, diagnosis, structured severity, taxonomy detail and provenance remain in the source Incident JSON. Do not manually edit generated outputs or recreate retired-class indexes.

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

Before closure, classify each touched supporting artefact as LIVE, GENERATED, REVIEW, AUDIT or RETIRE. Historical machinery must not masquerade as current authority. Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared history as cleanup. The bounded pre-PR ingestion-branch synchronization exception above is the only permitted rebase/lease-protected force-update under this guide.
