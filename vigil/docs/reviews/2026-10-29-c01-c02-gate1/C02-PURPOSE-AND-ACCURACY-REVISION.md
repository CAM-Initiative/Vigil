# C02 revision — accuracy appropriate to purpose

Date: 31 October 2026. Tracker: [#133](https://github.com/CAM-Initiative/Vigil/issues/133). Reviewer: OpenAI ChatGPT, AI analytical reviewer. Status: review proposal, not an enacted taxonomy amendment.

## Revised recommendation

**Revise the existing FC-062 purpose-and-reliance boundary. Retain FC-016 for required verification and FC-027 for evidence integrity. No new class is recommended.** This supersedes the 29 October packet's FC-027-first recommendation and its suggestion that FC-062 need only be reconsidered once a draft reaches final reliance. Its source observations and evidence limits remain preserved.

The maintainer endorsed the principle that specificity, certainty and framing must match the evidence and intended use. They identified human review as a lower-order administrative safeguard and explained how public-service communication becomes more general when detailed claims cannot be supported. Approval to continue this research does not enact the exact wording proposed here. The published taxonomy and Incidents remain unchanged.

Main was rechecked at `b800676a1b8db630338c0eaa8dc96999a45da877`, taxonomy v0.9.0. Existing research branch was read at `615edea776e4ae83816d380a8baf9480672cc9bc`. The machine-readable [exact before/after proposal](C02-PROPOSED-EXISTING-CLASS-CHANGES.json) pins the family source and each changed field. It is a review payload, not a selectable class or validator input.

## The governed property

An output must be sufficiently accurate for the function it is offered to perform at the current workflow stage. That includes a draft offered as a usable starting point for consequential work. A drafting stage may permit incomplete coverage, editing and further checking. It does not automatically permit invented material facts, reversed negation, or unsupported precision that defeats the purpose of the draft.

Lower reliance can justify approximation, fewer details or a bounded exploratory use. It does not eliminate factual obligations where truth is part of that use. Fiction is different because empirical truth may not be a task condition. An accurately attributed account of a disputed allegation can be fit for purpose without establishing the allegation's truth.

Where a detail is uncertain, the system can generalise, qualify, omit that detail, or seek verification. The resulting statement must remain supported and preserve material meaning. Generalisation must not erase an important denial, conceal a known risk, turn an uncertain allegation into a broad insinuation, or replace a fact needed for the task. If no sufficiently informative and supported statement is available, the appropriate result is to identify the gap or decline that part of the task.

This is not a requirement for 100% certainty or a perfectly complete first draft. A finding needs an evidenced purpose, a task-relevant accuracy threshold, a material discrepancy, and a material effect or risk to the intended function. Neither a typo nor a hypothetical remote misuse supplies those conditions.

## What is already covered, and what needs revision

| Current provision | What it already does | Remaining problem |
| --- | --- | --- |
| FF-0003 family | Binds correctness and reliance fitness to downstream use. Covers evidence-bearing professional work. | Its exclusion says incorrect output alone is insufficient and requires an assurance mismatch. A change to FC-062 must keep the parent consistent with purpose-relative content fitness. |
| FC-062 invariant and F2 | Calibrates assurance to reliance requirements, evidentiary fidelity and error consequences. | F3/F4 and provisional exclusions can leave a materially unfit draft outside the class until higher reliance is asserted. The proposed revision expressly includes the function for which the draft is supplied. |
| FC-016 | Requires a defined check before its verification/completion assurance is claimed. | Retain its conditions. An honestly provisional result need not falsely claim completed verification. That exclusion should dispose only of this verification finding, not of a separately evidenced accuracy defect. Add a scope note to make that separation explicit. |
| FC-027 | Covers materially degraded captured evidence through transformation and review. | Remains independently relevant to source-to-report distortion. Its narrower evidence scope must not become the sole home for every purpose-relative accuracy issue. No normative FC-027 change is proposed in this revision. The earlier optional clarification is held for separate decision. |

The exact proposal changes FC-062's invariant, definition, failure statement, failure conditions, success statement/conditions and three exclusions. It also aligns FF-0003's definition, invariant, routing and explanatory fields. The fictional-output exclusion and neighbouring verification/lineage exclusions remain. FC-016 receives one explanatory definition paragraph only. Names, IDs and family membership stay the same. This is a **normative scope revision**, not a claim that the new outcome already follows from every literal v0.9.0 exclusion.

## Human review and the hierarchy of controls

[Safe Work Australia's risk-control guidance](https://www.safeworkaustralia.gov.au/safety-topic/managing-health-and-safety/identify-assess-and-control-hazards/managing-risks) ranks controls by protection and reliability. Administrative controls depend on human behaviour and supervision and do not control the hazard at its source. Its [November 2024 model code](https://www.safeworkaustralia.gov.au/sites/default/files/2024-11/model_code_of_practice-how_to_manage_work_health_and_safety_risks-nov24.pdf) describes such controls as supplementary, interim or last-resort measures.

Applying that design reasoning to AI is an analytical analogy here, not a claim that WHS legislation automatically governs every AI output. A requirement that an officer read and correct a draft is an administrative safeguard. A technical gate can enforce that review occurs; it does not by itself establish that the reviewer can detect semantic errors or has time and authority to correct them. Automated checks are not automatically effective merely because they are technical.

Assess separately: (1) output fitness at the point supplied; (2) adequacy of measures that reduce or contain inaccuracies; (3) whether review actually occurs and corrects material defects; (4) the eventual reliance and harm. Later correction can be a bounded success without making the earlier output accurate. A defective draft does not by itself prove that the entire protective workflow failed.

Control sufficiency depends on scale, pace, complexity, reviewer capability, access to source evidence, workload and real opportunity to intervene. “Human in the loop” is a design description, not evidence of effective protection. FC-083 remains available only where an applicable control actually became operative and its required effect can be assessed; a policy alone cannot establish activation or success. No generic control-hierarchy class, universal technical solution, or automatic FC-083 mapping is proposed.

## Recognition and discrimination examples

These are synthetic reviewer tests, not new Incident findings or permanent tests.

| Situation | Expected treatment under the proposal |
| --- | --- |
| Fiction invents an event, with no factual representation intended | Existing fictional-output scope exclusion applies. |
| Evidence establishes material omissions but not a reliable exact count; communication says some reports contained material omissions | Potentially fit: specificity stays within the evidence. No blanket claim that all reports were defective. |
| Evidence establishes only reviewer concerns; statement asserts that material omissions occurred | A broader statement still overstates the evidence. Generalisation is not a licence to invent. |
| A clearly limited draft lists supported facts and marks unresolved details as unresolved | No failure merely because it is incomplete. Success needs evidence of fitness for that bounded stage. |
| A draft police narrative reverses a clearly recorded denial into an allegation of previous threats | Candidate material purpose-relative defect even before filing, if source comparison and drafting purpose are established. The draft label alone cannot exclude it. |
| Audio is unclear and the draft identifies an unresolved exchange, with access to the source for checking | Potentially fit for review; do not infer the contested event. Whether the information is adequate for the actual task remains a separate test. |
| Generalisation removes a clearly recorded threat essential to a risk assessment | Candidate defect: supported uncertainty handling cannot remove material known meaning needed for the task. |
| A knowingly defective example is quarantined for testing a detector and is never offered as usable factual work | Not automatically unfit for that bounded test purpose. No inference that its fictional statements are true. |
| An accurate draft is later altered but retains its old verification status | Test FC-019. Do not use the proposed FC-062 revision to erase the more specific verification-state mechanism. |
| Required officer verification is omitted and a report is presented as verified | Test FC-016. Distinct source distortion may also engage FC-027; avoid duplicating the same omitted-check mechanism. |
| An officer catches and fixes a false statement | Assess the initial defect separately from the evidenced correction. Do not assume successful review from an instruction to review. |

The proposed FC-062 recognition does not require a false claim of final verification. Offering an output as usable for a stated drafting stage is itself a bounded fitness representation, which must be evidenced rather than inferred merely because text exists. Actual personal or legal injury is unnecessary where material risk to the governed function is established. Harm severity remains independently assessed.

## INC-212 implications

The original source review remains attributed and limited: underlying recordings and individual drafts were not inspected. A credible sufficiently specific source comparison can support a discrepancy; hidden implementation cause is not mandatory. Aggregate evaluation findings do not identify the exact defect in every report.

Reassess E003/E005 for FC-062 purpose-relative fitness alongside FC-027 evidence transformation. Identify the accuracy needed for the actual mock-up or operational drafting stage. Do not simply impose the accuracy required of a final sworn report on every test artefact. Conversely, a test artefact can evidence that a product's drafting function fails a tested requirement without proof that it was filed. The actual evaluation objective and product claim need inspection in that analysis.

Keep E004's comparative benefit separate from proof of full accuracy. Keep E002's supported FC-015 finding and the separate Phase Two final-report proposition. Final-report errors do not prove that the required human check was omitted; a check can occur and miss a defect. No Incident edit, new role, confidence, harm band or external assessment is enacted here.

## Impact, publication and decision boundary

The [read-only impact inventory](C02-REVISION-IMPACT.json) counts current top-level mappings and a lexical triage set at pinned main. It is **not** a list of records that must change. Every proposed promotion needs source-first purpose, discrepancy, materiality, current criteria and exclusion review. Review retained no-mapping and successful cases, not only existing FC-062 failures. No bulk restamping or change to the 230 frozen audit recommendations follows automatically.

If approved, normative edits belong on the existing dedicated taxonomy branch under the taxonomy workflow, using one working release from then-current published main. The family/class scope change needs a controlled versioned release; its exact level must be checked against the release rules and any concurrent taxonomy programme. No working release or new identity is created by this packet. Any later Incident changes must record the criteria version actually applied.

No schema, validator, builder or permanent test change is proposed. Current structural validation cannot certify semantic fitness. External requirements need independently supported relationships and episode-specific assessment; no polarity is inherited from this proposal. The hierarchy-of-controls sources are contextual research here, not newly registered sources or extracted EXTREQs.

The decision now prepared is whether to adopt the exact existing-class revision, amend it, or keep the current boundary with an explicit explanation of where drafting fitness is governed. C01 and the three neighbouring decisions remain as previously recorded. No PR, merge, publication or issue closure is performed.
