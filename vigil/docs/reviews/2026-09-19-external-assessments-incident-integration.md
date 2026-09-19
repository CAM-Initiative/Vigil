# External Assessments Incident Integration Review

## Review identity

- Execution date: 2026-09-19
- Working branch: `fix/ambiguous-boundary-classification-role`
- Starting remote HEAD: `66fa3d6c834005f9962a8826c6f87b1b592f84b7`
- Canonical Incidents reviewed for existing assessment-bearing sources: 145

## Schema decision

`external_assessments` is an optional Incident-level array with an empty-array default. It preserves attributable analytical positions about an occurrence without turning those positions into Incident facts, Harm Impact evidence, VIGIL taxonomy evidence or VIGIL adjudication.

Each admitted assessment requires a stable VIGIL-owned ID, assessor, title, publication date and URL, controlled assessment type, controlled relationship to the Incident, neutral summary and VIGIL review date. Optional scope, external classification or rating, comparison, publication, version, status, supersession and source-link fields are admitted only when they carry a distinct semantic purpose.

Assessment IDs use `VIGIL-EXTASSESS-NNNNNN` and are unique across the canonical corpus. `source_record_refs` resolve to canonical `source_records[N]` entries rather than duplicating bibliographic metadata. Supersession links resolve to another admitted assessment ID and cannot self-reference.

## Information boundaries

- `source_records` remains the canonical evidence and bibliography layer for what happened and for materialised harm.
- `external_assessments` records what an identifiable external evaluator concluded, using that evaluator's scope and terminology.
- `external_incident_references` remains the cross-registry identity/linkage layer and is not repurposed.
- `vigil_assessment`, `taxonomy_classification` and `harm_impact_assessment` remain VIGIL's own governed analysis.
- Inclusion of an external assessment does not imply endorsement and does not automatically alter any VIGIL conclusion.

## Initial tranche

| Assessment ID | Incident | Assessor | Type | Relationship | Source linkage |
| --- | --- | --- | --- | --- | --- |
| `VIGIL-EXTASSESS-000001` | `VIGIL-INC-000129` | OpenAI | provider analysis | broader cluster | `source_records[0]`, `source_records[1]` |
| `VIGIL-EXTASSESS-000002` | `VIGIL-INC-000003` | METR and Redwood Research | independent evaluation | same occurrence | `source_records[5]` |

For INC-000129, OpenAI's broader misalignment and self-generated jailbreak-like instruction framing remains attributable to OpenAI. VIGIL's separate analysis of representation fidelity and downstream identity/authority adoption remains unchanged.

For INC-000003, the independent METR/Redwood investigation is admitted because it contains explicit behavioural and evaluative conclusions about the same occurrence, not merely a mention or registry link.

## Bounded discovery result

All 145 active Incident records were scanned for existing research papers, technical analyses, technical reports, investigation reports, government reports and legal decisions, then screened against the admission criteria. Most such sources are occurrence evidence, affected-party evidence, technical reporting or an originating study rather than a separately useful external assessment object. They were not mechanically converted.

Potential future candidates include formal court findings and evaluation reports already preserved in several records. They require a record-specific scope and date review before admission. Ordinary news coverage, regulator notices without a conclusion and registry duplicates without substantive analysis were excluded.

## Point-in-time treatment

Assessments are append-only when an evaluator materially changes its position. Historical entries may be marked `superseded`, `withdrawn` or `historical`; a later entry may identify the earlier VIGIL assessment ID through `supersedes_assessment_id`. Earlier positions are not silently rewritten.

## Public projection

The generated Incident index now carries structured `external_assessments` arrays, including empty arrays, and includes assessment terms in deterministic search vocabulary. The projection preserves the assessor, title, date, URL, type, relationship, summary, scope, external classification/rating and VIGIL comparison without flattening them into one string.

## Validation and tests

The canonical validator enforces required fields, stable IDs, ISO dates, HTTP(S) URLs, controlled type/relationship/status values, source-reference resolution, rating structure, corpus-wide ID uniqueness and supersession resolution. Regression tests cover valid empty arrays, invalid types, duplicate IDs, invalid source references, public projection, taxonomy independence and Harm Impact independence.

Generated outputs refreshed:

- `vigil/VIGIL.Incidents.Index.json`
- `vigil/VIGIL.Registry.Index.json`
- `vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json`

Validation completed on 2026-09-19:

- `python vigil/scripts/build-vigil-public-records.py`
- `python vigil/scripts/validate-vigil-records.py`
- `python vigil/scripts/validate-vigil-public-records.py`
- `python vigil/scripts/validate-vigil-source-provenance.py`
- `python vigil/scripts/validate-vigil-interpretive-provenance.py`
- `python vigil/scripts/validate-authorship-provenance.py`
- relevant Incident, pipeline-state and taxonomy tests required by repository guidance

## Known gaps

The initial tranche is deliberately conservative. The absence of an admitted object does not establish that no credible external assessment exists. Later additions should be made only after confirming occurrence identity, scope, publication date, stable source access and a neutrally summarised analytical conclusion.
