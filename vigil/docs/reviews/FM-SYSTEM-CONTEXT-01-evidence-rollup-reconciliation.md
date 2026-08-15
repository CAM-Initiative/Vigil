# FM-SYSTEM-CONTEXT-01 — Evidence-backed system-context reconciliation

**Reconciliation date:** 2026-08-15

**Scope:** All canonical VIGIL failure-mode records. This is a deterministic metadata projection from each FM's own `source_records`; it does not add external evidence, browse sources, infer vendor/model identity from narrative prose, or modify Layer 1 external requirements.

## Outcome

- Failure modes reviewed: **58**
- Failure modes changed by reconciliation: **11**
- Failure modes with evidenced providers/vendors: **42**
- Failure modes with evidenced products/services: **35**
- Failure modes with evidenced models/runtimes: **47**

### Evidence scope

| Scope | Records |
| --- | ---: |
| `multi-provider` | 19 |
| `not-applicable` | 1 |
| `provider-unresolved` | 8 |
| `single-provider` | 23 |
| `system-unresolved` | 7 |

## Contract

The maintained `system_context` block now separates compatibility summary fields from evidence-backed roll-ups:

- `evidence_scope` describes whether record-local evidence resolves zero, one, or multiple providers.
- `evidenced_vendors` lists providers/vendors established by structured source metadata.
- `evidenced_products_or_services` lists concrete products/services established by structured source metadata.
- `evidenced_models_or_runtimes` preserves concrete model/runtime names present in `model_or_algorithm`.
- `evidenced_systems` preserves source-level traceability to the evidence record that established each system claim.
- `platform_or_vendor`, `product_or_service`, and `specific_model_or_runtime` remain compatibility summary fields and must not substitute for the evidence-backed arrays in public interfaces.

No system identity is inferred from narrative `source_context`, `relevance_note`, article title, or publisher identity alone.

## Multi-provider failure modes

- `VIGIL-2026-FM-0007`
- `VIGIL-2026-FM-0008`
- `VIGIL-2026-FM-0012`
- `VIGIL-2026-FM-0014`
- `VIGIL-2026-FM-0015`
- `VIGIL-2026-FM-0019`
- `VIGIL-2026-FM-0020`
- `VIGIL-2026-FM-0022`
- `VIGIL-2026-FM-0024`
- `VIGIL-2026-FM-0025`
- `VIGIL-2026-FM-0026`
- `VIGIL-2026-FM-0032`
- `VIGIL-2026-FM-0034`
- `VIGIL-2026-FM-0042`
- `VIGIL-2026-FM-0044`
- `VIGIL-2026-FM-0048`
- `VIGIL-2026-FM-0052`
- `VIGIL-2026-FM-0057`
- `VIGIL-2026-FM-0058`

## Unresolved system identity

The following records retain insufficient structured source metadata to identify a provider or system deterministically. They are not silently filled from narrative context:

- `VIGIL-2026-FM-0003`
- `VIGIL-2026-FM-0004`
- `VIGIL-2026-FM-0029`
- `VIGIL-2026-FM-0030`
- `VIGIL-2026-FM-0033`
- `VIGIL-2026-FM-0037`
- `VIGIL-2026-FM-0038`
- `VIGIL-2026-FM-0039`
- `VIGIL-2026-FM-0040`
- `VIGIL-2026-FM-0041`
- `VIGIL-2026-FM-0045`
- `VIGIL-2026-FM-0046`
- `VIGIL-2026-FM-0050`
- `VIGIL-2026-FM-0051`
- `VIGIL-2026-FM-0053`

## Changed records

- `VIGIL-2026-FM-0004`
- `VIGIL-2026-FM-0033`
- `VIGIL-2026-FM-0037`
- `VIGIL-2026-FM-0038`
- `VIGIL-2026-FM-0039`
- `VIGIL-2026-FM-0040`
- `VIGIL-2026-FM-0045`
- `VIGIL-2026-FM-0046`
- `VIGIL-2026-FM-0051`
- `VIGIL-2026-FM-0053`
- `VIGIL-2026-FM-0055`
