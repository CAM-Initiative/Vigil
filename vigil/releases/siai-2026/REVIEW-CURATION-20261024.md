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


## Tranche 5 — obsolete 0.7.0 baseline inventories (24 October 2026)

**Exact recoverable parent:** `f46fcf30cf9e20e4726fd7e48fff2dc93c284ff8`. Removed **14** dated baseline inventory artefacts (1567910 bytes) from `vigil/docs/reviews/2026-10-18-incident-taxonomy-reasoning-readjudication/`: all 13 `inventory/` JSON files and the one-off `audit-reasoning-inventory.py`. The source inventory states explicitly that it is a **read-only 194-record, 465-mapping 0.7.0 census, not semantic adjudication**. The original temporary campaign was explicitly paused; these large repeat copies of historical canonical source/mapping inventories are not current scientific evidence or runtime inputs.

**Preserved:** `README.md`, all nine mapping/decision/comparator documents and historical Gate/maintainer decisions in this same directory; canonical Incidents and review histories; current 200-Incident 0.8.0 campaign worklist and all 196 active current-edition review artefacts. No individual current/rejected class decision or canonical record has been removed. Historic inventory bytes and its exact baseline context remain in the pinned parent and earlier commit ancestry. The live reproducible SIAI worklist has superseded the old census for current screening; this removal does not recast 0.7.0 as 0.8.0.

**Exit checks:** no 0.7.0 inventory blob appeared as a direct canonical or maintained-code dependency in the earlier repository retention reference inventory; current CI still must confirm no dangling paths and preserved publication/research validation. No release, tag, merge or taxonomic recognition change is included. Other 0.7.0 decision-bearing files remain held for review.


## Tranche 6 — reproducible historical Boundary population counts (24 October 2026)

**Recovery parent:** `72e97c1d2371df4b558c790e62e3729b16db1dc3`. Retired exactly **4** historical 0.7.0 population/census derivatives (389440 bytes): `2026-10-19-boundary-diagnostic/corpus-repair/CENSUS.json`, `POPULATION-VALIDATION.json`, `population-changed-paths.json`, and `contract-reassessment/CENSUS.json`. These are dated input/output enumerations, old checksums or changed-path listings of an already completed PR #140 operation, not independent evidence or new source-first verdicts. Their numerical checkpoints remain described in the campaign's retained method reports; the full blobs can be recovered from this exact Git parent.

**Deliberately preserved:** all per-Incident substantive Boundary diagnostic decisions, the current canonical Boundary data and review histories, its `POPULATION-REGISTER.json` with historically meaningful before/after information, role/confidence relocation records, the former census code and method documentation, all 196 actively used taxonomy 0.8.0 packets and all canonicals. The removed derivative filenames remain historical references in dated reports; those historical statements describe the older commit, not a promise of a presently resident file. No runtime code or current canonical `review_reference` pointed at the four removed paths in the previous retention inventory.

No Incident, taxonomy version/condition, HIM, external requirement, schema, validation policy, release or tag changed. Verify the new branch head's normal CI and curation checks before release.


## Tranche 7 — pinned historical source and method snapshots (24 October 2026)

**Exact pre-deletion recovery commit:** `82ee10e0be062a059fd893c5cff77f1f4ec0ebe5`. Removed **9 files (1241807 bytes)** that reproduce old published versions or execution states rather than independent adjudication decisions:

- Two 19 October outstanding-candidates baselines: `BASELINE-SNAPSHOTS.json` (full copies of selected canonical Incident records at Git `955239b...`) and `TAXONOMY-AUTHORITY.json` (published taxonomy class contents from the same pinned 0.7.0 commit). The 14 candidate decisions, taxonomy amendment proposal, independent analysis and research ledger remain. The historical review readme now links to exact Git-history snapshot rather than a missing active-tree path.
- One 18 October infrastructure-governance `baseline-inventory.json`, a registry/relationship/Incident inventory from the pinned original branch head `e176bef...`. All technical source-review/admission, proposal, gate and validation results remain; `PROGRESS.md` now links to the archived source inventory.
- Six dated HIM #126 read-only derivatives: `baseline-counts.json`, `corpus-counts.json`, `count-corpus.py`, `methodology-before.json`, `removed-frozen-test.txt`, and superseded `validation-round-1.json`. Retained **all 24 per-Incident HIM audits**, current `validation.json`, `hold-register.json`, per-record guards, `METHOD-AMENDMENT.md`, `SIAI-CORPUS-FACTS.md`, evidence source inventory, and canonical HIM findings. Both explanatory files now explicitly link their historical inputs via the pre-cull Git commit. This does not remove or redefine the adopted animal welfare criteria.

