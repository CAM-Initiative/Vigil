# VIGIL severity-schema alignment audit

**Review date:** 2026-09-16  
**Repository branch:** `chore/remove-aeon-governance-lab-public-references`  
**Starting branch HEAD:** `e1aae79bca3cbba7d1666da365414671085930d6`

## External alignment

The MIT AI Incident Tracker states that it classifies AI Incident Database reports by harm severity using a rating system based on CSET's AI Harm Taxonomy. Its Harm Taxonomy page publishes an ascending scale from 1 (Negligible) to 5 (Catastrophic). The June 2026 methodology update also treats harm severity as an ordinal low-to-high classification and reports that reviewers applied the same written criteria to the evidence contained in incident reports.

CSET's July 2023 *Adding Structure to AI Harm* is the underlying harm-framework source. It distinguishes realised harm events from potential harm issues, separates tangible and intangible harm, and supports documented customisation. The paper identifies severity and spread as future framework features; it does not itself establish MIT's later five-level severity rubric.

VIGIL therefore aligns only the direction and general ordinal legibility of its five-level scale. It does **not** claim that VIGIL severity is identical to, interchangeable with, or directly derived from MIT/CSET. VIGIL retains deterministic occurrence-level criteria for evidence-to-repair analysis and does not import CSET harm categories into the VIGIL Failure Taxonomy.

Canonical references:

