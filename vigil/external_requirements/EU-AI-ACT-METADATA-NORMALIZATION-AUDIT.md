# EU AI Act Metadata Normalization Audit

Date: 2026-08-26

Scope: staged semantic re-extraction of Regulation (EU) 2024/1689 consolidated to 27 July 2026, Articles 4a and 9–15.

## Purpose

Normalize source-explicit requirement metadata before canonical migration so that actor, governed object, timing, required artefact/output, evidence expectation, verification method, applicability and qualifications are machine-readable where the source actually supplies those semantics.

This pass does **not** manufacture generic audit evidence, implementation controls or documentary outputs that the Regulation does not itself require or necessarily produce.

## Baseline

The staged re-extraction currently replaces eight coarse article-level EXTREQ records with 102 deterministic candidate requirements.

The semantic decomposition was already substantially populated for `applicable_actor`, `governed_object`, `lifecycle_stage`, `applicability_conditions` and `exceptions_or_qualifications`. The principal normalization gaps were explicit timing conditions and source-required documentary/log outputs or assessable material that remained only in requirement prose.

## Normalization mechanism

Added:

`vigil/external_requirements/reextractions/EU-AI-ACT-2026-07-27-metadata-normalization.json`

The overlay is keyed by immutable candidate `requirement_id` and may modify only:

- `applicable_actor`
- `governed_object`
- `lifecycle_stage`
- `evidence_expectation`
- `timing_or_frequency`
- `required_artefacts`
- `verification_method`
- `applicability_conditions`
- `exceptions_or_qualifications`

The EU AI Act migration script applies the overlay before constructing canonical EXTREQ records and rejects:

- unsupported override fields;
- override IDs that do not correspond to staged requirements;
- deterministic-ID drift;
- duplicate or colliding replacement IDs.

## Source-explicit corrections added

18 staged requirements currently receive normalization overrides.

Representative corrections include:

- Article 4a(1)(c): access documentation is now represented as a required artefact/evidence surface rather than only appearing in prose.
- Article 9(1): the expressly documented risk-management system is represented as evidence material.
- Article 9(8): prior-defined metrics and probabilistic thresholds are represented with their pre-testing timing relationship.
- Article 11(1): technical-documentation creation, currency, compliance-demonstration and Annex IV content are represented as explicit evidence/output metadata.
- Article 12(3): mandatory logging outputs are represented as evidence expectations; Article 12(3)(a) also carries the `for each use` timing condition.
- Article 13(2): the instructions-for-use output and its source-defined quality criteria are represented as an evidence surface.
- Article 14(1): the during-use oversight period is represented explicitly in timing metadata.
- Article 14(3)(a) and (b): the pre-market / pre-service timing condition is represented explicitly rather than only in prose and lifecycle classification.
- Article 14(5): separate verification must occur before deployer action/decision, and the two-person verification mechanism is represented explicitly while preserving the statutory disproportionality exception.
- Article 15(3): accuracy-level and metric disclosure in the instructions for use is represented as evidence/output metadata.
- Article 15(4): the post-market continuing-learning condition is represented explicitly as timing/applicability metadata.

## Guardrails

The pass follows these rules:

1. Do not treat every governance duty as requiring a document.
2. Do not populate `evidence_expectation` solely because evidence would be desirable to an auditor.
3. Do not convert system capabilities into `required_artefacts` unless the source requires a document, log, record, form or other output.
4. Where the source states timing, repeat it in `timing_or_frequency` even if the prose summary already contains it.
5. Keep statutory exceptions and scope qualifications in dedicated machine-readable fields.
6. Preserve source-defined permissions as permissions rather than turning them into duties.

## Regression contract

`vigil/scripts/test_eu_ai_act_reextraction.py` now:

- excludes the metadata overlay from the staged-package glob;
- confirms all 102 candidate IDs remain deterministic and unique;
- confirms every metadata override targets an existing staged candidate;
- checks representative timing, artefact, evidence and verification normalizations;
- retains the eight coarse-record retirement contract.

## Status

The Article 4a and 9–15 candidates remain staged migration candidates. This normalization pass improves the metadata contract but does not by itself mark the EU AI Act source `fidelity-assured` or canonically migrate the replacement records.

Canonical migration should occur only after the full staged package and validators can be run together from a repository checkout.
