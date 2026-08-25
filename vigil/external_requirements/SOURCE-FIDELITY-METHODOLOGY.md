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
- `not-applicable`: the source is supporting/context-only or otherwise outside first-class requirement extraction.

A source with historical `extraction_status: complete` is **not effectively complete for clause-level use unless its source-fidelity state is `assured`**.

Unlisted historical `complete` sources default to `fidelity-unassured` and are treated as effectively partial until reviewed under this methodology.

## Atomicity decision test

For each source unit:

1. Identify the actor, modality, action and object.
2. Identify every material condition, threshold, timing rule, qualification and exception.
3. Ask whether different constituent propositions could be independently satisfied or breached.
4. Ask whether a downstream compliance or failure analysis would need to distinguish those propositions.
5. If yes, decompose into separate EXTREQ records unless the publisher expressly defines them as one source action/outcome whose constituents should remain linked.
6. For a source-defined compound, preserve the constituent propositions explicitly.
7. Do not split merely because a sentence contains a list of examples or explanatory detail with no independent governance meaning.

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
