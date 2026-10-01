# External Requirement Adjudication

Status: current clause-led maintainer methodology, 1 October 2026.

The analytical sequence is source evidence → material clause → neutral FC property → separately evidenced occurrence polarity → potentially relevant EXTREQ → independent applicability → independent requirement finding.

## Candidate resolution

Use `python vigil/scripts/resolve_clause_external_requirements.py <canonical-incident.json> --clause-index <zero-based-index>` for one adjudicated clause. The resolver reads reviewed `direct` and `strong-supporting` relationships in `external_governance/requirements/taxonomy-relationships.json`. It excludes unresolved, contextual and removed relationships. Its stdout is disposable candidate information, never a finding or canonical Incident dataset. Do not save a global Cartesian product. The former global candidate matrix and summary are retired; dated historical audits preserve their original context.

A requirement can also be identified independently from occurrence evidence. A missing taxonomy mechanism is recorded separately; it does not prevent independent applicability assessment or require creating an FC.

## Canonical assessment

`external_requirement_assessments` is optional. Each assessment identifies a canonical `requirement_id`, an occurrence-specific `applicability_basis`, `applicability_status`, `assessed_on`, and resolving `source_record_refs` using `source_records[N]`.

For taxonomy derivation, optional `derived_from_class_ids` and `source_clause_indices` must identify supported reviewed relationships on the actual canonical clause. Do not require all Incident-level mappings to be contributors. For independent identification, preserve a substantive `identification_basis` instead.

Assess actor, system/activity, time and lifecycle, jurisdiction, adoption where relevant, conditions, exclusions and normative force independently. `applicable` requires a separate `finding` and `finding_basis`: `met`, `not-met`, `evidence-insufficient`, or `not-assessable`. `insufficient-evidence` means applicability unresolved and prohibits a finding. `not-applicable` requires an affirmative scope reason and prohibits a finding. Neither taxonomy polarity nor source existence establishes applicability or compliance. An applicable recommendation retains its voluntary normative posture.

Positive requirement satisfaction needs affirmative evidence; an absence of reported failure is insufficient. Likewise, missing success evidence does not establish non-satisfaction. The basis must state the relevant bounded proposition and uncertainty. References resolve evidence but do not themselves prove its adequacy.

## Distinct surfaces

`source_records` remains the canonical evidence block. Material source clauses carry taxonomy adjudication. Conceptual taxonomy references support the property; canonical EXTREQs express source requirements; occurrence assessments address applicability and findings. `external_assessments` remains attributed third-party analysis. `standards_and_regulatory_references` remains contextual. None of these layers automatically confers authority on another.

## Validation and publication

Run `validate-occurrence-requirement-assessments.py` and `test_external_requirement_assessments.py`. The Incident validator delegates assessment integrity to this domain module. Evidence references, canonical IDs, derivation where recorded, explicit applicability and independent findings are enforced; no validator requires matrix completeness. Public indexes route to canonical records and must not become duplicate stores of substantive assessment payloads.
