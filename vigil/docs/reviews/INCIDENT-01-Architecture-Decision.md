# INCIDENT-01 Architecture Decision

**Status:** pilot stabilisation
**Baseline:** `fc0f53df8de476a74e5ebfb536ed77e215121880`
**Branch:** `agent/incident-registry-migration`
**Date:** 2026-08-30

## Decision

VIGIL admits `incident` as a first-class public record type with immutable, year-independent identities in the form `VIGIL-INC-NNNNNN`.

An Incident represents a bounded historical occurrence. It preserves:

- a plain-English historical event title and event-date precision;
- the factual account and evidence limitations;
- all incident-specific source evidence and discovery provenance;
- VIGIL's governed interpretation and CAM significance;
- preferred substantive evidence without deleting earlier sources;
- external incident-registry cross-references;
- zero or one primary Failure Class plus zero or more secondary Failure Classes;
- classification state independently of Incident existence; and
- legacy FM/OBS evidence, analysis and review provenance.

Failure Families and Failure Classes remain the authoritative reusable semantic taxonomy. There is no new schema combining taxonomy definitions with Incident records, and Incident records do not reproduce canonical Failure Class definitions.

## Classification state

Incident taxonomy classification uses `unclassified`, `provisionally-classified`, `classified`, `classification-disputed`, and `requires-human-review`.

`unclassified` and `requires-human-review` assert no primary or secondary class. Other states require one primary mapping; each primary or secondary mapping carries its own basis and confidence.

The Hanover Institute pilot (`VIGIL-INC-000002`) proves the boundary: its occurrence and evidence are sufficient for Incident identity while Failure Class reconciliation remains deliberately unresolved.

## Dual-dataset stabilisation

The migration initially publishes:

```text
INC + legacy FM + legacy OBS + RESEARCH
```

No FM or OBS source record is deleted or rewritten by the pilot. The complete disposition crosswalk is generated at `vigil/migrations/incident-registry/VIGIL.FM-OBS-to-INC.Crosswalk.json` from `Incident.Migration.Decisions.json`.

The crosswalk supports one-to-one, one-to-many, partial, non-incident and human-review dispositions, and accounts separately for every legacy source entry.

## Evidence authority

`source_records` remains the canonical evidence block. `preferred_evidence` points to one preserved source URL and records why it is presently preferred. It never removes earlier reporting and never implies that the earliest source is primary.

External incident databases remain cross-references rather than VIGIL identity authorities. Their registry name, identifier, URL, relationship and review date are structured under `external_incident_references`.

## Pilot scope

The eight-record pilot exercises one FM to one Incident, one OBS to an unclassified Incident, many legacy FMs consolidated into one historical Incident with multiple class mappings, mixed controlled research and distinct incidents disentangled without manufacturing a research Incident, one FM decomposed into four named-person incidents, and one OBS expressly retained as non-incident.

Bulk migration is not authorised by source count or record type. Remaining semantic decisions stay explicit as `requires-human-review` until reviewed.

## Retirement boundary

This tranche does not retire FM or OBS, cut over taxonomy-book Case Studies, alter catalogue routing, collapse Failure Classes, or modify Caelestis. Those steps require a later reviewed migration state and proof that evidence and VIGIL interpretation have not been lost.
