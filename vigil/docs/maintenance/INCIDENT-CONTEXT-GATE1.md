# Incident Context architecture — approved Gate 1 (22 October 2026)

## Maintainer authorization and boundary

The maintainer approved the **additive canonical metadata architecture** and an opt-in validator on the existing `agent/incident-ecosystem-ingestion` branch. Full backfill of the current 200 Incidents is a **separate Gate 2 Work-thread task**, not authorised by this change. Maintain Incident-ID allocation, incoming evidence ingestion and all existing classification/HIM/source provenance separately. No canonical existing Incident was rewritten in Gate 1.

**Stage 01 website proposal:** rename "Affected systems — Platforms, products and runtimes named in the evidence" to **Incident Context**, split into five subheadings: **Systems & Technology**, **Operational Environment**, **Affected Parties & Institutions**, **Geographic & Jurisdictional Context**, and **Regulatory Context**. Keep What happened and evidence as surrounding Stage 01 content. This is a display redesign, NOT permission to relocate canonical narrative or to edit its source evidence. Current site renderer changes are a separate catalogue-branch task.

### Semantic boundary

- Keep `system_context` intact. Its provider/product/agent/occurrence fields already have stable canonical roles. Do not duplicate them in geographic metadata.
- Add optional `affected_party_context.entities[]` on the Incident. An "affected" role means referenced/implicated in the occurrence; it **does not by itself establish materialised harm**. Roles such as `provider` and `operator` remain distinct.
- Add optional `jurisdictional_context.normalized_geography`, leaving existing primary/secondary narrative and sector/regulatory surface unchanged.
- Each geographic relationship independently states **why** a named country or region is relevant and may reference one or more affected-party entities. One Incident may have many such relationships, including several countries and different relationships to the same country.
- `regulatory-context` records a *potential geographic context* requiring separate review. Section 04 external-governance adjudication alone decides applicability/compliance interpretations. No relation asserts an applicable law, legal breach, harm severity or case taxonomy.
- `source_record_refs` resolves canonical Incident `source_records[N]` references; no source content is copied or fabricated. A valid reference is structural traceability, not independent verification that the referenced source supports every proposed assertion.
- Opt-in data may not invent precise GPS event coordinates. Geographic centroids are website presentation anchors, never event coordinates or a harmed-person location.
- Controlled `evidence_state`: supported, attributed, disputed, unresolved. "Supported" still needs source-level factual review; the validator only checks structural assertions.

## Canonical shapes

```json
{
  "affected_party_context": {
    "entities": [{
      "party_id": "PARTY-001",
      "name": "Illustrative affected public service",
      "kind": "service",
      "roles": ["affected-service"],
      "evidence_state": "attributed",
      "evidence_basis": "Illustrative only: replace with the supported occurrence-specific relationship.",
      "source_record_refs": ["source_records[0]"]
    }]
  },
  "jurisdictional_context": {
    "primary_jurisdiction": "Existing text preserved verbatim",
    "normalized_geography": {
      "scope": "cross-border",
      "relations": [{
        "relationship_id": "GEO-001",
        "role": "affected-service-jurisdiction",
        "evidence_state": "attributed",
        "evidence_basis": "Illustrative only: explain why the service is associated with this jurisdiction.",
        "source_record_refs": ["source_records[0]"],
        "party_refs": ["PARTY-001"],
        "locations": [{"country_code": "AU", "subdivision_code": "AU-NSW"}]
      }]
    }
  }
}
```

**This is a design illustration, not a proposed content update to an actual Incident.** Leave all asserted relationship fields absent unless evidence has been examined. Record-local IDs are stable within that one Incident. Full structure and enums: `vigil/VIGIL.Schema.json`, `incident_context_rules`. Optional authoring example: `vigil/templates/incident-context-optional-template.json`.

## Gate 1 validator change rationale and pass/fail delta

