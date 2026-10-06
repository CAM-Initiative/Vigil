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

The self-replicating prompt-injection examples are represented by INC-000183 through INC-000186. No new umbrella Incident was allocated.

The earlier continuity-propagation proposal remains rejected: reproduction alone is attack-chain topology rather than an independent governance failure. Subsequent review identified a different recurring mechanism and reinstated the FC-000084 identifier as **Verification Lineage Assurance Integrity** under proposed family FF-0003 Verification & Completion Integrity.

The revised proposal is:

`vigil/taxonomy/proposals/2026-10-06-verification-lineage-assurance-integrity-draft.json`

Its plain-language alias is **Verification Laundering**. It governs assurance that increases through system mediation, inherited verification state, repetition or false corroboration without additional independent verification. The worm-specific manifestation is **Recursive Descendant Corroboration**: descendants sharing a common verification origin must not be counted as independent confirmation merely because propagation has created several apparently separate artefacts.

INC-000185 and INC-000186 now preserve direct proposal support as `taxonomy-gap` clauses with partial adjudication coverage. INC-000183 and INC-000184 were re-tested and remain `resolved-no-mapping` because their published traces establish reproduction without the required verification-assurance increase. Existing canonical mappings remain unchanged.

The bounded re-adjudication is documented at:

`vigil/docs/reviews/2026-10-06-fc-000084-verification-laundering-readjudication.md`

The broader authority-laundering graph diagnostic remains useful and separate; FC-000084 captures the verification-assurance mechanism rather than generic propagation or authority laundering.

## Branch state

The ingestion branch remains a working allocation branch and is behind current `main`. Per maintainer contract, accumulated ingestion work should be preserved and the branch should be synchronised from main only at the pre-PR boundary. No pull request was opened from this incomplete state.
