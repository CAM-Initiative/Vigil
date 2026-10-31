# Approved continuation — existing NIST component crosswalks

## 31 October update — four CSF requirements admitted

The official PDF was retrieved successfully on 31 October. Its 1,518,858 bytes have SHA-256 `3c31f46fee98cac0c4323453e5109291a213b4de7fef8c058af9bf67f717433c`, exactly matching the registered source. The earlier source-file hold is resolved.

PR.IR-03, PR.IR-04, RC.RP-02 and RC.RP-04 are now admitted as four requirements, each with a supported FC-084 component relationship. CSF coverage increases from eight to twelve provisions and remains partial. The full requirement dataset increases from 1,130 to 1,134 records; FC-084 now has ten supported component pairs. Source scope, metadata decisions, fidelity review, source-review provenance and generated external-governance outputs are updated. The exact source and relationship evidence is retained in `vigil/external_governance/requirements/review-evidence/NIST-CSF-2-0-service-availability-20261031.json`.

RS.MA-05, the two RC.RP-06 propositions and RC.CO-03 remain unadmitted contextual candidates. Their source locators and dispositions remain in `DECISIONS-AND-CROSSWALK.md` and the current source-scope entry. ISO access and processing-rights holds remain unchanged. Issue #154 remains open; no closure, Incident repair, taxonomy amendment, PR or website deployment is included.

