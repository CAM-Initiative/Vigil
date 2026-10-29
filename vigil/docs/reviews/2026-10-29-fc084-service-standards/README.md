# Service availability and continuity standards review

29 October 2026 · [tracker #154](https://github.com/CAM-Initiative/Vigil/issues/154) · related [#150](https://github.com/CAM-Initiative/Vigil/issues/150) and [#173](https://github.com/CAM-Initiative/Vigil/issues/173).

**Status: research complete within the disclosed access limits; decisions proposed; maintainer approval pending.** AI-authored analysis, not human verification, certification or legal advice. This is an active REVIEW notice board under `REVIEW-RECORD-RETENTION.md`, with machine-measured AUDIT evidence. It is not canonical requirement or adjudication data. Retire working material after approved promotion, retaining pinned Git history. Owner: #154 / human maintainer.

Branch: `work/full-corpus-taxonomy-gap-audit-20261028`, shared with C01/C02. Research baseline: `de201bfb66faef81cca3c205c3d77a1134390fb0`. Published main checked: `b800676a1b8db630338c0eaa8dc96999a45da877`. Taxonomy, source registry, source-scope and FC–EXTREQ relationships agree between these baselines. Incident versions differ; the impact evidence measures both separately. No branch synchronisation or merge is implied.

## Recommendation for approval

Keep the existing FC-084 unchanged. Prioritise a bounded NIST crosswalk using existing requirements, followed by seven specifically located CSF extraction candidates. Hold ISO normative extraction until authorised text and processing rights are established. Registering ISO metadata, admitting a requirement, reviewing a class relationship, and assessing an Incident are separate decisions.

The inventory found **109 registered source entries**, including AI RMF 1.0 and CSF 2.0, but none for the four requested ISO editions or their amendments. AI RMF has 74 canonical requirements representing 72 Core subcategories; CSF has eight requirements within an explicitly partial scope. FC-084 has **zero canonical external-requirement relationship rows**. Its class file has one contextual reference to CSF RC.RP-05. Those are different surfaces.

The recommended first implementation is an approval-bounded crosswalk to the recovery component, with explicit conditions. It must not make a framework into a provider-specific service promise. No reviewed instrument establishes an unconditional migration/export duty or numerical uptime threshold for every AI service.

## Review files

- [Evidence, editions and access register](EVIDENCE-AND-ACCESS.md).
- [Candidate extraction and crosswalk decisions](DECISIONS-AND-CROSSWALK.md).
- [Implementation gates and read-only impact](APPROVALS-AND-IMPACT.md).
- [Pinned class and dataset evidence](evidence/baseline.json): exact FC-084 text, neighbouring definitions, source metadata/scope, existing NIST records and relationships.
- [Measured impact](evidence/impact.json): branch/main counts, exact occurrence rows and relevant requirement use. Screening is not semantic re-adjudication.

## Authority and identity

FC-084 is `VIGIL-FC-000084`, Service Availability and Degradation Integrity, under `VIGIL-FF-0017`. It was admitted in the v0.8.0 tranche; the inspected current published taxonomy is **v0.9.0, 27 October 2026**. FF-0017 source version is 0.1.1. The class definition, invariant, five failure conditions, three success conditions, nine exclusions and reference are preserved exactly in `evidence/baseline.json` with file digests.

Issue #154's original proposal wording is historical. Its 20 October comments already acknowledge admission under the then-working FC-089 identifier. Use the present canonical FC-084 identity, not that historical allocation. Neither this review nor admission of supporting standards re-admits a class.

## Recognition contract applied

The operative definition is:

> The property by which an AI-mediated service or material dependent function fulfils independently established availability and usable-functional-quality obligations. When service is materially interrupted, degraded, restricted or withdrawn, the responsible actor must meet the applicable continuity standard through proportionate operation, usable degraded service, timely recovery, feasible alternative or informed transition within its authority and control. Accurate outage reporting or a merely nominal fallback does not, by itself, establish that the required service continuity was preserved.

For failure, independently establish the actor/function/time-specific obligation and threshold; material degradation; the response actually required; the omitted or ineffective response or threshold breach; and impairment of governed use. For Aligned, require a materially tested obligation and demonstrated sufficient usable function or response. A nominal fallback does not prove practical usability. Later restoration cannot resolve an earlier failure retrospectively.

All-result exclusions defeat admission where there is no independently applicable obligation, only one harmful output, or only an access-description, verification-dependency, work-state, coercion or interaction-protection defect. Failure-only exclusions protect proportionate restrictions and adequate feasible recovery consistent with the actual commitment; they do not exclude a separately supported Aligned result. Source uncertainty is not permission to change these conditions.

## Bounded conclusion

This review delivers source identities, explicit access holds, existing-row analysis, candidate locators, proposed conditional relationships and a measured impact report. It does **not** claim completed ISO clause review or passing canonical admission validation. #154 should remain open pending the maintainer's decision and resolution or explicit acceptance of the source-access holds. No canonical files, Incidents, schema, validators, publications or website projections are changed.
