# INCIDENT-01 Majority Migration Coverage Report

**Date:** 2026-08-30
**Migration state:** majority-migration stabilisation

## Inventory and outcome

| Surface | Count |
|---|---:|
| Legacy FM records retained | 74 |
| Legacy OBS records retained | 32 |
| Legacy records with explicit decisions | 106 |
| Legacy source entries with explicit dispositions | 348 |
| Incident records | 78 |
| Legacy records requiring human review | 11 |
| Additional sources requiring human review inside otherwise assessed records | 3 |

No legacy FM or OBS record was deleted or rewritten. The eight pilot Incidents were
cleaned so their current summaries and VIGIL assessments describe the bounded event;
the original FM/OBS governance text remains unchanged under `legacy_governance_state`.

## Semantic outcomes

The tranche admits obvious single occurrences, clusters repeated sources about the
same event, and splits legacy records containing different events. Representative
results include:

- one OpenAI–Hugging Face Incident consolidating evidence and classification
  contributions previously distributed across FMs and OBS records;
- separate Incidents for the Aurora/Cursor campaign, Meta evaluation compromise and
  Affinda gym-booking exploitation rather than one broad “agent exploitation” event;
- four facial-recognition detention/arrest Incidents split from `FM-0038`;
- six distinct synthetic-authority occurrences split from `FM-0040`;
- one Incident each for the Otter.ai and Granola allegations, with primary and
  secondary mappings from `FM-0073` and `FM-0074` rather than duplicate Incidents;
- status-page and reporting sources clustered by identifiable provider outage rather
  than by generic access-failure pattern; and
- research papers, controlled security demonstrations, policy developments,
  regulatory instruments and broad product observations retained as explicit
  non-Incident dispositions.

## Unresolved records

Human review is limited to genuine boundary questions:

- the shared exploratory Live Voice session (`FM-0028`–`FM-0030`, `OBS-0011` and
  `OBS-0012`);
- the three target-specific incidents bundled in Anthropic's single `FM-0054` source;
- source-limited or causally ambiguous observations (`OBS-0003`, `OBS-0005`,
  `OBS-0021`, `OBS-0022`, and `OBS-0030`); and
- three isolated sources inside otherwise migrated records whose evidence is not yet
  sufficient to identify a bounded occurrence confidently.

`OBS-0033` remains the explicit lifecycle exemplar: `VIGIL-INC-000002` exists as an
unclassified Incident because event identity and taxonomy completion are independent.

## Evidence and reconciliation

Every migrated source retains its complete legacy evidence metadata and original
record/source position. Consolidated duplicate URLs preserve every additional legacy
origin. Every non-migrated source now carries a deterministic decision basis in the
crosswalk. Preferred evidence selection does not remove discovery chronology.

The migration validator checks all 106 record decisions and 348 source dispositions,
reciprocal legacy provenance, external registry identity uniqueness, preferred-source
integrity, Incident-title uniqueness, canonical IDs, and incident-native assessment
semantics.

## Publication cutover

The taxonomy Case File projection and Full Reference textbook now consume classified
and provisionally classified Incident records rather than legacy Failure Mode records.
This publication cutover does not retire FM/OBS data and does not force unclassified
Incidents into the taxonomy. The retained legacy datasets and migration crosswalk
remain the reconciliation authority during stabilisation.

## Deferred retirement work

FM retirement, OBS deletion, redirects and catalogue routing remain deferred.
Dual-dataset mode continues until the remaining human-review boundaries are resolved
and the registry is approved for legacy retirement. Failure Class rationalisation also
remains a separate reviewed tranche rather than an automatic consequence of migration.
