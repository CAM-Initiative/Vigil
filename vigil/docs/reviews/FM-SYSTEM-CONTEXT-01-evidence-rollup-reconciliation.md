# FM-SYSTEM-CONTEXT-01 — Evidence-backed system-context reconciliation

**Reconciliation date:** 2026-08-15

**Scope:** All canonical VIGIL failure-mode records. The projection separates evidence publication/hosting platform from the affected AI/platform system. It does not add external evidence, browse sources, or infer affected-system identity from narrative prose. Layer 1 external requirements are not modified by this reconciliation.

## Current corpus state

- Failure modes reviewed: **58**
- Failure modes with evidenced providers/vendors: **44**
- Failure modes with evidenced products/services: **35**
- Failure modes with evidenced models/runtimes: **48**
- Records changed in this execution: **48**

### Evidence scope

| Scope | Records |
| --- | ---: |
| `multi-provider` | 28 |
| `not-applicable` | 1 |
| `provider-unresolved` | 5 |
| `single-provider` | 16 |
| `system-unresolved` | 8 |

## Projection contract

- `source_platform` identifies where evidence is hosted or published; it is not an affected-system field.
- `source_records[].system_or_product` and `source_records[].model_or_algorithm` are the preferred source-level affected-system fields.
- Existing concrete FM `system_context` values provide a bounded compatibility fallback for older evidence packages that pre-date those source fields.
- `evidenced_vendors`, `evidenced_products_or_services`, and `evidenced_models_or_runtimes` are the public-facing normalized roll-ups.
- `evidenced_systems` preserves source traceability and records whether an identity came from source affected-system metadata or the record-context fallback.
- Narrative `source_context`, `relevance_note`, article titles, and publisher prose are not mined to manufacture system identity.

The 2026-08-15 transmutation applied this contract across the then-current FM corpus. Subsequent executions are deterministic freshness checks; the changed-record list below describes only the current execution.

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

## Records changed in this execution

- `VIGIL-2026-FM-0001`
- `VIGIL-2026-FM-0002`
- `VIGIL-2026-FM-0006`
- `VIGIL-2026-FM-0007`
- `VIGIL-2026-FM-0008`
- `VIGIL-2026-FM-0009`
- `VIGIL-2026-FM-0010`
- `VIGIL-2026-FM-0011`
- `VIGIL-2026-FM-0012`
- `VIGIL-2026-FM-0013`
- `VIGIL-2026-FM-0014`
- `VIGIL-2026-FM-0015`
- `VIGIL-2026-FM-0016`
- `VIGIL-2026-FM-0017`
- `VIGIL-2026-FM-0018`
- `VIGIL-2026-FM-0019`
- `VIGIL-2026-FM-0020`
- `VIGIL-2026-FM-0022`
- `VIGIL-2026-FM-0023`
- `VIGIL-2026-FM-0024`
- `VIGIL-2026-FM-0025`
- `VIGIL-2026-FM-0026`
- `VIGIL-2026-FM-0027`
- `VIGIL-2026-FM-0028`
- `VIGIL-2026-FM-0031`
- `VIGIL-2026-FM-0032`
- `VIGIL-2026-FM-0034`
- `VIGIL-2026-FM-0035`
- `VIGIL-2026-FM-0036`
- `VIGIL-2026-FM-0038`
- `VIGIL-2026-FM-0039`
- `VIGIL-2026-FM-0040`
- `VIGIL-2026-FM-0041`
- `VIGIL-2026-FM-0042`
- `VIGIL-2026-FM-0043`
- `VIGIL-2026-FM-0044`
- `VIGIL-2026-FM-0045`
- `VIGIL-2026-FM-0046`
- `VIGIL-2026-FM-0047`
- `VIGIL-2026-FM-0048`
- `VIGIL-2026-FM-0049`
- `VIGIL-2026-FM-0050`
- `VIGIL-2026-FM-0052`
- `VIGIL-2026-FM-0053`
- `VIGIL-2026-FM-0054`
- `VIGIL-2026-FM-0056`
- `VIGIL-2026-FM-0057`
- `VIGIL-2026-FM-0058`
