# EXTREQ-04 — EU AI Act Atomic Re-extraction

## Review date

2026-08-26

## Working branch

`agent/failure-taxonomy-prototype`

## Authoritative source

Review target: Regulation (EU) 2024/1689 as consolidated on 27 July 2026, CELEX `02024R1689-20260727`, including Regulation (EU) 2026/1744 amendments.

Authoritative review locator: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727`

The consolidated EUR-Lex text is a documentation tool; authentic acts published in the Official Journal remain the legal source of record.

## Objective

Replace article-level analytical compression with independently assessable propositions while preserving actor, modality, applicability, exceptions, source-defined compounds, amendment effects, deterministic identity and explicit retirement relationships.

The EU AI Act remains `requires-reextraction` / effectively partial. Staging a repaired block is not a source-level fidelity-assurance finding.

## Article 4a

The 2026 amendment inserted Article 4a. Existing `EXTREQ-F30E6B9A906370B9` merges two different exceptional processing permissions, different actor scopes and six mandatory safeguards/conditions.

The staged package replaces it with **9 deterministic candidates** covering the Article 4a(1) permission, each Article 4a(1)(a)-(f) safeguard/condition, the separate Article 4a(2)(a) permission and Article 4a(2)(b)'s incorporation of paragraph 1 safeguards. The express statement that Article 4a(2) creates no duty to conduct bias detection/correction is preserved as a qualification.

## Article 9

Existing `EXTREQ-44B7BB17CB030468` compresses the complete risk-management architecture into one article-level abstraction.

The staged package replaces it with **22 deterministic candidates**, separating:

- establishment/implementation/documentation/maintenance of the risk-management system;
- continuous lifecycle operation and review;
- each Article 9(2)(a)-(d) process step;
- interaction among Section 2 requirements;
- hazard-level and overall residual-risk acceptability;
- the risk-control hierarchy in Article 9(5)(a)-(c);
- deployer capability/context consideration;
- distinct testing purposes in Article 9(6);
- optional real-world testing under Article 9(7);
- development-stage, pre-market and metrics/threshold testing rules under Article 9(8);
- children/vulnerable-group consideration; and
- sectoral risk-process integration under Article 9(10).

Article 9(3) is preserved as a scope qualification on the relevant risk propositions rather than invented as an operational duty. The 2026 Article 2(13) limitation mechanism is also flagged because it can affect Articles 9-15 for specified Article 6(1) systems only under its statutory conditions and delegated-act mechanism.

## Article 10

Existing `EXTREQ-09AD2F5442A55B55` represents Article 10 as one requirement. The staged package replaces it with **16 deterministic candidates** covering the amended Article 10(1) dataset-quality basis and Article 4a(1) cross-reference, the Article 10(2) overarching governance criterion and points (a)-(h), separate Article 10(3) quality criteria, and Article 10(4) contextual suitability.

Article 10(6) is preserved as an applicability qualification on Article 10(2)-(4).

## Article 13

Existing `EXTREQ-126CB22D1FF08066` compresses Article 13(1)-(3). The staged package replaces it with **16 deterministic candidates** covering operational transparency, instructions quality, each prescribed Article 13(3) information class, pre-determined changes, human oversight, compute/hardware resources, lifetime, maintenance and logging mechanisms.

Source points that intentionally group attributes remain `source-defined-compound`; their constituent propositions are explicitly enumerated.

## Current migration state

Four coarse canonical identities are staged for retirement:

- `EXTREQ-F30E6B9A906370B9` — Article 4a;
- `EXTREQ-44B7BB17CB030468` — Article 9;
- `EXTREQ-09AD2F5442A55B55` — Article 10; and
- `EXTREQ-126CB22D1FF08066` — Article 13.

They are replaced by **63 deterministic candidate identities** across three re-extraction packages.

The canonical source/version shard has not been partially hand-edited through the connector. `vigil/scripts/migrate-eu-ai-act-atomic-reextraction.py` discovers the staged EU AI Act packages, verifies source fingerprints and retired identities, expands the candidates into canonical EXTREQ shape, performs deterministic-ID/collision checks, and writes the replacement transaction through the shared sharded-corpus I/O layer before regenerating `requirements.json`.

That migration must then be followed by the normal external-requirements build, generated-output validation and source-fidelity validation. This preserves the identity transaction as an atomic validator-backed operation.

## Validation

`validate-external-requirement-fidelity.py` now checks staged packages for source/version resolution, retired-identity ownership, deterministic IDs, cross-package duplicates, semantic-atomicity states and constituent-proposition preservation.

`test_eu_ai_act_reextraction.py` asserts the current **4 coarse → 63 candidate** contract.

## Next source blocks

Continue through the remaining core high-risk controls before broader operator and enforcement architecture:

1. Articles 11 and 12 — technical documentation and record-keeping;
2. Articles 14 and 15 — human oversight, accuracy, robustness and cybersecurity;
3. Articles 16-27 — provider, representative, importer, distributor and deployer duties, including fundamental-rights impact assessment; and
4. Articles 43, 49, 50, 53, 55, 72, 73 and 86 — conformity, registration, transparency, GPAI, post-market/incident and affected-person rights.

Every block must be checked against the 27 July 2026 consolidated text rather than assumed unchanged from the original 2024 Act.
