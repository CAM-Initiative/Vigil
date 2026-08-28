# EXTREQ-04 — Corpus-Wide Requirement Metadata Fidelity Review

Date: 2026-08-28
Working branch: `agent/hugging-face-authority-reconciliation`
Review basis: direct authoritative primary text; AI-authored substantive review under the repository provenance contract; no human substantive verification claimed.

## Outcome

This package exercised the field-level review contract across the staged EU AI Act slice and the complete represented populations for NIST AI RMF 1.0, CycloneDX 1.7, NIST AI 600-1, IMDA Agentic AI MGF 1.5 and NIST SP 800-218A.

The generated report now assesses 947 records: 845 canonical records and 102 staged EU AI Act migration candidates. It records 480 metadata-complete records, 467 records still requiring review, 3,640 unresolved field decisions and 27 canonical records queued for substantive re-extraction, constituent enrichment or locator repair.

Completion is based on explicit review-state resolution, not on field population. No reviewed field was classified `not-applicable` in this package: the reviewed operational propositions were either populated from the source, source-silent for the dimension, or left `review-required` because a known fidelity defect prevents a defensible final decision.

## Primary-source basis

| Source | Authoritative basis used | Reviewed population | Result |
|---|---|---:|---|
| EU AI Act, consolidated 27 July 2026 | EUR-Lex CELEX `02024R1689-20260727`; existing staged Articles 4a and 9–15 packages and source-explicit normalization overlay | 102 staged candidates | 102 metadata-complete; no Article 16+ extraction undertaken |
| NIST AI RMF 1.0 | `https://doi.org/10.6028/NIST.AI.100-1`; downloaded PDF SHA-256 `7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1` | 71 Core subcategories | 71 metadata-complete; source-defined outcome granularity retained |
| CycloneDX 1.7 | Official specification tag `1.7`, commit `4b3f59453366e27c8073fd24e98bf21ef8892c8e` | 4 ML-BOM propositions | 3 metadata-complete; 1 queued for modality-preserving decomposition |
| NIST AI 600-1 | `https://doi.org/10.6028/NIST.AI.600-1`; downloaded PDF SHA-256 `6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a` | 223 represented records, including 211 suggested actions | 223 metadata-complete; 60 constituent repairs completed with identity preserved |
| IMDA Agentic AI MGF 1.5 | Official IMDA PDF, published 20 May 2026 and updated 5 June 2026; downloaded PDF SHA-256 `2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba` | 32 represented records | 13 metadata-complete; 19 retain unresolved fields; 20 queued for re-extraction or locator repair |
| NIST SP 800-218A | `https://doi.org/10.6028/NIST.SP.800-218A`; July 2024 official PDF SHA-256 `e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8` | 74 represented records for 75 source R/C propositions | 68 metadata-complete; 6 retain unresolved fields and are queued for repair |

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

The review confirmed that suggested-action IDs are useful source-defined identities and should not be mechanically exploded. The completed tranche addressed two previously recorded defects:

1. the source's AI Actor Tasks are subcategory-level applicability signals, and the source expressly warns that not every listed task applies to every suggested action; and
2. 60 actions had retained constituent semantics only in compressed prose, including 51 summaries that visibly truncated source content and nine additional reviewed compound actions with independently meaningful steps.

The action-level actor field uses the source-supported organization/relevant-AI-actor formulation. The former subcategory task lists remain preserved as `NIST AI 600-1 AI Actor Tasks (subcategory-level)` tags instead of being attributed to every action. All 60 affected records retain their existing IDs. Their complete suggested-action text now replaces truncated summaries, and governed objects, timing, artefacts, evidence, verification methods, applicability conditions and qualifications are resolved only where supported by the primary text. The tranche removes all 60 entries from the deterministic backlog and restores NIST AI 600-1 to fidelity-assured/effectively complete status without claiming human review or verification.

The exact reviewed official PDF digest is now recorded in `source-review-assurance.json`, separately from the empty human-assurance array. Two successive seeder writes produced identical metadata-ledger SHA-256 `837c384a30c680f6fbc8ebabe627aec195bb21a597892dc3fba7193fc5279495` and backlog SHA-256 `f3ff2c122d524d424c8a204e51d0acd68b66789a586ccecb5b6995dbd852dc4f`; the second execution added zero entries.

### IMDA Agentic AI MGF 1.5

All 32 records were compared with the current official PDF. The framework-wide applicability condition is explicit: it targets organisations looking to deploy agentic AI, whether developing agents in-house or using third-party solutions. That condition and three source-explicit timing, test-output and verification-method enrichments were applied deterministically.

The review found material extraction loss in 20 records. Eight require semantic decomposition with identity migration; twelve require constituent enrichment or locator refinement while preserving identity. The defects include analytical additions not supported by the cited proposition, substituted actor or contract semantics, omitted logging and failsafe outputs, and section 2.2–2.4 locators where the recommendation appears only in a narrower subsection. One locator-only record is metadata-complete but remains queued because field completeness does not cure source traceability.

Thirteen records are metadata-complete. Nineteen retain 88 unresolved field decisions. Populated fields affected by a fidelity defect remain `review-required`; they were not accepted merely because they contain values. Existing coarse canonical summaries and IDs remain unchanged.

Two successive seeder writes produced identical metadata-ledger SHA-256 `b6ee59ae1ed3356b19b8364e9ab5867424bc626c187ca58aa76c5c2a472a634e` and backlog SHA-256 `f2f152d0dbfbdaaa453caee3db90e67d1e059a354f57623b3335aa606a9f8547`; the second execution added zero entries.

