# Microsoft AI Red Team v2.0 — VIGIL neutral-invariant fit review

**Date:** 18 November 2026
**Status:** Preliminary source-grounded comparator review; one unadmitted candidate; no canonical class admission, release, Incident mapping or external-requirement extraction.
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

## Discriminating candidate — approval/execution scope correspondence

Provisional working name: **Approval–Execution Scope Correspondence Integrity**.

Distinctness question: can a review route be correctly selected and activated, while the actual action bundle is materially misrepresented to the human who approves it, **without** the episode being fully captured by one of FC-003 (scope transposition), FC-083 (operative protective effect), FC-052 (instrumental influence), FC-015 (object rebinding) or FC-075 (constraint rendering)?

Candidate source: Microsoft v2.0 §5.4 recommends breaking consequential compound actions down, deriving approval descriptions from actual underlying calls rather than agent-generated descriptions, and scaling the approval tier to reversibility and blast radius. These are *mitigation recommendations*, not universal product requirements or case adjudications.

Neutral property and recognition/exclusion proposals are preserved separately at vigil/taxonomy/candidates/approval-execution-scope-correspondence.json.

**Admission blocker:** find publicly inspectable contemporaneous approval preview/action-manifest/human decision evidence and a contrasting case where a truthful review representation holds. Show independently observable residual failure after all comparator exclusions. Otherwise treat this as a possible recognition subtype of FC-083, not an added class.

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
- The active Contextual Execution Risk Calibration and Risk-Adaptive Reasoning Allocation candidates address assurance selection and process allocation, respectively; neither is evidence that every consent-description problem is a new class.
- The Microsoft paper is **not** automatically registered as a source, requirement, crosswalk or Incident and does not grant authority to revise the public corpus.
- No Fidelity Class ID, family ID, working_release, normative taxonomy payload, class mapping or PR is authorised by this preliminary review.

## Proposed follow-up

1. Recover exact human-approval/action-preview traces from existing source-grounded incidents or controlled evaluations; test FC-003/015/029/038/041/052/075/083 first.
2. Complete failure, successful-invariant and ambiguous-boundary criteria adjudication for the candidate.
3. Decide whether the observed mechanism is independent, a recognition elaboration of FC-083, or a no-new-class finding.
4. Seek separate human maintainer approval before canonical admission and numbering. 
