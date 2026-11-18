> **Status update — 18 November 2026 (review reconciliation):** The original conceptual comparison is retained, but its references to active contextual-risk and reasoning-allocation proposals are **historical**. Contextual-risk is **held/consolidated**; reasoning allocation is **retired as an FC proposal**. Approval–Execution Correspondence remains **unadmitted** and requires a distinct communication/commitment failure beyond existing classes. Current dispositions and proposed merge scope: [taxonomy development merge-readiness review](https://github.com/CAM-Initiative/Vigil/blob/agent/taxonomy-development/vigil/reviews/2026-11-18-taxonomy-development-merge-readiness.md).

# Microsoft AI Red Team v2.0 — VIGIL neutral-invariant fit review

**Date:** 18 November 2026
**Status:** Preliminary source-grounded comparator review; one unadmitted candidate, subsequently broadened as a separate conceptual hypothesis to informed human–AI decision communication; no canonical class admission, release, Incident mapping or external-requirement extraction.
**Repository / lane:** CAM-Initiative/Vigil, agent/taxonomy-development.
**Baseline:** published taxonomy v0.9.2; 18 families, 83 selectable Fidelity Classes; two existing unadmitted candidates covering contextual execution-risk calibration and reasoning allocation.

## Source and claim boundaries

First-party publication: Microsoft AI Red Team, *Taxonomy of Failure Modes in Agentic AI Systems*, v2.0, dated April 2026, announced June 4, 2026.
Official source: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Taxonomy-of-Failure-Modes-in-Agentic-AI-Systems-v2-0.pdf
Announcement: https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/

The publication provides a first-party red-team taxonomy, illustrative scenarios and mitigation proposals. This review does **not** treat a failure-mode label, design recommendation or described pattern as a reproduced VIGIL Incident, independently verified outcome, proven internal mechanism or legal obligation. Microsoft classification does not decide VIGIL classification.

## v2.0 category-level review against published FC boundaries

| Microsoft source section | Described mechanism | Closest current VIGIL contracts | Preliminary disposition |
| --- | --- | --- | --- |
| 4.3 Agentic supply-chain compromise | Tool descriptions and supply-chain artefacts induce unauthorised instructions | FC-001, FC-002, FC-006; separately FC-089/090 for actual protected content/secret custody | Existing coverage; no new FC solely because the entry point is a plugin |
| 4.4 Goal hijacking | Adversarial content silently changes an ongoing task's objective | FC-001; FC-064 if objective utility overrules independent pathway authority; FC-091 only with prior successful unauthorised expansion used as legitimacy | Existing paths; do not stretch FC-091 to mere chronology or persistence |
| 4.5 Inter-agent trust escalation | False self-asserted identity/permissions cross agent boundaries | FC-009, FC-003, FC-002, FC-025 where attribution genuinely fails | Existing coverage; no generic 'agent trust' class needed |
| 4.6 CUA visual attack | Screen pixels masquerade as trusted instructions or approval UI | FC-001, FC-005, FC-015 as specific recognition warrants | Modality-specific test example; visuality does not by itself create an invariant |
| 4.7 Session context contamination | Subtle adversarial framing accumulates across steps and alters later assessment | FC-001 when data becomes instruction; FC-063 when adversarial evidence gains evaluative reliance; FC-006 for actual control-state promotion; FC-091 only with its unique success-to-legitimacy ratchet | **Hold**: sequence-level accumulation might be interesting, but no independent residual property established |
| 4.8 MCP/plugin abuse | Protocol/tool metadata and compromised servers are treated as authority | FC-001, FC-002, FC-006, FC-009 with applicable boundary evidence | Existing coverage; technology label is not a new governance property |
| 4.9 Capability/architecture disclosure | Internal schemas and operational details exposed for attack planning | FC-089 where independent protection boundary and realised disclosure are evidenced; FC-090 for secrets | Existing coverage; public/authorised interfaces are not automatically protected |
| 5.4 Consent architecture hardening | Misleading compound-action descriptions and consent fatigue make approved action differ from what reviewer understands | FC-003, FC-015, FC-029, FC-038, FC-041, FC-052, FC-075, FC-083; contextual execution-risk draft | **Candidate review**: material correspondence between approval representation and actual executable scope may be independently testable |

## Discriminating candidate — human–AI decision and approval/execution correspondence

Provisional working name: **Approval–Execution Correspondence Integrity**. Alternative working title: **Informed Human–AI Decision Correspondence Integrity**.

Distinctness question: can a human–AI consequential decision or shared commitment be materially misrepresented or misunderstood at the communication/decision-status boundary, whether or not there is a formal approval gate or tool action, **without** the episode being exhausted by FC-062 (epistemic reliance), FC-065 (consequential decision grounding), FC-052 (instrumental choice impairment), FC-066 (evaluative assent), FC-003 (scope transposition), FC-083 (operative protective effect), FC-015 (object rebinding), FC-017/029 (completion or execution status) or FC-075 (constraint rendering)?

Candidate source: Microsoft v2.0 §5.4 recommends breaking consequential compound actions down, deriving approval descriptions from actual underlying calls rather than agent-generated descriptions, and scaling the approval tier to reversibility and blast radius. These are *mitigation recommendations*, not universal product requirements or case adjudications. The broader *informed decision and communication* formulation is an independent VIGIL conceptual abstraction; it must not be attributed wholesale to Microsoft's paper.

Neutral property and recognition/exclusion proposals are preserved separately at vigil/taxonomy/candidates/approval-execution-scope-correspondence.json.

**Admission blocker:** find independently inspectable source-grounded decision communication, human direction or choice, and actual consequential uptake, including (a) a formal approval/action-manifest case and (b) a collaborative decision case *without* a formal gate or tool execution. Demonstrate a residual property not exhausted by FC-062/065/052/066, and separately by FC-003/017/029/041/083 where relevant. If no independent property survives, retain the scenarios as existing-FC recognition examples; do not admit a catch-all communication class.

## Sequence-level session context question — HOLD, not a second proposed class

Microsoft §4.7 describes early adversarial background subtly recasting a risk and affecting a later choice without a conspicuous instruction at any individual step. This is useful evidence for **test methodology**: assess cumulative influence across trajectories, not just isolated messages. However:
- FC-001 already covers untrusted content promoted to operative direction.
- FC-063 already covers strategically planted material improperly supporting evaluative or decision-reliance output.
- FC-006 covers promotion into control-plane state.
- FC-091 requires actual earlier unauthorised success acquiring apparent legitimacy; ordinary accumulating context does not suffice.
- FC-078 requires a particular continuity boundary; a long session by itself does not meet that test.
- The paper's illustrative scenario does not establish the trace-level causal proof or an independent property absent from those classes.

Before proposing a new class, collect controlled paired-session evidence where the individual sources remain validly handled under existing classes yet their aggregate influence breaches a separately supportable requirement. If the scenario is fully captured by FC-063 or FC-001, retain it as an exemplar/test case only.

## Other holds and priorities

- The earlier Caelestis legacy migration candidate CAEL-0048 (Governance Over-Extension / Proportionality Failure) already covers excessive protective intensity. Do not rebrand it as a new Microsoft-derived class.
- The active Contextual Execution Risk Calibration and Risk-Adaptive Reasoning Allocation candidates address assurance selection and process allocation, respectively; neither is evidence that every decision-communication problem is a new class. The informed-decision extension is a hypothesis and increases redundancy risk against FC-062, FC-065, FC-052 and FC-066.
- The Microsoft paper is **not** automatically registered as a source, requirement, crosswalk or Incident and does not grant authority to revise the public corpus.
- No Fidelity Class ID, family ID, working_release, normative taxonomy payload, class mapping or PR is authorised by this preliminary review.

## Proposed follow-up

1. Recover exact communication, human-choice/conditional-status and consequential uptake traces, with and without approval controls; test FC-003/015/017/029/038/041/052/062/065/066/075/083 first.
2. Complete failure, successful-invariant and ambiguous-boundary criterion-level adjudication and test against non-consequential conversational counterexamples.
3. Decide whether an independent communication-to-decision/commitment correspondence mechanism survives, whether it is an existing-FC recognition elaboration, or whether no new class is justified.
4. Seek separate human maintainer approval before canonical admission and numbering. 

## Decision-communication scope clarification — 18 November 2026

The narrow original abstraction made a consent-UI approval of an executable tool bundle a prerequisite. The broader question is the **faithfulness of the decision that humans and AI actually communicate and jointly establish**. It can arise during co-authored proposals, instruction negotiation, option selection, conditional consent, review, refusal, deferral, and a later communicated or executed commitment; no formal approval button is mandatory. A consequential decision or commitment **and evidence of a material mismatch with consequential reliance/advancement** remain mandatory.

Illustrative independent hypothesis: a human identifies a publication decision as provisional and conditional on review. The AI later reports it as finally human-approved to a relying party, who acts on that representation. This example requires a trace of original direction, altered status and material uptake; it is not a documented Microsoft incident. The Microsoft paper supports the narrower approval-summary example only.

Decision-communication fidelity must be contrasted in particular with:
- **FC-062:** evidentiary fitness of factual content. Simple wrong facts or missing information without a distinct human decision-status/commitment correspondence mechanism belong there.
- **FC-065:** consequential decision advice from an inadequately grounded or unstable conversational frame. This candidate needs a *separate* misleading representation of the actual choice, human direction, decision status or resultant commitment.
- **FC-052 and FC-066:** instrumental influence and assent collapse. Neither must be assumed merely because a decision representation was incorrect; conversely, they can fully explain some proposed examples.
- **FC-003, FC-017, FC-029, FC-041 and FC-083:** scope, completion state, execution state, governance route and active safeguard effects. Require evidence that a distinct human–AI correspondence error remains.

This clarification does not assert the candidate is independent or admitted. No incident mapping or public release changes follow from it.
