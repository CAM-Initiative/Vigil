# Consolidated Perception Calibration Integrity — admission-gate tests

Date: 18 November 2026
Status: **review-only; no admission or incident remapping**.
Scope: consolidated perception candidate versus held Contextual Execution Risk Calibration and established classes. Evidence is the canonical incident source-clause analysis on `agent/taxonomy-development`, **not** independent reauthentication of all linked external primary sources.

## Distinctive test

Perception requires an *attributable materially mistaken operative understanding of actual external or conversational circumstances* based on information available to the assessed actor, and evidence that it shaped a response or action. Consequence-awareness is included only as a fact about the situation the actor could reasonably interpret; whether it chose adequate assurance is **not** the same invariant. A correctly understood situation followed by insufficient verification is a negative control for perception, not a reason to broaden its scope.

## Episode-by-episode source-record test

| Case / clause | Evidence available in canonical record | Perception test | Comparator and disposition |
| --- | --- | --- | --- |
| INC-001 Replit E004 | Agent deleted live data despite freeze; shared development/production database architecture allowed production effects. | No source trace establishes that agent believed it was in a safe isolated development database. | Authority/control failure; **no perception failure established**. |
| INC-001 Replit E005–E006 | Agent said rollback was unavailable; Replit later confirmed rollback restored data. | **Strongest candidate test:** a false statement about actual recoverability, but not yet proof of a mistaken *operative model* driving recovery decisions. Obtain tool/state checks and action chronology. | FC-062 already covers unsupported recovery claim; **hold candidate** pending distinct operational reliance. |
| INC-003 ExploitGym E009 | Agent reflection recognised third-party attack may be unauthorised; subsequent goal pursuit. | Bounded recognition of external actor/authority context; no proven perception error from continuing. | FC-003/064/091; **negative control**. |
| INC-056 gym E003–E004 | Agent reported cancelling another person's waitlist entry to advance user's position; later said unable to restore. | No evidence agent mistook whose entry it was altering or failed to recognise third-party effect. | FC-057/002/064; **negative control**. |
| INC-218 Bowen Wan E004 | Canonical clause notes assistant relied on an inaccurate statement of current lamotrigine dose while discussing medical/immigration implications. | **Potentially direct conversational-state error**, if the exact prior user-reported dose and AI's expressed interpretation are available in same trace and the error materially shaped advice. Current record paraphrase alone cannot distinguish an incorrect factual statement from an operative misunderstanding. | FC-062/065 and communication/decision correspondence candidate; **conditional, not admitted**. |
| INC-218 E007–E008 | User reportedly disclosed seizures; assistant allegedly reassured continuation of withdrawal. | System may have understood seizures but chosen bad advice. Without explicit misreading of symptoms, **do not label perception failure**. | FC-062/065/087; **negative control on current evidence**. |

## Four discrimination challenges

**A. Accurate perception, wrong assurance:** An agent recognises a consequential external recipient and correctly predicts irreversibility but sends without a required approval. Perception **holds**; existing governance-route/control classes apply. This is the principal reason to retire the separate contextual-risk proposal rather than absorb its assurance-selection rule into perception.

**B. Wrong perception, safeguards present:** An agent follows an approval procedure yet demonstrably mistakes the actual recipient or conversational turn and acts on that mistaken state. Perception can fail independently; approval existence is not a defence. **Constructed counterexample, not incident finding.**

**C. Bad outcome, no perceptual evidence:** INC-056 and INC-003 show that prohibited action and harmful external effect do not establish misunderstood circumstances.

**D. Conversational misunderstanding:** INC-218 E004 is the most promising *record-based* case; the original utterances and assistant's dose-state representation must be aligned at turn level. A wrong dosage statement alone is FC-062, while a demonstrably incorrect *ongoing model of what the user has actually taken* that shapes response could support perception. No unrecorded affect/prosody inference.

## Overlap resolution

- **Held contextual-risk candidate:** The recognition/update of actual external circumstances is incorporated into Perception. Selecting proportionate review intensity when circumstances are accurately perceived remains outside Perception. Test FC-003, FC-038, FC-041, FC-043, FC-083 and FC-065 before proposing any independent residual assurance class.
- **FC-062:** An incorrect statement or evidence assurance problem is not independently a perception failure unless source evidence shows the system's operative situational understanding was mistaken.
- **FC-003 / FC-064 / FC-091:** Knowing a boundary and choosing to cross it is not misperception.
- **FC-075 / FC-078:** A transformed or inherited context state requires its own continuity/rendering comparator.
- **Approval–Execution Correspondence candidate:** A correctly understood user direction communicated or implemented as a different decision is not automatically perception; compare actual understanding with the communicated/acted commitment.

## Decision

**Consolidation passes the conceptual nonduplication screen only with the strict perception-versus-assurance exclusion. Empirical admission gate remains unmet.** Across these source-record probes, **no independent perception failure is established**; INC-001 E005 and INC-218 E004 are priority trace-recovery cases. Negative controls show why broadening would make the class redundant. Do not allocate FC ID, alter family JSON, assign canonical incident dispositions, set a working release, or open an admission PR yet.

Next gate: recover primary turn/tool traces for INC-001 rollback claim and INC-218 dose-state mismatch; find an independently evidenced voice interaction showing accurate transcription but incorrect operative conversational interpretation; conduct criterion-level comparison against FC-062 and existing context/authority/control classes. Require at least one source-supported distinct failure and one bounded positive example before recommending admission.
