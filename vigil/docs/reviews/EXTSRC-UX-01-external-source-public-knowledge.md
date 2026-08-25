# EXTSRC-UX-01 — External Source Public-Knowledge and Review-Freshness Repair

## Scope and boundary

- Review date: 2026-08-24
- Repository scope: VIGIL only
- Starting canonical head: `e3d1dcb12875642c71ca3100b43b6d63872bf69a`
- Working branch: `agent/extsrc-ux-01`
- Human governance role: Dr Michelle Vivian O’Rourke — contract approver
- Substantive human review: not established
- Human source verification: not established

This pass repairs the external-source registry as a public governance-knowledge resource. It does not amend the public catalogue website, assess CAM/Caelestis coverage, create external requirements from metadata, or reproduce controlled standards text.

## Migration results

| Measure | Result |
| --- | ---: |
| Registered source versions reviewed | 81 |
| Distinct external source identities | 80 |
| Source versions with new `public_summary` | 81 |
| Source versions with structured AI-governance themes | 81 |
| Source versions with structured lifecycle stages | 81 |
| Source versions with `relevance_scope` | 81 |
| Source versions with `last_substantive_reviewed` | 81 |
| Source versions review-due at completion | 0 |
| Source versions without public clause records prioritised and summarised | 63 |
| Source versions lacking evidence for a bounded public summary | 0 |
| Source versions lacking sufficient evidence for detailed normative interpretation | 38 |

The 38 detailed-interpretation limitations comprise 37 `blocked-access` primary sources and IEEE 7003-2024, for which primary access is recorded but analytical extraction has not started. These sources still have bounded public summaries based on official publisher material; no inaccessible clause content was inferred.

## Contract changes

The source-registry schema advances from `1.0` to `1.1` and adds:

- `public_summary`;
- `ai_governance_relevance`;
- `applicable_lifecycle_stages`;
- `relevance_scope`; and
- `last_substantive_reviewed`.

The theme and lifecycle fields reuse the controlled vocabularies already maintained by the external-requirements schema. `notes` remains optional internal curation/provenance metadata and is not a public description.

The source manager now preserves public-knowledge fields and the last substantive-review date during ordinary ingestion. An unchanged metadata observation preserves the prior disposition. A material source-metadata change reopens `review_state` but does not reset `last_substantive_reviewed`, because change detection is not substantive reassessment.

## Review freshness

A review-eligible source becomes review-due when more than 90 days have elapsed since `last_substantive_reviewed`. Review freshness is calculated independently of `first_seen`, `last_seen`, source polling, metadata fingerprints and generated-file timestamps.

Review-due sources enter the generated source-review queue with `required_action: substantive-reassessment`. Validation also emits a review-due warning. Missing or malformed substantive-review dates on active sources remain errors.

## Public narrative assurance

Validation requires meaningful public summaries, valid controlled vocabularies, substantive scope statements and ISO-format review dates for active sources. It checks narrow contextual patterns for project-specific corpus language, repository workflow language and maintainer tasking. It does not apply a naive global word blacklist; legitimate public discussion of review or governance remains permitted.

The migration populated every summary source-by-source. Directly analysed public or licensed primary sources support fuller descriptions. Metadata-only sources state their actual subject and AI-governance contribution while expressly preserving the boundary against unseen normative clauses. Internal `notes` were retained unchanged and were not used as canonical public copy.

## Remaining interpretation boundaries

1. Thirty-seven primary standards remain `blocked-access`; official metadata supports bounded summaries, not clause-level requirements.
2. IEEE 7003-2024 remains `not-started` for analytical extraction despite recorded primary-source access.
3. The consolidated EU AI Act extraction remains `partial`; specialist legal analysis is still needed for specialised sectoral, institutional, market-surveillance, enforcement and penalty provisions and the consolidated effect of 2026 amendments.
4. The original July 2024 EU AI Act text remains preserved as a superseded historical source version; current interpretation should use the applicable consolidated text.
5. Eleven licensed IEEE source versions were described from lawful primary-text analysis without reproducing copyrighted source text.
6. Context-only and supporting-only sources provide bounded comparative or cross-cutting knowledge and are not represented as comprehensive AI conformance baselines.

## Validation result

The external-source registry, generated source catalogue and generated review queue validate with 81 source versions and zero review-required or review-due entries at completion. External-requirement, CAM-assessment and authorship-provenance validation remains part of the final repository validation run.
