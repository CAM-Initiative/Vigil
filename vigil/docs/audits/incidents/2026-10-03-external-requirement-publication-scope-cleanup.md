# External requirement publication-scope cleanup — INC-000001 / INC-000129

Date: 2026-10-03

## Trigger

Printed Case File review exposed a presentation and data-boundary problem in Section 04 Compliance. The Stage 4 review for INC-000001 had correctly reviewed the full taxonomy-derived candidate set, but then persisted all 125 candidate dispositions into the canonical Incident record. The result was 85 `insufficient-evidence` and 40 `not-applicable` rows, zero applicable requirements and zero occurrence-level findings. This made an exhaustive audit surface look like a public standards assessment.

## Disposition

The complete 125-candidate review remains preserved in `2026-10-02-stage4-INC-000001-reconciliation.json`. The canonical INC-000001 record now retains only the two occurrence assessments that the 1 October review had independently retained and that still have supported current derivation paths:

- `EXTREQ-2E1D2C63187C14E8` — NIST AI RMF MEASURE 2.5; applicability remains unresolved because the evidence does not establish that the relevant organisation undertook that voluntary RMF outcome for the system and deployment context.
- `EXTREQ-C25CB2D997BC6FE8` — SDOS-EN-01; applicability remains unresolved because the evidence does not establish SDOS adoption or the source-defined pre-execution enforcement point.

No external requirement finding was added or removed. The Alignment Taxonomy failures in INC-000001 remain separate occurrence findings and do not become external-standard failures by correspondence alone.

INC-000129 retains its single current `EXTREQ-B266BCD5C9F680AB` assessment (NIST SP 800-218A RV.2.2 R2). Unlike the INC-000001 candidate expansion, this is a bounded, materially plausible model-development stop-use/rollback question for the unreleased-model training occurrence. Applicability remains unresolved because the evidence does not establish the SSDF Profile undertaking or an applicable model-version stop/rollback programme.

## Method correction

`EXTERNAL-REQUIREMENT-ADJUDICATION.md` now distinguishes comprehensive candidate review from canonical publication. Candidate exhaustion belongs in dated audits. The public `external_requirement_assessments` array is selective and must not be used as a candidate ledger.

The website projection is being changed in parallel so that applicable findings are visually primary, unresolved and not-applicable assessments are secondary expandable groups, requirement links route through the VIGIL standards library, and evidence links resolve to numbered Case File references rather than repeating raw source URLs.
