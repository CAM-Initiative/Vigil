# Incident classification-role mapping migration audit

**Execution date:** 2026-09-18  
**Branch:** `chore/vigil-citation-root-url`  
**Starting branch head:** `5e0f3b3993ba7ca480c836ef7b6ccea7e7355a19`  
**Scope:** Canonical Incident records under `vigil/records/incidents/` and their schema, validation, build, template, test and generated-public-record machinery  
**Change type:** Deterministic schema and representation transformation; no taxonomy re-adjudication

## Preflight corpus audit

| Measure | Count |
| --- | ---: |
| Total canonical Incident records | 131 |
| Records with a primary class mapping | 86 |
| Records with one or more secondary class mappings | 29 |
| Primary class mappings | 86 |
| Secondary class mappings | 46 |
| Total class mappings | 132 |
| Records with block-level `failure-occurrence` | 5 |
| Records with block-level `successful-invariant` | 1 |
| Mapped records missing a block-level role | 80 |
| Records already carrying a mapping-local role | 0 |
| Records not deterministically migratable | 0 |

The 80 mapped records without a block-level role were deterministically ordinary failure mappings under the pre-migration contract, which expressly preserved `failure-occurrence` semantics for existing mapped Incidents without `classification_role`. No role was inferred from primary/secondary position, severity or `exemplar_execution`.

## Transformation applied

- Added `classification_role` to every existing canonical primary and secondary class mapping.
- Copied the six existing valid block-level roles to their mappings: five `failure-occurrence` records and the `VIGIL-INC-000126` `successful-invariant` regression anchor.
- Applied the existing backwards-compatible `failure-occurrence` semantics to all mappings in the other 80 mapped records.
- Retained every existing block-level role as a legacy compatibility summary and did not introduce a block-level `mixed` value.
- Preserved all family IDs, class IDs, mapping positions and ordering, classification bases, confidence, taxonomy versions, classification statuses, evidence, severity, diagnosis and provenance.
- Updated `record_identity.updated` to `2026-09-18` and incremented the patch component of `record_identity.version` once for each of the 86 structurally modified canonical records.
- Left the 45 Incidents without canonical class mappings structurally and version-wise unchanged.

Resulting mapping-role totals are 131 `failure-occurrence` mappings and one `successful-invariant` mapping. `VIGIL-INC-000126` remains classified against `VIGIL-FC-000073` solely as an admitted successful-invariant exemplar and is excluded from failure-case and Repair projections.

## Canonical records modified

The following 86 records received mapping-local roles and the associated patch metadata update:

```text
VIGIL-INC-000001, VIGIL-INC-000002, VIGIL-INC-000003, VIGIL-INC-000004,
VIGIL-INC-000005, VIGIL-INC-000006, VIGIL-INC-000007, VIGIL-INC-000008,
VIGIL-INC-000009, VIGIL-INC-000010, VIGIL-INC-000012, VIGIL-INC-000018,
VIGIL-INC-000023, VIGIL-INC-000024, VIGIL-INC-000027, VIGIL-INC-000029,
VIGIL-INC-000030, VIGIL-INC-000032, VIGIL-INC-000033, VIGIL-INC-000036,
VIGIL-INC-000041, VIGIL-INC-000045, VIGIL-INC-000047, VIGIL-INC-000048,
VIGIL-INC-000049, VIGIL-INC-000050, VIGIL-INC-000051, VIGIL-INC-000052,
VIGIL-INC-000053, VIGIL-INC-000054, VIGIL-INC-000055, VIGIL-INC-000056,
VIGIL-INC-000057, VIGIL-INC-000058, VIGIL-INC-000059, VIGIL-INC-000060,
VIGIL-INC-000061, VIGIL-INC-000062, VIGIL-INC-000063, VIGIL-INC-000064,
VIGIL-INC-000065, VIGIL-INC-000066, VIGIL-INC-000067, VIGIL-INC-000068,
VIGIL-INC-000069, VIGIL-INC-000070, VIGIL-INC-000073, VIGIL-INC-000078,
VIGIL-INC-000079, VIGIL-INC-000080, VIGIL-INC-000081, VIGIL-INC-000082,
VIGIL-INC-000083, VIGIL-INC-000084, VIGIL-INC-000085, VIGIL-INC-000086,
VIGIL-INC-000088, VIGIL-INC-000089, VIGIL-INC-000090, VIGIL-INC-000093,
VIGIL-INC-000097, VIGIL-INC-000098, VIGIL-INC-000099, VIGIL-INC-000101,
VIGIL-INC-000102, VIGIL-INC-000103, VIGIL-INC-000104, VIGIL-INC-000105,
VIGIL-INC-000110, VIGIL-INC-000111, VIGIL-INC-000112, VIGIL-INC-000113,
VIGIL-INC-000114, VIGIL-INC-000115, VIGIL-INC-000116, VIGIL-INC-000117,
VIGIL-INC-000121, VIGIL-INC-000122, VIGIL-INC-000123, VIGIL-INC-000124,
VIGIL-INC-000125, VIGIL-INC-000126, VIGIL-INC-000131, VIGIL-INC-000132,
VIGIL-INC-000133, VIGIL-INC-000134
```

## Contract and projection changes

- Mapping-local role is authoritative and required whenever a class mapping exists.
- A retained homogeneous block-level role must agree with every nested role; deliberately mixed records omit the legacy summary.
- Primary/secondary position is projected separately as `mapping_position` in generated class examples.
- The lightweight Incident index preserves primary and secondary mapping objects with `family_id`, `class_id` and `classification_role`.
- The generated Repair mapping set contains only `failure-occurrence` mappings.
- Generated class examples are separated into failure `classes` and `successful_invariants`, with deduplication by Incident ID, class ID and mapping role.
- The Incident template authors the role on the mapping rather than at block level.

Regression coverage includes primary failure only, primary plus secondary failure, primary exemplar only, primary failure plus secondary exemplar, and primary exemplar plus secondary failure. It also rejects a contradictory legacy block-level role.

## Human-review queue

None. Every existing canonical mapping was transformed deterministically. No record was left partially migrated and no taxonomy adjudication was reopened.

## Validation result

- Full `vigil/tests/` suite: 147 tests passed.
- Canonical Incident validation: 131 records passed.
- Lightweight public-record validation: 131 records passed.
- Source provenance: 228 active source records passed.
- Interpretive provenance: 131 Incidents passed.
- System-component validation: 131 Incidents passed.
- Authorship-provenance validation: passed.
- Taxonomy validation: 14 family files and 66 classes passed in working-branch mode.
- Deterministic build regression: passed.
