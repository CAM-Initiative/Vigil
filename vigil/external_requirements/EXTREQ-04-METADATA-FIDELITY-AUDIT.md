# EXTREQ-04 — Corpus-Wide Requirement Metadata Fidelity Review

Date: 2026-08-26  
Working branch: `agent/failure-taxonomy-prototype`  
Review basis: direct authoritative primary text; AI-authored substantive review under the repository provenance contract; no human substantive verification claimed.

## Outcome

This package exercised the field-level review contract across the staged EU AI Act slice and the complete represented populations for NIST AI RMF 1.0, CycloneDX 1.7 and NIST AI 600-1.

The generated report now assesses 947 records: 845 canonical records and 102 staged EU AI Act migration candidates. It records 339 metadata-complete records, 608 records still requiring review, 4,797 unresolved field decisions and 61 canonical records queued for substantive re-extraction or constituent enrichment.

Completion is based on explicit review-state resolution, not on field population. No reviewed field was classified `not-applicable` in this package: the reviewed operational propositions were either populated from the source, source-silent for the dimension, or left `review-required` because a known fidelity defect prevents a defensible final decision.

## Primary-source basis

| Source | Authoritative basis used | Reviewed population | Result |
|---|---|---:|---|
| EU AI Act, consolidated 27 July 2026 | EUR-Lex CELEX `02024R1689-20260727`; existing staged Articles 4a and 9–15 packages and source-explicit normalization overlay | 102 staged candidates | 102 metadata-complete; no Article 16+ extraction undertaken |
| NIST AI RMF 1.0 | `https://doi.org/10.6028/NIST.AI.100-1`; downloaded PDF SHA-256 `7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1` | 71 Core subcategories | 71 metadata-complete; source-defined outcome granularity retained |
| CycloneDX 1.7 | Official specification tag `1.7`, commit `4b3f59453366e27c8073fd24e98bf21ef8892c8e` | 4 ML-BOM propositions | 3 metadata-complete; 1 queued for modality-preserving decomposition |
| NIST AI 600-1 | `https://doi.org/10.6028/NIST.AI.600-1`; downloaded PDF SHA-256 `6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a` | 223 represented records, including 211 suggested actions | 163 metadata-complete; 60 queued for constituent enrichment |

## Source findings

### EU AI Act staged slice

The existing deterministic seeder populated 102 staged records from the previously reviewed extraction and normalization overlay. Two successive writes produced the same ledger SHA-256, `bf68510c56d07faa39e872b6a8c0a2f4d7d94845ff50550225d97dd60c96e547`, and the second execution added zero entries. The seeder retains its conflict-intolerant comparison and does not infer `not-applicable` from empty values.

The source/version appears as partially metadata-reviewed in the corpus report because 81 coarse canonical EU records remain unresolved alongside the 102 complete staged candidates. This package did not resume Article 16+ extraction.

### NIST AI RMF 1.0

All 71 represented Core subcategories were reviewed against Tables 1–4. The source-native subcategory remains a defensible independently assessable outcome; no artificial sentence-level split was introduced. Existing populated actor, object, timing, documentation, evidence and applicability metadata was checked against the cited subcategory and framework context. Empty fields were classified `not-specified-by-source` only after the direct review.

### CycloneDX 1.7

The component-type recommendation, non-ML prohibition and descriptive model-card proposition retain defensible boundaries. The `modelCard.bom-ref` record does not: it combines the mandatory uniqueness requirement with the recommendation that a value should not begin with `urn:cdx:` and represents both as mandatory. `EXTREQ-FA1B882FFAD54D93` is therefore queued for semantic decomposition with identity migration; no replacement IDs were allocated.

This finding changes CycloneDX 1.7 from fidelity-assured/effectively complete to provisional/effectively partial until that bounded repair occurs.

### NIST AI 600-1

The review confirmed that suggested-action IDs are useful source-defined identities and should not be mechanically exploded. It also confirmed two defects:

