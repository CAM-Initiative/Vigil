# TAXONOMY-04B — Legacy Failure-Taxonomy and Failure-to-Failure Linkage Removal

## Preflight

- Review date: `2026-08-25`
- Exact remote branch head before migration: `bc42aa3df7842e3ae1f6ff220c8d670bb95f7129`
- Current `main`: `9fcaf0e498ca5f7ea0db7c925da4f9c10a4a6891`
- Pre-work comparison: taxonomy branch 18 commits ahead and 1 commit behind `main`
- Merge base: `e3d1dcb12875642c71ca3100b43b6d63872bf69a`

The commit added since TAXONOMY-04A was `bc42aa3 — Add FM-0071 trajectory-level boundary erosion`. It changed only `VIGIL-2026-FM-0071.json` and was preserved. No merge, rebase, reset, cherry-pick, force-push, branch creation, PR, or branch-divergence reconciliation was performed.

## Corpus migration

- Canonical failure-mode records inspected: **71**
- Records containing legacy taxonomy metadata: **71**
- Records containing `linked_records.related_failure_modes`: **71**
- Records with non-empty peer-FM links: **46**
- FM-to-FM link entries removed: **95**
- Records retaining retired taxonomy fields after migration: **0**
- Records retaining the peer-FM field after migration: **0**

The following structured taxonomy fields were removed where present:

- `failure_classification.failure_family`
- `failure_classification.failure_subtype`
- `failure_classification.canonical_failure_group`
- `failure_classification.taxonomy_reference`
- `failure_classification.related_failure_groups`
- `failure_classification.allowed_canonical_failure_group_values`
- `failure_classification.classification_status`
- `failure_classification.faceted_analysis.external_taxonomy_refs`
- `cam_internal.cam_taxonomy_primary_group`
- `cam_internal.cam_taxonomy_secondary_groups`
- `cam_internal.cam_taxonomy_candidate_labels`
- top-level `proposed_taxonomy_patch`
- `linked_records.related_failure_modes`

No removed FM link was copied into contextual relations, notes, external references, dependencies, or placeholders. The case-chain arrays for observations, research, proposals, PATCHes, contextual relations, external references, standards, and evidence were compared field-by-field with the pre-work records; **zero case-chain fields changed**.

Substantive failure description remains in `failure_mode_definition`, `failure_threshold`, and the non-taxonomic parts of `failure_classification`, including harm vectors, severity, likelihood, confidence, affected interests, scope, recurrence, persistence, reproducibility, visibility, severity basis/gaps, and faceted evidence analysis.

## Contract and generation changes

- Removed the CAM legacy failure-taxonomy registry and taxonomy requirements from `VIGIL.Schema.json`.
- Added an explicit taxonomy-free transition rule and prohibited peer-FM fields on failure-mode records.
- Updated the record validator to reject reintroduction of retired taxonomy fields, taxonomy routing fields, taxonomy-patch proposals, and FM peer links while retaining substantive classification and case-chain validation.
- Updated the faceted-analysis validator and failure-mode template to remove external taxonomy references during the transition.
- Updated the generator so failure summaries and failure indexes no longer project legacy family, subtype, canonical group, taxonomy reference, or related groups.
- Preserved research-to-FM links in research projections because these are genuine evidence/case-chain relationships, not FM-to-FM similarity links.
- Rebuilt `VIGIL.Failures.Index.json`, `VIGIL.Observations.Index.json`, and `VIGIL.Registry.Index.json`; empty withdrawn record classes remain excluded from the public master registry.

Two consecutive builds were byte-identical for every affected generated index.

## Validation

| Check | Result |
|---|---|
| Parse every canonical failure-mode JSON | PASS — 71/71 |
| Retired taxonomy-field scan | PASS — 0 retained |
| FM peer-link scan | PASS — 0 retained |
| Case-chain preservation comparison | PASS — 0 changed case-chain fields |
| Generated-index stale-key scan | PASS — no retired structured key in failure projections |
| Deterministic regeneration | PASS — byte-identical consecutive builds |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | PASS — 120 tests |
| `python -m unittest discover -s vigil/scripts -p 'test_*.py'` | PASS — 34 tests |
| `python vigil/scripts/test_vigil_pipeline_state.py` | PASS |
| `python vigil/taxonomy/validate_taxonomy.py` | PASS — 8 families / 42 classes |
| `python -m unittest vigil.tests.test_failure_taxonomy` | PASS — 14 tests |
| Python bytecode compilation | PASS |
| `git diff --check` | PASS |

The repository-wide record validator retains **111 warnings and 16 errors**, all involving the already-withdrawn PROP/PATCH/OBS research-link surface. The untouched pre-work head additionally produced five FM-0071 errors because the same peer failures were duplicated in authoritative `related_failure_modes` and non-authoritative contextual relations. Removing the authoritative peer field as required resolves those five errors without modifying the contextual relations. No unrelated record was repaired.

The standalone faceted-analysis validator continues to report 16 pre-existing controlled-vocabulary mismatches in the newly added FM-0071 faceted block. Those values are unrelated to the retired taxonomy fields and were not rewritten in this bounded migration. They require separate review by the FM-0071 workstream.

## Transitional state

Failure-mode records now intentionally have no formal taxonomy classification. No VIGIL-native taxonomy ID, inferred replacement family, substitute peer graph, or placeholder classification was introduced. The corpus is ready for the separate new-taxonomy classification migration.