1. **Before:** `system_context` validates provider/product, agent topology and operational environment. `jurisdictional_context` text is effectively not checked for structured semantic relationships. No dedicated affected-party relationship validator.
2. **After:** if `affected_party_context` or `jurisdictional_context.normalized_geography` is present, enforce controlled entity/geographic roles and evidence states, valid local unique IDs, nonempty bases, resolvable citation references, valid ISO 3166-1 alpha-2 *country* codes, ISO 3166-2-style subdivision syntax and parent-country consistency, unique locations, and valid local party references. Unknown/unresolved relations must not carry affirmative country locations. Disallow unknown canonical relationship keys (such as `law_applies`).
3. **Previously passed, now fails:** an Incident asserting an affected-service jurisdiction `ZZ`, a US subdivision for an Australian country, unresolved geography with a country, or a provider/regulatory location without source evidence. **Previously failed, now passes:** the new structured objects with valid evidence/source relationships; they were not part of the prior declared schema contract. Legacy Incidents without these new structures still pass.
4. **Affected surfaces:** `VIGIL.Schema.json`; `incident-record-template.json`; `scripts/incident_context_validation.py` and `scripts/validate-vigil-records.py`; `tests/test_incident_context_validation.py`; future public index projection, website Stage 01, PDF and dashboard filters.
5. **Expected corpus impact:** 200 existing Incidents require a future semantic review to populate metadata. The present Gate 1 validator adds no requirement for legacy backfill; expected new corpus failures from *absence* of metadata: **zero**. New synthetic/incorrect populated metadata may fail.
6. **Repair implication:** no existing text, classification, source evidence, HIM, event scope or current `system_context` is moved/removed. A later authorized migration will append source-bounded relationships and preserve all original strings and source references.
7. **Drift/loss risk:** force-geocoding a provider HQ, mixing user-location with model execution location, confusing entity association with materialised harm, treating country as legal applicability, or losing cross-border distinctions. Guard with opt-in validation, per-relation evidence and source-first Gate 2 adjudication.
8. **Why validator:** structural consistency, recognized country codes, unique identifiers, reference resolution and unknown-claim contradictions are machine-testable. Whether a source supports a specific relationship or which law applies is **not** machine-certified and belongs in source review or Section 04.
9. **Stop condition:** after Gate 1 tests, run corpus read-only. Any failures require an exact failure inventory and a separate maintainer decision. **Do not auto-repair canonical records.**

**Known validation limit:** the validator tests subdivision-code syntax and country prefix, not membership in a complete authoritative ISO 3166-2 subdivision registry. Do not advertise full ISO 3166-2 verification until such a registry and its version are maintained.

## Detailed design and Work execution handoff

The earlier Gate 2 checklist is an overview, **not the complete design specification**. These two documents are required reading before any substantive migration or renderer work:

1. [Gate 2 all-Incident transformation Work handoff](INCIDENT-CONTEXT-GATE2-WORK-HANDOFF-20261022.md) — exact read-only inventory, five pilot cases, Gate 2 stop, source-first migration, CI, per-record audit and cross-repository sequence.
2. [Case Files Incident Context and 3D globe UI/interaction design](https://github.com/CAM-Initiative/cam-governance-catalogue/blob/feat/vigil-case-files-dashboard-20261022/docs-internal/VIGIL-INCIDENT-CONTEXT-DASHBOARD-DESIGN-20261022.md) — five Stage 01 subsection layouts, independent relationship/scope chips, many-to-many counts, provenance/uncertainty display, cross-filter rules, source sync and detailed acceptance tests.

Both documents are implementation plans. The schema/validator are committed, but the full 200-record backfill and new website role chips are **not** yet implemented. Gate 2 approval must follow a source-first pilot before broad canonical edits.

## Gate 2 Work-thread contract (not yet executed)

1. Freeze/sync `agent/incident-ecosystem-ingestion` with the latest evidence and preserve any concurrent intake work and existing PR #155.
2. Review every canonical Incident's `source_records`, `system_context`, `jurisdictional_context`, and existing source-specific context. Prepare a per-Incident record containing *candidate* parties, roles, geographic scope, location codes, supporting `source_records[N]`, explicit unknowns, and uncertainty, without auto-applying guesses.
3. Perform a small evidence-grounded pilot including a geographically local case, a multi-country case, an actor/provider vs affected-service contrast, and a controlled evaluation of unknown location. Show original-to-new semantic crosswalks. Report any necessary schema amendments.
4. Obtain maintainer **Gate 2** approval after pilot review before mass-editing canonical Incidents. No new source records or occurrence diagnosis should be manufactured to satisfy completeness.
5. Migrate in bounded batches, preserve original strings verbatim, keep record versions/provenance coherent, run VIGIL suite. Report completed/unresolved per Incident; "not established" is a legitimate evidence-limited outcome, not missing intake work.
6. Extend `VIGIL.Incidents.Jurisdictions.Index.json` to project the **reviewed role-labelled canonical** relationships, then update the catalogue dashboard branch's globe with chips for: Occurrence, Affected services, Affected institutions/populations, Provider/Operator, Infrastructure, Regulatory context, and Unknown/Global. Hide unsupported coordinates; use representative country centers only as visualization.
7. Update the `cam-governance-catalogue` Stage 01 web and static/PDF outputs; follow the existing `vigil/MAINTAINERS.md` field-to-render contract. Do not accidentally change Section 04 findings.
8. Review all changed records and generated outputs, then update PRs. Do not merge without the maintainer's explicit instruction.

## Current provisional indexing

The existing `vigil/scripts/build-vigil-jurisdiction-index.py` can continue producing the **text-derived** geography index until source-reviewed canonical relationship data is available. Its single-country `anchor_country_code` is a conservative geographic association, **not** a Stage 01 canonical relational conclusion. Avoid combining or double-counting candidate derived geography with reviewed relationships in the UI.