**Preservation boundaries:** no decision files, negative-candidate matrices, non-admission rationales or current Incident evidence were deleted. No current taxonomy screening packet under `2026-10-23-taxonomy-080-reconciliation/` was touched. Exact prior inputs can be reconstructed at `82ee10e0be062a059fd893c5cff77f1f4ec0ebe5`; current repository code may not depend on them. This commit changes only the historical note-board material, archived links, and the release curation ledger; no schema, canonical Incident, normative method, release or Git history is changed.

**Exit audit:** normal GitHub corpus/retention, taxonomy, external-governance and SIAI preflight checks must pass for the final head. Historic calculations remain scoped to their dated input versions and do not imply independent original-source verification.


## Tranche 8 — transient SOCI and infrastructure workflow receipts (24 October 2026)

**Recoverable pre-deletion commit:** `e8c1f6c07f3cd74b72d91d47d35c88b7fd27dd4f`. Retired **9 files (7040 bytes)** consisting only of small dated command/test receipts and prior pull-request/issue update acknowledgements:
- Six under `2026-10-18-soci-issue-132/`: `access-results.json`, `implementation-validation/results.json`, `proposal-validation.json`, `publication-results.json`, `remote-update-results.json`, and `validation-results.json`. The completed source admission, exact SOCI source/requirement proposition extraction, tested relationship proposals, raw access evidence, approved implementation summary, incident disposition, legal research, and permanent source metadata are unchanged. The dated `PROGRESS.md` replaces links/references to prior PR and validation receipts with pinned Git recovery URLs; it continues to record historical baseline integrity failure rather than misrepresenting it as an introduced defect.
- Three under `2026-10-18-infrastructure-governance-expansion/`: `baseline-results.json`, `stage-a-results.json`, `extraction-results.json`. Final validation result, source integrity/source-access hashes, actual admission proposals, normative extraction source-review files, and remaining research records are retained. The historical `PROGRESS.md` now links to its Git-pinned Stage A result instead of a missing file.

These are execution receipts, not unique Incident mapping dispositions, evidence, accepted requirements or method decisions. Their historical contents and CI/PR narrative remain recoverable through `e8c1f6c07f3cd74b72d91d47d35c88b7fd27dd4f`. No active taxonomy 0.8.0 packet was removed; no canonical Incident, taxonomy/HIM/EXTREQ/schema/test code or release tag was altered.

**Cumulative review curation at this checkpoint:** 386 files from prior tranches + 9 pinned historical snapshots from tranche 7 + 9 receipts from tranche 8 = **404 retired**. **563 review files remain**, including all 196 active v0.8.0 packets. Validate branch CI, reproducible screening worklist, canonical reference integrity and research preflight before further retirement.

## Tranche 9 — exact duplicate INC-003/SOCI notice-board copies (24 October 2026)

**Pre-deletion recovery Git commit:** `6aa2e54f41927390f3f7ae8f3f17d384514e09a0`. Retired **3** files (10609 bytes) after verifying equal Git blob SHA against the retained original for each of the three paths: follow-through INC-003 disposition and source-access records are identical to the SOCI issue #132 packet; baseline validation results are identical to the final receipt. The retained follow-through `README.md` now links to the two canonical notice-board locations for the duplicated review artefacts. Retained `adjudication-manifest.json`, all current Incident evidence, independent adjudication methods and the active v0.8.0 review. No substantive conclusions have been rewritten.


## Tranche 10 — dated historical validation/publication receipts (24 October 2026)

