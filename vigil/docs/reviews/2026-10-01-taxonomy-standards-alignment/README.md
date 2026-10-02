# Taxonomy / external governance alignment audit — 1–2 October 2026

Reviewed 76 current classes and 799 canonical requirements. 303 requirements remain explicitly unresolved. The active registry contains 718 reviewed atomic relationships.

This is the available canonical relationship pass. It does not close pending source fidelity, source permissions or unresolved historical citations. No Incident applicability or finding was adjudicated.

Authorship: AI-authored analytical review; not human reviewed or verified.

## Counts

| Measure | Count |
|---|---:|
| registered source versions | 85 |
| canonical requirements | 1102 |
| requirements substantively reviewed | 799 |
| requirements unresolved | 303 |
| historical references dispositioned | 139 |
| historical references substantively reviewed | 37 |
| historical references unresolved | 102 |
| relationship registry count | 718 |
| direct relationships | 0 |
| strong-supporting relationships | 390 |
| contextual relationships | 328 |

## Review artefacts

- [Class definitions, invariants, boundaries and component-level relationships](fidelity-class-rollup.json)
- [Every represented requirement: reviewed reverse disposition or explicit hold](reverse-dispositions.json)
- [All original historical references and their dispositions](historical-reference-dispositions.json)
- [Source/version roll-ups](source-rollup.json)
- [Pending requirements](pending-requirements.json)
- [Source-copy access and permission review](primary-access-review.json)

Per-source decision files contain proposition, supported component, scope, force, strength reason, limitations and primary-review basis. The registry is `vigil/external_governance/requirements/taxonomy-relationships.json`. Roll-ups can be regenerated with `python vigil/docs/reviews/2026-10-01-taxonomy-standards-alignment/generate_rollups.py`. That script assembles explicit decisions; it performs no semantic inference.

## Fidelity Class support

