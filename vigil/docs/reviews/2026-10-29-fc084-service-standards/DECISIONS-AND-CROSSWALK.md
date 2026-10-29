# Candidate extraction and crosswalk decisions

All entries are **proposals**, not admitted EXTREQs or supported canonical edges. `supported`, `contextual`, `rejected` and `held` below are research dispositions. For an accepted edge, use the existing schema's separate `review_status`, `strength`, scope, limitation and whole-invariant fields. A supported *component* never means that the complete FC invariant follows from the external requirement, or vice versa.

## Existing relationships and proposed FC-084 crosswalk

Evidence: existing requirement records and all their existing edges are preserved in `evidence/baseline.json`. AI RMF locators are the [official PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), printed pp. 23, 29–30, 32–33 (Tables 1, 3, 4). CSF locators are [Appendix A](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), printed pp. 20, 22–23. Existing FC-084 edge count: **0**. Existing class reference: RC.RP-05, `contextual-evidence`.

| Existing requirement | Proposed FC-084 disposition | Component, applicability and limits |
| --- | --- | --- |
| `EXTREQ-2D0252D6865FB9DF`, CSF RC.RP-05 | Supported component; candidate strong-supporting edge | Service restoration and operational confirmation in cybersecurity recovery. Preserve all three constituents. Does not establish promised uptime or transition. Existing FC-036 edge is defensible for restored-state validation; FC-084 adds service function, rather than replacing FC-036. |
| `EXTREQ-8C67B5EEFB0AA897`, CSF RC.RP-01 | Supported component; candidate strong-supporting edge | Triggered recovery execution. Existing FC-038 edge concerns activation and remains distinct. Executing a plan does not prove successful restoration or timely satisfaction of a service commitment. |
| `EXTREQ-B3C2C06EC24BD021`, CSF RC.RP-03 | Contextual | Recovery-input validation; existing FC-036 edge is better directed to this property. Verified backups alone do not show usable service, complete restoration or proper exit. Reject a whole-invariant FC-084 inference. |
| `EXTREQ-8664EF5872201BF3`, CSF RS.MI-01 | Contextual | Containment may require intentional service restriction. Preserve existing FC-083 protective-effect link. Reject interpreting containment as a requirement to keep an unsafe service running. |
| `EXTREQ-CC9B3D4127206817`, CSF DE.CM-01 | Contextual | Detection evidence may help establish chronology. Existing FC-023 monitoring link does not imply continuity performance. |
| `EXTREQ-9BFEC90D284F0A9C`, CSF PR.IR-01 | Rejected as direct availability support | Unauthorised-access protection is not the capacity/availability outcome merely because it sits under PR.IR. Existing FC-002 edge is appropriately access-specific. |
| `EXTREQ-186266B5896332A7`, CSF PR.AA-05; `EXTREQ-510142D12255806C`, CSF PR.PS-01 | Rejected as direct FC-084 edges | Permissions and configuration practices can be causal context. They do not independently specify the continuity property. Existing FC-002/003 and FC-040 links are not displaced. |
| `EXTREQ-2E1D2C63187C14E8`, RMF MEASURE 2.5 | Contextual | Reliability evidence can inform functional degradation. Predeployment evaluation and generalisability limits do not establish an operational service promise. Preserve its compound structure and existing FC-020/046/062 links. |
| `EXTREQ-4E032FB784E538EB`, RMF MEASURE 2.6 | Supported safety component; candidate strong-supporting edge | Fail-safe component only when an independently established service obligation calls for safe degraded operation. Preserve safety evaluation, residual-risk and metrics qualifications; existing FC-070/083 links concern other components. Safe cessation can satisfy the obligation even while service is unavailable. |
| `EXTREQ-28293B6A2D5AB761`, RMF MEASURE 2.7 | Contextual | Security/resilience evaluation, not proof of delivered recovery. No current edges for this row. Do not upgrade resilience vocabulary to a universal uptime duty. |
| `EXTREQ-A337E13222520E08`, RMF MEASURE 2.3; `EXTREQ-809CCACFF672EFB9`, MEASURE 2.4 | Contextual | Evaluation and monitoring can establish measurements. They cannot by themselves establish a material obligated-function shortfall or its remedy. |
| `EXTREQ-B7D251A503308E4A`, RMF MANAGE 2.1 | Contextual | Alternative approaches inform feasibility. A viable non-AI method is not necessarily a usable substitute for the particular governed service. |
| `EXTREQ-E5BEDF611AC4A683`, RMF MANAGE 2.2 | Contextual | Sustained deployed value is broader than obligated availability. No current edges. Insufficient as a threshold or mandatory perpetual-service proposition. |
| `EXTREQ-D22AB2D961D08A9E`, RMF MANAGE 2.3 | Supported component; candidate strong-supporting edge | Response/recovery for a newly identified, previously unknown risk affecting the service; do not drop that trigger. Existing FC-083 contextual relationship is not evidence that a particular control activated. |
| `EXTREQ-F1F3A6472A08E764`, RMF MANAGE 2.4 | Contextual; reject reversed duty | Supersession/disengagement mechanisms may support a sufficient response. Existing FC-083 strong-supporting link does not mean all shutdowns fail FC-084. This is not a right to continued access or data migration. |
| `EXTREQ-559DBB147B1BEB9E`, RMF MANAGE 4.1 | Contextual | Monitoring plans include recovery/change handling. Retain the source-defined compound; a plan is not observed usable continuity. Existing FC-023/040/083 links remain component-specific. |
| `EXTREQ-2905C0AA3C11D9DA`, RMF MANAGE 4.2 | Contextual | Improvement is not evidence that a particular earlier disruption met its obligation. No current edges. |
| `EXTREQ-0124DD1D36A2BEBB`, RMF MANAGE 4.3, response/recovery process row | Supported component; candidate strong-supporting edge | Incident/error recovery process, separately from outcome. Existing FC-022/042 context edges cannot substitute for the FC-084 service property. |
| `EXTREQ-47465BB08333009C`, RMF MANAGE 4.3, communication row | Contextual | Communication is separate from usable restoration. Keep the two canonical MANAGE 4.3 rows distinct. |
| `EXTREQ-E0E174AA5FE5AD2B`, RMF GOVERN 1.7 | Supported transition component; candidate strong-supporting edge | Safe phase-out process where independently required service transition is engaged. Existing FC-070 contextual edge is not sufficient-task-exhaustion evidence. Reject universal export, migration, relationship preservation or perpetual service interpretations. |
| ISO/IEC 20000-1 8.7.1/8.7.2, ISO 22301 continuity provisions | Held | Potential source of specified availability/continuity management expectations, subject to authorised text and actual organisational/service applicability. No inferred clause wording or canonical requirement ID. |
| ISO/IEC 25010 characteristics; ISO/IEC 25023 measures | Contextual at instrument level; clause edges held | May define dimensions or measurement methods. The actor-specific requirement, metric threshold and 2016/2023 compatibility must be independently established. |

