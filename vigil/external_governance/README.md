# External Governance Corpus

This directory groups VIGIL's external-governance source registry and the analytical requirements derived from those sources. They belong to one subsystem, but they remain separate authority layers.

## Structure

- `sources/` — identifies external instruments and maintains source/version identity, lifecycle, publisher metadata, source-review state and durable public source knowledge.
- `requirements/` — stores the atomic governance requirements, controls, definitions and guidance extracted from registered sources, together with source-fidelity, metadata-review and assurance state.

The flow is:

`external source -> extracted external requirement -> incident-level external requirement assessment (if applicable)`

A registered source does not by itself create an extracted requirement. A requirement is not automatically applicable to a specific Incident, and inclusion establishes neither CAM institutional applicability nor adoption, compliance, conformance or coverage. The unused standalone CAM assessment subsystem was retired; any future CAM-institution assessment belongs in a separately governed project.

The corpus includes legislation, regulatory material, standards, frameworks, specifications and other authoritative governance sources. For that reason, `external_governance` is intentionally broader than `external_standards`.

See `sources/README.md` and `requirements/README.md` for the contracts of each layer.
