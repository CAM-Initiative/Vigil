# Public Standards catalogue trace

Classification: REVIEW. Date: 11 October 2026.
Inspected `CAM-Initiative/cam-governance-catalogue` main HEAD `76346015f8b9b385f201f2cefbd030051ce3bbac` read-only.

The handoff advanced during implementation. Its new public Standards/source-listing requirement was read from integration HEAD `418134c32b3b0c881a20019bf9c8cd0c6d9707e2` and incorporated here.

## Existing governed data path

`src/lib/vigilExternalKnowledge.ts` loads the canonical `Vigil/main/vigil/external_governance/sources/source-registry.json`, source scope and requirement index/aggregate at runtime. `loadExternalSources` preserves entries and their source classes. `src/pages/vigil-standards-baseline.tsx` lists source entries, excludes explicitly excluded/superseded scopes, displays `source_class`, and derives clause counts independently. A supporting source with zero requirements remains listable. `src/pages/vigil-standard-source.tsx` displays source type, summary and source metadata in its dossier.

The 13 additions therefore enter the existing catalogue feed when this data reaches Vigil **main**, with genuine instrument types and summaries explaining their force. This PR targets the integration branch; it does not publish new entries to the live main-backed site. No website-only substitute data is created.

## Unverified and separate-site work

No deployed rendering or browser preview with the new registry was verified. Source code inspection is not a live render. The current list's umbrella title/ARIA text and dossier phrasing still refer to “AI governance standards”/“standard”. Those labels need a focused, separately reviewed catalogue PR if these wider instruments are published. Source-specific `source_class` and summary already convey the correct instrument kind; the general copy must not imply that all are consensus standards or AI-specific regulation.

Legal force is not a standalone source registry field. The list uses source type and public summaries; clause force will resolve from canonical requirement metadata after Gate 1 and extraction. Any new force-label display must follow the approved vocabulary and preserve the distinction between treaty duties, resolutions, non-binding principles and interpretation. Do not insert a website-only force field or manufacture an enforceable requirement.

Separate-site PR is deferred at the handoff's semantic publication-contract stop condition: final force vocabulary and canonical supporting-source extraction have not been approved. This file records the exact data route and discrepancy; it does not claim live listing completion or a completed site PR. The repository PR remains registration-only.
