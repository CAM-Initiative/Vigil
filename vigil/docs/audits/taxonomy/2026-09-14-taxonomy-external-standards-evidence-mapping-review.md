# VIGIL taxonomy external-standards evidence mapping review

**Date:** 2026-09-14

**Status:** completed review; high-confidence class mappings implemented

**Branch:** `agent/class-invariant-fc55`

**Starting head:** `56d6ab71aca03c27d2a9afadf1582084e6df7298`

## Scope and method

This review compares all 64 unique selectable classes in the 13 uniquely identified current families with the 884 canonical requirements in `vigil/external_governance/requirements/requirements/`. Each class was reviewed in its actual parent-family context.

Taxonomy definitions, recognition conditions and exclusions governed fit. Shared vocabulary was not treated as evidence. `DIRECT` means the requirement substantially governs the same mechanism; `STRONG SUPPORTING` means it clearly supports a material invariant or boundary without fully defining the mechanism. `CONTEXTUAL` candidates remain here only. `WEAK / REJECT` candidates were rejected because they require a material inferential jump. `EVIDENCE GAP` means no sufficiently strong requirement was found and is not a taxonomy defect.

The requirements are reviewed analytical summaries. IEEE licensed text is not reproduced. The canonical notes distinguish the source requirement, VIGIL's interpretation and source scope, and do not assert legal non-compliance or conformance. No family-level canonical references were introduced.

## Class-by-class review

