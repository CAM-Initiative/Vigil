# Gate 1 proposal: evidence of completed Incident processing

Role: REVIEW. Status: proposed; no canonical field, schema, validator, test, builder or publication guard implemented. Baseline: `1e55f38276279941146d2e679f574415067d51a5`. Date: 18 October 2026.

## Current behaviour and measured impact

An Incident may have `external_requirement_assessments: []`, partial taxonomy coverage and no evidence that the ordinary processing passes occurred. Validators check supplied assessment structure and references. They cannot infer a review from an empty list. The existing authoring template is a starting point, not a completion certificate.

Read-only measurement after this bounded review: 194 active Incidents; 34 with empty external-assessment lists, 160 with assessments; 56 with partial taxonomy coverage, 138 complete; all have clauses. None has the proposed `processing_review` field. These counts describe stored structures, **not 34 missing reviews or 56 unfinished work packages**. No historical completion inference is made.

Recommendation: add an explicit review declaration for newly created Incidents, with an audit reference. Keep taxonomy coverage and review completion independent. An evidence-limited taxonomy outcome can follow a completed review.

## Exact proposed fields

Optional top-level canonical `processing_review`, required only for new IDs under the prospective scope below. No other canonical field changes:

```json
{
  "processing_review": {
    "review_id": "VIGIL-REVIEW-YYYY-MM-DD-IDENTIFIER",
    "reviewed_on": "YYYY-MM-DD",
    "reviewer": "Actual reviewer identity and AI/human role",
    "record_version": "Exact reviewed record_identity.version",
    "taxonomy_version": "Exact adjudication taxonomy version",
    "him_version": "Exact harm-assessment methodology version",
    "audit_reference": "vigil/docs/reviews/dated-package/incident-review.json",
    "stages": {
      "evidence_and_scope": "reviewed",
      "chronology_and_taxonomy": "reviewed-evidence-limited",
      "harm_impact": "reviewed",
      "public_output_and_provenance": "reviewed",
      "media": "reviewed",
      "generated_outputs_and_validation": "reviewed"
    },
    "external_requirements": {
      "status": "reviewed-none-retained",
      "reason": "Specific reviewed scope and reason",
      "blockers": []
    }
  }
}
```

All shown keys would be required when the object is present; unknown keys rejected. `stages` has exactly the six keys shown. Each takes `not-reviewed`, `reviewed`, `reviewed-evidence-limited` or `blocked`. The external status takes `not-reviewed`, `reviewed-with-assessments`, `reviewed-none-retained` or `blocked`. `reason` is nonempty for every external status. `blockers` is an array of objects with exactly nonempty `missing_source_or_fact` and `prevented_work` strings, nonempty for a blocked external pass and empty otherwise. The audit must identify the evidence limitations for every evidence-limited stage and blockers for every blocked stage.

The version fields must equal their corresponding canonical values. `review_id` must resolve to an actual append-only interpretive review entry; `reviewed_on` and reviewer must agree with it. The audit reference must resolve within the repository to the same Incident, baseline/candidate version, candidate review decisions, twelve-dimensional harm disposition and stage evidence. These checks verify declarations and referential integrity, not the truth or sufficiency of an analysis.

`reviewed-with-assessments` requires one or more canonical assessments. `reviewed-none-retained` requires zero canonical assessments and a dated candidate/independent-search audit with a substantive exclusion/scope reason. It does not require a standards gap or negative standards result. Review of no class-derived candidates can still be substantive when the independent search and scope decision are recorded.

## Prospective scope and enforcement

On approval, freeze an immutable baseline set of the existing 194 IDs in the implementation audit. Require the declaration for IDs absent from that set; do not infer age from dates or numerical order. Existing IDs remain structurally admissible without the object. If an existing Incident voluntarily supplies it after a separately authorised review, validate the declaration as supplied. No retrospective migration is authorised.

Canonical validation would reject new entries with missing declarations, `not-reviewed` or `blocked` stages, inconsistent versions/references, or inconsistent external status/list. `reviewed-evidence-limited` is permitted with the referenced specific limitation. A blocked pass means required work could not be carried out, not merely that the sources leave a decisive factual question unresolved after review. A relevant canonical requirement with missing polarity evidence can remain a Boundary assessment after an actual review.

Use the existing canonical-validation CI/publication path to prevent an unprocessed new record being accepted. Do not change Case File rendering, hide existing records, or make all historical empty lists invalid. Do not require a global Incident-by-class/requirement matrix. Documentation guides substantive work; schema enforces shape; validator enforces cross-field/version/reference consistency; referenced audits provide inspectable review evidence. None independently proves source exhaustiveness.

## Pass/fail examples

| Example | Today | Proposed |
| --- | --- | --- |
| New intake with empty list and no review declaration | Structurally passes if other fields valid | Fails |
| New reviewed case, no relevant requirements retained, dated exclusions and reason | Passes | Passes with consistent declaration |
| New reviewed case with partial taxonomy due missing PIN-route facts | Passes | Passes with evidence-limited review; does not force taxonomy complete |
| New case marked reviewed-with-assessments but list empty | Passes without new declaration checks | Fails |
| New case whose material source could not be read and external review was never performed | May pass structurally | Fails completion gate while pass is blocked |
| Existing historical empty-list case without declaration | Passes | Remains valid; no fabricated backfill |
| Unsupported requirement ID or broken evidence reference | Fails | Still fails |

No currently invalid record is deliberately made valid. If applied retrospectively to everyone, all 194 would need new declarations; that option is rejected. Under the recommended prospective scope, zero existing IDs fail solely for missing declarations. Newly created IDs and voluntarily declared objects are the affected population.

## Preservation risks and stop conditions

Main risk: mechanically labelling historic records reviewed, removing unresolved clauses to satisfy a complete flag, or adding irrelevant standards rows. Prohibit all three. Keep before/after evidence, taxonomy roles, HIM, source episodes and provenance; accepted uncertainty is preserved. An audit-reference check must not require public prose to become process narration.

After approval, implement the described controls with isolated positive/negative fixtures and run them read-only. Report exact failing IDs/fields. **Stop for Gate 2 before repairs outside the five authorised records**, even if a declaration claims completion. Stop if the proposed rule changes public prose roles, needs deletion of accepted evidence, conflicts with renderer semantics, or makes an evidence-limited review indistinguishable from unperformed work.

The branch also has an independently reproduced, pre-existing allocation snapshot test failure: `test_current_class_ids_and_family_allocations_are_preserved` omits the admitted Human Dignity family/class. This work does not change that permanent test. It needs separate scoped handling; it is not evidence that the five Incident edits failed.
