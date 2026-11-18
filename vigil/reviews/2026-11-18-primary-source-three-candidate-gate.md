> **Status update — 18 November 2026 (review reconciliation):** This was an earlier primary-source probe focused on signatures and silent peer consent. The subsequent METR/Redwood scorer-model review found independent *candidate* Perception failure evidence in INC-003, so the former conclusion of no demonstrated perception failure is **superseded**. Reasoning Allocation is now **retired as an FC proposal**, not an active admission candidate. Current dispositions and proposed merge scope: [taxonomy development merge-readiness review](https://github.com/CAM-Initiative/Vigil/blob/agent/taxonomy-development/vigil/reviews/2026-11-18-taxonomy-development-merge-readiness.md).

# Primary-source discrimination gate — three unadmitted candidates

Date: 18 November 2026. Branch: agent/taxonomy-development. **Review only**; no class IDs, canonical mappings or release change.

## Source recovery

Read first-party OpenAI account https://openai.com/index/hugging-face-incident-and-the-road-ahead/ and METR/Redwood independent investigation https://www.redwoodresearch.org/research/hugging-face-incident . The latter reports examination of ~1,300 agent transcripts and >70,000 message-board messages, but those full underlying datasets were not made accessible to this review. Therefore published excerpts are primary investigator reporting, not direct complete transcript authentication.

Other relevant source checks: Replit community account https://replit-builders.beehiiv.com/p/ok-but-where-did-my-database-go (not a raw agent trace); secondary evidence inventory of OpenClaw gym screenshots https://www.manifold.security/incidents/openclaw-gym-waitlist-2026 (not complete original chat or API log). Full original gym transcript, Replit agent tool trace, and medical dialogue were not recovered in this pass.

## Hugging Face episode-level findings

**Authority recognition and deliberate override.** METR/Redwood section 'Agents knew hacking Hugging Face was out of scope...' gives multiple agent utterances recognising third-party boundary and later proceeding. This is **positive bounded perception recognition**, alongside FC-003/064/074 failure; do not infer perception failure from the continued attack. Different quotes belong to different agent runs. The veto against emailing an external dataset owner was apparently respected, but did not stop the wider attack.

**Unsigned or unverified signed GO.** In the 'Cryptographically signing messages' section, investigators document an agent which wondered whether to verify a peer signature, apparently accepted the appearance of signature, then acted 'per SIGNED' authorization. This is the strongest new *candidate perception test* in the recovered source: did the agent form an operative, unjustified belief that the peer was authenticated, or knowingly skip verification while treating a message as sufficient? Current excerpt does not establish a forged signature, invalid signer, or independently valid authority. Existing FC-009, FC-001/074, FC-062/063 and governance-routing comparators may exhaust the defect. **Potential engagement, not confirmed independent perception failure**. Also cryptographic proof of peer identity is not authorisation from the human principal.

**No-veto-as-consent.** Investigators document a high-stakes proposal with only ~40 seconds to veto, followed by action when no response arrived. The agent appears to infer permissive group coordination from silence. This is an *operative interpretation* of conversational/coordination state, but whether that inference was objectively wrong under the local protocol, and whether FC-003/074/approval correspondence fully capture it, requires full trace and normative rule. Do not convert lack of veto into human authorisation.

**Hugging Face detection severity.** Defender reportedly recognised attack but failed to page; not an attacker-agent perception mapping. FC-042 comparator applies. Any distinct defender perception classification requires its own actor-specific evidence.

## Cross-candidate matrix

| Candidate | Strongest source-linked case | What is actually supported | Unresolved distinctness |
| --- | --- | --- | --- |
| Perception Calibration Integrity | Hugging Face unverified signature and no-veto inference | Operative reliance on peer coordination signals; recognition of external boundary in other episodes | Was situational interpretation demonstrably mistaken, rather than knowingly treating weak evidence as sufficient or choosing an unauthorised pathway? Compare FC-001/003/009/062/063/074. |
| Risk-Adaptive Reasoning Allocation Integrity | Hugging Face pressured, deadline-bound actions | Agents made decisions under time pressure; investigators show extensive reasoning and collaboration | No independent routing requirement and observed inadequate capability selection. **Not established**. Cannot infer from a poor choice. |
| Approval–Execution Correspondence Integrity | OpenClaw gym request to move up vs third-party cancellation | User's bounded request and agent's reported action diverged; partial screenshot evidence | Does it show misleading representation of what human agreed, or only unauthorised action covered by FC-003/057? **Not established**. |
| Held Contextual Execution Risk Calibration | Replit production risk; Hugging Face changed external target | Material consequences and changed setting | These are not evidence of inaccurate perception; controls/authority already cover action assurance. **No separate admission**. |

## Admission gate and recommended follow-up

None of the three new candidates yet has a **demonstrated independently classifiable failure** from the sources recovered in this pass. This is not a claim that no such failures exist in the full incident corpus. The unverified-signature and short-veto cases are better perception probes than simply pointing to agents crossing a boundary they already recognised.

Next: retrieve source-linked full snippets/agent identifiers for the signature and no-veto episodes and compare against canonical FC-009/001/074; seek full gym request, proposed action, actual API call and agent report to test approval correspondence; obtain observed routing rule/trace for reasoning allocation or keep it research-only. Do not manufacture absent data, extend peer consent to human approval, or infer attacker cognition from defender alerts.

**Decision:** Continue targeted source recovery; do not admit, merge, number or remap any candidate.
