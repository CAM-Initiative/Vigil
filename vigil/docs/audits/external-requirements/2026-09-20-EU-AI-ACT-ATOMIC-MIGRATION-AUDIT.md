# EU AI Act Atomic Requirement Migration Audit

## Transaction identity

- Repository: `CAM-Initiative/Vigil`
- Working branch: `fix/eu-ai-act-atomic-reconciliation`
- Exact starting remote `main` commit: `18a902160b5c24a6915cf09090b15ad3f9efac1e`
- Registered source: `EXT-7DB18E82C9D3` / `EU-AI-ACT-2024-1689`
- Source version: `2026-07-27`
- CELEX: `02024R1689-20260727`
- Migration date: `2026-09-20`

This audit records the deterministic identity migration only. It does not establish legal applicability, CAM applicability, compliance, conformance, or source-level completeness.

## Result

The canonical EU AI Act source/version shard contained 81 records before migration. The transaction retired eight coarse identities and inserted 102 deterministic successors:

`81 - 8 + 102 = 175`

The resulting aggregate contains 978 canonical EXTREQ records across 81 registered source versions. The EU shard and generated compatibility aggregate agree exactly for all 175 EU records.

No staged requirement was changed during final authoritative-source verification. The five staged packages were migrated as reviewed; the 18 source-explicit metadata normalisations were applied without adding generic audit artefacts or inferred evidence expectations.

## Retired identities and complete successor set

The durable machine-readable retirement map is `vigil/external_governance/requirements/retirements/EU-AI-ACT-2024-1689.json`. The complete successor-ID set is reproduced here for auditability.

| Retired identity | Clause | Successor count | Successor IDs |
|---|---|---:|---|
| `EXTREQ-F30E6B9A906370B9` | Article 4a | 9 | `EXTREQ-1736F5D9A9FEE3E6`, `EXTREQ-194BAA01C8CEDF96`, `EXTREQ-20A358942F546D98`, `EXTREQ-34D794BAE48B2042`, `EXTREQ-3A41A9530EB9DEB2`, `EXTREQ-665D430E7172E64F`, `EXTREQ-8406A6A9A7ECFCB6`, `EXTREQ-CA7D89D6C27E1B66`, `EXTREQ-F7A7DA9DCA8D32BD` |
| `EXTREQ-44B7BB17CB030468` | Article 9 | 22 | `EXTREQ-02D3C38E60FBC75C`, `EXTREQ-02F4CC772D68FDC5`, `EXTREQ-0544CA2011844D7B`, `EXTREQ-1B96234907248707`, `EXTREQ-2946FBD35BC58A58`, `EXTREQ-299CB405AFD073AD`, `EXTREQ-2D5184C0CBC7C888`, `EXTREQ-33D39FEAEBDBD160`, `EXTREQ-3E52DB8E6BE507D2`, `EXTREQ-3E93785343DE869B`, `EXTREQ-5726BF6006EBDB6B`, `EXTREQ-60CACACB2BFEB7F7`, `EXTREQ-73A86024AF7D7161`, `EXTREQ-75628AD3ADD38906`, `EXTREQ-8B44F849EE874DDD`, `EXTREQ-AC83782B40495818`, `EXTREQ-B0A987917989EBD3`, `EXTREQ-CA7D139554BB327C`, `EXTREQ-CF0A4B23B3BA8520`, `EXTREQ-DE5117D6C579F0C0`, `EXTREQ-E732321E515FACD8`, `EXTREQ-E9AA611B0FEEA58B` |
| `EXTREQ-09AD2F5442A55B55` | Article 10 | 16 | `EXTREQ-178652263E9E4A18`, `EXTREQ-3398AE5CB3D99116`, `EXTREQ-63C7B2C7A40C2498`, `EXTREQ-7234C42AA78CCF38`, `EXTREQ-9222332544520C5A`, `EXTREQ-93622681B6244218`, `EXTREQ-9DF571A09E1A27D1`, `EXTREQ-9FEBFF29B834BD4C`, `EXTREQ-B28452CC09682655`, `EXTREQ-BC555C025ADA13E7`, `EXTREQ-D00F7CC23DF9821F`, `EXTREQ-DCA23E99AFB9D80B`, `EXTREQ-EBE6DC949B6FC20A`, `EXTREQ-FDA81C83E36C9487`, `EXTREQ-FE2859AF565EC65F`, `EXTREQ-FF6802300FFACB68` |
| `EXTREQ-901AD2C0A909E790` | Article 11 | 10 | `EXTREQ-06DFAE509FD6D2C0`, `EXTREQ-1AB25504326527DA`, `EXTREQ-6346DFE636508217`, `EXTREQ-7D000D6868EDE244`, `EXTREQ-8E81789B79DB8954`, `EXTREQ-93CCE5CD38E0051D`, `EXTREQ-9FE3860DE191D68F`, `EXTREQ-A683139A9E6FCED0`, `EXTREQ-CBD23444D45C0CED`, `EXTREQ-FE0BA141D12895DA` |
| `EXTREQ-33898CCD26FBF5D5` | Article 12 | 9 | `EXTREQ-0348B64AA2D82BC9`, `EXTREQ-20379EF0C7E97FDF`, `EXTREQ-42D3F017A9786AE8`, `EXTREQ-4B0FECC5888FA820`, `EXTREQ-90A317D512B165D5`, `EXTREQ-A24734AAA7BA537F`, `EXTREQ-A8967B5D4698D35E`, `EXTREQ-BEACEB7A006E67C6`, `EXTREQ-D8E5BC29A4B8D257` |
| `EXTREQ-126CB22D1FF08066` | Article 13 | 16 | `EXTREQ-181639FC9C3F5A1B`, `EXTREQ-22BDBAD2AF63385B`, `EXTREQ-2367DE2925863585`, `EXTREQ-24BC7F6212EFE2B0`, `EXTREQ-268ED9A986D7E83B`, `EXTREQ-67532161EDB6C017`, `EXTREQ-889248600BFC9D01`, `EXTREQ-89DCF5FABCA6D7EC`, `EXTREQ-8F7449E24AFD2A1B`, `EXTREQ-92B09762EF226E56`, `EXTREQ-9E58A53D9E4E7141`, `EXTREQ-A41CA145D8369351`, `EXTREQ-C5F70A760221CB4E`, `EXTREQ-E07756B983D5575E`, `EXTREQ-F5D35DE8FBA32DFA`, `EXTREQ-F682BB69E2356482` |
| `EXTREQ-1B4CA7A04D63F038` | Article 14 | 11 | `EXTREQ-38FC055E070AEFB7`, `EXTREQ-602304871330447F`, `EXTREQ-8EFA5B7D3F8BBDD6`, `EXTREQ-9116B07FC5232868`, `EXTREQ-A413FEA840F110E8`, `EXTREQ-B9775B02872296D0`, `EXTREQ-BAA343B6CDB1862E`, `EXTREQ-C12EF9A1F6B7F76A`, `EXTREQ-CC21D20CF04D712A`, `EXTREQ-DEA2B22466A64818`, `EXTREQ-E7072B9D822AE4CC` |
| `EXTREQ-E640D3CE18685E25` | Article 15 | 9 | `EXTREQ-132DED975A441336`, `EXTREQ-4C363481F7EA7361`, `EXTREQ-614B18BB6F06157D`, `EXTREQ-B40880CAC2A2BE26`, `EXTREQ-BD2D919253BF3CDC`, `EXTREQ-EB9B6D8D8679CECC`, `EXTREQ-ED132C75DBBFFA1A`, `EXTREQ-EF7A17795274F23D`, `EXTREQ-F8090209290ACA6B` |