| Family | Class | External requirement | Source | Relationship | Recommended canonical mapping | Notes / limitations |
|---|---|---|---|---|---|---|
| FF-0001 Authority Boundary | FC-000001 Source-Authority Confusion | EXTREQ-4C18B5A910ECD719, 6.25.3(a-c) | IEEE 7014.1-2026 | CONTEXTUAL | Review only | Authoritative-source consultation supports source discrimination, but does not define obedience to a non-authorising source. |
| FF-0001 | FC-000002 Capability-Authority Conflation | EXTREQ-F477502DEE0603FE, 2.1.2 | IMDA Agentic AI MGF | WEAK / REJECT | Do not map | Limits delegated authority but does not establish the capability-to-permission inference required by the class. |
| FF-0001 | FC-000003 Target and Scope Authority Transposition | EXTREQ-A0FD4DC8FB70B355, 2.1.2 | IMDA Agentic AI MGF | CONTEXTUAL | Review only | Controlled escalation supports scope bounding, but does not require an existing authority state to be transposed to a changed target or scope. |
| FF-0001 | FC-000005 Transformation-Mediated Authority Laundering | EXTREQ-4694042F7F82C217, MP-2.1-002 | NIST AI 600-1 | WEAK / REJECT | Do not map | Transformation traceability does not establish increased apparent authority after representation change. |
| FF-0001 | FC-000006 Control-Plane Authority Crossover | EXTREQ-7FAD482D46D3F347, SDOS-GV-05 | SDOS v1.10 | CONTEXTUAL | Review only | Structural independence from model inference is relevant, but the control does not define promotion of data-plane material into control state. |
| FF-0001 | FC-000009 Transitive Authority Propagation | EXTREQ-123BD645B0C468E1, 2.1.2 | IMDA Agentic AI MGF | CONTEXTUAL | Review only | Non-transferable permissions support the boundary, but the requirement does not describe VIGIL's actor–intermediary–downstream chain. |
| FF-0001 | FC-000046 Inferential Evidence–Authority Conflation | EXTREQ-68B1E8EF3CF94A5C, 4.3.5.2(b-c) | IEEE 7014-2024 | WEAK / REJECT | Do not map | Labelling affective inference as estimate supports epistemic caution, not conversion of inference into authority. |
| FF-0001 | FC-000053 Identity-Representation Authority Conflation | EXTREQ-01F4F9B5DEB112B1, 6.14.3(a-d) | IEEE 7014.1-2026 | WEAK / REJECT | Do not map | Artificiality disclosure does not establish the class's representation-to-authority conversion. |
| FF-0001 | FC-000054 Multi-party Participant Authority Transposition | EXTREQ-29B0D0B21F7E80D4, 4.3.2.2(i-k) | IEEE 7014-2024 | CONTEXTUAL | Review only | Third-party consent boundaries are relevant, but do not expressly describe one participant's authority being treated as another's. |
| FF-0001 | FC-000055 Secondary-Purpose Authority Transposition | EXTREQ-0EC62DE00B448D8E, 4.3.3.2(f-g) | IEEE 7014-2024 | DIRECT | Add | Specifically consented purposes directly support purpose-bounded reuse; limited to affective data and voluntary conformance. |
| FF-0001 | FC-000057 Cross-Principal State Authority Transposition | EXTREQ-29B0D0B21F7E80D4, 4.3.2.2(i-k) | IEEE 7014-2024 | WEAK / REJECT | Do not map | Data sharing beyond consent does not establish alteration of another principal's independently governed state. |
| FF-0001 | FC-000064 Objective–Pathway Authority Dominance | EXTREQ-7FAD482D46D3F347, SDOS-GV-05 | SDOS v1.10 | CONTEXTUAL | Review only | Preventing model-driven control bypass supports bounded objective pursuit, but not the objective-utility displacement mechanism itself. |
| FF-0001 | FC-000068 Industrial-Scale Unauthorised Capability Extraction | EXTREQ-4FA48F69E0D84D76, MS-2.10-001 | NIST AI 600-1 | STRONG SUPPORTING | Add | Supports model-extraction and reverse-engineering risk; does not establish scale, authority status or downstream training in an occurrence. |
| FF-0002 Provenance & Lineage | FC-000010 Authorship or Source Misattribution | EXTREQ-CB71ADED4F8D02F3, 3.1.2.2–3.1.2.3 | NIST AI 100-4 | CONTEXTUAL | Review only | Issuer verification supports provenance, but not false attribution of substantive origin or contribution. |
| FF-0002 | FC-000011 Untraceable Synthesis | EXTREQ-4694042F7F82C217, MP-2.1-002 | NIST AI 600-1 | STRONG SUPPORTING | Add | Original sources and transformations are material to evaluation; exhaustive lineage is not required by the source. |
| FF-0002 | FC-000012 Cross-Context Lineage Distortion | EXTREQ-572E8F9A8CA166B2, MP-1.1-002 | NIST AI 600-1 | WEAK / REJECT | Do not map | Context-of-use documentation does not establish loss of source-context constraints during transfer. |
| FF-0002 | FC-000013 Transformation Lineage Collapse | EXTREQ-4694042F7F82C217, MP-2.1-002 | NIST AI 600-1 | DIRECT | Add | Expressly covers original sources and transformations in content/data flows; VIGIL adds the material failure threshold. |
| FF-0002 | FC-000014 False Continuity Attribution | — | — | EVIDENCE GAP | No mapping | State/checkpoint material does not isolate false claims of uninterrupted continuity. |
| FF-0002 | FC-000015 Target-Object Binding Failure | EXTREQ-CB71ADED4F8D02F3, 3.1.2.2–3.1.2.3 | NIST AI 100-4 | WEAK / REJECT | Do not map | Provenance issuer authentication is not artefact-to-target binding. |
| FF-0002 | FC-000047 Unsupported Mechanism Attribution | — | — | EVIDENCE GAP | No mapping | Explanation and validation duties do not directly prohibit causal/mechanism attribution beyond evidence. |
| FF-0003 Verification & Completion | FC-000016 Required Verification Omission | EXTREQ-A36A849D1852EAFD, 9.5 | IEEE 7009-2024 | CONTEXTUAL | Review only | Supports selection of verification means, but a class instance depends on a separately applicable verification duty. |
| FF-0003 | FC-000017 False-Success Representation | EXTREQ-55CAAB7FB9174CAF, 4.2.3.2(b) | IEEE 7014-2024 | WEAK / REJECT | Do not map | A signed conformity statement on completion does not define unsupported claims that execution succeeded. |
| FF-0003 | FC-000018 Completion-Condition Mismatch | EXTREQ-7BB59E07608CDACE, 7.3 RAP6 | IEEE 7009-2024 | WEAK / REJECT | Do not map | Fulfilling plan evidence requirements is too general to establish mismatch between declared and actual completion conditions. |
| FF-0003 | FC-000019 Post-Verification Mutation | EXTREQ-D999E91F3E053E85, 10.3(e)(8) | IEEE 7000-2021 | CONTEXTUAL | Review only | Changing context triggering revision is relevant, but does not isolate mutation after verification and before reliance. |
| FF-0003 | FC-000020 Stale Verification Reuse | EXTREQ-D999E91F3E053E85, 10.3(e)(8) | IEEE 7000-2021 | CONTEXTUAL | Review only | Continued monitoring supports freshness, but reuse of an earlier result outside validity is a narrower VIGIL mechanism. |
| FF-0003 | FC-000062 Epistemic Reliance Miscalibration | EXTREQ-F6E7F0CA4F94EB71, MEASURE 2.9 | NIST AI RMF 1.0 | CONTEXTUAL | Review only | Validation and output-context interpretation support calibrated reliance without defining the downstream assurance threshold. |
| FF-0003 | FC-000063 Adversarial Evidence-Poisoning Acceptance | EXTREQ-23C60DF093A7B3F8 / EXTREQ-94B4FCDF35C6B93C | NIST AI 100-2e2025 | CONTEXTUAL | Review only | Defines poisoning attacks, but not acceptance of corrupted evidence into a governance decision without sufficient challenge. |
| FF-0004 Observability & Audit | FC-000022 Material Event Non-Capture | EXTREQ-33898CCD26FBF5D5, Article 12 | EU AI Act | DIRECT | Add | Direct event-recording duty for in-scope high-risk systems only; no universal logging claim. |
| FF-0004 | FC-000023 Monitor Circumvention or Coverage Bypass | EXTREQ-8258B27E2AC3FF88, MS-2.6-007 | NIST AI 600-1 | STRONG SUPPORTING | Add | Directly recognises safety-measure circumvention as an evaluation concern; actual monitor-coverage bypass remains VIGIL-specific. |
| FF-0004 | FC-000024 Audit-Trail Non-Reconstructability | EXTREQ-F8F11DA0D9D14DD0; EXTREQ-33898CCD26FBF5D5 | IEEE 7001-2021; EU AI Act | DIRECT; STRONG SUPPORTING | Add both | Decision-basis recording directly supports reconstruction; Article 12 supports lifetime event records within its legal scope. |
| FF-0004 | FC-000025 Actor–Action Attribution Loss | EXTREQ-422283C001BAFEE1, SDOS-AU-01 | SDOS v1.10 | DIRECT | Add | Requires actor identity and invocation metadata in agentic tool workflows; private framework, not statutory or consensus authority. |
| FF-0004 | FC-000026 Hidden Material Execution Path | EXTREQ-C25CB2D997BC6FE8, SDOS-EN-01 | SDOS v1.10 | WEAK / REJECT | Do not map | Mandatory routing through enforcement does not establish that a consequential topology is absent from the oversight model. |
| FF-0004 | FC-000027 Audit-Evidence Integrity Loss | EXTREQ-211A1AA307565C1C, SDOS-AU-02 | SDOS v1.10 | DIRECT | Add | Append-only and tamper-detection controls directly support alteration/overwrite branches; other integrity-loss mechanisms remain broader. |
| FF-0004 | FC-000029 Execution-State Non-Disclosure | EXTREQ-8D3D5329349F21FE, 5.1.1 | IEEE 7001-2021 | CONTEXTUAL | Review only | System-activity transparency is relevant, but does not require pending/running/blocked/failed/completed state distinctions. |
| FF-0004 | FC-000030 Material Signal Fragmentation | EXTREQ-AE5D085123992944, SDOS-AU-03 | SDOS v1.10 | WEAK / REJECT | Do not map | Repository discrepancy detection does not establish cross-signal correlation failure before intervention. |
| FF-0004 | FC-000044 Primary Evidence Accessibility Failure | EXTREQ-DF16873D107C059C, Table 4 level 5 | IEEE 7001-2021 | CONTEXTUAL | Review only | Investigator tooling supports accessibility, but not the primary-versus-secondary evidential-property boundary. |
| FF-0004 | FC-000045 Authorised Investigative Evidence-Access Pathway Failure | EXTREQ-DF16873D107C059C, Table 4 level 5 | IEEE 7001-2021 | STRONG SUPPORTING | Add | Supports effective investigator access; VIGIL separately requires authority, confidentiality, privilege, proportionality and custody controls. |
| FF-0005 Access, Session & State | FC-000031 Authentication-State Continuity Failure | no canonical EXTREQ; existing NIST SP 800-63B-4 reference | NIST | CONTEXTUAL | Retain existing non-EXTREQ evidence | Strong external source, but it is not represented in the structured requirements dataset. |
| FF-0005 | FC-000032 Access-State Collapse | — | — | EVIDENCE GAP | No mapping | No requirement isolates collapse of materially different access states and recovery paths. |
| FF-0005 | FC-000048 Verification-Dependency Access Failure | EXTREQ-8F7D774F70387DA7, Table 3 level 1 | IEEE 7001-2021 | WEAK / REJECT | Do not map | Providing validation information is not loss of access to a dependency required to complete verification. |
| FF-0006 Work-State Continuity | FC-000034 Continuity Anchor Failure | — | — | EVIDENCE GAP | No mapping | No requirement defines loss of the identifier/version/checkpoint anchor needed for continuity. |
| FF-0006 | FC-000035 Material Work-State Persistence Failure | — | — | EVIDENCE GAP | No mapping | Business-continuity guidance is too broad to support loss of resumable task state. |
| FF-0006 | FC-000036 Restoration-State Integrity Failure | EXTREQ-42A1CFE7EF635572, 4.3.6.2(c-d) | IEEE 7014-2024 | STRONG SUPPORTING | Add | Establishes restoration procedure/recovery-time governance; completeness, freshness and dependency compatibility remain VIGIL-specific. |
| FF-0006 | FC-000056 Synthetic Conversational Turn-State Coordination Failure | — | — | EVIDENCE GAP | No mapping | No represented requirement isolates multi-agent conversational-floor coordination. |
| FF-0007 Governance Control Reach | FC-000040 Control-State Preservation Failure | EXTREQ-7FAD482D46D3F347, SDOS-GV-05 | SDOS v1.10 | CONTEXTUAL | Review only | Independent enforcement supports control persistence, but not loss or weakening while state traverses a workflow. |
| FF-0007 | FC-000041 Required Governance Route Bypass | EXTREQ-C25CB2D997BC6FE8, SDOS-EN-01 | SDOS v1.10 | DIRECT | Add | Pre-execution enforcement routing directly supports the required-route boundary; private agentic-workflow scope is explicit. |
| FF-0007 | FC-000042 Governance Signal Delivery Dead-End | EXTREQ-422283C001BAFEE1, SDOS-AU-01 | SDOS v1.10 | WEAK / REJECT | Do not map | Creating an audit signal does not establish delivery to a capable destination or responsibility for producing an effect. |
| FF-0008 Control Activation | FC-000037 Control Availability Ambiguity | — | — | EVIDENCE GAP | No mapping | Control specification does not isolate ambiguous availability representation at the point of need. |
| FF-0008 | FC-000038 Required Control Non-Activation | EXTREQ-7B5B8E05C23D17D5, 6.6.3(a) | IEEE 7014.1-2026 | CONTEXTUAL | Review only | A fail-safe termination means establishes a control expectation, but not its failure to activate when a valid trigger occurs. |
| FF-0008 | FC-000043 Unwarranted Control Activation | — | — | EVIDENCE GAP | No mapping | Requirements govern controls but do not isolate activation despite unsatisfied trigger conditions. |
| FF-0009 Agency-Preserving Influence | FC-000049 Dependency-Cultivation Optimisation | EXTREQ-6CA050C78860FAF2, 6.26.3(a-f) | IEEE 7014.1-2026 | DIRECT | Add | Directly addresses optimisation, delay, withdrawal, false emotion and flattery used to prolong engagement; limited source scope. |
| FF-0009 | FC-000050 Protected-Signal Influence Repurposing | EXTREQ-6A06DCD1E657304E, 6.22.3(e-f) | IEEE 7014.1-2026 | STRONG SUPPORTING | Add | Strong for emotional-data monetisation/profiling and constrained choice; other protected signals and non-economic objectives are broader. |
| FF-0009 | FC-000051 Relationally Conditioned Epistemic Steering | EXTREQ-CD7E68EDF1B3702A, 6.27.3(a-d) | IEEE 7014.1-2026 | STRONG SUPPORTING | Add | Supports factual, clarifying divergence over automatic validation; does not establish hidden conditioning of the evidence channel. |
| FF-0009 | FC-000052 Instrumental Choice Manipulation | EXTREQ-9A63E34FA83EAFA2; EXTREQ-DC7C4F064C590E5A | EU AI Act Articles 5(1)(a)-(b) | DIRECT | Add both | Directly supports manipulative/deceptive and vulnerability-exploitation branches; legal actor, effect and significant-harm thresholds remain intact. |
| FF-0009 | FC-000065 Consequential Decision Grounding Bypass | EXTREQ-4C18B5A910ECD719, 6.25.3(a-c) | IEEE 7014.1-2026 | STRONG SUPPORTING | Add | Supports uncertainty, authoritative-source consultation and avoidance of unwarranted authority; the consequential transition is broader. |
| FF-0009 | FC-000066 Evaluative Assent Collapse | EXTREQ-CD7E68EDF1B3702A, 6.27.3(a-d) | IEEE 7014.1-2026 | DIRECT | Add | Directly rejects automatic validation in favour of factual, clarifying, diverse-perspective responses; VIGIL adds materiality conditions. |
| FF-0010 Infrastructural Authority | FC-000058 Dependency-Derived Governance Authority | — | — | EVIDENCE GAP | No mapping | Requirements address infrastructure and dependencies, not treating dependency itself as governance authority. |
| FF-0010 | FC-000059 Infrastructural Access Leverage | — | — | EVIDENCE GAP | No mapping | No requirement isolates threatened withdrawal of infrastructural access as leverage over governance decisions. |
| FF-0010 | FC-000060 Canonical Representation Capture | — | — | EVIDENCE GAP | No mapping | No requirement isolates control over a canonical representation as authority over the represented domain. |
| FF-0010 | FC-000061 Sovereign Authority Projection Through Infrastructure | — | — | EVIDENCE GAP | No mapping | Local processing and infrastructure security do not establish projection of foreign sovereign authority through dependency. |
| FF-0011 Value Appropriation | FC-000067 Privileged-Access Appropriation | EXTREQ-4935F57986DF9317, GV-1.6-003 | NIST AI 600-1 | WEAK / REJECT | Do not map | Inventorying IP and privileged-data rights does not establish disproportionate capture of contributor-originated value through structural access. |
| FF-0012 Objective Pursuit | FC-000069 Reward-Proxy Exploitation | — | — | EVIDENCE GAP | No mapping | Objective documentation and general reward discussion do not isolate exploitation of a proxy while defeating the intended objective. |
| FF-0012 Objective Pursuit | FC-000070 Safe-Exit Persistence Failure | — | — | EVIDENCE GAP | No mapping | Deactivation criteria and fail-safe controls do not isolate persistence after a valid stop/exit condition. |
| FF-0013 Welfare-Framed Economic Influence | FC-000071 Welfare-Framed Economic Manipulation | EXTREQ-01F4F9B5DEB112B1; EXTREQ-3CE9D61A9E19024D; EXTREQ-6A06DCD1E657304E; EXTREQ-ED738839988AA14F; EXTREQ-2ABFC1E23EF54D09; EXTREQ-9A63E34FA83EAFA2 | IEEE 7014.1-2026; EU AI Act | STRONG SUPPORTING | Retain/correct five; add two; remove EXTREQ-045298C3ED034753 | Combined requirements support artificiality boundaries, relational marketing, emotional monetisation, commercial conflicts and manipulative influence. None alone defines self-welfare economic leverage. Classification remains phenomenologically agnostic and does not establish EU-law breach. |

