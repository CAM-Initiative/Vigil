# Incident Context — Gate 2 pilot for maintainer approval

**22 October 2026 · REVIEW · Proposed, not applied.**

This packet completes the read-only corpus inventory and five source-reviewed proposals required before Gate 2. It does not claim that all 200 Incidents have received semantic context review. No canonical Incident, schema, validator, public projection or website implementation has been changed by this packet.

## Decision requested

Approve the five additive proposals below and their evidence-bounded migration approach for the remaining corpus. After approval, review and apply batches of at most 20 records, rechecking current versions and source evidence before every write. Retain original content, append actual review provenance and update record versions. Genuine unknowns are valid completed reviews. Then implement the reviewed geography projection and the existing catalogue design, with its required tests and visual checks. Keep both branches unmerged and PR #155 draft.

The user request and `INCIDENT-CONTEXT-GATE2-WORK-HANDOFF-20261022.md`, steps 3–4, require this approval checkpoint. Gate 1 is not bulk-migration approval. No new Gate 1 amendment is proposed: the current roles, `other` role with explicit basis, source references and unresolved relations represent these five cases without additional fields.

## Pinned baseline and inventory

| Item | Baseline |
| --- | --- |
| VIGIL branch | `agent/incident-ecosystem-ingestion` |
| VIGIL commit | `f3048a713667a53f14e4f3cf2b896ff1591f0f41` |
| VIGIL relation to fetched main | 0 behind, 58 ahead |
| Catalogue branch | `feat/vigil-case-files-dashboard-20261022` |
| Catalogue commit | `8419fd3f8e5521b23f926c84f3f331d92417ed21` |
| Catalogue relation to fetched main | 0 behind, 38 ahead |
| Canonical records | 200, including INC-204–209; highest ID INC-209 |
| Source records inventoried | 734 |
| Existing new party / geography structures | 0 / 0 |
| Source-reviewed pilot proposals | 5 |
| Remaining semantic reviews | 195 |
| Canonical migrations performed | 0 |

[inventory.csv](inventory.csv) is the compact per-ID matrix. [inventory.json](inventory.json) also preserves the complete existing system and jurisdiction contexts, source identities, historical access states, limitations and file hashes. Historical access labels are not claims of new external retrieval. The source-role inventory contains 458 incident-evidence, 95 contextual-background, 94 harm-evidence, 50 record-cross-reference, 15 affected-party-evidence, 14 governance-basis, seven direct-testimony and one standards-or-regulatory-basis entries.

Inventory outcomes distinguish four `reviewed-and-recorded` **pilot proposals**, one `reviewed-unresolved` pilot and 195 `not-yet-reviewed` records. `canonical_applied: false` and `canonical_change_sha: null` apply to all 200. The audit's recorded proposals must never be counted as migrated canonical records. See [coverage.json](coverage.json).

## Five proposed transformations

Each linked JSON contains the full proposed canonical objects, unchanged original context, per-source support and limitations, source-record hashes, uncertainty, original-to-new crosswalk and expected map behaviour. The two additions are `affected_party_context` and `jurisdictional_context.normalized_geography`; the dotted key in the packet is an overlay path, not a new top-level canonical field.

| Pilot | Proposed scope | Geographic relationships | Important boundary |
| --- | --- | --- | --- |
| [INC-040](VIGIL-INC-000040.proposal.json) | Cross-border | US providers / regulatory context; Singapore subsidiaries; China-linked parent companies | Subsidiary and parent associations use `other`, with their precise meaning in the basis. No affected-person or physical-execution claim. FT remains inaccessible; proposals rely on attributed secondary reporting at `source_records[1]`. |
| [INC-090](VIGIL-INC-000090.proposal.json) | Cross-border | Ukraine occurrence effects, service and institution; US operator relationship | Contested relationships remain disputed. No Russia or Crimea pin. `source_records[0]` supports the proposals; separate-event sources are excluded. |
| [INC-105](VIGIL-INC-000105.proposal.json) | Cross-border | Australia / Perth user and household; US legal referral under `other` | A referral does not establish a US harm location. A household does not represent Australia's population. `source_records[0]` supports these distinctions. |
| [INC-187](VIGIL-INC-000187.proposal.json) | Cross-border | Australian / NSW service and organisation; explicitly identified US provider headquarters | `source_records[0]` identifies the headquarters; `[0]` and `[1]` identify the affected service. Execution and hosting remain unresolved. No affected individuals are invented. |
| [INC-202](VIGIL-INC-000202.proposal.json) | Not established | No country pins; unresolved occurrence and infrastructure locations | `source_records[0]` supports research participants and technology identity. Affiliations and cloud branding do not locate runs. A controlled evaluation is not automatically non-geographic. |

All new affirmative relationships are attributed or disputed. The pilot does not upgrade historical evidence status or claim human authentication. Source URLs and section locators are in each proposal. No new sources need to be appended for these proposed claims.

