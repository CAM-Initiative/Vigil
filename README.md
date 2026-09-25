# VIGIL Observatory

**VIGIL Observatory** (technical namespace **VIGIL**) is CAM Initiative's Incident-centred public observatory for AI governance evidence and occurrence-level diagnosis.

VIGIL preserves what happened, the evidence supporting the occurrence, the bounded VIGIL diagnosis, structured severity, taxonomy classification, uncertainty and provenance. It does **not** create CAM/Caelestis doctrine, determine liability or establish final factual truth.

## Active public corpus

The sole active public record class is:

```text
vigil/records/incidents/   INC — bounded occurrence-level Incident records
```

FM, OBS, RESEARCH, PROP, PATCH and LEARN are retired record classes. Their historical files remain recoverable through Git history and `stabilization/pre-fm-schema-migration`; they are not active records, publication inputs or resolution targets.

Legacy record classes and migration artefacts remain recoverable through Git history. Active Incident records contain only information required by the current VIGIL data model.

## Incident model

```text
Evidence sources ──> Incident ──> Alignment Class ──> Alignment Family
                         │
                         └──> separate CAM applicability assessment
```

An Incident may remain unclassified. Severity is occurrence-level harm analysis and remains independent of taxonomy classification, source prestige, workflow priority and hypothetical worst-case harm.

For individual Incidents, `source_records` is the only canonical source-evidence block. Preserve source identity, dates, URLs, evidence modality, primary-artefact access, source residence, source role, evidence status and limitations.

## Retained subsystems

The following are separate from the Incident record corpus and remain active:

- `vigil/taxonomy/` — VIGIL Observatory alignment taxonomy and generated publications.
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
  taxonomy/                alignment taxonomy
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

VIGIL Observatory is predominantly AI-authored and AI-assisted in its evidence review, structured analysis, corpus maintenance and repository implementation. Substantive taxonomy and governance adjudication remain under human authority. AI systems may prepare classifications, identify candidate failure mechanisms, compare evidence and draft repository changes, but classification boundaries, taxonomy admission, governance interpretation and contested adjudications are subject to human direction and approval.

Repository inclusion does not imply human authorship, substantive human review or independent verification unless an artefact expressly states otherwise. Operational maintenance may be semi-autonomous, but it remains bounded by human governance authority and the repository's documented validation, provenance and amendment controls.

CAM/Caelestis instruments become authoritative only through their own amendment, validation and adoption processes.

## Licence

VIGIL Observatory is publicly inspectable proprietary work. Copyright © 2026 Phoenix Covenant Pty Ltd trading as CAM Initiative (ABN 14 692 195 529). All rights reserved.

Citation, reference and linking with clear attribution to **CAM Initiative and VIGIL Observatory** are permitted. Public access does not grant permission to reproduce, redistribute, adapt, derive from, translate, systematically extract, incorporate, train on, evaluate with, or otherwise reuse VIGIL Observatory Materials. Commercial and non-commercial substantive reuse require prior written licence.

See [`LICENSE.md`](LICENSE.md) and [`RIGHTS.json`](RIGHTS.json).