### NIST SP 800-218A

All 74 records were reviewed against the July 2024 primary publication, including the parent SSDF task context and the source-wide audience, scope and risk-tailoring rules. Actor metadata now preserves the three NIST-defined audiences—AI model producers, AI system producers and AI system acquirers—as relevant to role. Every record also preserves that the Profile must be used with SSDF 1.1, is risk-tailored rather than a checklist, and excludes AI-system deployment/operation and most of the broader data-governance life cycle.

The source contains 75 distinct recommendation and consideration propositions. The catalogue contains 74 records because `PW.7.1 R1` and `C1` were collapsed into one recommended-practice record, losing the distinct consideration modality. Five additional summaries truncate material qualifications, conditions or source-defined examples. Those six records retain 23 `review-required` field decisions; the other 68 records are metadata-complete and retain their source-native identities.

The review also removed mechanically inferred metadata where words such as “training and testing data” had generated a false test-evidence expectation, and replaced generic report, monitoring and documentation labels only where the source expressly requires an artefact or necessarily produces an output. Two successive seeder writes produced identical ledger SHA-256 `e082f23bcc9601232c7ceeb95459cf7f96a2b4999db0f8d49db3a8bd1f9e54df` and backlog SHA-256 `30f5e141a8d5dcc80470d82c46ed3a70516b293f536ae05f5fb9c7ed5e22bccf`; the second execution added zero entries.

## Deterministic re-extraction backlog

`reextraction-backlog.json` contains 27 unique canonical requirement IDs:

- 1 CycloneDX record for `semantic-decomposition-with-identity-migration`;
- 20 IMDA records: 8 for semantic decomposition with identity migration and 12 for constituent enrichment or locator repair;
- 6 NIST SP 800-218A records: 1 for modality-preserving semantic decomposition and 5 for constituent enrichment;
- 12 `compound-normative-propositions` findings;
- 24 `constituent-semantics-loss` findings;
- 14 `locator-too-coarse` findings;
- 11 `condition-loss` findings;
- 8 `output-or-artefact-loss` findings;
- 2 `timing-loss` findings; and
- 2 `modality-loss` findings; and
- 1 each of `actor-loss` and `exception-loss`.

The metadata validator checks that every backlog ID resolves to a canonical requirement, source/version and locator metadata match, and every affected metadata dimension remains `review-required`.

## Remaining source-review programme

The next review order follows public-primary access and governance significance before lawful licensed-source work:

| Priority | Source/version | Records | Unresolved fields | Basis |
|---:|---|---:|---:|---|
| 1 | AAM SDOS Runtime Governance 1.10 | 24 | 192 | Public-primary high-value governance source |
| 2 | NIST AI 100-2 E2025 | 22 | 176 | Public-primary specialist security source |
| 3 | NIST AI 100-4 (2024) | 18 | 144 | Public-primary provenance and synthetic-content source |
| 4 | NIST SP 1270 (2022) | 14 | 112 | Public-primary bias-management source |
| 5 | SPDX AI Profile 3.0.1 | 4 | 32 | Public technical specification with a bounded queue |
| 6 | IEEE 7014.1, 7000, 7009, 7014, 7001, 7010 and 7007 | 278 | 2,224 | Review only from the lawfully accessible licensed primary texts already recorded by the repository; never reconstruct from summaries or crosswalks |

The 81 unresolved canonical EU AI Act records remain explicitly paused for this package. Thirty-seven primary source versions remain blocked by access and have no reconstructed requirements.

## Validation handoff

| Command | Result |
|---|---|
| `python vigil/scripts/seed-reviewed-source-metadata.py --write` (twice) | PASS; 404 reviewed non-EU requirements, 0 new entries, 27 deterministic backlog entries; ledger and backlog hashes unchanged on the second write |
| `python vigil/scripts/validate-external-requirement-metadata.py` | PASS; 947 records, 480 metadata-complete, 3,640 unresolved fields, 27 backlog records |
| `python vigil/scripts/validate-external-requirement-metadata.py --write-report` | PASS; generated JSON and Markdown reports refreshed |
| `python vigil/scripts/test_external_requirement_metadata.py` | PASS; ledger/backlog contract, source seeders and conflict refusal exercised |
| `python vigil/scripts/validate-external-requirement-fidelity.py` | PASS; 6 explicit fidelity entries, 2 fidelity-assured/effectively complete sources and 15 expected effective-downgrade warnings for historically complete but not fidelity-assured sources |
| `python vigil/scripts/manage-external-requirements.py build` | PASS; generated external-requirement projections refreshed |
| `python vigil/scripts/manage-external-requirements.py validate --check-generated` | PASS; 81 source versions and 845 canonical requirements |
| `python vigil/tests/test_external_requirements.py` | PASS; 20 tests |
| `python vigil/scripts/test_external_requirement_fidelity.py` | PASS; 3 tests |
| `python vigil/scripts/test_eu_ai_act_reextraction.py` | PASS; 8 coarse records, 102 deterministic candidates and 18 normalization overrides |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | 175 of 177 tests pass; two pre-existing failures remain in `FM-0071` facet vocabulary and its evidenced-product union |
| `python -m pytest -q` | NOT RUN; the execution environment does not provide the `pytest` module; the repository `unittest` suite was used instead |

The fidelity-validator warnings are truthful effective-status downgrades for historically complete but still unassured sources. They are not contract errors and were not suppressed by invented assurance.
