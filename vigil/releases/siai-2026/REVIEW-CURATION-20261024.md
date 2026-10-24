# VIGIL 1.0.0 — review retention cleanup (tranche 1)

**Date:** 24 October 2026. **Working PR:** #162. **Pre-deletion parent:** 408d2740504fe051a0446b894e2fa30d8f1a4b6f.
**This is housekeeping only.** No canonical Incident, taxonomy class, HIM, registered source, external requirement or release tag was changed; no semantic conclusion was promoted by deleting a report.

## Exact removed sets

| Files | Path criterion | Why retired |
| ---: | --- | --- |
| 88 | *.log under vigil/docs/reviews/ | Historic execution output; final decisions/validation summaries remain |
| 11 | All files under vigil/docs/reviews/2026-10-22-incident-context-gate2-pilot/ | Superseded proposed-only geography pilot; the accepted full-corpus migration and its 200 per-Incident reviews remain |
| 1 | vigil/docs/reviews/2026-10-19-boundary-diagnostic/census.json | Reproducible dated census output; scripts and per-Incident decisions remain |

**Total removed: 100 files, 2498473 bytes from the live tracked tree.** Their exact Git blobs are recoverable at the pinned parent above.

## Explicitly protected from this cull

- The full ongoing taxonomy v0.8.0 reconciliation directory, notably the SIAI case decisions, decision packets and live progress.
- The 200 source-bounded per-Incident context reviews under 2026-10-22-incident-context-migration, geography preservation inventory and canonical context.
- Current review_reference targets, individual taxonomy/HIM positive and negative criterion adjudications, source-admission evidence, approved maintainer decisions, and the FC-089 to FC-084 prepublication identity crosswalk.
- Other large inventories and interim case files where a full exact-reference / uniqueness check has not established safe removal.

## Before release

Check live path references with the existing retention auditor, re-run VIGIL CI, complete the still-active v0.8.0 campaign, and regenerate the scientific checksum from the actual approved main commit after merge. A passing test does not authenticate sources or mean independent adjudication is complete. New working outputs follow vigil/docs/maintenance/REVIEW-RECORD-RETENTION.md.

## Tranche 2 — completed geography notice-board retirement (24 October 2026)

**Recoverable exact pre-cull parent:** `6eef70deabfcca007ab3fdd88d0dc98bb7c041dd`. Retired 206 dated working artefacts, including 200 per-Incident geography audit packets and the campaign's intermediate inventories (total 915036 tracked bytes). At the historical campaign checkpoint, all 200 unique inventory rows had `canonical_applied: true`; all 200 preservation rows stated `original_fields_preserved` and `history_append_only`. Outcomes were 98 reviewed-and-recorded, 87 reviewed-unresolved and 15 reviewed-non-geographic. This is a check of the campaign's own recorded preservation results, **not independent human reauthentication**.

Canonical Incident JSON, source-linked geography, the schema, and current jurisdiction projection were not changed by the archive. The substantive reusable guidance lives in `vigil/docs/maintenance/`, and the retired packet bytes remain in Git history. Gate 1/Gate 2 planning documents and Maintainers instructions were marked historical where needed. The **active v0.8.0 taxonomy reconciliation notice board was not touched**. No final dataset tag, main merge, Zenodo publication or semantic recoding is part of this cull.


## Tranche 3 — completed historical adjudication worksheets (24 October 2026)

**Exact recovery parent:** `d6682f36b898a3f2136b6a55b2476f5087327bc8`. **Working branch:** `chore/siai-2026-release-readiness-20261023`; PR #162. **Retired:** 54 Git-tracked files (2409491 bytes). This is notice-board curation, not an Incident, taxonomy, HIM, EXTREQ, schema or release modification. The exact deleted file bytes remain available at the pinned parent commit; no Git history was rewritten.