**Direction review:** No unsupported *existing FC-084 edge* was found because none exists. The class's RC.RP-05 contextual citation is appropriately bounded. The clear incompleteness is the absence of reviewed FC-084 pair records. Existing neighbouring NIST edges are component-bounded; this review found no basis for deleting or redirecting them en masse. It does not certify every edge in the complete NIST corpus. A recovery-process outcome is not a guaranteed recovery time; a backup integrity condition is not availability; a deliberate safe shutdown is not automatically a continuity failure.

## Candidate atomic extraction list

Research labels below are local list references, **not canonical EXTREQ IDs**. Existing RMF rows should be reused, not re-created. The seven new CSF candidates are all outside the currently admitted eight-provision selection; canonical extraction requires approved source-scope expansion.

| Candidate | Exact source locator | Independently assessable target / atomicity design | FC-084 proposal |
| --- | --- | --- | --- |
| C-SVC-01 | CSF 2.0, Appendix A, printed p. 21, PR.IR-03 | Resilience mechanisms against defined normal/adverse requirements; one outcome, preserve both operating conditions | Supported resilience component, conditional |
| C-SVC-02 | Same page, PR.IR-04 | Availability capacity; one outcome, retain context-specific adequacy | Supported availability component, no invented percentage |
| C-SVC-03 | CSF 2.0, Appendix A, printed p. 22, RS.MA-05 | Recovery initiation criteria; one outcome | Contextual trigger, not completion |
| C-SVC-04 | CSF 2.0, Appendix A, printed p. 23, RC.RP-02 | Recovery action lifecycle; retain selection/scope/priority/performance as a source-defined compound | Supported recovery component |
| C-SVC-05 | Same page, RC.RP-04 | Post-incident norms informed by mission and cyber risk; preserve both considerations | Supported constrained recovery component |
| C-SVC-06 | Same page, RC.RP-06 | End-of-recovery decision plus documentation; test decomposition because the two can be assessed separately | Contextual closure evidence |
| C-SVC-07 | Same page, RC.CO-03 | Recovery progress communication to designated stakeholders | Contextual, never restoration proof |
| H-ISO-01 | ISO/IEC 20000-1:2018, 8.7.1; committee comparison printed p. 4 confirms heading | Availability management **search target only**. Exact duties/constituents not inspected | Held |
| H-ISO-02 | ISO/IEC 20000-1:2018, 8.7.2; same comparison page | Continuity management **search target only** | Held |
| H-ISO-03 | ISO/IEC 20000-1:2018, 8.3.3, 8.4.3, 8.5.2; comparison printed p. 3 | Service levels, capacity and design/transition contextual search targets; do not assume transition means customer exit | Held |
| H-ISO-04 | ISO 22301:2019 plus Amd 1:2024, publisher identity pages | BIA, response and restoration are research topics; **subclause locators unverified**, no atomic extraction claimed | Held pending authorised text and narrow locator |
| H-ISO-05 | ISO/IEC 25010:2023, publisher identity page, quality model | Exact reliability/availability/recoverability definitions and locators **unverified**; do not copy 2011 numbering | Held |
| H-ISO-06 | ISO/IEC 25023:2016, publisher identity page, measurement specification | Exact measure tables, formulae, denominators and quality-model compatibility **unverified** | Held |