**Recovery parent:** `2519291962d1da0b01a1ae28caf38275496efdf2`. Retired **10 files (161116 bytes)** consisting solely of dated execution, CI, branch-diff, or publication receipts. A record of actual commands and previous success/failure remains recoverable at each Git blob URL under the pinned recovery commit, while the existing historical summary now links to that immutable provenance instead of stale relative paths.

| Historical campaign | Retired receipts | Substantive content retained |
| --- | ---: | --- |
| `2026-10-19-outstanding-candidates/` | 3 | Fourteen detailed candidate adjudications, source/research ledger, bounded non-admission reasoning, amendments and method summaries; archived issue-comment receipt and initial/final validation JSON |
| `2026-10-20-fc089-corpus-migration/` | 2 | All FC-084/089 transition class-criterion decision packets, final method report, baseline/screening/crosswalk, preservation manifest and code; archived concurrent-branch note and test results |
| `2026-10-19-boundary-diagnostic/` | 2 | Every Boundary and contract-reassessment per-incident adjudication, role-control inventory, before/after change register, confidence provenance, source-limited decisions, final method outcomes and old census code; archived two dated `VALIDATION.json` files |
| `2026-10-18-infrastructure-governance-expansion/` | 2 | Legislative/source research, primary carrier hashes, source and EXTREQ extractions, field-level candidates, branch work and integrated summaries; archived a Git-branch changed-path list and final command receipt |
| `2026-10-18-dignity-and-ecological-values/` | 1 | Exact bounded Incident and class screening, new dignity / ecology criterion reasoning and 194-incident candidate review; archived the dated test-command receipt |

No canonical Incident, taxonomy, HIM, registered requirement, schema, validator, current v0.8.0 packet, approved policy or maintained executable was deleted or changed. These are not substantive resolution of the still-held current-edition evidence/governance findings. The new source text cites prior execution only as historic outcome, not current evidence of independent human verification. **The GitHub CI and release-retention checks on the new commit are required before calling this tranche validated.**


## Tranche 11 — governed taxonomy-census copies and test receipts (24 October 2026)

**Exact recovery SHA:** `c25a80cb5ff8b43368b3f0af3ba9511cc017f5e6`. Retired **4 historical working files (124863 bytes)**:
- `2026-10-18-soci-issue-132/current-taxonomy-comparison.json`, a mechanical extract of seven historical taxonomy class definitions at the explicitly recorded prior Git head, with FC-078/081/088 delta IDs. It was not a new approved taxonomy change or canonical authority.
- `2026-10-18-soci-issue-132/inventory.json`, a historical cross-branch inventory of source/requirement counts and SOCI absence prior to the completed gated extraction.
- `2026-10-18-issue-126-him-reassessments/rebuild-guards.json`, the dated 24-command success receipts; **all 24 substantive per-Incident HIM audits, its adopted method amendment, final validation result, preservation analysis and remaining hold register are retained**.
- `2026-10-19-boundary-diagnostic/contract-reassessment/CONFIDENCE-CONTROL-REPRODUCTION.json`, a 442-byte test-command receipt; its role-scope/legacy-confidence inventory and actual decisions remain.

The parent SHA above now anchors Git-backed links in the historical reports, ensuring no false impression that these are current active-tree paths. The canonical taxonomy 0.8.0, Incident evidence, source/EXTREQ registries, Harm Impact framework, 196 still-active current-edition packets, and all maintained validators remain unchanged. No release or merge. CI on this commit is required before marking it validated.


## Tranche 12 — provably identical original Incident baseline snapshots (24 October 2026)

**Parent recovery SHA:** `41e5b8f40bcc76c014c39bdedc97d1960fbdf3a0`. Deleted 2 duplicated Incident JSON baseline files from `2026-10-20-fc089-corpus-migration/`, totaling **101762 bytes**. Verified each was exactly the **same Git blob SHA** as the governed canonical file in the original `be4bf1c784f956ff32c27377ff9e48c94a6fcb77` commit: `INC-000044-BASELINE.json` = `vigil/records/incidents/VIGIL-INC-000044.json` (`28aa82d`); `INC-000156-BASELINE.json` = `vigil/records/incidents/VIGIL-INC-000156.json` (`fa701f2`). Both original case states remain reproducible from that Git commit, and the actual FC-084 source-first decision files, negative evidence limits, and full rebuild manifests remain in the active tree. `METHOD-AND-OUTCOMES.md` now links directly to both original canonical objects. No taxonomy role, source or harm score changed.


