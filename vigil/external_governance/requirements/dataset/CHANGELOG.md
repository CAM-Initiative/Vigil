# AI Governance Standards Baseline changelog

## Unreleased — pending-source extraction, 2026-10-01

Added 119 canonical requirements: 54 from the bounded CETS No. 225 implementation/remedies/risk/oversight scope, 37 from OECD/LEGAL/0449 Sections 1-2, and 28 from a partial C2PA 2.4 provenance-integrity/AI-disclosure slice. The current corpus has 1,097 records. Canada and IEEE 7003 retain zero records and explicit exact-primary-text access blockers. No taxonomy relationships were added. See `../../../docs/audits/external-requirements/2026-10-01-pending-external-source-expansion.md` for scope, provenance, interpretation conflicts and validation. Release 0.2.0 below remains the historical published boundary; this work does not publish a new package.

## 0.2.0 — 2026-09-28

### Newly registered sources

The source registry now includes four verified authoritative source/version identities. Registration provides source-level catalogue coverage only and does not imply clause-level analysis, conformance, legal applicability, or Compliance coverage.

- Council of Europe Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law, CETS No. 225 (`2024-09-05`). The treaty is recorded as open for signature and not in force; no entry-into-force claim is made.
- OECD Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449 (`2024-05-03` revision).
- Government of Canada Directive on Automated Decision-Making (`current-2026-09-28` verified official instrument snapshot).
- C2PA Technical Specification (`2.4`, April 2026).

All four have `extraction_status: not-started`, zero `EXTREQ` records, and an explicit primary-source analysis action.

### Structured requirement extraction completed

No newly registered 0.2.0 source has completed structured requirement extraction. The canonical corpus remains **978 EXTREQ records**. Previously complete, fidelity-assured source versions retain their status; this release does not recast source registration as clause-level coverage.

### Awaiting extraction or access

- IEEE 7003-2024 remains registered and `not-started`; primary text was not available in the execution environment through the IEEE Get Program, so no requirements were inferred or created.
- The consolidated EU AI Act of 27 July 2026 remains `partial` and `requires-reextraction`; the existing atomic/source-fidelity continuation boundary is preserved.
- ISO/IEC 42001:2023, ISO/IEC TS 8200:2024, ISO/IEC 42005:2025, and ISO/IEC 5338:2023 remain registered, `blocked-access`, and pending lawful primary-text access.

### Release metadata and generated projections

- Bumped the AI Governance Standards Baseline from 0.1.0 to 0.2.0 for material source-layer expansion.
- Increased registered source versions from 81 to 85 while preserving 978 canonical requirements.
- Rebuilt the public source catalogue, review queue, requirement index, completeness report, coverage manifests, access-limitations report, external-requirement catalogue, and derivative indexes.
- Updated the source gap analysis from a provisional discovery audit to a verified 0.2.0 source-baseline release record.

## 0.1.0 — 2026-09-26

Initial experimental dataset release with 81 registered source versions and 978 canonical EXTREQ records.
