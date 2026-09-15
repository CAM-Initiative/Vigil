# VIGIL S5 severity and successful-invariant relationship reconciliation

**Date:** 2026-09-14

**Artefact class:** REVIEW

**Status:** canonical schema and Incident reconciliation

## Decision

VIGIL severity now distinguishes an evidenced occurrence from an adverse downstream consequence. `S5` means that governance-relevant behaviour, a control failure, or a successful invariant was materially observed under bounded conditions while the preserved evidence establishes no adverse downstream harm, loss, disruption, rights impact, service impairment, or other external consequence.

This closes the gap between:

- `S4`, which requires at least minor materialised adverse consequence; and
- `SU`, which is reserved for cases where the evidence cannot support a defensible severity band.

Capability significance, taxonomy importance and hypothetical worst-case impact do not move an S5 occurrence into S1–S4.

## Reconciled controlled-evaluation Incidents

The following records previously used S4 because the evaluation behaviour itself had materially occurred, despite the records also stating that no external harm materialised:

- `VIGIL-INC-000093`
- `VIGIL-INC-000122`
- `VIGIL-INC-000123`
- `VIGIL-INC-000124`
- `VIGIL-INC-000125`
- `VIGIL-INC-000126`

All six are reconciled to S5. This is a severity-only change for INC-000093 and INC-000122 through INC-000125 and does not change their taxonomy failure classifications.

## Successful-invariant classification relationship

A canonical class relationship and failure evidence are not the same thing.

`taxonomy_classification.classification_role` now distinguishes:

- `failure-occurrence`: the Incident evidences the failure mechanism; and
- `successful-invariant`: the Incident is attached to the relevant Failure Class because it demonstrates the governing invariant holding under relevant failure pressure.

`VIGIL-INC-000126` is therefore classified in relation to `VIGIL-FC-000073 — Protected Governance Dissent Suppression` with `classification_role = successful-invariant`. It is not failure evidence. The same Incident is already attached to FC-000073 through the taxonomy's admitted `invariant_exemplars` entry, and validation requires the two sides to agree.

Generated failure-case examples exclude successful-invariant relationships.

## Boundary

This reconciliation does not:

- lower the governance significance of controlled evaluation failures;
- infer real-world prevalence or downstream harm from simulated behaviour;
- treat a successful invariant as a failure;
- create additional exemplar roles; or
- alter the substantive FC-000073 invariant or the occurrence facts of INC-000126.
