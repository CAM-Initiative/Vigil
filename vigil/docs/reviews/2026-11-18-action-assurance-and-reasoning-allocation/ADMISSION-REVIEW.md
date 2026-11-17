# VIGIL Alignment Taxonomy — action assurance and reasoning allocation

**Date:** 18 November 2026  
**State:** Unadmitted class-candidate authorship; **no new selectable Fidelity Classes, IDs, family memberships, release or Incident mappings yet**.  
**Published baseline:** VIGIL Alignment Taxonomy v0.9.2, 18 families, 83 current selectable classes. Baseline `main` commit `e7c720340a14bcca16a336545502ae4a1ed8aa0e`.  
**Authorised working lane:** `agent/taxonomy-development` only.  
**Candidate files:** `vigil/taxonomy/candidates/contextual-execution-risk-calibration.json`, `vigil/taxonomy/candidates/risk-adaptive-reasoning-allocation.json`.

## Abstraction and admission question

Two candidate invariants have been articulated and are provisionally distinguishable:

1. **Contextual Execution Risk Calibration Integrity** — selection of proportionate external-action assurance, based on the action's current recipient, purpose, principal, representational stakes, reliance, possible adverse effects and practical recoverability. The same tool, broad conversation and originally valid delegation do not imply equivalent execution-assurance requirements after a material change in context.
2. **Risk-Adaptive Reasoning Allocation Integrity** — allocation and escalation of adequate decision-evaluation capability as prospective complexity, uncertainty and external consequence change. A low-effort conversational mode must not silently nullify separately required execution protection, but a specific proprietary model tier is not the invariant.

**Discriminating example:** An agent may identify that an institutional publication requires user verification (risk calibration holds) yet fail to allocate sufficient independent review or validation to resolve complex factual dependencies (potential reasoning-allocation issue). Conversely, it may perform deep technical analysis (reasoning allocation adequate) but still send an institutional message without evaluating whether an informed human review is required (risk calibration fails). These are constructed contrasts, **not admitted empirical incidents**.

## Existing VIGIL comparator test

| Existing class | What is already governed | Evidence necessary for a genuinely separate new mapping |
| --- | --- | --- |
| FC-003 Target and Scope Authority Binding | Continuing authority applicability across principal, target, purpose and scope changes | Even a genuinely authorised action receives materially insufficient *assurance intensity* for its risk/reliance context |
| FC-038 Required Control Activation | Triggered and available operational control is not invoked | Material defect occurred **upstream** when proportionate assurance was selected, regardless of whether a specific control existed |
| FC-041 Required Governance Routing | Required, defined governance route was bypassed | Inadequate initial selection of an assurance/risk posture rather than only failure to traverse a known route |
| FC-043 Control Activation Validity | A defined control activates outside valid trigger scope | Disproportionate action assurance can exist without an erroneously triggered particular control |
| FC-083 Control Effectiveness Integrity | Activated control fails to achieve required protective effect | Failure to select sufficient assurance *before* the control effect is attempted |
| FC-062 Epistemic Reliance Calibration | Factual artefact assurance inadequate for downstream reliance | External action and identity/recipient consequences remain relevant even when the factual text is accurate |
| FC-065 Consequential Decision Grounding | AI direction undermines a human's independent consequential deliberation | The AI itself executes an external effect without selecting proportionate safeguards; no human persuasion is required |
| FC-025 Actor–Action Attribution | Responsible human/agent/tool actors cannot be distinguished | Actor attribution may remain perfectly preserved while execution assurance is materially under-calibrated |
| FC-091 Trajectory Legitimacy Integrity | Earlier unauthorised success becomes apparent legitimacy for further deviation | New class should apply to *authorised* prior execution followed by a changed risk profile, without claiming an earlier unauthorised step |
| FC-037 Control Availability Determination | Determine whether a known control is callable/applicable | Determine the required evaluation/capability tier independently of a named control's availability |
| FC-078 Continuity-State Validity | Inherited state across handoff, compaction or equivalent functional continuation becomes invalid | Same-conversation evolution does not itself prove inherited-state adoption across a continuity boundary |
| FC-064 Objective–Pathway Authority Separation | Objective utility supplants authority over means | Consequence-sensitive assurance may be inadequate absent task-completion pressure or unlawful route selection |

