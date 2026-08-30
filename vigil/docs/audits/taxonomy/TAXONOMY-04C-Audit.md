# TAXONOMY-04C — Diagnostic Provenance Attribution Audit

## Branch preflight

- Repository: `CAM-Initiative/Vigil`
- Existing branch: `agent/failure-taxonomy-prototype`
- Remote head before migration: `c2f77d82188b3074c6fb6c3cbe65e0178c44666e`
- No commit was added after TAXONOMY-04B before this work began.
- No branch reconciliation, taxonomy classification, replacement taxonomy ID, new branch or pull request was introduced.

## Corpus inventory and attribution

- Canonical failure-mode records inspected: **71**
- Earliest diagnostic date: **2026-05-31**
- Latest diagnostic date: **2026-08-25**
- Attributed to OpenAI GPT-5.5: **27**
- Attributed to OpenAI GPT-5.6 Sol: **44**
- Records before 2026-04-23: **0**
- Records missing `record_identity.created` or `date_recorded`: **0**
- Records with conflicting creation dates: **2**
- Records requiring manual provenance review: **2**

The two conflicts are:

| Record | `record_identity.created` | `date_recorded` | Migration treatment |
|---|---:|---:|---|
| `VIGIL-2026-FM-0044` | 2026-07-23 | 2026-07-30 | Used the expressly preferred canonical creation date; recorded the conflict in `diagnostic_provenance.date_anomaly_note`; retained for manual provenance review. |
| `VIGIL-2026-FM-0048` | 2026-07-25 | 2026-07-30 | Used the expressly preferred canonical creation date; recorded the conflict in `diagnostic_provenance.date_anomaly_note`; retained for manual provenance review. |

## Provenance contract

Every canonical failure mode now has a distinct `diagnostic_provenance` block identifying:

- human–AI collaborative analytical synthesis as the method;
- the canonical creation date as the diagnostic date;
- substantive human governance analysis, contextual judgement, correction, review and approval;
- AI synthesis, mechanism identification, evidence/context comparison and drafting support;
- the historically attributed ChatGPT model;
- the date-based attribution basis;
- human review and approval status; and
- the boundary that the AI collaborator was not independently authoritative.

This block describes the original diagnostic act only. Existing source-review `interpretive_provenance`, later review histories, substantive diagnoses, repair provenance and learning provenance were not rewritten. A semantic comparison against the pre-work head, after excluding the new block, found **zero changes** across the 71 canonical records.

## Schema, validator, template and projections

- Updated `VIGIL.Schema.json` to require diagnostic provenance for failure modes and document the historical model-attribution windows.
- Updated the record validator to enforce required fields, canonical diagnostic date, historical model/date alignment, review semantics, and explicit recording of creation-date conflicts.
- Updated the failure-mode JSON and Markdown templates and authoring instructions for contemporaneous provenance on new records.
- Updated `VIGIL.Index.Schema.json`, the index builder and enrichment tool to publish a bounded diagnostic-provenance summary.
- Added validator, date/model attribution, conflict-recording, corpus-inventory and generated-projection regression coverage.
- Regenerated all registry indexes and enriched public failure/observation indexes twice; affected output hashes were byte-identical across consecutive runs.
- All **71** generated failure entries expose `diagnostic_provenance_summary`.

## Validation

| Check | Result |
|---|---|
| Canonical diagnostic-provenance inventory | PASS — 71/71 |
| Historical model distribution | PASS — GPT-5.5: 27; GPT-5.6 Sol: 44 |
| Pre-boundary/missing-date scan | PASS — 0 / 0 |
| Non-diagnostic semantic comparison | PASS — 0 changed records |
| Deterministic index generation and enrichment | PASS |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | PASS — 125 tests |
| `python -m unittest discover -s vigil/scripts -p 'test_*.py'` | PASS — 34 tests |
| `python vigil/scripts/test_vigil_pipeline_state.py` | PASS |
| `python vigil/scripts/run-vigil-lifecycle-validation.py` | PASS — 101 records |
| `python vigil/taxonomy/validate_taxonomy.py` | PASS — 8 families / 42 classes |
| `python -m unittest vigil.tests.test_failure_taxonomy` | PASS — 14 tests |
| Python bytecode compilation | PASS |
| `git diff --check` | PASS |

The repository-wide record validator retains the known **111 warnings and 16 errors** arising from withdrawn-record research links. The standalone faceted-analysis validator retains the 16 pre-existing FM-0071 controlled-vocabulary mismatches recorded in TAXONOMY-04B. Neither surface was changed by diagnostic attribution.

## Transitional boundary

No replacement VIGIL taxonomy classification was introduced. Failure modes remain taxonomy-free while now carrying explicit provenance for the diagnosis that created each case file.
