# EXTREQ-04 — Corpus-Wide Requirement Metadata Fidelity Review

Date: 2026-08-28
Working branch: `agent/hugging-face-authority-reconciliation`
Review basis: direct authoritative primary text; AI-authored substantive review under the repository provenance contract; no human substantive verification claimed.

## Outcome

The review package now assesses 956 records: 854 canonical requirements and 102 staged EU AI Act migration candidates. It records 539 metadata-complete records, 417 records still requiring review, 3,336 unresolved field decisions, and no canonical re-extraction backlog.

Completion is based on explicit review-state resolution, not field population. Reviewed propositions were populated from the source or marked source-silent for that dimension. Remaining unresolved decisions belong to other source populations that have not completed the same primary-text review.

## Primary-source basis

| Source | Authoritative basis used | Reviewed population | Result |
|---|---|---:|---|
| EU AI Act, consolidated 27 July 2026 | EUR-Lex CELEX `02024R1689-20260727`; existing staged Articles 4a and 9–15 packages | 102 staged candidates | 102 metadata-complete; no Article 16+ extraction undertaken |
| NIST AI RMF 1.0 | DOI `10.6028/NIST.AI.100-1`; PDF SHA-256 `7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1` | 71 Core subcategories | 71 metadata-complete; source-defined outcome granularity retained |
| AAM SDOS Runtime Governance 1.10 | Complete public control catalogue; HTML SHA-256 `547bfa9615f137429871951e2beb8de8f306ed8ae4995e6ef95dfcfbcc23c52b` | 24 controls | 24 metadata-complete; all source-native identities retained and related-control links restored |
| CycloneDX 1.7 | Official schema at commit `4b3f59453366e27c8073fd24e98bf21ef8892c8e`; SHA-256 `df472ef4aaf593904c479293723a1a5c191d6672715c93b3c0b5c318f3914221` | 5 propositions | 5 metadata-complete; MUST uniqueness and SHOULD reserved-prefix propositions separated |
| NIST AI 600-1 | DOI `10.6028/NIST.AI.600-1`; PDF SHA-256 `6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a` | 223 represented records | 223 metadata-complete; 60 constituent repairs completed with identity preserved |
| IMDA Agentic AI MGF 1.5 | Official IMDA PDF; SHA-256 `2636e19ff1c86e862394d2fc900592e97b83c04cc35e3c8443108114b7f1dfba` | 39 represented records | 39 metadata-complete; all 20 queued defects resolved, with seven migrated and seven additional deterministic identities |
| NIST SP 800-218A | DOI `10.6028/NIST.SP.800-218A`; PDF SHA-256 `e088c8bc75716824dae7c36a987f408364638561d381ed001b5c12254a7b10d8` | 75 R/C propositions | 75 metadata-complete; five records enriched and PW.7.1 R1/C1 separated |

## Completed fidelity repairs

### AAM SDOS Runtime Governance 1.10

All 24 records were compared with the complete public v1.10 control catalogue. The source-defined control is the defensible unit, so every established EXTREQ identity was retained. Generic runtime-system metadata was replaced with control-specific objects, timing, artefacts, evidence categories, verification methods, applicability conditions and qualifications. The catalogue's related-control references now resolve deterministically to the corresponding EXTREQ identities.

Source limitations are explicit: SDOS is an owner-authored private-sector framework; its public reference assigns implementation-level schemas and operational details to licensed documentation; framework mappings do not establish certification or independent compliance. Specific limitations for partial degradation, identity attestation, distributed timestamps, append-only storage, dual audit repositories, deliberation convergence and ROSI evaluation are preserved. SDOS v1.10 is fidelity-assured and effectively complete.

### CycloneDX 1.7

`EXTREQ-FA1B882FFAD54D93` retains the mandatory `modelCard.bom-ref` uniqueness identity. The distinct recommendation not to start the value with `urn:cdx:` is represented by deterministic identity `EXTREQ-F2C81603A7B306F6`, with the source-explicit limitation that the referenced `refType` pattern does not enforce that recommendation. CycloneDX 1.7 is fidelity-assured and effectively complete.

### NIST AI 600-1

All 60 affected suggested-action records retain their established identities. Complete action text and source-supported objects, timing, artefacts, evidence, methods, conditions, and qualifications replace compressed or truncated metadata. Subcategory-level AI Actor Tasks remain source-defined tags rather than being attributed to every suggested action. NIST AI 600-1 is fidelity-assured and effectively complete.

### IMDA Agentic AI MGF 1.5