## Tranche 13 — retired historical screening and disposable pipeline worklists (24 October 2026)

**Exact pre-deletion Git recovery SHA:** `e30f6f1f8c5da4662805ddafcd38d6018f155706`. Retired three outdated reproducible working outputs (324048 tracked bytes):
1. `vigil/docs/reviews/2026-10-20-fc089-corpus-migration/SCREENING.json`: historical taxonomy *0.8.1* broad relevance screen covering 194 titles/summaries. The 160 `screened-out` entries recorded generic non-relevance rather than a new criterion-tested case decision; the other 34 entries refer to **all 34 individually retained `INC-...-DECISION.json` files**, carrying the source-first candidate recognition, exclusion and unresolved evidence analysis. The screen does not supersede the current 200-Incident 0.8.0 taxonomy worklist. The retained method report now links to its pinned original for historical reproduction.
2. `vigil/docs/reviews/2026-10-18-infrastructure-governance-expansion/pipeline-qa.json`: its own scope says *in-memory downstream proposals; no Incident changes applied. Clause output is disposable candidates only.* The three studied cases INC-199, INC-200 and INC-203 have retained per-case proposal documents and current canonical 0.8.0 adjudications. The original upstream NIST sources and independently admitted EXTREQ records, source-review research, provenance, and final method report remain. Its `PROGRESS.md` now links to the pinned disposable candidate dump.
3. `vigil/docs/reviews/2026-10-19-boundary-diagnostic/census.py`: the prior read-only Boundary census script pinned to 0.7.0 at `032f8a2`, whose temporary output snapshots had already been retired. The preserved `README.md` now explains the original checkout requirement and links directly to the pinned script; current maintained validators and SIAI screening scripts were untouched.

**Preserved:** all canonical Incidents, FC/EXTREQ/HIM authorities, individual FC-084 source-first decisions (34), Boundary per-case decisions and before/after registers, current active 0.8.0 reconciliation files (196), maintenance rules, tests, review-history provenance and generated public source. These files were not independent evidence, accepted new mapping polarity or normative criteria. No release or Git-history rewrite; verify current CI and archival-reference gates.


## Tranche 14 — historical Issue #132 / PR #135 published communication copies (24 October 2026)

