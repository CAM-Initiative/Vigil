# Section 03 explanation completion — 18 October 2026

Status: explanation-only implementation and bounded repair; substantive follow-ups remain held.

Baseline: canonical branch `work/incident-taxonomy-reasoning-readjudication-20261018`, `42b631d`. It contains current `main` (83 unique commits, none behind at fetch). No wider readjudication resumed. The user expressly authorised corpus explanation inspection and bounded basis-only batches.

## Result

194 canonical Incidents and 458 actual primary/secondary mappings inspected. 441 explanations retained as satisfactory for this presentation task; 14 mapping-local bases improved across 11 Incidents; three held unchanged. Zero empty mapping bases. 456 mappings have explicit canonical episode relationships; two do not. All linked episodes have stable IDs and source refs.

“Satisfactory” means the existing explanation identifies an occurrence and mechanism and adequately communicates its recorded role for this focused review. It does not certify fresh source authentication, exhaustive recognition testing, historical taxonomy equivalence or correctness of every existing adjudication. Existing source packets, mapping bases and episode rationales are the evidence boundary; no fresh original-source inspection is claimed. Short text is not automatically defective. No automated semantic pass/fail rule was introduced.

## Reproduction and preservation

Run `python vigil/docs/reviews/2026-10-18-section03-completion/inventory.py` from the repository root. `inventory.json` records every existing mapping, its basis, role, confidence, recorded version, admitted episode relationships, source refs and explanation disposition. It also inventories all records with no mapping. This is a dated audit of admitted selections, not a canonical Incident × class matrix.

`basis-changes.json` preserves exact before/after text, baseline, role, confidence and supporting episode/source identities for all 14 edits. `reference-criteria.json` pins the relevant current taxonomy definitions, conditions and exclusions. Current reference is 0.7.0; recorded adjudication versions are preserved and are not silently upgraded or treated as equivalent.

Only mapping-local `classification_basis` changed in the 11 records. A full JSON comparison excluding those exact paths confirms every other canonical value is unchanged: membership, roles, confidence, aggregate bases, source evidence, episode rationales, independent external assessments, requirement outcomes, HIM, record identity and prior interpretive provenance. This review is AI-authored by OpenAI ChatGPT Work / Codex; it does not imply human source verification. Generated indexes and taxonomy examples were rebuilt with the existing builder. Those outputs also reconcile previously stale branch projections of earlier authorised repairs; they were not hand-edited.

The batches are: (1) INC-003/034/095 mixed notification and decisive control limits; (2) INC-154/155/159/160/168/173 authority, reliance and reconstruction specifics; (3) INC-190/191 distinguish the Canadian and US request sequences.

## Representative changes

- INC-003 / Governance Signal Delivery: before, only missed warning delivery; after, retains those failures and explains the later credential notification, prior rotations and bounded affected-party disposition. E001/E015/E019 remain different episode outcomes. The already-repaired aggregate synthesis is unchanged.
- INC-154 / Control-Plane Authority Separation: before, “A fabricated board document became operative management control state”; after, identifies purported Slack directors, displaced CEO approval authority, the resulting control-state change and unavailable full exchanges.
- INC-190/191 / Objective–Pathway Authority Separation: before, identical public-retrieval/exploit-parameter wording; after, distinguishes Canadian divorce-record probes from US school-statistics/state-parameter activity and states source-authentication and outcome limits.

No supported VIGIL divergence was removed in these edits. INC-001/002/004/006's latest repaired explanations are retained. INC-126 retains its single successful-invariant mapping. INC-129 currently has six Boundary mappings and a disputed status, **not the older mixed-role configuration**; regression checks must use this current canonical state. Mixed-role behaviour is exercised with INC-001/003/004 instead.

## Held substantive concerns

- [Issue #138](https://github.com/CAM-Initiative/Vigil/issues/138): INC-197 / FC-086 and INC-198 / FC-087 lack explicit admitted episode relationships. The renderer must disclose that gap, not invent links by topic. A separate approved evidence/relationship disposition is proposed.
- [Issue #139](https://github.com/CAM-Initiative/Vigil/issues/139): INC-194 / FC-049 does not identify the decisive material impairment of independent choice or disengagement. Locate that evidence in the existing evaluation or propose a criterion-grounded Boundary disposition. No polarity change made here.

Searches for the record numbers, Grok, Engagement Autonomy, source episodes and Section 03 found no matching bounded issues before creation. Existing #128 tracks general chronology/presentation work, and #133 concerns a different no-mapping class-fit cohort. No emails, PR, merge to main or deployment authorised or performed.

## Validation

- Canonical record validation: 194 passed.
- Public record validation: 194 passed.
- Source provenance: 711 active source records passed.
- Interpretive provenance, system components, authorship and occurrence-requirement validation: passed.
- Taxonomy validator: 16 families / 79 classes passed in working-branch mode.
- Full unittest discovery: 280 tests passed. First attempt lacked the local `jsonschema` dependency; installed it and reran successfully. Expected invalid-fixture messages in test output are not corpus failures.
- Build: existing canonical public builder completed. Generated output changes are expected; no builder, validator, schema or permanent canonical test changed.

Website build, static output and browser/PDF verification are recorded in the companion website branch's Section 03 review. This canonical tranche is reviewable; the three held mappings are not certified resolved by presentation repairs.

Artefact classification: Incident JSON = LIVE; builder outputs = GENERATED; this directory, inventory and pinned criteria = AUDIT; no new runtime authority or permanent semantic validator.

Canonical basis batches: `245bc65`, `3936b18`, `b8d0513`. The normal website publication build follows its configured canonical `main` source (465 mappings). Browser acceptance substitutes this adjudication branch's exact local payloads (458 mappings), so the newer repaired wording and preserved current roles are tested without changing production source selection or deploying unmerged canonical work.

Git transport could not authenticate writes. The selected GitHub connector publishes identical basis changes as bounded commits `177ea2e883aab56f2c896c78e20688c4a77bdec6`, `31c377a54a1b136e999db8f2cb656ea64b23d4f1` and `85afdd443d6078b2ed2fb7e670204060fb20b8dc`, preserving the existing remote branch ancestry with a guarded non-forced ref update. The shorter hashes above identify local validation checkpoints, not published commit identities.
