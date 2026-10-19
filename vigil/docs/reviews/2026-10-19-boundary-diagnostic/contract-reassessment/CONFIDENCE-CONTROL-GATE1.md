# Gate 1 proposal: confidence requiredness for Boundary mappings

Status: proposed; no schema, validator or permanent test edited.
Input: cf0c20a37c112188b284ba29fd42fd4dbc763201. Taxonomy: 0.7.0.

The three-record reassessment identifies a proposed new Control Effectiveness Integrity Boundary for INC-005 E003. Warrant recall and release establish an operative response; the correction-to-release interval is unknown. Its exact proposed canonical mapping and completed boundary_adjudication are in INC-000005-DECISION.json under proposed_canonical_additions. No confidence rating is proposed.

## Current behaviour

vigil/scripts/validate-vigil-records.py, validate_classification_mapping, requires classification_confidence on every mapping and permits only low, medium or high. Omitting that key from a new Boundary fails validation. The approved Boundary policy prohibits adding a rating merely for confidence that uncertainty exists; confidence applies to supported decisive findings. The current control cannot encode the proposed finding consistently with that policy.

## Exact proposed behaviour

- Require classification_confidence for failure-occurrence and successful-invariant, retaining the existing low/medium/high value check.
- Make classification_confidence optional for ambiguous-boundary. If historically present, retain its current value and validate its existing vocabulary. Do not delete or reinterpret historical confidence.
- Keep completed boundary_adjudication required on every admitted Boundary, with all current diagnostic and reference checks unchanged.
- Clarify the corresponding existing confidence documentation in VIGIL.Schema.json. Add no field, class, diagnostic reason, numerical calibration or recognition condition.

## Pass/fail delta

A complete Boundary object without classification_confidence currently fails and would pass. A decisive finding without confidence would continue to fail. An invalid confidence value, incomplete Boundary object or unresolved source/episode reference would continue to fail. No currently valid record would newly fail under this proposal.

## Scope and preservation

This is limited to taxonomy_classification primary/secondary mapping confidence requiredness. Section 03 consumes these mappings. The existing builder uses mapping.get for confidence and would emit null in its case-example projection; canonical confidence would be absent. Verify consumer fallback before admitting that new projection. No prose movement, renderer, builder, website, HIM, independent assessment or external-requirement rule changes are proposed. Existing historical Boundary ratings are preserved. The measured candidate census below has no missing historical confidence to repair; one newly proposed mapping is blocked. The control change itself does not reclassify the corpus. Admission of the specific INC-005 proposal would follow under the already authorised three-record work, with its provenance and rebuilt projections.

## Why the validator

This is an existing blocking validator requirement that contradicts the approved role-specific confidence policy. A renderer or prose change cannot make the evidence-grounded mapping valid without inventing a rating. The smallest correction is conditional requiredness at that validator, with matching contract documentation.

## Validation and stop condition

After explicit approval, verify the exact accepted/rejected behaviours with bounded disposable copies, run the existing checks and a read-only corpus census, then apply only the reviewed INC-005 mapping. Do not add record-specific regression tests or weaken the Boundary diagnostic control. Report remaining corpus failures and preserve the hold on the other 37 reviews. No new bulk repair is implied.

## Approval source

vigil/MAINTAINERS.md, “Gate 1 — approval before changing the control”, states: “No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.” The requested exception has not been applied.

Measured local candidate census: {"boundary_mappings": 91, "boundary_with_confidence": 91, "decisive_mappings": 364}
