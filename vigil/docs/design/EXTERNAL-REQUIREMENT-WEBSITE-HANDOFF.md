# External requirement website handoff

Artefact type: REVIEW. Downstream implementation contract, 4 October 2026.

Target repository: `CAM-Initiative/cam-governance-catalogue`.

The occurrence-assessment schema is stable. Independent external-requirement review is complete for all 170 active Incidents. Canonical, occurrence-assessment and public-projection validation pass. The completion audit records the preserved evidence and checks. A separate pre-existing taxonomy role-ledger inconsistency remains documented; this handoff does not implement the website.

## Data authority

Read `external_requirement_assessments` from each canonical Incident. The lightweight Incident index contains navigation and search projections, including an assessment count. It is not the source of complete assessment rows.

Resolve each `requirement_id` through the canonical external-requirement dataset. Use its requirement proposition, source identity, clause or control, and `normative_force`. Normative force belongs to the requirement metadata. It is not duplicated in the Incident and does not select the assessment result.

| Incident field | Consumer use |
| --- | --- |
| `requirement_id` | Resolve the external requirement and its governance source. |
| `alignment_result` | Render the assessment chip using the exact mapping below. |
| `assessment_basis` | Render the occurrence-specific evidence explanation. |
| `assessed_on` | Preserve the assessment date. |
| `source_record_refs` | Resolve evidence through the current Case File reference trail. |
| `derived_from_class_ids` and `source_clause_indices` | Optional explanation of the candidate's clause derivation. These fields do not determine its result. |
| `identification_basis` | Alternative explanation of independent requirement identification. It does not determine the result. |

| Machine value | Public label |
| --- | --- |
| `aligned` | Aligned |
| `not-aligned` | Not aligned |
| `boundary` | Boundary |

## Case File presentation

Use four columns in the Compliance assessment table:

1. Assessment result
2. External requirement
3. Normative force
4. Evidence / assessment basis

Link the requirement to the internal VIGIL standards or governance-source page where a route exists. Preserve the canonical source and clause context. Resolve `source_records[N]` references against that Incident's source array and link to its evidence trail. Do not place raw occurrence-source URLs throughout the assessment table.

Display normative force separately. The current metadata values are `government-voluntary-framework`, `voluntary-consensus-standard`, `binding-law`, `voluntary-technical-specification` and `industry-framework`. Labels can be human-readable, but their meaning must remain distinct from Aligned / Not aligned / Boundary. A voluntary source can receive any of the three assessment results.

A Boundary row represents a genuinely relevant requirement with a missing decisive occurrence fact. Its assessment basis names that fact. It is not a substitute for candidate relevance screening, proof of adoption or certification.

An absent or empty assessment array means there are no published occurrence assessments in that record. Do not infer Aligned, organisation-wide compliance or absence of governance risk. Do not generate rows from contextual `standards_and_regulatory_references`, taxonomy mappings or relationship-registry candidates.

## Retired presentation

Remove dependence on `applicability_status`, `applicability_basis`, `finding` and `finding_basis` for migrated assessment rows. Do not automatically translate historical values into current results. All active Incidents have completed independent review in VIGIL; historical audit values remain evidence of the earlier states.

Candidate exclusions are retained in dated repository audits. They are not canonical public assessment rows. Do not make primary tables of Not applicable or Applicability unresolved candidates. Do not restore a global Incident-by-requirement matrix.

Keep third-party `external_assessments` and their classifications separate from VIGIL's own requirement assessments. Preserve the external assessor's labels and citations. Keep the Alignment Taxonomy, Harm Impact and contextual standards references on their respective surfaces.

## Downstream acceptance checks

- Render all three machine values with the exact public labels.
- Resolve normative force and requirement text from central metadata.
- Resolve occurrence evidence within the correct Case File.
- Render only canonical retained rows, including relevant Boundary rows.
- Preserve assessment dates and the complete assessment basis.
- Handle zero-row Incidents without a positive compliance claim.
- Do not infer external polarity from a Fidelity Class role.
- Do not use voluntary adoption or certification as a display gate.
- Keep third-party assessments and candidate audits separate.
- Verify that no retired assessment fields control chips, filters, counts or exports.
- Verify print and PDF views against the same field and label mapping.

The governing contracts are `vigil/VIGIL.Schema.json`, `vigil/docs/maintenance/EXTERNAL-REQUIREMENT-ADJUDICATION.md` and `vigil/docs/maintenance/PUBLIC-OUTPUT-STYLE.md`. The dated corpus progress audit records migration readiness.
