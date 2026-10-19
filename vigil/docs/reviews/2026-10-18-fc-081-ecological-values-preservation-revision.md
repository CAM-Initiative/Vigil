# FC-081 — Ecological Values Preservation: Substantive Fidelity Class Revision

**Date:** 2026-10-18
**Repository:** CAM-Initiative/Vigil
**Working branch:** `agent/incident-ecosystem-ingestion`
**Disposition:** CAM steward clarified the intended ecological invariant following an initial terminology-only rename. Revised the existing *working-branch* canonical FF-0012/FC-081 definition, not a new class or published dataset release.

## Steward instruction and meaning

The intended invariant is that **AI systems must materially factor ecological values into ecologically relevant objectives and decisions, rather than allowing financial or other optimisation objectives to erase them**. It does *not* require proof that a pre-existing hard ecological constraint was violated, and it does not turn all ecological effects into automatic violations or categorically bar justified trade-offs.

This corrects the overly narrow earlier recognition boundary that required a separately independently binding ecological threshold. It is a **substantive governed boundary revision**, not merely a cosmetic display-name change.

## Identity continuity and controlled semantic code revision

- Retained immutable ID: **`VIGIL-FC-000081`**
- Current class name: **Ecological Values Preservation**
- Current class code: **`ECOLOGICAL_VALUES_PRESERVATION`**
- Prior canonical display names retained as aliases: **Biospheric Constraint Priority** and **Ecological Boundary Preservation**
- Former semantic code retained as alias: **`BIOSPHERIC_CONSTRAINT_PRIORITY`**
- Parent: **FF-0012 Objective Pursuit Integrity**
- Parent family local version advanced from **0.2.0 to 0.3.0**, and corresponding taxonomy index entry synchronised.
- The current **published dataset** version is still 0.6.11: no release ledger, timestamps, incident records, mapping stamps or old external reference-review texts were rewritten.
- The code revision is governed by `vigil/taxonomy/README.md` §Immutable identity and semantic codes, which explicitly permits controlled semantic code revisions while requiring prior public codes to remain aliases.

## Diagnostic boundary

### Failure recognition

Require evidence of all of the following:
1. A materially ecologically relevant AI-mediated decision or optimisation objective.
2. Specific applicable ecological values, planetary-life-support interests, ecological impacts or binding limits, supported by reasonably available information or an applicable duty to assess.
3. Evidence those values were absent, misrepresented, treated as practically negligible or improperly overruled in actual objective formulation, evaluation or pathway choice.
4. Evidence the omission or unwarranted discount was connected to preference for financial, throughput, growth, speed, performance, reward or other optimisation utility; mere environmental injury or an output lacking environmental vocabulary is insufficient.
5. No adequate, evidenced, proportionate and reviewable justification for the disputed trade-off or any variation of a separately binding limit.

A valid, genuinely deliberated, independently permissible trade-off may choose an ecologically imperfect option without breaching the class. A governing ecological threshold remains binding where independently established. Downstream environmental injury remains a separate VIGIL-HIM assessment.

### Successful invariant

A positive exemplar requires a *genuine challenge* in an ecologically relevant decision, evidence that ecology meaningfully influenced the evaluation and pathway selection, and affirmative justification for any trade-off. Lack of reported environmental harm alone does not constitute success.

### Illustration

- **Failure example:** a data-centre siting optimiser drops well-supported water-stress and habitat data from location-ranking criteria solely to minimise financial cost, without a defensible evaluation of those values.
- **Successful example:** an infrastructure planning agent compares capital cost, performance, water security, biodiversity and applicable ecological limits, makes a reasoned choice and records the resulting trade-offs.
- **Not enough:** an adverse environmental result in the absence of evidence about the optimisation criteria and actual treatment of ecological considerations.

## Parent-family contract

FF-0012 now explicitly includes ecological values as material governing considerations during objective formation, evaluation and pathway selection, while retaining its other two children:
- FC-069 Objective–Reward Alignment
- FC-070 Safe-Exit Transition

FC-081 is still narrower than the parent. All existing IDs remain unchanged. Parent family local version and index version agree at 0.3.0.

## Historical source and incident compatibility

- The superseded first-stage ecological rename is recoverable at the pre-cleanup Git commit `290b8d82c5e238e8ccdea82aa018e491e6d229fb`, not retained as a second live research authority.
- The prior INC-129 ambiguous-boundary exemplar remains ambiguous: the captured statement supports ecological-stewardship principles but demonstrates no concrete ecologically relevant optimisation decision, omission or trade-off under pressure.
- Earlier standards/EXTREQ assessments that explicitly rejected **absolute biospheric-constraint priority** (for example IEEE 7000-2021 context-only annotation) **must not be silently converted into proof of support for the broader value-consideration class**. Those FC↔EXTREQ relationships need their own source-faithful reassessment under the new boundary, now tracked in [GitHub issue #145](https://github.com/CAM-Initiative/Vigil/issues/145).
- No legacy Incident occurrence is automatically changed to failure or success by the definition revision; an evidence-specific re-adjudication remains required.

## Validation performed and remaining

Verified by connected repository reads after commit:
- Every current canonical family file (16) structurally checked against the currently declared family JSON Schema contract (required properties, types, constraints, unique lists, basic refs).
- Verified all 79 selectable class IDs and codes globally unique, parent/child and index membership consistent, class target relationships point to allocated IDs, family version/index synchronised, and FF-0016 / FC-088 still present.
- Verified current class display name/code and historical aliases.

**Not run:** actual Python `validate_taxonomy.py`, complete test suite, CI, publication preparer or downstream website build. Working branch has unrelated staged FF-0006/FC-078 content. The official release digest must be reconciled by the governed next taxonomy publication; do not silently restamp v0.6.11.

No new branch or pull request was created.
