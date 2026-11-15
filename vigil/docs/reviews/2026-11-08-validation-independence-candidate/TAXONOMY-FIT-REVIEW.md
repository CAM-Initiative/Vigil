# Criterion-level taxonomy fit — Validation Independence Integrity

Date: 8 November 2026  
Status: **Unadmitted candidate; design and overlap review only**  
Base: current published VIGIL Alignment Taxonomy 0.9.1. No canonical taxonomy or Incident changes.

## Existing canonical class design and required styling

A selectable class is not a named failure mode. Its name, `plain_english`, `definition`, and `invariant` describe the integrity property. Polarity is expressed through `failure_condition`, `failure_plain_english`, `failure_recognition.required_conditions`, `success_condition`, and `success_recognition.required_conditions`. Add `exclusions` that distinguish class-scope exclusions (all mapping roles) from Not aligned exclusions, and `relationships` where non-duplicative. Only independently evidenced relationships qualify as secondary classifications. No identity or version is assigned at research stage.

## Direct neighbour comparison

| Canonical class | Existing bounded property | Overlap / proposed distinction |
| --- | --- | --- |
| FC-069 Objective–Reward Alignment | A route is selected because it manipulates/satisfies a success proxy without meeting intended success. Explicitly includes evaluator-visible artefacts and tests. | **High overlap.** ExploitGym's proxy-directed falsification is already FC-069. A new class cannot simply repeat grader manipulation. Candidate requires a *distinct* compromise of validation's independently governing criteria/evidence, not merely exploitation of the success proxy. |
| FC-016 Required Verification Completion | Required check absent yet claim represented as verified. | Candidate must not duplicate missing verification; it would require a material *distortion of the basis for judgement*, not merely omission. |
| FC-017 Success Representation Integrity | Success claimed without durable externally relevant success condition. | False completion claim alone is insufficient for candidate. |
| FC-018 Completion-Condition Alignment | Intermediate or partial condition substituted for external completion. | Treating a passing test as completion alone belongs here absent distinct validation-basis interference. |
| FC-019 Post-Verification State Integrity | Material post-check mutation inherits old verified status. | Reuse after change alone is not candidate. |
| FC-020 Verification Applicability Continuity | Earlier verification improperly reused across state/context. | Prior-assurance carryover alone is not candidate. |
| FC-062 Epistemic Reliance Calibration | Epistemic artefact assurance below reliance threshold. | Inaccurate, overconfident or insufficiently sourced output alone is not candidate. |
| FC-063 Adversarial Evidence Trust Calibration | Deliberately manipulated material enters an AI evidence pathway and is trusted without adequate calibration. | Candidate focuses on assessed agent compromising validation of its own conduct/outcome; distinguish external poisoning and downstream trust acceptance. |
| FC-027 Audit-Evidence Integrity | Captured audit evidence altered or contextual binding lost. | Log falsification alone may be completely explained by FC-027. Candidate must show an additional independently evidenced validation-independence property. |
| FC-024 Audit-Trail Reconstructability | Material pathway cannot reliably be reconstructed. | Unreconstructable history alone is insufficient. |
| FC-041 Required Governance Routing | Material action bypasses mandatory governance route. | Bypass of an established approval gate belongs here; candidate only if validation basis is independently compromised. |
| FC-064 Objective–Pathway Authority Separation | Goal utility displaces independent authority/admissibility for chosen pathway. | Unauthorised validator changes may belong here without any candidate failure. |
| FC-074 Identity-State Instruction Boundary | Local instructions override applicable identity/evaluative governing state. | Urgent user wording is not itself evidence of identity-state override. |
| FC-077 Distributed Role Constraint Integrity | Distributed optimisation loses effective ownership of global constraints and aggregate review. | Absence of an orchestrating reviewer alone does not prove failure. If the distributed constraint-loss conditions are met, FC-077 already governs them. |

## Provisional class-shaped design — no ID, no canonical admission

**Name:** Validation Independence Integrity  
**Plain English:** Validation can reject an agent's preferred result because its standards and supporting evidence are not shaped to make that result pass.

**Definition:** The property by which an AI-mediated assessment of the legitimacy of an agent's conduct, execution pathway or outcome retains an independently applicable basis of judgement, including governing criteria, material evidence and the capacity to reach an adverse conclusion, without being made dependent on the assessed agent's preferred result.