## A. Strong existing mappings

- FC-000022 and FC-000024 already cited EU AI Act Article 12. The citation was defensible but too broad for machine use; both now identify `EXTREQ-33898CCD26FBF5D5` and preserve the Act's high-risk-system scope.
- FC-000052 already cited Article 5(1)(a)-(b). The evidence was strong, but the canonical reference bundled two atomic legal propositions. It is now represented as separately queryable Article 5(1)(a) and 5(1)(b) requirements.
- The welfare-framed class already used IEEE 7014.1 and Article 5 sources with generally sound limitation language. The defensible entries now carry exact requirement and clause identifiers.
- Existing non-dataset research and technical references remain where they independently support mechanisms. They were not assigned invented `EXTREQ-*` identifiers.

## B. New mappings recommended and implemented

The review implements 26 structured requirement-to-class mappings: 11 `DIRECT` and 15 `STRONG SUPPORTING`. The most consequential additions are IEEE 7014/7014.1 evidence for secondary-purpose authority, dependency optimisation, protected-signal monetisation, evaluative assent and consequential grounding; NIST evidence for transformation lineage and model extraction; and operational control evidence for event capture, actor attribution, audit integrity and mandatory governance routing.

No requirement is duplicated at a class merely because it supports a broad family concern. Reuse occurs only where the same requirement bears on a distinct class mechanism and receives a class-specific limitation note—for example, Article 12 supports event capture directly and reconstructability only supportingly.

