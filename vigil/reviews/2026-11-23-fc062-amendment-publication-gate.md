# FC-062 amendment: concrete publication approval packet

Status: prepared for maintainer approval, unpublished. 23 November 2026.

## Exact scope

Clarify existing FC-062 Epistemic Reliance Calibration, without creating a class or family. The exact proposed JSON is in `vigil/taxonomy/families/VIGIL-FF-0003-verification-completion-integrity.json`. This reproduces only the FC-062 proposal from `work/fc062-operative-reliance-incident-reconciliation-20261123`; no Incident changes from that branch are imported. Published metadata remains v0.9.2; one `working_release` proposes v0.9.3, patch, unpublished.

The amendment explicitly includes attributable operative interpretations of file, tool, environmental, system and conversational state when they guide consequential action. It requires traceable evidence of interpretation and uptake, judges assurance using information reasonably available at the decision point, and rejects hindsight-only error or presumed hidden belief. An effective pause or chosen action must substantiate success; verbal recognition alone is insufficient. Existing drafting-fitness obligations and literal exclusions remain intact. A new all-role exclusion addresses deliberate crossing of a correctly understood boundary without a separate assurance/reliance defect.

## Reconciliation with the completed corpus review

The completed review is pinned at `8d4c2642acc7820ab0e33a8a0b9160dde89a97bc`, under `vigil/docs/reviews/2026-11-23-fc062-full-corpus/`. Its 233 completed dispositions were tested against published v0.9.2, not this amendment. The review establishes a documentation need concerning operative interpretations, but its candidates are not automatic mappings under v0.9.3. Recheck exact amended conditions and exclusions for each affected episode after publication, including contemporaneous warrant, scope-only misconduct and independent defender attribution.

Preserve the review's 36 existing mappings and 61 clause relationships in before/after decision history. Resolve INC-103's empirical-scope/reliance uncertainty specifically; the amendment does not turn contemplative content into factual reliance. Refine INC-007's basis, retain the explicit AI-contribution limits on INC-222–224, and preserve mixed earlier-failure/later-success episodes in INC-086/170/201/202. Generate canonical Boundary objects only for positively engaged, unresolved-polarity findings against the actually published criteria. Retest the seven final-review promotions (137/154/183/184/185/186/205); multiple diagnostic properties do not multiply the single event or mechanism.

The Perception research recommendation on this branch remains preserved: no independent new class is admitted. Clarification of FC-062 is the bounded normative proposal; it does not retroactively approve, retire or rewrite those research candidates.

## Existing PR and required decision

Existing draft PR #195 targets main from this dedicated taxonomy branch and currently describes research-only work with no normative family change. Publishing this local proposal to that branch would change its reviewed scope. Do not silently push it into that research-only PR while leaving that scope unchanged.

Maintainer decision requested: approve this exact FC-062 wording and single unpublished v0.9.3 proposal, and authorise repurposing draft PR #195 to review and merge the amendment with the preserved research history. This also needs its PR title/body/scope statements updated before review. No new PR has been opened; no existing PR has been edited, marked ready or merged for this packet.

After the approved taxonomy PR merges, the existing main-only publication workflow consumes the single working release, stamps the actual publication date and final digest, and renders the taxonomy. Verify the completed workflow and published main version before synchronising the Incident review branch. Do not invoke the release preparer on this unmerged branch.

Then apply source-first approved Incident changes, record before/after decisions and provenance, reconcile clause relationships/reciprocal exemplars and Boundary objects, rebuild public data and validate. Prepare the implementation PR text/diff for maintainer approval; do not open that PR without explicit authorisation.

## Executed validation

- Taxonomy working-branch validation passed: 18 families, 83 classes.
- Single-release guard passed: published main 0.9.2; one unpublished 0.9.3 candidate; published release history unchanged.
- 18 existing release-mode/invariant-semantics tests passed. Test messages mentioning prepared releases refer to temporary fixtures, not a publication event.
- No schema, validator, Incident, HIM or generated-output changes.

## Authority and preserved heads

- Published main: `0a340103cd84715232b3f20584331083db4c6be1`.
- Existing dedicated taxonomy head: `ed3f1e7ad55195485893f676b32c8def9ebee986`.
- Comparator proposal head: `09f5392ca3db9c7396cb1e5572ce877c65fd26c8`.

## Maintainer approval — 24 November 2026

The maintainer explicitly approved the amendments and continuation under the earlier instruction set, including repurposing draft PR195 for review, merge and publication. The preparation-stage pending-approval statements above remain historical. Execution must verify CI and actual publication before Incident reconciliation. Implementation PR remains for separate approval.
