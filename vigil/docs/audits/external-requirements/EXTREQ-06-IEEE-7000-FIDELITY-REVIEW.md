# EXTREQ-06 — IEEE 7000-2021 Fidelity Review

**Review date:** 2026-09-03  
**Source:** `EXT-31AD0314218F` / `IEEE-7000` / `2021`  
**Access basis:** lawful licensed primary-text review  
**Reviewed-source SHA-256:** `559bdf6648f0d5f70529fd71848f068c92718ca9aa577a7de7abd8dc060b8ef6`

## Scope and fidelity finding

A clause-level comparison was performed against the complete licensed IEEE 7000-2021 primary PDF. Copyrighted source text was not stored in VIGIL.

The existing 55-record extraction was substantially sound but was not fully fidelity-complete. All 55 established `EXTREQ-*` identities and clause locators were confirmed as defensible and preserved. Four normative activities were absent from the represented process model:

- Clause `7.3(h)(3)` — ConOps refinement as prioritized values, ethical value requirements and ethical risk-based design information develop;
- Clause `8.3(e)` — identification and recording of technical and organizational risks and opportunities affecting values;
- Clause `8.3(f)` — conceptual value analysis and refinement of prioritized value clusters; and
- Clause `8.3(g)` — approval and recording of prioritized values.

Four deterministic records were therefore added:

- `EXTREQ-9F9F312D1F384F0A` — `7.3(h)(3)`
- `EXTREQ-6B251B00C962BBBC` — `8.3(e)`
- `EXTREQ-AA32F6158A98B7E1` — `8.3(f)`
- `EXTREQ-C4216CD9308BCAE5` — `8.3(g)`

The established Clause `8.3(d)` record `EXTREQ-C3E5B151DB2EE358` retained its ID, identity key and locator, but its analytical summary was narrowed because the previous summary incorrectly folded the separate Clause `8.3(g)` approval activity into `8.3(d)`.

The repaired IEEE 7000 source population is therefore **59 records**: 55 preserved established identities plus four deterministic source-fidelity additions.

## Metadata review

All 59 records were reviewed across the eight external-requirement fidelity dimensions. Metadata was populated only where supported by the primary source; silence was explicitly recorded as `not-specified-by-source`.

The reviewed tranche populated source-supported values on 59 actor records, 59 governed-object records, 10 timing/frequency records, 22 artefact records, 22 evidence records, 14 verification-method records, 59 applicability-condition records and 59 qualification records.

## Corpus effect

After the tranche:

- canonical external requirements: **858**
- IEEE 7000 metadata review: **59 / 59 complete**
- metadata-complete records: **722**
- review-required records: **238**
- unresolved field decisions: **1,904**
- fidelity-assured effective-complete sources: **12**
- historical-complete sources still downgraded for lack of fidelity assurance: **5**

`source-fidelity.json` records IEEE 7000-2021 as `assured` / effectively `complete`. The reviewed source digest is preserved in the requirement interpretation provenance and source-review assurance layer without implying human verification.

## Validation

The successful execution passed:

- metadata-review validation and report generation;
- source-fidelity validation;
- deterministic external-requirement projection rebuild;
- generated-output validation (`81` source versions / `858` requirements);
- metadata-review regression;
- source-fidelity regression; and
- **34** external requirements / external sources tests.

The canonical repair commit is `e4676621bf91bccf1dd71b2d08bde39771690ad3` (`EXTREQ-06: repair IEEE 7000 fidelity`).

The one-off repair script and temporary workflow are removed after successful execution. This file is the durable review record.
