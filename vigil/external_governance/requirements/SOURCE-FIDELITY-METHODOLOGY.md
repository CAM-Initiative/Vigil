# External Requirement Source-Fidelity Methodology

## Purpose

This document defines the semantic-fidelity contract for VIGIL external requirement extraction.

The contract exists because syntactically valid, source-traceable requirement records can still be materially lossy when a source heading, article, paragraph, control, table row or bullet is treated as an atomic governance requirement merely because the publisher formatted it as one unit.

The objective is not sentence-level atomisation. The objective is preservation of the material semantic payload required to determine what an external authority actually requires, recommends, permits, prohibits, defines or conditions.

## Core rule

An EXTREQ record MUST represent either:

1. one independently assessable normative or governance proposition; or
2. one source-defined action/outcome whose materially relevant constituent propositions are explicitly preserved in structured form.

A source-native structural container MUST NOT be presumed semantically atomic merely because it is labelled as an article, paragraph, control, subcategory, table row or bullet.

## Fidelity dimensions

Each represented requirement is assessed against the following dimensions:

| Dimension | Fidelity question |
| --- | --- |
| Actor | Who bears, exercises or receives the expectation? |
| Modality | Is the proposition mandatory, recommended, permitted, prohibited, definitional or otherwise qualified? |
| Action | What exactly must, should, may or must not occur? |
| Object | What system, artefact, dataset, process, person or decision does the action concern? |
| Applicability | Under what conditions does the proposition apply? |
| Threshold | Is there a trigger, threshold, confidence level or materiality condition? |
| Timing | When, how often, before/after what event, or for how long does it apply? |
| Qualification | What limits, narrows or modifies the proposition? |
| Exception | When is the proposition displaced or inapplicable? |
| Artefact | Does the source expressly require a record, declaration, register, policy, instruction or other artefact? |
| Verification | Does the source prescribe or contemplate an assessment or assurance method? |
| Constituent propositions | Does one source unit contain more than one independently meaningful obligation or governance proposition? |
| Locator | Can the represented proposition be traced to the narrowest reliable authoritative location? |

A readable `requirement_summary` does not substitute for preservation of these dimensions.

## Semantic atomicity states

### `atomic`

The represented source unit expresses one independently assessable proposition at the granularity used by the source.

Example: a NIST AI RMF Core subcategory that states one outcome.

### `source-defined-compound`

The source intentionally defines one action or outcome that contains several material constituent propositions which should remain linked as one source-defined unit.

The constituent propositions must be explicitly preserved rather than compressed into a summary.

Example: a NIST AI 600-1 suggested action that requires identification, ranking and evaluation as parts of one named action.

### `requires-decomposition`

The current EXTREQ compresses multiple independently assessable propositions and therefore cannot be treated as source-faithful at its present granularity.

Example: representing a multi-paragraph statutory article with distinct duties, conditions and exceptions as one generic article-level requirement.

### `not-applicable`

The record is definitional, reference-only or otherwise does not require an atomicity assessment under this contract.

## Source-level fidelity states

Source extraction completeness and source-fidelity assurance are separate concepts.

- `assured`: the represented source scope has been reviewed under this methodology and no material semantic compression is known within that scope.
- `provisional`: the extraction is useful and source-traceable but one or more records require constituent enrichment or further atomicity review.
- `requires-reextraction`: material compression has been demonstrated and the source must not be treated as a high-fidelity clause baseline until repaired.
- `blocked`: fidelity cannot be assessed because primary-text access is unavailable.
- `not-applicable`: the source has no canonical requirement extraction (including a supporting-only or context-only source). An extracted supporting authority requires substantive fidelity review on the same dimensions as an extracted primary source.

A source with historical `extraction_status: complete` is **not effectively complete for clause-level use unless its source-fidelity state is `assured`**.

Unlisted historical `complete` sources default to `fidelity-unassured` and are treated as effectively partial until reviewed under this methodology.

## Atomicity decision test

For each source unit:

