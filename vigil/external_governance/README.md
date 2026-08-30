# External Governance Corpus

This directory groups VIGIL's external-governance source registry and the analytical requirements derived from those sources. They belong to one subsystem, but they remain separate authority layers.

## Structure

- `sources/` — identifies external instruments and maintains source/version identity, lifecycle, publisher metadata, source-review state and durable public source knowledge.
- `requirements/` — stores the atomic governance requirements, controls, definitions and guidance extracted from registered sources, together with source-fidelity, metadata-review and assurance state.

The flow is:

`external source -> extracted external requirement -> CAM applicability/coverage assessment -> VIGIL routing or repair analysis`

A registered source does not by itself create an extracted requirement. An extracted requirement does not by itself establish CAM applicability, adoption, compliance, conformance or coverage.

The corpus includes legislation, regulatory material, standards, frameworks, specifications and other authoritative governance sources. For that reason, `external_governance` is intentionally broader than `external_standards`.

See `sources/README.md` and `requirements/README.md` for the contracts of each layer.
