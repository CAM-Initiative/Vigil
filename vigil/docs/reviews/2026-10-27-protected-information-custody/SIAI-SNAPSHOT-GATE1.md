# Gate 1 proposal: preserve the released SIAI snapshot during later taxonomy development

**27 October 2026 · REVIEW · superseded by authorised retirement**

The maintainer subsequently directed removal of the obsolete SIAI guard. The proposed pinned-snapshot job below was not implemented. `.github/workflows/siai-research-preflight.yml` has been removed, including its immutable-snapshot and historical release-validation jobs. The normal taxonomy, Incident, standards and provenance workflows remain active. The v1.0.0 tag, released files and historical snapshot scripts are unchanged and remain recoverable. The pipeline-state test no longer tries to read the deleted workflow; its retained assertions are unchanged.

Observed at PR #172 commit `30d846b90eefe6ee85b85f5ce12ed3770d394463`: [SIAI immutable-snapshot failure](https://github.com/CAM-Initiative/Vigil/actions/runs/40507072077/job/122198978332). The current branch's taxonomy, external-governance, branch-ownership and VIGIL-record jobs passed. The SIAI workflow's separate current-branch `release-validation` job also passed, including the full regression suite.

## Current behaviour and observed failure

`.github/workflows/siai-research-preflight.yml` runs its `immutable-snapshot` job against the current branch/PR checkout. `vigil/releases/siai-2026/build_research_snapshot.py` inventories HEAD while requiring exactly 200 Incidents and taxonomy metadata `0.8.1 / 17 families / 80 classes`. Its error is `Unexpected published taxonomy metadata; expected 0.8.1 / 17 / 80`.

The approved working proposal correctly contains 18 family objects and 82 classes while preserving the published v0.8.1 release ledger. It therefore fails the old research snapshot's inventory assumptions. Updating those constants to accept the new taxonomy would misrepresent a changing branch as the frozen SIAI paper baseline. No script or workflow has been changed to bypass this failure.

## Proposed bounded repair

Pin only the SIAI `immutable-snapshot` job's source checkout to the already released **v1.0.0** snapshot, at immutable commit `8294c4f3eec1e5ad6f12ab7b75aabb7f69ddba9f` (verified tag target). Label the uploaded manifest explicitly as the v1.0.0/SIAI snapshot. Run the existing checksum builder and checker on that source. Remove the current-branch `--require-main` dispatch from this pinned job, because a released-tag checkout is deliberately detached, and verify the selected immutable commit instead.

Keep `release-validation` and the taxonomy, external-governance and Incident CI jobs on the current PR head. They must continue to validate the actual new family, class content, source requirements and release proposal. Do not weaken the snapshot builder's existing 200 / 0.8.1 / 17 / 80 expectations or rewrite the frozen release artefacts. Do not amend Incident data, taxonomy criteria, source access or legal applicability.

The unchanged builder was run read-only against that exact released commit: it passes with 200 Incidents, 17 families, 80 classes and published taxonomy v0.8.1. Its SHA-256 entry-stream digest is `8838c7600cde3a03496964c8a35c959c6d4ecad9ead411ce7f51ebff8908abf0`. The same unchanged builder reproduces the stated error for the current proposal commit. No workflow or builder change was needed for this comparison.

## Pass/fail delta

- The current 18-family/82-class taxonomy PR would pass the SIAI immutable job only if the separately selected released v1.0.0 source satisfies its original checksum and inventory rules. Its current content remains subject to the other unchanged CI jobs.
- A modified or wrong pinned snapshot commit, an inventory mismatch within the released source, or checksum mismatch would still fail.
- Later ordinary Incident additions or approved taxonomy changes would no longer fail solely because the SIAI job mistakenly treats current HEAD as the frozen paper dataset.
- This changes which source the publication job attests to. It does not change what canonical Incident content passes any validator.

## Affected surfaces, impact and risk

Affected surface: one workflow job and its manifest label/source-identity verification. No Case File stage, canonical record field, taxonomy recognition rule or public dataset is changed. Current corpus impact: **zero canonical Incident edits**. The CI rejection is reproducible on this one taxonomy PR. A broader inventory of future branches is unnecessary for this bounded source-selection repair.

Main risk: a pinned-release job could be mistaken for validation of current PR content. Explicit release/source labels and preservation of the independent current-head jobs are required. Do not claim the frozen check validates the proposed taxonomy. No destructive migration or evidence rewrite is necessary.

Why this enforcement point: the failure comes from the workflow selecting current HEAD for a release-specific builder. The proposed fix corrects that selection instead of changing a frozen paper contract or making canonical records conform to it.

## Approval and stop condition

`vigil/MAINTAINERS.md`, **Human-maintainer stop conditions for validators, schema rules and corpus-wide tests → Gate 1**, requires: “Before editing any validator, schema rule, permanent test, builder rule or publication guard that can change whether canonical Incident content passes or fails, the agent or maintainer must first present the proposed change to the human maintainer and STOP.” It also treats uncertainty about the control as grounds to seek approval.

This repair changes a publication job's attested source, so it is presented for explicit approval even though it does not alter canonical Incident validity. The existing class-design approval does not by itself authorise this release-workflow change. After approval, implement the bounded source selection, verify exact released-commit identity, rerun frozen and current-head checks, and stop again if any failure would require canonical data or publication-history changes. ISO source access remains a separate blocker.
