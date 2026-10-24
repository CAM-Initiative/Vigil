# International infrastructure governance source registration

Classification: REVIEW. Date: 11 October 2026.
Baseline integration HEAD: `6192d5d4b66c6d8bb9fbf9e86347e8f0b56e7866`.
Branch: `work/infrastructure-governance-instruments`; PR base: `agent/incident-ecosystem-ingestion`.

The implementation handoff authorises source registration and exact requirement extraction, while explicitly withholding approval for semantic control changes. Registration is complete for 13 supporting source versions. Canonical extraction is held because the existing manager forbids supporting-source requirements. This package does not relabel treaties as AI standards to pass the guard.

Read [Gate 1 proposal](GATE-1-PROPOSAL.md), [source and occurrence screening](RELATIONSHIP-AND-INC-090-SCREENING.md), the [historical Git-pinned 13-source inventory](https://github.com/CAM-Initiative/Vigil/blob/e2a49427fce5236266174939633c970778c7a3a7/vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/inventory.json), the canonical `vigil/external_governance/sources/source-registry.json`, `requirements/source-scope.json`, `requirements/source-review-assurance.json`, and [historical validation receipt](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/VALIDATION.md). The single still-live source fiche is [ICRC-SPACE-CIVILIAN-SERVICES.md](ICRC-SPACE-CIVILIAN-SERVICES.md), pending full durable carrier-hash reconciliation.

## Inventory by external authority and time

| Category | Registered sources | Temporal boundary |
| --- | --- | --- |
| Treaty instruments | Geneva I–IV (1949), AP I (1977), ITU Constitution (1992, amended through 2010 in 2019 carrier), Outer Space Treaty (1967), ICCPR (1966) | Predate 2022. General commencement is recorded; actor/party/reservation/jurisdiction and country-specific temporal applicability remain separate unresolved questions. |
| UN-endorsed non-binding principles | UNGP (2011) | Predate 2022. Company responsibilities distinguished from State duties and legal liability. |
| Security Council resolution | Resolution 2573 (2021) | Predates 2022. Demand/reminder, condemnation and exhortation require separate clause-force review. |
| Non-binding conference guidance | 34IC/24/R2 (2024) | Post-2022; no retrospective duty claimed. |
| Institutional interpretation/research | ICRC space-services report (2024), connectivity analysis (2025) | Post-2022 supporting context. Report abstract only reviewed; commentary is not new law. |

## Source fidelity and identity

Source IDs and fingerprints use the repository manager's `stable_id`, `canonicalise` and `metadata_fingerprint` functions. No EXTREQ ID is invented or reserved. Original official locators are preserved. OHCHR booklet access returned 403; its principles were reviewed in the official UN Digital Library A/HRC/17/31 Annex instead. The original UNOOSA and UN resolution texts were retrievable through direct official downloads despite web-fetch errors. ICRC treaty collections supplied primary text where the database rendered a JavaScript shell.

Exact retrieved-carrier hashes are recorded without committing copied institutional publications. The 2024 report's page hash identifies publisher metadata only and is not entered as a primary-text requirement digest. Source metadata fingerprints are distinct from carrier hashes. No human review or verification is claimed. Source review remains required for canonical extraction; no completeness or field-level requirement assurance is fabricated.

## Artefact disposition

- LIVE: source matrix, registry, source scope and reviewed-source assurance sidecar entries.
- GENERATED: source catalogue/queue and requirement coverage/index/report outputs produced by the existing managers.
- REVIEW: this directory's source-first screening and Gate 1 material; dated bulk inventory and 12 redundant source fiches are archived at parent `e2a49427fce5236266174939633c970778c7a3a7`, while the exception with missing verified assurance digest remains live.
- AUDIT / RETIRE: no existing artefact is rewritten or retired by this package.

The 1,102 existing requirements, taxonomy relationship ledger, Incident records, schema, validator, tests and publication guards are preserved. No whole-corpus repair or release-complete assertion is made. Canonical extraction, FC relationships and Section 04 work resume only after the bounded Gate 1 decision.

Final reconciliation baseline: `2d85728288dfc9c286861d61e7815b0bff787f03`. Its military-personnel legal gate and revised INC-090 0.1.17 are preserved. See the screening addendum.

## Gate 1 amendment — FC-058/059 research (11 October 2026)

The later handoff requests an expanded supporting-source admission rule and research only. The revised [Gate 1 proposal](GATE-1-PROPOSAL.md) supersedes the category-limited proposal; its previous version remains in Git history. The earlier registration notes and validation report retain their historical scope.

Deliverables:

- A. [Amended Gate 1 proposal](GATE-1-PROPOSAL.md).
- B. [FC-058 / FC-059 primary-source assessment matrix](FC-058-059-SOURCE-ASSESSMENT.md).
- C. [Source registration gap report](SOURCE-REGISTRATION-GAPS.md).
- D. [INC-090 applicability and evidence note](INC-090-APPLICABILITY.md).
- E. [Atomic implementation and validation plan](IMPLEMENTATION-PLAN.md).

Amendment baseline: `f0baf24b3d05a972705995986c82e1b64770ae34`. Primary-source research includes the EU original OJ texts, dated GNI Principles/Guidelines, OECD 2023 Guidelines, UNGP, ITU Constitution/2012 ITRs and registered NIST texts. ISO review is metadata-only; no copyrighted clause reconstruction. The matrix is a queue of reviewed component relationships, not canonical admission or an occurrence finding.

Research-pass verification: all six changed files are review documents in this directory. Existing cited EXTREQ IDs resolve to their stated sources/clauses, relative Markdown links resolve, and `git diff --check` passes. Counts remain 98 source versions, 1,102 requirements and 189 Incidents. All source data, canonical shards, relationship ledger, taxonomy, Incidents (including INC-090), schema, scripts, builders and permanent tests are byte-identical to the amendment baseline. No semantic controls or new tests are implemented. Existing historical validation limitations remain recorded in [historical validation receipt](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/VALIDATION.md).

**Stop: revised Gate 1 implementation approval pending.** No new source registration, EXTREQ allocation, relationship admission or Section 04 change is authorised by this research package. Gate 2 remains separate.


### Archived 11 October validation receipt — 24 October 2026

The [full original command/CI result](https://github.com/CAM-Initiative/Vigil/blob/035b81e88368c92a88088ae1bec8b7d30f81376c/vigil/docs/reviews/2026-10-11-infrastructure-governance-registration/VALIDATION.md) documents **31/32 passing baseline validation commands**, with the sole thin-referential-integrity failure on unresolved historical FC-084 references in INC-060/189 (not a newly established source defect). It also recorded 98 source versions after registration, 1,102 unchanged requirements, 189 canonical Incidents and the original successful [records](https://github.com/CAM-Initiative/Vigil/actions/runs/38137737151) and [external governance](https://github.com/CAM-Initiative/Vigil/actions/runs/38137737197) runs on PR #125. The previously broken FC-084 proposal references were subsequently repaired in the later authorised taxonomy migration; **this is a historic execution receipt, not a present-day CI or regulatory assurance claim**. Detailed original command output is recoverable at the exact pinned Git commit, while registered source/scope/fidelity research, pending ICRC carrier integrity and all contemporary validation continue in the canonical records and current CI.
