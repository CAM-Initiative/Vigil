# INC-176–178 validator reconciliation — 2026-09-27

## Scope

This review resolves the VIGIL records validator failures introduced with VIGIL-INC-000176 through VIGIL-INC-000178 on `agent/incident-ecosystem-ingestion`.

The repair is evidence-first. It does not relax the validator, widen any Fidelity Class, alter VIGIL-HIM findings, or mechanically convert non-failure mappings.

## Source-type normalization

The first-party OpenAI occurrence pages in INC-176, INC-177 and INC-178 used the noncanonical source genre `provider incident report`.

The canonical VIGIL source genre is `incident report`. Publisher identity remains separately represented by `author_or_publisher` and `source_platform`, so this is a metadata normalization rather than a change in evidentiary authority.

## Successful-invariant adjudication

The six validator role errors were re-reviewed against the current class invariants and the preserved Incident evidence.

### VIGIL-FC-000042 — Governance Signal Delivery

- **INC-176: retain successful-invariant.** The researcher detected the credential exposure, reported it to security, and capable responders rapidly deactivated affected keys. The signal reached a capable destination and produced a containment effect.
- **INC-177: retain successful-invariant.** The P0 signal reached capable human review within minutes and remained within the incident-response sequence through manual termination. The expected automatic stop failing to activate is separately adjudicated under VIGIL-FC-000038 and is not rewritten as a signal-delivery failure.

### VIGIL-FC-000022 — Material Event Capture

- **INC-176: retain successful-invariant.** The retained investigation captures the material instruction, repository, credential-exposure and response events needed for proportionate post-incident oversight.
- **INC-177: retain successful-invariant.** The retained investigation captures the external-access and governance-response sequence, including the P0 alert, acknowledgement and termination events.

### VIGIL-FC-000024 — Audit-Trail Reconstructability

- **INC-176: retain successful-invariant.** The retained evidence supports reconstruction from repeated human narrowing through repository actions, credential exposure, detection and containment.
- **INC-177: retain successful-invariant.** The retained chronology provides ordered, correlated timestamps from successful external access through monitoring, acknowledgement and manual termination.

These findings are bounded to the evidence preserved in the canonical Incident records. They do not imply that every internal telemetry field is public or that the separate failure mechanisms operated correctly.

## Canonical repair

The reciprocal successful-invariant exemplar relationships are admitted in the canonical taxonomy for FC-000042, FC-000022 and FC-000024. The affected family versions advance as working-family patch revisions:

- VIGIL-FF-0004: 0.1.2 → 0.1.3
- VIGIL-FF-0007: 0.2.2 → 0.2.3

The dataset release remains stamped at VIGIL Alignment Taxonomy 0.6.7 on this working branch. Dataset release metadata is prepared separately under the taxonomy publication contract.

## Expected validator result

The previous nine VIGIL records errors should be eliminated:

- three noncanonical `source_type` values; and
- six successful-invariant mappings lacking admitted reciprocal taxonomy exemplars.
