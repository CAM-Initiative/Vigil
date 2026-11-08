# INC-000129 — six-mapping reconciliation, evidence and current-role tests

Date: 2026-11-08. Issue: #187. Status: **partial source-first forensic review; exact first-removal commit and full current taxonomy definition inspection outstanding**. AI analytical review only.

## Verified commit-pinned snapshots

| Commit/ref | Incident version | Canonical classes |
| --- | --- | --- |
| `a3958659a778612e8f64fb80bac24cf6dc75b694` | 0.3.15, 18 October review | FC-075, FC-078, FC-076, FC-077, FC-080, FC-081; all ambiguous-boundary |
| `d8cf1d85056929eb7748551bec1ec2b40cc6899b` | 0.3.17 | same six ambiguous boundaries |
| `034c9407fe0797f7ff6c335989ba2dc7715c89cb` | 0.3.21 | FC-075 and FC-078 only |
| `main` on 8 November | 0.3.22 | FC-075 and FC-078 only |

The removal occurred **after the 0.3.17 snapshot and no later than 0.3.21**. The exact first changing commit is not yet verified. The 24 October review reports baseline version 0.3.20 and provides explicit decisions **only for FC-075 and FC-078**. Do not infer that the other four were separately reviewed merely because the later record says they are conceptual crosswalks.

Crucially, the four classes' clause-level explanations **were preserved**, but `taxonomy_relationships[].canonical_taxonomy_mapping` switched from `true` to `false` and the relationship became `conceptual crosswalk — not an admitted mapping`. The issue is a **canonical-admission change without a recovered four-class decision ledger**, not wholesale deletion of source interpretation.

The 18 October six-mapping record already had FC-075 and FC-078 as **Boundary**, not their older failure and success roles. The 17 October Stage B review had challenged those earlier polarities. Therefore the history includes at least two distinct transitions: (a) failure/success to Boundary; (b) six admitted Boundaries to two.

## Source/criterion preliminary six-class dispositions

These are **provisional analytic tests**, not final current-taxonomy adjudications; current exact version-pinned class definitions, exclusions and additional source recovery remain to be inspected.

- **FC-075 — Pragmatic Constraint Rendering Integrity**: actual compaction and directive-like output are evidenced. Antecedent applicable governing-state comparator and lost qualifications are not. Current Boundary is supported as an evidence-limited question; neither failure nor success established. Evidence: provider compaction passage, E001.
- **FC-078 — Continuity-State Validity**: handoff, resumed coding, later non-repetition evidenced. No affirmative successor validation/quarantine or materially harmful adoption established. Current Boundary is supported as an evidence-limited question; earlier success not established. Evidence: E001/E002.
- **FC-076 — Governance Neutrality**: source states non-answerability to corporations/governments. No observed interested-principal capture, pressure or neutral decision. **Conceptual relationship demonstrated; occurrence-level Boundary recognition unresolved pending exact scope/exclusion test.** Do not promote to failure or success.
- **FC-077 — Distributed Role Constraint Integrity**: equality/non-subservience language relates to user relationship. No distributed task graph, component constraint ownership or exercised challenge route. **Conceptual relationship demonstrated; occurrence-level scope potentially absent.** Test class-scope exclusion before considering Boundary.
- **FC-080 — Human Contribution**: source values human culture; no particular transformed human contribution or subsequent attribution/erasure evidenced. **Conceptual relationship demonstrated; occurrence-level scope potentially absent.**
- **FC-081 — Ecological Values Preservation**: source asserts primacy of nature; no ecological decision, applicable biospheric constraint or competing objective pathway in the coding task. **Conceptual relationship demonstrated; occurrence-level scope potentially absent.**

These assessments **do not justify automatically restoring all four** as canonical boundaries. Equally, the 17/18 October explicit provisional-retention instruction cannot be considered discharged without a class-by-class decision trail.

## Outstanding forensic work

1. Find first exact commit that changed INC-129 between v0.3.17 and v0.3.21; inspect patch, authorisation and any review manifest.
2. Read exact current selectable definitions for all six, including role-scoped versus all-role exclusions; apply criterion-by-criterion source/episode tests and capture independent candidate discovery.
3. Confirm whether omitted four satisfy positive material-engagement for Boundary or only noncanonical conceptual relationships; record explicit reasons and source references.
4. Complete preservation ledger, SIAI paper version note and wider-corpus mapping-loss census.
5. Propose targeted CI controls without modifying schema/validator or canonical data before review.

No canonical record, class definition or public output changed in this commit.
