# External Requirement Metadata Review Queue Audit

Date: 2026-08-26

## Purpose

This audit records the transition from schema-valid EXTREQ metadata to explicit source-backed metadata review state before further clause extraction proceeds.

The review programme addresses a material ambiguity in the historical corpus: fidelity-critical array fields could be empty without distinguishing between (a) source review establishing that no value was specified, (b) the field being inapplicable, and (c) the field never having been reviewed.

## Scope

The metadata review contract covers:

- `applicable_actor`
- `governed_object`
- `timing_or_frequency`
- `required_artefacts`
- `evidence_expectation`
- `verification_method`
- `applicability_conditions`
- `exceptions_or_qualifications`

Review states are:

- `populated-reviewed`
- `not-specified-by-source`
- `not-applicable`
- `review-required`

## Corpus-wide queue

`validate-external-requirement-metadata.py --write-report` now produces:

1. a requirement-level queue of unresolved metadata decisions;
2. a source/version backlog ranked by unresolved field decisions; and
3. per-field counts distinguishing populated-but-unreviewed from empty-and-unreviewed values.

The report is intended to drive source-by-source remediation. Existing values are not treated as reviewed solely because they are populated.

## EU AI Act reviewed slice

The staged 27 July 2026 EU AI Act re-extraction covering Articles 4a and 9-15 has already undergone direct-primary-text semantic re-extraction and a source-explicit metadata-normalisation pass.

`seed-eu-ai-act-metadata-review.py` can therefore materialise field-level review decisions for that staged slice without manually maintaining hundreds of repetitive status rows. The seeder:

- is limited to the staged 27 July 2026 EU AI Act packages;
- applies the metadata-normalisation overlay before determining field state;
- records populated fields as `populated-reviewed`;
- records reviewed empty fields as `not-specified-by-source`;
- does not infer `not-applicable` automatically; and
- refuses to overwrite a conflicting existing review decision.

## Source-review order

Clause extraction remains paused while metadata review proceeds.

Recommended order:

1. EU AI Act staged Articles 4a and 9-15 — source-reviewed slice already suitable for ledger seeding;
2. NIST AI RMF 1.0 — previously assessed as fidelity-assured, but field-level metadata decisions still require explicit source review;
3. CycloneDX 1.7 — previously assessed as fidelity-assured for selected material, with field-level review still to be evidenced;
4. NIST AI 600-1 — provisional fidelity status; metadata review should be combined with constituent-semantic enrichment;
5. remaining public-primary sources, ranked by governance significance and review-queue size;
6. licensed primary sources only where lawful primary access is available;
7. blocked or metadata-only sources remain unresolved rather than being inferred from secondary material.

## Extraction-repair trigger

Metadata review is also an extraction-fidelity control.

Where source review shows that an actor, condition, timing rule, qualification, output, evidence expectation or verification requirement cannot be represented faithfully because the existing EXTREQ has collapsed multiple independent propositions, the record should be flagged for semantic re-extraction rather than patched with increasingly broad metadata.

The metadata programme therefore produces two outputs:

- closed metadata decisions for adequate EXTREQ records; and
- a bounded re-extraction queue for requirements that are structurally too lossy to repair in place.

## Validation boundary

Default metadata validation reports unresolved work but fails only on contradictory or malformed review-state contracts.

Strict validation is reserved for a source or corpus slice that is intended to be metadata-complete.

A green historical EXTREQ schema validation is not evidence that metadata fidelity has been substantively reviewed.

## Execution note

The repository changes in this pass define the deterministic queue and EU seeding workflow. A live corpus-wide report must be generated in a repository execution environment using the documented commands before numeric queue totals are treated as authoritative.
