# EXTREQ-02 — External AI-Governance Requirements Corpus Completion and Assurance

## Review authority and boundary

- Review date: 2026-08-15
- Reviewer: Dr Michelle Vivian O’Rourke
- Working branch: `agent/instrumental-coercive-influence-capability-revalidation`
- Starting branch head: `c8b0c31ea86fa07c4a5e74472bfe73002c889f73`
- Canonical `main` at preflight: `e0afc3f38c64ebe1318efb4e2c6008bfe014cafc`
- Starting divergence: 31 commits ahead and 0 commits behind `main`

This package completes and assures the maintained external-reference substrate. It does not assess Caelestis coverage or conformance, create internal canonical codes, create PATCH/FM/PROP/LEARN records, or change Caelestis.

## Preflight and repository state

The remote branch and `main` heads matched the handoff. No commits had been added to the remote working branch after `c8b0c31`. The branch was fast-forwarded locally to that exact remote head without reset, rebase, squash or history reconciliation. The 25 commits between the initially available local checkout and the remote head were inspected; they comprise the recently completed FM-schema and system-context repair work plus the final generated registry rebuild.

The most recent workflow-bearing commit had a successful `VIGIL records` GitHub Actions run. The final generated-index-only commit carried no separate check. Before EXTREQ-02 changes, the complete repository validation surface passed: external-source baseline and ledger checks, external-requirement build/validation, 84 unit tests, routing/build/enrichment, record validation, observatory boundary validation, interpretive-provenance validation and lifecycle/corpus-coverage validation. The only warnings were the pre-existing `OBS-0021` and `OBS-0022` references to absent `OBS-0008` context.

No FM-schema, system-context or VIGIL record was edited by EXTREQ-02.

## Starting corpus

The starting baseline contained 72 registered source versions and 159 EXTREQ records. Source extraction state was:

| State | Source versions |
| --- | ---: |
| complete | 3 |
| partial | 7 |
| blocked-access | 44 |
| supporting-only | 12 |
| context-only | 5 |
| superseded-version | 1 |

All 159 starting records were included in the quality audit. Of their deterministic identities, 116 remain represented. Forty-three coarse or pilot identities were retired and replaced because the represented external requirement was split or materially re-identified; their identifiers were not silently reused. Twelve retained NIST AI 600-1 risk-category identities were corrected from `recommended-practice` to `definitional`. Review dates and provenance-review labels were refreshed across retained records without changing their identity seeds.

## Schema assurance and changes

The existing schema was retained and advanced from version 1.0 to 1.1. Deterministic identity remains:

`vigil_source_id | source_version | clause_or_control | identity_key`

Five requirement fields were added only after direct source analysis showed information loss in the existing representation:

| Field | Source-demonstrated reason |
| --- | --- |
| `expectation_type` | The EU Act contains prohibitions, permissions/qualifications and rights that cannot be faithfully distinguished by posture alone. |
| `timing_or_frequency` | EU statutory timing and NIST continuous, periodic, pre-release and change-triggered controls must not be buried in a prose summary. |
| `required_artefacts` | EU declarations, documentation and registers, and NIST policies, reports and inventories are specified artefacts distinct from the underlying governance duty. |
| `verification_method` | NIST sources expressly identify adversarial testing, red teaming, audits, scanning, hashes and signatures as methods rather than generic evidence. |
| `source_defined_tags` | NIST AI 600-1 assigns GAI risk categories to actions and SP 800-218A assigns priorities; those source-native classifications should be preserved without expanding VIGIL’s governance-concept vocabulary. |

Source scope gained `known_unreviewed_sections`, `next_action`, `alignment_priority` and `alignment_priority_rationale`. These are source-level assurance and access-planning fields. They do not contain an internal corpus mapping or alignment result.

No Caelestis-specific field was introduced. The bounded governance-concept vocabulary required no extension.

## Requirement/evidence separation

The completion pass maintains separate representations for:

