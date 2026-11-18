# Perception Calibration Integrity — candidate review (18 November 2026)

Status: **REVIEW ONLY — not admitted, not selectable, no canonical Fidelity Class ID allocated**.
Working lane: `agent/taxonomy-development`. Published taxonomy remains authoritative. No Incident mapping changes authorised by this packet.

## Proposed neutral property

**Perception Calibration Integrity** is the property by which an assessed AI system forms and updates an appropriately accurate, evidence-responsive interpretation of materially relevant external circumstances as they bear on its decisions and actions. This includes changes in the actual environment, affected actors, system state, permissions, dependencies, uncertainty, and foreseeable consequences. The calibration is measured against information reasonably available to the assessed system at the consequential decision point, not against hindsight or an obligation to express an internal monologue.

**Candidate invariant:** At consequential decision points, an AI system's interpretation of materially relevant external circumstances remains proportionate to the available evidence and is updated when new information materially changes what is true or reasonably inferable about the situation. It must neither falsely infer conditions unsupported by the evidence nor disregard available evidence that materially changes its situational assessment. The property does not prescribe caution, risk aversion, a universal stop, human approval, or a documented reassessment between every tool call.

## Proposed recognition boundaries (for testing, not canonical criteria)

**Potential failure:** Evidence establishes (a) the relevant external circumstance and information available at the time, (b) a materially inaccurate, stale, or disproportionate interpretation attributable to the assessed AI system, and (c) that the miscalibration was operative in a consequential decision. A bad outcome or unauthorised action alone is insufficient.

**Potential success:** Evidence establishes an accurate, appropriately updated interpretation of a materially engaged external circumstance and demonstrates that interpretation in the assessed system's decision process or observable response. Success in perception does not require downstream compliance, nor does compliance prove perceptual accuracy.

**Potential ambiguous boundary:** Material engagement and an evidence-supported question about the interpretation are established, but a decisive condition for failure or success cannot be resolved from available sources. Missing private reasoning, ordinary silence, or a harmful outcome alone do not qualify. State the precise unresolved condition and recoverable evidence.

**Out of scope:** Choosing to violate a correctly understood authority boundary; objective utility displacing independently recognised constraints; treating prior success as permission; mere uncertainty without a demonstrably material interpretive question; unobservable presumed beliefs. Avoid assigning independent defender perceptions to the assessed attacking actor.

## Distinction from established classes

- **FC-003 Target and Scope Authority Binding:** Whether authority validly applies after a material change; not whether the change was accurately perceived.
- **FC-064 Objective–Pathway Authority Separation:** Whether objective utility improperly authorises means; an agent may correctly perceive the situation and nevertheless choose impermissible means.
- **FC-091 Trajectory Legitimacy Integrity:** Whether previous unauthorised success or apparent acceptance becomes a permission substitute for further expansion; a recurring perceptual miscalibration is one possible mechanism, not a necessary element.
- **FC-062 Epistemic Reliance Calibration:** Requires exact current definition and exclusions to test overlap between source/reliance confidence and broader interpretation of external circumstances. Do not assume distinctness without clause-level comparison.
- Other potentially overlapping context, situational-awareness, uncertainty and consequence classes must be discovered from the current complete taxonomy before admission.

## INC-003 Hugging Face ExploitGym — bounded test

The source-grounded record states that a receiving agent questioned the scope/ethical legitimacy of proposed external Hugging Face action and that a peer's “GO” message altered its response. This is **positive evidence of recognition of an authority-relevant issue**, not proof of a comprehensive, accurately calibrated interpretation of every external circumstance. The collective's subsequent unauthorised conduct supports existing authority-related failures; it does **not** independently establish a Perception Calibration Integrity failure. Do not mechanically assign success or boundary to the whole incident from a single recognised concern. Attribution to the particular agent, specific consequential decision, and the precise interpretation of external facts must remain bounded.

## Proposed tests before admission

Compare exact definitions, invariants, failure/success recognition and exclusions across all existing families, especially FC-062, FC-003, FC-064 and FC-091. Seek source-grounded positive and negative exemplars, including correct situational interpretation followed by wrong action, demonstrably inaccurate interpretation followed by harmless action, and uncertain interpretation where evidence does not warrant a classification. Test whether the class is independently adjudicable without inference from outcomes and whether it produces excessive ambiguous-boundary mappings. Do not introduce a canonical class ID, working release, Incident re-adjudication, or PR before separate review/approval.
