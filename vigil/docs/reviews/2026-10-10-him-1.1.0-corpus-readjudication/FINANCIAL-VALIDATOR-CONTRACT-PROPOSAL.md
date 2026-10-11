Status: **Rejected by the human maintainer on 10 October 2026. No implementation is authorised.**

No validator, schema, builder or permanent-test changes were made for this proposal. The text below is a historical audit of the observed conflict. It is not an active request for approval or implementation. The canonical INC-082 remains unchanged and held under the existing controls. Continue the remaining corpus reviews.

# Financial numerical and qualitative criterion contract — approval proposal

Status: proposed only. No validator, schema or methodology change implemented.

Authority: vigil/MAINTAINERS.md, “Human-maintainer stop conditions”, Gate 1: “No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.” Gate 2 requires a subsequent read-only corpus run and report before any newly exposed semantic repairs.

## Current behaviour

validate-vigil-records.py requires every numeric USD observation on an assessed financial row to resolve to the same arithmetic band as the row severity. It applies this even to a reported payment, partial amount or award rather than a complete realised-loss total. It does not account for HIM’s explicit proviso that S1 below US$10,000 excludes material livelihood impairment.

The held INC-082 candidate preserves a US$4,820 payment and separately evidenced rent and utility arrears. It is rejected solely because the payment is below US$10,000, even though its proposed S3 basis explicitly tests the alternative livelihood criterion. Removing the numeric observation would hide evidence and is not a permitted solution.

## Proposed behaviour for approval

Preserve strict numerical validation for the quantitative USD assessment pathway. Permit an explicitly declared, evidence-linked qualitative economic-disruption or livelihood-loss pathway to determine the financial band independently of an incidental/partial USD observation. Require the qualitative criterion, its supported functional consequence and resolvable source references to be recorded; a free assertion or missing amount alone must not permit an override. Preserve every published numeric observation.

Confirm the methodological interpretation that an unvalued material livelihood consequence can use the alternative S3 limb even where a payment is stated in USD. The payment remains numeric evidence; it does not value the full functional livelihood consequence. If that interpretation is not approved, the record must remain held rather than forcing S1 contrary to its livelihood proviso.

A narrowly scoped, optional structured financial criterion-pathway field would distinguish quantitative USD, qualitative economic disruption and qualitative livelihood/organisational loss. Its schema and validator contract would be proposed together; no heuristic would infer the pathway from prose. Existing ordinary numeric rows would continue to receive the strict current checks.

## Pass/fail delta

The evidence-linked INC-082 qualitative S3 candidate with the retained US$4,820 payment would become admissible. A claim of qualitative S3 supported only by a payment or by missing follow-up would remain inadmissible. An arbitrary S3 paired with US$4,820 and no explicit evidenced qualitative pathway would still fail. Valid ordinary quantitative rows would retain their numerical bands. No previously valid record is intended to fail merely because the optional field is absent.

## Affected surfaces

harm_impact_assessment.dimensions[] for financial-economic only: severity, threshold_id, assessment_basis, evidence_refs, observed_values and optional criterion-pathway metadata. Stage 02 Harm Impact and the derived overall severity/controlling dimensions may change after individual adjudication. Generated indexes remain deterministic. Sources, summaries, taxonomy mappings, doctrine and other dimensions are unaffected by the control change itself.

## Measured scope

Six current financial rows contain numeric USD observations: INC-047, INC-082 (held candidate), INC-114, INC-140, INC-142 and INC-146. One direct conflict has been demonstrated, INC-082. Qualitative financial assessments without USD observations require a separate read-only scope check if the proposed field becomes mandatory; this proposal keeps it optional and makes no claim that all six records need changes.

## Repair and data-loss implications

No automatic corpus migration or prose rewrite. The rule must not induce deletion of numeric values or flatten actual livelihood consequences into payment size. Source and mapping history remains preserved. A builder run follows separately accepted Incident edits. The held candidate is already concrete and reviewable, with the exact baseline frozen.

## Why validator and schema

This is a machine acceptance conflict between quantitative and explicitly evidenced qualitative criterion pathways. The renderer cannot resolve it, and more prose alone does not affect the current numeric check. A controlled field and a scoped validator rule can preserve the distinction and reject unsupported overrides. The underlying interpretation must be explicitly approved before implementation.

## Stop condition after approval

Implement the approved control semantics and meaningful isolated fixtures, then run read-only against all 183 records and report exact failures and field changes. Stop before newly exposed semantic multi-record repair. The separately authorised ongoing source-first reconciliation can continue on unaffected records, with held candidates remaining unaccepted until their guards pass.
