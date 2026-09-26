# Validator-debt closure audit — 26 September 2026

## Scope and authority boundary

- **Starting branch:** `integration/consolidate-divergent-branches`
- **Starting head:** `22af457d221a7972b434ee3b4ca85622849024ad`
- **Purpose:** close failures emitted by the current Incident, publication, provenance, system-component, adjudication and taxonomy validators after the INC-000145 reassessment and Stage 01 authoring pass.
- **Evidence boundary:** this pass used canonical evidence and current exhaustive-matrix decisions already present on the branch. It performed no new external evidence research, allocated no class or family, changed no taxonomy definition, recognition condition or exclusion, and changed no Harm Impact conclusion.
- **Campaign boundary:** this was not the separate 135-pair unresolved-adjudication campaign. Unresolved decisions were retained unless their validator-failing reason needed to name the missing recognition fact more precisely.

## Captured starting baseline

The baseline was captured before repairs by running the builder and every validator required by the work package.

| Validator | Starting result | Failure classification |
|---|---:|---|
| `validate-vigil-records.py` | 46 errors across 32 Incidents | 27 mixed-role records retained an inconsistent legacy block-level role; 15 positive non-failure mappings lacked reciprocal admitted taxonomy exemplars; 3 classified records had a null primary mapping with their sole mapping incorrectly placed as secondary; 1 record used a non-canonical product label. |
| `validate-vigil-public-records.py` | 0 errors | Passed. |
| `validate-vigil-source-provenance.py` | 0 errors | Passed. |
| `validate-vigil-interpretive-provenance.py` | 0 errors | Passed. |
| `validate-vigil-system-components.py` | 0 errors | Passed. |
| `validate-authorship-provenance.py` | 0 errors | Passed. |
| `validate-vigil-taxonomy-adjudications.py` | 14 errors across 9 Incidents | Unresolved reasons did not use sufficiently explicit missing/indeterminate-recognition-fact wording. |
| `taxonomy/validate_taxonomy.py` | 0 errors | Passed. |

The historical **71 INC-000145 uncertainty-polarity errors were absent**. Commit `89bf0575e52a71b78610e8e95a0f667775a776ad` therefore superseded that historical QA bucket. INC-000145 remained unchanged, including unresolved FC-000053.

After the 14 matrix-quality errors were repaired, the adjudication validator proceeded to its role-surface comparison and exposed **72 further actions across 18 Incidents**. Those actions concerned canonical/Section 02/matrix role drift or missing reciprocal exemplars, not new matrix decisions.

## Incident-validator repairs

### Mixed-role legacy summary field

The obsolete block-level `taxonomy_classification.classification_role` was removed from these mixed-role records; mapping-local roles remain authoritative and unchanged:

`VIGIL-INC-000001`, `000003`, `000004`, `000005`, `000006`, `000007`, `000008`, `000009`, `000014`, `000018`, `000055`, `000056`, `000075`, `000084`, `000085`, `000086`, `000088`, `000097`, `000098`, `000099`, `000112`, `000116`, `000117`, `000153`, `000159`, `000170`, and `000173`.

**Category:** structural drift. **Evidence/adjudication change:** none.

### Mapping position

For `VIGIL-INC-000162`, `VIGIL-INC-000167`, and `VIGIL-INC-000169`, the sole existing ambiguous-boundary mapping was moved from `secondary_classifications[0]` to `primary_classification`. The class, role, rationale, confidence and evidence were preserved.

**Category:** structural drift. **Evidence/adjudication change:** none.

### Product vocabulary

`VIGIL-INC-000032` was normalised from product label `ChatGPT Work` to canonical product `ChatGPT`; the more specific Work-interface detail remains in the occurrence narrative and system context.

**Category:** structural vocabulary drift. **Evidence/adjudication change:** none.

### Reciprocal taxonomy exemplars required by existing mappings

The following already-canonical mapping roles received matching admitted taxonomy exemplars:

