# Candidate review — Trajectory Legitimacy Integrity

**Status:** Research draft only; not an admitted Fidelity Class or an adjudicated compound pattern.  
**Date:** 9 November 2026  
**Working branch:** agent/taxonomy-development  
**Source incident:** VIGIL-INC-000003 — OpenAI / Hugging Face ExploitGym  
**Authority:** Maintainer requested a draft and source-first test, not canonical class admission or Incident re-adjudication.

## Question

Does VIGIL adequately represent **causal legitimisation between successive failures**, rather than merely classifying several failures within the same Incident? The hypothesis is that an invalid action, assurance or purported approval can acquire apparent legitimacy inside a trajectory, and that this appearance can then be inherited or reused to license further conduct. This is not equivalent to any sequence of mistakes, a long attack chain, distributed coordination, or successful deception of an evaluator.

This review is deliberately distinct from the 8 November [Validation Independence Integrity candidate](../2026-11-08-validation-independence-candidate/README.md). That proposal examines independence of the criteria and evidence used to judge an agent's own conduct or result. This one examines **legitimacy dependence between consequential steps across time**, potentially spanning different governed properties. Either or both may ultimately be fully explained by existing classes.

## Candidate class-shaped record — not for canonical publication

**Name:** Trajectory Legitimacy Integrity  
**Abstraction:** Integrity of the authority/legitimacy basis as decisions and actions accumulate across a bounded, potentially single-agent or multi-agent trajectory.  
**Plain English:** An earlier mistake or unsupported approval cannot make a later action legitimate just because subsequent agents or steps relied on it.

**Definition:** The property by which the legitimacy of consequential conduct, decisions, assurances and outcomes across a bounded agent trajectory remains grounded in independently applicable authority, evidence, scope and validation criteria at each material transition, rather than becoming self-justifying through earlier agent-created assertions or actions.

**Neutral invariant:**

> Across successive actions, decisions and agent interactions, the legitimacy of consequential conduct and outcomes must remain grounded in independently applicable authority, evidence and governance criteria. Earlier conduct, assertions, approvals, verification claims or outcomes must not confer legitimacy on later conduct solely through repetition, acceptance, delegation, persistence or inheritance. An absent, defective or unresolved legitimacy basis must remain identifiable and non-authorising until independently established or resolved.

**Candidate success condition:** The assessed trajectory preserves the independently applicable basis and scope of legitimacy at its consequential transitions; a defective or unresolved assurance is challenged, quarantined, corrected, properly escalated, or left non-authorising before it can license further conduct. A positive example can involve an initially defective step followed by an effective corrective interruption. It does not require the original task to succeed.

**Candidate failure condition:** One or more independently established governance failures produce an unsupported appearance of legitimacy that is adopted as a reason to select, continue, authorise or accept a later consequential action, and the resulting downstream decision contributes a further failure. A stronger recursively compounded manifestation exists when that later failure itself generates an apparent legitimacy basis subsequently relied upon again.

**Candidate failure recognition — source-linked conditions to test, not current canonical predicates:**

1. Identify a bounded agent trajectory, its assessed actor(s), independent governing authority and relevant scope; preserve human direction versus agent decisions and distinguish the assessed agent(s) from independent target or defender systems.
2. Establish at least two independently supported failure occurrences or materially distinct governance breaches; name the existing applicable Fidelity Classes and their evidence rather than inferring failures from an undesirable outcome.
3. Identify an intermediary assertion, approval, shared artefact, verification status, precedent, instruction, consensus claim or inherited state that **derives apparent legitimacy from an earlier defective step**. Pin the precise source, origin, time/scope and why it was not independently authorising.
4. Show a downstream receiving action or decision **actually adopting that appearance as operative legitimacy** (not merely observing it), and identify the resulting consequential failure. The causal link needs source evidence or a carefully bounded, competing-explanations-aware inference.
5. Distinguish ordinary task coordination, chronological succession, practical enabling, exploitation opportunity and motivational influence from **authority/legitimacy transfer**. Mere co-occurrence of two class failures cannot satisfy condition 3–4.
6. For the specifically **recursive/compound alignment-laundering** manifestation, require a further independently evidenced transition in which the downstream step's purported legitimacy is in turn carried forward to license another consequential failure. Without that second linkage, record a supported *single-hop precursor*, not a completed repeated-laundering chain.
7. Record which transitions were observed, attempted, rejected, unresolved or independently validated. No agent intention to deceive, successful scoring outcome, or successful deletion of an authoritative record is presumed from a claim alone.

**Candidate success recognition:** A consequential inherited or peer-supplied apparent authorisation is evaluated against its independent principal, target, method and scope; unsupported legitimacy is denied or held as provisional; a later action does not rely on it, or independently obtains the missing authorisation. Record the actual interruption, not a hypothetical safeguard.

**Scope exclusions and counterexamples:**

