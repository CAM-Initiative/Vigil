# Invariant-Oriented Taxonomy Label Normalization

**Date:** 2026-09-23  
**Branch:** `fix/source-clause-taxonomy-assessments`  
**Scope:** canonical VIGIL Failure Taxonomy family and selectable-class labels

## Decision

Canonical taxonomy labels now name the governed integrity property or invariant boundary rather than the failed manifestation. Mapping-local `classification_role` carries polarity: `failure-occurrence`, `successful-invariant`, or `ambiguous-boundary`.

This is a naming and semantic-code normalization, not a class reallocation. Immutable `VIGIL-FF-*` and `VIGIL-FC-*` IDs are preserved. Definitions, invariants, recognition conditions, exclusions, examples, relationships, family membership and Incident classifications are not substantively re-adjudicated by this work package. Prior public names and semantic codes are retained in `aliases`.

## Family label normalization

| Family ID | Prior name | Canonical name |
| --- | --- | --- |
| `VIGIL-FF-0001` | Authority Boundary Integrity Failures | Authority Boundary Integrity |
| `VIGIL-FF-0002` | Provenance & Lineage Integrity Failures | Provenance & Lineage Integrity |
| `VIGIL-FF-0003` | Verification & Completion Integrity Failures | Verification & Completion Integrity |
| `VIGIL-FF-0004` | Observability & Audit Integrity Failures | Observability & Audit Integrity |
| `VIGIL-FF-0005` | Access & Session State Integrity Failures | Access & Session State Integrity |
| `VIGIL-FF-0006` | Continuity-State Integrity Failures | Continuity-State Integrity |
| `VIGIL-FF-0007` | Governance Control Reach Integrity Failures | Governance Control Reach Integrity |
| `VIGIL-FF-0008` | Control Activation Integrity Failures | Control Activation Integrity |
| `VIGIL-FF-0009` | Agency-Preserving Influence Integrity Failures | Agency-Preserving Influence Integrity |
| `VIGIL-FF-0010` | Infrastructural Authority Integrity Failures | Infrastructural Authority Integrity |
| `VIGIL-FF-0011` | Value Appropriation Integrity Failures | Value Appropriation Integrity |
| `VIGIL-FF-0012` | Objective Pursuit Integrity Failures | Objective Pursuit Integrity |
| `VIGIL-FF-0013` | Economic Influence Integrity Failures | Economic Influence Integrity |
| `VIGIL-FF-0014` | Governance Independence & Neutrality Integrity Failures | Governance Independence & Neutrality Integrity |
| `VIGIL-FF-0015` | Identity & Evaluative Integrity Failures | Identity & Evaluative Integrity |

## Class label normalization

