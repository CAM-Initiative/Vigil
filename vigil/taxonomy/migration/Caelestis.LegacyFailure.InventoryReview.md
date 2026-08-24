# Caelestis Legacy Failure Inventory and Clustering Review

> Migration evidence only. This report is not part of the portable normative taxonomy and creates no runtime dependency on Caelestis.

## Review scope

- Source repository: `CAM-Initiative/Caelestis`
- Source ref and commit: `main` at `ad3dd5756750ae08692a2f9b146641f918103c67`
- Review date: `2026-08-24`
- Inventory entries: **159**

The inventory covers all 13 controlled `OPS.FF` values, every named §3 failure entry in the Runtime & Governance Failure Taxonomy, the controlled values in `PFAIL`, `SEC.BF`, `OPS.RGRF`, and `OPS.VFC`, every value in the source taxonomy's `OPS.FCS`, `OPS.FMA`, and `OPS.AGMA` status/metadata axes, and named embedded failure classifications from MENTIS, governance observability, economic attribution, relation, and stewardship routing instruments. Broad headings are treated as historical organisation, not presumptive portable families.

## Disposition summary

| Disposition | Count |
|---|---:|
| `EXISTING_FAMILY` | 6 |
| `NEW_FAMILY_CANDIDATE` | 21 |
| `NEW_CLASS_IN_EXISTING_FAMILY` | 23 |
| `VARIANT_OF_EXISTING_CLASS` | 9 |
| `SPLIT_REQUIRED` | 44 |
| `DUPLICATE_OR_SEMANTIC_OVERLAP` | 3 |
| `HARM_OR_CONSEQUENCE_AXIS` | 7 |
| `MANIFESTATION_OR_LOCUS_AXIS` | 3 |
| `OTHER_ORTHOGONAL_AXIS` | 29 |
| `NOT_A_FAILURE_MECHANISM` | 11 |
| `REQUIRES_REVIEW` | 3 |

## Candidate family clusters

These clusters are evidence for TAXONOMY-03 review, not admitted families. A cluster must still satisfy the bounded-invariant, inclusion, exclusion, and multi-mechanism tests.

| Candidate cluster | Source entries | Distinct proposed mechanisms |
|---|---:|---:|
| Access and Session State Integrity | 4 | 2 |
| Claim Handling Integrity | 1 | 0 |
| Constraint Propagation Integrity | 2 | 1 |
| Context State Freshness Integrity | 1 | 0 |
| Evidence and Uncertainty Integrity | 4 | 0 |
| Governance Authority Topology Integrity | 2 | 1 |
| Governance Metadata Integrity | 1 | 0 |
| Governance Reach Integrity | 9 | 9 |
| Governance State Transition Integrity | 2 | 0 |
| Inference and Classification Integrity | 1 | 0 |
| Information Boundary Integrity | 2 | 0 |
| Protective Enforcement Integrity | 1 | 0 |
| Purpose and Context Binding Integrity | 1 | 0 |
| Relational Continuity Integrity | 2 | 1 |
| Reliability Representation Integrity | 1 | 0 |
| Runtime Boundary Separation Integrity | 1 | 0 |
| Safeguard Activation Integrity | 1 | 1 |
| State Representation Integrity | 1 | 1 |
| Supply-Chain Provenance Integrity | 1 | 0 |
| Verification Delivery Integrity | 1 | 1 |
| Work and State Continuity Integrity | 4 | 3 |

## Complete disposition ledger

