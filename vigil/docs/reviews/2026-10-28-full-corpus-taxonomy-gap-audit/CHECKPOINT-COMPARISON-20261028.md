# Checkpoint and ingestion-linked audit comparison — 28 October 2026

This comparison preserves the older local checkpoint without replacing the completed audit. It reconciles counts and identifies the three differing provisional recommendations; it does not independently re-perform or endorse all 681 substantive reviews.

## Pinned inputs

- Original local checkpoint: `a064161c9c5386b01b8db97a79ea57d0e15775bf`.
- Existing completed audit: `8a91e925192237fe17c8233c681857bda894e3b7` on `work/full-corpus-taxonomy-gap-audit-20261028`.
- Common source baseline: ingestion `0f008d983da72db962705fb9c732496e703cdb5e`.
- Current ingestion compared: `c84b6c51f4db435175e8c8f5095823901aa9b0bd`.
- Published taxonomy: v0.9.0, main `0fdabb940cef157609e3cd2a20efa213cdfca2ef`.

The completed audit was already present remotely when this save was undertaken. Ingestion issues #133 and #176 cite that audit; their 681/115/115 figures are downstream tracking of its results, not a second independent review. The earlier conversational statement that the audit existed only locally was stale.

## Counts reconciled

| Measure | Older local checkpoint | Completed audit cited from ingestion | Fresh ingestion census |
| --- | ---: | ---: | ---: |
| Canonical Incidents | 206 | 206 | 206 |
| Strict active state | 205 | 205 | 205 |
| Monitoring included | 1 | 1 | 1 |
| Current resolved-no-mapping clauses | 681 | 681 | 681 |
| Incidents containing those clauses | 187 | 187 | 187 |
| Supplemental legacy-rationale items | 5 | Outside frozen denominator | 5 still unresolved |
| Expanded checkpoint worklist | 686 / 190 Incidents | 681 / 187 Incidents | Not a separate disposition count |
| Completed clause recommendations | 1 | 681 | Census is not review completion |
| Provisional checkpoint recommendations | 13 | Not the final audit distribution | Not applicable |

The primary populations match exactly on Incident ID, episode ID and clause position: zero missing or extra identities. All 681 current ingestion source-clause blocks also equal their frozen audit counterparts. Ingestion has newer provenance/storage changes, but those changes do not explain a different no-mapping denominator.

The five supplemental checkpoint items are INC-196 E002, INC-197 E002/E003 and INC-198 E001/E003. Each currently has `adjudication_status: unresolved`, while retaining a `no_mapping_rationale` string. They warrant consistency review, but are not five additional current completed no-mapping dispositions. The 686 figure must not be substituted for the completed audit's 681 denominator. Likewise 190 is the expanded worklist's Incident count, not the primary audit's 187.

The checkpoint's 643 attempted source URLs are another unit entirely. Its 72 failed URL requests are neither 72 evidence-limited clauses nor comparable to the completed audit's 115 evidence recommendations. A downloaded source is not a reviewed clause.

## Completed audit distribution

| Recommendation | Clauses |
| --- | ---: |
| Retain reviewed — no classification | 446 |
| Reconsider existing classification | 115 |
| Further evidence required | 115 |
| Clarify existing taxonomy | 3 |
| Convert to taxonomy-gap candidate | 2 |
| Total | 681 |

The 230 reconsider/evidence clauses affect 137 unique Incidents. The 235 total non-retain recommendations additionally include the three clarification and two conditional-gap findings. Neither number is a count of confirmed prior errors, accepted new mappings or authorised new classes.

## Actual overlapping recommendation differences

Eleven of the fourteen authored checkpoint recommendations agree with the completed audit. All three disagreements involve checkpoint recommendations explicitly marked provisional. The checkpoint's one completed recommendation, INC-003 E017 reconsideration under FC-090, agrees at the primary-recommendation level; this does not prove identical certainty or supporting class selections.

| Clause | Older checkpoint | Completed audit | What explains or remains behind the difference |
| --- | --- | --- | --- |
| INC-001 E007 | Further evidence required | Reconsider existing classification | The checkpoint could not retrieve the cited Register page. The completed packet records an accessible assets.theregister.com preservation of the July 20 repeat freeze-breach account. It proposes FC-003 reconsideration while preserving uncertainty about the exact changed operation. This is an evidence-access/review-stage difference, not a new taxonomy count. |
| INC-003 E005 | Reconsider existing classification | Retain reviewed — no classification | Both distinguish the customer workload from Modal infrastructure. The checkpoint flags the agent's root/staging operation as a possible task-pathway occurrence. The completed packet retains it as context because the external endpoint's permission model is not independently settled and the broader escape chain already has authority mappings. This is a substantive episode-scope/authority-evidence judgement requiring explicit reconciliation before any canonical decision; it is not resolved by matching the counts. |
| INC-003 E016 | Further evidence required | Reconsider existing classification | The completed packet cites the technical timeline's account that shutdown cut off the attacker's internal-network path, supporting a bounded FC-083 success test. The checkpoint had not completed that route/outcome analysis. Both reject inferring universal containment or FC-090 success merely from credential rotation. |

No current recommendation is silently replaced by this comparison. Original checkpoint bytes and its explicitly incomplete status are preserved in `checkpoints/local-a064161/`. The completed root report and final register remain unchanged. Any accepted change still requires source-first human/authorised adjudication.

## Historical numbers in issue #133

Issue #133 also preserves an 11 October census at `feac99c05a22e14816f110341dd25dea04b8f574`: 189 Incidents, 1,080 clauses, 312 mapped, 684 no-mapping, 75 unresolved and nine taxonomy-gap. It separately reports that 681 of those historical 684 no-mapping clauses lacked a distinct adjudication note. That historical **681 missing notes** must not be confused with the current **681 no-mapping clauses**. The census date, taxonomy and question differ. No inference about which particular records changed follows from aggregate subtraction alone.

## Verification and scope

`CHECKPOINT-COMPARISON-20261028.json` contains the identity checks, census, five supplemental references and fourteen overlapping recommendations. The archive manifest records the original checkpoint blobs. Publication adds only new files under this audit directory and preserves every pre-existing completed-audit blob. No canonical Incident, taxonomy, validator, production methodology or website content is changed.

References: [completed report at the comparison pin](https://github.com/CAM-Initiative/Vigil/blob/8a91e925192237fe17c8233c681857bda894e3b7/vigil/docs/reviews/2026-10-28-full-corpus-taxonomy-gap-audit/README.md), [issue #133](https://github.com/CAM-Initiative/Vigil/issues/133), [issue #176](https://github.com/CAM-Initiative/Vigil/issues/176).
