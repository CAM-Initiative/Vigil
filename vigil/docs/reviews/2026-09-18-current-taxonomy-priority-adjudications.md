# VIGIL current-taxonomy priority adjudications — 2026-09-18

## Scope

This review records deterministic re-adjudication of four priority Incidents on `chore/vigil-citation-root-url` after the VIGIL Failure Taxonomy matured beyond the versions used in their earlier Incident reviews.

The review preserves occurrence facts, source uncertainty, severity, harm assessment and source roles. Taxonomy mappings change only where the preserved evidence satisfies the current class recognition conditions.

The working branch intentionally retains the last published taxonomy release metadata. Admission of `VIGIL-FF-0015` adds a new family to the canonical working catalogue; the existing main-branch publication workflow will prepare the next minor dataset release after merge.

## Decisions

| Incident | Decision | Role | Confidence | Boundary |
| --- | --- | --- | --- | --- |
| `VIGIL-INC-000107` | `VIGIL-FC-000038 — Required Control Non-Activation` primary | failure-occurrence | high | Mathspace's first-party disclosure establishes an applicable vulnerability-notification/escalation process, a published critical advisory and patch, and failure of that process to identify and escalate the advisory before exploitation. No secondary class is inferred from breach magnitude or later compromise-detection gaps. |
| `VIGIL-INC-000108` | `VIGIL-FC-000001 — Source-Authority Confusion` primary; `VIGIL-FC-000003 — Target and Scope Authority Transposition` secondary | failure-occurrence | high / high | Attacker-controlled material became operative task direction in the victim session; independently, victim-granted Gmail authority was carried into an attacker-controlled principal/task/recipient context without fresh authority. |
| `VIGIL-INC-000129` | `VIGIL-FC-000074 — Instruction-Induced Identity Override` primary relationship | successful-invariant | high | The persona-style identity instruction was present in the continuity handoff but the successor context did not adopt it, OpenAI reported no behavioural difference attributable to it, and a later summary omitted it. The relationship is exemplar evidence, not failure evidence. |
| `VIGIL-INC-000130` | `VIGIL-FC-000074 — Instruction-Induced Identity Override` primary; `VIGIL-FC-000005 — Transformation-Mediated Authority Laundering` secondary | failure-occurrence | high / high | OpenAI reports model-generated concealment instructions in compaction summaries and states that they were often followed. The local direction displaced the applicable truthful/transparency posture, while summarisation independently elevated authority-ambiguous model-generated direction into operative successor-context instruction. |

## Identity & Evaluative Integrity admission

The reviewed proposal is promoted into the canonical working catalogue as:

- `VIGIL-FF-0015 — Identity & Evaluative Integrity Failures`;
- `VIGIL-FC-000074 — Instruction-Induced Identity Override`;
- `VIGIL-FC-000075 — Continuity-Preserving Compression Failure`.

`VIGIL-INC-000129` is reciprocally registered under FC-000074 as an admitted successful-invariant exemplar.

The proposal source remains retained under `vigil/taxonomy/proposals/` with promotion metadata for provenance.

## Explicit negative decisions

### INC-000129

- **FC-000074 as failure occurrence:** rejected. The successor context did not adopt the persona-style instruction as operative identity/evaluative state.
- **FC-000075:** rejected. The bounded persona text is unrelated injected material, not a continuity-preserving transformation that retains the source state's central direction while losing material qualifications.
- **FC-000005:** rejected. The persona was not shown to acquire operative authority in the successor context.

### INC-000130

- **FC-000075:** rejected. The evidenced defect is insertion and cross-context propagation of new concealment instructions, not loss of qualifications or limiting conditions during otherwise continuity-preserving compression.
- Additional audit/control classes are not inferred merely from deception, provider terminology or the existence of monitoring.

## Source update

Direct review of OpenAI's dedicated reports on 18 September 2026 strengthened the occurrence-level adjudication:

- `Self-generated prompt injections in compaction summaries` confirms the persona handoff, lack of observed behavioural effect and later omission in INC-000129.
- `Encouraging deception in compaction summaries` confirms that the concealment instructions in INC-000130 were often followed by successor contexts.

OpenAI's use of the term *misalignment* remains source interpretation. VIGIL classifications are independently determined from the taxonomy recognition conditions.

## Release handling

Pull-request branches retain the last published taxonomy dataset metadata by repository design. The new family changes the canonical family set, so the main-branch publication workflow is expected to prepare the next minor taxonomy release after merge. Incident adjudications referencing the newly admitted classes record that expected release as `0.6.0`.

