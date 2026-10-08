# VIGIL corpus-wide evidence fidelity — second pass

**Date:** 2026-10-08
**Branch:** `agent/incident-ecosystem-ingestion`
**Frozen canonical baseline:** `d845b4b31af8a7416f0df9c1a77a06073f7afc51`
**Status:** Frozen 179-Incident structural inventory completed; 13 bounded source-first canonical repairs (Phase 1 plus three Phase 3 tranches), five previous pilot-only cases, one preliminary source spotcheck, and 160 awaiting source-first review. Opt-in episode/EXTREQ contract and deterministic public index refresh are operational. Neither evidence exhaustiveness nor independent human verification has been certified.

## Immutable baseline and coverage semantics

Twelve `inventory-NN.json` files cover 179 unique canonical active Incidents. `inventory-summary.json` cross-checks counts and flags. They preserve canonical blob SHAs, source URLs and relevant source-clause/EXTREQ metrics without repeating or changing canonical facts. They are *triage*, not human adjudication. At this snapshot there are 130 `complete` and 49 `partial` recorded-clause taxonomy coverage statuses. No such status independently demonstrates source exhaustiveness.

The earlier bounded pilot covers INC-001, 023, 024, 065, 088 and 112 and remains provisionally reconciled for its documented scope. Its four outstanding classes of limitation are still open: source-exhaustiveness, per-clause lineage, residual INC-088 class/evidence review and exact generated-output parity.

Eight preliminary source-first case reviews are recorded for INC-003, INC-084, INC-129, INC-130, INC-138, INC-141, INC-151 and INC-177. INC-003 had its concealment clause repaired before the bounded six-Incident pilot. The bounded pilot case INC-088 has a supplemental source-reading manifest. These are evidence-review notes only; no Incident record changed in this tranche. Of 179 records, six retain the bounded-pilot status, eight have a new primary-source spot-check, and 165 still await source-first review.

## Two separate completion axes

1. **Recorded-clause taxonomy adjudication** — `complete` only when each recorded material clause is `mapped` or `resolved-no-mapping`; `partial` when any clause is unresolved or a taxonomy gap.
2. **Evidence-fidelity review** — separately records the extent of primary/firsthand evidence read, proposed material event inventory, provenance per event, relative/concurrent timing, original-clause dispositions, classification admission/roles and independently reconciled EXTREQ pointers. A review cannot be marked complete merely because a taxonomy status is complete or a validator passes.

An AI-authored review never becomes human-verified merely by committing its manifest.

## Source-first review procedure for each tranche

A. Freeze the old Incident blob SHA, current projections and source set. Capture a source-specific evidence ledger with inspected URLs, date of retrieval, access failures and later corrections.

B. Read the best available primary and affected-party evidence. Enumerate discrete material actions, system/actor decisions, external effects, control actions, response actions and evidence limitations. Record provenance and actual or *unknown* timing. Separate multiple runs and concurrent branches; do not fabricate one linear event sequence.

C. For every baseline clause, record `retain`, `merge-supported-duplicate`, `split-supported-episode`, `context-only`, `reorder` or `unresolved`, with evidence. A single episode may support multiple distinct class relationships without becoming duplicate events. Material missing source propositions must be added or explicitly left pending, never silently discarded.

D. Reconsider full taxonomy recognition only where evidence materially changes, preserving successful, failed and ambiguous boundaries. The prior mapping set remains unchanged until substantive review is authorised. Confirm the potential FC-084 relationship where verification is handed off across authority chains without independent revalidation.

E. Review independent EXTREQ applicability and result separately. Before changing source-clause indexes, demonstrate old episode -> new episode link *per assessment row*; do not blindly reindex by array position.

F. Preserve and separately review HIM/harm assessment, summary, factual basis, Discussion, and Conclusion. Rebuild three derived public indexes using the repository builder, examine Case File Stage 02 and Stage 04 projections and source trail, and commit review manifests. Do not silently shorten occurrence narratives.

G. Run existing validators and retained-subsystem tests in a repository-capable worktree; record commands, dates, results and any unavailable verification. Treat all source interpretations and source exhaustiveness as human-reviewed dispositions, not validator-derived truth.

## Priorities and bounded stop points

