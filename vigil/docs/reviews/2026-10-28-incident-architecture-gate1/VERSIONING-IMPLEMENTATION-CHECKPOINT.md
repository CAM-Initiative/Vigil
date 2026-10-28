# Incident versioning — Gate 1 implementation checkpoint

**28 October 2026 · Implemented on draft PR #178; not yet published, merged, or Gate 2 approved.**

Repository: `CAM-Initiative/Vigil`  
Architecture head: `work/incident-architecture-gate1-20261028`  
Target: `agent/incident-ecosystem-ingestion` (NOT `main`).

## Completed, on the architecture branch only

1. Added `vigil/scripts/check-incident-publication-versions.py`, a **read-only final-main-PR guard**. It compares the exact main and candidate canonical Git records, checks reviewer-declared MAJOR/MINOR/PATCH or first-publication level, checks the numeric increment against published main, detects changed canonical mapping/disposition as minimum MINOR, rejects stale main baselines, missing/duplicate declarations, no-op version edits, and deletion of an existing canonical ID. PR declaration is one tilde-fenced `vigil-incident-release` JSON block in the **final main PR's description**, carrying source-linked reason and current-main blob/version; the guard does not interpret source evidence, verify human review, or write records.
2. Added `vigil/scripts/build-incident-publication-manifest.py`, a generated **main-only** current-publication manifest builder. It records each canonical ID/version, exact SHA256 and Git blob, last first-parent source-changing commit, commit timestamp, optional prior version, and applied taxonomy/HIM version. It never edits canonical records; unchanged source files have stable commit pins across bot-generated index commits. It is not a second canonical database.
3. Updated `.github/workflows/vigil-records.yml`: full Git history for reproducibility, changed PR-body trigger, final-main-only publication checker, independently logged isolated tests, and main-only manifest build/check within the existing records workflow before its bot commit (which stages the new manifest). PRs targeting ingestion have **no published-version check**.
4. Added `vigil/tests/test_incident_publication_versions.py` with **25 executed isolated tests** covering synthetic Git baselines, mapping revisions, partial/unknown levels, no-op edits, stale main, first-publication preservation, deletions, manifest reproducibility and uncommitted canonical changes.

**Nothing modified in:** `vigil/records/incidents/`, taxonomy, HIM, EXTREQ, schema, website or the existing historical versions. No class was re-adjudicated. The separate source-coverage and compact-history issues are not implemented by this control.

## Actual GitHub Actions results

