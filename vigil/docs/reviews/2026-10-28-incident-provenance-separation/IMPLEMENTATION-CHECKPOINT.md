# Issue #168 — Gate 1 provenance implementation checkpoint

**Date:** 28 October 2026  
**Draft PR:** [#180](https://github.com/CAM-Initiative/Vigil/pull/180), base `agent/incident-ecosystem-ingestion`, **NOT main**, unmerged.  
**Source baseline:** `a63e3582f82b58954997cf69d5af9d29acb31c35`, the verified merge commit of versioning PR #178.  
**Authority:** Gate 1 approval for opt-in provenance schema, validator and isolated tests. **No Gate 2 approval for any canonical file migration.**

## Implemented controls

1. `vigil/VIGIL.Schema.json`: two mutually exclusive provenance storage modes. Legacy nonempty full `review_history` remains valid for every current Incident. Compact mode requires the full `current_ai_review`, complete `review_history_index` with full-object SHA-256 and original reviewer identity, and Git-anchored full-history archive batches. Existing optional current provenance fields remain unchanged.
2. `vigil/scripts/incident_provenance_archive.py`: fail-closed on duplicate/missing identities, mismatched current review/full-object hashes, unsupported or absent Git source commits/blobs, archived review missing from its pinned source, differing historical reviewer/date/content, future-review chronology, conflicting dual shapes, unresolvable named retention refs and unverified coverage. Existing original `null` reviewer platform/model values must remain unknown, never guessed. Supports repeated compact-review successor snapshots.
3. Both `validate-vigil-records.py` and `validate-vigil-interpretive-provenance.py` run strict compact verification when either new compact field is present. Otherwise their legacy validation behaviour remains in place. `verify_git=False` is a structural diagnostic only, never used for canonical acceptance.
4. `vigil/tests/test_compact_interpretive_provenance.py`: **23 new synthetic Git fixtures**, including a valid compact case, corrupted original digests, wrong Git blobs/commits, missing/unreachable retention refs, mixed modes, duplicate/missing review IDs, forged human attribution, unknown model identity preserved as `null`, and two subsequent full review versions.
5. `vigil/docs/maintenance/INCIDENT-INTERPRETIVE-PROVENANCE-STORAGE.md`: approved Gate 1 opt-in authoring/retention contract; separate Gate 2 prerequisites before live migration.

No canonical Incidents, source evidence, taxonomy/HIM/EXTREQ decisions, public-record builder, case-file renderer or live version stamps have been altered by this implementation.

## Actual GitHub Actions results

**[Full VIGIL records run #40687910569](https://github.com/CAM-Initiative/Vigil/actions/runs/40687910569): SUCCESS.** Complete unittest discovery: **391 tests passed**, including 23 new compact archive tests. All 206 legacy canonical Incidents passed existing record and interpretive provenance validation. The records workflow also passed the deterministic index/build freshness checks. The separate pathless Incident publication gate passed on the same review branch.

**One-off read-only five-Incident audit:** executed successfully in that same Actions run before retiring its temporary step from the workflow. Script: `vigil/docs/reviews/2026-10-28-incident-provenance-separation/simulate_read_only.py`. The source of every complete historical review is the exact Git blob at `a63e3582f82b58954997cf69d5af9d29acb31c35`, independently checked against all five unchanged canonical records. **All 88 full review objects reconstructed**, including all reviewer attribution, dates, scopes, capability profiles, limitations, outcomes and SHA-256 content. The simulation changed only the in-memory provenance history representation; all other canonical case fields and current provenance remained identical.

| Pilot Incident | Embedded reviews | Original bytes | Simulated compact bytes | Reduction bytes |
| --- | ---: | ---: | ---: | ---: |
| 034 | 24 | 101,175 | 81,863 | 19,312 |
| 062 | 21 | 112,430 | 95,342 | 17,088 |
| 101 | 22 | 76,918 | 58,114 | 18,804 |
| 145 | 15 | 65,949 | 52,565 | 13,384 |
| 195 | 6 | 58,842 | 53,477 | 5,365 |
| **Total** | **88** | **415,314** | **341,361** | **73,953** |

**Measured in-memory reduction: 17.81%.** This corrects the preliminary **22.9%** estimate by including per-review digests and explicit archive metadata. No actual disk writes to the canonical source set were made. This is a pilot result, **not** a corpus-wide storage saving forecast.

After obtaining the one-off evidence, the temporary workflow step was **removed**. Production workflows must not depend on a dated `docs/reviews` notice board script. The script is retained only as a temporary review artefact for the active work package, subject to ordinary notice-board closeout.

## Gate 2 blocker: retention durability is not yet established

The successful checks prove **current integrity and current Git reachability**, not permanent availability of an archival commit after source branches are deleted, squash-merged, or garbage-collected. `agent/incident-ecosystem-ingestion` is currently not an independently protected immutable archive ref, and the present helper cannot verify that GitHub protects a remote tag or branch from future deletion. **Do not migrate any canonical review history against an unprotected moving ref.**

Before requesting Gate 2, choose and verify a durable historical anchor—for example a specifically protected archival tag/branch with appropriate delete/update restrictions and documented retention, or a separately approved immutable external review ledger if protected Git retention cannot meet reproducibility requirements. Future snapshots must be pinned before a current review is superseded, with no reliance on transient feature-only commits.

Then independently verify the complete history of all five real files through the protected anchor, all other current substantive Incident fields, website/public authorship parity, and any approved per-record PATCH publication effects. **STOP for separate human approval before altering five pilot canonical Incidents**. Any 206-record migration would require its own later authority.

## Current branch boundaries

This PR does **not** implement #176 challenged no-mapping workflow, #179 publication-publisher migration, or #133 source-first taxonomy-gap remediation. No opening of a new permanent review-history database under `docs/reviews`. The original versioning architecture #175 remains intact.