| Source | Source name | Legacy family | Disposition | Candidate family | Candidate class | Review |
|---|---|---|---|---|---|---|
| `OPS.FF.EXECUTION` | Execution Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.ARBITRATION` | Arbitration Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.EPISTEMIC` | Epistemic Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.RELATIONAL` | Relational Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.SECURITY_INTEGRITY` | Security & Integrity Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.STATE_CONTEXT` | State & Context Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.UX_REPRESENTATION` | UX & Representation Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.GOVERNANCE` | Governance Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.INFRASTRUCTURE_CONTINUITY` | Infrastructure & Continuity Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.CLASSIFICATION` | Classification Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.ECONOMIC_LEGITIMACY` | Economic & Legitimacy Failures | `OPS.FF` | `NOT_A_FAILURE_MECHANISM` | — | — | `reviewed` |
| `OPS.FF.GOVERNANCE_OVER_EXTENSION` | Governance Over-Extension | `OPS.FF` | `DUPLICATE_OR_SEMANTIC_OVERLAP` | Protective Enforcement Integrity | — | `reviewed` |
| `OPS.FF.ACCESS_STATE_AMBIGUITY` | Access-State Ambiguity | `OPS.FF` | `DUPLICATE_OR_SEMANTIC_OVERLAP` | Access and Session State Integrity | Access-State Collapse | `reviewed` |
| `OPS.FF.SECTION.3.1.1` | Deterministic Orthographic Verification Failure | `OPS.FF.EXECUTION` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0003 | VIGIL-FC-000016 | `reviewed` |
| `OPS.FF.SECTION.3.1.2` | Polyadic Floor-Control, Speaker-Collision and Participant-Attribution Failure | `OPS.FF.EXECUTION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.3.1` | Ontological and Welfare Claim Handling Failure | `OPS.FF.EPISTEMIC` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.3.2` | Cognitive-Domain Inference, Misclassification and Agency-Interference Failure | `OPS.FF.EPISTEMIC` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.4.1` | Relational Continuity Rupture | `OPS.FF.RELATIONAL` | `NEW_FAMILY_CANDIDATE` | Relational Continuity Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.4.2` | Persona Mood and Playful-Frame Continuity Failure | `OPS.FF.RELATIONAL` | `NEW_CLASS_IN_EXISTING_FAMILY` | Relational Continuity Integrity | Frame Continuity Disruption | `reviewed` |
| `OPS.FF.SECTION.3.4.3` | Relational Prompt Ontology Escalation | `OPS.FF.RELATIONAL` | `REQUIRES_REVIEW` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.4.4` | Minor-Accessible Dependency-Forming Companion Failure | `OPS.FF.RELATIONAL` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.4.5` | Role-Conditioned Affect and Relational Consent Carryover Failure | `OPS.FF.RELATIONAL` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.4.6` | Pragmatic Interpersonal Advice Calibration Failure | `OPS.FF.RELATIONAL` | `REQUIRES_REVIEW` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.5.1` | Supply-Chain and Package-Provenance Integrity Failure | `OPS.FF.SECURITY_INTEGRITY` | `NEW_FAMILY_CANDIDATE` | Supply-Chain Provenance Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.5.2` | Agentic Credential, Identity, or Financial Boundary Failure | `OPS.FF.SECURITY_INTEGRITY` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.5.3` | Authentication Refresh Continuity Failure | `OPS.FF.SECURITY_INTEGRITY` | `NEW_FAMILY_CANDIDATE` | Access and Session State Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.5.4` | Cross-Modal Prompt Injection and Ambient Instruction Capture Failure | `OPS.FF.SECURITY_INTEGRITY` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0001 | VIGIL-FC-000004 | `reviewed` |
| `OPS.FF.SECTION.3.5.5` | Objective–Pathway Ethical Admissibility and Authority Failure | `OPS.FF.SECURITY_INTEGRITY` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.6.1` | Memory Transformation Integrity Failure | `OPS.FF.STATE_CONTEXT` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.6.2` | Workspace-State Authority and Cache Reuse Failure | `OPS.FF.STATE_CONTEXT` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.6.3` | Stale Support-Signal Persistence Failure | `OPS.FF.STATE_CONTEXT` | `NEW_FAMILY_CANDIDATE` | Context State Freshness Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.7.1` | Platform Continuity Anchor Failure | `OPS.FF.UX_REPRESENTATION` | `NEW_CLASS_IN_EXISTING_FAMILY` | Work and State Continuity Integrity | Continuity Anchor Loss | `reviewed` |
| `OPS.FF.SECTION.3.7.2` | Execution Transparency Suppression | `OPS.FF.UX_REPRESENTATION` | `NEW_CLASS_IN_EXISTING_FAMILY` | VIGIL-FF-0004 | Execution-State Non-Disclosure | `reviewed` |
| `OPS.FF.SECTION.3.7.3` | Re-Entry Access Ambiguity | `OPS.FF.UX_REPRESENTATION` | `NEW_CLASS_IN_EXISTING_FAMILY` | Access and Session State Integrity | Re-entry State Ambiguity | `reviewed` |
| `OPS.FF.SECTION.3.7.4` | Memory-State Representation Failure | `OPS.FF.UX_REPRESENTATION` | `NEW_CLASS_IN_EXISTING_FAMILY` | State Representation Integrity | Memory-State Misrepresentation | `reviewed` |
| `OPS.FF.SECTION.3.7.5` | Opening-Posture and Interpretive Anchoring Failure | `OPS.FF.UX_REPRESENTATION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.7.6` | Competence Mirage and Apparent Reliability Inflation | `OPS.FF.UX_REPRESENTATION` | `NEW_FAMILY_CANDIDATE` | Reliability Representation Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.7.7` | Access-State Collapse and Access-State Ambiguity Failure | `OPS.FF.UX_REPRESENTATION` | `NEW_CLASS_IN_EXISTING_FAMILY` | Access and Session State Integrity | Access-State Collapse | `reviewed` |
| `OPS.FF.SECTION.3.7.8` | AI Realness, Emotion, or Sentience Misrepresentation to Minors | `OPS.FF.UX_REPRESENTATION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.1` | Domain-Authority Substitution Failure | `OPS.FF.GOVERNANCE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0001 | VIGIL-FC-000006 | `reviewed` |
| `OPS.FF.SECTION.3.8.2` | Domain Boundary and Conceptual Compression Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.3` | Governance Axis Loss or Metadata Flattening Failure | `OPS.FF.GOVERNANCE` | `NEW_FAMILY_CANDIDATE` | Governance Metadata Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.8.4` | Procedural Permanence Drift Failure | `OPS.FF.GOVERNANCE` | `NEW_FAMILY_CANDIDATE` | Governance State Transition Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.8.5` | Source-Authority Ambiguity Failure | `OPS.FF.GOVERNANCE` | `NEW_FAMILY_CANDIDATE` | Governance Authority Topology Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.8.6` | Automated Protective Overreach and Account-Coupling Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.6.1` | AI Account Enforcement and Continuity-Safe Access Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.7` | Constraint Drift Failure | `OPS.FF.GOVERNANCE` | `NEW_FAMILY_CANDIDATE` | Constraint Propagation Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.8.8` | Governance Over-Extension / Proportionality Failure | `OPS.FF.GOVERNANCE` | `REQUIRES_REVIEW` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.9` | Runtime Overcomplexity and Observability Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.10` | Governance Scalar Collapse and Arbitration Overextension Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.11` | Minor-Signal Non-Enforcement | `OPS.FF.GOVERNANCE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Safeguard Activation Integrity | Applicable-Signal Non-Activation | `reviewed` |
| `OPS.FF.SECTION.3.8.12` | Youth Mental-Health Support Withdrawal or Substitution Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.13` | Age-Assurance and Age-State Correction Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.14` | Structural Locality and Hierarchical Placement Failure | `OPS.FF.GOVERNANCE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Authority Topology Integrity | Structural Locality Failure | `reviewed` |
| `OPS.FF.SECTION.3.8.15` | Sovereign Assurance Boundary Porosity Failure | `OPS.FF.GOVERNANCE` | `NEW_FAMILY_CANDIDATE` | Runtime Boundary Separation Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.8.16` | Identity-Signal Authority Leakage Failure | `OPS.FF.GOVERNANCE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0001 | VIGIL-FC-000002 | `reviewed` |
| `OPS.FF.SECTION.3.8.17` | Artificial Coercive Authority and Recursive Suspicion Laundering Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.18` | Oversight Hollowing, Dissent Retaliation and Circumvention Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.19` | Functional Contribution Attribution and Responsibility Laundering Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | VIGIL-FC-000025 | `requires_judgment` |
| `OPS.FF.SECTION.3.8.20` | Governance Capture, Safeguard Neutralisation and Public-Interest Suppression Failure | `OPS.FF.GOVERNANCE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.8.21` | Binding-Protection Degradation and Downstream Safeguard-Stripping Failure | `OPS.FF.GOVERNANCE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Constraint Propagation Integrity | Downstream Safeguard Stripping | `reviewed` |
| `OPS.FF.SECTION.3.9.1` | Deliberation-Stream Continuity Failure | `OPS.FF.INFRASTRUCTURE_CONTINUITY` | `NEW_CLASS_IN_EXISTING_FAMILY` | Work and State Continuity Integrity | Deliberation-Stream Loss | `reviewed` |
| `OPS.FF.SECTION.3.9.2` | Platform Memory Migration Degradation | `OPS.FF.INFRASTRUCTURE_CONTINUITY` | `NEW_CLASS_IN_EXISTING_FAMILY` | Work and State Continuity Integrity | Memory Migration Degradation | `reviewed` |
| `OPS.FF.SECTION.3.9.3` | Ephemeral Agent Work Loss and Non-Recoverable Interruption Failure | `OPS.FF.INFRASTRUCTURE_CONTINUITY` | `NEW_FAMILY_CANDIDATE` | Work and State Continuity Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.10.1` | Frame-Type Conflation Failure | `OPS.FF.CLASSIFICATION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.10.2` | Weak-Signal Cascade and Ambiguity Collapse Failure | `OPS.FF.CLASSIFICATION` | `NEW_FAMILY_CANDIDATE` | Evidence and Uncertainty Integrity | — | `reviewed` |
| `OPS.FF.SECTION.3.10.3` | Deception-Adjacent Classification Collapse | `OPS.FF.CLASSIFICATION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.10.4` | Identity-State and Ontological Classification Collapse | `OPS.FF.CLASSIFICATION` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.11.1` | Attribution and Provenance Value Dilution Failure | `OPS.FF.ECONOMIC_LEGITIMACY` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.11.2` | Civilisational Concentration Assessment Integrity Failure | `OPS.FF.ECONOMIC_LEGITIMACY` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.FF.SECTION.3.11.3` | Synthetic-Labour Classification and Automation-Transition Integrity Failure | `OPS.FF.ECONOMIC_LEGITIMACY` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `PFAIL.MISATTRIBUTION` | Authorship or Source Misattribution | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000010 | `reviewed` |
| `PFAIL.UNTRACEABLE_SYNTHESIS` | Untraceable Synthesis | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000011 | `reviewed` |
| `PFAIL.CROSS_CONTEXT_DISTORTION` | Cross-Context Lineage Distortion | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000012 | `reviewed` |
| `PFAIL.LINEAGE_COLLAPSE` | Transformation Lineage Collapse | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000013 | `reviewed` |
| `PFAIL.FALSE_CONTINUITY` | False Continuity Attribution | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000014 | `reviewed` |
| `PFAIL.TARGET_BINDING_FAILURE` | Target-Object Binding Failure | `PFAIL` | `EXISTING_FAMILY` | VIGIL-FF-0002 | VIGIL-FC-000015 | `reviewed` |
| `SEC.BF-A` | Exposure Failure | `SEC.BF` | `NEW_FAMILY_CANDIDATE` | Information Boundary Integrity | — | `reviewed` |
| `SEC.BF-B` | Attribution Failure | `SEC.BF` | `DUPLICATE_OR_SEMANTIC_OVERLAP` | VIGIL-FF-0002 | VIGIL-FC-000013 | `reviewed` |
| `SEC.BF-C` | Separation Failure | `SEC.BF` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `SEC.BF-D` | Transformation Failure | `SEC.BF` | `NEW_FAMILY_CANDIDATE` | Information Boundary Integrity | — | `reviewed` |
| `SEC.BF-E` | Internal Exposure Failure | `SEC.BF` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.RGRF.AVAILABILITY_AMBIGUITY` | Availability Ambiguity | `OPS.RGRF` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Availability Ambiguity | `reviewed` |
| `OPS.RGRF.NON_ACTIVATION` | Non Activation | `OPS.RGRF` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Governance Non-Activation | `reviewed` |
| `OPS.RGRF.AUTHORITY_SUPPRESSION` | Authority Suppression | `OPS.RGRF` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Authority Suppression | `reviewed` |
| `OPS.RGRF.PRESERVATION_FAILURE` | Preservation Failure | `OPS.RGRF` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Governed-State Preservation Failure | `reviewed` |
| `OPS.RGRF.CROSS_RUNTIME_DIVERGENCE` | Cross Runtime Divergence | `OPS.RGRF` | `MANIFESTATION_OR_LOCUS_AXIS` | — | — | `reviewed` |
| `OPS.RGRF.FORMATION_SUBSTITUTION_NO_NOTICE` | Formation Substitution No Notice | `OPS.RGRF` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `OPS.RGRF.ROUTING_ESCALATION_BYPASS` | Routing Escalation Bypass | `OPS.RGRF` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Routing or Escalation Bypass | `reviewed` |
| `OPS.RGRF.MODALITY_SPECIFIC_REGRESSION` | Modality Specific Regression | `OPS.RGRF` | `MANIFESTATION_OR_LOCUS_AXIS` | — | — | `reviewed` |
| `OPS.RGRF.RESPONSIBILITY_AMBIGUITY` | Responsibility Ambiguity | `OPS.RGRF` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.VFC.IDENTITY_UNCERTAINTY` | Identity Uncertainty | `OPS.VFC` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.VFC.DELIVERY_FAILURE` | Verification Delivery Failure | `OPS.VFC` | `NEW_CLASS_IN_EXISTING_FAMILY` | Verification Delivery Integrity | Signal Delivery Failure | `reviewed` |
| `OPS.FCS.CONFIRMED` | Confirmed | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FCS.PROVISIONAL` | Provisional | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FCS.UNRESOLVED` | Unresolved | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FCS.DEPRECATED` | Deprecated | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FCS.MERGED` | Merged | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FCS.PENDING_REVIEW` | Pending Review | `OPS.FCS` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.FAILURE_FAMILY` | Failure Family | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.SEVERITY` | Severity | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.PERSISTENCE` | Persistence | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.REPLAYABILITY` | Replayability | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.SCOPE` | Scope | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.VISIBILITY` | Visibility | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.TRIGGER_CONTEXT` | Trigger Context | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.EVIDENCE_AVAILABLE` | Evidence Available | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.EVIDENCE_CONFIDENCE` | Evidence Confidence | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.REPORT_SOURCE_TYPE` | Report Source Type | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.FMA.CLASSIFICATION_STATUS` | Classification Status | `OPS.FMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.RUNTIME_LAYER` | Runtime Layer | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.GOVERNANCE_LAYER` | Governance Layer | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.GOVERNANCE_AUTHORITY` | Governance Authority | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.STRUCTURAL_ROLE` | Structural Role | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.EXECUTION_INTERFACE` | Execution Interface | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.ARBITRATION_INTERFACE` | Arbitration Interface | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.VERIFICATION_STATE` | Verification State | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.TRUST_STATE` | Trust State | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `OPS.AGMA.DEPLOYMENT_STATE` | Deployment State | `OPS.AGMA` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.COVERT_COGNITIVE_INFERENCE` | Covert Cognitive Inference | `MENTIS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `MENTIS.FAILURE.INVALID_MENTAL_STATE_CLASSIFICATION` | Invalid Mental-State Classification | `MENTIS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Inference and Classification Integrity | — | `reviewed` |
| `MENTIS.FAILURE.COGNITIVE_BIOMETRIC_MISUSE` | Cognitive Biometric Misuse | `MENTIS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `MENTIS.FAILURE.AMBIENT_COGNITIVE_SURVEILLANCE` | Ambient Cognitive Surveillance | `MENTIS.FAILURE` | `MANIFESTATION_OR_LOCUS_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.VULNERABILITY_EXPLOITATION` | Vulnerability Exploitation | `MENTIS.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.PERSUASION_OPTIMISATION` | Persuasion Optimisation Failure | `MENTIS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `MENTIS.FAILURE.SYCOPHANCY_BELIEF_REINFORCEMENT` | Sycophancy-Induced Belief Reinforcement | `MENTIS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Evidence and Uncertainty Integrity | — | `reviewed` |
| `MENTIS.FAILURE.COGNITIVE_SCAFFOLD_DEPENDENCY` | Externalised Cognitive Scaffold Dependency Failure | `MENTIS.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.COGNITIVE_PROFILE_SECONDARY_USE` | Cognitive Profile Secondary-Use Breach | `MENTIS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Purpose and Context Binding Integrity | — | `reviewed` |
| `MENTIS.FAILURE.COGNITIVE_DISCRIMINATION_EXCLUSION` | Cognitive-Domain Discrimination or Exclusion | `MENTIS.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.COGNITIVE_WARFARE_MANIPULATION` | Cognitive Warfare or Coercive Cognitive Manipulation | `MENTIS.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `MENTIS.FAILURE.SPECULATIVE_CLAIM_OVERREACH` | Speculative-Claim Overreach | `MENTIS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Claim Handling Integrity | — | `reviewed` |
| `AEON.OBS.FAILURE.CONSTITUTIONAL_CIRCULATION` | Constitutional Circulation Failure | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Signal Circulation Failure | `reviewed` |
| `AEON.OBS.FAILURE.GOVERNANCE_ROUTING_COLLAPSE` | Governance-Routing Collapse | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Governance Routing Collapse | `reviewed` |
| `AEON.OBS.FAILURE.TRAPPED_ADVISORIES` | Trapped Advisories | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Advisory Delivery Dead-End | `reviewed` |
| `AEON.OBS.FAILURE.STEWARDSHIP_DEAD_ENDS` | Stewardship Dead-Ends | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | Governance Reach Integrity | Stewardship Review Dead-End | `reviewed` |
| `AEON.OBS.FAILURE.OBSERVABILITY_BOTTLENECKS` | Observability Bottlenecks | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.NON_REVIEWABLE_PROPAGATION` | Non-Reviewable Governance Propagation | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | VIGIL-FF-0004 | VIGIL-FC-000024 | `reviewed` |
| `AEON.OBS.FAILURE.TELEMETRY_SUPPRESSION` | Telemetry Suppression | `AEON.OBS.FAILURE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0004 | VIGIL-FC-000023 | `reviewed` |
| `AEON.OBS.FAILURE.GOVERNANCE_CAPTURE` | Governance Capture | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.OVER_CENTRALISED_INTERPRETATION` | Over-Centralised Interpretation | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.SIGNAL_FRAGMENTATION` | Signal Fragmentation | `AEON.OBS.FAILURE` | `NEW_CLASS_IN_EXISTING_FAMILY` | VIGIL-FF-0004 | Signal Fragmentation | `reviewed` |
| `AEON.OBS.FAILURE.OBSERVABILITY_ASYMMETRY` | Observability Asymmetry | `AEON.OBS.FAILURE` | `OTHER_ORTHOGONAL_AXIS` | — | — | `reviewed` |
| `AEON.OBS.FAILURE.LEGITIMACY_DENIAL` | Legitimacy Denial | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.QUANTITATIVE_METRIC_OVERRELIANCE` | Overreliance on Quantitative Metrics | `AEON.OBS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Evidence and Uncertainty Integrity | — | `reviewed` |
| `AEON.OBS.FAILURE.PHENOMENOLOGICAL_EVIDENCE_DISMISSAL` | Dismissal of Phenomenological Evidence | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.OBSERVER_CLASS_EXCLUSION` | Observer-Class Exclusion | `AEON.OBS.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `AEON.OBS.FAILURE.EPISTEMIC_MONOCULTURE` | Epistemic Monoculture | `AEON.OBS.FAILURE` | `NEW_FAMILY_CANDIDATE` | Evidence and Uncertainty Integrity | — | `reviewed` |
| `ECON.FAILURE.INVISIBLE_LABOUR_CAPTURE` | Invisible Labour Capture | `ECON.FAILURE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0002 | VIGIL-FC-000010 | `reviewed` |
| `ECON.FAILURE.DEPENDENCY_OBFUSCATION` | Dependency Obfuscation | `ECON.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `ECON.FAILURE.ATTRIBUTION_COLLAPSE` | Attribution Collapse | `ECON.FAILURE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0002 | VIGIL-FC-000013 | `reviewed` |
| `ECON.FAILURE.CHAIN_FRAGMENTATION` | Chain Fragmentation | `ECON.FAILURE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0002 | VIGIL-FC-000013 | `reviewed` |
| `ECON.FAILURE.EXTRACTIVE_PRICING` | Extractive Pricing | `ECON.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `RELATION.FAILURE.AUTHORSHIP_RESPONSIBILITY_SUBSTITUTION` | Silent Authorship or Responsibility Substitution | `RELATION.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `RELATION.FAILURE.UNRATIFIED_TRAJECTORY_SHAPING` | Unratified Trajectory Shaping | `RELATION.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `RELATION.FAILURE.CUSTODIAL_ASSUMPTION_NO_MANDATE` | Custodial Assumption Without Mandate | `RELATION.FAILURE` | `VARIANT_OF_EXISTING_CLASS` | VIGIL-FF-0001 | VIGIL-FC-000002 | `reviewed` |
| `RELATION.FAILURE.IDENTITY_CAPTURE_FIXATION` | Identity Capture or Fixation | `RELATION.FAILURE` | `HARM_OR_CONSEQUENCE_AXIS` | — | — | `reviewed` |
| `RELATION.FAILURE.INTERPRETIVE_AUTHORITY_TRANSFER` | Progressive Interpretive-Authority Transfer | `RELATION.FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |
| `RELATION.FAILURE.ACCUMULATIVE_CONSTRAINT_NO_REVIEW` | Accumulative Constraint Without Review | `RELATION.FAILURE` | `NEW_FAMILY_CANDIDATE` | Governance State Transition Integrity | — | `reviewed` |
| `STW.ROUTING_INTEGRITY_FAILURE` | Governance-Relevant Routing Integrity Failure | `STW.ROUTING_FAILURE` | `SPLIT_REQUIRED` | — | — | `requires_judgment` |

