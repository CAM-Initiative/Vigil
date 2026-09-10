# EXTREQ-14 — standards access continuation and reconciliation

**Review date:** 2026-09-10  
**Scope:** current international-standards ingestion state, source-access provenance and remaining work  
**Result:** existing clauses and mappings preserved; no new clause-level requirements created

## Continuation point

The repository contains 884 canonical requirements across 81 registered source versions. The seven first-class licensed IEEE sources represented in `source-fidelity.json` are already `assured` and effectively complete. The live re-extraction backlog contains no unresolved standards item. This pass therefore continued from the existing completion boundary instead of restarting extraction or duplicating sources.

The current environment could locate maintainer-supplied copies labelled as IEEE 7000-2021, 7001-2021, 7007-2021, 7009-2024, 7010-2020, 7014-2024 and 7014.1-2026. The connected-file interface did not provide a basis for recomputing and comparing their binary SHA-256 digests, so this pass does not independently re-verify their integrity or use them for new clause claims. It preserves—but does not silently reissue or weaken—the stronger prior licensed-primary review records and exact digests in `source-review-assurance.json`. The copies were not committed or redistributed.

No duplicate or conflicting canonical requirement was found. No existing clause, mapping, retirement record, source-fidelity finding or access limitation was removed.

## Sources reconciled

| Source or group | Current evidence status | Reconciliation |
|---|---|---|
| IEEE 7000-2021, 7001-2021, 7007-2021, 7009-2024, 7010-2020, 7014-2024 and 7014.1-2026 | Maintainer-supplied copies located in the current environment but current binary integrity not independently reverified; existing verified licensed-primary reviews and digests retained | Existing 308 live requirements and the IEEE 7009 retirement map were preserved without re-extraction or an access-status upgrade. |
| IEEE 2089-2021, 7002-2022, 7005-2021 and 7012-2025 | Maintainer-supplied copies located in the current environment but current binary integrity not independently reverified; canonical scope remains `supporting-only` | No requirement was created merely because a connected copy exists. Exhaustive decomposition remains outside the recorded source role and scope. |
| IEEE 7003-2024 | Official metadata/catalogue information verified; substantive primary text unavailable in the current environment | IEEE's official page identifies the standard, edition, publication date and a no-cost Get Program, but the standard text was not retrieved or inspected. The existing `direct-public-primary` / `not-started` entry requires provenance review before clause-level work; it is preserved rather than silently downgraded. |
| IEEE 2863-2026 | Official metadata only; blocked or unavailable substantive text | Existing `official-metadata-only` / `blocked-access` status retained. No clause statement was inferred. |
| ISO/IEC 12791:2024, 12792:2025, 17903:2024, 20226:2025, 21221:2025, 22989:2022, 23053:2022, 23894:2023, 24027:2021, 24028:2020, 24029-1:2021, 24029-2:2023, 24030:2024, 24368:2022, 24372:2021, 24668:2022, 25058:2024, 25059:2023, 38507:2022, 42001:2023, 42005:2025, 42006:2025, 42106:2026, 42112:2026, 42119-2:2025, 4213:2022, 5259-1:2024, 5259-2:2024, 5259-3:2024, 5259-4:2024, 5259-5:2025, 5259-6:2026, 5338:2023, 5339:2024, 5392:2024, 5469:2024, 6254:2025, 8183:2023, 8200:2024, and ISO/IEC/IEEE 24765:2017 | Official metadata or catalogue information only; no maintainer-supplied copy found | Existing scope retained: 36 `blocked-access`, three `context-only`, and one `supporting-only`. None is treated as direct evidence of clause content. |

## Access and provenance decisions

- Publisher pages and catalogue descriptions were used only to confirm document identity, edition, publication metadata, status and access routes.
- Connected maintainer-supplied files were not used for new substantive claims where current binary integrity could not be independently verified. Availability alone did not trigger new extraction.
- Prior licensed-primary requirements were not replaced with public summaries and their recorded reviewed-source digests were not altered.
- No copyrighted standards text or private file was added to the repository.
- IEEE 7003-2024 is the only current entry whose recorded access category needs specific provenance review: the official locator advertises an access route, but this pass did not obtain substantive text.

## Deferred work

Clause-level IEEE 7003 work is deferred until an authorised complete copy can be retrieved and its edition and integrity verified. IEEE 2863 and the 36 blocked ISO/IEC sources remain blocked for substantive extraction. The four licensed supporting-only IEEE sources remain out of first-class decomposition scope unless maintainers explicitly change that scope.
