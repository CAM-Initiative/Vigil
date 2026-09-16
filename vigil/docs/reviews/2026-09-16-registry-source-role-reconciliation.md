# Registry source-role reconciliation

**Date:** 2026-09-16  
**Scope:** Active VIGIL Incident records only

## Outcome

This review inspected all 124 active Incident records and adjudicated all 54
`incident database entry` source records across 50 Incidents. It was a bounded
semantic review, not a global conversion based on `registry-reported` status or
keywords.

- 22 source records in 18 Incidents changed from `incident-evidence` to
  `record-cross-reference`.
- 32 source records in 32 Incidents deliberately remain `incident-evidence`.
- No case remains ambiguous or requires further human adjudication.
- No source record, registry identifier, or external registry relationship was
  removed.
- Preferred-evidence selections and `external_incident_references` remain
  intact.

For the 22 reclassified sources, matching Harm Impact Matrix `evidence_refs`
were removed because cross-reference sources no longer claim to substantiate a
harm band. No harm dimension, band, basis, threshold, overall severity, or
other Harm Impact Matrix adjudication changed.

## Changed records

| Incident | Registry source(s) | Rationale |
| --- | --- | --- |
| VIGIL-INC-000003 | AI Incident Database | The separately reviewed provider and affected-party sources establish the Incident facts; AIID supplies a durable registry locator and traceability. |
| VIGIL-INC-000004 | AI Incident Database | AIID supplies registry identity and metadata; Gambit is the substantive source. |
| VIGIL-INC-000055 | OECD.AI | The entry is used for discovery and cross-registry traceability; Reuters supplies the substantive reporting. |
| VIGIL-INC-000060 | AI Incident Database; AIAAIC | Both entries support identity, discoverability, and reconciliation; the UK AI Security Institute source is primary evidence. |
| VIGIL-INC-000063 | AIAAIC | The registry entry is bounded corroborative metadata and traceability; The Guardian is the preferred substantive source. |
| VIGIL-INC-000070 | AIAAIC | The entry is a secondary registry cross-reference; 404 Media supplies the substantive reporting. |
| VIGIL-INC-000082 | AI Incident Database | The entry supports identity and report aggregation; ABC News and WLRN supply the substantive evidence. |
| VIGIL-INC-000083 | AI Incident Database | The entry links a narrower event for registry reconciliation; ASIC supplies the substantive evidence. |
| VIGIL-INC-000084 | AI Incident Database; OECD.AI | The entries provide same-incident and broader registry links; Anthropic's disclosure supplies the substantive evidence. |
| VIGIL-INC-000085 | AI Incident Database; OECD.AI | The entries provide registry reconciliation and traceability; Anthropic's disclosure supplies the substantive evidence. |
| VIGIL-INC-000086 | AI Incident Database; OECD.AI | The entries provide registry reconciliation and traceability; Anthropic's disclosure supplies the substantive evidence. |
| VIGIL-INC-000092 | AI Incident Database | The entry supports reconciliation only; the separately reviewed reporting preserves the evidentiary boundary. |
| VIGIL-INC-000097 | AI Incident Database | The entry is retained for registry reconciliation; the separately reviewed reporting supplies the Incident evidence. |
| VIGIL-INC-000098 | AI Incident Database | The entry is retained for registry reconciliation; Google and Reuters supply the substantive evidence. |
| VIGIL-INC-000099 | AI Incident Database | The entry is retained for cluster reconciliation; Reuters supplies the substantive evidence. |
| VIGIL-INC-000100 | AI Incident Database | The entry is retained for registry reconciliation; the separately reviewed reporting supplies the substantive evidence. |
| VIGIL-INC-000119 | OECD.AI | The entry is used for discovery and traceability; Nx, GitGuardian, and Wiz supply the substantive technical evidence. |
| VIGIL-INC-000127 | OECD.AI | The entry is used only for discovery and cross-registry traceability; GreyNoise remains primary/preferred evidence and PaperCut remains affected-party corroboration. |

## Registry sources retained as Incident evidence

The following 32 records retain an incident-database source as
`incident-evidence` because the registry entry itself materially contributes to
the factual basis:

- **Sole or preferred source supplying bounded occurrence facts:**
  VIGIL-INC-000001, VIGIL-INC-000005, VIGIL-INC-000006,
  VIGIL-INC-000007, VIGIL-INC-000008, VIGIL-INC-000013,
  VIGIL-INC-000029, VIGIL-INC-000030, VIGIL-INC-000041,
  VIGIL-INC-000043, VIGIL-INC-000044, VIGIL-INC-000047,
  VIGIL-INC-000048, VIGIL-INC-000049, VIGIL-INC-000050,
  VIGIL-INC-000051, VIGIL-INC-000052, VIGIL-INC-000053,
  VIGIL-INC-000054, VIGIL-INC-000058, VIGIL-INC-000061,
  VIGIL-INC-000065, VIGIL-INC-000067, VIGIL-INC-000068,
  VIGIL-INC-000069, and VIGIL-INC-000077.
- **Material bounded proposition alongside other sources:**
  VIGIL-INC-000002, VIGIL-INC-000040, VIGIL-INC-000057, and
  VIGIL-INC-000074.
- **Substantive source text preserved and relied upon by the record:**
  VIGIL-INC-000103 and VIGIL-INC-000104. The registry source in
  VIGIL-INC-000104 remains preferred evidence.

This retention confirms that neither `source_type = incident database entry`
nor `evidence_status = registry-reported` determines source role by itself.

## INC-127 and public projection checks

VIGIL-INC-000127 now expresses its hierarchy directly in structured data:

- GreyNoise: `incident-evidence` and preferred evidence;
- PaperCut: `affected-party-evidence`;
- OECD.AI: `record-cross-reference`, still `registry-reported` and still linked
  through `external_incident_references` as the same Incident.

The lightweight public Incident index now exposes sorted unique `source_roles`
derived from canonical source records. This allows catalogue consumers to
distinguish substantive evidence from contextual and cross-reference material
without copying full source records into the index.