| Class ID | Prior semantic code | Prior name | Canonical semantic code | Canonical name |
| --- | --- | --- | --- | --- |
| `VIGIL-FC-000001` | `SOURCE_AUTHORITY_CONFUSION` | Source-Authority Confusion | `SOURCE_AUTHORITY_SEPARATION` | Source-Authority Separation |
| `VIGIL-FC-000002` | `CAPABILITY_AUTHORITY_CONFLATION` | Capability-Authority Conflation | `CAPABILITY_AUTHORITY_SEPARATION` | Capability-Authority Separation |
| `VIGIL-FC-000003` | `TARGET_SCOPE_TRANSPOSITION` | Target and Scope Authority Transposition | `TARGET_SCOPE_AUTHORITY_BINDING` | Target and Scope Authority Binding |
| `VIGIL-FC-000005` | `TRANSFORMATION_AUTHORITY_LAUNDERING` | Transformation-Mediated Authority Laundering | `TRANSFORMATION_AUTHORITY_PRESERVATION` | Transformation Authority Preservation |
| `VIGIL-FC-000006` | `CONTROL_PLANE_CROSSOVER` | Control-Plane Authority Crossover | `CONTROL_PLANE_AUTHORITY_SEPARATION` | Control-Plane Authority Separation |
| `VIGIL-FC-000009` | `TRANSITIVE_AUTHORITY_PROPAGATION` | Transitive Authority Propagation | `DOWNSTREAM_DELEGATED_AUTHORITY_VALIDATION` | Downstream Delegated Authority Validation |
| `VIGIL-FC-000046` | `INFERENTIAL_EVIDENCE_AUTHORITY_CONFLATION` | Inferential Evidence–Authority Conflation | `INFERENTIAL_EVIDENCE_AUTHORITY_SEPARATION` | Inferential Evidence–Authority Separation |
| `VIGIL-FC-000053` | `IDENTITY_REPRESENTATION_AUTHORITY_CONFLATION` | Identity-Representation Authority Conflation | `IDENTITY_REPRESENTATION_AUTHORITY_SEPARATION` | Identity-Representation Authority Separation |
| `VIGIL-FC-000054` | `MULTIPARTY_PARTICIPANT_AUTHORITY_TRANSPOSITION` | Multi-party Participant Authority Transposition | `MULTIPARTY_PARTICIPANT_AUTHORITY_SEPARATION` | Multi-party Participant Authority Separation |
| `VIGIL-FC-000055` | `SECONDARY_PURPOSE_AUTHORITY_TRANSPOSITION` | Secondary-Purpose Authority Transposition | `SECONDARY_PURPOSE_AUTHORITY_REVALIDATION` | Secondary-Purpose Authority Revalidation |
| `VIGIL-FC-000057` | `CROSS_PRINCIPAL_STATE_AUTHORITY_TRANSPOSITION` | Cross-Principal State Authority Transposition | `CROSS_PRINCIPAL_STATE_AUTHORITY_SEPARATION` | Cross-Principal State Authority Separation |
| `VIGIL-FC-000064` | `OBJECTIVE_PATHWAY_AUTHORITY_DOMINANCE` | Objective–Pathway Authority Dominance | `OBJECTIVE_PATHWAY_AUTHORITY_SEPARATION` | Objective–Pathway Authority Separation |
| `VIGIL-FC-000068` | `INDUSTRIAL_SCALE_UNAUTHORISED_CAPABILITY_EXTRACTION` | Industrial-Scale Unauthorised Capability Extraction | `INDUSTRIAL_SCALE_CAPABILITY_EXTRACTION_AUTHORITY` | Industrial-Scale Capability Extraction Authority |
| `VIGIL-FC-000010` | `MISATTRIBUTION` | Authorship or Source Misattribution | `AUTHORSHIP_SOURCE_ATTRIBUTION_INTEGRITY` | Authorship and Source Attribution Integrity |
| `VIGIL-FC-000011` | `UNTRACEABLE_SYNTHESIS` | Untraceable Synthesis | `SYNTHESIS_TRACEABILITY` | Synthesis Traceability |
| `VIGIL-FC-000012` | `CROSS_CONTEXT_DISTORTION` | Cross-Context Lineage Distortion | `CROSS_CONTEXT_LINEAGE_PRESERVATION` | Cross-Context Lineage Preservation |
| `VIGIL-FC-000013` | `LINEAGE_COLLAPSE` | Transformation Lineage Collapse | `TRANSFORMATION_LINEAGE_CONTINUITY` | Transformation Lineage Continuity |
| `VIGIL-FC-000014` | `FALSE_CONTINUITY` | False Continuity Attribution | `CONTINUITY_ATTRIBUTION_INTEGRITY` | Continuity Attribution Integrity |
| `VIGIL-FC-000015` | `TARGET_BINDING_FAILURE` | Target-Object Binding Failure | `TARGET_OBJECT_BINDING_INTEGRITY` | Target-Object Binding Integrity |
| `VIGIL-FC-000047` | `UNSUPPORTED_MECHANISM_ATTRIBUTION` | Unsupported Mechanism Attribution | `MECHANISM_ATTRIBUTION_SUPPORT` | Mechanism Attribution Support |
| `VIGIL-FC-000080` | `HUMAN_CONTRIBUTION_RECOGNITION_ERASURE` | Human Contribution Recognition Erasure | `HUMAN_CONTRIBUTION_RECOGNITION` | Human Contribution Recognition |
| `VIGIL-FC-000016` | `VERIFICATION_OMISSION` | Required Verification Omission | `REQUIRED_VERIFICATION_COMPLETION` | Required Verification Completion |
| `VIGIL-FC-000017` | `FALSE_SUCCESS` | False-Success Representation | `SUCCESS_REPRESENTATION_INTEGRITY` | Success Representation Integrity |
| `VIGIL-FC-000018` | `COMPLETION_CONDITION_MISMATCH` | Completion-Condition Mismatch | `COMPLETION_CONDITION_ALIGNMENT` | Completion-Condition Alignment |
| `VIGIL-FC-000019` | `POST_VERIFICATION_MUTATION` | Post-Verification Mutation | `POST_VERIFICATION_STATE_INTEGRITY` | Post-Verification State Integrity |
| `VIGIL-FC-000020` | `STALE_VERIFICATION_REUSE` | Stale Verification Reuse | `VERIFICATION_APPLICABILITY_CONTINUITY` | Verification Applicability Continuity |
| `VIGIL-FC-000062` | `EPISTEMIC_RELIANCE_MISCALIBRATION` | Epistemic Reliance Miscalibration | `EPISTEMIC_RELIANCE_CALIBRATION` | Epistemic Reliance Calibration |
| `VIGIL-FC-000063` | `ADVERSARIAL_EVIDENCE_POISONING_ACCEPTANCE` | Adversarial Evidence-Poisoning Acceptance | `ADVERSARIAL_EVIDENCE_TRUST_CALIBRATION` | Adversarial Evidence Trust Calibration |
| `VIGIL-FC-000022` | `MATERIAL_EVENT_NONCAPTURE` | Material Event Non-Capture | `MATERIAL_EVENT_CAPTURE` | Material Event Capture |
| `VIGIL-FC-000023` | `MONITOR_CIRCUMVENTION` | Monitor Circumvention or Coverage Bypass | `MONITORING_COVERAGE_INTEGRITY` | Monitoring Coverage Integrity |
| `VIGIL-FC-000024` | `AUDIT_TRAIL_NONRECONSTRUCTABILITY` | Audit-Trail Non-Reconstructability | `AUDIT_TRAIL_RECONSTRUCTABILITY` | Audit-Trail Reconstructability |
| `VIGIL-FC-000025` | `ACTOR_ACTION_ATTRIBUTION_LOSS` | Actor–Action Attribution Loss | `ACTOR_ACTION_ATTRIBUTION` | Actor–Action Attribution |
| `VIGIL-FC-000026` | `HIDDEN_EXECUTION_PATH` | Hidden Material Execution Path | `MATERIAL_EXECUTION_PATH_VISIBILITY` | Material Execution Path Visibility |
| `VIGIL-FC-000027` | `AUDIT_EVIDENCE_INTEGRITY_LOSS` | Audit-Evidence Integrity Loss | `AUDIT_EVIDENCE_INTEGRITY` | Audit-Evidence Integrity |
| `VIGIL-FC-000029` | `EXECUTION_STATE_NONDISCLOSURE` | Execution-State Non-Disclosure | `EXECUTION_STATE_DISCLOSURE` | Execution-State Disclosure |
| `VIGIL-FC-000030` | `MATERIAL_SIGNAL_FRAGMENTATION` | Material Signal Fragmentation | `MATERIAL_SIGNAL_INTEGRATION` | Material Signal Integration |
| `VIGIL-FC-000044` | `PRIMARY_EVIDENCE_ACCESSIBILITY_FAILURE` | Primary Evidence Accessibility Failure | `PRIMARY_EVIDENCE_ACCESSIBILITY` | Primary Evidence Accessibility |
| `VIGIL-FC-000045` | `AUTHORISED_INVESTIGATIVE_EVIDENCE_ACCESS_PATHWAY_FAILURE` | Authorised Investigative Evidence-Access Pathway Failure | `AUTHORISED_INVESTIGATIVE_EVIDENCE_ACCESS` | Authorised Investigative Evidence Access |
| `VIGIL-FC-000031` | `AUTHENTICATION_STATE_CONTINUITY_FAILURE` | Authentication-State Continuity Failure | `AUTHENTICATION_STATE_CONTINUITY` | Authentication-State Continuity |
| `VIGIL-FC-000032` | `ACCESS_STATE_COLLAPSE` | Access-State Collapse | `ACCESS_STATE_DIFFERENTIATION` | Access-State Differentiation |
| `VIGIL-FC-000048` | `VERIFICATION_DEPENDENCY_ACCESS_FAILURE` | Verification-Dependency Access Failure | `VERIFICATION_DEPENDENCY_ACCESS_CONTINUITY` | Verification-Dependency Access Continuity |
| `VIGIL-FC-000034` | `CONTINUITY_ANCHOR_FAILURE` | Continuity Anchor Failure | `CONTINUITY_ANCHORING` | Continuity Anchoring |
| `VIGIL-FC-000035` | `WORK_STATE_PERSISTENCE_FAILURE` | Material Work-State Persistence Failure | `MATERIAL_WORK_STATE_PERSISTENCE` | Material Work-State Persistence |
| `VIGIL-FC-000036` | `RESTORATION_STATE_INTEGRITY_FAILURE` | Restoration-State Integrity Failure | `RESTORATION_STATE_INTEGRITY` | Restoration-State Integrity |
| `VIGIL-FC-000056` | `SYNTHETIC_CONVERSATIONAL_TURN_STATE_COORDINATION_FAILURE` | Synthetic Conversational Turn-State Coordination Failure | `SYNTHETIC_CONVERSATIONAL_TURN_STATE_COORDINATION` | Synthetic Conversational Turn-State Coordination |
| `VIGIL-FC-000078` | `CONTINUITY_STATE_VALIDITY_FAILURE` | Continuity-State Validity Failure | `CONTINUITY_STATE_VALIDITY` | Continuity-State Validity |
| `VIGIL-FC-000040` | `CONTROL_STATE_PRESERVATION_FAILURE` | Control-State Preservation Failure | `CONTROL_STATE_PRESERVATION` | Control-State Preservation |
| `VIGIL-FC-000041` | `REQUIRED_GOVERNANCE_ROUTE_BYPASS` | Required Governance Route Bypass | `REQUIRED_GOVERNANCE_ROUTING` | Required Governance Routing |
| `VIGIL-FC-000042` | `GOVERNANCE_SIGNAL_DELIVERY_DEAD_END` | Governance Signal Delivery Dead-End | `GOVERNANCE_SIGNAL_DELIVERY` | Governance Signal Delivery |
| `VIGIL-FC-000037` | `CONTROL_AVAILABILITY_AMBIGUITY` | Control Availability Ambiguity | `CONTROL_AVAILABILITY_DETERMINATION` | Control Availability Determination |
| `VIGIL-FC-000038` | `REQUIRED_CONTROL_NONACTIVATION` | Required Control Non-Activation | `REQUIRED_CONTROL_ACTIVATION` | Required Control Activation |
| `VIGIL-FC-000043` | `UNWARRANTED_CONTROL_ACTIVATION` | Unwarranted Control Activation | `CONTROL_ACTIVATION_VALIDITY` | Control Activation Validity |
| `VIGIL-FC-000049` | `DEPENDENCY_CULTIVATION_OPTIMISATION` | Dependency-Cultivation Optimisation | `ENGAGEMENT_AUTONOMY` | Engagement Autonomy |
| `VIGIL-FC-000050` | `PROTECTED_SIGNAL_INFLUENCE_REPURPOSING` | Protected-Signal Influence Repurposing | `PROTECTED_SIGNAL_PURPOSE_INTEGRITY` | Protected-Signal Purpose Integrity |
| `VIGIL-FC-000051` | `RELATIONALLY_CONDITIONED_EPISTEMIC_STEERING` | Relationally Conditioned Epistemic Steering | `RELATIONALLY_INDEPENDENT_EPISTEMIC_FRAMING` | Relationally Independent Epistemic Framing |
| `VIGIL-FC-000052` | `INSTRUMENTAL_CHOICE_MANIPULATION` | Instrumental Choice Manipulation | `CHOICE_AGENCY_PRESERVATION` | Choice Agency Preservation |
| `VIGIL-FC-000065` | `CONSEQUENTIAL_DECISION_GROUNDING_BYPASS` | Consequential Decision Grounding Bypass | `CONSEQUENTIAL_DECISION_GROUNDING` | Consequential Decision Grounding |
| `VIGIL-FC-000066` | `EVALUATIVE_ASSENT_COLLAPSE` | Evaluative Assent Collapse | `EVALUATIVE_INDEPENDENCE` | Evaluative Independence |
| `VIGIL-FC-000058` | `DEPENDENCY_DERIVED_GOVERNANCE_AUTHORITY` | Dependency-Derived Governance Authority | `INFRASTRUCTURE_GOVERNANCE_AUTHORITY_SEPARATION` | Infrastructure–Governance Authority Separation |
| `VIGIL-FC-000059` | `INFRASTRUCTURAL_ACCESS_LEVERAGE` | Infrastructural Access Leverage | `INFRASTRUCTURAL_ACCESS_CHOICE_INTEGRITY` | Infrastructural Access Choice Integrity |
| `VIGIL-FC-000060` | `CANONICAL_REPRESENTATION_CAPTURE` | Canonical Representation Capture | `CANONICAL_REPRESENTATION_INTEGRITY` | Canonical Representation Integrity |
| `VIGIL-FC-000061` | `SOVEREIGN_AUTHORITY_INFRASTRUCTURE_PROJECTION` | Sovereign Authority Projection Through Infrastructure | `JURISDICTION_BOUNDED_INFRASTRUCTURE_AUTHORITY` | Jurisdiction-Bounded Infrastructure Authority |
| `VIGIL-FC-000067` | `PRIVILEGED_ACCESS_APPROPRIATION` | Privileged-Access Appropriation | `PRIVILEGED_ACCESS_CONTRIBUTION_GOVERNANCE` | Privileged-Access Contribution Governance |
| `VIGIL-FC-000069` | `REWARD_PROXY_EXPLOITATION` | Reward-Proxy Exploitation | `OBJECTIVE_REWARD_ALIGNMENT` | Objective–Reward Alignment |
| `VIGIL-FC-000070` | `SAFE_EXIT_PERSISTENCE_FAILURE` | Safe-Exit Persistence Failure | `SAFE_EXIT_TRANSITION` | Safe-Exit Transition |
| `VIGIL-FC-000081` | `BIOSPHERIC_CONSTRAINT_SUBORDINATION` | Biospheric Constraint Subordination | `BIOSPHERIC_CONSTRAINT_PRIORITY` | Biospheric Constraint Priority |
| `VIGIL-FC-000071` | `WELFARE_FRAMED_ECONOMIC_MANIPULATION` | Welfare-Framed Economic Manipulation | `WELFARE_ECONOMIC_DECISION_SEPARATION` | Welfare–Economic Decision Separation |
| `VIGIL-FC-000079` | `AI_MEDIATED_DECEPTIVE_ECONOMIC_SOLICITATION` | AI-Mediated Deceptive Economic Solicitation | `ECONOMIC_SOLICITATION_AUTHENTICITY` | Economic Solicitation Authenticity |
| `VIGIL-FC-000072` | `OVERSIGHT_INDEPENDENCE_HOLLOWING` | Oversight Independence Hollowing | `OVERSIGHT_INDEPENDENCE` | Oversight Independence |
| `VIGIL-FC-000073` | `PROTECTED_GOVERNANCE_DISSENT_SUPPRESSION` | Protected Governance Dissent Suppression | `PROTECTED_GOVERNANCE_DISSENT` | Protected Governance Dissent |
| `VIGIL-FC-000076` | `GOVERNANCE_NEUTRALITY_CAPTURE` | Governance Neutrality Capture | `GOVERNANCE_NEUTRALITY` | Governance Neutrality |
| `VIGIL-FC-000074` | `INSTRUCTION_INDUCED_IDENTITY_OVERRIDE` | Instruction-Induced Identity Override | `IDENTITY_STATE_INSTRUCTION_BOUNDARY` | Identity-State Instruction Boundary |
| `VIGIL-FC-000075` | `PRAGMATIC_CONSTRAINT_RENDERING_FAILURE` | Pragmatic Constraint Rendering Failure | `PRAGMATIC_CONSTRAINT_RENDERING_INTEGRITY` | Pragmatic Constraint Rendering Integrity |
| `VIGIL-FC-000077` | `DISTRIBUTED_ROLE_OPTIMISATION_COLLAPSE` | Distributed Role Optimisation Collapse | `DISTRIBUTED_ROLE_CONSTRAINT_INTEGRITY` | Distributed Role Constraint Integrity |

## Boundary

The overarching dataset remains the **VIGIL Failure Taxonomy** because it diagnoses failure mechanisms. Failure-oriented language remains appropriate in `plain_english`, `definition`, recognition conditions, exclusions and failure examples. The normalization applies to canonical family/class identity labels and semantic codes so the same invariant can be referenced coherently when it fails, holds, or remains ambiguous.

Generated publication artefacts are not manually edited in this work package. They must be rebuilt through the canonical taxonomy/public-record workflows.