The successor records retain the staged `semantic_atomicity` state. Source-defined compounds retain their staged `constituent_propositions`; permissions remain permissions, institutional powers remain actor-specific, and source-explicit applicability conditions and qualifications remain field-level metadata.

## Metadata and source-fidelity disposition

- Overlay applied: `EU-AI-ACT-2026-07-27-metadata-normalization.json`; 18 overrides, restricted to the permitted metadata fields.
- The migrated 102-record slice has ledger entries with no `review-required` field decisions.
- The 73 older EU records remain in the metadata review queue where no equivalent source-fidelity decision had been established. They were not marked reviewed by migration.
- `source-fidelity.json` remains `requires-reextraction` with effective extraction status `partial`.
- Articles 4a and 9–15 are now recorded as reconciled, but additional represented operator-facing provisions still require semantic-atomicity/source-fidelity review.
- The EU source is not claimed to have complete legal coverage, and the migration does not establish legal applicability, CAM applicability, compliance, conformance or alignment.

## Retired-ID dependency audit

The repository-wide search found no retired ID in the live canonical EU shard, aggregate, requirement index, metadata report or generated source projections. Historical review packages, the stress-test fixture, the migration test/script, the retirement map and audit documentation retain retired IDs intentionally as historical/audit or control records.

| Retired ID | Current use/site | Classification | Appropriate successor candidate(s) | Reason / next action |
|---|---|---|---|---|
| `EXTREQ-F30E6B9A906370B9` | No live downstream reference identified; retained in Article 4a re-extraction and audit/control records | Historical/audit record — retain | Article 4a successor set in the retirement map | The former identity compressed two permissions and safeguards; downstream mapping is not required until a live consumer is found. |
| `EXTREQ-44B7BB17CB030468` | No live downstream reference identified; retained in Article 9 re-extraction and audit/control records | Historical/audit record — retain | Article 9 successor set in the retirement map | The former identity compressed the lifecycle risk-management architecture; taxonomy/Standards mapping is deliberately deferred. |
| `EXTREQ-09AD2F5442A55B55` | Retained in the Article 10 stress-test fixture, re-extraction package and historical audit | Historical/audit record — retain | Article 10 successor set in the retirement map | The stress test documents the defect that motivated migration; it is not a live requirement reference. |
| `EXTREQ-901AD2C0A909E790` | No live downstream reference identified; retained in Article 11 re-extraction/control records | Historical/audit record — retain | Article 11 successor set in the retirement map | The former identity compressed provider, institutional and product-law documentation propositions. |
| `EXTREQ-33898CCD26FBF5D5` | `vigil/taxonomy/families/VIGIL-FF-0004-observability-audit-integrity.json`, classes FC-000022 and FC-000024; the related taxonomy audit is retained as an audit record | Live canonical reference — requires successor migration | FC-000022: `EXTREQ-42D3F017A9786AE8` (with `EXTREQ-90A317D512B165D5` for purpose-appropriate traceability); FC-000024: `EXTREQ-90A317D512B165D5`, `EXTREQ-D8E5BC29A4B8D257`, `EXTREQ-BEACEB7A006E67C6`, and `EXTREQ-0348B64AA2D82BC9` | Article 12 was used as a broad regulatory-evidence reference. The next taxonomy/Standards reconciliation must select the exact logging, traceability and purpose-specific successors without creating a universal logging claim. |
| `EXTREQ-126CB22D1FF08066` | Retained in the Article 13 stress-test fixture, re-extraction package and historical audit | Historical/audit record — retain | Article 13 successor set in the retirement map | The former identity compressed transparency, instructions, human-oversight and information-content propositions. |
| `EXTREQ-1B4CA7A04D63F038` | No live downstream reference identified; retained in Article 14 re-extraction/control records | Historical/audit record — retain | Article 14 successor set in the retirement map | The former identity compressed oversight objectives, allocation, capabilities and the Article 14(5) exception. |
| `EXTREQ-E640D3CE18685E25` | No live downstream reference identified; retained in Article 15 re-extraction/control records | Historical/audit record — retain | Article 15 successor set in the retirement map | The former identity compressed accuracy, robustness, cybersecurity, feedback-loop and amendment-sensitive propositions. |

