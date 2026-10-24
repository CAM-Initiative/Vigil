# Review notice board and repository cleanup — maintainer policy

**Authority:** VIGIL repository maintenance procedure, not a taxonomy criterion, Incident finding, or harm-scoring rule.

## Ownership: where accepted work belongs

| Content | Durable home | /docs/reviews lifecycle |
| --- | --- | --- |
| Occurrence evidence, episodes, admissible or excluded taxonomy relationship, material non-admission, missing decisive recognition fact, harm or external-requirement interpretation | Canonical `vigil/records/incidents/VIGIL-INC-*.json`, with source and version provenance | Temporary source-first review worksheet; retire after reconciliation |
| Reusable adjudication procedure, source-admission rule, definitions of evidence/completeness, release controls or maintenance instructions | `vigil/docs/maintenance/`, with change approval and dated rationale where needed | Draft method here while discussing; promote the accepted rule to maintenance |
| Normative taxonomy, Harm Impact Matrix, registered governance source, EXTREQ metadata or schema | Its existing governed canonical subsystem; operational guidance belongs in `docs/maintenance` | Never substitute a dated review for these authorities |
| Executable validation logic or reusable tests | `vigil/scripts/`, `vigil/tests/`, CI/workflows or other appropriate maintained code | Tests and scripts must not require a retired notice-board file at runtime |
| Temporary checklists, criterion matrices, source search trails, draft proposals, bulk copied JSON, inventories, progress files, generated logs or exploratory decisions | Current working branch/PR notice board, CI artifact, or local scratch | **No presumption of permanent retention**; retire at closeout |
| Prior versions and process chronology | Immutable Git history, commit/PR links and CI run artifacts | Not a separate continuously accumulating second database |

**Invariant:** `vigil/docs/reviews/` is a **temporary notice board** for ongoing work; it is not a permanent repository of record, a shadow adjudication database, or a normative dependency. Neither Git-tracked existence nor a `review_reference` makes a review packet authoritative. Once a campaign closes, a reader should be able to understand the substantive current finding from its Incident and the other governed sources, without needing the temporary notice board.

## Working → accepted → retired

1. **Open a bounded work area.** During a live campaign, dated per-Incident packets may be created in `vigil/docs/reviews/<campaign>/` to help multiple agents/humans compare version-pinned criteria, evidence, exclusions, missing facts and previous findings. They are *working material*, not independently authenticated decisions. Include campaign/PR ownership and active status in its root README or ledger.
2. **Adjudicate source-first.** Apply [ADJUDICATION-ROOT-CAUSE-CORRECTIONS.md](ADJUDICATION-ROOT-CAUSE-CORRECTIONS.md): derive the provisional finding from sources and exact criteria independently **before** comparison with stored verdicts. A repeated correction fixes an applicable method error, not a case-specific answer table. Do not skip criterion/exclusion/negative-candidate analysis merely to reduce files. Keep historical and provisional outcomes distinguishable from final supported ones. Required semantic checks happen **before** updates to the canonical Incident.
3. **Promote decisions.** Before campaign closeout, ensure every materially supported occurrence finding, rejection, unresolved candidate, scope limitation and rationale required to interpret VIGIL's current decision is reflected in canonical Incident clauses/mappings/interpretation/provenance, with exact relevant source and taxonomy-version references. Do not dump work logs, exhaustive lists of trivially irrelevant classes, CI narrative or a second decision matrix into the Incident. If current canonical fields cannot express a genuinely necessary decision, seek a bounded schema/workflow decision in `docs/maintenance` rather than making the packet permanent by default.
4. **Promote reusable methods.** Move any adopted general method or procedural control to `vigil/docs/maintenance/`; place normative changes in their actual governed subsystem. Update live code, links, tests and guidance. Remove dependency on the notice-board path. The move must not itself silently change an Incident finding, source state or class criterion.
5. **Exit audit.** Run the repository dependency inventory and CI. Confirm that relevant accepted findings and methods have a durable owner, zero newly broken canonical references, and no live runtime/build/documentation requirement for retiring files. Replace historical `review_reference` values only with valid, evidence-preserving provenance (for example, a pinned commit of the superseded packet where the field contract permits), never with a fabricated approval or an unfounded replacement. Record exceptions with exact owner and closure condition.
6. **Retire the notice board.** Delete completed campaign worksheets, duplicates, scratch files and logs from the active branch in a reviewable Git commit, pinning the pre-deletion commit and any promoted paths in the PR. Git history remains accessible. The goal at final release freeze is no historical review collection in the citable scientific snapshot. Do not rewrite Git history or merge/tag as part of housekeeping alone.

## Routine schedule and safeguards

- **At each campaign / PR closeout:** perform steps 3–6 as part of Definition of Done; an open campaign is explicitly exempt while it is doing real work.
- **Monthly (when maintenance is undertaken):** inventory `docs/reviews` by campaign; flag completed/orphaned workspaces, ownerless files, unresolved references and any hard runtime imports. This is a light hygiene pass, not a corpus-wide semantic re-adjudication.
- **Before scientific release or dataset tag:** run the full exit audit, resolve or explicitly block archival exceptions, and establish the final snapshot on approved merged `main`; a PR-head preflight is not a final scientific manifest.
- **Do not delete active v0.8.0 SIAI reconciliation packets while the parallel adjudicator is using them.** No clean-up decision may retroactively mark its source-first adjudication as completed.
- **No blanket purge of currently referenced historical packets.** References are *migration blockers*, not proof of permanent value. Check the canonical decision before retiring them. Preservation by Git history is not proof that the canonical Incident now contains all required information.
- An audit log or working packet may be committed to permit handoff and distributed review, but its presence in the Git tree is not permanent status or an obligation to publish it. Do not open GitHub Issues simply to store process notes or unknown vendor internals.

## Mechanical audit and closeout evidence

`vigil/releases/siai-2026/audit_repository_retention.py` inventories tracked paths, canonical review references, links and prospective candidates. Treat its buckets as **discovery and migration worklists**, never retention orders or automated permission to remove substantive evidence. It does not replace checking content, relative Markdown links or uniqueness of source-first decisions.

Record at closeout in the existing PR: campaign, branch, count of retired files, pinned recovery SHA, where accepted Incident/method changes were promoted, unresolved blockers, zero new dangling references, and CI result. The PR is the lightweight notice-board closure report; there is no requirement for another permanent audit directory.

**Existing 1.0.0 transition:** the pre-closeout cleanup and its historical recovery SHA are recorded at `vigil/releases/siai-2026/REVIEW-CURATION-20261024.md`. That report is a release-specific progress record, not an exception to this lifecycle. Earlier wording that said review packets must be “retained” indefinitely is superseded by this workflow.