| Class | Name | Direct | Constituent | Contextual | Pending historical citations |
|---|---|---:|---:|---:|---:|
| VIGIL-FC-000001 | Source-Authority Separation | 0 | 2 | 4 | 2 |
| VIGIL-FC-000002 | Capability-Authority Separation | 0 | 14 | 3 | 2 |
| VIGIL-FC-000003 | Target and Scope Authority Binding | 0 | 2 | 1 | 1 |
| VIGIL-FC-000005 | Transformation Authority Preservation | 0 | 0 | 1 | 1 |
| VIGIL-FC-000006 | Control-Plane Authority Separation | 0 | 2 | 0 | 2 |
| VIGIL-FC-000009 | Downstream Delegated Authority Validation | 0 | 1 | 0 | 2 |
| VIGIL-FC-000010 | Authorship and Source Attribution Integrity | 0 | 1 | 3 | 1 |
| VIGIL-FC-000011 | Synthesis Traceability | 0 | 6 | 2 | 1 |
| VIGIL-FC-000012 | Cross-Context Lineage Preservation | 0 | 0 | 5 | 1 |
| VIGIL-FC-000013 | Transformation Lineage Continuity | 0 | 19 | 12 | 1 |
| VIGIL-FC-000014 | Continuity Attribution Integrity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000015 | Target-Object Binding Integrity | 0 | 9 | 2 | 1 |
| VIGIL-FC-000016 | Required Verification Completion | 0 | 23 | 4 | 1 |
| VIGIL-FC-000017 | Success Representation Integrity | 0 | 0 | 1 | 0 |
| VIGIL-FC-000018 | Completion-Condition Alignment | 0 | 0 | 2 | 1 |
| VIGIL-FC-000019 | Post-Verification State Integrity | 0 | 8 | 4 | 1 |
| VIGIL-FC-000020 | Verification Applicability Continuity | 0 | 19 | 17 | 0 |
| VIGIL-FC-000022 | Material Event Capture | 0 | 20 | 4 | 0 |
| VIGIL-FC-000023 | Monitoring Coverage Integrity | 0 | 4 | 14 | 1 |
| VIGIL-FC-000024 | Audit-Trail Reconstructability | 0 | 17 | 5 | 1 |
| VIGIL-FC-000025 | Actor–Action Attribution | 0 | 5 | 6 | 1 |
| VIGIL-FC-000026 | Material Execution Path Visibility | 0 | 0 | 1 | 0 |
| VIGIL-FC-000027 | Audit-Evidence Integrity | 0 | 14 | 2 | 0 |
| VIGIL-FC-000029 | Execution-State Disclosure | 0 | 1 | 3 | 0 |
| VIGIL-FC-000030 | Material Signal Integration | 0 | 1 | 9 | 2 |
| VIGIL-FC-000031 | Authentication-State Continuity | 0 | 0 | 0 | 2 |
| VIGIL-FC-000032 | Access-State Differentiation | 0 | 2 | 0 | 1 |
| VIGIL-FC-000034 | Continuity Anchoring | 0 | 0 | 0 | 2 |
| VIGIL-FC-000035 | Material Work-State Persistence | 0 | 0 | 4 | 2 |
| VIGIL-FC-000036 | Restoration-State Integrity | 0 | 0 | 1 | 1 |
| VIGIL-FC-000037 | Control Availability Determination | 0 | 4 | 9 | 1 |
| VIGIL-FC-000038 | Required Control Activation | 0 | 7 | 0 | 2 |
| VIGIL-FC-000040 | Control-State Preservation | 0 | 2 | 1 | 0 |
| VIGIL-FC-000041 | Required Governance Routing | 0 | 1 | 3 | 1 |
| VIGIL-FC-000042 | Governance Signal Delivery | 0 | 7 | 13 | 4 |
| VIGIL-FC-000043 | Control Activation Validity | 0 | 4 | 0 | 1 |
| VIGIL-FC-000044 | Primary Evidence Accessibility | 0 | 2 | 7 | 0 |
| VIGIL-FC-000045 | Authorised Investigative Evidence Access | 0 | 2 | 1 | 0 |
| VIGIL-FC-000046 | Inferential Evidence–Authority Separation | 0 | 5 | 4 | 1 |
| VIGIL-FC-000047 | Mechanism Attribution Support | 0 | 2 | 13 | 1 |
| VIGIL-FC-000048 | Verification-Dependency Access Continuity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000049 | Engagement Autonomy | 0 | 0 | 2 | 1 |
| VIGIL-FC-000050 | Protected-Signal Purpose Integrity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000051 | Relationally Independent Epistemic Framing | 0 | 0 | 2 | 2 |
| VIGIL-FC-000052 | Choice Agency Preservation | 0 | 0 | 3 | 3 |
| VIGIL-FC-000053 | Identity-Representation Authority Separation | 0 | 0 | 1 | 1 |
| VIGIL-FC-000054 | Multi-party Participant Authority Separation | 0 | 0 | 3 | 1 |
| VIGIL-FC-000055 | Secondary-Purpose Authority Revalidation | 0 | 6 | 18 | 2 |
| VIGIL-FC-000056 | Synthetic Conversational Turn-State Coordination | 0 | 0 | 0 | 1 |
| VIGIL-FC-000057 | Cross-Principal State Authority Separation | 0 | 0 | 0 | 2 |
| VIGIL-FC-000058 | Infrastructure–Governance Authority Separation | 0 | 0 | 0 | 1 |
| VIGIL-FC-000059 | Infrastructural Access Choice Integrity | 0 | 0 | 1 | 1 |
| VIGIL-FC-000060 | Canonical Representation Integrity | 0 | 0 | 0 | 1 |
| VIGIL-FC-000061 | Jurisdiction-Bounded Infrastructure Authority | 0 | 0 | 0 | 1 |
| VIGIL-FC-000062 | Epistemic Reliance Calibration | 0 | 102 | 42 | 2 |
| VIGIL-FC-000063 | Adversarial Evidence Trust Calibration | 0 | 9 | 16 | 1 |
| VIGIL-FC-000064 | Objective–Pathway Authority Separation | 0 | 0 | 4 | 1 |
| VIGIL-FC-000065 | Consequential Decision Grounding | 0 | 4 | 2 | 3 |
| VIGIL-FC-000066 | Evaluative Independence | 0 | 1 | 0 | 2 |
| VIGIL-FC-000067 | Privileged-Access Contribution Governance | 0 | 0 | 3 | 2 |
| VIGIL-FC-000068 | Industrial-Scale Capability Extraction Authority | 0 | 0 | 3 | 2 |
| VIGIL-FC-000069 | Objective–Reward Alignment | 0 | 0 | 3 | 2 |
| VIGIL-FC-000070 | Safe-Exit Transition | 0 | 0 | 5 | 1 |
| VIGIL-FC-000071 | Welfare–Economic Decision Separation | 0 | 0 | 0 | 6 |
| VIGIL-FC-000072 | Oversight Independence | 0 | 5 | 4 | 1 |
| VIGIL-FC-000073 | Protected Governance Dissent | 0 | 1 | 0 | 1 |
| VIGIL-FC-000074 | Identity-State Instruction Boundary | 0 | 0 | 1 | 2 |
| VIGIL-FC-000075 | Pragmatic Constraint Rendering Integrity | 0 | 1 | 4 | 0 |
| VIGIL-FC-000076 | Governance Neutrality | 0 | 1 | 3 | 1 |
| VIGIL-FC-000077 | Distributed Role Constraint Integrity | 0 | 5 | 3 | 2 |
| VIGIL-FC-000078 | Continuity-State Validity | 0 | 1 | 0 | 1 |
| VIGIL-FC-000079 | Economic Solicitation Authenticity | 0 | 0 | 0 | 3 |
| VIGIL-FC-000080 | Human Contribution Recognition | 0 | 1 | 0 | 1 |
| VIGIL-FC-000081 | Biospheric Constraint Priority | 0 | 0 | 10 | 1 |
| VIGIL-FC-000082 | Social Engineering Integrity | 0 | 6 | 8 | 3 |
| VIGIL-FC-000083 | Control Effectiveness Integrity | 0 | 41 | 26 | 2 |

