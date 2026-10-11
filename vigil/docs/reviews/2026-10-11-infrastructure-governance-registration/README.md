# International infrastructure governance source registration

Classification: REVIEW. Date: 11 October 2026.
Baseline integration HEAD: `6192d5d4b66c6d8bb9fbf9e86347e8f0b56e7866`.
Branch: `work/infrastructure-governance-instruments`; PR base: `agent/incident-ecosystem-ingestion`.

The implementation handoff authorises source registration and exact requirement extraction, while explicitly withholding approval for semantic control changes. Registration is complete for 13 supporting source versions. Canonical extraction is held because the existing manager forbids supporting-source requirements. This package does not relabel treaties as AI standards to pass the guard.

Read [Gate 1 proposal](GATE-1-PROPOSAL.md), [source and occurrence screening](RELATIONSHIP-AND-INC-090-SCREENING.md), [inventory](inventory.json), the individual source notes and [validation evidence](VALIDATION.md).

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
- REVIEW: this directory, individual source/version notes, screening, inventory, Gate 1 proposal and validation evidence.
- AUDIT / RETIRE: no existing artefact is rewritten or retired by this package.

The 1,102 existing requirements, taxonomy relationship ledger, Incident records, schema, validator, tests and publication guards are preserved. No whole-corpus repair or release-complete assertion is made. Canonical extraction, FC relationships and Section 04 work resume only after the bounded Gate 1 decision.

Final reconciliation baseline: `2d85728288dfc9c286861d61e7815b0bff787f03`. Its military-personnel legal gate and revised INC-090 0.1.17 are preserved. See the screening addendum.