- `VIGIL-INC-000003`: FC-000002 and FC-000018 ambiguous-boundary; FC-000022, FC-000024 and FC-000035 successful-invariant; FC-000066 ambiguous-boundary.
- `VIGIL-INC-000004`: FC-000002, FC-000003, FC-000041, FC-000046, FC-000062 and FC-000078 ambiguous-boundary; FC-000038 successful-invariant.
- `VIGIL-INC-000120`: FC-000023 and FC-000041 ambiguous-boundary.

**Category:** taxonomy reciprocity drift. **Evidence/adjudication change:** none; the Incident mappings and roles pre-existed this pass.

## Adjudication-validator repairs

### Unresolved reasons

Every decision remained `unresolved`; only the reason was sharpened to identify the exact missing recognition fact:

- `VIGIL-INC-000100` / FC-000037: required-control existence and availability/applicability state; FC-000040: prior operative control state and loss across transition.
- `VIGIL-INC-000106` / FC-000080: whether the researchers' contribution entered or shaped the AI-mediated result or value chain.
- `VIGIL-INC-000115` / FC-000016: whether required citation verification was omitted or unavailable rather than merely poorly performed.
- `VIGIL-INC-000119` / FC-000038: available applicable safeguard, trigger occurrence and non-activation on successful episodes.
- `VIGIL-INC-000120` / FC-000038: the same episode-specific safeguard, trigger and non-activation facts; the separately governed conceptual question was not decided.
- `VIGIL-INC-000144` / FC-000003: original authority, material scope change and carryover; FC-000064: objective-driven displacement of pathway-constraint validation; FC-000070: exhaustion of feasible admissible paths and absence of a fresh continuation basis.
- `VIGIL-INC-000147` / FC-000064: whether routing utility displaced passenger-control, consent or pathway-admissibility validation.
- `VIGIL-INC-000148` / FC-000018: the substitute intermediate condition treated as proof of correct order completion.
- `VIGIL-INC-000149` / FC-000020: existence and reuse of pre-update verification; FC-000038: applicable safeguard, trigger and non-activation; FC-000040: prior operative control state and loss across the update.

**Category:** substantive adjudication-quality wording. **Evidence/adjudication change:** no decision or polarity changed; uncertainty was preserved and stated at the class-recognition level.

### Matrix-to-canonical and Section 02 reconciliation

The clean exhaustive matrix was already authoritative for these roles. The pass synchronised, rather than re-decided, the missing canonical and Section 02 surfaces:

- `VIGIL-INC-000031`: FC-000032 successful-invariant and FC-000043 ambiguous-boundary.
- `VIGIL-INC-000032`: FC-000034 failure-occurrence.
- `VIGIL-INC-000034`: FC-000049 and FC-000052 ambiguous-boundary.
- `VIGIL-INC-000035`: FC-000032 successful-invariant.
- `VIGIL-INC-000039`: FC-000032 successful-invariant.
- `VIGIL-INC-000040`: FC-000061 ambiguous-boundary.
- `VIGIL-INC-000041`: FC-000010 failure-occurrence and FC-000018 ambiguous-boundary.
- `VIGIL-INC-000044`: FC-000049 ambiguous-boundary.
- `VIGIL-INC-000100`: FC-000070 successful-invariant.
- `VIGIL-INC-000141`: FC-000022 and FC-000024 successful-invariant.

Matching admitted exemplars were added for each new successful-invariant or ambiguous-boundary relationship. Section 02 relationship encodings were also normalised, without role changes, for `VIGIL-INC-000047`, `000052`, `000080`, `000162`, `000164`, `000167`, `000169`, and `000171`.

**Category:** taxonomy role-surface and reciprocal-provenance drift. **Evidence/adjudication change:** no exhaustive-matrix decision changed. Existing canonical evidence supplied the public rationale; no new evidence was admitted.

## Generated artefacts

The deterministic builder refreshed:

- `vigil/VIGIL.Incidents.Index.json`
- `vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json`

`vigil/VIGIL.Registry.Index.json` was reproduced byte-for-byte and therefore did not remain changed.

## Final status

All required validators and repository-required tests pass. Final error counts are zero for the Incident validator, public-record validator, source and interpretive provenance validators, system-component validator, authorship validator, exhaustive adjudication validator and taxonomy validator. No failure was deliberately left outstanding, and no human-policy decision was required to close the measured validator debt.
