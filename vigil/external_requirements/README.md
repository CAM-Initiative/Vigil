# External AI-Governance Requirements

This directory is Layer 1 of VIGIL's external-governance reference machinery. Layer 0 in `vigil/external_sources/` preserves source identity, version and lifecycle. Layer 1 preserves governance-meaningful requirements and expectations derived from registered source versions.

These records are maintained external reference data. They are not VIGIL evidentiary record classes, do not create CAM/Caelestis authority, and do not state whether Caelestis conforms.

The Layer 0/Layer 1 identification, extraction, analytical paraphrase, classification, and crosswalk-preparation content is AI-authored and semi-autonomous under human contract approval. It has not been manually reviewed line by line or independently human-verified. External sources retain their own authorship and authority. See `../provenance/AUTHORSHIP-PROVENANCE.json` for the controlled vocabulary and inheritance rules.

## Maintained inputs

- `source-scope.json` and `requirements.json` preserve the deterministic baseline corpus.
- `extensions/*.json` contains reviewed additive source identities, later source-access dispositions, direct-source requirement/control seeds, and separately labelled derivative-crosswalk data.
- `external-requirement.schema.json` and `source-scope.schema.json` remain the normalized Layer 1 contracts.

The effective builder expands extension packs into the same normalized Layer 1 schema and validates them with the existing deterministic identity, provenance and access rules.

## Generated outputs

- `effective-requirements.json` is the complete normalized effective Layer 1 dataset.
- `requirements-index.json` is the lean machine-readable index.
- `completeness-report.json` records effective source-level extraction statistics and unresolved access or interpretation state.
- `EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md` is the human-reviewable effective catalogue.
- `SOURCE-ACCESS-LIMITATIONS.md` is the maintainer access list.
- `BLOCKED-SOURCE-PRIORITIES.md` prioritises inaccessible primary standards without asserting that their normative text was reviewed.
- `derivative-crosswalks.json`, `derivative-crosswalk-index.json` and `DERIVATIVE-CROSSWALKS.md` project the separately governed derivative mapping dataset.
- `../external_sources/effective-ledger.json` and `../external_sources/EFFECTIVE-GOVERNANCE-SOURCES.md` project the frozen Layer 0 ledger plus extension-pack sources.

## Commands

```bash
python vigil/scripts/manage-external-requirements-extended.py build
python vigil/scripts/manage-external-requirements-extended.py validate --check-generated
python vigil/tests/test_external_requirements.py
python vigil/tests/test_authorship_provenance.py
python vigil/scripts/validate-authorship-provenance.py
```

Requirement identifiers remain deterministic from the registered source version, clause/control and stable `identity_key`. Editing an analytical summary does not change identity; changing the represented source clause or atomic requirement does.

Copyrighted or access-controlled standards are never reconstructed from titles, abstracts or third-party summaries. Where lawful primary text is available, VIGIL stores clause/control identifiers, analytical abstractions and provenance rather than the copyrighted standard text.

## Derivative-crosswalk boundary

A crosswalk records a relationship asserted by its developer. It may support navigation, comparison or provisional conceptual coverage analysis, but it does not supply missing source-standard wording, convert third-party interpretation into source authority, or establish Caelestis conformity. Every mapping remains bounded to the cited source/target versions.