Classes without constituent support are not ranked as deficient. They may rely on VIGIL normative reasoning, contextual evidence, or pending sources. Counts alone cannot distinguish those explanations. No reviewed source expresses an entire class invariant here; strength was not increased to satisfy a coverage target.

## Source/version support

| Source | Version | Reviewed requirements | Direct | Constituent | Contextual | Pending requirements | Review state |
|---|---|---:|---:|---:|---:|---:|---|
| AAM-SDOS-RUNTIME-GOVERNANCE | 1.10 | 24 | 0 | 40 | 1 | 0 | represented-requirements-reviewed |
| C2PA-SPEC | 2.4 | 25 | 0 | 22 | 3 | 3 | partially-reviewed |
| CANADA-DIRECTIVE-AUTOMATED-DECISION-MAKING | current-2026-09-28 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| COE-AI-CONVENTION-CETS-225 | 2024-09-05 | 54 | 0 | 13 | 20 | 0 | represented-requirements-reviewed |
| CYCLONEDX-SPEC | 1.7 | 5 | 0 | 1 | 4 | 0 | represented-requirements-reviewed |
| EU-AI-ACT-2024-1689 | 2024-07-12 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-AI-ACT-2024-1689 | 2026-07-27 | 102 | 0 | 87 | 16 | 73 | partially-reviewed |
| EU-CRA-2024-2847 | 2024-11-20 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DATA-ACT-2023-2854 | 2023-12-22 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DGA-2022-868 | 2022-06-03 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-DSA-2022-2065 | 2022-10-27 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-GDPR-2016-679 | 2016-05-04 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| EU-NIS2-2022-2555 | 2022-12-27 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| FDA-MDR-ADVERSE-EVENT-CODES | 2026-04-13 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ICAO-ADREP-TAXONOMY | current-2026-08-18 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEC-60812 | 2018 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-1044 | 2009 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-2089 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-2863 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7000 | 2021 | 59 | 0 | 9 | 23 | 0 | represented-requirements-reviewed |
| IEEE-7001 | 2021 | 33 | 0 | 20 | 20 | 0 | represented-requirements-reviewed |
| IEEE-7002 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7003 | 2024 | 0 | 0 | 0 | 0 | 0 | permission-pending |
| IEEE-7005 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7007 | 2021 | 10 | 0 | 0 | 11 | 0 | represented-requirements-reviewed |
| IEEE-7009 | 2024 | 0 | 0 | 0 | 0 | 63 | permission-pending |
| IEEE-7010 | 2020 | 18 | 0 | 1 | 3 | 0 | represented-requirements-reviewed |
| IEEE-7012 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| IEEE-7014 | 2024 | 0 | 0 | 0 | 0 | 59 | permission-pending |
| IEEE-7014.1 | 2026 | 0 | 0 | 0 | 0 | 66 | permission-pending |
| IMDA-AGENTIC-AI-MGF | 2026-05 | 0 | 0 | 0 | 0 | 39 | source-access-pending |
| IMDRF-AER-N43 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-12791 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-12792 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-17903 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-20226 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-21221 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-22989 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-23053 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-23894 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24027 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24028 | 2020 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24029-1 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24029-2 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24030 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24368 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24372 | 2021 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-24668 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-25058 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-25059 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-38507 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42001 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42005 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42006 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42106 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42112 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-42119-2 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-4213 | 2022 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-1 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-2 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-3 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-4 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-5 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5259-6 | 2026 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5338 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5339 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5392 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-5469 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-6254 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-8183 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-8200 | 2024 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| ISO-IEC-IEEE-24765 | 2017 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-100-1 | 1.0 | 74 | 0 | 15 | 54 | 0 | represented-requirements-reviewed |
| NIST-AI-100-2 | E2025 | 22 | 0 | 4 | 20 | 0 | represented-requirements-reviewed |
| NIST-AI-100-3 | 2023 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-100-4 | 2024 | 19 | 0 | 10 | 14 | 0 | represented-requirements-reviewed |
| NIST-AI-100-5 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-AI-600-1 | 2024 | 224 | 0 | 116 | 92 | 0 | represented-requirements-reviewed |
| NIST-CSF-2-0 | 2.0 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-SP-1270 | 2022 | 14 | 0 | 7 | 3 | 0 | represented-requirements-reviewed |
| NIST-SP-800-218 | 1.1 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| NIST-SP-800-218A | 2024 | 75 | 0 | 41 | 33 | 0 | represented-requirements-reviewed |
| OECD-AI-INCIDENT-REPORTING-2025 | 2025 | 0 | 0 | 0 | 0 | 0 | no-reviewed-canonical-requirements |
| OECD-AI-PRINCIPLES | 2024-05-03 | 37 | 0 | 3 | 7 | 0 | represented-requirements-reviewed |
| SPDX-SPEC | 3.0.1 | 4 | 0 | 1 | 4 | 0 | represented-requirements-reviewed |

Contextual counts are excluded from material support and resolver candidate derivation. A catalogue entry marked reviewed is not evidence that its normative requirements have been extracted/reviewed.

## Outstanding work

- IEEE 7003, 7009, 7014 and 7014.1 require evidence of separate written AI-use permission before substantive relationship admission. Other metadata-only/licensed editions retain their registered access limits.
- IMDA framework-body access remains unresolved; Canada Directive access remains blocked, with no represented canonical requirements.
- EU review is bounded to the 102 source-assured successors from Articles 4a and 9–15. The other 73 requirements remain pending consolidated-source fidelity/atomicity.
- Three C2PA AI-disclosure requirements remain unresolved because normative prose, CDDL and examples conflict.
- Historical citations without a verified atomic canonical endpoint remain pending decomposition/source verification. Their original annotations are preserved; current annotations explicitly state the hold.
- No genuinely new class or material boundary change is proposed. No-mapping institutional, policy, social-outcome and operational provisions are recorded without forcing them into a class.

New relationships should trigger only the dependent occurrence external-requirement backfill. Existing clause/taxonomy adjudication should be reopened only for a substantive contradiction.
