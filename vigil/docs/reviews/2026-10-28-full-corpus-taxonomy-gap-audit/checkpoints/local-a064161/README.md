# Full-corpus taxonomy-gap detection audit — 28 October 2026

Status: **in progress; not a completed semantic audit**. Owner: maintainer-requested read-only audit, `work/full-corpus-taxonomy-gap-audit-20261028`. Base: ingestion SHA `0f008d983da72db962705fb9c732496e703cdb5e`. No canonical changes are authorised by these recommendations.

## Population

206 canonical Incidents (205 active, one monitoring), 1,187 listed clauses. All listed clauses carry one of the four current schema values. The population is all 681 `resolved-no-mapping` clauses in 187 Incidents, plus five supplemental legacy `no_mapping_rationale` representations under current `unresolved` status in INC-196–198: **686 review items across 190 Incidents**. No missing or alternative structured status value was found. The supplemental inconsistencies must not be silently treated as completed no-mapping decisions. Monitoring is included; generated indexes and historical review copies are excluded as duplicates, not separate occurrences. Narrative terminology and noncanonical relationship representations remain a separate inspection task.

`BASELINE.json` pins the population; `INCIDENT-MANIFEST.json` records each canonical file hash; `REGISTER.json` enumerates every in-scope clause with stable episode ID and 1-based clause index. Initial `not-reviewed` statuses are deliberate and must not be converted into evidence-limited conclusions without actual review. `CRITERIA-SNAPSHOT.json` records the 82 selectable class definitions and exact recognition/exclusion wording from 18 family files at published main commit `0fdabb940cef157609e3cd2a20efa213cdfca2ef`, v0.9.0, dated 27 October 2026. All normative class contracts match ingestion. FF-14 differs only in a non-normative INC-126 exemplar, not the class recognition contract.

## Review sequence and completeness

For each clause: recover original source/context and responsible actor; independently state material governance properties; test plausible current classes and their literal necessary conditions and exclusions; reconcile the original rationale and relevant previous reviews; record one of the five requested recommendations with confidence and exact uncertainty. Distinguish observation from causal interpretation, and actual unavailable evidence from unfinished review. A favourable result or remediation announcement is not proof of the entire protective pathway. Unknown root cause is not proof of no failure.

No canonical classifications, source records, taxonomy definitions, validators, production methodology or website outputs may change. Proposed class concepts remain non-normative. This working notice board is exempt from retirement until human review of the requested audit findings; later reconciliation and retirement require separate work and authorisation.

## Prior work and deduplication

- [#133](https://github.com/CAM-Initiative/Vigil/issues/133): broad source-first no-mapping review, historical 189-record/684-clause baseline. Its counts are not this audit baseline.
- [#171](https://github.com/CAM-Initiative/Vigil/issues/171): seven positive-outcome Incidents and material no-mapping omissions; version-dependent custody questions must now be tested against published v0.9.0 rather than assumed still uncovered.
- [#150](https://github.com/CAM-Initiative/Vigil/issues/150): dependency cultivation versus disengagement/exit boundaries.
- [#170](https://github.com/CAM-Initiative/Vigil/issues/170): defender-centred honeypot outcomes, actor attribution and positive boundaries.

These are overlapping review inputs, not evidence or pre-decided outcomes. No duplicate issues have been created.

## Completion ledger

- [x] Ingestion branch head pinned; audit branch created directly from that head, locally and remotely.
- [x] Root and vigil agent instructions, schema status/coverage contract, validator status logic, source-first protocol, no-mapping gate and taxonomy-gap proposal inspected.
- [x] Enumerate canonical files, workflow states and all structured clause statuses.
- [x] Create complete initially unreviewed clause register and canonical hash manifest.
- [x] Check main publication version v0.9.0 and compare every normative class contract.
- [x] Inspect noncanonical relationship labels, legacy no-mapping rationales and all 40 statement-analysis entries for representation differences.
- [x] Attempt initial source recovery for the expanded population; results remain access/extraction states, not source-review findings.
- [ ] Finish substantive original-evidence inspection, PDF/image review and failed-access fallbacks.
- [ ] Complete independent clause-level materiality and literal criterion/exclusion review for 686 items.
- [ ] Reconcile historical rationales and related issues after independent review.
- [ ] Consolidate repeated mechanisms, compare prior proposals and draft any justified candidates.
- [ ] Produce executive findings and prospective methodology/QA recommendations.
- [ ] Run register completeness/recommendation QA and canonical byte-preservation check.

A source download is not a source review. Population enumeration is not a semantic finding. No executive distribution may be represented as final while reviews remain outstanding.

## Actual checkpoint state

One completed clause recommendation: **INC-003 E017 — reconsider existing classification under FC-090**, supported by printed page 14 of the original provider technical report and individual condition/exclusion tests. This is not a canonical mapping change or an Incident-wide completeness claim. Thirteen other clauses have provisional recommendations awaiting completion of their literal condition/exclusion matrices. The remaining **672 items are unreviewed**. No consolidated taxonomy-gap finding or full-corpus recommendation distribution has been established.

The next sequential work is INC-006 onward, alongside completion of the thirteen provisional matrices. `REGISTER.json` retains every original clause and prior rationale; do not overwrite it with a fresh empty inventory. `SOURCE-RECOVERY.json` provides URLs, source-reference joins, response states and content/extraction hashes for recovery. A 200 response or extracted wrapper does not establish that the original evidence was substantively available. The number of clauses genuinely lacking sufficient evidence is still undetermined.
