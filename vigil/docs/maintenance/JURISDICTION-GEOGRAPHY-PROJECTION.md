# Jurisdiction geography projection — generated public dataset

**Status:** deterministic derived data contract, introduced 22 October 2026 on `agent/incident-ecosystem-ingestion`.

## Source of truth and boundaries

The sole authoritative source remains each Incident's existing `jurisdictional_context` block under `vigil/records/incidents/`. The generator `vigil/scripts/build-vigil-jurisdiction-index.py` produces `vigil/VIGIL.Incidents.Jurisdictions.Index.json`. It **does not** edit the canonical Incident, create evidence, adjudicate geography, modify taxonomy or Harm Impact, or determine regulatory/legal applicability. Original natural-language primary and secondary jurisdiction strings are preserved verbatim in the generated projection.

The derived dataset is **not** a new VIGIL record class or registry; it remains a view over INCs. The canonical schema and adjudication framework are unchanged. A proposal to add structured jurisdiction data directly to canonical Incident records requires a separate Gate 1 decision under the existing VIGIL maintenance contract.

## Consumer contract

Each projected `records[]` entry carries:

- `incident_id`, `record_version` to reconcile to a canonical Incident.
- `scope`: one of `single-country`, `multi-jurisdiction`, `cross-border`, `global`, `mixed-global`, `not-established`, `non-geographic`, or `unresolved`.
- `primary_jurisdiction_text`, `secondary_jurisdictions_text[]`: original canonical fields, not reinterpreted facts.
- `country_codes_mentioned[]`: lexical mentions using a conservative maintained country alias table (ISO 3166-1 alpha-2 identifiers). Mentions can reflect several *different relationships* and must not be converted to event or legal jurisdiction assertions.
- `anchor_country_code`: one country only if the primary jurisdiction names exactly one country and secondary fields do not name a second country; otherwise null.
- `subdivision_codes_mentioned[]`: ISO 3166-2 subdivisions identified only under a single, explicitly named country; omissions mean no supported code was extracted, not that the record contains no subdivision.
- `map_eligible`: whether a **representative country-level jurisdiction marker** may be displayed. This is **never** proof of an incident coordinate, jurisdiction of the harmed party, applicable law or where the system was operated.
- `source_fields[]`: exact original canonical field paths used; `evidence_review_status` is `source-field-derived-not-independently-verified`. This traceability is *not* a claim that external source records were re-reviewed.
- `requires_review`: a conservative normalization hold for geography that lacks an unambiguous single-country anchor, **not** a new VIGIL Incident adjudication status.

**Dashboard guidance:** Country pins and filtering must use only `map_eligible && anchor_country_code`. Always show unmapped, global and multi-jurisdiction cases as distinct meaningful categories, not as zeros and never as random lat/long markers. If geographic centroids are added on the website, they are presentation anchors for countries and must be labelled as such. Secondary subdivisions may support nested country/region filters but must not be treated as event origin or verified victim location.

The public projection only matches expressions actually present in canonical jurisdiction fields. It deliberately does not infer location from company headquarters, service availability, source publisher, a domain, a cloud-region label, source search terms, or the case title. Conflicting/nested roles in primary versus secondary fields remain review candidates.

## Deterministic updates

Run:

```bash
python vigil/scripts/build-vigil-jurisdiction-index.py
python vigil/scripts/build-vigil-jurisdiction-index.py --check
python vigil/tests/test_jurisdiction_projection.py
```

The `VIGIL records` workflow builds and tests the projection with the rest of the canonical Incident pipeline. On the dedicated ongoing ingestion branch, the workflow commits *only this generated geography index* on successful push validation, leaving canonical and taxonomy/source records untouched. On `main`, it is included in the already-authorized generated-index commit step. PRs require the derived index to match the source.

## Next phase: source-level relationship adjudication (separate Gate 1)

The current projection standardizes text without asserting why each jurisdiction is relevant. For robust institutional analytics, a future additive canonical schema proposal should separate **event location**, **affected institution**, **affected population**, **provider/operator location**, **data infrastructure**, and **regulatory applicability**, each with role, evidence/source references, uncertainty and review provenance. That migration must independently review ambiguous cases and shall not automatically transform source-field mentions into confirmed facts. The dashboard can use the current projection immediately for conservative jurisdiction filtering without waiting for the full semantic migration.

## Subsequent Gate 1 relationship model

The 22 October opt-in canonical schema now permits `affected_party_context.entities[]` and `jurisdictional_context.normalized_geography.relations[]` with source-linked geographic roles. This **does not** upgrade the existing deterministic *text-derived* geo index to an independently reviewed set of event locations. Continue conservative filtering until a separately approved Gate 2 record-by-record evidence review, new canonical relationship projection and catalogue renderer update. See `vigil/docs/maintenance/INCIDENT-CONTEXT-GATE1.md`.

## Version 2 — source-linked canonical relationships

Following Gate 2 approval on 22 October 2026, the same deterministic builder publishes `schema_version: 2.0.0`. Each entry retains its Incident ID and current record version. `projection_status: reviewed-canonical` means the optional canonical context was reviewed and recorded; it does not mean independent human verification or that every location is known.

`scope`, `relations`, `parties` and `reviewed_country_codes` come from canonical structured context. Relations preserve roles, locations, evidence states, bases and source/party references. The builder checks the existing Incident Context contract, including source references, and rejects duplicate Incident IDs. `--check` rejects stale outputs. Country totals count distinct Incidents, not relations, sources or affected people.

The complete v1 lexical result is retained under `legacy_text_projection`. Original jurisdiction text and lexical mention fields remain for compatibility, but are not reviewed geography. A reviewed entry has no v1 `anchor_country_code`: consumers must use role-filtered relations. An explicit unknown never falls back to legacy text. Entries without structured context remain `legacy-text-derived` and must not be shown as reviewed pins.

Supported, attributed and disputed relationships may receive representative country-centroid anchors with their evidence label. Unresolved relations have no locations. A country anchor is not a physical event coordinate. Country counts can sum above the distinct matching Incident total. Scope and role are independent filters; provider location never substitutes for occurrence location. Regulatory context is not a legal applicability finding.

Consumers must join ID and record version from the same source branch. A mismatch is unavailable/unsynchronised geography, not zero incidence. Canonical records remain the source for full evidence and assessment text.
