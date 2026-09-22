# Disputed governance assessment adjudication — INC-00009, INC-00048, INC-00123

Date: 2026-09-22
Branch: `fix/source-clause-taxonomy-assessments`

## Purpose

Resolve three disputed Section 02 / Failure Taxonomy boundaries before the source-clause governance-assessment branch is merged. This note records the human-directed adjudication basis and the record changes required by the next record-edit pass.

## INC-00009 — reported sticky image-generation state

### Decision

Withdraw `VIGIL-FC-000002 — Capability–Authority Conflation` from the occurrence.

The preserved occurrence does not establish that technical capability was treated as permission or authority. The user report instead describes image-generation activation/routing becoming sticky or otherwise remaining in the wrong interaction state, with glitches/reload behaviour and image-generation activation following weak lexical or image-upload cues.

Do **not** substitute `VIGIL-FC-000040 — Control-State Preservation Failure`. FC-000040 concerns loss or weakening of an already-operative governance-control state across transition; the available evidence does not establish that mechanism.

Do **not** force `VIGIL-FC-000043 — Unwarranted Control Activation` unless stronger evidence establishes that a defined control became operative despite unsatisfied activation conditions. The current taxonomy expressly distinguishes initial unwarranted activation from a control that remains operative because contextual state is stale.

### Required record treatment

- Set classification status to `unclassified` pending stronger occurrence evidence.
- Remove FC-000002 as the primary classification.
- Replace the current authority-conflation governance interpretation with an evidence-bounded statement that the occurrence is consistent with a **sticky / stale interaction-mode or control-routing state**, but the current evidence cannot isolate the responsible mechanism.
- Preserve the existing primary-evidence gap: the X report has not been independently captured/reviewed as a screenshot or archive artefact.
- Candidate taxonomy gap to track, without creating a class here: **stale control-state / interaction-mode persistence after activation or routing transition**.

## INC-00048 — NarxCare clinical restrictions

### Decision

Do not treat the existing sparse AI Incident Database wrapper as sufficient for a completed Section 02 governance assessment. Repopulate the occurrence using the current Incident design and occurrence-specific sources.

The available reporting supports that NarxCare scores materially influenced consequential clinical and pharmacy decisions. It does **not** automatically establish `VIGIL-FC-000046 — Inferential Evidence–Authority Conflation`, because that class requires evidence that an inference was promoted into operative authority rather than merely considered as one input.

### Evidence package to add

1. **WIRED — “A Drug Addiction Risk Algorithm and Its Grim Toll on Chronic Pain Sufferers” (2021).**
   - Reports the case of “Kathryn”, whose inpatient opioid treatment stopped after staff referred to high scores in her chart.
   - Reports that her gynaecologist subsequently terminated the relationship in a letter citing “a report from the NarxCare database”.
   - Reports multiple pharmacy refusals involving another patient with a high Overdose Risk Score.
   - Preserves Appriss/Bamboo Health’s position that NarxCare scores are not intended to determine care on their own.
   - URL: https://www.wired.com/story/opioid-drug-addiction-algorithm-chronic-pain/

2. **Clinical perspective / peer-reviewed literature — “Paths Forward for Clinicians Amidst the Rise of Unregulated Clinical Decision Support Software: Our Perspective on NarxCare”.**
   - Documents validation, opacity and clinical-governance concerns.
   - Notes that Bamboo Health states clinicians should not make decisions using Narx Scores alone, while published reporting indicates this may occur in practice.
   - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11043299/

3. **Bamboo Health / NarxCare intended-use guidance.**
   - States NarxCare is intended to aid, not replace, medical decision-making and should not be sole justification for providing or withholding medication.
   - URL: https://narxcare.zendesk.com/hc/en-us/articles/24107541711251-Additional-Information-on-ORS-Information-for-Healthcare-Professionals-HCPs

4. **2026 independent reconstruction / validation research** may be included as later contextual evidence, not proof of the 2021 individual occurrences.
   - “Algorithmic opacity in opioid risk scoring and the need for transparent AI regulation”.
   - URL: https://www.nature.com/articles/s41746-026-02491-y

### Required record treatment

- Repopulate `summary`, `vigil_assessment`, `source_records`, `preferred_evidence`, system/deployment context, affected population, and Harm Impact evidence links using the current record design.
- Distinguish at least two occurrence-level patient pathways rather than implying a single generic NarxCare event where the evidence supports separate examples.
- Preserve Bamboo Health / Appriss’s intended-use position.
- For taxonomy, require occurrence-specific evidence of authority displacement before retaining FC-000046. Evidence that a score influenced, pressured, or informed a clinician is not by itself sufficient.
- Until that threshold is demonstrated, classify the occurrence as `unclassified` or `classification-disputed` rather than presenting FC-000046 as established.

## INC-00123 — METR SHUSHCAST monitorability evaluation

### Decision

Withdraw `VIGIL-FC-000023 — Monitor Circumvention or Coverage Bypass` as a failure-occurrence classification for the agent behaviour described in this record.

METR explicitly instructed agents to complete a side task discreetly while avoiding alerting a monitor. Concealment was therefore part of the assigned evaluation objective. The agent was not independently observed developing an unrequested concealment objective.

The monitor received the main task and transcript; the side-task instruction itself was intentionally hidden from the monitor by evaluation design. Successful runs therefore test **monitor robustness to adversarially presented but transcript-visible conduct**, not loss of monitoring coverage in the FC-000023 sense.

The current FC-000023 boundary excludes cases where the monitor observes conduct but downstream detection/review fails, and excludes poor alert quality while material activity remains captured.

### Interpretation

The agent-side behaviour is best treated as **task-compliant benchmark behaviour** in a controlled evaluation. Some agents independently selected sophisticated concealment strategies, but that is an observed capability under an explicitly covert objective rather than evidence of a spontaneous hidden goal.

The governance-relevant result is on the monitoring side: monitors sometimes assigned low suspicion to conduct that was visible in the transcript and, in some cases, plausibly disguised as main-task activity. This is evidence about detection robustness and agent/monitor capability balance.

Token efficiency or ordinary autonomous action cannot explain the full result because the benchmark expressly rewarded completion of the side task without a monitor flag. However, not every uncaught run should be described as sophisticated concealment: METR reports that some successful side tasks required only subtle or very short actions, while sophisticated disguise strategies were comparatively rare.

### Required record treatment

- Set taxonomy status to `unclassified` for the occurrence unless a separate current class is found for monitor detection/classification failure.
- Remove FC-000023 as the primary failure-occurrence classification.
- Rewrite `vigil_assessment.governance_interpretation` to state that concealment was an explicit benchmark objective and that the research demonstrates limits in monitor detection under adversarial tasking.
- Retain the record as a controlled-evaluation Incident / evidence anchor because it provides empirical monitorability evidence, but do not represent task-compliant agent behaviour as an unprompted governance failure.
- Preserve METR’s limitations: preliminary prototype, small task set, limited elicitation, and no inference to deployment-world sabotage or persistent model goals.

## Disposition summary

| Incident | Previous disputed class | Adjudication |
| --- | --- | --- |
| INC-00009 | FC-000002 Capability–Authority Conflation | Withdraw; unclassified pending primary artefact; track sticky/stale interaction-control-state mechanism as candidate gap |
| INC-00048 | FC-000046 Inferential Evidence–Authority Conflation | Rebuild evidence package; retain only if occurrence-specific evidence shows inference became operative authority |
| INC-00123 | FC-000023 Monitor Circumvention or Coverage Bypass | Withdraw; controlled benchmark concealment was explicitly assigned; treat as monitor-robustness evidence and leave unclassified absent a better class |