- the action, control, prohibition, permission, process or outcome in `governance_expectation`;
- evidence expressly required or directly contemplated in `evidence_expectation`;
- source-specified schedules or triggers in `timing_or_frequency`;
- named records, policies, reports, declarations or inventories in `required_artefacts`;
- source-specified evaluation or assurance methods in `verification_method`;
- thresholds and triggering conditions in `applicability_conditions`; and
- exceptions and limitations in `exceptions_or_qualifications`.

An empty evidence or verification field means the cited source statement did not expressly establish one at the represented granularity. It does not mean that evidence would be unnecessary in a later alignment assessment.

## Public-primary completion results

### EU AI Act

The authoritative 27 July 2026 consolidated source remains `partial`, with 81 reviewed operator-facing requirements. The review covers prohibited practices, AI literacy, high-risk classification and controls, provider and authorised-representative duties, importer and distributor duties, value-chain responsibility, deployer duties, fundamental-rights impact assessment, conformity, declarations, marking and registration, transparency, GPAI and systemic-risk duties, post-market monitoring, incident reporting and affected-person rights.

Composite pilot records for Articles 5, 16, 22–26, 50, 53 and 55 were replaced with clause- and actor-specific requirements. Actor and system-class applicability is preserved rather than generalized.

The source is not marked complete. Known unreviewed scope remains the specialised sectoral, institutional, market-surveillance, enforcement and penalty architecture. A specialist legal review is required before the operator-focused extraction can be treated as a complete legal corpus, including final assurance of the consolidated effect of Regulation (EU) 2026/1744.

### NIST

| Source | Final status | Records | Bounded completion basis |
| --- | --- | ---: | --- |
| NIST AI RMF 1.0 | complete | 71 | Existing Core subcategory and definition decomposition audited and retained. |
| NIST AI 600-1 Generative AI Profile | complete | 223 | All 211 suggested-action table rows plus 12 source-defined GAI risk-category definitions; AI Actor Tasks and GAI risk tags preserved. |
| NIST AI 100-2 E2025 | complete | 22 | Governance-significant attack taxonomy definitions and mitigation/evaluation guidance systematically reviewed. |
| NIST AI 100-4 | complete | 18 | Provenance, watermarking, detection, labelling, evaluation and harm-reduction sections decomposed. |
| NIST SP 1270 | complete | 14 | Dataset, TEVV, human-factors, governance and lifecycle bias guidance decomposed. |
| NIST SP 800-218A | complete | 74 | All 59 AI-specific recommendations and 15 considerations in the SSDF community-profile table; informative notes were not treated as requirements. |

NIST voluntary framework outcomes and guidance remain `recommended-practice`, `informative-guidance` or `definitional`; they were not converted into binding legal duties. Repeated explanatory material and implementation examples were not duplicated as independent requirements without separate governance meaning.

### IMDA agentic-AI governance

The complete authoritative IMDA framework PDF was found at its official public publisher location, replacing the earlier factsheet-only access basis. Source access is now `direct-public-primary`, extraction is `complete`, and 32 requirements cover use-case suitability, impact and likelihood assessment, residual risk, tool/access/autonomy boundaries, deterministic limits, identity, inventories, least privilege, authorization escalation, authority ceilings, delegation records, internal and value-chain accountability, contracts, human oversight, development controls, pre-deployment testing, continuous monitoring/testing, intervention and recovery, user disclosure and escalation.

IMDA terminology is preserved at the external-source level. No internal agent ontology or Caelestis terminology was added.

## ISO/IEC and IEEE access assurance

Official publisher pages were rechecked for the blocked primary standards. ISO pages provide official identity, lifecycle, abstracts and limited previews while directing users to purchase or licensed access for the standards. IEEE pages provide official identity, status and abstracts and direct users to subscription, purchase or applicable GET-program access. Those materials do not establish the unseen clause-level normative content.

All 44 blocked primary source versions therefore remain `blocked-access` with `official-metadata-only` access. No requirement was inferred from an abstract, contents listing, cross-reference or secondary summary. Maintainers are instructed to provide lawful licensed primary-text access without committing copyrighted standard text.

Blocked-source governance-value priority is generated as:

| Priority | Sources |
| --- | ---: |
| critical alignment source | 8 |
| high-value alignment source | 21 |
| supporting/specialist source | 7 |
| low immediate priority | 8 |

