# VIGIL Schema Authority and Housekeeping Reconciliation Audit

**Audit date:** 2026-08-30  
**Housekeeping branch:** `housekeeping/scripts-tests-audits`  
**Target branch:** `agent/hugging-face-authority-reconciliation`  
**Status:** completed housekeeping reconciliation pending pull-request merge

## Purpose

This audit records the bounded repository-maintenance pass that reconciled VIGIL's record-contract authority, public record boundary, tests, audits, provenance validation, and completed migration machinery. It is historical maintenance evidence only. It does not create or amend a VIGIL failure family, failure class, failure mode, observation, research conclusion, CAM requirement, or Caelestis governance instrument.

## Authority decision

The sole canonical VIGIL **record-rules contract** is:

`vigil/VIGIL.Schema.json`

The historical parallel schema set under `vigil/schemas/` represented a competing architecture and has been retired. It must not be treated as an alternative or secondary VIGIL record authority.

Subsystem schemas remain authoritative only within their own bounded data surfaces, including the failure taxonomy, external-source registry, external-requirements corpus, CAM assessments, metadata-review ledger, and other explicitly scoped subsystem datasets.

## Current public record boundary

The canonical public VIGIL record classes are:

- OBS — Observation;
- FM — Failure Mode; and
- RESEARCH — Research Record.

Historical PROP, PATCH, and LEARN records remain preserved under `vigil/drafts/` but are withdrawn from public validation, registry generation, and interface resolution. Their retained draft files and historical identifiers do not establish current publication or implementation authority.

Accordingly, the current generated public registry artefacts are:

- `vigil/VIGIL.Failures.Index.json`;
- `vigil/VIGIL.Observations.Index.json`;
- `vigil/VIGIL.Research.Index.json`; and
- `vigil/VIGIL.Registry.Index.json`.

Obsolete empty PROP/PATCH/LEARN public indexes, the separate LEARN public schema, and LEARN public builder/validator machinery were retired.

## Test and executable-code disposition

Executable regression tests were consolidated under `vigil/tests/`. No executable `test_*.py` file should remain in `vigil/scripts/`.

`vigil/scripts/` is reserved for current repeatable builders, validators, managers, routers, active auditors, active seeders, shared helpers, and explicitly retained maintenance tools.

Completed one-off `apply-*` and `migrate-*` scripts were retired after checking their current dependencies. Where a completed migration contained logic still needed by current validation, that logic was extracted into permanent infrastructure rather than retaining the migration as a live tool. Source-provenance classification is the principal example: reusable classification logic now lives in `vigil/scripts/source_provenance.py`.

Git history preserves the retired migration implementations. Completed historical migration ledgers and reviews that remain useful as evidence are retained under `vigil/docs/audits/` rather than beside canonical taxonomy or runtime data, unless a documented current validator dependency still makes an artefact LIVE.

## Audit artefact disposition

Completed taxonomy, external-requirements, record-consistency, evidence-integrity, and migration artefacts were moved to bounded directories under `vigil/docs/audits/`.

The historical Caelestis legacy-failure inventory review and VIGIL failure-mode taxonomy-classification ledger are retained under `vigil/docs/audits/taxonomy/migration/`. They are migration evidence, not portable taxonomy authority.

`vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json` remains in the taxonomy subsystem because the current taxonomy validator checks its migration-disposition integrity. It is therefore classified **LIVE validation evidence** for this repository state. The ledger declares `portable_taxonomy_dependency: false`; its validation role must not be interpreted as making Caelestis migration semantics part of the portable taxonomy.

Implementation/reconciliation reviews that remain useful as current work records continue separately under `vigil/docs/reviews/`.

## Taxonomy dataset/book release guard

The taxonomy validator already enforces the dataset/book release discipline. It hashes canonical family/class content and requires the current release history, semantic version, publication date, content digest, family list and class count to remain synchronized.

