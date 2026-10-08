# Validator and source-event integrity repair — maintainer decision proposal

**Date:** 2026-10-08
**Status:** Proposal only. No validator, schema, builder, CI workflow, taxonomy or canonical record modification authorised by this file.

## 1. Current behaviour

- `vigil/scripts/validate-vigil-records.py` checks the existing clause `adjudication_status` values, whether `mapped` has a canonical relationship, `resolved-no-mapping` does not, and whether the stored `adjudication_coverage.status` agrees. It does not determine that clauses are unique material events, chronologically correct, exhaustive or source-provenanced.
- `vigil/scripts/occurrence_requirement_validation.py` checks that `external_requirement_assessments[].source_clause_indices` refer to in-range clauses supporting the referenced canonical class and reviewed FC–EXTREQ relationship. A semantically stale *in-range* pointer can still pass, especially when the same class recurs.
- Clause groups have `source_url` and `source_record_order`, but individual clauses lack stable episode identifiers and reliable source-record references. The source evidence exists in `source_records[]`.
- `validate-vigil-public-records.py` checks derived index content against canonical records, but `.github/workflows/vigil-records.yml` calls `build-vigil-public-records.py` before the validator and later commits rebuilt outputs. A green run cannot, by itself, prove that the branch's previously committed index was current before the build.
- The retired global Incident × FC matrix is not a canonical authority or validation prerequisite. It must remain retired; the separate Harm Impact Matrix is not implicated.

## 2. Proposed behaviour, phased and separately approved

**Phase A — read-only diagnostics, no new canonical pass/fail:** report candidate duplicate episodes, source-linkage gaps, event-order uncertainties and any prebuild generated-output drift. Store findings in dated review manifests; lexical similarity and missing-keyword heuristics remain advisory.

**Phase B — optional additive event identity and provenance contract:** propose an immutable incident-local `episode_id` per material source-clause episode and resolvable `source_record_refs[]` per clause, with optional reviewed `display_order` plus an explicit `temporal_relation`/unknown-or-concurrent cue. Choose exact syntax/schema after maintainer approval. Do not infer event identities, timestamps or ordering from clause index or topic similarity.

**Phase C — stable EXTREQ event references:** after exact old/new episode crosswalk review, add `source_episode_refs[]` as an alternative to numeric `source_clause_indices`. During transition, allow both; if both present, check equivalent evidence and canonical class membership. Migrate records per approved tranche. Retire position-only references only after complete verified migration and downstream renderer review.

**Phase D — generated-output hygiene:** produce an independently visible diff/status between checked-in outputs and deterministic builder outputs *before* any automatic write or commit. Initially diagnostic. An enforcing freshness gate that newly fails a PR is a separate semantic decision.

**Phase E — human evidence-fidelity review certificate:** maintain review manifest disposition separately from `taxonomy_classification.adjudication_coverage`. The validator may check structure and provenance links once approved; only an attributable source-first reviewer can attest to evidence coverage and semantic event distinctness.

## 3. Pass/fail delta and counterexamples

| Example | Today | Proposed after explicit activation |
|---|---|---|
| Two clauses paraphrase one action for different FC roles | Can pass | Permitted structurally; human review determines whether they are one episode supporting both classes, not a forced deletion |
| A material source action is missing but every recorded clause is mapped | Can say taxonomy `complete` | Taxonomy status unchanged; evidence-fidelity state remains unreviewed/pending until independent source comparison |
| An in-range EXTREQ pointer targets a new event with the same FC after reordering | Can pass | Episode-ID referential equality rejects mismatched **reviewed** event reference once migrated |
| Clause has no source-record lineage | Passes current contract | Would fail *only for migrated opt-in records* once strict provenance contract approved; historical records pass until phased transition |
| Concurrent agent actions lack exact timestamps | Can pass | Still valid; unknown/concurrent timing explicitly representable, never forced into fabricated chronology |
| Checked-in generated index lags canonical records, but CI rebuilds it | CI may subsequently pass and auto-commit | Diagnostic drift is surfaced before rebuild; gate to fail is not enabled unless approved |
| Historic positive/ambiguous class mapping on a shared episode | Can pass | Continues to pass; episode may hold failure, success and boundary relations where evidenced |

## 4. Affected surfaces

`vigil_assessment.source_clause_analysis`, `source_records[]`, `taxonomy_classification` (completeness language only), `external_requirement_assessments[].source_clause_indices`, newly proposed stable episode links, `vigil/VIGIL.Schema.json`, `validate-vigil-records.py`, `occurrence_requirement_validation.py`, `build-vigil-public-records.py`, `validate-vigil-public-records.py`, `.github/workflows/vigil-records.yml`, and website Case File Stage 02 and Stage 04 projections. Renderer changes are not authorised by this proposal.

## 5. Measured corpus impact

Frozen inventory at `d845b4b`: **179** canonical Incidents, **592** source-record entries, **557** source-clause entries, **1,315** external-requirement assessment rows. **88** Incidents contain position-based EXTREQ assessment links; **1,051** assessment rows use them. **61** Incidents contain four or more source records. These are exposure counts, **not** counts of incorrect mappings, source omissions or required migrations.

Backfilling episode IDs and per-clause provenance could require review across the whole 179. Exact semantic-change counts are unknown until source-first manifests are assessed. The six pilot records and the four preliminary first-tranche reviews are not source-exhaustiveness certified.

## 6. Repair implications

Phased record-by-record schema additions and approved evidence-source crosswalks; revised public projection and documentation; potentially changed clause order or detail; conditional taxonomy and harm review only on actual new evidence; EXTREQ links reviewed individually. No bulk summary rewrite, automated class reassignment, severity change or role polarity inference.

## 7. Data-loss and semantic-drift risks

Automatic deduplication can remove multiple distinct observations of one event or erase distinct successful-invariant evidence. A single chronological integer can incorrectly linearise concurrent agent activity. A mechanically shifted EXTREQ index can silently attach assessments to unrelated events. Requiring a source reference before migration can invalidate all legacy cases. Public `complete` may be misread as evidence exhaustiveness; do not change its stored semantics silently.

## 8. Appropriate enforcement surfaces

- **Schema/validator:** referential uniqueness and integrity, allowed statuses, stable ID resolution, dual-reference consistency, provenance shape and deterministic generated projection equality *if approved*.
- **Human review manifest:** source comparison, material omitted action, duplicate-episode judgment, true chronology and completeness, taxonomy recognition and evidence limitations.
- **Renderer:** present documented relative chronology and uncertainty clearly; one event with multiple relationship explanations is not multiple events.
- **Authoring guide:** require source-specific support and explicit historical corrections; prohibition on fabricated timestamps or harmonised prose.

## 9. Stop conditions and approval questions

1. Human maintainer first reviews and explicitly approves each **specific** Phase B/C/D semantic control and its migration policy. A broad instruction to review the corpus is not approval to redefine validator failures.
2. After any approved change, execute a read-only whole-corpus run, publish exact failing record/field list and before/after examples; **stop for separate broad-record repair approval**.
3. Do not modify existing semantic fields or validators where observed behaviour conflicts with documented crosswalk; escalate ambiguity.
4. Do not restore the old global Incident × Fidelity Class matrix or make the new review ledger a replacement mapping authority.

**Recommended decision:** approve source-first review manifests and Phase A diagnostics now; consider Phase B/C stable event provenance after representative old/new crosswalks from INC-084/141/151/177; separately decide how prebuild generated-output drift should be enforced.