| Retired area | Files | Material disposition and durable home |
| --- | ---: | --- |
| `2026-10-18-duplicate-explanation-repairs/` | 40 | Approved duplicate-assessment explanation guard is maintained in `vigil/scripts/occurrence_requirement_validation.py` and its tests. The 35 repaired Incidents, including six IEEE 7001 Level 4 Aligned-to-Boundary corrections, carry accepted row-level outcomes in their canonical external-requirement assessments and review history. Retired the prior raw before/after audit, generated diagnostics, snapshots and duplicate review packets, not the live validator. |
| `2026-10-18-section03-completion/` | 5 | Explanation-only basis changes to 14 mappings in 11 Incidents are carried in canonical `vigil/records/incidents/` records. Historic 0.7.0 inventory, criteria snapshots and one-off reproduction script are now process history. Open substantive questions are not declared resolved by this removal. |
| `2026-10-21-new-incident-tranche/` | 5 | Initial 0.7.0 completion packets for INC-205–209 are superseded by source-first 0.8.0 corrections under `vigil/docs/reviews/2026-10-23-intake-readjudication/`, its `README.md`, and current canonical Incident records. |
| `2026-10-21-new-agent-incidents/` | 2 | Earlier INC-205/206 intake snapshots are superseded by the same corrected 23 October adjudication and canonical records. |
| `2026-10-21-starshield-ukraine/` | 1 | Initial INC-204 intake audit superseded by the corrected 23 October review, updated canonical evidence and retained open follow-up on external restoration/authority evidence. |
| `2026-10-21-ingestion-main-080-merge/` | 1 | Completed main/ingestion compatibility worksheet retained in Git/PR #155 merge ancestry and current published 0.8.0 canonical records; it is not a runtime input. |

**Reference and uniqueness boundaries:** the 24 October preflight retention inventory did not identify canonical or non-review-code references to these exact retired directories; retirement also requires the current GitHub CI and dangling-reference gate. The earlier audit established these projects were completed and their implemented changes had durable owners. The 23 October corrected intake packets remain live for the SIAI worklist, as do active `2026-10-23-taxonomy-080-reconciliation/` screens. Neither canonical mapping nor evidence state was changed in this commit.

**Still held:** the active taxonomy 0.8.0 reconciliation (196 files), legacy Boundary and HIM decision records with live canonical references, potentially unique FC migration negative decisions, source-admission decisions and other historical worksheets pending content-by-content canonical promotion. No claim that 200 completed screens means 200 canonically reconciled or independently human-verified. Do not retire further packets without the established owner/uniqueness/dependency check.

**Post-change checks:** GitHub branch CI and retention/reference validation to be recorded in PR #162. The scientific main-based snapshot, final dataset checksum and any release/tag remain separate maintainer-controlled steps.


## Tranche 4 — completed INC-199–203 intake review (24 October 2026)

**Exact recovery parent:** `e0d58e4a14cd9e87b32dc43edcc434b618f019f3`. Retired all **8** files (680883 bytes) under `vigil/docs/reviews/2026-10-18-inc-199-203-completion/`. Its 18 October `README.md`, five Incident completion/adjudication snapshots and supporting checklists/validation are dated transitional worksheets, not a current canonical or runtime input.

The current canonical INC-199, INC-200, INC-201, INC-202 and INC-203 records were each checked individually before deletion: all five now carry taxonomy 0.8.0 and reference their **retained** dated current-edition full-rebuild decisions under `vigil/docs/reviews/2026-10-23-taxonomy-080-reconciliation/`; none references the retired 18 October folder. The original source evidence, harm, external assessment and mapping history remain in canonical Incident records. The permanent new-entry workflow and schema remain untouched. This cull does not assume all original vendor evidence has been independently authenticated or that the active current-edition reconciliation can be closed.

Prior tranche CI at `e0d58e4a14cd9e87b32dc43edcc434b618f019f3` passed the VIGIL records, taxonomy publications, external-governance and SIAI preflight workflows. The same checks must pass for this commit. Historic review bytes remain accessible through the exact pinned recovery commit. No merge to main or scientific tag was made.

**Cumulative additional review-notice-board cull on 24 October, tranches 3–4:** 62 files; earlier tranches 1–2 separately retired 306, giving 368 retired files in this curation sequence. All active 0.8.0 screen packets remain protected until canonical promotion and completion of the live campaign.
