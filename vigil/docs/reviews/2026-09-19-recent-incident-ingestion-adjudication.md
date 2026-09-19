# Recent Incident Ingestion Adjudication — INC-000150–INC-000169

## Review boundary

- Branch: `agent/recent-incident-ingestion-2025-2026`
- Starting branch HEAD: `25e37230bf9cfec60a6fcefa9e5a08dfda2add5e`
- Starting `main` HEAD: `4cec178699891c121eda6bd838053e4ebfec8fd9`
- Execution date: 2026-09-19
- Records reviewed: 20 (`VIGIL-INC-000150` through `VIGIL-INC-000169`)
- New substantive source records: 27

The pass separated external-registry discovery from occurrence evidence, reviewed occurrence dates, reassessed all eleven VIGIL-HIM dimensions, compared supported mechanisms with the selectable taxonomy, and appended a point-in-time adjudication review without removing the intake review.

## Results

| Incident | Intake severity | Adjudicated severity | Taxonomy status | Admitted failure mappings |
| --- | --- | --- | --- | --- |
| INC-000150 | S3 | S3 | provisionally-classified | FC-000002 |
| INC-000151 | S4 | S3 | classified | FC-000053 |
| INC-000152 | S2 | S2 | classified | FC-000053 |
| INC-000153 | S2 | S2 | classified | FC-000062, FC-000016, FC-000010 |
| INC-000154 | S2 | S1 | classified | FC-000001, FC-000006 |
| INC-000155 | S3 | S3 | classified | FC-000015, FC-000062 |
| INC-000156 | S3 | S3 | unclassified | — |
| INC-000157 | S4 | S4 | classified | FC-000053, FC-000055 |
| INC-000158 | S3 | S4 | unclassified | — |
| INC-000159 | S3 | S2 | classified | FC-000006, FC-000009 |
| INC-000160 | S2 | S2 | provisionally-classified | FC-000046 |
| INC-000161 | S3 | S3 | requires-human-review | — |
| INC-000162 | S3 | S3 | requires-human-review | — |
| INC-000163 | S3 | S3 | unclassified | — |
| INC-000164 | S3 | S3 | classified | FC-000053 |
| INC-000165 | S2 | S2 | classified | FC-000062, FC-000016, FC-000010 |
| INC-000166 | S4 | S4 | unclassified | — |
| INC-000167 | S4 | SU | requires-human-review | — |
| INC-000168 | S2 | S2 | classified | FC-000062, FC-000016, FC-000010 |
| INC-000169 | S3 | S3 | requires-human-review | — |

Five overall severity assignments changed:

- INC-000151: S4 → S3. The reported SEK 500 million aggregate loss is substantial but does not support the intake's S4 band under the preserved evidence and currency rule.
- INC-000154: S2 → S1. The controlled experiment's documented loss exceeded $1,000 but remained below the VIGIL-HIM S2 financial threshold and caused no evidenced external harm.
- INC-000158: S3 → S4. Exposure of roughly 35,000 email addresses, thousands of private messages and about 1.5 million authentication tokens supports large-scale sensitive-data exposure despite rapid containment.
- INC-000159: S3 → S2. The npm credential compromise and unauthorised package were real, but the eight-hour exposure, benign payload and absence of evidenced user-data loss support bounded remediable harm.
- INC-000167: S4 → SU. VIGIL-HIM 1.0.0 does not provide an animal-welfare dimension, and the human physical-health thresholds were not applied by analogy to an unadjudicated veterinary allegation.

## Evidence and date findings

Primary, affected-party, provider, court, regulator or detailed independent sources now lead the evidence set. AI Incident Database entries remain preserved as `record-cross-reference` sources and in `external_incident_references`; they are not cited as Harm Impact evidence.

Occurrence dates were materially strengthened for the tranche, including:

- INC-000153: publication and withdrawal fixed to 15 October 2025;
- INC-000159: unauthorised npm publication fixed to 17 February 2026;
- INC-000164: bounded to the earliest supported public warning on 9 January 2026;
- INC-000165: affected filing fixed to 6 May 2026 from the corrective declaration;
- INC-000168: court occurrence fixed to 13 August 2025; and
- INC-000166: represented as a May–November 2025 conduct range.

The record-specific system surfaces, component roles, sectors and regulatory surfaces were also replaced where the intake had generic placeholders.

## Human follow-up and known limits

- **INC-000161:** public evidence describes CAD/navigation routing but does not establish an AI or machine-learning component. Continued VIGIL admission requires human scope review.
- **INC-000162:** the Cost Explorer interruption is established, but Amazon disputes the press attribution to autonomous Kiro action and no public technical postmortem resolves the conflict.
- **INC-000167:** the litigation allegations and clinical records require primary review, and VIGIL-HIM requires a governance decision before non-human animal harm can be banded.
- **INC-000169:** the affected party documents travel-programme revocation, but government sources do not publicly confirm the facial-recognition system, identification result or causal connection.
- **INC-000156 and INC-000163:** operational consequences are supported, but current evidence does not establish a sufficiently exact selectable failure mechanism.
- **INC-000166:** the guilty plea establishes prolonged criminal harm; the incomplete public conversation record does not establish that ChatGPT caused or selected the conduct.

No new Failure Class was created, and no record was classified from outcome severity alone. Disputes and inaccessible primary artefacts are stated in each record's assessment boundaries and appended review limitations.

## Publication and validation

Generated outputs were rebuilt from canonical records with `python vigil/scripts/build-vigil-public-records.py`.

Validation completed successfully:

- `python vigil/scripts/validate-vigil-records.py`
- `python vigil/scripts/validate-vigil-public-records.py`
- `python vigil/scripts/validate-vigil-source-provenance.py`
- `python vigil/scripts/validate-vigil-interpretive-provenance.py`
- `python vigil/scripts/validate-vigil-system-components.py`
- `python vigil/scripts/validate-authorship-provenance.py`

The complete `vigil/tests` discovery run passed: 149 tests, 0 failures. Taxonomy validation also passed for all 15 family files and 70 classes. A final semantic audit confirmed that each tranche record retains exactly one AIID cross-reference source and that no assessed Harm Impact dimension cites it as substantive evidence.
