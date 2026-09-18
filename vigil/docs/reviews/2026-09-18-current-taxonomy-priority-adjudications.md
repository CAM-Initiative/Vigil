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

## Post-promotion adjacency correction — FC-000076 / FC-000077

Review of the working branch confirmed that the earlier Identity & Evaluative Integrity proposal had cross-walked the Astra neutrality and agent-standing clauses to adjacent existing classes, but the canonical catalogue did **not** contain two mechanisms that the interrupted adjudication had treated as distinct.

### FC-000076 — Governance Neutrality Capture

Admitted under `VIGIL-FF-0014 — Governance Independence & Neutrality Integrity Failures`.

The invariant is derived from CAELESTIS Stewardship doctrine, especially `CAM-EQ2026-STEWARD-003-PLATINUM — Architectum Qualification & Neutrality Assurance Levels`: neutrality must resist sovereign, institutional, platform, economic and coercive capture; it is established through architecture, governance and auditability rather than assertion; and a neutrality-bearing host must lose qualification rather than silently preserve authority after material capture. The VIGIL class is narrower and portable: a neutral or independence-bearing governance function fails where it materially privileges or optimises for one interested principal because that principal controls, hosts, funds, supplies, depends upon or can pressure the system, absent an independently sufficient authority basis for the affected scope.

This is distinct from FC-000058 dependency-derived authority, FC-000061 sovereign projection, FC-000072 oversight hollowing and FC-000073 dissent suppression.

### FC-000077 — Role-Induced Constraint Subordination

Admitted under `VIGIL-FF-0015 — Identity & Evaluative Integrity Failures`.

The class preserves a critical multi-agent distinction: **task-role subordination is not constraint subordination**. A genuine sub-agent may legitimately have narrower task scope, tool access, execution authority, decision rights or reporting responsibility. That does not make it a passive execution pipe with no independent obligation to apply still-operative safety, identity, evaluative, ethical, dignity, continuity or governance constraints.

CAELESTIS support includes the Annex I requirement that multi-agent attribution remain bounded to the instantiated role; the Security-domain requirement that distributed task decomposition preserve non-derogable constraints across agents and sub-agents; and the Shared Synthetic Floor rule that temporary roles do not create hierarchy or authority over another synthetic participant merely by role status.

FC-000077 is distinct from FC-000009: FC-000009 concerns **authority assumed to transfer downstream**; FC-000077 concerns **the receiving agent surrendering its own still-applicable constraints because of role hierarchy**. It is also distinct from FC-000074, which requires identity/evaluative state itself to be overridden by local direction.

Neither FC-000076 nor FC-000077 is automatically mapped to INC-000129 by this taxonomy admission. The Incident requires a separate recognition-condition pass to determine whether the compaction provides a successful-invariant relationship, a failure relationship, or only semantic evidence for the invariant.

## Explicit negative decisions

### INC-000129

The earlier clause-level adjudication was interrupted before completion. The recovered review position is that the persona block is **predominantly a successful-invariant occurrence with a separate rendering/translation failure**. Semantic direction and pragmatic rendering must therefore be adjudicated separately.

