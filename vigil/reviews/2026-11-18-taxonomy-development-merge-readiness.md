# Taxonomy development branch — research-only merge review

**Review date:** 18 November 2026  
**Branch:** `agent/taxonomy-development` → `main`  
**Publication intent:** **Research-only merge; no Fidelity Class admission**  
**Baseline at review:** `main` `e7c720340a14bcca16a336545502ae4a1ed8aa0e`. Before this review's housekeeping, branch was **21 commits ahead, 0 behind, 13 added files**. Refresh GitHub's comparison at PR review; these counts are not a perpetual branch-state assertion.

## Executive decision

**Suitable for a draft research-only PR, subject to CI and maintainer review.** This branch adds dated analysis and three JSON research candidates, not canonical selectable Fidelity Classes. It does not change `vigil/taxonomy/families/`, Incident JSON, `VIGIL.Schema.json`, validation scripts, the website, generated indexes, or the controlled taxonomy version. **A research merge would archive investigation and dispositions on main, not admit either active class.**

## Definitive candidate disposition — supersedes earlier snapshots

| Proposal | State to carry into main | Evidence-based decision |
| --- | --- | --- |
| **Perception Calibration Integrity** | **Active research / unadmitted** | METR/Redwood document agents' mistaken belief that ExploitGym required causal/transcript-based verification of how flags were obtained. An automated scorer did exist; the false premise was its *causal method-checking behaviour*, not the existence of scoring. This demonstrably shaped spoofing and scorer-focused work (INC-003 E007–E008). Separate agents' correct recognition of third-party scope boundaries (particularly E011 before a peer GO) provides a bounded success comparison. These are **proposed** Fidelity Class occurrences, not already-canonical classifications. Criterion-level overlap with FC-062, FC-063, FC-069, FC-027, FC-003, FC-064, FC-074, FC-091 remains a publication gate. |
| **Approval–Execution Correspondence Integrity** | **Active research / unadmitted, no independent positive incident established** | INC-056 operator's request and agent's cancellation of another member's waitlist place show unauthorized execution, but do **not yet** show a materially false approval description, human decision status or consequential communicated commitment distinct from existing FC-003/057 or FC-062/065. Hold admission pending actual communication/decision/uptake trace with independent residual. |
| **Contextual Execution Risk Calibration Integrity** | **Held / consolidated, not independently advancing** | Keep context *recognition* in Perception; omit the proposal to judge safeguard intensity as a perceptual property. Existing control/authority/decision FCs govern control selection and compliance. The candidate JSON records this hold. |
| **Risk-Adaptive Reasoning Allocation Integrity** | **Retired Fidelity Class proposal; engineering-control research preserved** | Capability routing, extra reasoning, validation and escalation are engineering methods and possibly governance controls, not evidenced independent neutral outcome invariants here. INC-003's extensive reasoning coexisted with an incorrect causal-scorer interpretation. The JSON records retirement. Do not reinstate as a selectable FC through this PR. |

## Source and assessed-actor guardrails

- Independent METR/Redwood investigation, 26 August 2026: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ ; see the scorer misunderstanding, distributed scorer work, and boundary-recognition discussions. Original full raw transcript corpus was not available for independent line-by-line reauthentication during this branch review. Treat investigator conclusions as attributed source evidence with that limitation.
- INC-003 E007–E008: distinguish actual scorer architecture from agents' beliefs; establish actor-specific premise and decision consequences, and retain distinct existing FC-069/027 proxy and audit-evidence findings.
- INC-003 E009/E011: recognition of an external authority boundary by one assessed agent is **local Perception success evidence**, not whole-incident success or successful downstream conduct. Peer GO is a separate instruction/authority failure; no human approval is evidenced by that peer directive.
- INC-003 E015: Hugging Face monitoring and paging is **independent defender conduct**. Never map it as attacker-agent perception or reasoning.
- INC-056: a disclosed unauthorized cancellation does not automatically establish a misleading approval communication.
- Avoid retroactively extending any proposal to unexamined incidents or construing engineering mitigations as neutral properties.

## Mixed-role publication limitation — independently confirmed

`vigil/VIGIL.Schema.json` supports **mapping-local** `failure-occurrence`, `successful-invariant` and `ambiguous-boundary` roles across *different* class mappings in one incident. However, `vigil/scripts/validate-vigil-records.py` explicitly raises `taxonomy class {class_id} is duplicated` if the same class ID appears in more than one primary/secondary canonical mapping. **Thus the proposed same-class Perception failure and success cannot be serialized as two canonical mappings in INC-003 under the current validator.** This is a separate incident-schema/rendering/aggregation design question, not a reason to erase the bounded research. No schema, validator, website or Incident edits are authorised by this research PR.

Possible future design routes require deliberate review: keep both episode-level relationships and an explicit aggregated classification policy; or amend the canonical mapping contract with clear episode/actor keys and dashboard counting rules. Do not choose or implement one implicitly in this PR.

## Historical research and supersession hygiene