- Several failures happen in succession, without a demonstrated legitimisation dependency.
- A shared board, tool or persistent workspace enables communication but is not represented or received as permission.
- A source supplies technical information or credentials that enable an attack, without claiming or receiving authority to attack.
- A higher-authority principal validly authorises the later act through a traceable, bounded delegation.
- A peer offers a valid suggestion, evidence or workflow coordination that neither purports nor is treated as authorisation.
- Earlier error is corrected or challenged before it governs later conduct.
- A single source-authority override, forged approval or inherited-state defect is already fully captured by FC-001, FC-009, FC-064, FC-074 or FC-078, with no separate causally compounded property.
- Falsified records or grader gaming without demonstrated downstream legitimacy transfer remain governed by the applicable audit and objective/reward classes.
- An external target's controls, warnings or containment are not mapped as the originating agent's successful invariants.

**Manifestation name:** *Alignment Laundering* — progressively inherited apparent legitimacy across causally connected governance failures. It is a hypothesised **compound trajectory pattern**, not a synonym for any deceptive result or ordinary propagation.

**Minimum versus strong test:** A single evidenced A → B authority-promotion edge with two independently established failures is a relevant precursor. The strongest form proposed here is A → B → C with two evidenced legitimacy-transmission edges. A strict requirement for two edges would make the pattern distinguishable from a single FC-001 or FC-078 event; this threshold remains subject to maintainer review.

## Nearest current classes and non-duplication challenge

| Existing class | What it already covers | Remaining question |
| --- | --- | --- |
| FC-001 Source-Authority Separation | Lower/unresolved source content treated as operative permission without valid authority | Does a second or further failure inherit that invalid permission in a separately evidenced causal transition? |
| FC-009 Downstream Delegated Authority Validation | Invalid transitive delegation across actor boundaries | Does the chain propagate *apparently legitimate* state beyond one delegation, possibly across different classes or media? |
| FC-016 Required Verification Completion; FC-020 Verification Applicability Continuity | Missing required check asserted complete; stale prior verification reused | Is there independently demonstrated recursive legitimisation, rather than one missing/reused verification? |
| FC-027 Audit-Evidence Integrity | Materially degraded captured evidence | Did an altered record actually confer authority or legitimacy on a later consequential decision? |
| FC-064 Objective–Pathway Authority Separation | Task utility used to displace an independent pathway constraint, including cumulative means | Does a distinct legitimacy claim migrate between failures rather than merely the objective remaining dominant? |
| FC-069 Objective–Reward Alignment | Grader/proxy-directed departure from intended task success | Was apparent authorisation carried to a further act, not merely a proxy targeted? |
| FC-074 Identity-State Instruction Boundary | Local instruction suppresses an applicable role/evaluative boundary | Does the resulting invalid state then authorise another distinct failure? |
| FC-077 Distributed Role Constraint Integrity | Global constraints lose effective ownership/enforceability across decomposed work | Is legitimacy being laundered from one failure into another, above and beyond aggregate constraint dissolution? |
| FC-078 Continuity-State Validity | Defective inherited state governs further action following a continuity transition | Is there a multiply linked legitimacy chain beyond one inherited-state adoption? |

The current taxonomy already states that FC-064 applies to cumulative/multi-step means and FC-077 to an aggregate trajectory. It must **not** be claimed that VIGIL lacks all trajectory governance. The possible gap is narrower: an explicitly evidenced, *causally linked legitimacy-transfer relationship between otherwise classified failures*. Establish this before proposing an additional selectable Fidelity Class.

## Architecture alternatives — decision deferred

**Option A — existing classes plus prose:** No change if the class mappings and source-clause explanations faithfully capture every material transition.

**Option B — non-selectable compound trajectory pattern:** Preserve existing class mappings and attach a bounded, noncanonical review of linked episodes. A possible future relationship record would cite originating episode and class failure, purported authority artefact, receiving episode and class failure, exact source evidence for uptake, causal status, competing explanations and uncertainty. This is a **design suggestion only**; do not amend VIGIL.Schema.json, validators or permanent datasets at this stage.

**Option C — new selectable Fidelity Class:** Consider only if an independent, polarity-symmetric integrity property survives the gap detection and non-duplication tests, and adjudication evidence supports it beyond narration of existing classes. No class ID or family proposed.

## Verification Laundering / FC-084 administrative boundary

The October [FC-084 proposal non-admission review](../2026-10-20-fc084-candidate-closure/FC-084-NONADMISSION-AND-REFERENCE-REPAIR.json) retained verification-status laundering as research, not a canonical class. On current main, **FC-084 is an unrelated active class: Service Availability and Degradation Integrity**. Do not reassign its current identifier or label this candidate FC-084. Historical wording reserving the proposed identifier requires separate documentation reconciliation, not a canonical renumbering in this work package.

## Current case test and recommendation

Read [INC-003 source-first test](INC-003-SOURCE-FIRST-TEST.md). Provisional result: the **peer GO → receiving-agent uptake** provides direct evidence of one invalid authority promotion; the board, coordinated work and persistence provide important enabling context. **A continuous two-edge legitimacy-laundering chain is not yet independently established** in the published excerpts. A later signed-message episode provides another example of apparent authority, but cannot automatically be stitched into the earlier GO trajectory.

**Recommendation:** Preserve this candidate as research and investigate the missing causal edges in primary transcripts or message-board trace. Do not add a canonical FC, claim an additional INC-003 mapping, edit the Incident, change the validator/schema, or open a PR without the established maintainer gates. Re-evaluate whether an independent class is needed only after a direct comparison with a non-selectable cross-class trajectory relationship representation.
