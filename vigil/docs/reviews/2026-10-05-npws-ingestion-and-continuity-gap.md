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

## Authority-lineage diagnostic observation

The self-replicating prompt-injection examples are already represented by INC-000183 through INC-000186. No new umbrella Incident was allocated.

A first-pass review treated active reproduction of instruction-bearing state as a possible continuity taxonomy gap. Subsequent cross-corpus review rejected that conclusion. Reproduction is material attack-chain topology, but it does not itself establish a governance failure missing from the current taxonomy. The operative governance questions arise when descendant state is relied upon, promoted, delegated, transferred or inherited without the applicable authority, provenance, scope or validity checks.

The earlier proposed FC-000084 is therefore withdrawn from promotion. The reproduction clauses in INC-000183–186 are retained as `resolved-no-mapping` occurrence facts, and existing canonical mappings remain unchanged.

The successor analytical work is documented at:

`vigil/docs/reviews/2026-10-05-authority-lineage-laundering-diagnostic.md`

The candidate invariant requires authority to remain traceable to an independently valid originating mandate across propagation, transformation, delegation, persistence and replication, and prohibits treating descendant artefacts as independent corroboration of their own authority lineage. This is a chain-level diagnostic, not a canonical class amendment.

## Branch state

The ingestion branch remains a working allocation branch and is behind current `main`. Per maintainer contract, accumulated ingestion work should be preserved and the branch should be synchronised from main only at the pre-PR boundary. No pull request was opened from this incomplete state.
