# TAXONOMY-02 Migration and Validation Audit

## Repository-state preflight

Verified on 2026-08-24 before editing:

| Ref | Remote head | Position relative to `main` |
|---|---|---|
| `main` | `e3d1dcb12875642c71ca3100b43b6d63872bf69a` | baseline |
| `agent/failure-taxonomy-prototype` | `0578a70b71fac1ae4ed3cf25a713230319acfa55` | 13 ahead, 0 behind |
| `agent/extsrc-ux-01` | `c390c9f2bed36c29981e0cb4f17d00526995dd0f` | 4 ahead, 0 behind |

No commits had been added after the handoff heads. The taxonomy and EXTSRC branches shared merge base `e3d1dcb12875642c71ca3100b43b6d63872bf69a` and remained intentionally diverged. Their preflight changed-file sets did not overlap. No merge, rebase, reset, cherry-pick, force-push, branch creation, or EXTSRC copying was performed.

## Identifier migration

- Families migrated: **4**
- Classes and variants migrated: **27**
- Immutable family IDs allocated: `VIGIL-FF-0001` through `VIGIL-FF-0004`
- Immutable class IDs allocated: `VIGIL-FC-000001` through `VIGIL-FC-000027`
- Stable-ID filenames applied: **4**
- Legacy public semantic paths preserved as aliases: **31** (4 family paths and 27 class paths)
- Relationships converted to immutable class-ID targets: **all current relationships**
- New canonical families admitted: **0**

## Legacy corpus inventory

Source corpus: `CAM-Initiative/Caelestis` `main` at `ad3dd5756750ae08692a2f9b146641f918103c67`.

- Inventory entries reviewed: **159**
- `OPS.FF` controlled values inventoried: **13**
- Named Runtime & Governance Failure Taxonomy §3 entries inventoried: **58**
- Related `PFAIL`, `SEC.BF`, `OPS.RGRF`, and `OPS.VFC` controlled values inventoried: **22**
- Orthogonal `OPS.FCS`, `OPS.FMA`, and `OPS.AGMA` status/metadata values inventoried: **26**
- Named domain-embedded classifications inventoried across MENTIS, observability, economics, relation, and stewardship routing: **40**
- Direct matches to an existing portable family: **6**
- Existing-class variants: **9**
- New-family candidates retained for later evidence review: **21 entries**
- New-class candidates retained for later evidence review: **23 entries**
- Entries requiring split: **44**
- Additional entries requiring judgement: **3**
- Historical buckets determined not to be mechanisms: **11**
- Harm/consequence axes: **7**
- Manifestation/locus axes: **3**
- Other orthogonal axes: **29**
- Duplicate or semantic-overlap entries: **3**

The inventory is a separate non-normative migration ledger. No Caelestis path, instrument authority, constitutional relationship, or CAM dependency was added to the portable family JSON.

The completeness boundary is classificatory: canonical failure/status/metadata values, every named primary-taxonomy entry, and named enumerated failure families or modes in the reviewed domain instruments. Ordinary normative clauses that merely describe a possible operational failure are not treated as separate legacy taxonomy entries unless the source presents them as a classification.

## Generated references

- Complete standalone family HTML pages: **4**
- Combined complete reference-book HTML pages: **1**
- Combined reference contents include all **4 families** and **27 classes/variants**.
- Public reference pages contain no renderer, canonical-source, review-view, repository-workflow, or implementation-commentary notice.

## Validation results

Passed:

- `python -m unittest vigil.tests.test_failure_taxonomy` — **8 tests passed**
- `python vigil/taxonomy/validate_taxonomy.py` — **4 family files and 27 classes validated against JSON Schema; catalogue integrity OK**
- Python bytecode compilation for taxonomy scripts and tests
- HTML parser check for all five generated reference pages

Repository-wide `python vigil/scripts/validate-vigil-records.py` still fails on unresolved research-to-PROP/PATCH links and emits unresolved-link warnings across existing FM/OBS records. Those records were not changed in TAXONOMY-02; the failures pre-date and are outside this package.

## Unresolved interpretation boundaries

The 44 `SPLIT_REQUIRED` entries must be decomposed before admission, especially compound claim handling, cognitive inference, protective enforcement, governance overcomplexity, oversight/capture, classification collapse, and economic/automation entries. The 21 named candidate clusters in the review projection are hypotheses, not approved families; singleton and low-evidence clusters remain subject to the family-admission rule. Harms, affected groups, modality, responsibility, severity, and evidence state remain outside the hierarchy.

## TAXONOMY-03 handoff

Use the migration ledger to select only three to five high-evidence bounded families. Resolve splits and overlaps first, approve family invariants and exclusion rules, then allocate immutable IDs. Return unresolved entries to the ledger rather than forcing classification. Regenerate all family pages and the combined reference and run catalogue-wide validation after every batch.
