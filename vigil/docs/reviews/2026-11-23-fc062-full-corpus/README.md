# FC-062 full-corpus source-first reconciliation

**Review date:** 23 November 2026  
**Review branch:** `work/fc062-full-corpus-source-first-review-20261123`  
**Baseline:** `origin/main` at `0a340103cd84715232b3f20584331083db4c6be1`  
**Published taxonomy authority:** VIGIL v0.9.2 (published 15 November 2026)  
**Comparator only:** proposed v0.9.3 on `work/fc062-operative-reliance-incident-reconciliation-20261123`; unpublished and unapproved at this review start.

## Status

The canonical corpus contains **233 Incident JSON records** on the baseline ref. The machine-readable ledger records all 233, their record taxonomy version, any current canonical FC-062 mapping, existing clause relationships explicitly linked to FC-062, and exact source-record references attached to those relationships. Source references for unmapped candidate episodes are left unasserted until screening.

Initial bounded control screen: INC-001, INC-003, INC-056 and INC-218. Their decisions, condition-level screening, exclusions, competing classes and limits are in `BATCH-01-ESTABLISHED-CONTROLS.json`. This batch reuses the prior bounded review packet on the amendment branch and is **not** a fresh review of every primary source. These four ledger rows remain marked incomplete pending a full-incident source-first pass. Batch 02 adds bounded source-grounded screens of unmapped INC-085, INC-112, INC-130 and INC-138. It identifies one candidate failure for authorised FC-062 reconciliation (INC-085), leaves INC-138 unresolved between provenance-only and content-assurance defect, rejects an FC-062 addition for INC-112 on current evidence, and records INC-130 as unresolved on case-specific downstream adoption. These are candidate dispositions, not canonical mappings. The remaining **225 Incidents are not screened**, and all eight completed cases still need full-Incident review. No corpus-completion claim is made.

The amendment branch contains proposed FC-062 wording changes and bounded edits/review for INC-001, INC-003 and INC-218. It is not a pre-existing full-corpus review. PR #195 and `research/perception-calibration-evaluation-20261123` are related candidate research, not a canonical FC-062 corpus review. Neither source is incorporated as published authority or as evidence in an Incident unless present on baseline `main`.

## Corpus-level baseline counts

- Canonical Incident JSON records: 233
- Records with a current canonical FC-062 mapping: 36
- Current canonical FC-062 mapping rows: 36
- Clause-level FC-062 relationships found: 61
- Review dispositions completed: 0 full reviews; eight bounded screens (four initial controls and four independent candidates)
- New canonical FC-062 mappings proposed in this packet: 0

Mapping and clause counts are structural inventory results, not semantic review results. A validator or inventory cannot establish source-grounded classification completeness.

## Sequencing and preservation

Use v0.9.2 for all current canonical decisions until a specific amended taxonomy release is approved and published. Keep the v0.9.3 language as a labelled comparator only. After publication, update the review branch from the exact main commit and record the applied version; do not globally restamp records. Preserve every existing supported finding, episode attribution, source provenance, harm assessment and external requirement unless separately dispositioned under the maintenance workflow.

Do not amend Incident records, taxonomy, generated outputs, or website data in this review branch without the relevant separate authorization. Do not open a PR or merge without maintainer approval.

## Files

- `BASELINE-INVENTORY.json` — one explicit ledger entry per canonical Incident.
- `BATCH-01-ESTABLISHED-CONTROLS.json` — initial bounded screen and its limits.
- `BATCH-02-INDEPENDENT-CANDIDATES.json` — four unmapped candidate/control screens, recognition-condition findings, exclusions and competing classes.
- `CHANGE-AUDIT.json` — baseline-to-candidate changes; no canonical changes.
