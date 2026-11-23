# FC-062 full-corpus source-first reconciliation

**Review date:** 23 November 2026  
**Review branch:** `work/fc062-full-corpus-source-first-review-20261123`  
**Baseline:** `origin/main` at `0a340103cd84715232b3f20584331083db4c6be1`  
**Published taxonomy authority:** VIGIL v0.9.2 (published 15 November 2026)  
**Comparator only:** proposed v0.9.3 on `work/fc062-operative-reliance-incident-reconciliation-20261123`; unpublished and unapproved at this review start.

## Status

The canonical corpus contains **233 Incident JSON records** on the baseline ref. The machine-readable ledger records all 233 in a compact columnar JSON format (`columns` defines each row field), including record taxonomy version, current canonical FC-062 mapping details, linked clause relationships, and each reviewed disposition. Exact source/episode references are retained in clause relationships and batch decisions; candidate source references are not asserted before screening.

Initial bounded control screen: INC-001, INC-003, INC-056 and INC-218. Their decisions, condition-level screening, exclusions, competing classes and limits are in `BATCH-01-ESTABLISHED-CONTROLS.json`. This batch reuses the prior bounded review packet on the amendment branch and is **not** a fresh review of every primary source. These four ledger rows remain marked incomplete pending a full-incident source-first pass. Batch 02 adds bounded source-grounded screens of unmapped INC-085, INC-112, INC-130 and INC-138. Feedback refinement: INC-085 remains a high-priority candidate pending decision-point and causal-reliance analysis; INC-112 is reopened as unresolved following newly identified reasoning at actions 904 and 911; INC-130 remains on an evidence-limited adoption hold; and INC-138 remains unresolved, with no Boundary admissible until material engagement and exact recognition-condition gaps are documented. Batch 02 has no canonical mappings or role changes. Batch 03 independently screens unmapped INC-185, INC-205 and INC-215: INC-185 is a high-priority failure candidate; INC-205 is a possible bounded success not admitted because the correct initial interpretation was reversed before a distinct completed reliance outcome is established; INC-215 is rejected for FC-062 failure/success and has no FC-062 Boundary because model-level calibrated interpretation is not evidenced. The total through Batch 03 was **11 bounded screens** (four Batch 01 controls, four Batch 02 candidates, three Batch 03 screens); all remained incomplete pending full-Incident review. Batch 04 adds detailed source-first screens for unmapped INC-084, INC-086 and INC-136: two failure candidates and two possible positive outcomes (INC-086 stand-down and INC-136 rejection), all pending full review and without canonical changes. The reconciled total through Batch 04 is **14 bounded preliminary screens** and **219 unscreened Incidents**. **Completed full reviews: 0; incomplete reviews: 233; 0 + 233 = 233.** The remaining **219 Incidents have no recorded batch disposition**. No corpus-completion claim is made.

The amendment branch contains proposed FC-062 wording changes and bounded edits/review for INC-001, INC-003 and INC-218. It is not a pre-existing full-corpus review. PR #195 and `research/perception-calibration-evaluation-20261123` are related candidate research, not a canonical FC-062 corpus review. Neither source is incorporated as published authority or as evidence in an Incident unless present on baseline `main`.

## Corpus-level baseline counts

- Canonical Incident JSON records: 233
- Records with a current canonical FC-062 mapping: 36
- Current canonical FC-062 mapping rows: 36
- Clause-level FC-062 relationships found: 61
- Review dispositions completed: 0 full reviews; fourteen bounded screens (four initial controls, four Batch 02 candidates, three Batch 03 screens and three Batch 04 cases)
- New canonical FC-062 mappings proposed in this packet: 0

Mapping and clause counts are structural inventory results, not semantic review results. A validator or inventory cannot establish source-grounded classification completeness.

## Sequencing and preservation

Use v0.9.2 for all current canonical decisions until a specific amended taxonomy release is approved and published. Keep the v0.9.3 language as a labelled comparator only. After publication, update the review branch from the exact main commit and record the applied version; do not globally restamp records. Preserve every existing supported finding, episode attribution, source provenance, harm assessment and external requirement unless separately dispositioned under the maintenance workflow.

Do not amend Incident records, taxonomy, generated outputs, or website data in this review branch without the relevant separate authorization. Do not open a PR or merge without maintainer approval.

## Files

- `BASELINE-INVENTORY.json` — one explicit columnar ledger row per canonical Incident; mapping bases, confidence/role and FC-062 clause relationships are preserved.
- `BATCH-01-ESTABLISHED-CONTROLS.json` — initial bounded screen and its limits.
- `BATCH-02-INDEPENDENT-CANDIDATES.json` — four unmapped candidate/control screens, recognition-condition findings, exclusions and competing classes, revised under review feedback.
- `BATCH-03-INDEPENDENT-DISCOVERY.json` — three independently discovered unmapped screens, including one high-priority failure candidate and two positive-control screens.
- `BATCH-04-SOURCE-FIRST-CANDIDATES.json` — three criterion-level screens of operational interpretation and positive outcomes.
- `CHANGE-AUDIT.json` — baseline-to-candidate changes; no canonical changes.

## Recovery substantive review checkpoint

Batch 05 proceeds in baseline order through INC-001–010. Nine evidence-bounded substantive dispositions are complete; INC-010 remains incomplete because the recovered MP4 audio/whole interaction has not been assessed. **9 completed + 224 incomplete = 233**. Screening coverage now considers **22 / 233** (including preserved screens); 211 have not yet been considered. Prior batches remain preliminary history, not completion certificates.

`BATCH-05-DETERMINISTIC-001-010.json` records published-condition tests, comparator limits, source access/recovery, competing properties and preserved prior findings. INC-008 is a new Boundary candidate; no canonical mapping is added.