- MIT AI Risk Initiative, [AI Incident Tracker](https://airisk.mit.edu/ai-incident-tracker)
- MIT AI Risk Initiative, [Harm Taxonomy](https://airisk.mit.edu/ai-incident-tracker/harm-taxonomy)
- MIT AI Risk Initiative, [AI Incident Tracker June 2026 Update](https://airisk.mit.edu/blog/ai-incident-tracker-june-2026-update)
- Mia Hoffmann and Heather Frase, CSET, [Adding Structure to AI Harm: An Introduction to CSET's AI Harm Framework](https://cset.georgetown.edu/wp-content/uploads/20230022-Adding-structure-to-AI-Harm-FINAL.pdf) (July 2023)

## Pre-migration implementation audit

The authoritative definitions were in `vigil/VIGIL.Schema.json` and `vigil/docs/incident-severity-standard.md`. Every canonical Incident contained a structured `severity_assessment`; the Incident template, validator, tests and public-index builder relied on those fields. Generated outputs projected the canonical code without reinterpreting it.

The previous scale was descending: lower numbers meant greater materialised harm. The VIGIL validator's adjacency map was ordinal but direction-neutral. No VIGIL builder or validator compared bands numerically. The downstream CAM Initiative website did contain a direction-sensitive sort map (`S1` first through `S5` last) and old code-to-label mappings; those require coordinated update.

Historical failure-mode severity values inside `legacy_governance_state` are provenance, not Incident severity. They were not used to assign or transform the canonical Incident band and remain historically scoped.

## Old severity semantics

- **S1 — Critical:** death, grave injury, grave or enduring liberty or essential-care deprivation, severe sexual or child-safety harm, very large realised loss, destructive loss of critical assets, or comparably grave persistent rights or societal harm.
- **S2 — High:** substantial materialised financial, property, privacy, rights, health, operational or equivalent harm below S1.
- **S3 — Moderate:** meaningful but bounded materialised harm above minor inconvenience.
- **S4 — Low:** minor, short-lived, localised or readily remedied materialised effect.
- **S5 — No materialised adverse downstream harm:** a materially observed governance-relevant occurrence without an established adverse downstream consequence.
- **SU — Unassessed:** no defensible band from the preserved evidence.

## New severity semantics

- **S1 — Minimal or no materialised adverse downstream harm:** a materially observed governance-relevant occurrence without an established adverse downstream consequence.
- **S2 — Low:** minor, short-lived, localised or readily remedied materialised effect.
- **S3 — Moderate:** meaningful but bounded materialised harm above minor inconvenience.
- **S4 — High:** substantial materialised financial, property, privacy, rights, health, operational or equivalent harm below S5.
- **S5 — Catastrophic or critical:** death, grave injury, grave or enduring liberty or essential-care deprivation, severe sexual or child-safety harm, very large realised loss, destructive loss of critical assets, or comparably grave persistent rights or societal harm.
- **SU — Unassessed:** no defensible band from the preserved evidence.

## Migration rule

This was a criteria-verified direct inversion plus a full-corpus evidence pass. The substantive thresholds were retained exactly and each record's structured materialised consequence, affected scope, seriousness/persistence, quantitative information, evidentiary limits and band rationale were checked against the translated criteria. The verified mapping was:

- old S1 = new S5;
- old S2 = new S4;
- old S3 = new S3;
- old S4 = new S2;
- old S5 = new S1; and
- SU remains SU.

This is not a blind text replacement: canonical severity codes, adjacent-band rationales and severity-specific threshold references were translated together. SU evidence-gap ranges were updated to the complete new S1-S5 scale. Legacy failure-mode severity was not rewritten. No failure-family, failure-class, primary/secondary classification, exemplar, evidence-status or evidence-confidence decision was changed.

## Legacy priority audit

No current schema, template, validator, generator, public index or website surface required a separate operational priority scale. The only structured residue was 86 historical `triage` objects across 70 migrated Incident records, including `triage_priority` values P0/P1/P2/P3/PN. Their prior semantic basis was not consistently evidenced and the active Incident methodology already separates occurrence severity from maintainer workflow state.

All 86 historical operational-triage objects were removed from those 70 records. The schema and validator now prohibit operational priority/triage keys recursively so the obsolete model cannot silently return. Stable historical review IDs were retained as provenance, while stale prose that represented priority as a current model component was removed or bounded. No replacement priority model was created.

## Corpus results

- Total canonical Incident records examined: **124**
- Records whose severity code changed: **72**
- Records whose severity code was unchanged: **52**
- Records at SU: **6**
- Before: S1: 11, S2: 40, S3: 46, S4: 15, S5: 6, SU: 6
- After: S1: 6, S2: 15, S3: 46, S4: 40, S5: 11, SU: 6
- Records from which legacy operational-priority metadata was removed: **70**
- Ambiguous cases requiring further human/evidentiary review: **6** — `VIGIL-INC-000028`, `VIGIL-INC-000033`, `VIGIL-INC-000037`, `VIGIL-INC-000065`, `VIGIL-INC-000120`, `VIGIL-INC-000121`

The SU records were not newly made ambiguous by the migration. Their existing evidence gaps remain controlling, and unsupported harm was not inferred merely to force a numeric band.

### Changed severity codes

| Incident | Old | New |
| --- | --- | --- |
| `VIGIL-INC-000001` | S2 | S4 |
| `VIGIL-INC-000003` | S2 | S4 |
| `VIGIL-INC-000004` | S1 | S5 |
| `VIGIL-INC-000005` | S1 | S5 |
| `VIGIL-INC-000006` | S1 | S5 |
| `VIGIL-INC-000007` | S1 | S5 |
| `VIGIL-INC-000008` | S1 | S5 |
| `VIGIL-INC-000009` | S4 | S2 |
| `VIGIL-INC-000010` | S4 | S2 |
| `VIGIL-INC-000011` | S4 | S2 |
| `VIGIL-INC-000013` | S2 | S4 |
| `VIGIL-INC-000016` | S4 | S2 |
| `VIGIL-INC-000017` | S4 | S2 |
| `VIGIL-INC-000019` | S4 | S2 |
| `VIGIL-INC-000020` | S4 | S2 |
| `VIGIL-INC-000021` | S4 | S2 |
| `VIGIL-INC-000029` | S1 | S5 |
| `VIGIL-INC-000030` | S1 | S5 |
| `VIGIL-INC-000031` | S4 | S2 |
| `VIGIL-INC-000034` | S4 | S2 |
| `VIGIL-INC-000035` | S2 | S4 |
| `VIGIL-INC-000036` | S4 | S2 |
| `VIGIL-INC-000041` | S2 | S4 |
| `VIGIL-INC-000042` | S4 | S2 |
| `VIGIL-INC-000045` | S2 | S4 |
| `VIGIL-INC-000047` | S2 | S4 |
| `VIGIL-INC-000048` | S2 | S4 |
| `VIGIL-INC-000049` | S1 | S5 |
| `VIGIL-INC-000053` | S1 | S5 |
| `VIGIL-INC-000054` | S2 | S4 |
| `VIGIL-INC-000055` | S2 | S4 |
| `VIGIL-INC-000057` | S2 | S4 |
| `VIGIL-INC-000060` | S2 | S4 |
| `VIGIL-INC-000061` | S2 | S4 |
| `VIGIL-INC-000062` | S2 | S4 |
| `VIGIL-INC-000064` | S1 | S5 |
| `VIGIL-INC-000067` | S2 | S4 |
| `VIGIL-INC-000069` | S2 | S4 |
| `VIGIL-INC-000070` | S2 | S4 |
| `VIGIL-INC-000072` | S2 | S4 |
| `VIGIL-INC-000073` | S2 | S4 |
| `VIGIL-INC-000074` | S2 | S4 |
| `VIGIL-INC-000075` | S2 | S4 |
| `VIGIL-INC-000076` | S2 | S4 |
| `VIGIL-INC-000077` | S2 | S4 |
| `VIGIL-INC-000078` | S4 | S2 |
| `VIGIL-INC-000079` | S4 | S2 |
| `VIGIL-INC-000082` | S2 | S4 |
| `VIGIL-INC-000083` | S1 | S5 |
| `VIGIL-INC-000084` | S2 | S4 |
| `VIGIL-INC-000085` | S2 | S4 |
| `VIGIL-INC-000086` | S2 | S4 |
| `VIGIL-INC-000088` | S2 | S4 |
| `VIGIL-INC-000090` | S2 | S4 |
| `VIGIL-INC-000092` | S4 | S2 |
| `VIGIL-INC-000093` | S5 | S1 |
| `VIGIL-INC-000094` | S2 | S4 |
| `VIGIL-INC-000096` | S2 | S4 |
| `VIGIL-INC-000102` | S2 | S4 |
| `VIGIL-INC-000103` | S2 | S4 |
| `VIGIL-INC-000104` | S2 | S4 |
| `VIGIL-INC-000107` | S2 | S4 |
| `VIGIL-INC-000110` | S2 | S4 |
| `VIGIL-INC-000113` | S2 | S4 |
| `VIGIL-INC-000118` | S2 | S4 |
| `VIGIL-INC-000119` | S2 | S4 |
| `VIGIL-INC-000122` | S5 | S1 |
| `VIGIL-INC-000123` | S5 | S1 |
| `VIGIL-INC-000124` | S5 | S1 |
| `VIGIL-INC-000125` | S5 | S1 |
| `VIGIL-INC-000126` | S5 | S1 |
| `VIGIL-INC-000127` | S2 | S4 |

## Record metadata and provenance

All 124 records were formally re-evaluated. `severity_assessment.assessed_on` and `record_identity.updated` were set to 2026-09-16, the patch component of `record_identity.version` was incremented, and an append-only interpretive review entry records whether the translated band changed or was affirmed. Existing source provenance and historical reviews were preserved except for removal of obsolete operational-priority residue.

## Validation

All coordinated checks passed:

- `build-vigil-public-records.py`: rebuilt the 124-record Incident index, registry manifest and taxonomy Case File examples;
- canonical Incident validation: 124 records passed;
- lightweight public Incident-index validation: 124 records passed;
- source provenance: 218 active source records passed;
- interpretive provenance: 124 Incidents passed;
- component-role validation: 124 Incidents passed;
- authorship provenance: passed;
- taxonomy validation: 14 family files and 66 classes passed in working-branch mode;
- VIGIL unit and pipeline tests: passed, including the recursive legacy-priority prohibition and ascending-severity adjacency rules;
- website build: consumed the migrated local Incident index and generated 124 crawlable Case File entrypoints;
- website VIGIL tests: 33 passed;
- website registry, catalogue, palette and published `/docs` validators: passed.

No validation warnings remain from this migration.
