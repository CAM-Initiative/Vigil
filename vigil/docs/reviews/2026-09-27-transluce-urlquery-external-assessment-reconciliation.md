# Transluce urlquery external-assessment reconciliation — 2026-09-27

## Scope

This review reconciles Transluce's 23 September 2026 publication *Early rogue AI agent activity and attempts to hack found on urlquery.net* against the active VIGIL Incident corpus.

The publication describes three bounded attempted-compromise occurrences already represented as separate VIGIL Incidents:

- VIGIL-INC-000161 — University of New Mexico Digital Library;
- VIGIL-INC-000172 — Australian Institute of Health and Welfare;
- VIGIL-INC-000175 — Data USA.

The review does not assume agreement with Transluce's interpretation. External assessments preserve the assessor's attributable analytical position; VIGIL taxonomy adjudication remains independent.

## Reconciliation

Each of the three Incidents already preserved the Transluce publication as canonical occurrence evidence in `source_records[0]`, but had no structured `external_assessments` entry.

This pass adds one incident-specific Transluce technical assessment to each record:

- `VIGIL-EXTASSESS-000067` — VIGIL-INC-000161;
- `VIGIL-EXTASSESS-000068` — VIGIL-INC-000172;
- `VIGIL-EXTASSESS-000069` — VIGIL-INC-000175.

All three use `relationship_to_incident: same-occurrence` and `assessment_type: technical-analysis`. Their scope notes, summaries and VIGIL comparison notes are occurrence-specific rather than copied across the cluster.

No Transluce assessment is added to VIGIL-INC-000174 (BOCSAR): the 23 September Transluce publication does not provide a corresponding BOCSAR-specific technical case section, and the canonical record already preserves that boundary.

## Data/log release boundary

Transluce also publishes a downloadable urlquery data archive and links numerous underlying urlquery records. Those artefacts are evidence, not analytical positions, and therefore are not represented as additional `external_assessments`.

The archive itself was not directly inspected in this pass. No claim of direct review of the complete released log corpus is made.

If occurrence-specific logs are admitted after direct review, they should be represented through the Incident evidence/artefact layer (for example `source_records` where relied upon as canonical evidence, or `incident_artefacts` with `artefact_type: log` for occurrence-specific source artefacts) rather than being mislabeled as external assessments.

## Broader-corpus boundary

The Transluce publication describes additional urlquery activity outside the three bounded attempted-compromise cases, including earlier March 2026 data-retrieval activity and a broader March–September corpus. This pass does not convert those log clusters into new VIGIL Incidents. Admission requires the normal incident-ingestion workflow and evidentiary minimums.

## Generated outputs

Only canonical Incident records are changed in this reconciliation. The repository's deterministic public-record builder projects structured `external_assessments` into generated indexes. Generated outputs should be refreshed by the normal build workflow when this branch is tested/merged; they are not manually edited.
