# Gate 1 — supporting international governance requirement extraction

Classification: REVIEW. Date: 11 October 2026. Status: **approval required; control changes not implemented**.
Baseline: `6192d5d4b66c6d8bb9fbf9e86347e8f0b56e7866`.
AI-authored review under the explicit source-registration instruction. No substantive human review or source verification is claimed.

## Current behaviour

`manage-external-requirements.py:validate_requirements` rejects every requirement whose source scope role is not `primary-ai-governance`. `validate_scope` requires `supporting-external-authority` to use `supporting-only`; requirements are forbidden in that state. The source-fidelity methodology also treats supporting sources as outside first-class extraction.

The requirement schema exposes a supporting role, but the manager cannot admit its extraction. Thus source registration is possible, while source-faithful treaty requirements are blocked. Assigning `primary-ai-governance` merely to evade this guard would misrepresent these instruments.

The `normative_force` enumeration includes binding law, regulatory requirements, government voluntary frameworks and technical/industry standards. It has no precise category for a mixed State/Movement conference resolution or a Security Council resolution containing different operative modalities. None of these should be labelled an industry standard or treated uniformly as binding treaty law.

## Proposed bounded behaviour

Approve a separate implementation to:

1. Permit source-reviewed requirements from `supporting-external-authority`, initially for the registered treaty, intergovernmental-principle and resolution source classes in this work package. Preserve `primary-ai-governance` unchanged. Keep `context-or-discovery` and `excluded-from-current-scope` ineligible. Keep institutional research and legal commentary reference-only, without enforceable requirements.
2. Permit eligible supporting sources to record `partial` or `complete` extraction alongside the existing `supporting-only` registration state. Retain actor, source access, known unreviewed sections and explicit incomplete-review action guards. `supporting-only` remains a zero-requirement state. Extend source-fidelity assessment to an extracted supporting source rather than automatically calling it not applicable.
3. Add precise `normative_force` categories `non-binding-intergovernmental-principles`, `non-binding-conference-resolution` and `international-resolution`. The last category describes the instrument form, not uniform binding effect. Use clause posture, actor, conditions and qualifications to preserve demand/reminder, condemnation and exhortation. Treaty provisions continue to use `binding-law`, subject to party, force and jurisdiction conditions.
4. Align the schema, manager, generic isolated-fixture tests, fidelity checks, documentation and public projection/resolver vocabulary. Preserve the existing occurrence assessment route and Aligned / Not aligned / Boundary labels. Audit downstream website recognition of added categories before publishing any Incident row.

## Pass/fail delta

| Example | Now | After approved implementation |
| --- | --- | --- |
| Reviewed Outer Space Treaty VI supervision proposition, supporting source, partial extraction, valid State-party conditions | Rejected by role/status guards | Admitted structurally; occurrence relevance still separately assessed |
| Reviewed UNGP company due-diligence proposition with precise non-binding principles category | Rejected by role/status and force vocabulary | Admitted structurally; no automatic finding or adoption gate |
| Requirement reconstructed from the ICRC 2024 abstract or inaccessible treaty text | Rejected | Still rejected |
| Treaty relabelled as an AI-specific rule to bypass the guard | Semantically wrong despite possible structural acceptance | No such relabelling needed or authorised |
| An unreviewed commentary or discovery source used as enforceable law | Rejected | Still rejected |

## Affected surface and corpus impact

Affected: external source scope/status validation, canonical requirement schema and manager, source-fidelity methodology/checks, source coverage projections, metadata review, resolver/public projection vocabulary, and website Section 04 normative-force display. The taxonomy invariants, Incident evidence, HIM and classification contracts do not change.

This branch adds 13 supporting source versions and **zero requirements**. The existing 1,102 requirements and canonical Incident assessments are unchanged. Initial implementation must be limited to this package; broader impact of any generic guard alteration is not yet measured. Run the revised controls read-only and report exact failures before any repair. Gate 2 applies separately to broad semantic repairs.

## Repair and information-loss implications

No corpus rewrite is authorised. Newly reviewed requirements will need normal deterministic ID allocation, source/version shards, exact source conditions, metadata-fidelity decisions and independent relationship review. Existing sources are not automatically promoted to extraction-complete. Missing civilian impacts, State attribution or party applicability must remain explicit. Do not suppress these qualifications to obtain passing data or a populated Compliance section.

The guard belongs in the manager because it currently enforces source-role eligibility across the corpus. Schema and renderer changes alone cannot make canonical supporting requirements valid. Public display additions must follow canonical metadata without selecting alignment polarity.

## Stop condition and approval requested

Under `vigil/MAINTAINERS.md`, **Gate 1 — approval before changing the control**: “No semantic validator/schema/test change may be implemented until the human maintainer explicitly approves that described behaviour.” The handoff repeats this stop condition.

Approve the bounded behaviour above before any schema, validator, permanent-test, builder or publication-guard change. This PR contains source registrations and review evidence only. Do not extract canonical requirements, allocate provisional EXTREQ IDs, admit FC relationships or insert INC-090 Section 04 rows until the approved controls and source-fidelity checks pass.