The eight superseded draft proposal files have been retired from the active tree. Their exact pre-admission objects and isolated validation remain [recoverable at the 29 October commit](https://github.com/CAM-Initiative/Vigil/tree/615edea776e4ae83816d380a8baf9480672cc9bc/vigil/docs/reviews/2026-10-29-fc084-service-standards/proposals). No canonical dependency points to those drafts. The sections below describe the earlier 29 October stage, not the present requirement-admission state.

Validation passed: source and requirement validators with generated-output checks, fidelity and authorship checks, 57 regression tests and the metadata-review contract regression. All four new records have complete eight-field metadata decisions. The prior eight CSF requirements and all 758 existing relationship objects are unchanged. Read-only resolution adds four disposable candidates each to INC-156 E005, E006 and E007. No Incident, taxonomy, code, schema, public Case File index or Harm Impact projection is changed. The full metadata report still identifies 73 previously outstanding records elsewhere; this bounded addition does not claim corpus-wide completion.

29 October 2026. The maintainer responded “Beautiful. Please continue” after the complete standards review and six-pair recommendation. This continuation implements those six bounded relationships to **existing admitted requirements**. Contract approval is not substantive human source verification. The initial proposal documents remain dated research history; this file records the resulting current state.

## Canonical delta

- `taxonomy-relationships.json`: **752 → 758** relationships. All 752 existing objects remain byte-equivalent as JSON values, in their original order. Six FC-084 strong-supporting component pairs are appended. Each has `whole_invariant_supported: false`, actual applicability/qualification limits, current class and requirement digests, and resolving evidence.
- Two live evidence packets under `vigil/external_governance/requirements/review-evidence/`: `NIST-CSF-2-0-fc084-service-components-20261029.json` and `NIST-AI-100-1-fc084-service-components-20261029.json`. These are maintained resolving evidence, not disposable review worksheets. No runtime link points into the draft proposal directory.
- Requirements remain **1,130** across **109 source versions**. Source registry, source scope, fidelity and assurance ledgers, all existing requirement bytes, taxonomy criteria, Incidents and public projections are unchanged.

| Source/control | Existing requirement | Accepted component |
| --- | --- | --- |
| CSF RC.RP-05 | `EXTREQ-2D0252D6865FB9DF` | Restored service function and operational confirmation |
| CSF RC.RP-01 | `EXTREQ-8C67B5EEFB0AA897` | Execution after the actual recovery trigger |
| RMF MEASURE 2.6 | `EXTREQ-4E032FB784E538EB` | Safe failure/constrained operation component |
| RMF MANAGE 2.3 | `EXTREQ-D22AB2D961D08A9E` | Response/recovery for a newly identified previously unknown risk |
| RMF MANAGE 4.3, process row | `EXTREQ-0124DD1D36A2BEBB` | Incident/error response and recovery process |
| RMF GOVERN 1.7 | `EXTREQ-E0E174AA5FE5AD2B` | Safe phase-out process where an independent transition obligation applies |

None establishes a universal uptime guarantee, continued access entitlement, mandatory export or migration service. Actual service duty, actor, threshold, time and episode remain independently established. Existing neighbouring-class relationships are retained.

## New candidates prepared, not admitted

`proposals/requirements.json` contains **eight concrete draft records for seven controls**. RC.RP-06 is split into a criteria-based recovery-end declaration and completion of incident documentation. These can be independently assessed; passing one cannot establish the whole control.

Four draft records have a proposed strong-supporting FC-084 component pair: PR.IR-03, PR.IR-04, RC.RP-02 and RC.RP-04. Four remain contextual and fail the existing supporting-source admission rule: RS.MA-05, both RC.RP-06 records and RC.CO-03. This failure is expected and retained. No unrelated class was assigned and no relationship was inflated to force admission.

The proposals include exact requirement objects, relationship objects, eight-field metadata decisions, source-scope before/after and separate source-specific review evidence. They are outside the canonical shards and do not allocate admitted EXTREQ identities. Their deterministic prospective identifiers must be collision-checked again at any approved promotion. Draft `review_status: supported` describes the analytical pair inside this package; it is not canonical admission or human verification.

The directly downloadable NIST PDF carriers returned HTTP 403. Primary PDF text was available through web retrieval, but no newly downloaded bytes were hashed. Existing source-version digests are explicitly retained as registered provenance rather than represented as newly computed checksums. Confirm the exact reviewed carrier before promoting new requirements. The six implemented pairs reference unchanged, already admitted requirement objects and their established provenance.

ISO metadata proposals and normative extraction remain unimplemented. The original access, processing-rights and edition-compatibility holds still apply.

## Verification

Passed:

- Existing canonical requirement validator with generated-output consistency: 109 source versions, 1,130 requirements.
- External requirement fidelity validation and authorship provenance validation.
- 35 relevant regression tests: 20 external requirement, 11 supporting-source admission and 4 clause resolver tests.
- Direct candidate validation using the existing source-scope and requirement validation functions: all eight draft objects pass the structural contract. Four correctly fail supporting admission because they have only contextual pairs. The isolated simulation uses an explicitly synthetic provisional fidelity list; no canonical fidelity approval is inferred.
- Exact review-artifact/digest resolution for all 14 draft pairs; 14 altered-checksum copies are rejected. See the [historical candidate validation](https://github.com/CAM-Initiative/Vigil/blob/615edea776e4ae83816d380a8baf9480672cc9bc/vigil/docs/reviews/2026-10-29-fc084-service-standards/proposals/validation.json).

No permanent test, schema or validator change was made. Full Incident semantic join validation and website deployment remain outside this bounded crosswalk implementation.

## Read-only occurrence impact

The six accepted edges broaden **candidate discovery only** for matching canonical FC-084 episodes. Existing external results and polarity remain unchanged. The measured before/after resolver delta is in `evidence/continuation-impact.json`.

Six existing assessment rows use one of these requirements, in INC-030, INC-044, INC-205, INC-206, INC-209 and INC-212. None currently has `derived_from_class_ids`. Adding the new pair does not validate those occurrences: each still needs the correct independently supported class and episode. They remain part of #173 reconciliation; no row is silently relinked, deleted or reclassified.

INC-156 remains the sole currently admitted FC-084 Incident. Its existing mapping does not make every newly discoverable NIST outcome applicable, especially cybersecurity recovery outcomes in a power-outage context. INC-044 still requires independently evidenced transition obligations before any FC-084 admission.

## Remaining gates

No Gate 1 control implementation or Gate 2 corpus repair has occurred. Both retain the explicit approvals recorded in #173 and `MAINTAINERS.md`. New requirement promotion must separately resolve the carrier hold, approve the exact admitted subset and source-scope delta, retain full fidelity/metadata/pair evidence and pass canonical validation. Context-only candidates and ISO requirements stay held. No new PR or branch was created.
