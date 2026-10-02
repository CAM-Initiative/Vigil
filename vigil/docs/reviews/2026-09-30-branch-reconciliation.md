# VIGIL Branch Reconciliation

Review date: 2026-09-30

Status: P0 consolidation completed on `work/reconcile-taxonomy-external-requirements`; no pull request created.

## Source state

- `agent/incident-ecosystem-ingestion` and `work/reconcile-taxonomy-external-requirements` both pointed to `e5964df1f96ca686280dbd658130d76fbee31963`.
- `feat/external-requirement-adjudication` pointed to `81920bf96f475cec016c803066a3680f21da991d`, two commits ahead of its `d604d81` base and diverged from the source-clause branch at `dd19d8a`.

## Reconciliation method and preserved content

The source-clause branch was retained as the corpus baseline. External-requirement schema, methodology, validators, builders, tests, Article 12 taxonomy updates, and review artefacts were incorporated from the external-requirement branch without rewriting either branch's history. Its deletion of `vigil/CONSTITUTION.md` was not carried over because the newer source-clause branch contains that file.

The 170 latest Incident records and their source-clause analyses were retained. The prior external-requirement branch had 96 assessment entries on 60 records. Those `external_requirement_assessments` fields alone were transferred onto the corresponding latest Incident records; all 96 `derived_from_class_ids` were checked against the latest mapped classes before transfer. Other Incident content was not replaced from the older corpus branch.

Generated public indexes and the deterministic candidate matrix were rebuilt from the consolidated tree.

## Reconciled output

- 170 canonical Incident records: 169 active and one monitoring.
- 147 source-clause assessments reported complete and 23 partial at the source-branch checkpoint; those clause results were preserved.
- Candidate matrix: 479 Incident–requirement pairs across 53 requirement IDs; 149 taxonomy-mapped Incidents; zero unresolved structured requirement references.
- EU AI Act subset: 94 candidate pairs across six requirements.
- Existing external-requirement assessments: 96 entries across 60 Incidents.

The Article 12 migration and EU AI Act assessments are preserved as prior branch work. They are not treated as final post-taxonomy results: complete P1A (both full-corpus Fidelity Class assessments) and P1B (the 23 partial Incidents) before treating the candidate matrix or affected external assessments as final. Regenerate the matrix and revisit impacted findings after those reviews.

## Validation and known baseline issues

Passed on the consolidated tree: canonical Incident validation (170), public Incident index validation (170), source provenance (574 source records), interpretive provenance (170), system-component validation (170), authorship provenance, external requirement metadata/fidelity validation, the external-assessment and matrix-builder tests, and failure-taxonomy tests.

The full 213-test suite initially had five failures; the public-projection fixture was updated for the new required empty `external_requirement_assessments` projection and its focused test passes. Four unrelated failures remain: the existing environment-metadata audit count (171 versus 170 current records), an alignment-exemplar expectation in the builder test, 64 unresolved external-assessment candidate flags, and a taxonomy-role fixture affected by the same source-branch taxonomy ledger mismatch below.

The taxonomy-adjudication validator also fails on the unchanged source-branch ledger: `VIGIL.FailureTaxonomy.Adjudications.json` declares taxonomy 0.6.8 while the validator requires 0.6.9, and it retains a reciprocal reference to absent `VIGIL-INC-000017`. This mismatch predates reconciliation; the ledger and deleted Incident were not rewritten as part of P0.