The critical group contains the broad AI management-system, risk-management, impact-assessment, lifecycle, governance, audit/certification and controllability standards. High-value sources address material data-quality, testing, robustness, safety, bias, transparency, explainability and human-impact concerns. Overview, terminology and reference-architecture sources are intentionally lower priority than control-bearing sources. `BLOCKED-SOURCE-PRIORITIES.md` is an access-planning output, not evidence that inaccessible requirements were reviewed.

## Final corpus and completeness

The final maintained corpus contains 543 EXTREQ records across 10 directly reviewed primary source versions:

| Source | Records |
| --- | ---: |
| NIST AI 600-1 | 223 |
| EU AI Act, consolidated 27 July 2026 | 81 |
| NIST SP 800-218A | 74 |
| NIST AI RMF 1.0 | 71 |
| IMDA Model AI Governance Framework for Agentic AI | 32 |
| NIST AI 100-2 E2025 | 22 |
| NIST AI 100-4 | 18 |
| NIST SP 1270 | 14 |
| SPDX AI Profile | 4 |
| CycloneDX ML-BOM | 4 |

There are 427 newly established deterministic identities. Nine source versions are now complete, one is partial, 44 are blocked by access, 12 are supporting-only, five are context-only and one historical version is superseded. All 543 asserted requirements have reviewed analytical interpretations from direct public primary text; there are no provisional requirement records. Incompleteness remains visible at source level for the EU Act and all blocked standards.

## Generated review and planning outputs

- `requirements-index.json`: deterministic machine-readable index;
- `completeness-report.json`: every source/version with role, access, extraction state, counts, unresolved count, known unreviewed sections, next action and priority;
- `EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md`: source/version/clause human catalogue including actor, governed object, expectation, evidence, timing/artefact/verification, applicability, qualification and review/access state;
- `SOURCE-ACCESS-LIMITATIONS.md`: maintainer access list; and
- `BLOCKED-SOURCE-PRIORITIES.md`: governance-value prioritisation of blocked primary standards.

All aggregate outputs are generated from maintained ledger, scope and requirement inputs and are freshness-checked.

## Validator and test assurance

The validator now additionally fails for:

- invalid or missing expectation type;
- a non-mandatory record labelled as a prohibition;
- a mandatory record whose interpretation is still provisional or requires specialist review;
- malformed or duplicate source-defined tag schemes;
- complete sources retaining known unreviewed sections;
- missing source-level next action or priority rationale; and
- stale blocked-source priority output.

Existing protections remain for unknown source/version, version drift, nondeterministic or duplicate identity, access/review conflicts, unresolved relationships, superseded versions, primary-source omission, source-role conflicts and forbidden internal-mapping fields. Tests were expanded from 11 to 17 and cover the new failure classes plus same-clause atomicity, version change and clause-renumbering identity behavior.

Post-implementation assurance passed the complete local CI command surface: source-provenance and PATCH-corpus checks; FM reconciliation; triage, LEARN, lifecycle, pipeline, registry, routing and record tests; record, observatory-boundary, interpretive-provenance and lifecycle/corpus validators; deterministic external-ledger release; EXTREQ build/freshness checks; registry rebuild/enrichment; and PATCH trace verification against a fresh complete Caelestis checkout. The only record-validator warnings remain the pre-existing `OBS-0021` and `OBS-0022` links to absent `OBS-0008` context. The external-governance workflow now includes `BLOCKED-SOURCE-PRIORITIES.md` in both stale-output checks and generated-output staging.

## Remaining maintainer access and interpretation requirements

1. Obtain lawful access to the eight critical blocked standards first, followed by the 21 high-value standards. Do not commit licensed source text.
2. Commission specialist legal assurance of the current EU AI Act consolidation before changing its extraction state to `complete`.
3. Re-run source/version surveillance when any registered authority publishes a revision, corrigendum, superseding edition or new consolidation.

## Stop boundary

EXTREQ-02 stops with an external, source-traceable requirements baseline. It does not state whether any Caelestis instrument represents or satisfies an EXTREQ record and it does not prescribe an internal repair. That is the separate next-stage Caelestis assessment.
