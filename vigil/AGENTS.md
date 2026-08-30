# VIGIL Agent Instructions

VIGIL is a public evidence-to-repair observatory for AI governance evidence, research, failure modes, taxonomy, external requirements and CAM applicability assessment.

VIGIL does **not** create CAM/Caelestis doctrine, amend adopted instruments, determine liability, or establish final factual truth. Do not treat a VIGIL record, repository commit, schema change, validator change, migration, audit or generated output as a CAM amendment.

VIGIL operates by default as AI-authored, semi-autonomous production under human contract approval. Use `vigil/provenance/AUTHORSHIP-PROVENANCE.json` for the controlled authorship, review and verification vocabulary. Contract approval does not imply human authorship, source verification or line-by-line review.

## Current publication boundary

The only public VIGIL record classes are:

```text
OBS       observation / early-warning record
FM        failure-mode / triage record
RESEARCH  substantive non-binding research record
```

Canonical public records are stored only under:

```text
vigil/records/observations/
vigil/records/failures/
vigil/records/research/
```

PROP, PATCH and LEARN files are currently withdrawn from publication and retained under:

```text
vigil/drafts/proposals/
vigil/drafts/patches/
vigil/drafts/learn/
```

Public validators, registry builders, lifecycle checks and interfaces must not load or resolve files from `vigil/drafts/`. Existing withdrawn IDs may remain as historical provenance text in public records, but their targets are intentionally non-public.

Do not create or restore public PROP/PATCH/LEARN records without explicit maintainer instruction that reactivates the record class.

## OBS — Observation

Create or update OBS only for a material unresolved governance proposition that is not already adequately represented by an existing FM or RESEARCH record.

Source evidence for an existing record belongs in that record's canonical `source_records`. Do not create an OBS merely because a new article, incident, status-page entry or report has appeared.

OBS must preserve evidence, uncertainty, governance significance and next action. It must not contain failure-mode triage or pretend a repair has been implemented.

## FM — Failure Mode

Use FM when an ecosystem failure pattern is confirmed, strongly evidenced, recurring, or sufficiently clear to require diagnosis, taxonomy classification, triage, monitoring or CAM coverage/repair assessment.

FM must define both the failure and its recognition threshold. The failed subject is an ecosystem system, deployment, runtime, platform behaviour, governance practice or externally observable failure pattern. VIGIL itself is not the failed system.

`failure_classification` contains event/case dimensions such as severity, likelihood, harms, scope, recurrence, persistence, reproducibility and visibility.

`taxonomy_classification` contains VIGIL Observatory taxonomy membership. Peer class membership belongs to the taxonomy layer. Do not recreate it through `linked_records.related_failure_modes`.

### Triage boundaries

Use this distinction consistently:

> Failure severity is classification. Triage priority is current action urgency. Triage status is workflow. Ecosystem monitoring is continuing external observation.

Model 2.0 controlled values are defined in `vigil/VIGIL.Schema.json`. Do not invent alternative severity, priority or workflow vocabularies.

Preserve real triage transitions in append-only `triage_history`; do not fabricate legacy transitions.

## RESEARCH — Research Record

Use RESEARCH only for substantive analysis that independently warrants publication.

Published research must meet the quality contract in `vigil/VIGIL.Schema.json`, including scope/method, source corpus, findings, counter-evidence, limitations, governance implications, open questions and bibliography/primary sources.

Short, single-source or lightly synthesised material belongs in an existing record's `source_records` or, where it is a distinct unresolved proposition, in OBS.

## Source evidence rules

For individual VIGIL records:

- `source_records` is the **only** canonical source-evidence block;
- do not add `source_data` or `source_data.sources`;
- preserve the original source URL and available archive/retrieval information;
- preserve evidence modality and whether the named reviewer directly inspected the primary artefact;
- a transcript, screenshot, summary or human description is not equivalent to direct audiovisual/behavioural review;
- preserve `source_residence` and `source_role` so external evidence, CAM-internal provenance and VIGIL-internal cross-reference provenance remain distinct;
- interpretive commentary may mention VIGIL/CAM without changing the source's actual origin;
- do not invent sources, dates, legal claims, access claims, direct-review claims, severity or harm outcomes;
- keep uncertainty and limitations visible.

