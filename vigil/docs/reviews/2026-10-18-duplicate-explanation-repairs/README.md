# Duplicate assessment explanations — implemented control and completed repairs

Date: 18 October 2026. Baseline: `333bf9d34ef3973068dfacf26815686b1740ddc3`. Branch: `agent/incident-ecosystem-ingestion`; existing draft PR 137.

Michelle explicitly approved both Gate 1 (the described blocker) and Gate 2 (its affected failures). The earlier proposal and inventory remain historical artefacts. This audit records implementation and the subsequent review; no further approval was requested for that scope.

## Implemented rule

`assessment_errors()` in `vigil/scripts/occurrence_requirement_validation.py` now blocks identical complete `assessment_basis` values reused across different canonical requirement IDs within an Incident. Comparison normalises Unicode NFKC, case and whitespace. The diagnostic names every participating row and requirement. Canonical and standalone occurrence-requirement validation use the same helper.

The rule permits a common factual sentence when the complete explanations address different requirements. It excludes other fields, source evidence, taxonomy reference conditions and review history. It does not use similarity scores, a word-count threshold or an automatic replacement system. Permanent tests use isolated fixtures rather than a fixed live-record failure set.

## Actual failure set and repair review

The implemented read-only run produced **43 groups, 259 participating assessment rows in 35 Incidents**, exactly matching the post-INC-117 proposal inventory. `implemented-rule-before-repair.txt` preserves the actual diagnostics. The repeated text was an authored-content defect; evidence and references were structurally valid. The new blocker was not weakened to clear those failures.

All 259 affected explanations were reviewed against **77 distinct canonical requirement propositions**, relevant actors, scope/qualifications, existing occurrence evidence and decisive missing facts. Shared event facts remain where needed. Missing organisational plans, cadence, training records, secure timestamps, record formats or governance gates are distinguished rather than combined into a generic list. No identifiers or arbitrary suffixes were added merely to make the text unique. No evidence or assessment row was deleted.

The per-Incident audits preserve complete old/new rows and the canonical propositions compared. `reviewed-requirement-snapshots.json` records the central requirements used, including their conditions. Existing occurrence narratives, source clauses, source references and limitations were reviewed as context; primary sources were reopened selectively for recording/traceability and the NIST Profile. This is not a claim to have independently reread every original source or re-adjudicated all unflagged rows.

## Six substantive result corrections

The retained IEEE 7001 Table 4 Level 4 requirement expressly requires Levels 1–3 as prerequisites. INC-157, INC-159, INC-170, INC-173, INC-176 and INC-177 already retained Boundary findings for secure timestamps and standard/open-standard recording. Their positive decision-context evidence cannot establish full progressive Level 4 alignment. The corresponding six rows therefore change **Aligned → Boundary**. Their useful recorded decision premises remain in the explanations.

All other affected-row results are preserved. Provider/evaluator investigation and event-recording evidence remain distinct from secure timestamps, standard recorder conformity, complete organisational audit history and data-retention policy. Existing integrated conclusions describe bounded reconstruction and unresolved broader arrangements; they do not assert complete Level 4 conformity, so those narratives need no rewrite.

The NIST output-review findings retain the current canonical proposition's broad output-validity/safety wording and its code-specific qualification. Non-code findings are expressly bounded to the observed output review; they do not claim generated-code testing. The authoritative NIST Profile was reopened to inspect the full action wording. No central requirement, extraction or normative source was rewritten.

## Preservation and verification

Each changed Incident increments its record version, dates the reviewed rows and appends AI interpretive provenance. Before/after assertions protect source records, quotations, source-clause structure, episode references, derivation links, taxonomy mappings, Harm Impact, narratives and all unflagged external rows. The record-level audit retains six result-change reasons; all other protected canonical content is unchanged as parsed JSON.

Builders regenerate public projections. Required canonical/public/provenance/component/authorship/occurrence-requirement checks and the complete test suite are run. The full suite passes **281/281 tests**, and the new blocker reports **zero remaining failures**. The final command outcomes are in `validation.json`. Structural success establishes the implemented contracts; the row-specific audits establish what was substantively compared and what remains evidence-limited.

No taxonomy release, source admission, requirement extraction, global Incident-by-requirement runtime matrix, website change, merge or deployment is included.
