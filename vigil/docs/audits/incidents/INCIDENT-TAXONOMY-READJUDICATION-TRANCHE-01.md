# VIGIL Unclassified Incident Re-adjudication — Tranche 1 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 1 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
- Taxonomy: **VIGIL Failure Taxonomy 0.6.5**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **71**
- Active families: **15**
- Release content digest: `sha256:68700f3c5a2e7c2eb46bc082604ffacce35f7083ccd082c38dd09103a0f39fa9`
- Evidence boundary: canonical `source_records` already preserved in each Incident; no broad or new external incident research was performed.
- Review method: deterministic full-current-taxonomy re-adjudication in frozen Incident-ID order. Harm Impact, source roles, occurrence facts, agent/environment metadata, external assessments, external-requirement mappings and CAM applicability were not reopened.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000011` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000078: no evidenced defective inherited state across a bounded continuity transition; FC-000035: displacement/underweighting does not establish persistence loss; FC-000012: no evidenced cross-context lineage/applicability loss | Retained unclassified. The preserved evidence establishes strategic-continuity loss but not a current selectable mechanism. Possible taxonomy-gap signal: strategic-continuity weighting without defective carryforward or persistence loss. |
| `VIGIL-INC-000013` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000002 / FC-000003: stolen credentials and illicit use do not establish provider permission logic or a transposed valid grant; FC-000041 / FC-000038: guardrail-bypass reporting does not establish the defined route or trigger needed for those classes | Retained unclassified. No provider-internal authority/control mechanism inferred from credential theft and bypass reporting. |
| `VIGIL-INC-000014` | unclassified / 0.2.3-draft | **classified / 0.6.5** | **FC-000043 Unwarranted Control Activation** (failure-occurrence, medium) | — | FC-000032: wrongful suspension is not itself collapse or misleading representation of distinct access states | Newly classified. Preserved reporting states Anthropic characterized the organisation-wide block as a false positive; the usage-policy enforcement control therefore activated without its valid trigger. |
| `VIGIL-INC-000015` | unclassified / 0.2.3-draft | **classified / 0.6.5** | **FC-000043 Unwarranted Control Activation** (failure-occurrence, high) | — | FC-000032: incorrect enforcement does not establish access-state representation collapse | Newly classified. OpenAI's own status record identifies incorrect account suspensions and later restoration, directly establishing unwarranted enforcement activation. |
| `VIGIL-INC-000016` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: SSO errors do not establish state collapse; FC-000031: no auth-state propagation defect; FC-000048: no failed verification dependency | Retained unclassified. Bounded SSO service failure without an evidenced current access-state mechanism. |
| `VIGIL-INC-000017` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: overload is capacity degradation rather than collapsed/misleading access state; FC-000048: no verification dependency | Retained unclassified. No current mapping asserted for model-capacity degradation. |
| `VIGIL-INC-000019` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: ordinary login/account-creation failure does not establish state collapse; FC-000031: no auth-state propagation defect; FC-000048: no verification dependency | Retained unclassified. Access outage without an evidenced current Failure Class mechanism. |
| `VIGIL-INC-000020` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000032: generic access degradation does not establish state collapse; FC-000031: no auth-state propagation defect | Retained unclassified. Bounded service-access incident without an evidenced access-state taxonomy mechanism. |

## Cross-incident consistency check

The two incorrect-enforcement records, `VIGIL-INC-000014` and `VIGIL-INC-000015`, receive the same structural mechanism because each preserves evidence that the suspension control activated when the represented policy trigger was not valid. Confidence differs because INC-000015 contains the provider's own status record explicitly identifying incorrect suspensions, while INC-000014 relies on preserved reporting of Anthropic's false-positive characterization.

The ordinary access/service failures `VIGIL-INC-000016`, `VIGIL-INC-000017`, `VIGIL-INC-000019` and `VIGIL-INC-000020` remain unclassified. They are negative controls for FC-000032: unlike classified access-state examples such as records where authorization, quota, capacity or model-state signals masked the operative condition, these four records do not preserve evidence that materially distinct access states were collapsed or misleadingly represented.

`VIGIL-INC-000011` remains distinct from FC-000078 examples: it records strategic-continuity displacement/underweighting, but the preserved evidence does not establish a discrete transition carrying defective inherited state that a receiving context then accepted without revalidation.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **2**
- Retained unclassified: **6**
- Moved to another schema status: **0**
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **1** (`VIGIL-INC-000011`; no new class proposed)

### Corpus classification counts

| Status | Before Tranche 1 | After Tranche 1 |
| --- | ---: | ---: |
| classified | 86 | **88** |
| provisionally-classified | 3 | **3** |
| unclassified | 52 | **50** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranche 1 is the only frozen-population tranche covered by this audit. The 52-record campaign is **not complete**. Tranche 2 and later frozen Incidents have not been re-adjudicated by this work package.
