# EXTREQ-07 — IEEE 7009-2024 Fidelity Review

**Review date:** 2026-09-03  
**Source:** IEEE 7009-2024  
**VIGIL source ID:** `EXT-564A4CAA4F00`  
**External source ID:** `IEEE-7009`  
**Access basis:** lawfully accessed licensed primary text  
**Reviewed primary-source SHA-256:** `9fb640fd57202fcc1c90aec0b6b767bf5c4621bfdefa7911c5e102425a83b133`

## Disposition

The existing IEEE 7009 corpus was reviewed directly against the licensed primary PDF using analytical paraphrase only. No licensed IEEE source text is stored in VIGIL.

All 55 established canonical `EXTREQ-*` identities were preserved. Twelve deterministic source-native complementary records were added to represent distinct requirements that were compressed inside four legacy aggregate records and to represent the Clause 9.3 property-of-interest specification structure. The resulting canonical IEEE 7009 shard contains 67 records.

The four pre-existing aggregate identities remain canonical for compatibility and are linked to their source-native complementary records through `related_external_requirements`. They are also recorded in the re-extraction backlog because their coarse boundaries prevent five metadata dimensions from being asserted at source-native fidelity without an explicit future identity-migration decision. No established IEEE 7009 requirement was deleted or renumbered in this tranche.

Source-explicit metadata was added across the reviewed corpus, including actors, governed objects, evidence expectations, artefacts, timing, verification methods, applicability conditions and qualifications where supported by the source. Source silence is recorded rather than inferred. The Annex A.3 baseline ASOI requirement identities remain stable and now preserve substantially richer source-explicit conditions, constraints and verification context.

## Fidelity status

IEEE 7009-2024 remains `requires-reextraction` with effective status `partial` by design. This is not an access limitation: the complete licensed source was available. It records the deliberate preservation of four historical aggregate identities pending an explicit future compatibility/retirement decision.

## Validation results

The committed repair produced:

- 67 canonical IEEE 7009 records: 55 established identities preserved plus 12 deterministic additions;
- 785 metadata-complete records corpus-wide;
- 1,484 unresolved metadata field decisions corpus-wide;
- 187 records still requiring metadata review;
- four IEEE 7009 re-extraction backlog entries;
- 12 fidelity-assured effective-complete sources, unchanged because IEEE 7009 remains explicitly partial.

The following validation surfaces passed before commit:

- external-requirement metadata contract and generated metadata report;
- external-requirement source-fidelity validator;
- deterministic external-requirement projection build and generated-output validation;
- metadata regression suite;
- dedicated IEEE 7009 identity-preservation and bounded-fidelity regression;
- source-fidelity regression suite;
- `vigil/tests/test_external_requirements.py` and `vigil/tests/test_external_sources.py` — 34 tests passed.

## Maintainer action

Retain the four legacy aggregate identities until an explicit identity-migration decision is made. Future work may either continue treating them as compatibility aggregates or retire them through a documented successor migration; they must not be silently deleted, renumbered or reconstructed.