All 32 original records were compared with the complete official version 1.5 PDF. Twelve identities were enriched without migration. Of eight compound abstractions, one retained a defensible constituent identity under its existing clause key; seven migrated to deterministic subsection identities. Seven additional constituent records represent approval-request quality, oversight audit, overseer training, automated real-time monitoring, runtime controls, change review, and integrating-user training.

The resulting 39 records preserve subsection traceability through the deterministic clause key or, for five identity-preserving coarse keys, through exact subsection provenance and `parent_section_or_group`. Unsupported additions such as generic report duties, organisation-wide delegation authority, and materially-affected-person scope were removed. Source-explicit outputs for logging, failsafe mechanisms, testing, approvals, contracts, training, and escalation were restored. IMDA 1.5 is fidelity-assured and effectively complete.

### NIST SP 800-218A

Five truncated propositions now preserve complete source conditions, qualifications, examples, outputs, and methods with identity retained. `PW.7.1 R1` retains `EXTREQ-CFC9864F6289630A`; the separately stated C1 consideration is `EXTREQ-1FFE1710582A469A` with informative-guidance posture. The corpus now represents all 75 source-native R/C propositions. NIST SP 800-218A is fidelity-assured and effectively complete.

## Provenance and determinism

Exact reviewed-source digests are recorded in `source-review-assurance.json`, separately from empty human-assurance arrays. Record provenance remains AI-authored, semi-autonomous, contract-approver, with human authorship false and human review and verification both `not-reviewed` / `not-verified`.

The reviewed-source seeder is conflict-intolerant and now covers 437 non-EU requirements. Its current metadata-ledger SHA-256 is `b7d4904d2f65341df38f380fd881a6ff85ca59c31b8e40c173225814a5a70d46`; the empty deterministic backlog SHA-256 is `296e5fd756b620a432ada788a7ececd6c90cb32080d835581155371923922492`.

## Deterministic re-extraction backlog

`reextraction-backlog.json` contains zero entries. The validator confirms that no record remains flagged for re-extraction and no retired IMDA identifier is present or referenced.

## Remaining source-review programme

| Priority | Source/version | Records | Unresolved fields | Basis |
|---:|---|---:|---:|---|
| 1 | NIST AI 100-2 E2025 | 22 | 176 | Public-primary specialist security source |
| 2 | NIST AI 100-4 (2024) | 18 | 144 | Public-primary provenance and synthetic-content source |
| 3 | NIST SP 1270 (2022) | 14 | 112 | Public-primary bias-management source |
| 4 | SPDX AI Profile 3.0.1 | 4 | 32 | Public technical specification with a bounded queue |
| 5 | IEEE 7014.1, 7000, 7009, 7014, 7001, 7010 and 7007 | 278 | 2,224 | Use only the lawfully accessible licensed primary texts recorded by the repository |

The 81 unresolved canonical EU AI Act records remain explicitly paused. Thirty-seven source versions remain access-blocked; no requirements are reconstructed from summaries or secondary sources.

## Validation handoff

| Command | Result |
|---|---|
| `python vigil/scripts/migrate-sdos-runtime-fidelity.py --write` | PASS; 24 identities retained, zero added and zero retired |
| `python vigil/scripts/seed-reviewed-source-metadata.py --write` | PASS; 437 reviewed non-EU requirements and zero backlog entries |
| `python vigil/scripts/validate-external-requirement-metadata.py --write-report` | PASS; 956 records, 539 metadata-complete, 3,336 unresolved fields, zero backlog records |
| `python vigil/scripts/test_external_requirement_metadata.py` | PASS; ledger, digest, migration, and conflict-refusal contracts exercised |
| `python vigil/scripts/validate-external-requirement-fidelity.py` | PASS; 6 fidelity-assured/effectively complete sources and 11 expected effective-downgrade warnings |
| `python vigil/scripts/manage-external-requirements.py build` | PASS; generated projections refreshed |
| `python vigil/scripts/manage-external-requirements.py validate --check-generated` | PASS; 81 source versions and 854 canonical requirements |
| `python -m unittest vigil/tests/test_external_requirements.py vigil/tests/test_external_sources.py` | PASS; 34 tests |
| `PYTHONPATH=vigil/scripts python -m unittest vigil/scripts/test_external_requirement_fidelity.py` | PASS; 3 tests |
| `PYTHONPATH=vigil/scripts python vigil/scripts/test_eu_ai_act_reextraction.py` | PASS; 8 coarse records, 102 deterministic candidates, and 18 normalizations |
| `python -m unittest discover -s vigil/tests -p 'test_*.py'` | 175 of 177 pass; two pre-existing unrelated failures remain in `FM-0071` facet vocabulary and its evidenced-product union |

The fidelity warnings are truthful effective-status downgrades for historically complete but still unassured sources. They are not contract errors and were not suppressed with invented assurance.
