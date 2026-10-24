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
