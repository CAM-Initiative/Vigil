# VIGIL Failure Taxonomy Bibliography Reconciliation — 2026-09-21

## Scope

This audit records the external-source reconciliation performed on `agent/taxonomy-external-reference-reconciliation` before merge.

The work is limited to the supporting-reference layer of selectable VIGIL Failure Classes. It does not alter class IDs, definitions, recognition conditions, exclusions, Incident mappings, Harm Impact, or CAM/CAELESTIS doctrine.

## Evidence rule

Every selectable Failure Class should retain at least one independent external foundation that is not an Incident used to demonstrate that class.

Preferred foundations are:

1. binding legislation or regulatory instruments;
2. consensus standards or technical standards;
3. independent research literature;
4. authoritative technical or governance guidance as supplementary support.

Provider Incident reports may remain canonical Incident evidence or case context, but should not serve as the sole class-level justification for a Failure Class instantiated by that same occurrence.

## Self-reference repair

The following circular class-level references were removed:

- `VIGIL-FC-000078 Defective-State Carryforward Failure` — removed OpenAI's *Self-generated prompt injections in compaction summaries* as class-level support.
- `VIGIL-FC-000069 Reward-Proxy Exploitation` — removed OpenAI's *The Hugging Face incident and the road ahead* as class-level support.
- `VIGIL-FC-000070 Safe-Exit Persistence Failure` — removed the same OpenAI Hugging Face incident report as class-level support.

Current independent foundations are:

- FC-000078 — independent peer-reviewed memory-poisoning research.
- FC-000069 — *Concrete Problems in AI Safety* and *AI Safety Gridworlds*.
- FC-000070 — IEEE 7009-2024 plus supplementary NIST AI RMF guidance.

## Internal standards-corpus reconciliation

The repository's canonical external-governance requirements corpus was used as the primary discovery and authority layer, particularly:

- `vigil/external_governance/requirements/requirements-index.json`
- `vigil/external_governance/sources/source-registry.json`

Where a clause/control is represented by a canonical `EXTREQ-*` record, taxonomy references preserve the requirement ID and source-native clause/control.

The reconciliation added or strengthened support for authority boundaries, provenance, verification, observability, access/session continuity, governance-control reach, control activation, identity/evaluative integrity, infrastructure authority, value appropriation and objective-pursuit classes.

## Final gap closure

The final previously unsupported or guidance-only population was closed as follows:

| Failure Class | Independent foundation added |
| --- | --- |
| FC-000005 Transformation-Mediated Authority Laundering | W3C PROV-DM |
| FC-000031 Authentication-State Continuity Failure | IETF RFC 7009 |
| FC-000041 Required Governance Route Bypass | EU AI Act Article 14(4)(e) |
| FC-000042 Governance Signal Delivery Dead-End | EU AI Act Article 73; IEEE 7009 |
| FC-000058 Dependency-Derived Governance Authority | EU Data Act Article 23 |
| FC-000059 Infrastructural Access Leverage | EU Data Act Articles 23 and 25 |
| FC-000060 Canonical Representation Capture | W3C PROV-DM |
| FC-000061 Sovereign Authority Projection Through Infrastructure | EU Data Act Article 32 |
| FC-000067 Privileged-Access Appropriation | EU AI Act Article 53(1)(c) and 53(1)(d) |
| FC-000069 Reward-Proxy Exploitation | Independent reward-hacking research |
| FC-000074 Instruction-Induced Identity Override | IEEE 7000 |
| FC-000075 Pragmatic Constraint Rendering Failure | IEEE 7000 |
| FC-000076 Governance Neutrality Capture | Global Internal Audit Standards; IEEE 7000 |
| FC-000077 Distributed Role Optimisation Collapse | IEEE 7000 |

## Result

At closeout:

- current selectable Failure Classes inspected: **74**
- classes with at least one `standards-evidence`, `regulatory-evidence`, or `research-evidence` reference: **74**
- classes without any external reference: **0**
- classes supported only by authoritative/contextual guidance: **0**
- class-level references published by OpenAI: **0**
- known self-referential class justifications remaining: **0**

The taxonomy may still retain provider material in Incident records, external assessments or case-specific evidence. That material is intentionally separate from the independent class-level bibliography.
