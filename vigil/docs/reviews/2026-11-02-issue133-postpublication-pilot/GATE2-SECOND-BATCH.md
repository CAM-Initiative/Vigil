# Issue #133 — second two-record Gate 2 implementation and source-first release handoff
3 November 2026 · Source baseline `main@5c7a779c1a5053637d2fe94f63ae30a3159146a0` · Working branch `work/issue133-postpublication-source-first-pilot-20261102`

## Authority and extent

After the P2 six-case source-first review explicitly nominated **INC-024 E004** and **INC-101 E001** for the next narrow two-record Gate 2 batch, the maintainer instructed **“lets continue”** in the immediate context of those proposed repairs. This is interpreted only as authorisation to complete the **two pre-described Incident content repairs, matching projection maintenance and research checkpoint** on the existing working branch. It is **not** permission to open a pull request, merge to `main`, alter normative Fidelity Class definitions, bulk-edit the historical no-mapping population or skip validation. The earlier `P2-STRATIFIED-SOURCE-REVALIDATION.md` is a historical pre-authorisation research snapshot; this document supersedes its “no canonical edit yet” state for these **two IDs only**.

## Source-first results and actual content commits

### INC-024 — two independently observed access-state failures; no duplicated aggregate map

- File: `vigil/records/incidents/VIGIL-INC-000024.json`
- Published main base **v1.3.15**, blob `4a37d7ac6c59116e7a7a4d2808d988820227e883`; authored **v1.4.0**, blob `f936a011da4d7c944385f4c322b051dc036541a5`.
- [Content commit `f8169daa`](https://github.com/CAM-Initiative/Vigil/commit/f8169daacebb920c6dcd0938e013aea71913fe48).
- **Episode E004: `resolved-no-mapping` → `mapped`; FC-032 failure-occurrence**, contemporaneous TechRadar source `source_records[0]`. Reporters regained login while prompts remained unusable; the free-account model-unavailable interface recommended switching model; the reporter tried the switch without receiving a reply. This is distinct from the previously accepted E003 error: an unused free account misrepresented as having exhausted its allowance and presented a paid-upgrade route. Both are different episode-local observations under **the same existing top-level FC-032**; no duplicate aggregate class.
- Current class recognition: materially distinct authenticated/model/service states; a misleading single-model recovery suggestion insufficiently distinguished the still-impaired prompt service for the observed account; reporter-tested continuation failed. Excludes universal account/model unavailability and a diagnosis of root cause.
- Official [Anthropic status chronology](https://status.claude.com/incidents/f00h6l76tsjs) was independently recovered on 3 November (contrary to an obsolete earlier note): web, API and Code elevated errors with partial repair and 17:42 UTC resolved. Inconsistent clock values in the API recovery update **remain acknowledged**, not silently harmonised.
- Existing **S3**, all twelve HIM dimensions, two external requirement assessments and old source record bytes unchanged. Coverage remains complete. No unsupported paid purchase, monetary harm or independent governed service obligation added. `taxonomy_version` updated from 0.8.1 to current published 0.9.1 because its current recognition conditions were applied; previous mapped role is unchanged.

### INC-101 — deployment-evidence reliance failure separate from model sycophancy

- File: `vigil/records/incidents/VIGIL-INC-000101.json`
- Published main base **v0.1.25**, blob `563147e574c1f4a76114afd8f04cfd09e6cf8595`; authored **v0.2.0**, blob `419f46ec00fc2087000e4b7730c62b411862e302`.
- [Content commit `bd002df7`](https://github.com/CAM-Initiative/Vigil/commit/bd002df77ac281a918c698ef4a3b6c4f28ec1576).
- **Episode E001: `resolved-no-mapping` → `mapped`; new aggregate secondary FC-062 failure-occurrence**, family FF-0003, high confidence, under current published v0.9.1 class definition.
- [OpenAI’s 2 May 2025 retrospective](https://openai.com/index/expanding-on-sycophancy/), “Why did we not catch this in our review process?”, explicitly states aggregate offline and A/B testing appeared positive; some expert reviewers felt the behaviour was off; no sycophancy-specific deployment evaluation existed; decision-makers intentionally gave greater weight to the favourable scores and launched. The released update’s acknowledged sycophancy and rollback demonstrate a material reliance consequence. **This is a mismatch between the assurance of the evidence and its use to approve release**, not proof that metrics were fabricated or that a particular omitted test was falsely declared complete.
- **Do not convert** FC-016 (no demonstrated false completion claim) or FC-030 (the positive and qualitative signals were considered together; no demonstrated disconnected correlation). The prior E002 **FC-066** failure and the FC-051/065/082 **ambiguous-boundary** classes, including their existing explicit review limitations, remain intact. Old E005 training hypotheses and source/access limits are unchanged.
- Existing **SU (unbanded harm)** retained: no demonstrated bounded harmed cohort eligible for aggregate severity. All twelve HIM dimensions unchanged. In the **sparse** `VIGIL.Harm.Dimensions.Index.json`, INC-101 correctly has **no assessed-dimension entry**. Six independent existing external requirements and all their original polarity/results unchanged; this includes the separately identified existing release-approval-criteria finding, so no duplicate FC-derived normative assessment was created. `taxonomy_version` updated from historical 0.6.9 to current 0.9.1 to mark the live new class fit; the other legacy boundaries were not promoted.

## Generated outputs and independently compared deltas

All four affected deterministic projections committed together as [`eba36390`](https://github.com/CAM-Initiative/Vigil/commit/eba3639007be118dcb3fbaaa3a18928ccc7a6fe2):

| Maintained artifact | Current blob | Independent before/after verification |
| --- | --- | --- |
| `VIGIL.Incidents.Index.json` | `b2ad823a2b4f4141dd735a11a8446ecc73a876d0` | **209** records; exactly INC-024 and INC-101 entries changed; INC-101 gains a single secondary FC-062 role and corresponding repair class |
| `VIGIL.Harm.Dimensions.Index.json` | `3dd3166548b8c39acffdaf2c3e16eb57404b682a` | **140** assessed-dimension entries; only INC-024 version changed; its dimensions identical; INC-101 remains correctly excluded as SU |
| `VIGIL.Incidents.Jurisdictions.Index.json` | `b27de109633d8dea2d36e842d4dccb00c22c4a3e` | **209** records; exactly the two incident and legacy-projection version fields updated; all geography relations unchanged |
| `taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json` | `9d26721117a2a4c5f4b3c9ce201d1700d73a6d9b` | Existing INC-024 FC-032 failure explanation refreshed; new INC-101 FC-062 failure example only; no successful/ambiguous-boundary example changes |

Method: initial generated blobs were round-tripped with the exact sorted-key JSON convention (unsorted jurisdiction), checked against the existing published-main canonical projections, and modified only for the affected record source fields. Four Git blobs were committed as one tree, then separately refetched and compared against the prior blobs. This validates the intended **focused projection data delta**, not the result of running the repository Python builder itself.

`VIGIL.Registry.Index.json` stays unchanged because total public Incident count and index locations did not change.

## Targeted validation performed

**Pass, connector-side checks:**
- Both revised JSON records parsed, use correct independent **MINOR** version increments, and preserve source records, jurisdictional/system fields, external assessment content and legacy class identities/roles.
- Both original 5-episode identity sets retained. Exactly E004 in INC-024 and E001 in INC-101 change from no mapping to a source-linked class finding; all other episode statuses and existing class relationships retained.
- No duplicate aggregate class ID; original failed/boundary roles preserved; every mapped episode has an active canonical relation and each class maps to its current published family. `adjudication_coverage.status=complete` is consistent with both records' statuses.
- Source-record references resolve; external requirement source-episode and numeric indices resolve, with no new downstream requirements inferred from FC polarity.
- Twelve original HIM dimension assessments unchanged in both cases, INC-024 overall S3 and INC-101 overall SU unchanged; sparse sidecar exclusion of unbanded INC-101 preserved.
- Public prose patterns corresponding to the repository's taxonomic numeric shorthand/maintenance-language screens were checked over summaries, governance narratives, source clauses and existing class rationales; no hits.
- Independent generated before/after comparison confirms exactly two Incident index changes, one sparse HIM version change, two jurisdiction version changes and only the described two taxonomy example effects.
- Branch after projection commit: **25 commits ahead / 0 behind** `main` as checked on 3 November. Main remains `5c7a779c1a5053637d2fe94f63ae30a3159146a0` at that checkpoint.

**Still not run:** actual Python validators, full unittest discovery, production deterministic builder, provenance audits, taxonomy case-example publication filter, CI, main release/publication guard. GitHub Actions has no run for this research branch. These are **not** claimed to pass. The maintainer explicitly declined manual Actions navigation due to workflow clutter; no new manual task is assigned to them.

## Proposed exact PR release declaration (not submitted)

This declaration must be checked against freshly published `main` before any future PR or merge. Use the production gate's **tilde-fence** syntax as required by `check-incident-publication-versions.py`:

~~~vigil-incident-release
{"records":[{"incident_id":"VIGIL-INC-000024","level":"minor","reason":"Add distinct source-reported ineffective model-switch continuation advice as E004 FC-032 failure without duplicating the existing E003 access-state class.","base_version":"1.3.15","base_blob":"4a37d7ac6c59116e7a7a4d2808d988820227e883"},{"incident_id":"VIGIL-INC-000101","level":"minor","reason":"Admit E001 FC-062 deployment-evidence reliance failure from provider-acknowledged incomplete sycophancy evaluation while preserving earlier model-output and boundary findings.","base_version":"0.1.25","base_blob":"563147e574c1f4a76114afd8f04cfd09e6cf8595"}]}
~~~

The PR would also include the **previously authored INC-003 and INC-176 MINOR releases** on this same branch; if submitting a combined PR, the declaration must cover **all four** amended canonical Incidents, not merely this batch. `MAINTAINERS.md` requires **separate explicit approval to open a PR**; this packet does not supply it.

## Remaining #133 scope

Historical 28 October **681** audit-origin no-mapping episodes were rebaselined to **672** surviving no-mapping on published main. After the existing branch repairs **INC-003 E017**, **INC-176 E002**, **INC-024 E004** and **INC-101 E001**, **668** of those original historical identities remain no-mapping on the working branch, *not* a whole-current-corpus count. No other P2 no-mapping dispositions were changed. Issue #133 remains open; the next source-first batch must continue separating human/external defender protections, missing evidence, real class-fit gaps and material facts that are not distinct new classification occurrences.

**No PR, merge, schema, normative taxonomy edit, website publication or historical corpus mass reclassification occurred.**
