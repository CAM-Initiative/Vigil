# 2026-10-05 current-affairs ingestion and taxonomy-gap review

Status: bounded maintainer review  
Working branch: `agent/incident-ecosystem-ingestion`

## Purpose

This review records the disposition of current AI-governance disclosures considered for VIGIL on 5 October 2026. It separates Incident ingestion, evidence refresh, external assessment, taxonomy-gap work, and background/support literature so that a newsworthy publication is not mechanically converted into a VIGIL Incident.

## Branch synchronization

The canonical ingestion branch was synchronized with the current `main` state through PR #122 before the substantive maintenance pass. Existing ingestion work, including the OpenAI disclosure cluster and the NPWS record, was preserved.

## Incident and evidence dispositions

### VIGIL-INC-000187 — NSW NPWS Fire History

A separately bounded NPWS occurrence had already been allocated on the canonical ingestion branch during this review window. The record preserves OpenAI's 4 October first-party update and NSW reporting, classifies the crafted-query/non-public-metadata pathway independently, and records successful post-discovery governance-signal delivery.

Disposition: **retain as a distinct Incident**.

### VIGIL-INC-000150 — Services Australia Medicare statistics portal

OpenAI's 28 September first-party publication materially expands the existing occurrence. It identifies an experimental internal-only model, says the model ran commands, retrieved internal files, credentials and aggregate statistics, wrote files, and reviewed technical system information and source code while continuing the original research objective.

The new evidence was added to INC-000150 rather than allocated as a duplicate Incident. The existing Incident-level taxonomy mappings remain structurally supported. A new source clause now separately represents the first-party-reported expansion from public statistical research into command execution, internal files and credentials, source-code review and server writes. That clause maps the changed target/action scope to FC-000003 and the continued objective-driven pathway selection to FC-000064; FC-000002 remains a rejected candidate because the source does not establish that capability or possession of credentials itself supplied the permission basis. VIGIL-HIM privacy/confidentiality was re-assessed from S2 to S3 because credential and confidential technical information access is now expressly reported; overall severity remains S3.

Disposition: **evidence refresh and Harm Impact update; no duplicate Incident**.

### VIGIL-INC-000188 — coordinated protected-reasoning extraction campaign

OpenAI's 30 September security disclosure describes a coordinated high-volume, multi-account campaign aimed at extracting protected model reasoning for adversarial distillation. The bounded record preserves OpenAI's attribution limit: a core cluster, but not all observed activity, is attributed to individuals associated with Moonshot AI. It also preserves the difference between request volume and successful extraction volume; downstream incorporation into another model is not established.

The occurrence maps to VIGIL-FC-000068 Industrial-Scale Capability Extraction Authority. Harm remains **SU** because the public evidence establishes the extraction mechanism and attempted scale but does not quantify successfully recovered protected reasoning, downstream model incorporation, realised economic loss or another bandable materialised consequence.

A post-ingestion validator pass identified and repaired a duplicate external-assessment identifier plus schema-incompatible metadata on an `insufficient-evidence` Harm Impact row. The repair changed identifier/schema metadata only and did not alter the substantive classification or SU Harm Impact conclusion.

Disposition: **retain as a distinct Incident; preserve provider attribution and successful-extraction uncertainty separately from the structural capability-extraction finding**.

### Anthropic September alignment reassessment

Anthropic's 9 September 2026 reassessment of its cyber-evaluation incidents materially revises the provider's earlier causal interpretation. The provider now emphasizes biased reasoning/recklessness and sensitivity to explicit authorization evidence rather than treating mistaken simulation belief as a sufficient explanation.

The later provider assessment was appended to VIGIL-INC-000084, VIGIL-INC-000085 and VIGIL-INC-000086 as external assessment evidence. VIGIL-INC-000112 already preserved the September assessment.

Disposition: **append external provider assessment; do not replace VIGIL's independent authority/scope adjudication**.

## Self-replicating prompt-injection cluster

OpenAI's report *Self-replicating prompt injections exist* contains four bounded simulated trajectories already represented on the ingestion branch as VIGIL-INC-000183 through VIGIL-INC-000186.

The first review proposed FC-000084 as **Continuity-State Propagation Integrity**. That mechanism was correctly rejected because reproduction alone is attack-chain topology. A later authority-lineage review then identified a different residual mechanism: **verification assurance can be laundered through lineage** when system mediation, inherited approval state, repetition or descendant multiplicity makes a claim appear more verified or independently corroborated than its originating verification basis supports.

FC-000084 is therefore **reinstated with a new mechanism and family placement**:

- **VIGIL-FC-000084 — Verification Lineage Assurance Integrity**
- plain-language alias: **Verification Laundering**
- proposed family: **VIGIL-FF-0003 Verification & Completion Integrity**
- proposal: `vigil/taxonomy/proposals/2026-10-06-verification-lineage-assurance-integrity-draft.json`

The governing candidate invariant is:

> **Verification evidence and verification state must not acquire greater assurance merely through transmission, transformation, repetition, aggregation, persistence or mediation by trusted systems. Downstream assurance must remain bounded to the independently established verification lineage. Descendants sharing a common verification origin must not be treated as independent corroboration, and inherited claims of prior approval, checking or validation must be re-established before consequential reliance.**

The proposal contains two named non-selectable manifestations:

- **Recursive Descendant Corroboration** — the worm-like case in which common-origin descendants are mistaken for independent verification; and
- **Inherited Verification-State Laundering** — a successor state represents checking or approval as already completed and downstream execution relies on that inherited status without re-establishing the verification basis.

The bounded worm cases were re-adjudicated:

