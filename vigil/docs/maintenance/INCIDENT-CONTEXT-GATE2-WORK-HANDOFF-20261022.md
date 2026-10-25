# VIGIL — Gate 2 Work handoff: all-Incident context transformation and catalogue dashboard integration
**Prepared:** 22 October 2026 · **Historical preparation status:** initially not started. **Canonical Gate 2 migration completed later** across all 200 Incidents (98 reviewed-and-recorded, 87 reviewed-unresolved, 15 reviewed-non-geographic). Working audits archived at Git commit `6eef70deabfcca007ab3fdd88d0dc98bb7c041dd`. Website integration is a separate catalogue-branch task and is not certified by this historical handoff. Canonical Incidents and `JURISDICTION-GEOGRAPHY-PROJECTION.md` are current authority.
**Approved Gate 1 branch:** `CAM-Initiative/Vigil` → `agent/incident-ecosystem-ingestion` (existing draft PR #155).
**Existing website branch:** `CAM-Initiative/cam-governance-catalogue` → `feat/vigil-case-files-dashboard-20261022`.
**Authoritative website design:** [VIGIL Case Files — Incident Context and relational globe design](https://github.com/CAM-Initiative/cam-governance-catalogue/blob/feat/vigil-case-files-dashboard-20261022/docs-internal/VIGIL-INCIDENT-CONTEXT-DASHBOARD-DESIGN-20261022.md). **Read it before designing UI.**
**Governance:** `AGENTS.md`, `vigil/AGENTS.md`, `vigil/MAINTAINERS.md`, `vigil/docs/maintenance/INCIDENT-CONTEXT-GATE1.md`, `vigil/VIGIL.Schema.json`, `vigil/scripts/incident_context_validation.py`.

## Goal

After separately approved Gate 2, transform **every active canonical Incident record** in the existing ingestion branch (baseline: 200 on 22 October 2026; enumerate actual current records when executing) into an evidence-grounded **Incident Context** dataset. Add source-linked `affected_party_context.entities[]` and `jurisdictional_context.normalized_geography` without changing the scope, history, narrative, provenance, taxonomy mapping, harm assessment, external requirement conclusions, record identity or chronological episode evidence. Derived data should power the redesign of the Case File's Stage 01 and the jurisdictional 3D globe with independent relationship and scope chips.

**Never claim "all records migrated" merely because the new optional fields exist.** Explicit unresolved or non-geographic conclusions may be the correct complete outcome. Track reviewed, supported, unresolved, not reviewed, ineligible and deferred distinctly; do not backfill invented facts to achieve coverage.

## Mandatory two-gate execution order

1. **Read and reconcile** all governed branch instructions and sources before any changes. Do not create a competing VIGIL or catalogue branch, reset concurrent ingestion work, force push, remove unique changes or merge to main. Preserve PR #155 as draft unless separately authorised.
2. **Inventory in read-only mode:** enumerate all current canonical Incident IDs; build the proposal matrix by comparing old and new fields, source-record citations, availability, context, actor/system roles, affected services and geographic descriptions. Record limits of evidence (unestablished ≠ not migrated). The 200-case 22 Oct snapshot is a baseline, not a maximum.
3. **Pilot without editing canonical Incidents:** create per-Incident reviewed candidate payloads and original-to-new crosswalks for **INC-090, INC-105, INC-187, INC-202, INC-040**, or substitute cases only with documented reason:
   - INC-090: Ukrainian occurrence/service relationship vs United States commercial provider; prevent provider HQ = event coordinates.
   - INC-105: Perth case vs attempted US legal referral; do not convert mentioned country into harm location.
   - INC-187: NSW service and external model/provider interaction; distinguish affected government service from execution location.
   - INC-202: not-established controlled evaluation; preserve unknown/non-geographic state.
   - INC-040: US, Singapore and China-linked entities; do not flatten a multi-country relationship to the first country.
   For each, show `source_records[N]`, exact relationship being asserted, what that source does/does not establish, proposed party and geography objects, and consequences for map semantics.
4. **Gate 2 checkpoint:** present the pilot, audited coverage, false-positive/ambiguity classes, genuine schema gaps, repair implications, and exact pass/fail delta to the human maintainer. **STOP.** Do not write 200 canonical payloads before explicit Gate 2 approval of their migration approach. Gate 1 approval did not authorize mass record repair.
5. **After Gate 2 approval**, write reviewed records in bounded batches, retaining original text/fields. Preserve source citations, evidence limitations, and date/version/provenance policy. For unresolved cases use the approved model without inventing an asserted country. Keep related IDs distinct from current source record refs; no fabricated refs. Run entire repository tests on every batch, maintain per-ID audit state. Reinspect any changed Incident under concurrent ingestion before writing.
6. **After stable canonical migration**, version and extend `vigil/scripts/build-vigil-jurisdiction-index.py` and its output with reviewed `normalized_geography` relations and party roles, preserving backward-compatible lexical projection with explicit provenance names. Join by Incident ID and record version, not guessed country strings. CI must reject stale or mismatched projections.
7. **Implement website design** on the EXISTING `feat/vigil-case-files-dashboard-20261022` branch (do not create a replacement). Read the referenced complete catalogue design, then implement Stage 01 Incident Context five subsections, 3D globe independent role/scope chips, many-to-many country filtering and distinct-Incident aggregation, accessible mobile/print/PDF paths, and role-aware evidence and uncertainty labels.
8. **Verify both repositories, preview and handoff.** Do not merge or publish to main without maintainer authorization. Update draft PR #155 with completion/provenance references, not a claim of human evidence authentication.

## Source-first field extraction and review logic

**Existing source fields remain authoritative.** Read `system_context` for technology/environment; `jurisdictional_context` for legacy text, secondary references and sector/regulatory surface; `source_records[]` and occurrence-specific analysis for evidence. Do not infer entity or event location from index `search_terms`, vendor brand, web domain, product availability, corporate headquarters, title, arbitrary place mention, model vendor or regulator headquarters.

For `affected_party_context.entities[]` populate local stable `PARTY-NNN` with:
- Exact, public-source-supported entity/population name (or generic kind without identifying unverified individuals), kind, one or multiple semantically evidenced party roles;
- `evidence_state` and a **specific source-bounded basis** explaining the role; `source_record_refs` correct at the Incident's local index.
- A participating actor/provider is not automatically an affected/harmed person. No harm status is deduced from party roles.

For `jurisdictional_context.normalized_geography` populate scope and `relations[]` with:
- Local stable `GEO-NNN`, distinct relationship role, source-evidence state and occurrence-specific basis, `source_record_refs`, location(s) and any defensible `party_refs`;
- Many-to-many: several different roles may be associated with the same country, and one role may be associated with several countries; do not derive directional connections unless separately evidenced;
- Use ISO 3166-1 alpha-2 country codes, optional correct subdivision code/locality only if evidenced; no GPS, guessed location, or automatic provider-corporate domicile relation;
- `unresolved` relation = no affirmative `locations`; distinguish no review, not established by evidence, non-geographic, global/multi-country and disputed/alleged associations in review inventory;
- `regulatory-context` indicates a potential area of governance *consideration*, not applicability, compliance finding, certification or legal opinion. Keep Section 04 authoritative;
- Source-reference integrity is checked structurally by validator; semantic source support still requires reviewer inspection.

## Canonical acceptance and migration inventory

Create an audit table for **every current Incident**:
`incident_id`, `record_version`, `old_primary_jurisdiction`, `old_secondary_jurisdictions`, `new_entities_status`, `new_geography_status`, `proposed_roles`, `proposed_country_codes`, `source_record_refs`, `evidence_limitations`, `human_review_needed`, `outcome`, `canonical_change_sha`.
Keep outcomes: `reviewed-and-recorded`, `reviewed-unresolved`, `reviewed-non-geographic`, `needs-specific-source`, `blocked-schema-gap`, `not-yet-reviewed`. Never use a silent empty object for a purported reviewed case.

Produce: baseline corpus coverage, category totals, pilot narratives, updated source-consistent schema/tests only if separately approved, per-batch record diff and index diff, global regressions, review packet and updated draft PR explanation. Respect permanent provenance and current dated audits rather than destructive rewrite.

### Stop/failure conditions

- If evidence does not support a claimed relationship: withhold assertion, mark source gap, never invent.
- If schema cannot represent a real event without conflation: present proposed **new Gate 1 amendment** and stop instead of adding uncontrolled fields.
- If ambiguous evidence or entity names risk identity/privacy errors: hold with source-limited status, do not infer identity.
- If a test failure suggests source prose movement, taxonomy/HIM change, loss of published evidence or validator-induced semantic drift: stop for maintainer decision.
- If a newly discovered Incident is admitted concurrently: preserve its work, include in updated inventory with appropriate status; do not overwrite or force-push.

## Web design and interaction contract (mandatory, not a future unspecified suggestion)

The companion catalogue design document linked above is normative for this Work task. Key acceptance points:
- Opened Case File Stage 01 title **Incident Context**, five subsections: Systems & Technology; Operational Environment; Affected Parties & Institutions; Geographic & Jurisdictional Context; Regulatory Context. Preserve existing Stage 01 summary/artefacts/evidence cards.
- Globe relationship chips and **separate** geographic scope chips with grounded counts. Distinct Incident counts; pin count sums may exceed unique matching Incident total for legitimately multi-country cases, label this.
- Preserve existing photorealistic Three.js Earth and 2D fallback, mobile access, severity doughnut, failure-class ranking, and advertising placement.
- Unreviewed source geography may be shown **only as labelled legacy context**, not as reviewed relationship pills/pins.
- Do not use site-local ad hoc country matching after reviewed structured data becomes the canonical published source. A version mismatch must not produce false geographic certainty.
- Keep all evidence states, source links and unknown location states visible; Stage 01 regulatory context never changes Section 04 applicability.

## PR and release control

The requested VIGIL branch carries the draft PR #155 and concurrent intake; the catalogue dashboard changes live on its own existing feature branch. Keep both draft/reviewable until explicit approval. Update maintainers crosswalk and generated documentation. A green CI run proves structural correctness only; it does not substitute for individual source adjudication or a visual browser review.