1. the source's AI Actor Tasks are subcategory-level applicability signals, and the source expressly warns that not every listed task applies to every suggested action; and
2. 60 actions retain constituent semantics only in compressed prose, including 51 summaries that visibly truncate source content and nine additional reviewed compound actions with independently meaningful steps.

The action-level actor field now uses the source-supported organization/relevant-AI-actor formulation. The former subcategory task lists are preserved as `NIST AI 600-1 AI Actor Tasks (subcategory-level)` tags instead of being attributed to every action. The 60 affected records retain their existing IDs and are queued for constituent enrichment; the seven affected metadata dimensions remain `review-required` rather than being padded with generic evidence or qualifications.

## Deterministic re-extraction backlog

`reextraction-backlog.json` contains 61 unique canonical requirement IDs:

- 60 NIST AI 600-1 actions for `constituent-enrichment-preserve-identity`;
- 1 CycloneDX record for `semantic-decomposition-with-identity-migration`;
- 61 `compound-normative-propositions` findings;
- 60 `constituent-semantics-loss` findings; and
- 1 `modality-loss` finding.

The metadata validator checks that every backlog ID resolves to a canonical requirement, source/version and locator metadata match, and every affected metadata dimension remains `review-required`.

## Remaining source-review programme

The next review order follows public-primary access and governance significance before lawful licensed-source work:

| Priority | Source/version | Records | Unresolved fields | Basis |
|---:|---|---:|---:|---|
| 1 | IMDA Agentic AI MGF 2026-05 | 32 | 256 | Critical public-primary governance source |
| 2 | NIST SP 800-218A (2024) | 74 | 592 | Largest remaining public-primary queue; software and model-development governance significance |
| 3 | AAM SDOS Runtime Governance 1.10 | 24 | 192 | Public-primary high-value governance source |
| 4 | NIST AI 100-2 E2025 | 22 | 176 | Public-primary specialist security source |
| 5 | NIST AI 100-4 (2024) | 18 | 144 | Public-primary provenance and synthetic-content source |
| 6 | NIST SP 1270 (2022) | 14 | 112 | Public-primary bias-management source |
| 7 | SPDX AI Profile 3.0.1 | 4 | 32 | Public technical specification with a bounded queue |
| 8 | IEEE 7014.1, 7000, 7009, 7014, 7001, 7010 and 7007 | 278 | 2,224 | Review only from the lawfully accessible licensed primary texts already recorded by the repository; never reconstruct from summaries or crosswalks |

The 81 unresolved canonical EU AI Act records remain explicitly paused for this package. Thirty-seven primary source versions remain blocked by access and have no reconstructed requirements.

## Validation handoff

| Command | Result |
|---|---|
| `python vigil/scripts/validate-external-requirement-metadata.py` | PASS; 947 records, 339 metadata-complete, 4,797 unresolved fields, 61 backlog records |
| `python vigil/scripts/validate-external-requirement-metadata.py --write-report` | PASS; generated JSON and Markdown reports refreshed |
| `python vigil/scripts/test_external_requirement_metadata.py` | PASS; ledger/backlog contract, source seeders and conflict refusal exercised |
| `python vigil/scripts/validate-external-requirement-fidelity.py` | PASS with 16 expected effective-downgrade warnings for historically complete but not fidelity-assured sources |
| `python vigil/scripts/manage-external-requirements.py validate --check-generated` | PASS; 81 source versions and 845 canonical requirements |
| `python vigil/tests/test_external_requirements.py` | PASS; 17 tests |
| `python vigil/scripts/test_external_requirement_fidelity.py` | PASS; 3 tests |
| `python vigil/scripts/test_eu_ai_act_reextraction.py` | PASS; 8 coarse records, 102 deterministic candidates and 18 normalization overrides |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | PASS; 148 tests; expected negative-fixture diagnostics emitted |
| `python -m pytest -q` | NOT RUN; the execution environment does not provide the `pytest` module; the repository `unittest` suite was used instead |

The fidelity-validator warnings are truthful effective-status downgrades for historically complete but still unassured sources. They are not contract errors and were not suppressed by invented assurance.
