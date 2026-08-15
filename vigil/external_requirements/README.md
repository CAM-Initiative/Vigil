# External AI-Governance Requirements

This directory is Layer 1 of VIGIL's external-governance reference machinery. Layer 0 in `vigil/external_sources/` preserves source identity, version and lifecycle. Layer 1 preserves governance-meaningful requirements and expectations derived from those registered source versions.

These records are maintained external reference data. They are not VIGIL evidentiary record classes, do not create CAM/Caelestis authority, and do not state whether Caelestis conforms.

## Maintained inputs

- `source-scope.json` classifies every registered source version by role, access basis and extraction status.
- `requirements.json` contains stable requirement-level records.
- `external-requirement.schema.json` and `source-scope.schema.json` define the data contracts.

## Generated outputs

- `requirements-index.json` is the lean machine-readable index.
- `completeness-report.json` records source-level extraction statistics and unresolved access or interpretation state.
- `EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md` is the human-reviewable catalogue.
- `SOURCE-ACCESS-LIMITATIONS.md` is the maintainer access list.

## Commands

```bash
python vigil/scripts/manage-external-requirements.py build
python vigil/scripts/manage-external-requirements.py validate --check-generated
python vigil/tests/test_external_requirements.py
```

Requirement identifiers are deterministic from the registered source version, clause/control and a stable `identity_key`. Editing an analytical summary does not change identity. Changing the represented source clause or atomic requirement does.

Copyrighted or access-controlled standards are never reconstructed from titles, abstracts or third-party summaries. Their source-scope rows remain visibly access-blocked until licensed primary text is available for review.
