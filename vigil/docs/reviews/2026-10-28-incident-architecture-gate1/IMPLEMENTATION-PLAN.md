# Implementation and assurance plan — contingent on Gate 1 approval

**28 October 2026.** This plan sequences work for issues [#168](https://github.com/CAM-Initiative/Vigil/issues/168), [#175](https://github.com/CAM-Initiative/Vigil/issues/175), [#176](https://github.com/CAM-Initiative/Vigil/issues/176) and master [#133](https://github.com/CAM-Initiative/Vigil/issues/133). It is a design specification, **not authorisation to implement** a schema, validator, builder or records migration.

**Branch:** `work/incident-architecture-gate1-20261028`; parent commit from `agent/incident-ecosystem-ingestion`: `0f008d983da72db962705fb9c732496e703cdb5e`.  
**Authority:** `vigil/MAINTAINERS.md` Gate 1 semantic control, Gate 2 corpus repair; source-first Incident workflow and temporary review notice-board policy.  
**Frozen evidence:** [SIZE-PILOT.json](SIZE-PILOT.json), [GATE1-DECISION.md](GATE1-DECISION.md), [full-corpus audit](https://github.com/CAM-Initiative/Vigil/blob/work/full-corpus-taxonomy-gap-audit-20261028/vigil/docs/reviews/2026-10-28-full-corpus-taxonomy-gap-audit/README.md).

## Phase 0 — completed read-only discovery and checkpoint

- [x] Create a **new branch from ingestion** rather than `main`; do not reset or rewrite the ingestion branch.
- [x] Read current Incident provenance validators, canonical schema, maintainer controls, records and taxonomy publication workflows, temporary review-retention policy.
- [x] Inspect five existing canonical records by exact version, Git blob SHA and historic review size; 415,314 source bytes; 88 embedded review-history objects.
- [x] Test *in memory only* a suggested compact index and original Git history anchor, verify every other top-level field and full current review unchanged, with 22.9% illustrative size reduction. This **does not** prove all historical review reconstruction, public render compatibility or schema validity.
- [x] Write proposed current/new control contract, pass/fail examples, impact scope, risks and stop conditions.

**Checkpoint:** design files committed on this branch only. No source record, schema, validator, builder, CI workflow, publication or taxonomy changes.

## Phase 1 — human Gate 1 decision (blocked pending approval)

**Decision owner:** human maintainer. Independently accept/reject/amend decisions **A–F** in [GATE1-DECISION.md](GATE1-DECISION.md#7-human-gate-1-decision-request).

**Required before semantic controls change:**
- Exact approved legacy/compact provenance shapes, archive source and recoverability requirements.
- Exact changed-payload definition and conflict handling for per-Incident version bump; note the ingestion→main two-stage pipeline.
- Exact review-challenge scope and public visibility/retirement requirement.
- New passing/failing examples for all three.
- Read-only impact inventory beyond five size-pilot records.
- Explicit stop condition after validators change and before any multi-record edits.

**Do not** construe approval to create the working branch or design files as permission for Gate 1 implementation.

## Phase 2 — isolated fixtures and contract implementation (after Gate 1 only)

**Preferred implementation order:** versioning contract first; provenance shape second; review-challenge field last. Separate reviewable commits/PRs and run existing validators at each boundary. Coordinate changes to `vigil/VIGIL.Schema.json`, `vigil/scripts/validate-vigil-records.py`, `vigil/scripts/validate-vigil-interpretive-provenance.py`, `vigil/scripts/build-vigil-public-records.py`, `.github/workflows/vigil-records.yml`, taxonomy-publications workflow and website only as specifically approved.

### A. Versioned publication contract test matrix

| Fixture | Proposed expected result |
| --- | --- |
| No canonical Incident content changed; only audit/review docs changed | No Incident version bump; PR valid |
| One Incident `0.1.16` content changed, single final main PR | Candidate `0.1.17`; accepted only if main still publishes `0.1.16` and content baseline reconciles |
| INC034 `1.1.23` and INC145 `0.1.16` both modified | Independent proposed `1.1.24` / `0.1.17`; no global corpus version |
| Same source Incident changed in three commits or several work PRs merged only into ingestion | One next-patch *published* version at final main integration, not three |
| Two final PRs prepared from same main baseline; first merges and changes same Incident | Second fails freshness and requires rebase/source-first reconciliation and version recomputation |
| Unchanged Incident version incremented without substantive payload change | Reject gratuitous bump |
| Changed Incident keeps old version | Reject missing published revision |
| Future taxonomy edition published with no Incident change | Do not patch untouched Incident; taxonomy authority remains independent |
| Bot-generated public index/manifest update only | Do not edit canonical source or increment any Incident |
| Merge source input commit already published but workflow reruns | Idempotent manifest/index build; no second revision |
| Merge manifest includes own generated output SHA circularly | Reject design; use a stable canonical source snapshot/input commit |

**CLI/workflow design requirements:** select exact target published `main` ref, identify changed canonical paths, compare semantic payload excluding explicitly publication-only stamp fields, parse each existing per-record version, require one candidate, report added/removed/changing IDs, and detect a changed-main conflict. Make computed candidate explicit for review. Final main-only generated manifest records actual content hash and stable source input commit. Tests must not have write access to existing canonical source records except an **explicit approved preparation command** run during final integration PR authoring.

### B. Provenance storage tests

| Fixture | Proposed expected result |
| --- | --- |
| Legacy record containing full current review in non-empty history | Continue to pass until individually migrated |
| Migrated record retains current full review, full index and reconstructable original history | Pass new contract only after independent reconstruction and model/date checks |
| Index loses any old `review_id` | Fail |
| Index reports a different reviewer/platform than source historical object | Fail |
| Archive commit exists but path/blob mismatch | Fail |
| Archive cannot be fetched/reconstructed in the declared support environment | Block migration or meet approved offline archive requirement |
| New AI review is only recorded in PR thread but not publication state | Fail until it has a durable, attributable current/archived home |
| A human editor is inferred from an AI reviewer | Fail; preserve actual authority and AI authorship disclosure |
| Historic review is a pre-squash, branch-only object not pinned to reachable Git history | Block migration, explicitly preserve historic bytes before squash |
| Current `boundary_adjudication` or exclusion rationale disappears after compaction | Fail semantic-preservation comparison |
| Public Stage 02 review transparency or canonical traceability becomes empty | Fail public rendering parity |

**Five-record pilot after Gate 2:** Compare source `source_records`, all `vigil_assessment`, `taxonomy_classification`, `harm_impact_assessment`, `external_requirement_assessments`, `affected_party_context`, `system_context`, `jurisdictional_context`, `related_incidents`, `incident_artefacts`, `summary` and other governed fields byte/semantic-equivalent except exact approved provenance/revision fields. Reconstruct all **88** prior complete review objects and compare content hash/order/IDs. Verify source object provenance, human review claims, old Git history, generated outputs and public readability. Measure exact before/after sizes. If any check fails, **do not treat compacted records as migrated**.

**Pilot source anchors, frozen:** `INC034` blob `ea1b4c179ca9e0d7111e0831f495e420efd18130`; `INC062` `acc8420187e1c3d1cd8588558b2cf04db5e1ef2b`; `INC101` `22446d77c70f34a5b57a6d1e17f18d6ac4e81b7b`; `INC145` `12b524bd6cb1aca23bac028e16e3f0c855405839`; `INC195` `0ae3818650c8e090ef138dc96bcb22e6aa4d5997`.

### C. Review-challenge status tests

| Fixture | Proposed expected result |
| --- | --- |
| Frozen `resolved-no-mapping` clause, exact episode/source identity, one audit challenge | Preserve existing disposition; mark separately as *under re-adjudication* |
| Same clause has evidence requirement but no confirmed class fit | Evidence-review posture, not automatic taxonomy-gap or Boundary |
| Audit source pointer references altered or missing clause | Fail identity join; require manual source-first reconciliation |
| Duplicate challenge ID or a challenge connected to wrong Incident | Fail |
| Approved independent review confirms original no-mapping was sound | Close challenge as retained; preserve source-specific reason |
| Supported existing-class success/failure later established | Only accepted taxonomy adjudication changes canonical mapping; close challenge and reconcile episode/top-level and EXTREQ |
| Completed evidence-limited review cannot resolve decisive criterion | Express explicit evidence-limited non-admission separately from a review never performed |
| Simulated version of public website silently describes audit recommendation as an approved mapping | Fail |
| Open challenge tries to redefine `adjudication_coverage` structural completeness | Fail; review challenge is orthogonal |

## Phase 3 — human Gate 2 and controlled sample migration

**Stop again after new control validators run read-only against entire current corpus.** Report: every newly failing record+field, unchanged valid legacy records, exact source/main versions and generated index impact. Obtain separately recorded **Gate 2 authorisation** for:
1. migration of the five historical-review pilot records only; and
2. any flagging of 230 challenged source clauses across approximately 137 records.

Do not combine these two Gate 2 permissions implicitly. Both use small commits and exact pre/post preservation manifests; no unrelated HIM, external assessment or taxonomy changes.

## Phase 4 — substantive remediation and publication

Under [#133](https://github.com/CAM-Initiative/Vigil/issues/133), after enabling architecture has passed its separate approval/QA:
1. source-extraction audit and pilot [#177](https://github.com/CAM-Initiative/Vigil/issues/177), checking omitted source propositions before class fit;
2. independently adjudicate an initial 5–10-case sample, including bounded safeguards and counterexamples; compare to current v0.9.0 criteria **before** viewing prior recommendations;
3. process remaining 115 existing-class reconsiderations in small versioned batches with reciprocal FC↔episode↔EXTREQ checks; preserve independent harm conclusions;
4. investigate the 115 evidence recommendations with explicit recoverable/irrecoverable/finished-research distinctions;
5. adjudicate the three taxonomy clarification questions and two conditional gap candidates through the **separate taxonomy-governance branch**;
6. independently sample the 446 retained no-mapping findings and verify public website reading, archive recovery and canonical-to-published projections.

Each substantive accepted change must be versioned on main, with a complete audit trail and stable source identity. No classification is promoted solely to clear a challenge counter.

## Phase 5 — exit, rollback and notice-board retirement

- Confirm all accepted changes have a current authoritative home; original source and criterion-level historical decisions can be recovered via immutable commits, without private undisclosed references.
- Check zero broken review references, external-governance reviewed relationships and runtime dependencies on soon-retired `docs/reviews` paths.
- Run records full suite, source provenance, interpretive provenance, taxonomy relevant tests, generated index reproducibility, EXTREQ reciprocal checks and public projection tests at the **actual final main integration**. Connector-only read/write is not proof of successful local tests.
- Record current main published Incident version+SHA manifest, source SHA, tests, approvals, exceptions and recovery path in PR.
- Only then promote accepted general method to `vigil/docs/maintenance/`, remove temporary review packets from active tree under `REVIEW-RECORD-RETENTION.md`, and retain exact pre-deletion recovery commit.
- Rollback is **another explicit governed published correction** or rejected PR, not force-resetting main, squashing away provenance or silently decrementing released version numbers.

## Work to request next

1. Human maintainer answers the independent Gate 1 decisions A–F.
2. Once approved, implement only the approved **isolated fixture tests and control logic** on this architecture branch (or a separately approved child branch), in small commits.
3. Measure actual corpus pass/fail deltas, then **stop for Gate 2** before canonical file migration.
4. Start five-record pilot. Begin 230-clause flagging only after the challenge-state and public presentation contract have passed review.
