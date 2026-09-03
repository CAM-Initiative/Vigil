# VIGIL

**VIGIL** is the CAM Initiative's Incident-centred public observatory for AI governance evidence and occurrence-level diagnosis.

VIGIL preserves what happened, the evidence supporting the occurrence, the bounded VIGIL diagnosis, structured severity, taxonomy classification, uncertainty and provenance. It does **not** create CAM/Caelestis doctrine, determine liability or establish final factual truth.

## Active public corpus

The sole active public record class is:

```text
vigil/records/incidents/   INC — bounded occurrence-level Incident records
```

FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Their historical files remain recoverable through Git history and `stabilization/pre-fm-schema-migration`; they are not active records, publication inputs or resolution targets.

Migrated Incidents retain historical provenance where it explains their derivation. A legacy identifier embedded in `legacy_provenance`, `legacy_governance_state`, migration-source metadata or historical links is a provenance token only and does not require a live retired record.

## Incident model

```text
Evidence sources ──> Incident ──> Failure Class ──> Failure Family
                         │
                         └──> separate CAM applicability assessment
```

An Incident may remain unclassified. Severity is occurrence-level harm analysis and remains independent of taxonomy classification, source prestige, workflow priority and hypothetical worst-case harm.

For individual Incidents, `source_records` is the only canonical source-evidence block. Preserve source identity, dates, URLs, evidence modality, primary-artefact access, source residence, source role, evidence status and limitations.

## Retained subsystems

The following are separate from the Incident record corpus and remain active:

- `vigil/taxonomy/` — VIGIL Observatory failure taxonomy and generated publications.
- `vigil/external_governance/` — external source registry and requirement corpus.
- `vigil/cam_assessment/` — CAM applicability and coverage assessment.

External requirement inclusion does not establish that CAM is bound by, has adopted or conforms to an instrument.

## Schema and generated outputs

The sole active VIGIL record contract is `vigil/VIGIL.Schema.json`. Subsystem schemas remain scoped to their own data.

Generated public record outputs are:

```text
vigil/VIGIL.Incidents.Index.json
vigil/VIGIL.Registry.Index.json
vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json
```

Build them with:

```bash
python vigil/scripts/build-vigil-public-records.py
```

Do not edit generated indexes manually. The master registry exposes one registry: `incidents`.

## Validation

```bash
python vigil/scripts/build-vigil-public-records.py
python vigil/tests/test_build_vigil_records.py
python vigil/tests/test_validate_vigil_record_rules.py
python vigil/tests/test_validate_vigil_records.py
python vigil/tests/test_validate_vigil_public_records.py
python vigil/tests/test_vigil_pipeline_state.py
python vigil/scripts/validate-vigil-records.py
python vigil/scripts/validate-vigil-public-records.py
python vigil/scripts/validate-vigil-source-provenance.py
python vigil/scripts/validate-vigil-interpretive-provenance.py
python vigil/scripts/validate-vigil-system-components.py
python vigil/scripts/validate-authorship-provenance.py
```

Taxonomy, external-governance and CAM-assessment changes require their own subsystem validators.

## Repository organisation

```text
vigil/
  records/incidents/       canonical Incident corpus
  taxonomy/                failure taxonomy
  external_governance/     external sources and requirements
  cam_assessment/          CAM applicability assessment
  templates/               Incident authoring template
  scripts/                 live builders and validators
  tests/                   executable tests
  docs/reviews/            bounded current reviews
  docs/audits/             non-normative historical audits
```

See [`vigil/MAINTAINERS.md`](vigil/MAINTAINERS.md) for authority boundaries and maintenance rules.

## Authorship and relationship to CAM

VIGIL is predominantly AI-authored and semi-autonomously maintained under human contract approval. Repository inclusion does not imply human authorship, substantive human review or independent verification unless an artefact expressly states otherwise.

CAM/Caelestis instruments become authoritative only through their own amendment, validation and adoption processes.

## Licence

Unless otherwise stated, VIGIL record text, schema documentation and public governance notes are licensed under **CC BY-NC-SA 4.0**. See [`Licence.md`](Licence.md).