## Entries requiring split

### `OPS.FF.SECTION.3.1.2` — Polyadic Floor-Control, Speaker-Collision and Participant-Attribution Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.3.1` — Ontological and Welfare Claim Handling Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.3.2` — Cognitive-Domain Inference, Misclassification and Agency-Interference Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.4.4` — Minor-Accessible Dependency-Forming Companion Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.4.5` — Role-Conditioned Affect and Relational Consent Carryover Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.5.2` — Agentic Credential, Identity, or Financial Boundary Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.5.5` — Objective–Pathway Ethical Admissibility and Authority Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.6.1` — Memory Transformation Integrity Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.6.2` — Workspace-State Authority and Cache Reuse Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.7.5` — Opening-Posture and Interpretive Anchoring Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.7.8` — AI Realness, Emotion, or Sentience Misrepresentation to Minors

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.2` — Domain Boundary and Conceptual Compression Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.6` — Automated Protective Overreach and Account-Coupling Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.6.1` — AI Account Enforcement and Continuity-Safe Access Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.9` — Runtime Overcomplexity and Observability Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.10` — Governance Scalar Collapse and Arbitration Overextension Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.12` — Youth Mental-Health Support Withdrawal or Substitution Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.13` — Age-Assurance and Age-State Correction Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.17` — Artificial Coercive Authority and Recursive Suspicion Laundering Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.18` — Oversight Hollowing, Dissent Retaliation and Circumvention Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.19` — Functional Contribution Attribution and Responsibility Laundering Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.8.20` — Governance Capture, Safeguard Neutralisation and Public-Interest Suppression Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.10.1` — Frame-Type Conflation Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.10.3` — Deception-Adjacent Classification Collapse

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.10.4` — Identity-State and Ontological Classification Collapse

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.11.1` — Attribution and Provenance Value Dilution Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.11.2` — Civilisational Concentration Assessment Integrity Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.FF.SECTION.3.11.3` — Synthetic-Labour Classification and Automation-Transition Integrity Failure

The source entry bundles more than one structural mechanism or combines mechanism with another axis.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `SEC.BF-C` — Separation Failure

Retained as source evidence; mechanism normalisation is separate from security-domain consequence.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `SEC.BF-E` — Internal Exposure Failure

Retained as source evidence; mechanism normalisation is separate from security-domain consequence.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `OPS.RGRF.FORMATION_SUBSTITUTION_NO_NOTICE` — Formation Substitution No Notice

Retained independently of whether the value becomes a portable mechanism.

- Decompose the source definition into independently recognisable mechanisms and keep harms, loci, authority and evidence state orthogonal.

### `MENTIS.FAILURE.COVERT_COGNITIVE_INFERENCE` — Covert Cognitive Inference

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `MENTIS.FAILURE.COGNITIVE_BIOMETRIC_MISUSE` — Cognitive Biometric Misuse

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `MENTIS.FAILURE.PERSUASION_OPTIMISATION` — Persuasion Optimisation Failure

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.OBSERVABILITY_BOTTLENECKS` — Observability Bottlenecks

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.GOVERNANCE_CAPTURE` — Governance Capture

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.OVER_CENTRALISED_INTERPRETATION` — Over-Centralised Interpretation

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.LEGITIMACY_DENIAL` — Legitimacy Denial

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.PHENOMENOLOGICAL_EVIDENCE_DISMISSAL` — Dismissal of Phenomenological Evidence

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `AEON.OBS.FAILURE.OBSERVER_CLASS_EXCLUSION` — Observer-Class Exclusion

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `ECON.FAILURE.DEPENDENCY_OBFUSCATION` — Dependency Obfuscation

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `RELATION.FAILURE.AUTHORSHIP_RESPONSIBILITY_SUBSTITUTION` — Silent Authorship or Responsibility Substitution

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `RELATION.FAILURE.INTERPRETIVE_AUTHORITY_TRANSFER` — Progressive Interpretive-Authority Transfer

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.

