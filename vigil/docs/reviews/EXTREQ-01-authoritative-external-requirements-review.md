# EXTREQ-01 — Authoritative External AI-Governance Requirements Corpus Review

**Review date:** 2026-08-15

**Working branch:** `agent/instrumental-coercive-influence-capability-revalidation`

**Human governance role:** Dr Michelle Vivian O’Rourke — contract approver

**Substantive human review:** not established

**Human source verification:** not established

**Scope:** VIGIL Layer 0 source identity/lifecycle and Layer 1 external requirement reference data only. No Caelestis coverage, conformance or repair assessment was performed.

## 1. Repository preflight and identifier reconciliation

The handoff heads were verified before repository changes:

| Ref | Verified head |
| --- | --- |
| Working branch | `cffc463bf582146a95c4a89137dba2af389919ee` |
| Canonical `main` | `e0afc3f38c64ebe1318efb4e2c6008bfe014cafc` |

The branch was two commits ahead of and one commit behind `main`. Commit and record inspection confirmed that both lines of development claimed `VIGIL-2026-PROP-0030` for substantively different proposals. Repository-wide searches confirmed that `VIGIL-2026-PROP-0031` was unclaimed at the point of reconciliation.

The branch-local capability-transition proposal was mechanically renumbered to `VIGIL-2026-PROP-0031`. Its record identity, filename and review identifiers were updated without changing its substantive proposal. Canonical `main` retained `VIGIL-2026-PROP-0030` for typed intentional non-response and abstention-state governance. Generated VIGIL indexes were rebuilt.

The renumbering was committed as `504e9fb` (`Resolve PROP-0030 identifier collision`). Canonical `main` was then merged into the working branch by merge commit `f2e0b40`; divergent history was not reset, rebased, overwritten or silently reconciled. Generated-index conflicts were resolved by deterministic regeneration from the preserved record sources.

The pre-existing `VIGIL-2026-FM-0058` and renumbered capability-transition proposal were retained. Neither was implemented into Caelestis.

## 2. Layer 0 ledger state and correction

The existing `vigil/external_sources/` ledger remains the authority for source identity, version, publisher, lifecycle, official locator, fingerprint and coarse alignment workflow state. EXTREQ-01 does not replace or overload it.

The starting ledger contained 71 source versions. Review found that the EU AI Act entry represented only the original 12 July 2024 text while EUR-Lex identified a current consolidated version dated 27 July 2026. The original source version was preserved historically and the current consolidation was added as a second version under the same stable VIGIL source identity. The Layer 0 baseline now contains 72 source versions.

The ledger’s `alignment_state` remains a coarse source-level workflow status. Requirement extraction status is represented separately in Layer 1 so that source review, requirement decomposition and later internal alignment cannot be conflated.

## 3. Baseline scope decisions

Every registered source version has an explicit entry in `source-scope.json`. Scope classification is analytical and does not change source lifecycle state or withdraw historical ledger records.

| Source role | Source versions | Treatment |
| --- | ---: | --- |
| `primary-ai-governance` | 55 | Eligible for requirement decomposition, subject to source access. |
| `supporting-external-authority` | 12 | Retained for bounded support; not expanded into a general-law corpus. |
| `context-or-discovery` | 5 | Retained for terminology, discovery or programme context; no first-class requirement decomposition. |
| `excluded-from-current-scope` | 0 | Supported by the schema but not required for a current ledger entry. |

General instruments including the GDPR, NIS2, Digital Services Act, Data Act, Data Governance Act and Cyber Resilience Act are supporting authorities rather than comprehensive first-class corpora. NIST CSF 2.0 and the general SSDF are treated similarly. Terminology and standards-planning publications are context/discovery sources. AI-specific ISO, IEEE, NIST, IMDA, SPDX, CycloneDX and EU instruments remain primary where their principal subject warrants that role.

## 4. Source access and copyright controls

| Access state | Source versions |
| --- | ---: |
| `direct-public-primary` | 20 |
| `official-public-extract` | 1 |
| `official-metadata-only` | 51 |

No record was created from a title, abstract or third-party summary as though normative text had been reviewed. ISO and IEEE publications without lawfully available full text remain metadata-only. Forty-four primary source versions are therefore `blocked-access`, with explicit maintainer actions to obtain lawful licensed access without committing copyrighted text to the repository.

The IMDA agentic-AI framework was reviewable only through official public factsheet/extract material in the available environment. Its six requirement records are provisional and the source remains partial. The current EU AI Act text was directly accessible, but full legal decomposition remains incomplete and requires specialist continuation.

The generated `SOURCE-ACCESS-LIMITATIONS.md` is the maintainer access list. It distinguishes blocked normative text from partial public-primary extraction and records inaccessible material and next action per source.

## 5. Layer 1 schema design

External requirements are maintained reference data, not new OBS/FM/PROP/PATCH/LEARN records. Schema v1 preserves:

- registered source and version identity;
- authoritative locator, clause/control and parent hierarchy;
- source role, lifecycle and access basis;
- posture: mandatory, recommended, optional, definitional, informative, example or conformity/evidence expectation;
- source-specific actors and governed objects;
- lifecycle applicability;
- analytical governance and evidence expectations;
- applicability conditions, exceptions and qualifications;
- a small controlled governance-concept tag set for later querying;
- interpretation state, direct provenance, source fingerprint and limitations;
- non-equivalent cross-source relationships where a reviewer explicitly establishes them.

An EXTREQ identity is deterministically derived from:

`vigil_source_id | source_version | clause_or_control | identity_key`

The human-readable summary is deliberately outside the identity seed, so editorial improvement does not churn identity while the represented source requirement is unchanged. Version and clause remain identity inputs so requirements cannot silently migrate between authoritative versions or provenance locations.

