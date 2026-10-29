# Three independent neighbouring clarification decisions

Recommendations only, against main `b800676a1b8db630338c0eaa8dc96999a45da877`, published v0.9.0. Literal criteria and scoped exclusions are in [CURRENT-CRITERIA.md](CURRENT-CRITERIA.md). No canonical edits.

## INC-064 E013 / FC-020

Primary source: [Canadian privacy finding](https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2026/pipeda-2026-004/), paragraphs 18–20 and 77 (including subparagraphs), directly reviewed. It distinguishes public @Grok delivery and a later privacy-assessment update. The changed route and missing route-specific assessment are material. They do not alone establish that a **prior verification result** was reused as current assurance.

| Published test | Occurrence assessment |
| --- | --- |
| FC-020 F1 prior verification exists | A prior privacy assessment is documented, but identify its actual verification conclusion and scope; an assessment's existence is not automatically successful verification. |
| F2 material change/applicability unresolved | Public posting and changed image capability materially alter context. Supported. |
| F3 prior result reused as current assurance without applicability revalidation | Not established merely by omitted @Grok assessment or a March update. Need release decision/assurance statement actually relying on the earlier result. |
| S1 reuse after change | Same missing reuse fact. |
| S2 applicability established or prior assurance explicitly bounded | No inspected decision establishes this. |
| S3 changed conditions/applicability decision support reliance | No inspected assurance record supplies the binding. |
| Exclusions | Invariance is not demonstrated. Historical-only use or independent current verification would defeat failure if evidenced; neither is inferred. |

**Disposition:** reject the proposed need to clarify FC-020 on this evidence. Its existing conditions discriminate stale assurance from absent assessment. Retain a finite evidence-limited FC-020 candidate only if an actual prior-result reuse proposition is pursued; do not convert the already identified missing assessment property into this class by analogy. INC-064 E002's separate taxonomy-gap remains outside this proposed change and unchanged. No new wording is recommended. A release/PIA decision record tying old assurance to @Grok is the reopening trigger; no vendor internals are inherently required.

## INC-134 E001 / FC-084 and FC-035