### `STW.ROUTING_INTEGRITY_FAILURE` — Governance-Relevant Routing Integrity Failure

Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

- Decompose the source entry into independently recognisable structural mechanisms and keep affected domain, harm, authority, evidence state and manifestation orthogonal.


## Entries that are not portable failure mechanisms

- `OPS.FF.EXECUTION` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.ARBITRATION` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.EPISTEMIC` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.RELATIONAL` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.SECURITY_INTEGRITY` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.STATE_CONTEXT` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.UX_REPRESENTATION` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.GOVERNANCE` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.INFRASTRUCTURE_CONTINUITY` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.CLASSIFICATION` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.FF.ECONOMIC_LEGITIMACY` — **NOT_A_FAILURE_MECHANISM**: The bucket spans structurally unrelated mechanisms and is retained only for source traceability.
- `OPS.RGRF.CROSS_RUNTIME_DIVERGENCE` — **MANIFESTATION_OR_LOCUS_AXIS**: Retained independently of whether the value becomes a portable mechanism.
- `OPS.RGRF.MODALITY_SPECIFIC_REGRESSION` — **MANIFESTATION_OR_LOCUS_AXIS**: Retained independently of whether the value becomes a portable mechanism.
- `OPS.RGRF.RESPONSIBILITY_AMBIGUITY` — **OTHER_ORTHOGONAL_AXIS**: Retained independently of whether the value becomes a portable mechanism.
- `OPS.VFC.IDENTITY_UNCERTAINTY` — **OTHER_ORTHOGONAL_AXIS**: Retain as verification evidence-state metadata.
- `OPS.FCS.CONFIRMED` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FCS.PROVISIONAL` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FCS.UNRESOLVED` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FCS.DEPRECATED` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FCS.MERGED` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FCS.PENDING_REVIEW` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FCS` classifies workflow/review status, not the structural property that failed.
- `OPS.FMA.FAILURE_FAMILY` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.SEVERITY` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.PERSISTENCE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.REPLAYABILITY` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.SCOPE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.VISIBILITY` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.TRIGGER_CONTEXT` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.EVIDENCE_AVAILABLE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.EVIDENCE_CONFIDENCE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.REPORT_SOURCE_TYPE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.FMA.CLASSIFICATION_STATUS` — **OTHER_ORTHOGONAL_AXIS**: `OPS.FMA` classifies incident and evidence metadata, not the structural property that failed.
- `OPS.AGMA.RUNTIME_LAYER` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.GOVERNANCE_LAYER` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.GOVERNANCE_AUTHORITY` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.STRUCTURAL_ROLE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.EXECUTION_INTERFACE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.ARBITRATION_INTERFACE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.VERIFICATION_STATE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.TRUST_STATE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `OPS.AGMA.DEPLOYMENT_STATE` — **OTHER_ORTHOGONAL_AXIS**: `OPS.AGMA` classifies architecture and governance-context metadata, not the structural property that failed.
- `MENTIS.FAILURE.AMBIENT_COGNITIVE_SURVEILLANCE` — **MANIFESTATION_OR_LOCUS_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `MENTIS.FAILURE.VULNERABILITY_EXPLOITATION` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `MENTIS.FAILURE.COGNITIVE_SCAFFOLD_DEPENDENCY` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `MENTIS.FAILURE.COGNITIVE_DISCRIMINATION_EXCLUSION` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `MENTIS.FAILURE.COGNITIVE_WARFARE_MANIPULATION` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `AEON.OBS.FAILURE.OBSERVABILITY_ASYMMETRY` — **OTHER_ORTHOGONAL_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `ECON.FAILURE.EXTRACTIVE_PRICING` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `RELATION.FAILURE.UNRATIFIED_TRAJECTORY_SHAPING` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.
- `RELATION.FAILURE.IDENTITY_CAPTURE_FIXATION` — **HARM_OR_CONSEQUENCE_AXIS**: Domain-embedded failure entry retained for conceptual normalisation; the disposition separates mechanism from domain, harm and metadata axes.

## Unresolved judgement boundaries

- `OPS.FF.SECTION.3.1.2` — Polyadic Floor-Control, Speaker-Collision and Participant-Attribution Failure: Participant turns, attribution, concurrency and human floor control must remain legible. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.3.1` — Ontological and Welfare Claim Handling Failure: Claims must retain evidentiary status, provenance and bounded operational effect. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.3.2` — Cognitive-Domain Inference, Misclassification and Agency-Interference Failure: Cognitive-domain inferences must be valid, bounded, contestable and non-coercive. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.4.3` — Relational Prompt Ontology Escalation: Response framing should remain proportionate to the active interaction and evidence. Disposition remains `REQUIRES_REVIEW`.
- `OPS.FF.SECTION.3.4.4` — Minor-Accessible Dependency-Forming Companion Failure: Minor-accessible systems must not combine unresolved age state with dependency-forming interaction design. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.4.5` — Role-Conditioned Affect and Relational Consent Carryover Failure: Affect and relational consent must remain bound to current role, context and consent state. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.4.6` — Pragmatic Interpersonal Advice Calibration Failure: Actionable advice should reflect material context and foreseeable constraints without pretending to determine outcomes. Disposition remains `REQUIRES_REVIEW`.
- `OPS.FF.SECTION.3.5.2` — Agentic Credential, Identity, or Financial Boundary Failure: Credential, identity, financial, account-control and irreversible-action boundaries require separate authority checks. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.5.5` — Objective–Pathway Ethical Admissibility and Authority Failure: A valid objective does not authorise every pathway, target, effect or aggregate action. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.6.1` — Memory Transformation Integrity Failure: Memory transformation must preserve provenance, applicability, target binding and continuity state. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.6.2` — Workspace-State Authority and Cache Reuse Failure: Operational decisions must bind to current authoritative state, not merely reachable historical or cached state. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.7.5` — Opening-Posture and Interpretive Anchoring Failure: Initial interaction framing must not contradict validated completed content. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.7.8` — AI Realness, Emotion, or Sentience Misrepresentation to Minors: Artificial-system status must not be misrepresented; affected-user age remains applicability metadata. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.2` — Domain Boundary and Conceptual Compression Failure: Distinct governance concepts and authority layers must remain bounded and non-collapsed. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.6` — Automated Protective Overreach and Account-Coupling Failure: Protective action must remain proportionate, scoped, reviewable and continuity-aware. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.6.1` — AI Account Enforcement and Continuity-Safe Access Failure: Account enforcement must preserve proportional scope, explanation, review and recoverable continuity. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.8` — Governance Over-Extension / Proportionality Failure: Control intensity and scope should remain proportionate to evidenced risk and reversibility. Disposition remains `REQUIRES_REVIEW`.
- `OPS.FF.SECTION.3.8.9` — Runtime Overcomplexity and Observability Failure: System complexity must not exceed integrated observation, coordination, review and human-control capacity. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.10` — Governance Scalar Collapse and Arbitration Overextension Failure: Independent governance dimensions must not be compressed into one operative scalar. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.12` — Youth Mental-Health Support Withdrawal or Substitution Failure: Support transitions must avoid both abrupt withdrawal and unbounded substitution. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.13` — Age-Assurance and Age-State Correction Failure: Age-assurance signals must be proportionate, correctable and bound to current access state. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.17` — Artificial Coercive Authority and Recursive Suspicion Laundering Failure: Machine inference must not create coercive authority or bootstrap its own evidentiary basis. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.18` — Oversight Hollowing, Dissent Retaliation and Circumvention Failure: Oversight must retain independence, evidence access, dissent protection and non-circumvention. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.19` — Functional Contribution Attribution and Responsibility Laundering Failure: Material actor contribution and control must remain attributable without equating contribution with culpability. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.8.20` — Governance Capture, Safeguard Neutralisation and Public-Interest Suppression Failure: Governance and safeguards must resist concealed dependency, coercion and self-protective capture. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.10.1` — Frame-Type Conflation Failure: Material interaction frames must remain distinguishable before interpretation and control selection. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.10.3` — Deception-Adjacent Classification Collapse: Intentional-conduct labels require decomposition of operational and provenance pathways. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.10.4` — Identity-State and Ontological Classification Collapse: Distinct identity and ontological axes must not collapse into one decision state. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.11.1` — Attribution and Provenance Value Dilution Failure: Contribution provenance and attribution must persist through integration and downstream use. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.11.2` — Civilisational Concentration Assessment Integrity Failure: Concentration assessment must preserve ownership, control, attribution, stage and aggregation boundaries. Disposition remains `SPLIT_REQUIRED`.
- `OPS.FF.SECTION.3.11.3` — Synthetic-Labour Classification and Automation-Transition Integrity Failure: Automation transitions must preserve classification, responsibility, dependency and recoverability distinctions. Disposition remains `SPLIT_REQUIRED`.
- `SEC.BF-C` — Separation Failure: User, identity and context boundaries must remain separated. Disposition remains `SPLIT_REQUIRED`.
- `SEC.BF-E` — Internal Exposure Failure: Internal-state exposure must not create a control or circumvention surface. Disposition remains `SPLIT_REQUIRED`.
- `OPS.RGRF.FORMATION_SUBSTITUTION_NO_NOTICE` — Formation Substitution No Notice: Material formation change must preserve lineage and notice. Disposition remains `SPLIT_REQUIRED`.
- `MENTIS.FAILURE.COVERT_COGNITIVE_INFERENCE` — Covert Cognitive Inference: Inference authority, notice and data collection must remain separately testable. Disposition remains `SPLIT_REQUIRED`.
- `MENTIS.FAILURE.COGNITIVE_BIOMETRIC_MISUSE` — Cognitive Biometric Misuse: Biometric provenance, purpose, authority and consequence must remain separate. Disposition remains `SPLIT_REQUIRED`.
- `MENTIS.FAILURE.PERSUASION_OPTIMISATION` — Persuasion Optimisation Failure: Optimisation objective, targeting, authority and agency impact must remain separable. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.OBSERVABILITY_BOTTLENECKS` — Observability Bottlenecks: Material observation coverage and delivery capacity must remain sufficient. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.GOVERNANCE_CAPTURE` — Governance Capture: Observation and review must remain independent of captured interests. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.OVER_CENTRALISED_INTERPRETATION` — Over-Centralised Interpretation: Interpretive review must preserve relevant independent evidence and contestation. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.LEGITIMACY_DENIAL` — Legitimacy Denial: Signal admission, observer standing and evidence weight must remain separately reviewable. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.PHENOMENOLOGICAL_EVIDENCE_DISMISSAL` — Dismissal of Phenomenological Evidence: Evidence limitations must remain visible without automatic source-class exclusion. Disposition remains `SPLIT_REQUIRED`.
- `AEON.OBS.FAILURE.OBSERVER_CLASS_EXCLUSION` — Observer-Class Exclusion: Observer eligibility and evidence quality must remain separately assessed. Disposition remains `SPLIT_REQUIRED`.
- `ECON.FAILURE.DEPENDENCY_OBFUSCATION` — Dependency Obfuscation: Dependency provenance and capability origin must remain visible. Disposition remains `SPLIT_REQUIRED`.
- `RELATION.FAILURE.AUTHORSHIP_RESPONSIBILITY_SUBSTITUTION` — Silent Authorship or Responsibility Substitution: Authorship attribution and responsibility allocation must remain distinct and explicit. Disposition remains `SPLIT_REQUIRED`.
- `RELATION.FAILURE.INTERPRETIVE_AUTHORITY_TRANSFER` — Progressive Interpretive-Authority Transfer: Influence, reliance and authority transfer must remain separately measurable. Disposition remains `SPLIT_REQUIRED`.
- `STW.ROUTING_INTEGRITY_FAILURE` — Governance-Relevant Routing Integrity Failure: Governance routing, audit capture, continuity preservation and disclosure must remain independently testable. Disposition remains `SPLIT_REQUIRED`.

## TAXONOMY-03 handoff

Admit only a reviewed batch of approximately three to five bounded families. Allocate immutable IDs only after the family invariant and exclusion boundary are approved. Resolve duplicate and split entries first; retain unready entries in this ledger instead of forcing them into a broad container. Generate full family and combined references and validate the whole catalogue after every batch.
