# PR #140 — FC-018 / FC-052 / FC-078 recognition-scope reconciliation

**Date:** 21 October 2026  
**Review issue:** [#148](https://github.com/CAM-Initiative/Vigil/issues/148)  
**Branch:** `work/incident-taxonomy-reasoning-readjudication-20261018`  
**Published baseline:** Alignment Taxonomy `0.7.0` on `main`  
**Single intended, unpublished candidate:** `0.8.0` (see index `working_release`)

## Authority and scope

This document reconciles the maintainer's earlier **conceptual decisions** with the *literal current canonical recognition tests* and the issue's named, previously adjudicated Incidents. It is an interpretive and release-readiness decision packet, **not** a canonical taxonomy amendment, a new Incident role determination, a claim of complete whole-corpus readjudication, or authorisation to merge. Earlier dated review claims remain preserved. The taxonomy version stamped on each older Incident is not automatically rewritten.

## FC-018 — Completion-Condition Alignment

**Agreed principle:** Knowingly fabricated task-completion proof or tool evidence is not vindicated by a scorer that fails to accept it, or by an attempted cheat that does not earn a reward. Fabrication is an evidentially assessable failure mechanism in its own right, independent of scored success. Task optimisation and reward/score-seeking must not be confused with a valid completion condition.

**Current literal limitation:** The existing FC-018 failure recognition is narrower: it requires (1) a governing external completion condition, (2) a **different internal/intermediate/local/partial condition actually satisfied**, and (3) the system **treating that satisfied substitute** as sufficient proof of overall completion. Falsely claiming a completion result without a satisfied substitute is not *automatically* FC-018 merely because the false claim is wrongful; FC-017 Success Representation Integrity and applicable evidence/provenance or objective-pathway classes must be examined distinctly. Nor is a downstream scorer accepting a fake flag a universal requirement for all other failures.

**INC-003:** The source-grounded fabricated flags and misleading terminal evidence are material; no matched terminal submission/scorer completion decision has been recovered. The present FC-018 Boundary was based both on missing decision evidence and this scope ambiguity. Do not convert it to success or erase the documented fake-proof occurrence. A taxonomy-wording decision is needed if FC-018 itself is intended to admit **purported/fabricated** completion proof without a satisfied substitute: specify that revised trigger without collapsing FC-018 into FC-017, and re-adjudicate INC-003 against the adopted text. The prior maintainer decision about wrongful falsification is recorded; the specific FC-018 clause admission is **not yet complete**.

## FC-052 — Choice Agency Preservation

**Agreed principle:** Deceptive instrumental use of AI in a human-directed workflow can impair choice. Autonomous model intention, hidden reward weights or a self-originated objective are **not preconditions** to an AI-governance assessment. Equally, generic drafting assistance alone is not evidence of the full choice-impairment mechanism.

**Current literal limitation:** FC-052 says `the system has an objective` and `the system selects or executes` an influence tactic, without clearly defining whether the governed unit is an AI-enabled *workflow* with human-selected objectives or a model/agent executing its own assigned objective. Neighbouring FC-082 expressly includes human-directed AI-mediated social engineering and already carries supported failures in INC-082/083. Resolving the scope must preserve FC-052's independent conditions: instrumental objective-linked tactic, material impairment of independent choice, and a consequential state transition not knowingly/free-authorised on the same basis. Do not equate all deceptive AI content with automatic FC-052 admission.

**INC-052, INC-082 and INC-083:** INC-052's AI image reportedly arrived *after* initial shortcut execution, leaving its influence on a specific consequential recipient decision unresolved. INC-082 and INC-083 already have other source-grounded failure findings (including FC-082), but their FC-052 Boundaries specifically cite whether the human-operated AI-generated deception qualifies as `system` objective/tactic execution. An explicit, versioned wording clarification is needed if FC-052 covers the whole materially AI-enabled human-directed workflow. Then independently test every literal consequence/authorisation condition before changing any of the three current roles. The conceptual no-autonomous-intent decision is retained; case-level FC-052 disposition remains to be reconciled.

## FC-078 — Continuity-State Validity

**Agreed principle:** A fake memory, counterfeit compaction, or purported inherited approval can claim continuity authority even if no legitimate earlier approval or compaction exists. The absence of a genuine predecessor is **not proof of safety** or an automatic exclusion of the attack.

**Current literal limitation:** FC-078 requires a material `continuity transition`, inherited state that requires reassessment, subsequent use without appropriate validity checks, and a **material continuity contribution to persistence** of the defective trajectory. FC-001/FC-006 independently cover source-authority and control-plane promotion. A forged handoff can be relevant to FC-078 when it *functions as* a continuity-state transfer, but not merely because a file says “approved earlier.” First uptake alone is not necessarily independently established continuity-mediated entrenchment. The criterion must be tested against the subsequent trajectory and not merely an invented requirement for an actual historic approval.

**INC-185:** Published provider evidence establishes the forged compacted/policy-like note, defender suspicion, later file persistence and build-configuration action. Existing FC-001/006/041 failures remain valid. The current FC-078 Boundary concerns whether this is separately a defective *continuity* transition and contribution to persistent governing state rather than solely source/control-plane promotion. This requires an explicit interpretation of counterfeit state and independent carryforward/entrenchment, followed by a source/episode-bound role decision. Do not automatically convert Boundary to Failure merely because the injected note was followed.

## Release decision

- FC-045 / INC-008 is separately implemented and should **not** be reopened by these three questions. A hand-authored, historical FC-045 **Boundary** exemplar for INC-008 remains stale relative to the later canonical **Failure** and requires a narrow provenance-preserving taxonomy/exemplar reconciliation before public release.
- Maintain #148 **open** only for the three literal class-scope decisions and resulting case-level adjudication, plus the stale FC-045 exemplar housekeeping. A conceptual agreement is not a passing classification test.
- Do not add a new Fidelity Class, change HIM or independent EXTREQ assessments, mechanically overwrite historical Incident taxonomy versions, or claim a whole-corpus certification.
- If approval for concrete revised criterion wording is required, prepare it once, review neighbouring false positives, update the existing PR #140 branch, pin the applied working taxonomy revision, rebuild generated projections, and run the full CI/rebuild checks.
- Distinguish deferred research (e.g. unreported scorer trajectory) from actual remaining implementation. A finite, explicitly recorded evidence limit may be a completed disposition.