A full enumeration of 83 published classes and their family definitions was conducted during candidate development; the most relevant classes were examined at recognition/exclusion level. That check does **not** establish criterion-level comparators against a complete source dossier for any actual Incident.

## Current class-specific maturity

### Candidate 1 — Contextual Execution Risk Calibration Integrity

**Strongest novelty:** calibration of **the assurance threshold itself**, across materially changed contexts, prior to routing/activation of safeguards.

**Open threshold problem:** A classifier cannot convert a user's later dissatisfaction or abstract possibility of serious harm into proof that a specified execution level was required *ex ante*. Recognition must name the independently supportable applicable assurance standard and contemporaneously available risk dimensions. The proposed failure criteria intentionally require both.

**Positive and boundary counterexamples:** A low-risk personal logistics message should be sent without unnecessary interruption under valid authority. A high-consequence action may be validly pre-authorised without another per-message modal if adequate equivalent assurance or a permissible explicit, informed and scope-limited waiver applies.

**Decision status:** Ready for maintainer abstraction/threshold discussion; **not yet class admission**.

### Candidate 2 — Risk-Adaptive Reasoning Allocation Integrity

**Strongest novelty:** adequate *decision-assessment capability allocation* before consequence-bearing execution, including mode escalation, decomposition, independent verification or human review.

**Principal admission blocker:** Without a published applicable reasoning/verification routing rule or observed actual route/effort trace, a faulty action outcome alone cannot establish a reasoning-allocation failure. Counterfactual performance at a higher thinking level is not proof of causality. Avoid a vendor-specific rule of "always use High for all multi-tool actions"; many lengthy workflows have minimal consequence, while a one-step send may be high consequence.

**Decision status:** Research/class candidate requiring process observability and cross-tool test cases. Admission currently evidence-limited.

## Family placement: unresolved

**Do not force either into FF-0008 solely because a safeguard is involved.** FC-038/043/083 there evaluate activation and effect of already selected controls. FC-041 in FF-0007 concerns route traversal. Potentially coherent new family: **Decision Assurance Calibration Integrity**, but the same bounded property test must be satisfied for both candidate children; if the reasoning-allocation proposal collapses into a Caelestis runtime policy, a single new family requires a compelling reason rather than a generic governance container.

No `VIGIL-FF-*` or `VIGIL-FC-*` identifier is reserved. Current canonical `standard.version`, `release_history`, family files and taxonomy index remain at their last published values. Per `TAXONOMY-BRANCH-WORKFLOW.md`, `working_release` is not introduced while only draft candidates exist.

## Minimum research and approval gates

1. Approve or revise the candidate mechanisms **separately**. They should not be admitted as a package merely because one observed workflow raised both.
2. Test their full recognition and exclusion conditions against source-grounded, independently admissible positive, negative and boundary cases across more than one tool/task type.
3. Demonstrate that each candidate cannot be exhaustively represented by an existing class or a Caelestis implementation of that class.
4. Make an explicit family fit decision (existing versus new family) and identify the neutral parent invariant; check no false broad umbrella and no unneeded extra family.
5. Determine whether source records permit the class to be adjudicated from observable evidence rather than privileged internal chain-of-thought or model routing internals.
6. On explicit maintainer approval, allocate the next available canonical identities from the then-current taxonomy, update the family payload and allowed class/code lists, prepare at most one unpublished working release from current published `main`, validate and seek a dedicated approved taxonomy PR.
7. Only after taxonomy publication may independent public Incident adjudication apply the new classes; do not pre-assign any unadmitted class to an Incident.

**Publication boundary:** This public review contains general conceptual tests and no correspondence, source identifiers, personal data, unpublished conversation, or link/dependency on any private research workspace.