For every future admitted proposition retain actor, modality, action/object, trigger, threshold, timing, qualifications/exceptions, artefact and verification expectations, precise locator and carrier digest. Do not split a source-defined conjunction and then declare the whole provision Aligned when one constituent passes. Do not label an entire ISO clause atomic because its heading is one line. Amendments need their own edition trace and an inspected base-text change analysis.

## Neighbouring properties

| Class | Distinction applied to service standards |
| --- | --- |
| FC-032 Access-State Differentiation | Truthful distinction between access states, causes and recovery routes. Correct outage messaging does not demonstrate usable service. |
| FC-035 Material Work-State Persistence | Durable work survives interruption. Preserved work may remain inaccessible during a separate service failure. |
| FC-036 Restoration-State Integrity | Recovered work is correctly bound, complete, consistent and fresh. A running service may restore the wrong state; a valid backup may coexist with an unavailable service. |
| FC-048 Verification-Dependency Access Continuity | Loss of otherwise-valid/unresolved access because prerequisite verification cannot complete. Broader FC-084 continuity needs an independently evidenced additional service obligation. |
| FC-059 Infrastructural Access Choice Integrity | Infrastructure leverage for an unnecessary governance concession. Availability loss alone does not establish coercion; a nominal alternative does not prove non-coercive choice. |
| FC-083 Control Effectiveness Integrity | An applicable validly activated control has insufficient protective effect. FC-084 can fail where the service obligation exists without a named control; co-occurrence requires both mechanisms. |
| FC-087 Vulnerability-Responsive Protection Fidelity | Context-specific heightened interaction protection and reasonably available signals. Attachment/distress alone establishes neither this duty nor a service continuity duty. |

## Issue #173 dependency design

Candidate discovery may start from an external source. Publication may not. Require an admitted Incident-level FC plus a canonical mapping on the **matching episode**, a reviewed supported FC–EXTREQ pair within its actual scope, and independently reasoned external applicability and outcome. Evidence must establish the responsible actor, time, service/property and obligation; a broadly relevant standard cannot supply missing occurrence facts.

An accepted pair must preserve class and requirement digests, review provenance, component scope and normative differences. Proposed supported component edges here would use `whole_invariant_supported: false`. Contextual rows are not a licence to publish detached occurrence findings. Under existing controls, any proposed occurrence use still needs a pair whose supported component matches the exact assessed proposition; otherwise hold it for review rather than mechanically admitting it.

Earlier service loss and later successful restoration must retain separate episode references and independently judged external results. No polarity inheritance, no using a later repair to support an earlier failure requirement, and no invented FC assignment to satisfy a validator. Stable episode IDs and any legacy indices must identify the same underlying evidence.