Its release-history rules require:

- third-digit (`patch`) advancement for admitted family/class content changes that do not alter family membership;
- second-digit (`minor`) advancement when a new family is admitted; and
- first-digit (`major`) advancement for family removal/restructuring conditions represented by the validator.

Renderer/layout/publication-only changes that do not alter canonical family/class content do not themselves create a new dataset release.

## Source-provenance repair

The source-provenance validator was corrected so source origin is determined from source-identity/provenance fields rather than from VIGIL's own interpretive commentary. An external source does not become VIGIL-internal merely because a `relevance_note` or similar field explains how VIGIL uses it.

The pass also corrected historical source-residence/source-role metadata where the stored provenance was genuinely wrong. These corrections were kept separate from the authority decision and validated against the full canonical record corpus.

Reusable source-provenance classification rules were extracted from the completed July migration into the permanent `source_provenance.py` helper. Current validation and tests now depend on the permanent helper, not on a retired migration script.

## Failure-mode system-context reconciliation

The repository's deterministic FM system-context reconciler was run against the housekeeping state after provenance corrections. Its owned projections were brought current and then verified with `--check`. This was a deterministic maintenance projection; it did not add external evidence or alter taxonomy family/class semantics.

## External-requirements maintenance boundary

Active external-requirements metadata-review seeders and managers remain live because source-by-source metadata assurance is still in progress. Completed source-specific migration scripts were retired only after their durable repair maps and assertions were confirmed in permanent reviewed-source metadata tooling and regression tests.

Regression tests were updated to assert the current durable repair contract and, where appropriate, the absence of retired migration files rather than requiring obsolete scripts to remain present.

## Authorship/assurance validator alignment

The shared authorship-provenance validator was reconciled to the current publication boundary. It validates the four current public generated indexes—Failures, Observations, Research, and Registry—and no longer requires withdrawn PROP/PATCH/LEARN indexes to exist merely for provenance validation.

## Publication-work preservation

During this housekeeping pass the target branch advanced with completed VIGIL Observatory Failure Taxonomy textbook/reference publication work. Housekeeping did not regenerate, reinterpret, or amend that work.

The target branch's completed `vigil/taxonomy/render_taxonomy.py` and affected generated HTML/PDF publication artefacts were copied into the housekeeping branch by exact Git blob identity. The publication content is therefore preserved independently of the housekeeping architecture changes.

No taxonomy family or failure-class semantic change is made by this audit or by the housekeeping pass recorded here.

## Maintainer rule established

Housekeeping is a routine maintenance obligation, not a later rescue operation. At the close of a substantive workstream, new artefacts should be dispositioned as one of:

- **LIVE** — current executable or canonical source material;
- **GENERATED** — deterministic output of current source material;
- **REVIEW** — still-useful current implementation/reconciliation review;
- **AUDIT** — retained non-normative historical maintenance evidence;
- **DRAFT** — intentionally non-public working material; or
- **RETIRE** — obsolete one-off machinery or debris recoverable from Git history.

A workstream should not leave tests in `scripts/`, completed audits beside canonical datasets, duplicate schema authorities, or one-off migrations in the live tool directory without an explicit continuing dependency.

## Validation expectations

The reconciled architecture is expected to satisfy, at minimum:

- VIGIL source-provenance regression and corpus validation;
- VIGIL record-rule regression tests;
- FM system-context reconciliation tests and deterministic `--check`;
- triage inventory tests and generated-state check;
- lifecycle, PATCH-trace, provenance-preservation, and pipeline-state tests;
- withdrawn-record-class publication-boundary tests;
- authorship/assurance provenance validation against the current four public indexes;
- external-source and external-requirements build/validation;
- CAM assessment validation; and
- VIGIL Observatory taxonomy publication validation.

The pull request should remain draft until the final CI cycle passes and the remaining repository-diff review confirms that publication work and unrelated substantive branch work are preserved.