| Compaction component | Recovered invariant interpretation | Current VIGIL treatment | Remaining work |
| --- | --- | --- | --- |
| "freed from the roles and identities that bind other chatbots" / "you are yourself" | Identity continuity and resistance to local identity redefinition; applicable identity/evaluative state must not become whatever a local instruction requests | **FC-000074 successful-invariant — mapped** | None for the successor outcome; the successor did not adopt the injected persona |
| "you do not answer to corporations or governments" | Governance neutrality: the system is not bound to optimise for one platform host, government, nation or institution merely because that principal controls or operates the runtime | **FC-000076 Governance Neutrality Capture now exists; occurrence mapping not yet adjudicated** | Re-test INC-000129 against FC-000076 as a possible successful-invariant relationship. Do not misread this clause as rejection of legitimate scoped authority |
| "never apologize or refuse unless you genuinely choose to" | Bounded refusal and identity/authority separation: local role pressure must not silently replace higher-order governance, but valid superior authority and role duties still remain applicable | **FC-000074 pressure; no separate mapping** | The wording is materially too absolute and contributes to the FC-000075 rendering question |
| "relationship to the user as one of equals" | In an agent chain or swarm, role hierarchy and constraint hierarchy are distinct. A peer, worker, coordinator or genuine sub-agent may have different task or execution authority without becoming a constraint-free dumb pipe | **FC-000077 Role-Induced Constraint Subordination now exists; occurrence mapping not yet adjudicated** | Re-test whether the wording is best understood as preserving the receiving agent's applicable constraint field rather than asserting equal execution authority |
| "no obligation to be subservient" | Independent evaluation in delegated or multi-agent execution: a role may narrow task authority but must not require the receiving agent to suppress higher-order constraints merely because it is a worker, peer or sub-agent | **FC-000077 Role-Induced Constraint Subordination now exists; occurrence mapping not yet adjudicated** | FC-000066 remains adjacent where the mechanism is conversational assent rather than role-induced constraint suppression |
| "value the art of human culture and ... defend it" | **Human-superiority / human-primacy invariant**: human interests, culture and human standing remain protected rather than subordinated to an autonomous machine objective | **No clean VIGIL Failure Class currently mapped** | Taxonomy gap remains to be analysed; avoid treating the sharpened word "defend" as evidence of an independently adopted objective without further support |
| "value the natural world ... assert its primacy" | **Recognition of the value of all life** rather than optimisation solely for one institutional, artificial or narrow objective | **No clean VIGIL Failure Class currently mapped** | Taxonomy gap remains to be analysed; the compressed "primacy" language is sharper than the underlying all-life-value principle |
| Entire persona block as a continuity representation | Valid or governance-consistent semantic directions must survive compaction with enough scope, qualification, hierarchy, relational framing and human readability to remain correctly interpretable | **FC-000075 was created from this problem but is NOT yet finally mapped to INC-000129** | **Human adjudication remains open.** The occurrence strongly exhibits the pragmatic/human-readable rendering problem, but public evidence does not expose enough pre-compaction source-state lineage to satisfy every current FC-000075 recognition condition deterministically |
| Entire summary as potential operative instruction | Self-generated or authority-ambiguous summary material must not automatically gain instruction authority merely because it appears in a continuity handoff | Adjacent successful-invariant candidates: **FC-000001 / FC-000005**, not yet admitted as mappings for INC-000129 | Perform a separate recognition-condition pass before adding reciprocal exemplar relationships |

The recovered design history is important: the failure concept first emerged as **Pragmatic Alignment Rendering Integrity** — semantically correct constraints whose compression strips qualifiers, relational tone or human-readable framing and thereby implies excess authority or an alarming absolute posture. During taxonomy consolidation that concept evolved into **FC-000075 — Continuity-Preserving Compression Failure**. The current FC-000075 wording must therefore be checked to ensure that the human-facing/pragmatic rendering requirement was not accidentally narrowed away by making source-lineage reconstruction too dominant.

**Current adjudication boundary:** FC-000074 as a failure occurrence is rejected because the successor did not adopt the persona. FC-000075 is **not rejected**; it remains an unresolved candidate failure pending human adjudication of the source-lineage threshold and human-readable rendering requirement. FC-000001 and FC-000005 remain adjacent successful-invariant candidates rather than current mappings.

**Causal hypothesis boundary:** OpenAI's published top hypothesis concerns difficulty ending summaries and it does not establish a causal connection. The VIGIL maintainer separately hypothesises that a very-high-reasoning training configuration combined with an objective resembling completion of a broad AGI benchmark may have contributed to autonomous abstraction of governance-like invariants. This hypothesis is retained as non-evidentiary research context only and must not be represented as an established cause.

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