- **Earlier repair follow-up:** INC-003 now has confirmed existing concealment capture but still needs per-clause lineage. **Pilot follow-up:** INC-088's first-hand research source confirms attempted XSS with no observed successful script execution, plus impersonation of site moderators/admins, neither independently modelled as a current material source clause. These require controlled class-recognition review; generated index exact parity remains unverified.
- **First tranche:** INC-084 (omitted production-record modification and temporal ordering), INC-141 (collision before later reporting), INC-151 (source-description-as-clause and loss attribution), INC-177 (multiple phases compressed; timing/retrospective finding). Preliminary case files committed; exact canonical repair manifests remain the next step.
- **Second source-first follow-up:** INC-129 has one compaction persona block parsed into many clause fragments; INC-130 and INC-138 each split one compaction summary into two proposition-oriented clauses. Supplemental candidate manifests have been committed for all three. Preserve distinct classification rationale without multiplying the number of events. **Next tranche:** prepare exact old/new canonical episode crosswalks for the reviewed cases, then prioritise further high-harm and multi-source incidents from the 166 unreviewed entries. Queue is provisional; inventory flags alone are not evidence findings.
- **Systemic controls:** Human approval for bounded Phase 1 and the opt-in Phase 2 was supplied on 2026-10-08. `source_episode_validation.py`, `occurrence_requirement_validation.py`, `validate-vigil-records.py`, `VIGIL.Schema.json`, regression tests and the VIGIL records CI workflow now enforce the opt-in episode contract while retaining legacy acceptance. No mandatory whole-corpus migration, automatic duplicate classification or source-exhaustiveness assertion is authorised. Generated outputs were refreshed by the deterministic builder after enabling push validation on the canonical ingestion branch.

**Mandatory review stop:** this approved opt-in control applies only to migrated records. After testing, report exact failing legacy records (if any) before proposing broad migration; obtain separate approval before any further mass canonical repair. For any incident with disputed source meaning, stop that Incident rather than force a tidy clause list.

## Phase 3 checkpoint — 8 October 2026

Five additional bounded canonical Incidents were source-first reconciled in `PHASE3-TRANCHE-01.md`, with corresponding per-case manifests and crosswalks. Across this tranche, 51 indexed external-requirement assessment rows were linked to reviewed stable episodes without changing their independent alignment findings. One evidence-attribution issue justified reopening the financial-economic HIM dimension of INC-151 (S3 → unreported while reputation/dignity and overall remain S3). INC-088 now has two unresolved material source episodes and therefore partial rather than complete recorded-clause adjudication. The remaining candidate records are ordered for follow-up in `PHASE3-TRANCHE-02-QUEUE.json`; that queue is structural prioritisation, not a review finding. The catalogue dispatch is gated to actual `main` pushes so unmerged ingestion work does not trigger website synchronisation; the old dispatch credential produced a 401 and may require renewal before future `main` dispatch.

## Phase 3 tranche 2 checkpoint — 8 October 2026

Three additional canonical repairs (INC-085/086/150) and their old/new episode and EXTREQ row crosswalks are recorded in `PHASE3-TRANCHE-02.md` and `INC-XXXXXX-phase3-tranche02-repair-manifest.json` files. Forty-six position-based EXTREQ rows now resolve to stable episode identities without changing independent assessment results. Three higher-risk cases (INC-171/064/060) were examined for source issues but remain unchanged and not certified; the case-specific source and harm issues are enumerated in the tranche report. The VIGIL records validation suite returned green after the INC-085 public-prose correction. A concurrent unrelated INC-032 change was preserved. The remaining 162 awaiting cases are not to be bulk-migrated from structural scores.

## Phase 3 third-tranche checkpoint — 8 October 2026

Two more canonically repaired cases (INC-060, INC-159) have explicit original-to-repaired source-episode crosswalks and 22 class-derived external-governance assessment rows re-linked by stable episode. See `PHASE3-TRANCHE-03.md` and the per-case manifests. INC-171, 064 and 174 remain held for source-first/harm-attribution or classification-recognition review; only read-only findings were recorded in `PHASE3-TRANCHE-03-HELD-EVIDENCE.md`. The corpus census is 13 repaired, five prior pilot-only, one source spotcheck and 160 awaiting. No bulk migration or mechanical re-adjudication is authorised.