## Interpretive and diagnostic provenance

Every substantive public record must preserve the provenance required by its schema contract.

For FM, `diagnostic_provenance` identifies the human–AI collaboration that formulated the diagnosis. Later interpretive review must not overwrite the original diagnostic collaborator.

`interpretive_provenance.review_history` is append-only. A later model may disagree with an earlier interpretation, but both reviews and their capability/access boundaries must remain visible.

AI substantive review is not human review or human verification.

## Failure taxonomy

The canonical VIGIL Observatory failure taxonomy is under `vigil/taxonomy/`.

Use the taxonomy index/schema and canonical family/class identifiers. Do not revive retired CAM taxonomy fields inside FM `failure_classification` and do not infer a new canonical class ID without the taxonomy admission process.

Generated taxonomy HTML/PDF is a projection, not a second source of truth.

Historical taxonomy audits under `vigil/docs/audits/taxonomy/` are non-normative transition evidence.

## External sources and external requirements

Preserve the separation:

```text
external source
  -> external requirement
  -> CAM applicability / coverage assessment
  -> VIGIL routing / repair analysis
```

For `vigil/external_sources/`, public narrative fields must describe the external source for an external reader. Do not leak internal tasking, branches, review queues or migration plans into public source descriptions.

For `vigil/external_requirements/`, do not infer inaccessible normative clauses from titles, abstracts, tables of contents, summaries or derivative crosswalks. Preserve source-fidelity state and review provenance explicitly.

External requirement inclusion does not establish that CAM is bound by, has adopted, conforms to or complies with the source instrument.

## Schema authority

The sole canonical VIGIL record-rules contract is:

```text
vigil/VIGIL.Schema.json
```

Do not create a competing VIGIL record ontology under `vigil/schemas/` or elsewhere.

Subsystem schemas remain scoped to their own surfaces, including the taxonomy, external requirements, external source registry and CAM assessment.

Schema changes must update the validator/tests and documentation in the same bounded change. Do not weaken validation simply to make a branch pass.

## Public record automation

The source of truth is the individual public record files under `vigil/records/`.

Current public generated indexes are:

```text
vigil/VIGIL.Failures.Index.json
vigil/VIGIL.Observations.Index.json
vigil/VIGIL.Research.Index.json
vigil/VIGIL.Registry.Index.json
```

Do not manually edit them and do not recreate withdrawn-class indexes.

Use:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/enrich-vigil-indexes.py
```

Core validation includes:

```bash
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py -b
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/run-vigil-lifecycle-validation.py
```

Use the external-governance and taxonomy validators/tests when those subsystems are touched.

## Repository housekeeping

Housekeeping is part of every substantive pass.

- executable tests belong under `vigil/tests/`, never `vigil/scripts/`;
- completed audits/transition reports do not remain beside canonical schemas, data or live code;
- `vigil/docs/reviews/` is for bounded reviews that remain operationally useful;
- `vigil/docs/audits/` is for retained non-normative historical audit/transition evidence;
- completed one-off `apply-*`, `migrate-*`, reconciliation and seeding scripts must be reviewed for retirement when their output is canonical and independently validated;
- delete obsolete working debris when Git history is sufficient;
- update path references, workflows and documented commands in the same administrative change.

Use the full maintenance and artefact-disposition contract in `vigil/MAINTAINERS.md`.

## Implementation discipline

Before writing:

1. verify the exact branch head and inspect concurrent changes;
2. identify the canonical authority and current consumers;
3. preserve stable IDs and source evidence;
4. make the smallest coherent change;
5. update tests/validators/docs with the authority change;
6. run relevant validation and inspect generated diffs; and
7. disposition temporary migration/audit artefacts before closure.

Do not reset, rebase, merge, cherry-pick, force-push or rewrite shared branch history as a cleanup technique unless explicitly instructed.

Do not broad-rewrite existing records merely because a deterministic migration is possible. Do not erase uncertainty to satisfy a validator. Do not update the CAM interface or adopted CAM instruments from a VIGIL maintenance pass unless separately instructed.

When a material ambiguity cannot be resolved from authoritative repository/source evidence, preserve the uncertainty rather than inventing a mapping.
