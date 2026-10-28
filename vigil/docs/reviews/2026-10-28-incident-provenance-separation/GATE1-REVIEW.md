# VIGIL — Interpretive provenance separation: Gate 1 decision

**Date:** 28 October 2026  
**Tracking:** [#168](https://github.com/CAM-Initiative/Vigil/issues/168)  
**New working branch:** `work/incident-provenance-separation-gate1-20261028`, derived from **ingestion commit `a63e3582f82b58954997cf69d5af9d29acb31c35`** (merged [PR #178](https://github.com/CAM-Initiative/Vigil/pull/178)). **Do not target `main` directly.**  
**Status:** **Gate 1 proposal ONLY — no authorisation yet for semantic schema/validator/test changes or canonical migration.**

## Decision requested

**Approve an opt-in, backward-compatible compact interpretive-provenance contract**, allowing explicitly migrated Incident files to retain their entire current `current_ai_review`, current substantive case adjudications, and a **complete, verifiable compact index of past reviews**, rather than indefinitely embedding full past `interpretive_provenance.review_history[]` objects inside the active Incident.

Prefer **immutable Git-pinned archive batches**, **only if retrieval, object longevity, integrity and future review append can be demonstrated**. If those guarantees fail, return for a distinct decision on a governed, immutable review ledger **outside** temporary `vigil/docs/reviews/`; never silently discard history.

**Approval sought for** scoped schema/validators/permanent tests and five-record *non-destructive fixture* implementation with read-only corpus diagnostics. **Not sought:** approval to change five canonical records, run any bulk migration, delete old review material, alter classification, restamp versions, or change public rendering. Those require a separate Gate 2/other specific authorisation.

## Actual inspected baseline

Live `agent/incident-ecosystem-ingestion` at the merged PR #178 commit:

| Pilot Incident | Current version | Complete embedded review objects | Review full current copy also in history? |
| --- | --- | ---: | --- |
| VIGIL-INC-000034 | 1.1.23 | 24 | Yes |
| VIGIL-INC-000062 | 1.1.21 | 21 | Yes |
| VIGIL-INC-000101 | 0.1.24 | 22 | Yes |
| VIGIL-INC-000145 | 0.1.16 | 15 | Yes |
| VIGIL-INC-000195 | 0.1.4 | 6 | Yes |

**88 historical review objects** in five records; review IDs are distinct in each inspected history; `current_ai_review` is duplicated in each history (once). The initial 28 October read-only simulation measured **415,314 bytes** of case files; a hypothetical index plus Git anchor was **320,108 bytes (22.9% smaller)**. This was not a schema change or a proven archival migration; additional integrity metadata may lower that saving. Source: `vigil/docs/reviews/2026-10-28-incident-architecture-gate1/SIZE-PILOT.json`. The 5 current record blobs match the baseline blob SHAs in that report. The source bytes presented by the GitHub API vary in formatting/representation; use an exact committed-byte baseline when measuring final changes.

Current `vigil/VIGIL.Schema.json` has `interpretive_provenance_rules.required_fields` including `review_history` and `current_ai_review`; current `validate-vigil-records.py` insists on a nonempty full history, required reviewer fields and `current_ai_review.review_id` in that history. `validate-vigil-interpretive-provenance.py` repeats those checks and validates review-date chronology. The full object has fields including reviewer type/platform/model, review date/scope, capability profile, known limitations and outcome. Some records also have `operating_model`, `human_governance_editor`, `historical_reviewer_note`; preserve all existing optional fields and their semantics.

`vigil/docs/maintenance/REVIEW-RECORD-RETENTION.md` makes `docs/reviews/` a temporary notice board, **not** a durable archive. Current current-state Incident evidence and canonical accepted interpretations must remain in the Incident. Git/PR history currently owns prior versions/process chronology, but a bare commit hash does not establish permanent future reachability.

## Nine-part MAINTAINERS.md Gate 1 disclosure

### 1. Current behaviour

Every active Incident keeps full append-only `interpretive_provenance.review_history[]`, including the current AI review, along with a separate full `current_ai_review`. Both validators reject missing/empty history or a current review not present in it. No supported alternate compact form exists.

### 2. Proposed behaviour

Permit **exactly one of two explicit representation modes per Incident**:

- **Legacy (default):** existing `review_history[]` plus `current_ai_review` continues unchanged and valid for all unmigrated files.
- **Compact (opt-in):** full `current_ai_review` remains; `review_history_index[]` records *every* historical/current review identity, date, original reviewer type/platform/model (unknown stays unknown), a stable content digest and its retrieval location. `review_archive_batches[]` identifies retained immutable full-review sources by exact Git commit, canonical path and Git blob SHA, with covered review IDs and associated digests. The index entry for current review resolves to the complete active `current_ai_review`; previous full reviews resolve into verified frozen Git archives, **not** a short summary standing in for them. The existing `review_history[]` full-object field is absent in compact mode; do not allow contradictory simultaneous full and compact histories.

The concrete field names and object shape in this paragraph are **proposed**, not an already approved schema. A full contract must cover first migration *and successive new reviews*: at every replacement of `current_ai_review`, pin an immutable preceding committed snapshot containing the previous full current review; append an index entry with original date/identity/digest; keep earlier immutable anchors. A transient uncommitted review cannot disappear through a squash merge. Review identity, chronology, supersession and uncertainty are not implied by a new status. An AI reviewer is not a human authoriser.

**Important:** An arbitrary Git SHA is **not automatically durable**. The fixture and release design must prove each archive commit is fetchable, reaches the exact expected blob and survives repo cleanup/branch removal/squash. Prefer a protected permanent reachability reference or separately governed immutable archival store if normal branch history is insufficient. Do not create a permanently retained copy in `docs/reviews`. No broad deletion or archival tag mutation is authorised in this gate.

### 3. New pass/fail cases

**Newly passes in opt-in compact mode:** an otherwise valid record with full current review, all original indexed review IDs, positive identity/digest match to recoverable archival full objects and unbroken chronology.

**Newly fails in opt-in compact mode:** missing review ID; inconsistent reviewer/model/date; duplicate or missing index; current review not matching indexed identity/digest; archive object absent, invalid or moved; incorrect pinned blob/path; history gap across successive reviews; invented human approval; contradictory full and compact histories; index lacking a full historical retrieval target.

**Still passes without edits:** all existing legacy records, no matter how long their currently valid full `review_history` is. Nothing is auto-migrated or globally made invalid.

**Still fails:** existing genuine historical-provenance errors. No blanket skip of prior identity, chronology or authorship verification.

### 4. Affected surfaces

- Canonical: `interpretive_provenance.current_ai_review`, `review_history` (legacy), proposed `review_history_index` and `review_archive_batches`, and existing optional current provenance fields.
- Governing contract: `vigil/VIGIL.Schema.json` plus `vigil/docs/maintenance/REVIEW-RECORD-RETENTION.md`/a specific adopted opt-in provenance maintenance contract.
- Validators: `vigil/scripts/validate-vigil-records.py` and `vigil/scripts/validate-vigil-interpretive-provenance.py`, with structural schema validation and separate Git object/recovery/integrity checks.
- Generic isolated tests, authoring template and future builder/site authorship transparency **only if** needed and separately reviewed. No automatic change to Stage 01 narrative, classification, HIM, EXTREQ, or public prose.
- Git archival refs and commit/object retrieval (including full-history CI) for genuine provenance integrity. Current public renderer parity must be verified before any live pilot.

### 5. Expected corpus impact

**Five explicitly measured pilot Incidents:** 034, 062, 101, 145, 195, 88 historical review objects. Broader currently active 206-record ingestion corpus **not yet measured for migration**. A Gate 1 opt-in schema change should let all legacy records continue passing unchanged; pilot fixtures only until Gate 2.

### 6. Repair implication

Potential optional migration: extract redundant full history from canonical storage **only after** exact historical objects are proven reconstructible from durable pinned sources; replace with compact identity and digest index and keep the complete current review and optional current provenance. This will eventually require metadata changes to five pilot canonical records, a PATCH-or-higher published version assessment under #175, and generated-output checks; **none of those actions is approved in Gate 1**. Never rewrite chronology or change mappings, source clauses, harm, requirements or assertions to satisfy a storage target.

### 7. Data-loss and semantic-drift risks

A Git blob can exist temporarily then become unreachable; squash/garbage collection/shallow clones can break archives. Per-review context (scope, capability limitations, reasoning, review outcome) could be deleted or summarised away if a compact index points to the wrong source. Review dates could be fabricated. Model provenance could be misrepresented as human approval. Historical substantive decision reasons could disappear from current canonical state. Mitigations: immutable exact content digest, recover every historical object, verify identity/chronology, preserve all accepted current findings and limits, fail migration on any discrepancy, require durable reachability strategy, retain full legacy form when uncertain.

### 8. Why validator/schema enforcement?

The schema should express the two supported shapes and their required fields; structural validators should reject invalid/mixed identities and histories; the provenance validator (or a dedicated Git-aware verifier) must check full archive resolution, per-object digest, chronological continuity and current/historical authorship. The website renderer is not an archival integrity authority. Retention policy governs *where* old data can live; it cannot verify hash matches. Do not use brittle prose regexes or change canonical substantive fields to enforce size.

### 9. Stop condition and Gate 2

After explicit Gate 1 approval: implement schema and validator behaviour **on a work branch**, preserve unchanged 206-record legacy validity, run generic positive/negative fixture tests and do a read-only live-corpus and five-record preservation/recovery analysis. **STOP** and show exact before/after, archive refs, retrieved full reviewer objects, byte differences, QA/website parity, and failure report **before** changing any pilot or other canonical Incident. A five-record migration requires a **separate Gate 2 human approval**; larger population migration later requires its own governed authorisation. Never migrate on a blanket branch-wide script without evidence verification.

## Five-record pilot acceptance protocol

1. Pin the five existing Git blobs/commits/versions and snapshot source facts, chronology, clause episode identifiers, all classification roles (including Boundaries), HIM/EXTREQ, current reviewer identities and every full historical review object.
2. Build **in-memory proposed compact structures**, not canonical edits; validate both legacy and compact fixtures.
3. Recover **all 88** original review objects through immutable archive anchors; compare review IDs, reviewer type/platform/model, ISO date, scopes, limitations, review outcome and full content digest. Test missing blobs, wrong blobs, gaps, conflicting/repeated review IDs, future date and fabricated human approval.
4. Verify that a second subsequent review can be appended and the old full current review remains resolvable, without relying on a soon-deleted feature branch.
5. Preserve current substantive case interpretation byte-for-byte for the fixture; check public output, expected authorship and projections against unchanged baseline.
6. Report actual byte deltas; size reduction is secondary to full fidelity. Stop if source is not durable/recoverable.
7. Present exact schema/validator diff and Gate 1 test outcome; request Gate 2 separately for the five canonical files.

## Separate workstreams and exclusions

- [#175](https://github.com/CAM-Initiative/Vigil/issues/175) per-Incident published version control has been merged into ingestion in PR #178; coordinate future **approved** provenance PATCH candidates at eventual main release, not per preparation commit.
- [#176](https://github.com/CAM-Initiative/Vigil/issues/176) disputed `resolved-no-mapping` review posture is **not** equivalent to historical interpretive provenance and is not authorised here.
- [#179](https://github.com/CAM-Initiative/Vigil/issues/179) conversion of generated-output publishers for strict main rules remains separate.
- [#133](https://github.com/CAM-Initiative/Vigil/issues/133) 230 flagged source clauses/137 Incidents require independent source-first adjudication **after** this storage discipline; no automatic mapping or classification changes.
- Current classification and historical human-review authority are not inferred from an AI-authored review entry.

**Explicit decision requested:** Approve only the opt-in two-mode interpretive-provenance contract and associated governed controls/isolated non-destructive fixtures described above. If durability cannot be demonstrated with Git-pinned archives, STOP for a new ledger decision; this approval would not authorise that fallback.
