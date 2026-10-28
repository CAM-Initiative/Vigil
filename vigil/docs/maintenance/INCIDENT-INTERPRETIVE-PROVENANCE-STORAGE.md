# Incident interpretive provenance — current-state retention policy

**Maintainer decision:** 28 October 2026, revised issue #168 / PR #180. This replaces the superseded historical-review indexing/archive proposal. Implemented as a backward-compatible Gate 1 contract; **not an authorisation to bulk-edit canonical Incidents**.

## Governing rule

**A canonical VIGIL Incident is a current evidence-and-assessment record, not a cumulative AI work diary.** Maintain the complete, attributable `interpretive_provenance.current_ai_review` in every Incident, with the original recorded reviewer platform/model, review date/scope, capability limitations and bounded review outcome. Preserve `human_governance_editor`, `operating_model`, `historical_reviewer_note` when present, accurately and without falsely implying human source verification or substantive approval.

Keep all current substantive `source_records`, factual chronology, `vigil_assessment`, source-clause/episode dispositions, material negative findings and exclusions, supported taxonomy-class mappings with occurrence-specific reasons, unresolved Boundary reasoning, HIM assessments, EXTREQ assessments, uncertainty and external-relationship evidence. **No source, accepted finding, classification polarity, review authority or current limitation can be removed merely to reduce file size.**

**New canonical files must not create an accumulated full `review_history`.** Routine bulk taxonomy re-adjudications, unchanged-outcome confirmations, validator repairs, reviewer capability checklists, reconciliation worklists and temporary process notes belong in time-bounded working review artefacts, Git commits/PRs, and maintained methods where adopted, **not appended to canonical historical-review arrays**. Do not manufacture one new review-history object per mechanical maintenance action. Replace `current_ai_review` only when a new, genuine current review is completed, preserving original authorship claims and accuracy.

## Accepted formats

- **Preferred:** full valid `current_ai_review`, with `review_history` absent.
- **Legacy transition:** existing nonempty `review_history[]` is still accepted; every retained historical object must remain individually valid and the current review must resolve to it. Do not append new routine process history merely because the legacy field exists.
- The abandoned `review_history_index` and `review_archive_batches` archive scheme is **not** part of this contract and is invalid.

The canonical schema, main Incident validator, interpretive provenance validator and authoring template must agree. Failures of current reviewer identity, required full current review fields, date chronology, existing human-editor truthfulness or retained legacy history remain real failures; removing history never exempts a current review from provenance validation.

## Historic record availability and cleanup

Git history and the verified **`v1.0.0` release tag** retain a prior release snapshot of VIGIL. They are recovery aids, not a new shadow database and not proof of immutable long-term archival guarantees. A review after the tagged release may exist only in later Git commits; do not assume the tag alone preserves every subsequent review. No review-index ledger, protected archive branch, new GitHub App or permanent `docs/reviews` collection is needed for the approved *routine process-history cleanup*.

The active `vigil/docs/reviews/` tree remains a temporary notice board under `REVIEW-RECORD-RETENTION.md`. Retire completed duplicated material only after checking current live references and preserved substantive decisions. Do not delete still-active work packets or reviewed external requirement evidence needed by maintained controls.

## Change authority and stop conditions

Gate 1 approves the **schema/validator/authoring contract** and isolated regression tests only. No existing canonical Incident is edited under Gate 1. A separately approved Gate 2 cleanup may remove superseded **in-record historical AI review entries**, provided that a source-first or mechanically verifiable review of affected fields confirms every substantive current record field is untouched and no distinct human approval, current limitation or missing decisive fact is lost.

Before any broad rewrite: inventory exactly which Incidents would change and how much size they save; show representative before/after output and all semantic/provenance exceptions; run full CI, built-output and website checks; reconcile per-Incident version candidates against published `main` under #175. Then stop for maintainer approval. Repeated edits to unrelated evidence/taxonomy/HIM/EXTREQ fields or blanket version resets are not authorised.