No Caelestis instrument, code, failure class, coverage, PATCH, gap or alignment field is permitted by the schema or validator.

## 6. Heterogeneous pilot findings

The pilot tested the schema against materially different governance forms:

| Pilot source | Result |
| --- | --- |
| EU AI Act, current consolidated text | Binding actor duties, applicability, exceptions, conformity and evidence expectations are representable. Full Act remains partial pending specialist legal decomposition. |
| NIST AI RMF 1.0 | All 71 voluntary Core subcategories are represented without converting recommendations into legal obligations. |
| NIST Generative AI Profile | Risk categories and suggested actions remain distinct; the broad profile remains partial. |
| IMDA agentic-AI framework | Agent authority, oversight and monitoring concepts are representable, while official-extract access is visibly provisional. |
| SPDX AI Profile 3.0.1 | Exactly-one conformance relationships, mandatory package properties and optional AI-governance properties retain different postures. |
| CycloneDX 1.7 ML-BOM/model card | `SHOULD`, `MUST NOT`, conditional uniqueness and informative field vocabulary retain their distinct meanings. |
| ISO/IEC 42001:2023 | The schema represents a primary source blocked by controlled/copyrighted access without inventing requirements from metadata. |

The pilot did not require an internal ontology or Caelestis-specific field. Actor arrays, governed-object arrays, lifecycle tags, evidence arrays and qualification arrays were sufficient for the reviewed forms.

## 7. Extraction results

The corpus contains 159 requirement records:

| Source | Version | Extraction | Records | Reviewed | Provisional/unresolved |
| --- | --- | --- | ---: | ---: | ---: |
| NIST AI RMF | 1.0 | complete | 71 | 71 | 0 |
| Regulation (EU) 2024/1689 | consolidated 2026-07-27 | partial | 35 | 35 | 0 |
| NIST Generative AI Profile | 2024 | partial | 22 | 22 | 0 |
| NIST Adversarial Machine Learning Taxonomy | E2025 | partial | 5 | 5 | 0 |
| NIST Synthetic Content Transparency Methods | 2024 | partial | 4 | 4 | 0 |
| NIST SP 1270 | 2022 | partial | 3 | 3 | 0 |
| NIST SP 800-218A | 2024 | partial | 5 | 5 | 0 |
| IMDA Model AI Governance Framework for Agentic AI | 2026-05 | partial | 6 | 0 | 6 |
| SPDX AI Profile | 3.0.1 | complete | 4 | 4 | 0 |
| CycloneDX ML-BOM/model card | 1.7 | complete | 4 | 4 | 0 |

Across all 72 registered versions, extraction states are:

| Extraction state | Source versions |
| --- | ---: |
| `complete` | 3 |
| `partial` | 7 |
| `blocked-access` | 44 |
| `supporting-only` | 12 |
| `context-only` | 5 |
| `superseded-version` | 1 |

“Complete” is bounded to governance-meaningful decomposition of the identified source structure; it does not mean that every informative sentence became a requirement. The EU Act and broad NIST guidance remain partial even though substantial records are present.

## 8. Deterministic outputs and validation coverage

Maintained truth now consists of the Layer 0 ledger, Layer 1 scope decisions and the source/version shards under `external_requirements/requirements/`. The manager deterministically builds the backward-compatible `requirements.json` aggregate and:

- `requirements-index.json`;
- `completeness-report.json`;
- `EXTERNAL-AI-GOVERNANCE-REQUIREMENTS.md`;
- `SOURCE-ACCESS-LIMITATIONS.md`.

Validation fails for unknown source/version references, metadata or fingerprint drift, non-deterministic or duplicate IDs, absent clause provenance, invalid source/access/extraction combinations, direct-review claims unsupported by access, requirements on superseded versions, primary-source omissions without explicit incomplete/access state, stale generated outputs, invalid controlled terms, unresolved related-requirement identifiers and forbidden internal-alignment fields.

Eleven focused tests exercise deterministic identity, generated-output freshness, duplicate IDs, unknown versions, missing clauses, metadata-only and official-extract review claims, omitted complete sources, superseded versions, forbidden Caelestis mapping fields and role/extraction conflicts. The GitHub workflow now rebuilds and verifies both source-ledger and requirement projections.

The full existing VIGIL build, routing, record validation, lifecycle validation, CAM boundary and provenance checks were run after identifier reconciliation and again after EXTREQ-01 implementation. The only record-validator warnings are the pre-existing missing contextual observation links from `OBS-0021` and `OBS-0022` to absent `OBS-0008`; no EXTREQ-01 validation failed.

## 9. Incomplete sources and decision gates

Maintainer or specialist continuation is required for:

1. lawful access to 44 primary ISO/IEEE source versions currently limited to official metadata;
2. full article-level legal review of the 27 July 2026 EU AI Act consolidation, including the effects of Regulation (EU) 2026/1744;
3. stable access to and full review of the May 2026 IMDA agentic-AI framework;
4. completion of the broad NIST Generative AI Profile, adversarial-ML, synthetic-content, bias and secure-AI-development publications beyond the bounded records included here.

The repository does not represent these access or interpretation gaps as completed work. No requirement was synthesized into a cross-source consensus, and no similar requirements were collapsed across authorities.

## 10. Stop boundary

EXTREQ-01 stops at the external baseline. This review does not state whether Caelestis represents, satisfies or conflicts with any requirement; does not create Caelestis codes or releases; and does not create PATCH, FM or LEARN records from the external corpus. The next work thread may use this substrate to perform that separate assessment after the planned Caelestis refactor and internal repair.
