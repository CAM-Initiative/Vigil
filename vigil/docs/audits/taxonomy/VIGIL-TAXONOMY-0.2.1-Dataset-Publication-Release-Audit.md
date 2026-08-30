# VIGIL Failure Taxonomy 0.2.1 Dataset Publication Release Audit

**Release date:** 2026-08-27  
**Working branch:** `agent/hugging-face-authority-reconciliation`  
**Pre-release head:** `86549eeb8a0fdced5a76be900059765041a6b8ac`  
**Dataset/book version:** `0.2.1-draft`  
**Taxonomy state:** 9 families / 53 classes and variants / `removed_ids: []`

## Purpose

This bounded follow-up publishes the family semantic and parent/child alignment repair as a versioned downloadable taxonomy dataset and Full Reference Manual. It also prevents future canonical family or class amendments from being published under stale dataset metadata.

The preceding `VIGIL-TAXONOMY-Family-Semantic-and-Parent-Child-Alignment-Repair-Audit.md` correctly records that its implementation initially retained dataset version `0.2.0-draft`. This release does not rewrite that historical statement. It records the subsequent publication decision separately.

## Versioning decision

Dataset/book versioning is distinct from individual family-record versioning and from the historical taxonomy version attached to a Failure Mode classification decision.

- Amendments or additions within the existing family structure increment the third digit.
- Admission of a new failure family increments the second digit and resets the third digit.
- The first digit is reserved for a deliberately approved, materially incompatible re-foundation.
- Every dataset release carries a fixed ISO publication date.
- Historical Failure Mode classification stamps are not advanced without substantive re-adjudication.

The semantic reconciliation amended existing family records without admitting a new family. The correct dataset transition is therefore `0.2.0-draft` to `0.2.1-draft`, dated `2026-08-27`.

## Enforcement architecture

`VIGIL.FailureTaxonomy.Index.json` now contains a release history with:

- dataset version;
- fixed publication date;
- declared change level;
- canonical family/class content digest;
- immutable family-ID set; and
- class count.

The taxonomy validator recomputes the canonical digest from the `family` and `classes` objects, excluding duplicated dataset-release metadata. It rejects:

- family or class content changes without a new release digest;
- missing, invalid or inconsistent dataset version/date metadata;
- dataset metadata not projected consistently into every family document;
- a minor increment for an existing-record change;
- a patch increment when a new family has been admitted; and
- a routine release entry without an underlying family/class content change.

The current `0.2.0-draft` digest is preserved as a legacy undated baseline. The repaired family/class content is recorded as the `0.2.1-draft` patch release.

## Publication projection

The Full Reference Manual cover now renders:

- Version: `0.2.1-draft`
- Status: `Draft`
- Edition date: `27 August 2026`
- Families: 9
- Failure classes: 53

The date is canonical metadata rather than a generation-time clock value, preserving deterministic regeneration. The Case File reverse-mapping projection and classification ledger identify the current dataset version. Existing Failure Mode classification records retain their historical version stamps.

## Scope preservation

No family or class content, immutable ID, family membership, Failure Mode classification, confidence assessment, historical audit, HF-02 evidence record, EXTREQ content, or unrelated provenance work was changed by this release package.

## Validation

The final validation record is:

- taxonomy schema and catalogue: PASS — 9 families / 53 classes;
- focused failure-taxonomy tests: PASS — 29 tests, including five release-metadata regressions;
- focused taxonomy-classification tests: PASS — 24 tests, including legacy `0.2.0-draft` classification compatibility;
- full `vigil/tests` discovery: PASS — 174 tests;
- full `vigil/scripts` discovery: PASS — 37 tests;
- repository and public-record validators: PASS — 102 JSON records, 6 research records and 108 public records;
- Failure Mode facets: PASS — 72 Failure Modes / 2 faceted records;
- pipeline state, lifecycle/corpus coverage, observatory boundary, interpretive provenance, authorship provenance, source provenance, system-component and CAM-assessment validation: PASS;
- external sources and requirements: PASS — 81 source versions / 845 requirements;
- source-fidelity and metadata-review contracts: PASS, retaining the existing 16 fidelity downgrades and 527 metadata-review records;
- EU AI Act staged re-extraction: PASS — 8 retirements / 102 candidates / 18 metadata normalisations;
- registry/index, family HTML, Full Reference HTML and PDF deterministic regeneration: PASS, byte-stable;
- JSON and generated-HTML parsing, Python bytecode compilation and `git diff --check`: PASS; and
- final PDF: valid PDF 1.7, A4, 82 pages, with the amended cover and contents pages visually inspected without layout defects.
