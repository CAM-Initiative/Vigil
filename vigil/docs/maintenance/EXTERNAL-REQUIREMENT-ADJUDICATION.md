# External Requirement Adjudication

Status: occurrence-level alignment contract, 3 October 2026.

## Analytical sequence

Source evidence → material clause → reviewed FC ↔ EXTREQ relationship or independent identification → candidate → genuine occurrence relevance → independent alignment assessment.

Taxonomy and external requirements share the same substantive alignment concept: a successful invariant is Aligned, a failure occurrence is Not aligned, and an unresolved evidentiary boundary is Boundary. Assess each external proposition independently. No taxonomy result selects an external result.

## Candidate resolution and relevance

Use `python vigil/scripts/resolve_clause_external_requirements.py <canonical-incident.json> --clause-index <zero-based-index>`. The resolver reads supported direct and strong-supporting relationships from the reviewed registry. Its disposable output identifies candidates only. Do not restore the retired global candidate matrix or create a Cartesian product. Independently identified requirements remain permitted with a substantive identification basis.

Read the actual canonical requirement before deciding relevance. Wrong actor, system type, subject, lifecycle, occurrence date, commencement, jurisdiction, absent technical precondition, or overly broad correspondence can exclude a candidate. Preserve that decision in a dated audit; excluded candidates do not populate canonical assessments. A reviewed relationship alone establishes neither occurrence relevance nor alignment.

Formal adoption, certification, implementation claims and conformance undertakings are not prerequisites for assessing voluntary standards. Retain real technical and contextual conditions; do not disguise an adoption gate as a missing technical precondition.

## Canonical assessment

`external_requirement_assessments` is optional and contains only materially relevant occurrence assessments. Each entry requires:

- `requirement_id`: resolving canonical EXTREQ identifier;
- `alignment_result`: `aligned`, `not-aligned`, or `boundary`;
- `assessment_basis`: concise occurrence-specific relevance and evidence rationale;
- `assessed_on`: review date;
- `source_record_refs`: resolving `source_records[N]` evidence references.

Taxonomy derivation uses `derived_from_class_ids` and `source_clause_indices` identifying actual clause mappings and admitted relationships. Independent identification uses a substantive `identification_basis`. Neither route determines polarity.

Aligned needs affirmative evidence that the requirement held. Not aligned needs evidence that its proposition did not hold. Boundary requires both material relevance and an unresolved decisive occurrence fact. Absence of reported failure is not success; missing success evidence is not failure. Voluntary status, unknown adoption, unknown certification, and a weak candidate are not Boundary reasons.

`applicability_status`, `applicability_basis`, `finding`, and `finding_basis` are retired from canonical assessments. There is no dual legacy polarity or automatic conversion. During the dated migration, untouched legacy records fail the new contract until individually reviewed; this is an explicit incomplete migration state, not backward compatibility or permission to mechanically rewrite them.

## Normative force and public presentation

Resolve `normative_force` from the canonical requirement/source metadata. Do not duplicate it in Incidents or use it to select alignment polarity. Current canonical values include `government-voluntary-framework`, `voluntary-consensus-standard`, `binding-law`, `voluntary-technical-specification`, and `industry-framework`. Retain source-specific dates, legal commencement and jurisdiction conditions. An occurrence-level alignment finding does not assert certification, legal liability or organisation-wide compliance.

Section 04 Compliance consumes Assessment result / External requirement / Normative force / Evidence and assessment basis. Chips are Aligned / Not aligned / Boundary. Candidate exclusions remain audit-only. The website migration is a separate downstream change.

## Evidence, history and validation

Preserve `source_records`, source clauses, taxonomy, Harm Impact, uncertainty and append-only interpretive provenance. `external_assessments` remains third-party analysis and `standards_and_regulatory_references` remains contextual.

For each Incident, recover current assessments and prior dated candidate reviews, read requirement propositions, record relevance and independent evidence dispositions, update only reviewed entries, append provenance, and validate. No retained-count target applies. Preserve prior values through immutable baseline Git references and existing audits; new dated audits record candidates, old/new results, reasons, resolving evidence and validation. Do not rewrite historical audits.

Run `validate-occurrence-requirement-assessments.py`, the canonical/public/provenance validators and the assessment/resolver/projection tests. Structural validation checks canonical IDs, evidence, admitted derivation and alignment fields. Semantic relevance, evidence sufficiency and independence remain substantive adjudication decisions; a validator cannot prove them from a label or rationale string. Builders own generated indexes and must not mutate governed source records.
