# Interpretive provenance storage — Gate 1 opt-in contract

**Approved 28 October 2026, issue #168.** Initial implementation in draft PR #180. The approval authorises opt-in schema/validator support and lossless fixtures; **no canonical Incident migration or deletion is authorised**. Current VIGIL Incident evidence and adjudication, including every retained mixed-role taxonomy mapping and Boundary, are outside this storage change.

## Governing separation

A canonical Incident must remain independently interpretable: retain its current complete `interpretive_provenance.current_ai_review`, existing `human_governance_editor` (where established), `operating_model`, `historical_reviewer_note`, source records, material findings and every necessary uncertainty. Superseded complete reviewer packets may move out of the *active JSON* only when all their full content remains independently verifiable and recoverable.

`vigil/docs/reviews/` remains a **temporary working notice board**, not a historical provenance archive. Do not treat an audit packet reference or unprotected feature branch as immutable storage. A Git source commit, path and blob SHA are source integrity anchors; a named retention ref establishes **present reachability** but **does not prove future permanence**.

## Two supported representations

- **Legacy (default, unchanged):** nonempty full `review_history[]` with the full current review represented in that history and separately as `current_ai_review`. All existing Incidents remain valid without backfill.
- **Compact (strict opt-in):** full `current_ai_review`; nonempty `review_history_index[]` containing the original review ID, type, platform, model, date, SHA-256 of each **full source object**, and archive-batch ID for every *historical* review (null for the current one). `review_archive_batches[]` links each historical review to an original full JSON object inside an exact Git source commit/path/blob, with covered review IDs and a named retention ref. The old full `review_history` must be absent. A historical review can be covered by exactly one archive batch.

The index must retain all historical and current review identities in chronological order, with the current full review last. Never invent a reviewer model or human verification. Unknown original author/model values remain as recorded, including any existing limitations.

The verifier uses SHA-256 over UTF-8 JSON with sorted dictionary keys, compact separators and no lossy transformation, so fields such as scope, capabilities, limitations and outcome are all included in the full-object integrity check. It rejects wrong content, IDs, dates, batches, blobs, missing Git objects, inaccessible retention refs and contradictory simultaneous representations. A later review must preserve an archival batch pin of the previous `current_ai_review` before replacing it, while keeping all earlier batches discoverable.

### Archive verifier

`vigil/scripts/incident_provenance_archive.py` is the common verifier for both canonical validation paths:

- `vigil/scripts/validate-vigil-records.py`
- `vigil/scripts/validate-vigil-interpretive-provenance.py`

**Do not use `verify_git=False` for canonical acceptance**: that parameter is structural diagnostics only. Both governing validators call strict verification. Retention refs must be validated against an independent repository retention policy before a *live* compact Incident is accepted for publication. The code presently verifies current Git ancestry and object identity; it does **not** certify that a ref is protected from future deletion or rewriting. Do not claim it does.

## Read-only measured pilot, baseline

Five Incidents `034`, `062`, `101`, `145`, `195`; versions `1.1.23`, `1.1.21`, `0.1.24`, `0.1.16`, `0.1.4`. Each complete full history remains in its original Git blob. Distinct review counts **24 + 21 + 22 + 15 + 6 = 88**. All five current full reviews are duplicated in their histories. The original SHA-1 Git blobs from the 28 October prior read-only pilot are still identical at the versioning PR #178 merge commit and on the new Gate 1 branch.

The earlier in-memory 22.9% potential reduction is an estimate for one index+Git shape, not a prediction of the full verified storage contract or an authorisation to migrate records.

## Exit conditions and independent Gate 2

Before altering five actual canonical records, report and independently approve:

1. Immutable, durable archival retention **beyond a moving branch ref**; prove original full review objects survive branch retirement, squash/rebase and non-shallow retrieval, or return for a governed immutable-ledger decision. Existing temporary notice boards are not an acceptable fallback.
2. A five-case controlled in-memory migration where each of the **88 complete** review objects is reconstructed and hashed from pinned Git source, with a review-date/author/supersession ledger and positive/negative fixture tests for future reviews.
3. Exact before/after diffs showing unchanged case facts, clauses, sources, every adjudicated FC outcome, Boundary, HIM, EXTREQ, current interpretation and remaining provenance, plus public authorship-render parity.
4. Actual byte savings and versioning consequences, respecting `record_identity.version` and #175; no silent restamping of already staged historical versions.
5. Explicit human-maintainer **Gate 2** approval for the five named Incidents, separate from the Gate 1 rule implementation. A larger population requires its own approval.

Git migration must **fail closed** if any full review is not recoverable, chronology or reviewer identity differs, or a current accepted finding relies on content removed from the active Incident. No auto deletion and no coercion of reviewer types or identities.
