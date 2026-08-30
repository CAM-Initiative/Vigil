# INCIDENT-01 Pilot Coverage Report

**Date:** 2026-08-30
**Migration state:** pilot stabilisation

## Inventory

| Surface | Count |
|---|---:|
| Legacy FM records | 74 |
| Legacy OBS records | 32 |
| Legacy records with explicit crosswalk dispositions | 106 |
| Legacy source entries with explicit source dispositions | 348 |
| Pilot Incident records | 8 |
| Legacy records still requiring semantic review | 92 |

No legacy FM or OBS record was deleted.

## Pilot reconciliation

| Legacy record(s) | Decision | Successor |
|---|---|---|
| `FM-0041` | single reported occurrence | `VIGIL-INC-000001` |
| `OBS-0033` | bounded Incident; classification unresolved | `VIGIL-INC-000002` |
| ten HF-related FMs | shared OpenAI–Hugging Face occurrence; incident-specific sources deduplicated | `VIGIL-INC-000003` |
| `FM-0071` | distinct Aurora occurrence separated from HF and controlled research | `VIGIL-INC-000004` |
| `FM-0038` | four named-person occurrences | `VIGIL-INC-000005` through `VIGIL-INC-000008` |
| `OBS-0011` | broad observational/research session, not forced into Incident | no successor in pilot |

## Evidence accounting

The crosswalk records each source as migrated to a named Incident, retained in the legacy record pending disentanglement, non-incident and not migrated, or requiring semantic review.

Incident sources retain full legacy source metadata plus their original legacy record and source position. Duplicate URLs consolidated into one Incident source preserve additional legacy origins.

## Deferred work

The remaining 92 FM/OBS records require semantic assessment. Pilot state deliberately permits those dispositions; a future `reconciled` migration state will fail validation while any `requires-human-review` entries remain.

Public Case Study cutover, FM retirement, OBS deletion, redirects, catalogue routing and taxonomy textbook changes remain deferred.
