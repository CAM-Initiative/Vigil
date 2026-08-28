# External Requirement Source-Fidelity Status

Review date: 2026-08-28

The external-requirements corpus contains 854 canonical EXTREQ records across 81 registered source versions. Historical `extraction_status` remains preserved in `source-scope.json`; it is not, by itself, a claim of clause-level semantic fidelity.

## Effective completion rule

A first-class source is effectively complete for clause-level use only when its historical extraction state is `complete` and `source-fidelity.json` marks that exact source/version `assured`. A historically complete source without explicit fidelity assurance is conservatively treated as fidelity-unassured and effectively partial.

## Explicitly audited sources

| Source | Historical extraction | Fidelity | Effective status | Finding |
|---|---|---|---|---|
| EU AI Act consolidated 27 July 2026 | partial | requires-reextraction | partial | Article-level records compress independently assessable legal propositions; staged stress-test packages remain separate. |
| NIST AI RMF 1.0 | complete | assured | complete | Source-native Core subcategories retain defensible outcome-level granularity. |
| NIST AI 600-1 Generative AI Profile | complete | assured | complete | Sixty suggested actions retain identity with complete constituent semantics and source-supported metadata. |
| CycloneDX 1.7 ML-BOM | complete | assured | complete | Five propositions represent the distinct MUST uniqueness and SHOULD reserved-prefix modalities. |
| IMDA Agentic AI MGF 1.5 | complete | assured | complete | Thirty-nine records resolve all 20 queued fidelity defects with deterministic subsection decomposition. |
| NIST SP 800-218A | complete | assured | complete | Seventy-five source-native recommendation and consideration propositions are represented separately. |

## Other historically complete sources

Until individually re-audited under `SOURCE-FIDELITY-METHODOLOGY.md`, every other source carrying historical `extraction_status: complete` remains fidelity-unassured and effectively partial. Existing records remain useful and source-traceable, but absence of an EXTREQ record must not be treated as proof that an unaudited source contains no corresponding obligation.

## Next reprocessing order

The next public-primary tranche is AAM SDOS Runtime Governance 1.10, followed by NIST AI 100-2 E2025, NIST AI 100-4 (2024), NIST SP 1270 (2022), and SPDX AI Profile 3.0.1. Licensed IEEE sources should be reviewed only from the lawfully accessible primary texts already recorded by the repository. Blocked-access sources remain blocked and are not inferred from metadata.