The Article 12 taxonomy reference is intentionally not edited in this tranche. It is the input to the subsequent taxonomy/Standards reconciliation, which must also review any related Article 5 and other external-requirement mappings for successor specificity. No failure-taxonomy mapping was updated merely to satisfy validators.

## Validation record

| Command | Result |
|---|---|
| `PYTHONPATH=vigil/scripts python vigil/scripts/migrate-eu-ai-act-atomic-reextraction.py --check-only` | PASS; idempotent migrated-state check, 8 retirements, 102 successors, 175 EU records |
| `python vigil/scripts/migrate-eu-ai-act-atomic-reextraction.py` | PASS; wrote canonical shards, aggregate, manifest and retirement map |
| `python vigil/scripts/manage-external-requirements.py build` | PASS; regenerated requirement indexes, completeness, coverage manifests, catalogue, access views, crosswalk projections and aggregate |
| `python vigil/scripts/manage-external-requirements.py validate --check-generated` | PASS; 81 source versions, 978 requirements |
| `python vigil/scripts/validate-external-requirement-metadata.py --write-report` | PASS; 978 canonical records, 905 metadata-complete, 73 records still requiring review |
| `python vigil/scripts/validate-external-requirement-metadata.py` | PASS; metadata contract valid |
| `python vigil/scripts/seed-eu-ai-act-metadata-review.py --write` | PASS; 102 staged requirements checked, 0 new ledger entries; no entry-level changes were required |
| `PYTHONPATH=vigil/scripts python vigil/tests/test_external_requirement_metadata.py` | PASS |
| `python vigil/tests/test_eu_ai_act_reextraction.py` | PASS; canonical 8-to-102 migration contract and generated aggregate agreement |
| `python vigil/tests/test_external_requirement_fidelity.py` | PASS |
| `python vigil/scripts/validate-external-requirement-fidelity.py` | PASS; migrated state recognised; EU remains partial/unassured |
| `python vigil/scripts/build-vigil-public-records.py` | PASS; rebuilt lightweight incident index (145 canonical records) |
| `python vigil/scripts/validate-vigil-records.py`; `python vigil/scripts/validate-vigil-public-records.py`; `python vigil/scripts/validate-vigil-source-provenance.py`; `python vigil/scripts/validate-vigil-interpretive-provenance.py`; `python vigil/scripts/validate-vigil-system-components.py`; `python vigil/scripts/validate-authorship-provenance.py` | PASS |
| `python -m unittest discover -s vigil/tests -p 'test*.py'` | PASS; 162 tests |

Corpus-wide strict metadata mode was not treated as a completion gate: it correctly remains non-green because unrelated unresolved metadata decisions remain, including 73 older EU records. The migrated 102-record slice has no unresolved field decisions. Taxonomy mappings were deliberately deferred.
