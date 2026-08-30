# VIGIL

**VIGIL** is the CAM Initiative's public evidence-to-repair observatory for AI governance evidence, research, failure modes, taxonomy, external requirements, and CAM applicability assessment.

VIGIL preserves what has been observed, what evidence supports it, how a failure is diagnosed and classified, what remains uncertain, and how CAM-side coverage or repair state is assessed. It does **not** create binding CAM doctrine, amend adopted CAM/Caelestis instruments, determine liability, or establish final factual truth.

## Current public record boundary

The canonical public record corpus is intentionally narrow:

```text
vigil/records/
  observations/
  failures/
  research/
```

Public record classes are:

- **OBS — Observation:** a material unresolved governance proposition or early-warning signal.
- **FM — Failure Mode:** a confirmed or strongly evidenced ecosystem failure pattern with a defined recognition threshold, taxonomy classification, triage state and repair/coverage assessment.
- **RESEARCH — Research Record:** substantive non-binding analysis that independently warrants publication and may support an evidence-to-repair pathway.

The following historical/design record classes are currently **withdrawn from publication** and retained under `vigil/drafts/`:

```text
vigil/drafts/proposals/
vigil/drafts/patches/
vigil/drafts/learn/
```

Their existing IDs and files are preserved, but they are excluded from public validation, registry generation and interface resolution. Presence under `drafts/` does not establish publication, implementation authority, adoption, or validated learning closure.

See [`vigil/drafts/README.md`](vigil/drafts/README.md) for the withdrawal boundary.

## Public evidence-to-repair model

The current public workflow is conditional rather than a compulsory record chain:

```text
External evidence ─┬─> OBS ──> FM
                   ├─> FM
                   └─> RESEARCH ──> FM

FM ──> CAM coverage / repair assessment / monitoring
```

An observation is not required where the evidence already supports a failure mode or substantive research record. A research record is not required for every failure. Public VIGIL records preserve the evidence and diagnosis; CAM authority arises only through the separate CAM/Caelestis governance process.

Historical PROP/PATCH/LEARN identifiers may remain in public-record provenance where they reflect the history of an existing record, but their retained files are not public registry targets while those classes are withdrawn.

For lifecycle and routing rules, see [`vigil/docs/VIGIL.RecordLifecycle.md`](vigil/docs/VIGIL.RecordLifecycle.md).

## Source evidence

For individual VIGIL records, `source_records` is the only canonical source-evidence block.

Do not add `source_data` or `source_data.sources` to records. Preserve source identity, dates, URLs, source/retrieval state, evidence modality, primary-artefact access, interpretive reliance, source residence and source role according to the record contract. Keep uncertainty and access limitations visible.

Evidence authoring guidance is in [`vigil/docs/evidence-authoring-guidance.md`](vigil/docs/evidence-authoring-guidance.md).

## Failure taxonomy

The VIGIL Observatory failure taxonomy is maintained separately under:

```text
vigil/taxonomy/
```

Canonical taxonomy data consists of the taxonomy index/schema and family records. Human-readable HTML/PDF publications under `vigil/taxonomy/generated/` are deterministic projections.

Historical taxonomy construction, transition and assurance audits are retained under:

```text
vigil/docs/audits/taxonomy/
```

They are non-normative history, not competing taxonomy authority.

## External governance corpus

VIGIL maintains separate external-governance layers:

```text
vigil/external_sources/       source identity and review state
vigil/external_requirements/  extracted external requirements and source-fidelity state
vigil/cam_assessment/         CAM applicability/coverage assessment
```

The governing flow is:

```text
external source
  -> external requirement
  -> CAM applicability / coverage assessment
  -> VIGIL routing or repair analysis
```

External requirements do not themselves establish that CAM is legally bound by, has adopted, or conforms to the source instrument.

## Schema and validation authority

The sole canonical VIGIL **record-rules contract** is:

```text
vigil/VIGIL.Schema.json
```

It is enforced by `vigil/scripts/validate-vigil-records.py` and specialised validators. Historical parallel class-specific VIGIL schemas are not a second authority and must not be reintroduced.

Subsystem schemas remain scoped to their own data surfaces, including the taxonomy, external-requirements, external-source and CAM-assessment schemas.

## Source of truth and generated indexes

Individual files under `vigil/records/` are the source of truth for public VIGIL records.

Current generated public indexes are:

```text
vigil/VIGIL.Failures.Index.json
vigil/VIGIL.Observations.Index.json
vigil/VIGIL.Research.Index.json
vigil/VIGIL.Registry.Index.json
```

Do not edit generated indexes manually.

Build them with:

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/scripts/enrich-vigil-indexes.py
```

Withdrawn-class indexes and the old `VIGIL.ActiveRecords.json`, `VIGIL.ClosedRecords.json`, `VIGIL.Records.Index.json` and `VIGIL.Records.json` aggregate architecture are not current public outputs.

## Validation

Core record validation:

```bash
python vigil/tests/test_vigil_source_provenance.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py -b
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/run-vigil-lifecycle-validation.py
```

External-governance and taxonomy work have additional subsystem-specific tests and validators.

## Repository organisation

Key VIGIL directories are:

```text
vigil/
  records/                public OBS/FM/RESEARCH source records
  drafts/                 retained non-public PROP/PATCH/LEARN records
  taxonomy/               canonical failure taxonomy + generated publications
  external_sources/       external-source registry
  external_requirements/  external requirement corpus
  cam_assessment/         CAM applicability/coverage assessment
  provenance/             authorship and assurance declarations
  templates/              authoring templates
  scripts/                current executable maintenance infrastructure
  tests/                  executable tests
  docs/reviews/           bounded current review/reconciliation records
  docs/audits/            retained non-normative historical audits
```

Executable tests belong under `vigil/tests/`, not `vigil/scripts/`.

## Maintenance discipline

Repository housekeeping is part of normal VIGIL maintenance. Completed transition reports, migrations, one-off scripts and review artefacts must be dispositioned when work closes rather than accumulating beside current canonical data.

The maintainer contract, including schema authority, artefact disposition and safe-change sequence, is in [`vigil/MAINTAINERS.md`](vigil/MAINTAINERS.md).

The audit archive contract is in [`vigil/docs/audits/README.md`](vigil/docs/audits/README.md).

## Authorship and review disclosure

VIGIL is predominantly AI-authored and semi-autonomously maintained under human contract approval. Unless an artefact expressly states otherwise, repository inclusion or publication does not imply human authorship, substantive human review or independent human verification.

The authoritative machine-readable declaration and controlled vocabulary are in [`vigil/provenance/AUTHORSHIP-PROVENANCE.json`](vigil/provenance/AUTHORSHIP-PROVENANCE.json).

## Relationship to CAM

VIGIL is an observatory and evidence system. CAM/Caelestis instruments become authoritative only through their own amendment, validation and adoption processes. VIGIL may assess, route or document CAM-side coverage without itself creating that authority.

## Licence and reuse

Unless otherwise stated, VIGIL record text, summaries, schema documentation and public-facing governance notes are licensed under **CC BY-NC-SA 4.0**. See [`Licence.md`](Licence.md) for the repository licence and reuse conditions.
