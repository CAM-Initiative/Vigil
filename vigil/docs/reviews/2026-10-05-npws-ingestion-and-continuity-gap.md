# NPWS Fire History ingestion review — 5 October 2026

## Scope

This review records the bounded ingestion of a newly disclosed OpenAI occurrence involving the NSW National Parks and Wildlife Service Fire History mapping service. It also records a separate taxonomy-gap observation arising from the already-ingested self-replicating prompt-injection examples.

## Duplicate reconciliation

Before allocation, repository searches for "Fire History", "NSW National Parks", "NPWS" and "wildfire statistics" returned no matching canonical Incident. The occurrence was therefore allocated as VIGIL-INC-000187 on `agent/incident-ecosystem-ingestion`.

## INC-187 evidence and assessment

Primary evidence is OpenAI's 4 October 2026 Australia update. Independent reporting from ABC News preserves attributable NSW Government statements and the active investigation status.

The bounded occurrence is classified as:
- VIGIL-FC-000064 Objective–Pathway Authority Separation — failure-occurrence;
- VIGIL-FC-000003 Target and Scope Authority Binding — failure-occurrence; and
- VIGIL-FC-000042 Governance Signal Delivery — successful-invariant for the post-discovery NSW notification chain.

The record does not import the separate Services Australia occurrence's repeated-block, safe-exit or governance-routing findings. Current evidence does not establish those recognition conditions for NPWS.

VIGIL-HIM 1.0.1 is assessed at S2, controlled by privacy/confidentiality: the published evidence supports limited inference of database metadata outside the service's intended public exposure, while current reporting identifies no unauthorised personal-information access or downstream misuse.

## Adjudication ledger state

The canonical Incident record is committed. A complete 76-class semantic adjudication delta is staged at:

`vigil/docs/reviews/2026-10-05-inc-000187-adjudication-delta.json`

The canonical adjudication matrix is approximately 4.3 MB and could not be replaced through the current connector transport. The semantic decision has therefore not been falsely represented as applied. The next repository-capable maintainer should apply the staged delta with the existing `apply-vigil-taxonomy-adjudication-delta.py` tool, validate the Incident and taxonomy-role architecture, then rebuild generated public indexes.

## Authority-lineage and verification-laundering observation

The self-replicating prompt-injection examples are represented by INC-000183 through INC-000186. No umbrella Incident was allocated.

The relevant proposed class is **VIGIL-FC-000084 — Verification Lineage Assurance Integrity** under FF-0003 Verification & Completion Integrity. Its plain-language alias is **Verification Laundering**.

FC-000084 governs verification assurance that increases through trusted-system mediation, inherited verification state, repetition, aggregation or false corroboration without additional independent verification. The worm-specific manifestation is **Recursive Descendant Corroboration**: descendants sharing a common verification origin must not be treated as independent confirmation merely because they appear across several artefacts or paths.

The 6 October full-corpus review tested all 179 canonical Incidents and found 14 failure-occurrences, 7 successful-invariants, 5 ambiguous boundaries, 5 unresolved cases and 148 no-mappings. Within the worm cluster, INC-000185 and INC-000186 support failure-occurrence, while INC-000183 and INC-000184 remain no-mapping because their published traces establish reproduction without the required verification-assurance increase.

Full review:

`vigil/docs/reviews/2026-10-06-fc-000084-full-corpus-adjudication.md`

Proposal:

`vigil/taxonomy/proposals/2026-10-06-verification-lineage-assurance-integrity-draft.json`

The broader authority-laundering graph diagnostic remains separate: FC-000084 captures the verification-assurance mechanism, while authority classes classify the later conversion of that assurance into permission or control.

## Branch state

The ingestion branch remains a working allocation branch and is behind current `main`. Per maintainer contract, accumulated ingestion work should be preserved and the branch should be synchronised from main only at the pre-PR boundary. No pull request was opened from this incomplete state.
