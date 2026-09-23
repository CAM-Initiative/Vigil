# Incident Scope Retirement — VIGIL-INC-000143 — 23 September 2026

## Decision

`VIGIL-INC-000143` is retired from the active VIGIL Incident corpus.

## Rationale

The preserved occurrence concerns Zillow's decision to wind down Zillow Offers after home-price forecasting uncertainty and resulting earnings and balance-sheet volatility proved greater than anticipated. Although the business workflow used machine-learning-assisted forecasting, the preserved evidence does not establish a sufficiently distinct AI-governance failure for continued inclusion as a VIGIL Incident.

The material is better characterised as a business-risk, forecasting-risk and business-continuity / strategic-exit problem in which an AI-enabled forecasting system was one component of a broader commercial operating model. Model involvement alone is not sufficient for VIGIL inclusion where the occurrence evidence does not establish a separate governance failure attributable to the AI system, its authority, controls, deployment, oversight or consequential use beyond ordinary organisational risk management.

The prior medium-confidence mapping to `VIGIL-FC-000062` depended on treating insufficient predictive assurance for the scale of financial reliance as an AI-governance failure. On review, that boundary is too broad for VIGIL: it would risk converting ordinary forecasting error, commercial model risk and business-continuity failures into AI governance incidents merely because machine learning was present in the workflow.

## Preservation boundary

The canonical Incident file is removed from `vigil/records/incidents/` and therefore should be omitted from regenerated public Incident indexes and taxonomy Case File projections. Historical references in dated audits and review artefacts remain part of the repository's append-only review history and should not be rewritten to imply that the record was never assessed.

The former canonical record, source material, taxonomy analysis, Harm Impact assessment and interpretive provenance remain recoverable through Git history.

## Current corpus effect

- retired Incident: `VIGIL-INC-000143`
- active Incident count after retirement: 142
- canonical successor: none
- retirement reason: occurrence falls outside the intended VIGIL AI-governance incident boundary; the preserved evidence supports business / forecasting / continuity risk more strongly than a distinct AI-governance failure
