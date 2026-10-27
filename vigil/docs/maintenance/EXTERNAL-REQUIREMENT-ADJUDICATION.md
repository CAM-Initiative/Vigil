# External Requirement Adjudication

Status: occurrence-level alignment contract; maintainer crosswalk correction approved 27 October 2026. Schema, blocking validation and retrospective multi-record repair require separate maintainer gates.

## Analytical sequence

Source evidence → material source clause → independently justified canonical Fidelity Class (FC) mapping → reviewed FC ↔ EXTREQ relationship → requirement candidate → genuine occurrence relevance → independently evidenced external alignment assessment. Independent discovery may propose candidates, but cannot admit a final assessment without a supported canonical FC and source-clause mapping.

Taxonomy and external requirements share the same substantive alignment concept: a successful invariant is Aligned, a failure occurrence is Not aligned, and an unresolved evidentiary boundary is Boundary. Assess each external proposition independently. No taxonomy result selects an external result.

## Candidate resolution and relevance

Use `python vigil/scripts/resolve_clause_external_requirements.py <canonical-incident.json> --clause-index <zero-based-index>`. The resolver reads supported direct and strong-supporting relationships from the reviewed registry. Its disposable output identifies candidates only. Do not restore the retired global candidate matrix or create a Cartesian product. Independent discovery remains permitted for **candidate discovery and review only**; it is not an alternative canonical admission route. An admitted `external_requirement_assessments[]` entry must trace to a real canonical FC mapping on a supporting source clause/episode, as well as an adequately reviewed FC ↔ EXTREQ relationship. Reject thematic or guessed links. Do not force a Fidelity Class to legitimise a requirement, or infer a requirement's Aligned/Not aligned/Boundary polarity from a mapping's role.

Read the actual canonical requirement before deciding relevance. Wrong actor, system type, subject, lifecycle, occurrence date, commencement, jurisdiction, absent technical precondition, or overly broad correspondence can exclude a candidate. Preserve that decision in a dated audit; excluded candidates do not populate canonical assessments. A reviewed relationship alone establishes neither occurrence relevance nor alignment.

Formal adoption, certification, implementation claims and conformance undertakings are not prerequisites for assessing voluntary standards. Retain real technical and contextual conditions; do not disguise an adoption gate as a missing technical precondition.

## Canonical assessment

`external_requirement_assessments` is optional and contains only materially relevant occurrence assessments. Each entry requires:

- `requirement_id`: resolving canonical EXTREQ identifier;
- `alignment_result`: `aligned`, `not-aligned`, or `boundary`;
- `assessment_basis`: concise occurrence-specific relevance and evidence rationale;
- `assessed_on`: review date;
- `source_record_refs`: resolving `source_records[N]` evidence references.

An admitted assessment must use `derived_from_class_ids` to identify the actually supported canonical Fidelity Class mapping(s), and `source_episode_refs` or appropriate legacy `source_clause_indices` to identify the matching material clause(s). Those mappings and an applicable reviewed FC ↔ EXTREQ relationship must be real and evidence-supported; source-record references remain required. `identification_basis` may record how a requirement candidate was discovered, but never substitutes for canonical FC evidence. External alignment polarity is decided independently against the exact external proposition; it is not inherited from taxonomy polarity.

If the source establishes a material governance property for which the current taxonomy has no defensible mapping, classify the relevant source clause as `taxonomy-gap` (or preserve a genuinely unresolved existing-class recognition condition as `unresolved`). Preserve the potential external requirement, its source evidence and substantive analysis in a dated review/hold record rather than admitting an unlinked Aligned/Not aligned/Boundary claim to the canonical Section 04 assessment. A successful later repair does not supply the class mapping for an earlier loss. Pre-existing unlinked published rows require a measured read-only audit and Gate 2 human approval before any mass correction, deletion or movement. Do not erase adverse evidence or historical decisions.

Aligned needs affirmative evidence that the requirement held. Not aligned needs evidence that its proposition did not hold. Boundary requires both material relevance and an unresolved decisive occurrence fact. Absence of reported failure is not success; missing success evidence is not failure. Voluntary status, unknown adoption, unknown certification, and a weak candidate are not Boundary reasons.

`applicability_status`, `applicability_basis`, `finding`, and `finding_basis` are retired from canonical assessments. There is no dual legacy polarity or automatic conversion. During the dated migration, untouched legacy records fail the new contract until individually reviewed; this is an explicit incomplete migration state, not backward compatibility or permission to mechanically rewrite them.

## Normative force and public presentation

Resolve `normative_force` from the canonical requirement/source metadata. Do not duplicate it in Incidents or use it to select alignment polarity. Current canonical values include `government-voluntary-framework`, `voluntary-consensus-standard`, `binding-law`, `voluntary-technical-specification`, and `industry-framework`. Retain source-specific dates, legal commencement and jurisdiction conditions. An occurrence-level alignment finding does not assert certification, legal liability or organisation-wide compliance.

Section 04 Compliance consumes Assessment result / External requirement / Normative force / Evidence and assessment basis. Chips are Aligned / Not aligned / Boundary. Candidate exclusions remain audit-only. The website migration is a separate downstream change.

Public wording for these fields follows `vigil/docs/maintenance/PUBLIC-OUTPUT-STYLE.md`. Use **Aligned**, **Not aligned** and **Boundary** consistently on public surfaces. Do not reintroduce `met`, `not met`, `applicability unresolved`, `insufficient evidence` or similar legacy labels as presentation synonyms. Keep the result separate from normative force, and state the occurrence evidence in direct language rather than generic hedging.

## Evidence, history and validation

Preserve `source_records`, source clauses, taxonomy, Harm Impact, uncertainty and append-only interpretive provenance. `external_assessments` remains third-party analysis and `standards_and_regulatory_references` remains contextual.

For each Incident, recover current assessments and prior dated candidate reviews, read requirement propositions, record relevance and independent evidence dispositions, update only reviewed entries, append provenance, and validate. No retained-count target applies. Preserve prior values through immutable baseline Git references and existing audits; new dated audits record candidates, old/new results, reasons, resolving evidence and validation. Do not rewrite historical audits.

Run `validate-occurrence-requirement-assessments.py`, the canonical/public/provenance validators and the assessment/resolver/projection tests. Structural validation checks canonical IDs, evidence, admitted derivation and alignment fields. Semantic relevance, evidence sufficiency and independence remain substantive adjudication decisions; a validator cannot prove them from a label or rationale string. Builders own generated indexes and must not mutate governed source records.


## Complete-explanation duplication control

Each retained assessment must explain its own canonical proposition against the occurrence evidence. Reusing an identical complete `assessment_basis` for different requirement IDs within one Incident is a blocking boilerplate error. The shared occurrence-requirement validator compares complete values after Unicode NFKC, case and whitespace normalisation. It reports all participating rows and requirement IDs.

Shared factual sentences are permitted when the rest of each explanation addresses its own requirement. Do not clear the error by adding an identifier, row number or cosmetic synonym. Compare the actual required activity, evidence and missing decisive fact. Preserve legitimate uncertainty and common evidence. This check does not compare evidence quotations, shared taxonomy conditions or historical review entries, and it cannot certify semantic adequacy or detect paraphrased boilerplate.

The control and the measured affected-record repairs were explicitly approved together under Gate 1 and Gate 2 on 18 October 2026. Implementation evidence and per-record decisions are in `../reviews/2026-10-18-duplicate-explanation-repairs/`.
