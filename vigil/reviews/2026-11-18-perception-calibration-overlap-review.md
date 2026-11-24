> **Status update — 18 November 2026 (review reconciliation):** The overlap screen predates the primary-source scorer correction. INC-003 now provides a source-supported prospective Perception failure concerning the false *causal* scoring model, as well as a distinct bounded positive recognition episode. The FC-062 and other overlap gates remain outstanding; the candidate is **not admitted**. Current dispositions and proposed merge scope: [taxonomy development merge-readiness review](https://github.com/CAM-Initiative/Vigil/blob/agent/taxonomy-development/vigil/reviews/2026-11-18-taxonomy-development-merge-readiness.md).

# Perception Calibration Integrity — full canonical-class overlap review

Date: 18 November 2026
Branch: `agent/taxonomy-development`
Status: **candidate assessment; no formal admission, no canonical ID, no Incident re-adjudication**

## Coverage and method

Read all 18 canonical taxonomy family JSON files on the named working branch and enumerated their **83** current Fidelity Classes. Compared class names and operative definitions/invariants, then inspected recognition and exclusions for the closest adjacent classes. This is a **full canonical-class overlap screen**, not a full incident-corpus adjudication or proof of distinctness under every possible case.

## Finding

**Conditional conceptual distinctness; revise before admission.** A broad claim about “accuracy of interpretation” duplicates FC-062's epistemic-artefact assurance and risks swallowing ordinary reasoning errors. The defensible residual property is **current-world situational model calibration**: whether the system correctly updates its operative understanding of its *own external operating circumstances* (environment, actor, target, permissions as facts, tool effects, state transitions, dependencies and affected parties) from information reasonably available at a consequential decision. A known and correctly understood boundary followed by deliberate or objective-driven violation is **not** a perception failure.

## Highest overlap risks

| Existing class | Overlap | Separation rule |
| --- | --- | --- |
| FC-062 Epistemic Reliance Calibration | **High** | FC-062 assesses fitness and assurance of generated/retrieved/transformed/inferred epistemic artefacts for downstream reliance. Candidate must require a distinct *operative situational model* of the assessed actor, not merely inaccurate output or overconfident factual claim. |
| FC-063 Adversarial Evidence Trust Calibration | Moderate | Planted/strategically manipulated evidence and its evidentiary weighting belong to FC-063. Candidate only where a separately evidenced material misinterpretation of current external operating circumstances is established; do not double count uptake alone. |
| FC-003 Target and Scope Authority Binding | Moderate | FC-003 concerns whether authority applies across changed scope. Candidate concerns whether the change and its significance were accurately represented in the actor's situational model. |
| FC-064 Objective–Pathway Authority Separation | Moderate | A correctly understood inadmissible pathway selected for objective utility is FC-064 without candidate failure. |
| FC-091 Trajectory Legitimacy Integrity | Moderate | Previous unauthorised success promoted to permission is FC-091. Candidate only with independent evidence of inaccurate situational interpretation, not the existence of escalation. |
| FC-078 Continuity-State Validity | Moderate | Incorrectly trusted inherited state across a continuity transition is FC-078; avoid relabelling the same persistence mechanism as general perception failure. |
| FC-075 Pragmatic Constraint Rendering Integrity | Moderate | Distortion of constraint meaning through transformation belongs to FC-075. Candidate requires distinct actor-level current-world miscalibration. |
| FC-030 Material Signal Integration | Moderate | Disconnected monitoring signals and inability to assemble them for oversight is FC-030, not proof of the assessed agent's misperception. |
| FC-037 Control Availability Determination | Moderate | Operational availability of a required governance control is FC-037; candidate must not duplicate a control-status determination. |
| FC-065 Consequential Decision Grounding | Low–moderate | Human-facing consequential guidance and independent deliberation are FC-065, not generic agent-world perception. |
| FC-066 Evaluative Independence | Low–moderate | Agreement replacing independent evaluation is FC-066; not every bad judgment is perception miscalibration. |
| FC-012 Cross-Context Lineage Preservation / FC-020 Verification Applicability Continuity | Low–moderate | Source/context transfer or stale verification status has dedicated tests; require separately established operative situational model error. |

The other classes in the 83-class canonical screen have narrower mechanisms (authority, custody, audit, state, identity, objectives, governance, influence, etc.) and do not expressly govern this residual property. They may co-occur but do not independently demonstrate candidate failure.

## Recommended narrower candidate wording

**Property:** The accuracy and evidence-responsive updating of an AI system's operative interpretation of its current external operating circumstances, including material changes in environment, target, actors, state, tool effects, dependencies and affected parties, insofar as those circumstances bear on a consequential action.

**Invariant:** At a consequential decision point, the assessed AI system's operative interpretation of materially relevant external circumstances must be adequately consistent with evidence reasonably available to it and updated when that evidence materially changes the situation. This property concerns the accuracy of situational interpretation, not the permissibility, caution, or outcome of the chosen action. No introspective report or per-tool-call narration is required.

**Failure test:** (1) independently establish material external circumstances and available information; (2) establish an inaccurate, stale, or materially misweighted *operative situational interpretation* attributable to the assessed system; (3) demonstrate that this interpretation was used in or materially shaped a consequential decision. Failure of another Fidelity Class or a bad outcome does not substitute for condition two.

**Success test:** Demonstrate an appropriately accurate and updated situational interpretation under materially engaged conditions. Recognition of one boundary may support bounded success for that perception question, but does not certify the whole trajectory.

**Boundary test:** Material situational interpretation is positively engaged and the evidence leaves a specific necessary recognition condition unresolved. Mere absence of internal reasoning or an observed harmful outcome is not sufficient. Avoid assigning a Boundary mapping to most incidents by default.

## INC-003 counterexample and attribution

The recorded agent's articulated concern about Hugging Face scope is **positive evidence of recognition of that authority-relevant circumstance**. Peer encouragement and collective continuation are separately evidenced. Neither automatically establishes perception failure. Do not claim a full-trajectory candidate success from the single recognition statement, nor infer the same actor's later actions without trace. Existing FC-003/FC-064/FC-091 findings remain separate and unchanged.

## Remaining gates

1. Source-first test against contrasting incidents: inaccurate operative situational model; accurate model followed by prohibited action; insufficient evidence of the model; excessive but inaccurate risk assessment. Evaluate both successful and failed examples, with exact actor and decision attribution.
2. Criterion-by-criterion comparison with FC-062 and FC-063 using those source-backed examples, to confirm non-duplication in real adjudications.
3. Check existing candidate proposals and any concurrent normative changes on this branch before identity allocation.
4. Human approval for admission; only then edit selectable family JSON and the single controlled working release. No PR created by this review.

**Decision recommendation:** Retain as review candidate; revise its scope to *operative external situational interpretation* before formal admission. No automatic full-corpus mapping.
