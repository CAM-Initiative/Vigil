# INCIDENT-01 Architecture Decision

**Status:** majority-migration stabilisation
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

The Hanover Institute Incident (`VIGIL-INC-000002`) proves the boundary: its occurrence and evidence are sufficient for Incident identity while Failure Class reconciliation remains deliberately unresolved.

## Dual-dataset stabilisation

The migration initially publishes:

```text
INC + legacy FM + legacy OBS + RESEARCH
```

No FM or OBS source record is deleted or rewritten by the migration. The complete disposition crosswalk is generated at `vigil/migrations/incident-registry/VIGIL.FM-OBS-to-INC.Crosswalk.json` from `Incident.Migration.Decisions.json`.

The crosswalk supports one-to-one, one-to-many, partial, non-incident and human-review dispositions, and accounts separately for every legacy source entry.

The deterministic migration rebuild order is:

```bash
python vigil/scripts/build-incident-registry.py
python vigil/scripts/build-incident-migration-decisions.py
python vigil/scripts/build-incident-migration-crosswalk.py
python vigil/scripts/validate-incident-migration.py
```

## Evidence authority

`source_records` remains the canonical evidence block. `preferred_evidence` points to one preserved source URL and records why it is presently preferred. It never removes earlier reporting and never implies that the earliest source is primary.

External incident databases remain cross-references rather than VIGIL identity authorities. Their registry name, identifier, URL, relationship and review date are structured under `external_incident_references`.

## Majority-migration scope

The original eight-record pilot established the schema and migration mechanics. The
majority pass now contains 78 Incidents and explicit semantic decisions for all 106
legacy records and 348 source entries. It exercises one-to-one migration,
cross-record source clustering, multi-Incident decomposition, multiple Failure Class
mappings, research/non-Incident dispositions, and deliberately unresolved Incident
classification.

Migration is never inferred from source count or record type. Human review is retained
only for eleven genuinely ambiguous record boundaries and three isolated sources
inside otherwise assessed records.

The taxonomy publication has now been cut over to the Incident-backed Case File
projection. Classified and provisionally classified Incidents supply publication Case
Studies; unclassified Incidents remain valid registry records without being forced into
a Failure Class solely for publication coverage.

## Retirement boundary

This tranche does not retire FM or OBS, alter catalogue routing, collapse Failure Classes, or modify Caelestis. Legacy FM/OBS retirement, redirects and catalogue routing remain later reviewed steps that require proof that evidence and VIGIL interpretation have not been lost. The taxonomy-book Case Study cutover is already implemented on this branch and does not imply retirement of the retained legacy datasets.
