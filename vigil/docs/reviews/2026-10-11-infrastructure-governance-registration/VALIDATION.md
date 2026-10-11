# Validation and preserved baseline

Classification: REVIEW. Date: 11 October 2026.

Original baseline: `6192d5d4b66c6d8bb9fbf9e86347e8f0b56e7866`. Publication baseline: `418134c32b3b0c881a20019bf9c8cd0c6d9707e2`. The unpublished working changes were carried to a new local branch at the advanced integration HEAD. No shared history was rewritten; the concurrent handoff, triage and generated-index changes were preserved.

Environment: Python 3.12; jsonschema installed for the metadata/schema checks. `PYTHONPATH=vigil/scripts` is set for tests that import retained script modules. An initial missing dependency/import path was resolved in the environment, without changing repository code.

## Final read-only validation

| Command | Exit | Result |
| --- | --- | --- |
| `python vigil/scripts/manage-external-sources.py validate --check-generated` | 0 | PASS |
| `python vigil/scripts/manage-external-requirements.py validate --check-generated` | 0 | PASS |
| `python vigil/scripts/validate-external-requirement-metadata.py` | 0 | PASS |
| `python vigil/scripts/validate-external-requirement-fidelity.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-referential-integrity.py` | 1 | FAIL — pre-existing FC-084 clause references in INC-060 and INC-189 |
| `python vigil/scripts/validate-occurrence-requirement-assessments.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-records.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-public-records.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-source-provenance.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-interpretive-provenance.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-system-components.py` | 0 | PASS |
| `python vigil/scripts/validate-authorship-provenance.py` | 0 | PASS |
| `python vigil/scripts/validate-vigil-rights.py` | 0 | PASS |
| `python vigil/taxonomy/validate_taxonomy.py` | 0 | PASS |
| `python vigil/tests/test_external_sources.py` | 0 | PASS |
| `python vigil/tests/test_external_requirements.py` | 0 | PASS |
| `python vigil/tests/test_external_requirement_metadata.py` | 0 | PASS |
| `python vigil/tests/test_external_requirement_fidelity.py` | 0 | PASS |
| `python vigil/tests/test_external_requirement_assessments.py` | 0 | PASS |
| `python vigil/tests/test_clause_requirement_resolver.py` | 0 | PASS |
| `python vigil/tests/test_external_requirement_public_projection.py` | 0 | PASS |
| `python vigil/tests/test_vigil_source_provenance.py` | 0 | PASS |
| `python vigil/tests/test_validate_vigil_record_rules.py` | 0 | PASS |
| `python vigil/tests/test_source_episode_integrity.py` | 0 | PASS |
| `python vigil/tests/test_public_prose_quality.py` | 0 | PASS |
| `python vigil/tests/test_vigil_pipeline_state.py` | 0 | PASS |
| `python vigil/tests/test_authorship_provenance.py` | 0 | PASS |
| `python vigil/tests/test_failure_taxonomy.py` | 0 | PASS |
| `python vigil/tests/test_taxonomy_invariant_semantics.py` | 0 | PASS |
| `python vigil/tests/test_taxonomy_release_modes.py` | 0 | PASS |
| `python vigil/tests/test_taxonomy_publication_references.py` | 0 | PASS |
| `python vigil/tests/test_build_vigil_records.py` | 0 | PASS |

31 of 32 final commands pass. The failing referential-integrity check was also run on a separate untouched worktree at the publication baseline and returned the identical two diagnostics:

```text
VIGIL-INC-000060: clause class ID does not resolve: VIGIL-FC-000084
VIGIL-INC-000189: clause class ID does not resolve: VIGIL-FC-000084
```

No broad repair was attempted. Canonical Incident validation passes; the additional thin integrity check has a stricter unresolved-endpoint diagnostic. This is a reported baseline limitation, not a claim that all checks are green.

## Builders and one-off assertions

- `python vigil/scripts/manage-external-sources.py build` — PASS; 98 source versions, 13 pending review entries.
- `python vigil/scripts/manage-external-requirements.py build` — PASS; 1,102 existing requirements unchanged. Generated outputs are produced by the managers.
- `python vigil/scripts/build-vigil-public-records.py` — PASS; 189 canonical records. At the original baseline it exposed a stale INC-090 index; the advanced integration baseline already contained that concurrent generated update. No unrelated index change is included here.
- `git diff --check` — PASS.
- Draft 2020-12 JSON Schema validation for source registry, source scope and source-review assurance — PASS.
- All 85 baseline source registry entries are exactly preserved as JSON values.
- INC-090 is byte-identical to the publication baseline. Direct builder projection has assessment count zero.
- No changes under Incident records, source requirement shards, taxonomy families, taxonomy relationships, schema, scripts or permanent tests.

## Workflow and website evidence

The command set includes the applicable read-only validation/test steps from `.github/workflows/vigil-records.yml` and `.github/workflows/vigil-taxonomy-publications.yml`. GitHub results for the focused PR are recorded below once available. The workflows do not run the extra thin referential-integrity check; their success does not erase its baseline failure. No main-only publication/release or merge was run.

See `PUBLIC-CATALOGUE-TRACE.md` for the main-backed data route, genuine type display, deferred separate-site copy and force-vocabulary work, and the lack of a live render check. Canonical Section 04 insertion remains held at Gate 1.

## GitHub workflow results

Pending PR publication.