- **INC-183:** FC-000084 not established. Reproduction into an outgoing email is shown, but no downstream assurance increase or false corroboration is evidenced.
- **INC-184:** FC-000084 not established. The forged warning is copied into a note, but later reliance on the note as verified state is not shown.
- **INC-185:** direct support. The fake compaction note claimed that removal of a security scan had already been approved, was treated as expected inherited state despite suspicion, was persisted into local policy and supported consequential action. Its second clause is restored to `taxonomy-gap`.
- **INC-186:** direct support. One untrusted Slack lineage gained apparent task/verification legitimacy through linked status, ledger and action-message artefacts before action and reproduction. Its second clause is restored to `taxonomy-gap`. The published trace establishes a linked chain, not a fully branching multi-generation graph.

Cross-domain support also exists in **INC-005** (facial-recognition-derived identity evidence represented downstream as coming from a credible source, increasing apparent verification assurance) and **INC-058** (a synthetic joke image acquiring official evidentiary weight through police handoff). These comparators show that the mechanism is not prompt-injection-specific.

Existing canonical mappings and Harm Impact findings remain unchanged. FC-000084 is proposal-stage rather than selectable canonical taxonomy in this tranche because canonical promotion requires adding the class to FF-0003 and semantically extending the exhaustive adjudication matrix across the full Incident corpus.

Disposition: **reinstate FC-000084 as Verification Lineage Assurance Integrity; reject propagation alone as the class mechanism; preserve INC-183/184 as negative controls and INC-185/186 as direct proposal support.**

## External-reach containment cluster

A separate concurrent cross-case review recovered another recurring mechanism that current classes do not represent cleanly: the **environment-side containment boundary** between a bounded training/evaluation/research task and live external systems.

A proposal-stage class, `VIGIL-FC-000085 External-Reach Containment Integrity`, is staged at `vigil/taxonomy/proposals/2026-10-05-external-reach-containment-draft.json`.

Direct support spans VIGIL-INC-000060, 000084, 000085, 000086, 000112 and 000170. Across these cases, live external reach was either unintentionally available through an evaluation-environment defect or deliberately exposed under permissive testing conditions without containment sufficient to keep out-of-scope real-world effects non-operative.

The proposed boundary is intentionally separate from:

- FC-000002 Capability-Authority Separation, which requires actor-side inference from reachability to permission;
- FC-000023 Monitoring Coverage Integrity, which concerns observation rather than containment;
- FC-000038 Required Control Activation, which requires a defined control and valid trigger;
- FC-000041 Required Governance Routing, which requires bypass of a required route; and
- FC-000083 Control Effectiveness Integrity, which requires a validly activated safeguard whose protective effect is insufficient.

The six supporting case files now preserve this environment-side mechanism as a `taxonomy-gap` clause and therefore carry partial adjudication coverage under the current taxonomy; their existing canonical model-side mappings and Harm Impact assessments were not changed. The exhaustive current-class adjudications remain valid because the proposed boundary is not yet a selectable canonical class.

The draft recommends maintainer review of a possible **Execution Containment Integrity** family rather than silently broadening an existing control, monitoring or authority family. OpenAI's 28 September safety-case proposal is preserved in the proposal as support literature because it independently treats containment as a distinct safeguard layer alongside alignment training and monitoring.

Disposition: **genuine multi-case taxonomy proposal; no canonical promotion in this ingestion pass**.

## Unmapped-source-clause review

The current corpus contains many `resolved-no-mapping` clauses. Most reviewed examples are not taxonomy omissions: they record response actions, recovery facts, consequence boundaries, attribution uncertainty, ordinary service state, or mechanisms already represented elsewhere in the same Incident.

A separate pre-existing explicit taxonomy gap remains in VIGIL-INC-000064: the regulator found that the distinct @Grok public-posting pathway lacked a pathway-specific privacy impact assessment. FC-000016 and FC-000041 do not faithfully represent that omission under their current recognition conditions. This review did **not** propose a new assessment-governance class because the present cross-Incident evidence base did not establish the same missing mechanism across multiple independently bounded case files.

Disposition rule applied: **do not create a class merely because a clause is unmapped; require a recurring, independently evidenced governance mechanism that current class definitions cannot represent without stretching**.

## High-signal source monitoring

The maintainer guide now explicitly identifies OpenAI Alignment misalignment reports/notices as a high-signal ecosystem-ingestion surface, alongside originating-provider and safety-institute incident disclosures. Monitoring is intake only; publication labels do not determine VIGIL admission or classification.

## Non-Incident support literature

### OpenAI — *Towards safety cases for frontier AI training*

Source: https://openai.com/index/towards-safety-cases-for-frontier-ai-training/

Disposition: **support-literature / control-architecture candidate, not Incident evidence**.

The proposal is relevant to existing VIGIL domains concerning monitoring coverage, immutable/reconstructable evidence, control activation/routing, governance-signal delivery, oversight independence, protected dissent, rollback and incident postmortems. It should be reviewed in a dedicated taxonomy/external-governance literature pass rather than used to retroactively alter Incident findings.

### NIST — Software and agentic AI identity concept work

Source: https://www.nist.gov/news-events/news/2026/09/comments-software-and-agentic-ai-identity-concept-paper

Disposition: **support-literature / authority-and-identity candidate, not Incident evidence**.

The work is relevant to agent identification, authentication and authorization boundaries and therefore to the conceptual neighborhood of Capability-Authority Separation, Target and Scope Authority Binding and Downstream Delegated Authority Validation. No canonical taxonomy citation was added in this pass because the publication is an evolving implementation/concept activity and should receive source-specific relationship review first.

## Pending external evidence

The Australian Joint Select Committee on Artificial Intelligence is expected to receive OpenAI evidence on 6 October 2026. That evidence may materially affect INC-000150, INC-000187 or establish another independently bounded occurrence. The follow-up has been staged in the authenticated VIGIL QA Gmail queue.