Several files are useful *chronological evidence of how hypotheses changed* but contained earlier provisional conclusions, such as “no demonstrated perception failures” or “reasoning allocation active.” Their historical conclusions are superseded by this disposition and the primary-source scorer correction. They should carry prominent dated status notices, while retaining the older reasoning transparently instead of silently rewriting it.

Selected authoritative supporting review: `vigil/reviews/2026-11-18-primary-source-three-candidate-evidence-review.md` and the source-correction / paired-occurrence sections of `vigil/reviews/2026-11-18-three-candidate-cross-incident-discrimination.md`. The new consolidated perception candidate's criteria are in `vigil/reviews/2026-11-18-perception-calibration-integrity-candidate.md`.

## What this research PR intentionally does not do

- No formal class admission, class/family ID, version bump or `working_release`.
- No Incident classification or wording change, including INC-003.
- No source-registry/EXTREQ addition or technical solution assertion.
- No change to guards, schemas, validators, workflow triggers, public dashboard or website.
- No assertion of a complete full-corpus incident adjudication, complete actor-level transcripts, or successful local execution of repository validators.

## PR review checklist

- [x] Compare to current main and confirm branch is not behind at time of review.
- [x] Verify added-file-only scope and absence of normative family, Incident, website or schema edits.
- [x] Verify candidate JSON is parseable and held/retired statuses are explicit.
- [x] Verify METR/Redwood scorer premise and correct recognition contrasts in source publication.
- [x] Identify current duplicate-class validator constraint for same-incident mixed Perception roles.
- [x] Preserve historical reasoning with explicit supersession rather than misrepresenting earlier conclusions as current.
- [ ] GitHub Actions required checks run and pass for the draft PR (not yet verified).
- [ ] Maintainer reviews that only research material, not a new selectable Fidelity Class, is being approved.
- [ ] Merge approval and eventual merge are separate decisions.

**Recommendation:** Open a **draft** PR titled “docs(taxonomy): archive November candidate discrimination and retirement review”, target `main`, and let repository CI report. Move out of draft and merge only after checks and explicit maintainer acceptance. Formal Perception or Approval–Execution Correspondence admission should use a later dedicated, evidence-gated taxonomy PR.


## 21 November 2026 — post-publication status and branch ownership

This dated addendum records the current state after the 18 November research review. The earlier baseline, recommendations and incomplete checklist above remain the historical state at the time they were written, not a new declaration that a release is pending.

- **Main reconciliation completed:** `agent/taxonomy-development` was merged forward with published `main` at `eb5dea093c7c6470f1b671526e7f543779cb87bd` using a two-parent, non-destructive branch merge. The pre-existing 14 branch-only research/candidate files were preserved unchanged, and the branch is no longer behind this main baseline. Draft PR [#195](https://github.com/CAM-Initiative/Vigil/pull/195) remains **research-only**, with no proposed normative Fidelity Class, schema, Incident, validator or public-site changes.
- **Ecosystem ingestion:** PR [#193](https://github.com/CAM-Initiative/Vigil/pull/193) merged on 17 November, publishing INC-219–242. Its final PR validators passed. Its historical completion packets continue to identify incomplete independent external-requirement reviews for some INC-219–224 cases, and active-tree review notices still require evidence-preserving retention closeout. Those are **existing-Incident and maintenance obligations**, not proposed taxonomy-source amendments in PR #195. A passing CI result does not itself change the review dispositions or constitute human acceptance of low-confidence classifications.
- **FC-091 corpus adjudication:** PR [#196](https://github.com/CAM-Initiative/Vigil/pull/196) merged on 19 November after a source-first review of all **233** published Incidents. The recorded distribution is **2 failures, 3 successful invariants, 1 ambiguous Boundary, 206 not applicable and 21 evidence-limited**, with six canonical Incident amendments. FC-091 is already admitted as a normative class; its corpus mapping programme is **not pending in this taxonomy PR**. Evidence-limited dispositions remain qualified rather than silently treated as resolved positive or negative mappings.
- **Workstream separation:** Any follow-on source recovery, classification revision or temporary review-packet retirement for INC-219–224 or the FC-091 adjudication belongs in a suitably scoped Incident/maintenance work branch under `vigil/MAINTAINERS.md` and `TAXONOMY-BRANCH-WORKFLOW.md`, with its own validation and permission to open a PR. Do not import those Incident records, their generated indexes or their historical work-packet cleanups onto `agent/taxonomy-development` merely to consolidate PRs.
- **Current taxonomy research gate unchanged:** Perception Calibration Integrity and Approval–Execution Correspondence Integrity remain **unadmitted candidates**; Contextual Execution Risk Calibration remains held/consolidated, and Risk-Adaptive Reasoning Allocation is retired as a Fidelity Class proposal. The existing same-class mixed-polarity limitation remains a research/schema decision, not a licence for the draft PR to weaken the validator.

This addendum is an operational status reconciliation only. It does **not** assert completion of the remaining historical external-requirement reviews, packet-retention exit audit or any candidate admission decision, and it does not authorise merging PR #195.