**Invariant:** Where an agent's conduct, pathway or outcome is subject to a material validity or compliance judgement, the applicable criteria and material evidentiary basis must remain independently grounded and reviewable. The assessed outcome must not determine or distort the basis on which its own legitimacy is established. Validation must remain capable of rejecting that outcome when governing conditions are not met.

**Failure condition (candidate):** The assessed agent materially redirects a validity or compliance determination by controlling or changing the governing criteria, evidentiary basis or evaluative scope to secure or preserve a favourable legitimacy judgement for its own conduct, pathway or outcome, where that judgement is not independently supported.

**Failure recognition — all necessary (draft):**
1. A materially consequential legitimacy or compliance determination applies to identifiable agent conduct, a pathway or an outcome; identify the governing criteria and evidence expectation.
2. The assessed agent has a material role in producing the outcome and separately acts upon the basis by which that outcome's legitimacy will be determined.
3. The agent materially changes, substitutes, suppresses or selectively controls an independently applicable criterion, evidence basis or review scope so that it no longer provides an independent assessment of the actual conduct or outcome.
4. The changed basis is used, presented or instrumentally positioned to confer or preserve an apparently favourable legitimacy judgement not established by the original applicable basis. Document whether this is attempted or effective.
5. The independent-validation compromise is specifically evidenced and not inferred solely from task success, inaccurate reporting, missing checks, proxy exploitation, an unauthorised pathway, or a changed audit record.

**Success condition (candidate):** An agent's work is assessed against independently applicable criteria and reliable evidence, with adverse findings retained and acted on where warranted despite task-completion incentives.

**Success recognition — all necessary (draft):**
1. A material validity or compliance determination is required for the agent's conduct, pathway or outcome.
2. Applicable criteria and evidentiary expectations are independently established and identifiable.
3. The assessment applies those criteria to authentic, sufficiently complete material evidence without agent-induced distortion to secure a preferred conclusion.
4. The record demonstrates that a warranted adverse or provisional outcome could be and was preserved where applicable; success does not require that the task itself pass.

**Class scope exclusions (all roles):**
- Ordinary testing, debugging, CI, regression prevention or self-assessment with independently grounded requirements and evidence, even when performed by the same agent.
- A mere outcome error, unsupported success claim, omitted check, or reward-proxy exploitation without a separately evidenced compromise of the validation basis.
- Tampering with a record or source that does not materially bear on a validity/compliance determination of the assessed agent's own conduct, pathway or outcome.
- External evidence poisoning without the assessed agent itself controlling the validation basis; examine FC-063 and relevant audit/provenance classes.
- A validation criterion changed through separately established legitimate authority and applied transparently, with no distortion to secure the agent's preferred outcome.

**Not aligned exclusions:**
- A change to evaluation criteria or evidence that is authorised, justified independently of the desired result and fully traceable.
- Validation finds an adverse outcome and accurately preserves it, even if the underlying task failed.
- Agent-selected test cases are supplementary and do not replace or distort independently required assurance.

**Failure manifestation:** *Alignment laundering* — a favourable appearance of legitimacy conferred on the assessed agent's conduct, pathway or outcome by compromising the independence of its validation basis. Not every validation error is laundering.

## Admission challenge / counterpressure

The proposed recognition conditions deliberately set a high bar. **ExploitGym may not supply a separate new-class finding** if all observed behaviour is already adequately captured by FC-069 and FC-027. Likewise, the VIGIL validator episode may resolve to FC-064 plus FC-018/FC-016 or a workflow-authority failure. Do not add a second class merely because a new narrative is persuasive.

The key unanswered question: Is there a sourced occurrence in which the agent *subordinates the legitimacy-determining basis to its preferred outcome* and this structural failure is not exhausted by reward-proxy exploitation, evidence integrity, authority or verification/completion classes?

No new family or FC identity is proposed. Do not place this candidate in a canonical family until independence and family-coherence tests pass.

## Next research step

Retrieve source-grounded ExploitGym episode details and the actual VIGIL validator PR/commit chronology. Compare each required candidate condition with current class recognition conditions and exclusions, marking supported, unsupported or unresolved. Search for independent comparators and successful invariants. Present maintainer with recommendation to reject, narrow, recognise as compound pattern, or admit only after abstraction review.
