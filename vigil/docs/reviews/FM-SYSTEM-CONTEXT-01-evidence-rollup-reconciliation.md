# FM-SYSTEM-CONTEXT-01 — Evidence-backed system-context reconciliation

**Original migration date:** 2026-08-15

**Scope:** All canonical VIGIL failure-mode records. The projection separates evidence publication/hosting platform from the affected AI/platform system. It does not add external evidence, browse sources, or infer affected-system identity from narrative prose. Layer 1 external requirements are not modified by this reconciliation.

## Current corpus state

- Failure modes reviewed: **71**
- Failure modes with evidenced providers/vendors: **52**
- Failure modes with evidenced products/services: **41**
- Failure modes with evidenced models/runtimes: **58**
- Records changed in this execution: **12**

### Evidence scope

| Scope | Records |
| --- | ---: |
| `multi-provider` | 31 |
| `not-applicable` | 1 |
| `provider-unresolved` | 7 |
| `single-provider` | 21 |
| `system-unresolved` | 11 |

## Projection contract

- `source_platform` identifies where evidence is hosted or published; it is not an affected-system field.
- `source_records[].system_or_product` and `source_records[].model_or_algorithm` are the source-level affected-system fields when that source establishes affected-system identity.
- Source roles that do not establish the affected system, such as `contextual-background`, are not included in the affected-system roll-up.
- Existing concrete FM `system_context` values provide a bounded compatibility fallback for older evidence packages that pre-date those source fields.
- `evidenced_vendors`, `evidenced_products_or_services`, and `evidenced_models_or_runtimes` are the public-facing normalized roll-ups.
- `evidenced_systems` preserves source traceability and records whether an identity came from source affected-system metadata or the record-context fallback.
- Detailed model/runtime names are intentionally open-ended; closed compatibility fields remain constrained to the schema's admitted values.
- Narrative `source_context`, `relevance_note`, article titles, and publisher prose are not mined to manufacture system identity.

The 2026-08-15 transmutation applied this contract across the then-current FM corpus. Subsequent records use a deterministic per-record reconciliation date that is never earlier than the record's canonical creation date.

## Multi-provider failure modes

- `VIGIL-2026-FM-0007`
- `VIGIL-2026-FM-0008`
- `VIGIL-2026-FM-0010`
- `VIGIL-2026-FM-0011`
- `VIGIL-2026-FM-0012`
- `VIGIL-2026-FM-0013`
- `VIGIL-2026-FM-0014`
- `VIGIL-2026-FM-0015`
- `VIGIL-2026-FM-0016`
- `VIGIL-2026-FM-0020`
- `VIGIL-2026-FM-0022`
- `VIGIL-2026-FM-0024`
- `VIGIL-2026-FM-0025`
- `VIGIL-2026-FM-0026`
- `VIGIL-2026-FM-0027`
- `VIGIL-2026-FM-0032`
- `VIGIL-2026-FM-0034`
- `VIGIL-2026-FM-0035`
- `VIGIL-2026-FM-0042`
- `VIGIL-2026-FM-0043`
- `VIGIL-2026-FM-0044`
- `VIGIL-2026-FM-0047`
- `VIGIL-2026-FM-0048`
- `VIGIL-2026-FM-0049`
- `VIGIL-2026-FM-0052`
- `VIGIL-2026-FM-0053`
- `VIGIL-2026-FM-0057`
- `VIGIL-2026-FM-0058`
- `VIGIL-2026-FM-0063`
- `VIGIL-2026-FM-0068`
- `VIGIL-2026-FM-0071`

## Unresolved system identity

These records still lack sufficient structured affected-system metadata or a concrete pre-existing FM system context. They remain unresolved rather than being filled from narrative evidence:

- `VIGIL-2026-FM-0003`
- `VIGIL-2026-FM-0004`
- `VIGIL-2026-FM-0021`
- `VIGIL-2026-FM-0029`
- `VIGIL-2026-FM-0030`
- `VIGIL-2026-FM-0033`
- `VIGIL-2026-FM-0037`
- `VIGIL-2026-FM-0038`
- `VIGIL-2026-FM-0039`
- `VIGIL-2026-FM-0040`
- `VIGIL-2026-FM-0045`
- `VIGIL-2026-FM-0046`
- `VIGIL-2026-FM-0051`
- `VIGIL-2026-FM-0059`
- `VIGIL-2026-FM-0060`
- `VIGIL-2026-FM-0061`
- `VIGIL-2026-FM-0062`
- `VIGIL-2026-FM-0065`

## Records changed in this execution

- `VIGIL-2026-FM-0059`
- `VIGIL-2026-FM-0060`
- `VIGIL-2026-FM-0061`
- `VIGIL-2026-FM-0062`
- `VIGIL-2026-FM-0063`
- `VIGIL-2026-FM-0064`
- `VIGIL-2026-FM-0065`
- `VIGIL-2026-FM-0066`
- `VIGIL-2026-FM-0067`
- `VIGIL-2026-FM-0068`
- `VIGIL-2026-FM-0069`
- `VIGIL-2026-FM-0070`
