# Adjudication reason length rule removal

Date: 2026-09-26

Branch: `integration/consolidate-divergent-branches`
Human direction: remove the validator rule for overlong adjudication reasons and report the remaining failures.

## Control change

`validate-vigil-taxonomy-adjudications.py` previously rejected any nonempty matrix `reason` longer than 280 characters. The two-line length check was removed. Required, class-specific reasons, boilerplate and duplicate checks, decision polarity, canonical role, Section 02 and exemplar checks remain in force.

The change affects `vigil/taxonomy/VIGIL.FailureTaxonomy.Adjudications.json` validation. It does not change the Incident schema, canonical Incident prose, source evidence, taxonomy recognition conditions, generated public indexes or website rendering. A 281-character reason that otherwise satisfies the validator now passes; no previously passing reason becomes invalid. In the current corpus, 1,999 length errors across 32 Incidents disappear. No reason was truncated or rewritten. A character ceiling is not a recognition condition and would encourage loss of case-specific explanation if repaired mechanically; editorial concision can be reviewed without a canonical validity cap.

## Read-only validation after the change

| Gate | Result |
| --- | --- |
| Full adjudication matrix | 86 errors: 71 `no-mapping` uncertainty-polarity flags, all in INC-000145; 15 `unresolved` missing-fact-marker defects across ten Incidents. |
| Full Incident validator | 46 pre-existing errors across 32 records; unchanged. |
| Taxonomy validator | Pass: 15 families, 76 classes. |
| Adjudication role tests | Pass: 5 tests. |

The 71 polarity flags and 15 marker defects require evidence and decision-quality review. They are not authorised for automatic reclassification or mechanical wording changes by this validator edit. Broad canonical record repairs remain a separate human-governed step under `vigil/MAINTAINERS.md`.