**Run [40673992893](https://github.com/CAM-Initiative/Vigil/actions/runs/40673992893)** (architecture draft PR into ingestion):
- **Test isolated Incident publication versioning and Git history — PASS.** `Ran 25 tests in 0.483s — OK`, from job `122767606015`.
- **Final-main publication guard — SKIPPED BY DESIGN:** the current draft PR targets `agent/incident-ecosystem-ingestion`, not `main`. Synthetic Git integration checks exercise its implementation but do **not** establish that an actual main PR check has run.
- **Full VIGIL corpus and maintenance contracts — FAIL**, with two existing source-specific assertions: `test_build_vigil_records.IncidentBuilderTests.test_taxonomy_examples_are_incident_derived` expects INC126 not to occur in case examples; `test_taxonomy_classification.IncidentTaxonomyClassificationTests.test_successful_invariant_is_classified_but_not_failure_evidence` expects `classified` rather than `provisionally-classified`.
- **Pre-existing status confirmed:** a **documentation-only** architecture commit preceding the new versioning code had the same two failures in [run 40672000341](https://github.com/CAM-Initiative/Vigil/actions/runs/40672000341). These failures are not introduced by the new versioning tests. No unrelated test, record or taxonomy expectation was changed to manufacture green CI.

**Untested on the actual main publication path:** main-only manifest generation over all published records, branch-protection freshness as an atomic merge requirement, a final-main-PR body with all declared changes, and downstream catalogue/render distribution. Those require controlled validation at real main integration. Do not claim production release readiness solely from synthetic test success.

## Read-only population and stop condition

At the pinned comparison (main commit `0fdabb940cef157609e3cd2a20efa213cdfca2ef`, ingestion `0f008d983da72db962705fb9c732496e703cdb5e`), **53 existing canonical Incident files differ and six new Incidents (INC210–INC215) are staged**. The ingestion geography sidecar still contains only 200 entries and has a stale INC001 version; direct canonical files and Git diff govern. No semantic major/minor/patch decision has been generated for the 53 changed records. Nothing has been renumbered. New staged records INC213 and INC214 already have version `0.1.1` and must keep that initial publication history.

**STOP for Gate 2:** Before changing any of the 53 existing record versions, or touching bulk source evidence/provenance in the 206-record ingestion corpus, run the new guard read-only on a final-main integration candidate, report missing/incorrect declarations with exact Incident IDs and current-main changes, resolve the two unrelated baseline CI failures in their appropriate workstream, and obtain the separate human-maintainer authorisation required by `vigil/MAINTAINERS.md`. The main-only manifest is not published until a governed merge; do not bypass the conditional check to simulate success.

## Remaining design/implementation considerations

- A GitHub PR description is machine-parseable publication metadata but does **not** certify human review or source-first sufficiency. Human governance remains independent.
- Set GitHub branch-protection checks / merge queue to require a fresh-main passing run; this draft cannot independently modify repository protection settings.
- Confirm public website projections and publication manifest agree on the *actual* main source tree and that the generated-only bot commit does not create a false new Incident version.
- Before broad initial rollout, add a reviewer-friendly read-only declaration/preflight generator for the 53+6 final integration candidates, with review-required placeholders that cannot be mistaken for approved classifications.
- After this versioning Gate 1, separately seek storage/review-posture Gate 1 and subsequent Gate 2 approvals for #168 and #176. Do not let the version-control PR implicitly approve them.


## Follow-up publication-gate verification — 28 October 2026

A separate `.github/workflows/incident-publication-gate.yml` is now on the draft branch in commit `0afd18003deaa5bb3b232721b83d57176ef66000`. It runs the isolated versioning/manifest tests on PRs to the ingestion branch and, without path filters, runs the published-main version checker on every PR targeting `main`. This gives documentation-only PRs a successful check result without requiring the unrelated full corpus suite to pass.

The dedicated check passed in [Actions run 40678150978](https://github.com/CAM-Initiative/Vigil/actions/runs/40678150978): **25 isolated tests passed**. The existing VIGIL records run [40678150968](https://github.com/CAM-Initiative/Vigil/actions/runs/40678150968) still fails only on the two known baseline assertions: INC126 taxonomy exemplar eligibility and the successful-invariant classification expectation.

**Current main ruleset state — read-only checked 28 October 2026:** ruleset `26034000`, “VIGIL — Protect main,” is **active** and targets the default branch. It blocks deletion and non-fast-forward updates. It does not currently require pull requests or required status checks. This confirms existing main protection; the outstanding gap is mandatory PR/status-check enforcement. **No ruleset changes were made.**

### Generated-output compatibility assessment

Two workflows currently commit generated outputs directly to `main`: `.github/workflows/vigil-records.yml` updates the registry indexes and Incident publication manifest; `.github/workflows/taxonomy-publications.yml` publishes taxonomy outputs and its PDF. A future require-PR rule must convert both writers to open or update generated-output PRs rather than push to `main`.

Those PRs need a token that triggers their validation workflows. GitHub documents that events created with `GITHUB_TOKEN` do not start new workflow runs except for `workflow_dispatch` and `repository_dispatch`; it recommends a GitHub App installation token or PAT for events that must trigger workflows. A repository-scoped publisher GitHub App with only `contents:write` and `pull_requests:write` is the narrower fit. See [GitHub’s GITHUB_TOKEN guidance](https://docs.github.com/en/actions/concepts/security/github_token) and [workflow trigger guidance](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

The records publisher must build from settled main, push to a dedicated automation branch, and open/update a PR containing the generated indexes and manifest. The taxonomy publisher must run after the records projection has landed, then prepare a separate taxonomy-output PR; the current `workflow_run` ordering would otherwise publish taxonomy outputs from main before a records-output PR has merged. Both generated PRs can use the dedicated pathless `Incident publication gate / publication-check`; the taxonomy PR should also retain its taxonomy-specific validations. Do not require the unrelated red full-suite check as a substitute for this publication gate.

This writer conversion has not been applied in this versioning PR: neither workflow currently references a dedicated publisher app credential, and the active ruleset was not changed. It is separate implementation work required before enabling mandatory PR/status-check enforcement. PR #178 remains open and draft against `agent/incident-ecosystem-ingestion`; the PR diff still contains no canonical Incident record changes.
