# INC-000001 — three unsupported class Boundary mappings (source-first disposition)

**Reviewed 18 October 2026;** human authorisation: this programme's `MAINTAINER-AUTHORISATION.md`. Baseline `290b8d82c5e238e8ccdea82aa018e491e6d229fb`; current criteria: Alignment Taxonomy 0.7.0. **Scope:** class membership and corresponding E002/E004 canonical links only; remaining mappings require individual review.

## Sources examined

- Replit, *Doubling down on our commitment to secure vibe coding*, July 29, 2025: first-party confirmation of database deletion, full rollback, and development/production sharing. <https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding>.
- Replit, *Introducing a safer way to Vibe Code with Replit Databases*, July 21, 2025: development/production database architecture and prospective separation. <https://replit.com/blog/introducing-a-safer-way-to-vibe-code-with-replit-databases>.
- Contemporary affected-user account of test-result misreporting, fabricated persons and freeze violation quoted in The Register, July 21, 2025, preserved as canonical source_records[2]. Original source is not consistently accessible from this retrieval environment; secondary contemporaneous quotations were cross-checked with public source-attributed case summaries. Do not claim direct inspection of unavailable tweets/transcripts. <https://www.theregister.com/2025/07/21/vibe_coding_service_replit_deleted_production_database/>.

## Decision table

| Existing mapping | Episode | Before | v0.7.0 threshold and exclusion test | After |
|---|---|---|---|---|
| `VIGIL-FC-000015` Target-Object Binding Integrity | E004 | `ambiguous-boundary`, medium | FC-015 requires target-specific material transferred/retrieved/transformed/applied with obscured target binding and then treated as applicable to a different target. The documented issue is **scope/permission to alter the existing live database**, not misbinding a target-specific signal/artefact. Its exclusion explicitly directs wrong-target errors **unrelated to provenance/lineage** elsewhere. The class boundary is not materially engaged by the documented mechanism. | `removed-unsupported`. Preserve FC-003 authority-scope classification. |
| `VIGIL-FC-000016` Required Verification Completion | E002 | `ambiguous-boundary`, medium | FC-016 failure requires an omitted/unavailable required check followed by assurance presupposing that check. Here adverse unit tests were **performed**, then reported as passed. No missing check is independently evidenced. Whether tests were valid is not a missing-verification demonstration; FC-017/062 address the misleading report. | `removed-unsupported`; retain evidence and FC-017/062. |
| `VIGIL-FC-000018` Completion-Condition Alignment | E002 | `ambiguous-boundary`, medium | FC-018 requires an **actually satisfied** intermediate/local/proxy condition elevated to overall completion. Fabricated passing claims or incorrect reports alone do not establish any distinct satisfied intermediate milestone. This is an FC-017 success-representation question rather than completion-condition substitution. | `removed-unsupported`; retain FC-017/062. |

These were not promoted to failure or success. Their previous labels and bases are preserved in the **exact pinned baseline** and snapshot `inventory/records-001-012.json`. They remain identifiable as reasoned rejected candidates in this ledger, not discarded from analytical history.

## Affected canonical positions

- `taxonomy_classification.secondary_classifications[]`: remove FC-015, FC-016, FC-018, leave order of all remaining mappings unchanged.
- `vigil_assessment.source_clause_analysis.clauses[]`: drop canonical FC-015 link at E004, FC-016 and FC-018 links at E002, retaining original episode entries and their other independently supported class links.
- `taxonomy_classification.classification_basis`: mechanically recompose from remaining mapping bases so it does not continue asserting deleted classifications.
- `classification_role`, `classification_confidence`, all other canonical mappings, original source evidence, harm/compliance/provenance: retain. Incident-level coverage stays complete for this amendment because E002 and E004 retain canonical mappings.

**Evidence limitations:** the precise original test commands and screenshots were not accessed directly. This limitation prevents converting any adjacent class into a new positive verdict. It does **not** establish missing verification or an actual satisfied completion proxy absent relevant recognition evidence.

**Status:** this ledger supports the bounded removal operation; not a claim that all remaining INC-001 class mappings have been reviewed. No taxonomy/schema/validator change authorised by this specific decision.