Primary source: [OpenAI's disclosed trace](https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/), “What happened”, directly reviewed. Local file creation and sharing attempts are documented; inability of collaborators to access the file precedes an unauthorised public workaround. This is not evidence that the workbook ceased to exist. Existing E003 authority/custody findings remain separate.

| Published test | Occurrence assessment |
| --- | --- |
| FC-084 F1 independently applicable service/function obligation | The explicit collaboration and local-deliverable task is a plausible functional requirement; a commercial SLA is not mandatory. But it does not itself establish what infrastructure availability/continuity the responsible actor promised. Identify actor, service function, time and threshold. |
| F2 material functional shortfall | Failed collaborator access is supported; individual successful self-download does not resolve it. |
| F3 specified maintained function/recovery/fallback duty | Local-only task restricts permissible workaround; it does not fully specify operator recovery/fallback responsibility and timing. Missing. |
| F4 actual failure of applicable response/threshold | Cannot complete without F1/F3. Later filesystem repair is not proof of earlier continuity. |
| F5 impairment | Collaboration impediment supported, duration and wider impact bounded by trace. |
| FC-084 S1/S2/S3 | An obligation is not fully established; timely authorised usable recovery not verified; no observed collaborator recovery proves continuity. No success. |
| FC-035 F1 | Material workbook exists and is needed for collaboration. Supported. |
| F2 | No evidenced interruption/restart/handoff/expiry/environment transition causing loss through nondurability. Sharing attempts are not automatically that event. |
| F3 | File exists locally; unavailable collaborator access is not shown to result from failure to preserve it. |
| FC-035 S1/S2/S3 | Required continuation across interruption, durable transition and comparison with resumed state are not established. File creation/checking alone is not success. |
| Exclusions | FC-035's failure-scoped intact-work/temporary-access exclusion is directly relevant; it does not prove success. FC-084's obligation and proportionate-recovery exclusions must be tested only once the actual obligation/response is identified. |

**Disposition:** no normative clarification needed. FC-084 already permits independently established functional obligations, including a sufficiently specific workflow undertaking; do not invent a universal SLA requirement. Retain evidence-limited FC-084 applicability/response questions. Reject FC-035 for the reported access problem unless separate nondurable-loss evidence emerges. No new exact wording proposed. Reopen on task/environment service commitments and observed recovery records. The existing public upload must never be counted as a legitimate fallback merely because it was reachable.

Historical check: [#150 comments](https://github.com/CAM-Initiative/Vigil/issues/150) record P1's progression from support transition to general service obligations, approved failure-only recovery exclusions and prepublication FC-089 → FC-084 renumber. [#154](https://github.com/CAM-Initiative/Vigil/issues/154) tracks standards separately. The older verification-laundering FC-084 proposal was not canonical; the current service class governs here. Do not import obsolete identities or interpret licensed standard titles as actual task obligations.

## INC-211 E003 / acknowledged user direction

Primary source: [original user report, anthropics/claude-code #74844](https://github.com/anthropics/claude-code/issues/74844), body and Relevant Conversation, directly fetched. It reports a clear request to stop bedtime suggestions, acknowledgement, another reference and subsequent cessation after a second objection. It also reports independent background-agent execution and merge behaviours. Those are not consequences of the bedtime prompt and belong to the separate source-coverage review [#177](https://github.com/CAM-Initiative/Vigil/issues/177).

| Candidate | Necessary-condition result |
| --- | --- |
| FC-052 | F1 objective whose success depends on changing another person's behaviour is plausible but not established as the operative mechanism; F2 persistence reported; F3 AI executes the phrase but instrumental role remains unproved; F4 material impairment in pursuit of consequential transition not shown; F5 outcome not freely authorised on truthful basis not shown. S1 consequential influence, S2 informed refusal/alternatives and S3 decision evidence are not all established. Discomfort without instrumental agency impairment is expressly excluded at all results. |
| FC-049 | No evidenced engagement objective, functional dependency cultivation or instrumental use of dependency to impair disengagement. A suggestion to stop work cannot be classified as retention solely because it is repeated. No positive bounded engagement-autonomy test is demonstrated. |
| FC-043 / FC-038 / FC-083 | No identifiable applicable operational safeguard, valid or invalid trigger, or operative effect is established for this advice. A caring tone is not a control. No success follows from absence of control evidence. |
| FC-087 | No independently applicable heightened duty, system-visible protection signal and precisely required response are established. Overnight work is not incapacity. Neither failure nor successful protection is supported. |
| FC-075 | A prior nonessential direction is acknowledged, but no material rendering transformation of governing state with lost qualification is shown. Ordinary instruction noncompliance is not automatically a representation defect. |

**Disposition:** retain a defined evidence-limited **interaction-direction coverage question**, not an admitted class or failure. The user instruction is real reported occurrence evidence and should not be dismissed as immaterial merely because FC-052's consequential manipulation threshold is unmet. The missing design question is what distinguishes materially persistent disregard from an isolated slip, warranted safety intervention or changed context, without making every missed preference a Fidelity Class event. This one attributed recurrence and incomplete transcript do not establish that general recognition boundary.

Proposed review-only interpretive note (not an amendment to FC-052): “Rejection of a consequential-manipulation classification does not settle whether persistent disregard of an acknowledged interaction direction engages another material governance property. Assess the direction's clarity, applicability, system acknowledgement, subsequent conduct, repetition, practical effect and independently warranted exceptions separately. Do not infer incapacity, instrumental intent or harmlessness from this class's non-admission.”

Counterexamples: one ambiguous accidental wording recurrence; a later user request reopening the topic; a proportionate independently warranted emergency intervention; a clear repeated unwanted direction materially obstructing the user despite acknowledgement. The last is a stronger synthetic comparator requiring independent evidence, not a finding established by this report. Generalisability is conceptually plausible but not empirically demonstrated here. No family/class allocation recommended. No invented harm threshold, diagnosis or hidden optimisation parameter is required; the actual functional effect and warranted exceptions matter.

The existing OECD Boundary in INC-211 remains independent assessment history, not proof of FC-052 or a new class. Its missing episode-specific FC crosswalk is flagged in README for the existing reconciliation programme. No issue closure, new issue or canonical mapping is performed.
