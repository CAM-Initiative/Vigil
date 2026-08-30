# VIGIL Maintainer Guide

## Purpose and authority boundary

VIGIL is a public evidence-to-repair observatory for AI governance evidence, research, failure modes, taxonomy, external-governance requirements, and CAM applicability assessment.

VIGIL does **not** create CAM constitutional authority, amend adopted CAM/Caelestis instruments, determine legal liability, or establish final factual truth. Repository maintenance is not a CAM governance patch and must not be represented as a VIGIL PATCH record.

The operating model is AI-authored, semi-autonomous production under human contract approval unless an artefact-level provenance declaration states otherwise. Authorship, review and verification vocabulary is enforced by `vigil/scripts/validate-authorship-provenance.py` against artefact-local provenance metadata.

## Current publication boundary

The canonical **public record corpus** is limited to:

```text
vigil/records/
  observations/
  failures/
  research/
```

These are the only record classes loaded by the public registry builder and public record validators.

The following historical/design record classes are currently **withdrawn from publication** and retained under `vigil/drafts/`:

```text
vigil/drafts/proposals/
vigil/drafts/patches/
vigil/drafts/learn/
```

Retained draft files preserve identifiers and historical work. They are not public registry inputs, must not be resolved by public interfaces, and must not be treated as published proposals, verified implementation authority, or validated learning closure.

Do not recreate `vigil/records/proposals/`, `vigil/records/patches/` or `vigil/records/learn/` without an explicit architecture decision that reactivates those classes.

## Canonical subsystem boundaries

Maintain these as separate authoritative surfaces:

- `vigil/records/` — public OBS, FM and RESEARCH records.
- `vigil/taxonomy/` — the VIGIL Observatory failure taxonomy and its generated publications.
- `vigil/external_governance/sources/` — registered external-source identity and review state.
- `vigil/external_governance/requirements/` — authoritative external-governance requirement shards and generated projections.
- `vigil/cam_assessment/` — CAM applicability/coverage assessment against a named corpus state.
- `vigil/drafts/` — retained non-public record classes.
- `vigil/docs/reviews/` — bounded implementation/reconciliation reviews that remain useful as work records.
- `vigil/docs/audits/` — retained non-normative historical audit and transition evidence.

Do not mix these authority layers merely because they are related.

## Schema and validation authority

The sole canonical record-rules contract for VIGIL records is:

```text
vigil/VIGIL.Schema.json
```

`VIGIL.Schema.json` is a machine-readable VIGIL rules contract. It is not a CAM instrument and is not itself a record.

Operational enforcement is provided by `vigil/scripts/validate-vigil-records.py` and the specialised validators under `vigil/scripts/`. The validator and tests must implement the canonical contract; they must not create a second competing ontology.

Subsystem schemas remain authoritative only for their own bounded subsystems, for example:

- `vigil/taxonomy/VIGIL.FailureTaxonomy.Schema.json` for taxonomy records;
- `vigil/external_governance/requirements/*.schema.json` for external-requirement state;
- `vigil/external_governance/sources/source-registry.schema.json` for the source registry;
- `vigil/cam_assessment/assessment.schema.json` for CAM assessment records.

Do **not** reintroduce a parallel VIGIL record-class schema tree under `vigil/schemas/`. Historical class-specific schemas were retired because they duplicated and drifted from `VIGIL.Schema.json`.

A new schema surface requires an explicit authority statement, a consumer, validator coverage, tests, and an update to this guide in the same change.

## Taxonomy dataset/book versioning

`vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json` carries the portable taxonomy dataset/book version and publication date. `vigil/taxonomy/validate_taxonomy.py` enforces this contract from the canonical family/class content digest.

When canonical family or class content changes:

- an update to existing admitted family/class content advances the **third** semantic-version digit (`patch`);
- admission of a new failure family advances the **second** digit and resets the third digit (`minor`);
- removal or restructuring of admitted family membership is a **major** change and advances the first digit according to the validator's release-history rules;
- the current release-history entry, content digest, family list, class count, version and publication date must all agree; and
- every family file's dataset/book version and publication date must agree with the index.

A renderer, stylesheet, layout, PDF/HTML presentation, or other publication-only change that does not alter canonical family/class content does not by itself create a new taxonomy dataset release.

Do not manually weaken or bypass this rule. If taxonomy validation reports that canonical family/class content changed without a new version/date/release digest, update the release metadata as part of the same substantive taxonomy change.

## Source evidence rules

Source evidence is load-bearing.

For individual VIGIL records:

- `source_records` is the **only** canonical source-evidence block;
- `source_data` and `source_data.sources` are forbidden;
- preserve source identity, date, URL, retrieval state, source type/platform, affected system metadata, evidence modality, primary-artefact access, interpretive reliance, source residence and source role where the contract requires them;
- preserve uncertainty and access limitations explicitly;
- do not flatten rich evidence into a URL-only representation;
- do not invent source values or retrospective verification;
- distinguish external evidence from CAM-internal and VIGIL-internal provenance.

Interpretive commentary may mention VIGIL or CAM without changing the origin of an external source. Source residence must be determined from source identity and provenance, not from VIGIL's own relevance note.

## Public record classes

### OBS — Observation