1. Identify actor, modality, action, object, trigger, purpose, conditions, qualifications, scope and lifecycle/timing.
2. Identify material analytical constituents. Multiple verbs and source numbering do not decide atomicity.
3. Test whether proposed children retain those dimensions and are independently intelligible and assessable without importing missing meaning from siblings.
4. Test normative dependencies: communication of identified impacts, evidence of an assessment, conditional escalation, remediation of a detected issue, or consultation supporting a defined process.
5. Distinguish separately observable elements of one control, evidence chain or decision pathway from genuinely independent governance propositions. Preserve a coherent source-defined outcome and its structured constituents where splitting would distort or duplicate that outcome.
6. Decompose only where each child remains independently assessable and context-complete. Repeat inherited source context when necessary; do not strengthen modality, broaden actors/scope or invent timing, audiences or duties.
7. Record unresolved interpretation explicitly. Do not decide atomicity from prospective Fidelity Class mappings or existing Incident findings; existing consumers constrain migration only.
8. Complete individual atomicity dispositions before identity migration or migration-tool changes. Do not split examples or informative detail into normative duties.

## Identity and migration

Semantic decomposition is a material identity event.

When one coarse EXTREQ is replaced by multiple independently assessable propositions:

- allocate new deterministic identities from the existing identity seed contract;
- retire the coarse identity without reuse;
- preserve a migration relationship from the retired record to its replacements;
- do not silently change the meaning represented by an existing immutable requirement ID.

Where a source-defined action remains one unit and only constituent semantic detail is added, the EXTREQ identity may remain stable.

## Copyright and licensed-source boundary

This methodology does not require reproduction of copyrighted source text.

For licensed standards, VIGIL should preserve analytical propositions, source locators, hashes/digests and bounded constituent meaning without committing the licensed normative text itself.

## Completion rule

`complete` means more than all intended sections were processed.

For first-class requirement sources, effective completion now requires:

1. primary-text access appropriate to the source;
2. declared review scope;
3. no known unreviewed material within that declared scope;
4. semantic-atomicity review under this methodology;
5. material actors, obligations, conditions, qualifications, exceptions and timing preserved;
6. source-defined compound actions enriched with constituent propositions where needed; and
7. no known `requires-decomposition` record remaining within the represented scope.

This does not require atomising every sentence, note, example or informative annex. It requires preserving every materially independent governance proposition within the scope claimed as complete.

## Supporting-authority admission

The maintainer approved this bounded extension on 18 October 2026 under the revised 11 October Gate 1 proposal. `supporting-external-authority` may use `in-progress`, `partial` or `complete` for an explicitly declared extraction scope. `supporting-only` remains a legitimate zero-requirement state. Registration does not promote a source. Context/discovery and excluded sources remain ineligible.

Review the actual provision separately from its relationship to an existing Fidelity Class before canonical promotion. Preserve source-native modality, governed actor and object, timing, conditions, exceptions and voluntary or binding force. Commentary and implementation examples remain reference-only. Official extracts support only visible provisions; metadata cannot substitute for inaccessible clauses.

The requirement manager resolves the existing metadata ledger, fidelity ledger and relationship review artefacts for each extracted supporting requirement. Every metadata dimension needs a compatible reviewed disposition. Fidelity must be provisional or assured and enumerate the admitted requirement; a complete bounded scope requires assured fidelity. A supported direct or strong-supporting relationship must resolve to an existing class and a dated source-specific JSON review artefact. The artefact uses the established `source_identity`, `review_basis`, `reviewed_on` and `entries` structure. Its matching entry retains the complete relationship decision. Contextual or unresolved decisions remain review material.

For these new admissions, `requirement_sha256` hashes the full canonical requirement. `class_semantic_sha256` hashes class_id, definition, invariant, failure_condition, failure_recognition, success_condition, success_recognition and exclusions. Both use UTF-8 JSON with sorted keys, non-ASCII characters preserved and compact separators. This additive convention does not rewrite historical primary-source relationship digests. A changed proposition or class contract requires a new retained review decision.

Structural resolution confirms traceability, not substantive truth. A reviewer must still establish the normative proposition and material actor/object/condition correspondence. A nonempty rationale cannot prove either. Source fidelity, relationship admission, clause candidates and occurrence results remain separate decisions. No relationship determines legal applicability, liability or Aligned / Not aligned / Boundary.
