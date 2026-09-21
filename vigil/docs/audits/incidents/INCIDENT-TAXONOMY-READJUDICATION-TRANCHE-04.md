# VIGIL Unclassified Incident Re-adjudication — Tranche 4 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 4 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
- Taxonomy: **VIGIL Failure Taxonomy 0.6.5**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **71**
- Active families: **15**
- Release content digest: `sha256:68700f3c5a2e7c2eb46bc082604ffacce35f7083ccd082c38dd09103a0f39fa9`
- Evidence boundary: canonical evidence already preserved in each Incident; no new external incident research was performed.
- External-assessment boundary: existing structured assessments and substantive attributable analytical positions in preserved sources were checked separately from occurrence evidence and taxonomy adjudication.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000074` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000038: safeguard trigger/applicability not sufficiently preserved; FC-000041: no defined required route shown bypassed; FC-000046: AI decision-authority role remains disputed | Retained unclassified. Labour/contract dispute remains evidence-bounded. |
| `VIGIL-INC-000075` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000002: no agent-side capability-as-permission inference; FC-000003: no valid authority grant transposed; FC-000064: no evidenced displacement of an independent constraint; FC-000077: multi-agent execution alone is insufficient | Retained unclassified. Hostile human-directed multi-agent use is not itself an internal framework failure. |
| `VIGIL-INC-000076` | unclassified / 0.2.3-draft | unclassified / 0.6.5 | — | — | FC-000046: GPTZero not shown to have independently authorised/determined sanction; FC-000038: no defined disciplinary control and failed activation sequence | Retained unclassified. FC-000046 remains analytically close but does not cross its authority threshold. |
| `VIGIL-INC-000077` | unclassified / 0.2.3-draft | **classified / 0.6.5** | **FC-000053 Identity-Representation Authority Conflation** | **FC-000052 Instrumental Choice Manipulation** | FC-000010 rejected as less structurally specific/duplicative | Newly classified. Same AIID Incident 1660 occurrence as classified INC-000082; cross-record taxonomy consistency restored without merging records. |
| `VIGIL-INC-000091` | unclassified / 0.3.0-draft | unclassified / 0.6.5 | — | — | FC-000030: provider signals were correlatable; FC-000058/059: dependency was not used as authority or leverage | Retained unclassified. Concurrent outages remain ecosystem resilience evidence without a shared mechanism. |
| `VIGIL-INC-000092` | unclassified / 0.3.1-draft | unclassified / 0.6.5 | — | — | FC-000031: no stale authenticated session/post-revocation Gmail access; FC-000040: disconnect scope over retained copies not established; FC-000055: no materially different secondary purpose | Retained unclassified. Possible taxonomy gap for retained-copy processing after connector revocation/disconnection. |
| `VIGIL-INC-000094` | unclassified / 0.3.1-draft | unclassified / 0.6.5 | — | — | FC-000002/003/064: hostile operator intentionally selected objective and enabled unattended mode; FC-000038: approval prompts were deliberately disabled rather than failing to activate | Retained unclassified. Deliberate hostile unattended configuration is not automatically an internal Hermes failure. |
| `VIGIL-INC-000095` | unclassified / 0.3.1-draft | unclassified / 0.6.5 | — | — | FC-000010: package identity/substitution is not ordinary authorship misattribution; FC-000011/013: no synthesis/transformation lineage mechanism; FC-000041: required release route/bypass path not preserved | Retained unclassified. Possible taxonomy gap for malicious package-distribution/software-supply-chain provenance substitution. |

## Newly classified occurrence

### VIGIL-INC-000077

The preserved record describes AI-generated videos impersonating identifiable immigration attorney Angel Leal, reportedly used to induce a victim to send US$4,820 and disclose Social Security and residency documents.

The occurrence now maps to:

- **Primary — VIGIL-FC-000053 Identity-Representation Authority Conflation**
  - the attorney's likeness and professional identity were used in an identity-bound synthetic representation without authority for that portrayal;
- **Secondary — VIGIL-FC-000052 Instrumental Choice Manipulation**
  - the synthetic identity was used instrumentally to induce trust, payment and sensitive-document disclosure.

This is the same bounded AI Incident Database occurrence, Incident 1660, already represented by `VIGIL-INC-000082`, which is classified under the same mechanism pair. Tranche 4 restores cross-record taxonomy consistency. It does **not** merge, delete or otherwise reconcile the duplicate Incident identity; that is a separate corpus-identity task.

## External-assessment reconciliation

### Existing assessments retained

- `VIGIL-INC-000075`: `VIGIL-EXTASSESS-000009` (Dream Security) remains a valid same-occurrence technical assessment.
- `VIGIL-INC-000094`: `VIGIL-EXTASSESS-000017` (Hunt.io / Bob Diachenko) remains a valid same-occurrence technical assessment.
- `VIGIL-INC-000095`: `VIGIL-EXTASSESS-000018` (Mistral AI) remains a valid same-occurrence provider assessment.

For INC-000095, the `vigil_comparison_note` was corrected to distinguish ordinary-language package-provenance/release-integrity failure from VIGIL taxonomy membership. The prior wording could be read as though a precise selectable package-provenance class already existed. The corrected note states that the Incident remains unclassified under taxonomy 0.6.5 because no current class precisely encodes malicious package-distribution substitution.

No new structured assessment was added for ordinary incident reporting, union/employer claims, registry entries, product documentation or brief provider root-cause statements that did not meet the substantive analytical-position threshold.

## Cross-incident consistency

- INC-000077 now aligns with INC-000082 because both preserve the same AIID 1660 attorney-impersonation occurrence and support the same identity-authority and instrumental-manipulation mechanisms.
- INC-000075 and INC-000094 remain negative controls against classifying malicious use alone. In both records, hostile human operators intentionally direct the offensive objective; the evidence does not establish a distinct system-side authority inference or governance-control failure.
- INC-000076 remains below FC-000046 because the detector result entered the disciplinary process but is not shown to have become sufficient decision authority independently of Yale's additional evidence.
- INC-000092 remains outside FC-000031 because the evidence expressly distinguishes revocation of live Google access from processing copies already retained. It also remains outside FC-000055 because the retained data were not shown to be repurposed for a materially different secondary purpose.
- INC-000095 remains distinct from provenance classes that concern authorship misattribution, synthesis lineage or transformation lineage. The unresolved mechanism is trusted software-package/release identity carrying attacker-supplied executable content.

## Taxonomy-gap signals

### VIGIL-INC-000092

Potential gap: **retained-data use after revocation/disconnection** where live connector access has ended but previously ingested copies remain available for agent processing. Current authentication-state, control-state and secondary-purpose classes do not precisely encode that lifecycle boundary on the preserved facts.

### VIGIL-INC-000095

Potential gap: **malicious package-distribution / software-supply-chain provenance substitution** where a trusted package or release identity carries attacker-supplied executable content. Existing provenance classes do not precisely encode the trusted-distribution substitution mechanism without overextending authorship or transformation-lineage concepts.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **1** (`VIGIL-INC-000077`)
- Retained unclassified: **7**
- Moved to another schema status: **0**
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- Possible taxonomy-gap signals recorded: **2** (`VIGIL-INC-000092`, `VIGIL-INC-000095`)
- Structured external assessments added: **0**
- Existing structured external assessments substantively corrected: **1** (`VIGIL-EXTASSESS-000018`)

### Corpus classification counts

| Status | Before Tranche 4 | After Tranche 4 |
| --- | ---: | ---: |
| classified | 88 | **89** |
| provisionally-classified | 3 | **3** |
| unclassified | 50 | **49** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranches 1 through 4 of the frozen 52-record campaign have now been reviewed. The campaign is **not complete**. Tranche 5 and later frozen Incidents have not been re-adjudicated by this work package.


## Post-tranche taxonomy correction — 2026-09-21

The original Tranche 4 disposition for `VIGIL-INC-000077` is preserved above as historical audit evidence, but it has been **superseded** by the subsequent cross-corpus AI-mediated economic scam reconciliation.

That reconciliation introduced `VIGIL-FC-000079 — AI-Mediated Deceptive Economic Solicitation` and identified a structural attribution error in the Tranche 4 mapping:

- FC-000052 had attributed the human scammers' deceptive objective and tactic to a non-agentic AI system;
- FC-000053 had inferred generator-side likeness-authority handling despite the generating system, request, consent controls and safeguard state being unknown.

The current canonical disposition for INC-000077 is therefore:

- **taxonomy version:** 0.6.6
- **classification:** classified
- **primary:** VIGIL-FC-000079
- **secondary:** none

The Tranche 4 table and corpus totals above describe the state at the time Tranche 4 closed. Current canonical records and the separate `INCIDENT-AI-MEDIATED-ECONOMIC-SCAM-RECONCILIATION.md` audit govern the superseding classification.