Use OBS for a material unresolved governance proposition or early-warning signal that is not already adequately represented by an existing FM or RESEARCH record. OBS is not a duplicate evidence container for an existing record.

### FM — Failure Mode

Use FM for a confirmed, strongly evidenced, recurring, or sufficiently clear ecosystem failure pattern requiring diagnosis, classification, triage, monitoring or repair assessment. FM is the authoritative public diagnostic record for the failure definition and threshold.

VIGIL taxonomy classification is stored separately from event-level `failure_classification` dimensions. Peer class membership belongs to the taxonomy layer, not `linked_records.related_failure_modes`.

### RESEARCH — Research Record

Use RESEARCH for substantive non-binding analysis that independently warrants publication and supports an evidence-to-repair pathway. Published research must meet the quality contract in `VIGIL.Schema.json`.

Short source summaries belong in `source_records` or, when genuinely unresolved and independently material, in OBS.

## Withdrawn PROP, PATCH and LEARN classes

PROP, PATCH and LEARN files retained under `vigil/drafts/` are historical/design material only while their architecture is under review.

Public validators, registry builders, interfaces and lifecycle checks must not load or resolve draft records. Historical references to withdrawn IDs may remain where they are part of the provenance of an existing public record, but the target remains intentionally non-public.

Repository maintenance, schema changes, validator fixes, housekeeping, migration scripts and generated-index rebuilds belong in Git commits, pull requests, audits and reviews—not in VIGIL PROP or PATCH records.

## Generated public outputs

The current public generated indexes are:

```text
vigil/VIGIL.Failures.Index.json
vigil/VIGIL.Observations.Index.json
vigil/VIGIL.Research.Index.json
vigil/VIGIL.Registry.Index.json
```

They are derived outputs. Do not edit them manually.

Build them with:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/enrich-vigil-indexes.py
```

Do not use the legacy internal builder as a publication command and do not recreate withdrawn-class indexes.

## Scripts and tests

`vigil/scripts/` is for current executable infrastructure: builders, validators, managers, routers, active auditors, active seeders and explicitly retained maintenance tools.

`vigil/tests/` is the only home for executable tests.

A completed one-off `apply-*`, `migrate-*`, reconciliation or seeding script must be dispositioned when its work closes. It may remain live only where at least one of the following is true:

1. current CI/tests depend on it;
2. current recovery or repeatable maintenance procedures require it;
3. it remains the authorised way to reproduce a maintained transformation; or
4. a current review explicitly records why it is still operational.

Otherwise delete it and rely on Git history plus any retained audit/review record.

The legacy taxonomy migration assurance ledger at `vigil/taxonomy/migration/Caelestis.LegacyFailure.MigrationLedger.json` is currently **LIVE validation evidence** because `validate_taxonomy.py` checks its migration-disposition integrity. Its presence does not make Caelestis migration semantics part of the portable taxonomy: the ledger itself declares `portable_taxonomy_dependency: false`. The remaining completed taxonomy migration review/classification artefacts belong under `vigil/docs/audits/taxonomy/migration/`.

## Audit, review and generated artefact discipline

Do not leave completed audit reports beside canonical schemas, datasets, taxonomy families or live executable code.

Use:

- `vigil/docs/reviews/` for bounded reviews that remain operationally useful;
- `vigil/docs/audits/` for retained historical audit, transition and assurance evidence;
- subsystem `generated/` directories only for deterministic current outputs;
- Git history for obsolete working debris that has no continuing evidentiary value.

The audit archive is non-normative. Historical transition documents do not remain operative merely because they are retained.

## Mandatory housekeeping closure

Housekeeping is part of every substantive VIGIL pass.

Before declaring a work item complete, disposition every new or touched supporting artefact as one of:

```text
LIVE       current executable/canonical infrastructure
GENERATED  deterministic current output
REVIEW     bounded current work/reconciliation record
AUDIT      retained non-normative historical evidence
DRAFT      explicitly non-public retained design/record material
RETIRE     delete; Git history is sufficient
```

No file may remain in a canonical or executable directory merely because that is where it happened to be created.

When a schema, field, record class, workflow, migration architecture or taxonomy structure is superseded, remove or relocate the superseded artefacts in the same bounded maintenance programme unless a documented dependency prevents retirement.

## Safe change sequence

For infrastructure changes:

1. verify the exact branch head and inspect concurrent changes;
2. identify the canonical authority and all current consumers before editing;
3. update the canonical contract/source first;
4. update validators, builders and tests in the same bounded change;
5. update documentation and path references;
6. run the focused tests and validators;
7. run the public builders and full relevant CI surface;
8. inspect generated diffs;
9. disposition temporary migration/audit/reconciliation artefacts; and
10. record any deliberately deferred cleanup explicitly.

Do not weaken validation merely to make a branch green. Do not overwrite uncertainty. Do not silently reconcile concurrent branch divergence. Do not reset, rebase, force-push or rewrite shared history as a housekeeping technique.

## Core validation commands

```bash
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py -b
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/run-vigil-lifecycle-validation.py
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/enrich-vigil-indexes.py
python vigil/taxonomy/validate_taxonomy.py
```

External-governance and taxonomy work must additionally run the validators/tests owned by those subsystems.

## Maintenance principle

The repository should make the current architecture obvious from its directory structure. Historical evidence may be preserved, but historical machinery must not masquerade as live authority.
