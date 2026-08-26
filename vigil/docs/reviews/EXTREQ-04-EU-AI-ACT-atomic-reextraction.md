# EXTREQ-04 — EU AI Act Atomic Re-extraction

## Review date

2026-08-26

## Working branch

`agent/failure-taxonomy-prototype`

## Authoritative source

Current review target: Regulation (EU) 2024/1689 as consolidated on 27 July 2026, CELEX `02024R1689-20260727`, including the amendments made by Regulation (EU) 2026/1744.

Authoritative locator used for this review:

`https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727`

The consolidated EUR-Lex text is used as the review instrument. Its own legal notice states that the consolidated text is a documentation tool; authentic acts published in the Official Journal remain the legal source of record.

## Repair objective

Replace article-level analytical compression with independently assessable propositions while preserving:

- actor scope;
- modality;
- applicability and exceptions;
- source-defined compound structure where appropriate;
- 2026 amendment effects;
- deterministic EXTREQ identity; and
- explicit retirement relationships for superseded coarse analytical identities.

This work does **not** mark the EU AI Act fidelity-assured. The source remains `requires-reextraction` / effectively partial until the represented operator-facing scope has been reviewed under the source-fidelity methodology and the staged migrations have passed the full corpus validators.

## Article 10 — repaired candidate

The existing record `EXTREQ-09AD2F5442A55B55` (`data-governance`) represents the whole of Article 10 as one requirement. That is materially lossy.

The staged replacement package now separates Article 10 into 16 deterministic candidate requirements covering:

- the amended Article 10(1) dataset-quality basis and its Article 4a(1) cross-reference;
- the overarching Article 10(2) requirement for data-governance practices appropriate to intended purpose;
- each Article 10(2)(a)-(h) governance practice;
- separately assessable Article 10(3) relevance, representativeness, error, completeness and statistical-property criteria; and
- Article 10(4) contextual-setting suitability.

Article 10(6) is preserved as an applicability qualification on Article 10(2)-(4), rather than misrepresented as a standalone operational duty.

## Article 13 — repaired candidate

The existing record `EXTREQ-126CB22D1FF08066` (`transparency-instructions`) compresses Article 13(1)-(3) into one requirement.

The staged replacement package now separates Article 13 into 16 deterministic candidate requirements covering:

- operational transparency for interpretation and appropriate use;
- the source-defined quality criteria for instructions for use;
- provider/representative identity information;
- each Article 13(3)(b)(i)-(vii) information class;
- pre-determined changes;
- human-oversight measures;
- computational/hardware resources;
- expected lifetime;
- maintenance/care measures and frequency; and
- log collection/storage/interpretation mechanisms.

Where one source point intentionally groups a set of attributes into one named information duty, the record remains a `source-defined-compound` and its constituent propositions are explicitly enumerated rather than silently compressed.

## Article 4a — repaired candidate

The 2026 amendment inserted Article 4a and the existing record `EXTREQ-F30E6B9A906370B9` compresses materially different permissions, actors and safeguards.

The staged replacement package now separates Article 4a into nine deterministic candidate requirements:

- the exceptional Article 4a(1) permission for providers of high-risk AI systems;
- each mandatory Article 4a(1)(a)-(f) condition/safeguard;
- the separate Article 4a(2)(a) permission for providers/deployers of other systems/models and deployers of high-risk systems; and
- Article 4a(2)(b)'s incorporation of all paragraph 1 safeguards.

The paragraph 2 statement that it creates no obligation to conduct bias detection or correction is preserved as a qualification rather than lost.

## Current migration state

Three coarse canonical identities are staged for retirement:

- `EXTREQ-F30E6B9A906370B9` — Article 4a;
- `EXTREQ-09AD2F5442A55B55` — Article 10; and
- `EXTREQ-126CB22D1FF08066` — Article 13.

They are replaced by 41 deterministic candidate identities across the two re-extraction packages.

The canonical `requirements.json` has **not** been rewritten through the connector merely to make the branch appear finished. The migration script `vigil/scripts/migrate-eu-ai-act-atomic-reextraction.py` performs the retirement/replacement transaction against the full local corpus and is designed to be followed by the normal external-requirements build, generated-output validation and source-fidelity validation.

This is intentional: semantic identity replacement should be atomic and validator-backed, not performed by partial manual edits to a large canonical JSON file.

## Validation additions

`vigil/scripts/validate-external-requirement-fidelity.py` now validates staged re-extraction packages for:

- source/version resolution;
- retired-identity ownership;
- deterministic replacement IDs;
- cross-package duplicate IDs;
- permitted semantic-atomicity states; and
- constituent-proposition presence for source-defined compounds.

`vigil/scripts/test_eu_ai_act_reextraction.py` adds a focused regression contract for the current three-to-forty-one migration.

## Next source blocks

The next EU AI Act re-extraction pass should remain within the highest-value operator/control surface before moving into institutional and enforcement architecture:

1. Article 9 — risk management system;
2. Articles 11 and 12 — technical documentation and record-keeping;
3. Articles 14 and 15 — human oversight, accuracy, robustness and cybersecurity;
4. Articles 16-27 — provider, authorised-representative, importer, distributor and deployer duties, including fundamental-rights impact assessment; and
5. Articles 43, 49, 50, 53, 55, 72, 73 and 86 — conformity, registration, transparency, GPAI, post-market/incident and affected-person rights.

Each block should be checked against the 27 July 2026 consolidated text because Regulation (EU) 2026/1744 materially altered applicability and selected substantive provisions.