**Exact pre-deletion recovery commit:** `d40da7d562a55859c6cd482036fd306bbaffd380`. Removed five locally stored outbound draft/post copies (21085 bytes): `ISSUE-132-UPDATE.md`, `ISSUE-132-IMPLEMENTATION-UPDATE.md`, `PR-135-APPEND.md`, `PR-135-IMPLEMENTATION-UPDATE.md`, `ISSUE-132-OBSERVATION.txt`. Two files were verified *exactly* equal to [issue comment #6249530344](https://github.com/CAM-Initiative/Vigil/issues/132#issuecomment-6249530344) and [issue comment #6249644578](https://github.com/CAM-Initiative/Vigil/issues/132#issuecomment-6249644578); the earlier PR-append was the first of those with a comment marker; the implementation PR note was verified as text in PR #135's description. The scraped observation is represented by Issue #132's original body and thread. The original Git blobs remain accessible at the pre-deletion SHA.

Canonical SOCI law/source/requirement admission artefacts, original legislation research, source checks, specific INC-003 success/non-applicability findings, remaining operational website/approved-form questions and current v0.8.0 Incident worklist are preserved. The retained SOCI `README.md` now identifies the published sources and historical recovery path. No source admission, Incident, HIM, taxonomy, schema, maintained logic, validation or release was changed by this housekeeping commit.


## Tranche 15 — completed INC-003 process/checksum receipts (24 October 2026)

**Recoverable pre-deletion SHA:** `adf13e1e6802c5d2c046a16ea3b7fb6c46f7e4e3`. Retired two dated `2026-10-18-inc003-soci-followthrough/` result JSON receipts (1246 bytes): `preservation-results.json` (checksum/unchanged-field assertions) and `validation/results.json` (seven command exit statuses). The canonical INC-003 review reference resolves to **retained** `adjudication-manifest.json`, not either retired receipt; its existing class mappings, E019/E021 episode evidence, HIM and other requirements are unchanged. The adjacent `README.md` now links to both historical bytes at the recovery commit, and substantive source-first negative candidate analysis remains in its retained files. No canonical Incident or current v0.8.0 worklist touched.


## Tranche 16 — mechanical pre-repair Boundary schema-error enumeration (24 October 2026)

**Exact recovery commit:** `9eebf38326c5bc66d72d04fe10ddfb9400d69143`. Removed `2026-10-19-boundary-diagnostic/CONTROL-FAILURES.json` (36365 bytes). The JSON contained exactly 96 enumerated missing-`boundary_adjudication` field errors over 56 affected Incidents. Every entry's only error was `required completed object absent`; no differing recognition test, source-grounded decision, exclusion result or observed harm was represented. The still-retained `CONTROL-IMPLEMENTATION.md` records the original counts and now links to the Git-pinned full enumeration.

**Protected:** role-field control in maintained schema/validation; later substantive corpus-repair and contract-reassessment adjudication packets, their decision/provenance and remaining-failure analyses; canonical Incident history, current 0.8.0 screens, taxonomy/EXTREQ/HIM and release gates. The schema missing-field enumeration is a historical test receipt only; removal does not relabel unaddressed Boundary evidence as resolved. No merge/tag.


## Tranche 17 — registered external-source metadata fiches, safely promoted (24 October 2026)

**Exact recovery parent:** `e2a49427fce5236266174939633c970778c7a3a7`. Retired **13** historical duplicate files (37638 bytes) under `2026-10-11-infrastructure-governance-registration/`: 12 source fiches and the 13-source one-off `inventory.json`. Each of the 12 sources was checked against its exact external source ID/version in the current governed source registry, reviewed source scope, and source-assurance overlay; **source title, class, original historical reviewed scope and full SHA-256 carrier digest were verified present in those canonical governed records**. These are supporting source registrations, not a completed clause-level normative extraction or a finding of legal applicability.

**Deliberate exception:** retain `ICRC-SPACE-CIVILIAN-SERVICES.md`: its dated reviewed abstract-carrier hash was **not verified** in the current governed source-assurance overlay. The fiche provides the only visible retained full carrier digest while the source remains abstract-only; this is a reference-fidelity hold, **not** a GitHub Issue. The original historical complete 13-source inventory and all 12 retired note bytes are available at the pinned parent above; historical `README.md`, occurrence screening and registration gaps now link to the archive and to maintained live source records. No new or changed canonical source or provision, no altered legal force, taxonomy, HIM, Incident or validator. The active 196 current-edition taxonomy packets remain untouched.


## Tranche 18 — reconciled preliminary Boundary diagnostic packets (24 October 2026)

**Recoverable Git parent SHA:** `dfad3b20a70f1ec38ab350f13d5148f7f8131157`. Retired **53** older `2026-10-19-boundary-diagnostic/decisions/VIGIL-INC-*-BOUNDARY.json` packets (1028982 bytes). Before retiring, each was compared to its subsequent retained case-specific `corpus-repair/INC-*-DECISION.json` or `INC-*-CONFIDENCE-PROVENANCE.json`: preservation of all original mapping class identifiers, full initial mapping classification bases and decisive unresolved blockers was tested. All 53 current canonical Incident records were checked for exact references to those preliminary paths; none had one. Rechecked two canonicals updated concurrently by the v0.8.0 workthread (INC-048 and INC-098); no interim dependency was introduced.

**Exemptions:** INC-005, INC-018 and INC-095 old preliminary packets remain because the later `contract-reassessment/` packets do not verbatim preserve their earlier bases in this audit. Preserve these three until a source-specific historical basis reconciliation verifies their disposition; not a GitHub Issue. The original complete preliminary corpus is recoverable at [the pinned Git tree](https://github.com/CAM-Initiative/Vigil/tree/dfad3b20a70f1ec38ab350f13d5148f7f8131157/vigil/docs/reviews/2026-10-19-boundary-diagnostic/decisions). The later reviewed and unresolved outcomes, source provenance, 53 surviving newer case packets, confidence histories and 197 now-active 0.8.0 workthread files remain. No canonical Incident, source, taxonomy, HIM, EXTREQ or maintained validator was changed by this deletion.

**Concurrent branch context:** parent `dfad3b20a70f1ec38ab350f13d5148f7f8131157` contains the independent SIAI workthread's new progress on observable-evidence methodology and two current-edition incidents. This cleanup was rebuilt on that exact parent, preserving its new canonical and 0.8.0 work. Verify latest CI and release preflight before further retirement. No merge/tag/release.


## Tranche 19 — last three preliminary Boundary decisions after historical-reason promotion (24 October 2026)

**Recoverable pre-deletion parent:** `61ebadf5530cc19dfcc1415d8aaff2ae08a80ccd`. Retired **3 historical provisional review files (34430 bytes)**: `2026-10-19-boundary-diagnostic/decisions/VIGIL-INC-000005-BOUNDARY.json`, `.../VIGIL-INC-000018-BOUNDARY.json` and `.../VIGIL-INC-000095-BOUNDARY.json`.

Unlike tranche 18, their specific baseline bases were not found in the contract-reassessment packet alone, so these three were originally exempted. This tranche checked each baseline class ID and **all five verbatim original classification bases** against the retained intervening source-first per-incident decision, checked the final later contract reassessment for all five class IDs, and verified all three current canonical Incidents do **not** refer to the retired preliminary paths. The five original provisional negative/role-review `result.reason` explanations were explicitly promoted into the retained [Boundary README](https://github.com/CAM-Initiative/Vigil/blob/chore/siai-2026-release-readiness-20261023/vigil/docs/reviews/2026-10-19-boundary-diagnostic/README.md) alongside precise archival links to the original three Git blobs at this parent. These old diagnostic proposals are distinguishable from later outcomes; no previously rejected candidate was silently converted into a settled failure or success.

**Cumulative:** 503 retired from original 968 review files; **465 remain** including **197 current v0.8.0** reviews and 268 other historical items. No canonical Incident, evidence, class, harm, requirement, schema, validator, active v0.8.0 packet, held decision or release data changed. CI on the new head is required; no merge/tag/DOI/deposit.


## Tranche 20 — archived dated validation and PR-readiness receipts (24 October 2026)

**Exact recovery parent:** `d8368454f07709ab0ec21a124fc5d38d06bb96ed`. Retired **2 superseded historical review files (18,663 bytes)**: `vigil/docs/reviews/2026-10-18-issue-126-him-reassessments/validation.json` (14,458 bytes) and `vigil/docs/reviews/2026-10-20-fc089-corpus-migration/PR-READINESS.md` (4,205 bytes). The former is a historical test-command/output receipt with baseline/candidate counts, not an independently conducted HIM study; all 24 substantive HIM case audits, the approved method-amendment, preservation/impact and source evidence, held cases and final corpus facts remain. The three HIM method/facts documents now point directly to the Git-pinned original rather than an absent active-tree path. The latter duplicates a closed FC-084 migration's dated readiness/status text; its 34 source-first case decisions, source-access research ledger, class/mapping preservation proof, approved success-recognition taxonomy correction and implementation regression audit remain. The FC-084 method report links to the old readiness text at this pinned SHA, noting that its pending-approval statement was subsequently superseded.

**Cumulative:** **505 review files retired**, **463 remain** (**197 active current-edition v0.8.0** and **266 other historic**). Historical test counts are not current CI assurance; neither historical status note was relabelled as evidence of independent adjudication. No canonical Incidents, source registry, taxonomy, HIM rule, EXTREQ, schema, validator, current v0.8.0 packet or release artefact changed. Recheck branch CI; no merge/tag/DOI/deposit.


## Tranche 21 — archival of four dated process/coordination receipts (24 October 2026)

**Exact recovery parent:** `f2d832199f27e22280bb508e38510c3f403bbef8`. Retired **four non-authoritative historical review files (7,720 Git blob bytes):** `vigil/docs/reviews/2026-10-18-incident-taxonomy-reasoning-readjudication/validation/spotcheck-INC001-INC003.json`, `vigil/docs/reviews/2026-10-18-soci-issue-132/IMPLEMENTATION-RESULTS.json`, `vigil/docs/reviews/2026-10-18-infrastructure-governance-expansion/extraction-summary.json`, `vigil/docs/reviews/2026-10-19-outstanding-candidates/PR-READINESS.md`.

Promoted: the original INC-003 E019/FC-042 structural flag and two-case baseline scope into the historical retrospective README; exact SOCI source identities, four EXTREQ IDs and six reviewed relationship count into the approved implementation report (validated against current governed source/requirement registries); three primary NIST SHA-256 source carrier hashes, 8/5/2 requirements and 15/17/1102 extraction totals into SOURCE-REVIEW (each digest already independently retained in source-access and governed requirements); and the 14-candidate PR #140's nonadmission/readiness/initial CI-correction summary into the consolidated candidate analysis. Exact original bytes remain recoverable in Git at the pinned parent. Historical administrative reports are not independent semantic verification or evidence of current release readiness.

**Cumulative: 509 review files retired, 459 remain — 197 active current v0.8.0, 262 historical.** No active reconciliation, historical dissent or negative decision, canonical Incident, external source/requirement, HIM, class criterion, schema, validator, policy, or release/tag changed. Four current GitHub Actions workflows must pass on the new head; no merge, deposit or DOI authorised.


## Tranche 22 — two old implementation/validation execution receipts (24 October 2026)

**Exact recovery parent:** `035b81e88368c92a88088ae1bec8b7d30f81376c`. Removed **2** historical review files: `vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/VALIDATION.md` (6,711 Git blob bytes) and `vigil/docs/reviews/2026-10-18-wording-validation-implementation.json` (2,385 Git blob bytes). The former's exact command table, early 31/32 baseline pass, distinct pre-existing two-record FC-084 referential issue, and contemporaneous CI run IDs are retained as Git-pinned evidence and reconciled in the international registration README. The latter's approved structural evidence contract, 12 positive fixture tests, 258 at-time tests and strict limits on detecting quotation truth/chronology are promoted into the corresponding Gate 1 proposal. Active validators/fixtures, accepted governing decisions and current source/Incident records remain. Earlier reference links in registration README, implementation plan and INC-090 review are updated to exact Git-pinned objects.

**Cumulative: 511 retired, 457 remain (197 protected active v0.8.0, 260 other historical reviews).** No canonical Incident, source, requirement, HIM, taxonomy class, schema, code, validator, or scientific release changed. Current-head workflow status must be verified; draft PR and no merge/tag/DOI/deposit.


## Tranche 23 — reconciled Boundary recheck and role-control receipts (24 October 2026)

**Exact recovery parent:** `e614e2c096a4345770ae1c99a8fee21a1f42f7f8`. Retired **2 dated structural/control receipts** (`vigil/docs/reviews/2026-10-19-boundary-diagnostic/REMAINING-FAILURES.json`, `vigil/docs/reviews/2026-10-19-boundary-diagnostic/contract-reassessment/ROLE-CONTROL-VALIDATION.json`; Git blob sizes: 17,293 + 25,328 = **42,621 bytes**). The 42 earlier held-case reasons matched exactly by Incident, class and complete text against retained `POPULATION-REGISTER.json.held_proposals`. The 91 legacy Boundary confidences matched exactly by Incident, class and value against retained `corpus-repair/CONFIDENCE-RELOCATION-REGISTER.json.entries`. Earlier command/test/guard outcomes, including non-green historical fixture limits and original counts, are preserved in the Boundary README, source-specific Gate 1 method report and pinned Git originals. Existing test/controller code and current CI run unchanged. This is removal of *repeated structural snapshots*, not an evidentiary discharge or reopening of taxonomy semantics.

**Cumulative: 513 retired, 455 remain** (197 protected active v0.8.0 + 258 older). No canonical Incident, registered source/EXTREQ, HIM, taxonomy criterion, maintained validator/schema, published dataset, historical case negative decision or scientific release touched. Validate exact new head before merge consideration; PR remains draft, no tag/deposit.