## Source and interpretation holds

- **INC-040:** original FT text was not accessible. Secondary attribution is explicit. Individual subsidiary legal identities and execution locations remain withheld; no transactions or legal conclusions are independently authenticated.
- **INC-090:** preserve the contested account. No private internal command records were authenticated. The source's separate-event context does not expand this occurrence.
- **INC-105:** no server location, provider domicile or separate clinical/individual family-member conclusions are inferred. No new private identifying details are added.
- **INC-187:** service jurisdiction and headquarters are source-backed relationships; neither locates the runtime or hosting. The unnamed technology service provider stays unnamed.
- **INC-202:** the experiment's physical location remains unestablished. This is a completed geography review with a bounded unresolved result, not missing work.

These limits do not block recording the bounded proposals. A later source refresh can add a relationship only when it supplies the missing fact. The other 195 records still need substantive review; no automatic country or party extractor has pre-adjudicated them.

## False-positive classes and controls for the full pass

1. Corporate identity mistaken for execution location: require source-local location evidence and a separate relationship role.
2. Mentioned lawyer, regulator, attacker or parent company mistaken for harmed population: preserve its actual relationship, including `other` where appropriate.
3. Public service jurisdiction mistaken for hosting: allow a known service relationship alongside an unresolved infrastructure relationship.
4. Research affiliations, model release status or cloud use mistaken for physical deployment geography: retain the independent environment fields and withhold unsupported locations.
5. Global product availability mistaken for global occurrence: no global scope from brand reach alone.
6. Contested reporting rendered as settled fact: keep evidence states on each relationship and visible in the interface.
7. Several roles or countries double-counted: deduplicate by Incident ID within each country and across the filtered case list.
8. Historical source descriptions mistaken for current source access: retain the inventory's historical labels separately from actual new retrieval.

`other` is necessary in this pilot and therefore its optional globe chip will be needed after migration. It must show the source-grounded basis; it must not be silently relabelled as an affected institution. No directional arcs are authorised by these objects.

## Validation and exact delta

[validation.json](validation.json) contains command results and per-pilot checks.

- Current canonical validation: **200 pass**.
- Temporary copies of the entire corpus, with five candidate overlays: **200 pass**; **zero new failures and zero newly passing records**. No candidate overlay was applied to the canonical directory.
- All five context payloads pass the existing context validator. References resolve, baseline file hashes match and removing the two additions restores the original record exactly.
- Existing context unit tests: **11 pass**. Existing jurisdiction projection tests: **7 pass**.
- Public-record, source, interpretive, component and authorship validators pass. The source validator checked all **734 source records**.
- An isolated invalid candidate combining unresolved geography with a US assertion is rejected as expected. No permanent test or validator was changed.
- **One pre-existing generated-output mismatch:** the official public builder adds existing INC-032 / FC-035 and INC-043 / FC-088 examples to `VIGIL.FailureTaxonomy.CaseFileExamples.json`. No source finding changed. The exact official output diff is retained in [baseline-generated-drift.patch](baseline-generated-drift.patch); the working generated file was returned to its baseline bytes. The Incident, registry and jurisdiction indexes have no builder drift. This is a failed generated-freshness comparison, so this packet does **not** claim every repository check is green. Reconcile this derived output during the approved implementation pass without changing classifications.

No website code was changed, so mobile, accessibility, static/PDF output, interactive selectors and browser preview acceptance have not yet been executed. Stage C follows stable canonical migration under the handoff. No current-head CI or completed website claim is made here.

### Proposal-only count oracle

For these five proposals, All relationships / All scopes yields **5 distinct cases**, **4 with country relationships** and **1 without pins**. Country counts are US 4, AU 2, CN 1, SG 1 and UA 1. Their sum is **9**, not five, because a case can have several country relationships. The website must label that distinction.

Occurrence selects AU for INC-105 and UA for INC-090. It produces no pin for INC-040, INC-187 or INC-202. Provider/operator selects three distinct cases through US relationships. Infrastructure produces no pins. These are review expectations, not published metrics or proof of website selector implementation.

## Approved-next-step boundary

On approval, re-fetch both branch heads and compare every candidate's file/source hashes before applying it. If concurrent edits exist, re-review them rather than overwrite them. Update the 200-row inventory as actual source reviews finish and record the canonical commit for each batch. Leave an evidence-limited record unresolved when appropriate. Run the repository gates after each bounded batch, then extend the deterministic projection and integrate the catalogue exactly as its design specifies.

Schema or control changes discovered during that work still require a measured Gate 1 amendment. This packet requests approval for evidence-led migration using the existing contract, not automatic backfill, new compulsory coverage controls, taxonomy/HIM changes or merge to main.

Artefact classification: this README and five proposals are **REVIEW**; inventory, coverage, validation results and builder-drift patch are **AUDIT**. None is a runtime source or a substitute for canonical records. Temporary preparation/validation scripts are not committed as permanent machinery.
