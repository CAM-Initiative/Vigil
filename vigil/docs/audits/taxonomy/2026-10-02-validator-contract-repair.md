# Taxonomy adjudication validator repair — 2026-10-02

The maintainer-approved validator change is complete. Canonical Incident content and ledger decisions were not rewritten. This audit supersedes the earlier six-issue snapshot for current validation status; historical reports remain unchanged.

## Changed contract

- Canonical `ambiguous-boundary` is accepted alongside the compatible legacy `ambiguous-boundary exemplar` label. Unsupported labels remain errors.
- Successful and ambiguous occurrence findings do not require exemplar admission. Explicitly admitted taxonomy exemplars must still match the linked occurrence's class and role. This now detects stale admitted exemplars rather than forcing ordinary occurrences into exemplar status.
- Occurrence-specific uncertainty wording such as `no successor trace establishes`, `does not identify`, and `unavailable` is recognised. Empty reasons, generic class-state placeholders, duplicated reasons, boilerplate, MISSING cells and unsupported decisions remain invalid. The wording check does not certify substantive class recognition.
- The maintainer documentation and isolated generic fixture tests now express the same contract.

## Verification

All 57 relevant tests pass: 14 adjudication-rule tests, 33 external-requirement tests, 3 resolver tests and 7 classification tests. Required record, public projection, source, interpretive, system-component and authorship checks pass. Taxonomy family/catalogue validation passes for 15 families and 76 classes; occurrence requirement validation passes. Public outputs were rebuilt. The generated CaseFileExamples projection now reflects existing Stage 4 changes at INC-151/157/159/170/173; no new Incident classifications were chosen.

The four prior unresolved-reason wording failures now clear. The ledger quality phase reports zero errors. The newly accepted boundary spelling occurs in 82 Incident/class pairs across 46 Incidents.

## Remaining merge blockers — read-only results

| Surface | Remaining findings |
|---|---:|
| Ledger/canonical/Section 02/exemplar comparison diagnostics | 214 across 59 enrolled Incidents |
| Canonical architecture: stale admitted exemplar class/role relationships | 23 |
| Canonical architecture: classification/Section 02 role-set disagreement | 1: INC-126 / FC-083 |
| Canonical Incidents not enrolled in ledger | 4: INC-176–179 |

These counts overlap and are not numbers of distinct defective records. The ledger validator exits 1 on comparison diagnostics, not on the repaired wording/role parsing rules. Its CLI does not prove enrollment of every active Incident; the audit independently compares enrollment against all 170 current records. There are 166 enrolled records.

Examples: INC-151/FC-053 remains unresolved in the historical ledger while the canonical clause is a failure occurrence; INC-138/FC-078 and INC-174/FC-083 remain unresolved candidates in canonical records while taxonomy exemplars still claim admitted ambiguous-boundary roles. At INC-126, Section 02 includes successful FC-083 while the canonical classification does not. These require explicit reconciliation, not changing evidence or uncertainty to satisfy a guard.

The full per-Incident/class diagnostic list and affected IDs are in [the JSON audit](2026-10-02-validator-contract-repair.json). No broader semantic repairs were performed under validator-change approval. No Gmail message was sent; the diagnostic prefix alone does not perform or authorize communication.
