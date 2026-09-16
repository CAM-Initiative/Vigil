# Harm Impact Matrix migration audit — 2026-09-16

## Scope and starting point

This review examined all 124 canonical Incident records on
`chore/remove-aeon-governance-lab-public-references`. The branch already used the
ascending S1–S5 direction established by the earlier severity-alignment audit.
This migration replaced the single narrative `severity_assessment` with the
versioned `harm_impact_assessment` contract and re-derived overall severity under
VIGIL-HIM 1.0.0.

The review did not alter Failure Families, Failure Classes, primary or secondary
classifications, exemplars, source evidence, or invariant/repair analysis.

## External alignment

The central Observatory Reference Registry records the sources used:

- `VIGIL-REF-000001`–`000003`: MIT FutureTech AI Incident Tracker scale,
  tracker methodology and June 2026 evidence-bounded review note;
- `VIGIL-REF-000004`: CSET AI Harm Framework;
- `VIGIL-REF-000005`–`000006`: CISA functional impact, information impact and
  recoverability guidance;
- `VIGIL-REF-000007`: NIST SP 800-34 recovery-time and maximum-tolerable-downtime
  concepts;
- `VIGIL-REF-000008`: NIS2 implementing thresholds;
- `VIGIL-REF-000009`: DORA ICT incident materiality thresholds; and
- `VIGIL-REF-000010`: ASD Australian cross-government cyber incident guidance.

VIGIL aligns the ascending direction and adapts selected consequence,
functional-impact, recoverability and materiality concepts. It does not claim
equivalence with MIT, CSET, CISA, NIST, NIS2, DORA or ASD. External references
provide context; VIGIL-HIM owns the operational dimensions, thresholds and
derivation rule.

## Canonical derivation

Overall severity is the maximum S1–S5 band among assessed materialised-harm
dimensions. No averaging or summation occurs. Multiple lower harms do not
escalate the result. Every dimension tied at the maximum is controlling.

`unreported` records missing published impact information and is never S1.
`insufficient-evidence` records impact evidence that cannot support a band.
`not-applicable` requires affirmative contextual grounds. S1 requires positive
evidence of minimal/no downstream materialised harm. If no dimension is assessed,
the overall severity is SU.

## Transformation method

The controlled migration read each record's preserved summary, materialised
consequence, affected scope, seriousness/persistence, quantitative information,
evidentiary limits, band rationale and source references. It selected a primary
materialised-harm dimension from occurrence evidence, linked the matching stable
matrix threshold, preserved supported quantitative text as an observed value,
and explicitly marked all other dimensions. Generic statements that a quantity
was not reported were excluded from dimension selection.

The old severity code was treated as a candidate result, not as a harm category.
The validator independently recomputes the maximum from assessed rows. Eight
assessed records changed because their preserved evidence did not meet the new
dimension threshold corresponding to the legacy code. The other 110 assessed
records retained their severity. The six former SU records remain SU because no
dimension can yet be defensibly banded.

## Corpus results

| Measure | Result |
| --- | ---: |
| Canonical records examined | 124 |
| Records structurally migrated | 124 |
| Overall severity changed | 8 |
| Overall severity unchanged | 116 |
| Records at SU / requiring human evidence review | 6 |
| Assessed dimension rows | 119 |
| Unreported dimension rows | 825 |
| Insufficient-evidence dimension rows | 6 |
| Not-applicable dimension rows | 42 |

### Before/after distribution

| Severity | Before | After |
| --- | ---: | ---: |
| S1 | 6 | 6 |
| S2 | 15 | 15 |
| S3 | 46 | 49 |
| S4 | 40 | 44 |
| S5 | 11 | 4 |
| SU | 6 | 6 |

### Changed severity

| Incident | Old | New | Matrix basis |
| --- | --- | --- | --- |
| `VIGIL-INC-000004` | S5 | S4 | Live organisational intrusions are substantial, but catastrophic/prolonged essential-service loss is not established. |
| `VIGIL-INC-000005` | S5 | S4 | Wrongful arrest is substantial; prolonged or enduring detention is not established. |
| `VIGIL-INC-000006` | S5 | S4 | Wrongful arrest while pregnant is substantial; grave injury or prolonged/enduring detention is not established. |
| `VIGIL-INC-000007` | S5 | S4 | Wrongful detention is substantial; prolonged or enduring deprivation is not established. |
| `VIGIL-INC-000049` | S5 | S4 | Reported realised loss is US$25 million, within the S4 financial band. |
| `VIGIL-INC-000053` | S5 | S3 | ₹10.70 crore supports meaningful bounded harm; no USD conversion or S4 qualitative override is evidenced. |
| `VIGIL-INC-000077` | S4 | S3 | US$4,820 loss plus identity-document disclosure is meaningful but bounded and does not meet an S4 threshold. |
| `VIGIL-INC-000083` | S5 | S3 | A$7.4 million aggregate loss supports meaningful bounded harm; no USD conversion or S4 qualitative override is evidenced. |

### Human evidence review required

- `VIGIL-INC-000028`
- `VIGIL-INC-000033`
- `VIGIL-INC-000037`
- `VIGIL-INC-000065`
- `VIGIL-INC-000120`
- `VIGIL-INC-000121`

Each remains SU with a concrete `assessment_gap`; the most plausible impact
dimension is `insufficient-evidence`, not assigned S1.

## Versioning and provenance

Every migrated record received a patch-version increment, `record_identity.updated`
was set to 2026-09-16, and a new append-only interpretive review entry identifies
the VIGIL-HIM migration scope and evidence limits. Existing source, diagnostic,
legacy and interpretive provenance was preserved.

## Legacy priority metadata

The preceding severity-schema audit had already removed canonical and record-level
P0/P1/P2/P3/PN or equivalent operational-priority metadata. This pass found no
canonical priority field to preserve and removed priority metadata from 0 records.
The schema continues to reject legacy priority keys recursively. VIGIL-HIM does
not introduce a replacement priority model.

## Generated outputs and validation

- `python3 vigil/scripts/build-observatory-reference-registry.py`: passed; 10
  registry references and CSV rows.
- `python3 vigil/scripts/validate-vigil-records.py`: passed; 124 records.
- `python3 vigil/scripts/build-vigil-public-records.py`: regenerated lightweight
  Incident and master indexes from `overall_severity`.
- `python3 vigil/scripts/validate-vigil-public-records.py`: passed; 124 records.
- `python3 -m unittest discover -s vigil/tests -p 'test_*.py'`: passed; 134 tests.

The generated Incident index remains lightweight. It publishes only the derived
overall code and canonical record link; the full matrix remains in the canonical
Incident JSON.