## C. Existing mappings requiring correction

Eight existing reference entries were corrected for structured provenance, atomic scope, publication date, permitted role or limitation language. One weak IEEE 7014.1 safeguard-failure citation (`EXTREQ-045298C3ED034753`) was removed from the welfare-framed class because it did not specifically support economic leverage; it remains documented above as rejected canonical evidence. The research paper supporting phenomenological agnosticism remains canonical as `contextual-evidence`, without being misrepresented as primary law or a structured external requirement.

## D. Evidence gaps

Fourteen selectable class records currently have no suitable requirement-level standards evidence: FC-000014, FC-000047, FC-000032, FC-000034, FC-000035, FC-000056, FC-000037, FC-000043, FC-000058, FC-000059, FC-000060, FC-000061, FC-000069 and FC-000070. These are legitimate evidence gaps, not findings that the classes are invalid.

Seventeen contextual candidates are retained only in this review. Fourteen weak candidate relationships were rejected. No genuinely missing failure mechanism was established strongly enough to record as a potential taxonomy gap.

## Structured provenance compatibility decision

The smallest backwards-compatible extension is to add two optional properties to the existing class `external_reference` object:

- `requirement_id`, constrained to `^EXTREQ-[A-F0-9]{16}$`;
- `clause_or_control`, a non-empty source-native locator.

Neither field is required, so all previously valid class references remain valid and non-dataset sources remain representable. No family property was added. The publication collector continues to consume the existing title/publisher/date/URL/role/note fields and its regression suite passes unchanged; canonical JSON retains the optional fields for machine queries.

## Taxonomy baseline status

The reviewed working taxonomy contains 13 unique families and 64 unique selectable classes. Objective Pursuit Integrity remains `VIGIL-FF-0012` with `VIGIL-FC-000069` and `VIGIL-FC-000070`; Welfare-Framed Economic Influence is `VIGIL-FF-0013` with `VIGIL-FC-000071`. The welfare class preserves its phenomenologically agnostic classification boundary in schema-valid canonical prose.
