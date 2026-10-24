# Wording-specific evidence checks — Gate 1 proposal

Status: approved by the human maintainer on 18 October 2026: “blocking validation is approved as a validation update.” Implemented as recorded in [the pinned historical implementation report](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-18-wording-validation-implementation.json). The proposal below preserves the approved scope.

## Current behaviour

MAINTAINERS.md requires exact wording where interpretation depends on wording, chronological context, separately reasoned statements, clear attribution and explicit unknowns. Existing canonical checks cover episode identifiers, references, clause dispositions and classification completeness. They do not enforce this wording-specific authoring contract. The website checks statement bindings at display time and falls back to the complete parent episode if bindings are malformed; it does not reject the canonical record.

## Proposed behaviour

Add bounded structural checks to the canonical Incident validator, with regression fixtures:

1. Whenever optional `vigil_assessment.source_clause_analysis.clauses[].statement_analysis` is supplied, require unique nonempty statement IDs, nonempty statement-specific interpretation, and integer, in-range relationship indices. Every parent relationship must be bound exactly once. Empty index arrays remain valid for context statements with no taxonomy relationship. Do not merge episodes or manufacture new episode IDs.
2. Add an optional `wording_evidence` object to a clause or individual statement. Its `basis` is `original-quotation`, `attributed-quotation` or `unavailable`. Quotation bases require a nonempty local `source_anchor`, valid effective parent source references, and nonempty local context (`source_paraphrase`). An attributed quotation additionally requires nonempty `attribution` and `access_limitations`. An unavailable basis requires nonempty `access_limitations` and `source_paraphrase`; `source_anchor` must be absent or empty so a paraphrase cannot be presented as verbatim evidence.
3. Existing records without the marker remain accepted. Do not infer wording dependency from keywords. Do not add the marker retrospectively without a separately approved bounded edit. If the schema rejects additional properties at those locations, amend it only to allow this optional object with the stated shape.

These checks can enforce declared structure, not truth. Exact correspondence to the source, chronology, missing pre-context, interpretive adequacy and whether statements have been improperly combined remain human-review obligations. The validator must not claim to establish them from nonempty strings.

## Pass/fail delta

A parent with three relationships but statement indices `[0]` and `[2]` currently survives canonical validation and falls back in the renderer; it would fail with a diagnostic identifying missing index 1. Duplicate, fractional or out-of-range indices would also fail. A marked quotation without its actual anchor, or an attributed quotation without attribution/access limits, would newly fail. An unavailable source with explicit limitations would remain valid without inventing wording. Unmarked historical clauses would remain valid. No previously failing record is intentionally newly accepted.

## Affected fields and surfaces

Only the optional structures above and canonical validator/schema fixtures are proposed for enforcement. The public builder must continue to preserve these structures. Section 02 interactive, print and static displays consume them; renderer fallback continues to protect legacy or externally supplied data. No Section 05 prose, taxonomy mapping, evidence-state, severity, HIM or external-requirement acceptance rule changes are proposed.

## Expected corpus impact and repair implications

Read-only inventory after the eight approved repairs: 9 of 194 records use statement analysis: INC-043, 129, 130, 136, 137, 138, 183, 185 and 195; 12 parent clauses, 38 statements. All current bindings pass a one-off exhaustive/unique binding check. No record currently carries the proposed marker. Its full proposed fixture/check suite has not been implemented, so a complete failure inventory is not yet available.

No mandatory migration, prose rewrite, reclassification, source replacement, field movement or deletion is proposed. Any later marker adoption requires explicit review of the evidence basis. Generated outputs would need rebuilding only for an approved record change. Mechanical repair could delete relationships, flatten chronology, mislabel an author's account as a native model quotation, or invent text to satisfy a nonempty-field check; none is permitted.

## Why validation, and stop condition

Relationship indices and a deliberately declared evidence basis have machine-checkable invariants shared by all consumers; documentation alone cannot prevent broken bindings or an empty quotation disclosure. Interpretation remains in authoring/review, and readability remains in the renderer. These checks deliberately do not substitute a keyword or minimum-length heuristic for adjudication.

Under MAINTAINERS.md Gate 1, stop before implementing this proposal and obtain approval for precisely this pass/fail behaviour. If approved, implement the checks and run a read-only corpus audit. Report every newly failing record and stop again under Gate 2 before any multi-record repair. Preserve full record content while resolving failures; never automatically drop relationships or rewrite wording to pass.


### Implementation verification archived — 24 October 2026

The completed 18 October Gate 1 receipt ([original JSON](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-18-wording-validation-implementation.json)) recorded **12 passing isolated wording-evidence fixtures**, **258 passing tests**, 194 at-time valid canonical records, no validator-induced repair, and independently approved INC-199/200 rebuild guards. It did **not** establish authenticity, quotation fidelity, adequate chronological context, or a semantic classifier: unmarked historical clauses remained admissible. The structural validator and maintained fixture suite, original approved control specification above, and canonical Incident records continue to own the implementation. That snapshot's taxonomy 0.6.11 and 15-family/78-class test counts are historical rather than claims about the present taxonomy.
