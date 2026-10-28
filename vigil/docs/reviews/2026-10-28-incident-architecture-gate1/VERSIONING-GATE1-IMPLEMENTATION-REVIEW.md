# Versioning implementation — exact Gate 1 decision and handoff

## Approval and implementation disposition — 28 October 2026

**APPROVED:** Following the explicit Gate 1 disclosure in this paper, the human maintainer approved the final-main-PR-only version checker, declared semantic level, published-main arithmetic, staged-first-publication preservation, stale-main rejection and main-only deterministic manifest. This narrow approval was implemented on draft PR #178. Isolated synthetic Git tests **25 PASS**; the two full-suite failures predate this work. **Not implemented on main; not approved:** bulk source edits, version re-stamping of 53 changed records, schema changes for compact review history, challenged-status fields or website changes. Full evidence and run links: [implementation checkpoint](VERSIONING-IMPLEMENTATION-CHECKPOINT.md). The earlier 'request' below is retained as the historical decision proposal, not an unresolved request for the same implementation.


**28 October 2026 · Narrow versioning Gate 1 approved and staged, not published · Working branch `work/incident-architecture-gate1-20261028` · Draft PR #178 into `agent/incident-ecosystem-ingestion`.**

**Already approved, without source-code change:** Incident numbering means *MAJOR = exceptional identity/scope incompatibility; MINOR = material evidence/adjudication (including **every new or removed canonical taxonomy mapping**); PATCH = non-substantive record maintenance; NONE = unchanged*. Incident IDs and versions are independent of corpus/taxonomy versions; legacy numbers are grandfathered.

**This document requests the separate, exact Gate 1 implementation decision** described in `vigil/MAINTAINERS.md` §Human-maintainer stop conditions. Approval of the numbering meaning alone is **not** approval to edit publication controls.

## 1. Current behaviour

- `record_identity.version` and `record_identity.updated` already exist. `vigil/templates/incident-record-template.json` initializes a **newly created** Incident at `0.1.0`; current stored versions are retained, not renumbered.
- `vigil/scripts/validate-vigil-records.py` checks many structural and semantic Incident rules but does **not** compare the canonical file's version with a previous published-main version on every PR.
- `.github/workflows/vigil-records.yml` runs on PRs, main and the dedicated ingestion branch, builds/reconciles generated public projections, **rejects CI mutation of canonical records**, and bot-commits generated indexes on main only.
- `vigil/scripts/build-vigil-public-records.py` projects `record_identity.version` into `record_version` for the public index and into the sparse HIM sidecar; a downstream jurisdiction projection may be stale independently. `.github/workflows/taxonomy-publications.yml` runs after the records workflow on main and can itself commit generated taxonomy output.
- A generated per-Incident immutable revision publication manifest does **not yet exist**.
- `main` at `0fdabb940cef157609e3cd2a20efa213cdfca2ef` publishes **200 versioned Incidents** (128 at major 0; 71 major 1; INC032 `2.0.7`). The pinned ingestion source at `0f008d983da72db962705fb9c732496e703cdb5e` has **206 canonical Incidents**. Git comparison shows **53 modified existing** files and **six added (INC210–INC215)**; only those six are unpublished new IDs. The ingestion jurisdiction index still enumerates 200 and even has a stale INC001 version, so do not treat that index as authoritative.
- No established evidence proves that the historical 200 versions were numbered according to the new policy; never retroactively reinterpret them.

## 2. Proposed behaviour — keep separate the policy and arithmetic

**Stage A (non-mutating PR preparation, final PR targeted to main only):**
1. Read the **fresh, exact published main canonical record blob** for each altered Incident and compare it to the final proposed canonical JSON, ignoring **only** `record_identity.version` and `record_identity.updated` for detecting substantive *payload* differences. Do **not** ignore review provenance, taxonomy, HIM, source or EXTREQ material.
2. Require a **reviewer-authored per-Incident change declaration** identifying classification `major`/`minor`/`patch`/`none`, source/episode evidence, specific field paths and why the level applies. Code can compute obvious lower bounds (e.g. changed canonical `class_id` or `classification_role` requires at least minor); it cannot claim to prove semantic significance from field names or tokens.
3. When the Incident exists on published main, calculate **once, at the highest applicable declared change level**, from **main's published value** (not current ingestion version):
   - major: `X.Y.Z -> (X+1).0.0`
   - minor: `X.Y.Z -> X.(Y+1).0`
   - patch: `X.Y.Z -> X.Y.(Z+1)`
   - none: unchanged
4. When the Incident is **absent** from published main, retain its actually approved, already-staged authoring version on first main publication (`INC213` and `INC214` already `0.1.1`); do not treat that version as an increment over a nonexistent main baseline.
5. A candidate stamp is **unpublished until the PR lands on main**. If the same record's main blob changed after candidate preparation, **fail** and require a full source-first merge/reconciliation, then recompute the candidate. If the branch's historic provisional stamp differs from the correct published-main candidate, preserve its decision history while preparing the new stamp; do not silently discard it.
6. Do **not** enforce final-main publication arithmetic on feature PRs targeting `agent/incident-ecosystem-ingestion`. This lets the 53 already-edited records and future small commits remain working state without manufacturing releases. No unrelated record is bumped.

**Stage B (PR check, read-only):**
- Deterministic helper `vigil/scripts/check-incident-publication-versions.py` (proposed name, not yet created as production tool) checks exact main SHA/blob freshness, declared change level, numeric candidate, first-publication preservation, any known mapping-role lower bound, idempotent unchanged records, record-identity stability and coverage of every modified/new/deleted Incident. No direct writes or AI classification are allowed in this guard.
- Proposed wrapper in `.github/workflows/vigil-records.yml` should run **only for final PRs whose base ref is `main`**, after checkout/fetch of current main. Require up-to-date branch protection or merge queue to prevent another main advancement between a green check and merge. A running CI job by itself is **not an atomic lock**.
- A separate explicit preparation helper may stamp **only** reviewed candidate `record_identity.version` on a working final integration PR. That helper is invoked by the author/reviewer, *not* automatically by main publication CI.

**Stage C (main publication, generated metadata only):**
- After main merge, derive a manifest of `incident_id`, released version, canonical path, exact file content digest, **canonical input commit/tree**, effective publication date, applied taxonomy/HIM editions and predecessor revision if known. Avoid including the bot-generated manifest commit's own hash in its content, which creates a hash loop. Re-run idempotently.
- Publish and validate generated registry/case-file/HIM/geography outputs from the same canonical snapshot. Stage the manifest writer within the existing records job so its sequencing with the taxonomy-publications workflow remains safe; separate atomicity/PR freshness testing is mandatory.
- Do **not** make a global Incident version bump when a taxonomy edition or the VIGIL dataset release changes without per-Incident edits.

## 3. Exact pass/fail delta

| Scenario | Current baseline behaviour | Proposed PR-to-main check |
| --- | --- | --- |
| Modified existing INC001, main `1.4.11`, ingestion `1.4.12`, reviewed **new FC mapping** | Version may pass current structural validator | **Require `1.5.0` (MINOR)** and explicit semantic declaration; cannot pass as merely `1.4.12` PATCH |
| Existing INC001 only typo/provenance repair on main `1.4.11` | Structurally possible | **Require `1.4.12` PATCH** and non-substantive declaration |
| Two different Incidents changed in one final PR | Structurally possible | Independently derive a candidate for each from its own main version |
| Three commits changing same Incident on ingestion | Existing authoring continues | No published bump **until final main integration**, then one highest level |
| New INC213 with staged `0.1.1`, no main counterpart | Existing authored version accepted | **Retain `0.1.1`** on first publication, subject to accepted evidence/provenance |
| Unchanged canonical record, version bumped arbitrarily | May pass structural checks | **Fail** gratuitous bump |
| Changed record keeps same published version | May pass structural checks | **Fail** missing reviewed revision |
| Another PR changes the same canonical main blob since preparation | May still be structurally valid | **Fail** stale baseline, require content reconciliation and recomputation |
| Incident at `2.0.7` receives a minor change | Structurally possible | **`2.1.0`**, preserving existing major lineage |
| Taxonomy-only publication, no canonical Incident change | Existing records unchanged | All Incident versions remain unchanged |

The versioning arithmetic **must not** label every touched `taxonomy_classification` field as automatically MINOR: moving non-substantive reviewer metadata does not necessarily change a mapping. Conversely, changes to source-episode relationships and material mapping interpretation are not necessarily mere PATCH even when the top-level class ID remains the same. The reviewer makes the evidenced semantic decision, and the test enforces *unambiguous* minimum-delta cases.

## 4. Fields, surfaces, corpus impact

**Canonical:** `vigil/records/incidents/VIGIL-INC-*.json` → existing `record_identity.version` and `updated`; source, clause relationship, taxonomy mapping, HIM and EXTREQ values are comparison inputs but **not rewritten by the version validator**. Stable `id` and `record_identity.record_id` cannot be reassigned through a version bump.

**Scripts and CI (proposed):** new isolated publication check/preparation script, `.github/workflows/vigil-records.yml` PR-main-only guard, generated manifest builder/validator and associated maintained tests *after Gate 1*. A separate Site renderer change, if needed, must be explicitly scoped, not smuggled into the version guard.

**Projection and website:** `vigil/VIGIL.Incidents.Index.json`, sparse HIM, geography index, taxonomy case-exemplar links, catalogue dispatch, and public Case File header/version key must agree on the published canonical snapshot. Website/source output itself must not trigger a record revision.

**Measured impact:** all 200 historical main Incidents have versions and all six new ingestion Incidents have working versions; the final-main integration currently compares 53 changed existing files plus six newly added. The number of those 53 requiring minor versus patch is **unmeasured and cannot be inferred from diff size or historical version numbers**. The proposed guard should grandfather untouched, previously published legacy records; it should never demand an immediate full-corpus rewrite. Future approvals to migrate review history and 230 audit flags are distinct.

## 5. Repair implications, data loss and enforcement placement

- The final integration PR may require **reviewed** per-Incident version updates and change-level declarations for changed records; this is not authority to re-adjudicate classifications, rewrite source evidence, simplify rationales, change HIM or EXTREQ or rewrite all versions.
- The greatest risk is accidentally downgrading/removing historic ingestion version stamps and review outcomes when making final-main candidates; preserve complete prior Git/PR provenance and source-linked decisions. Another risk is masking missing mapping changes as patch or treating an old successful safeguard as a new event.
- The version constraint belongs in a **PR-level checker**, because a single JSON record cannot know the last published main blob or an interbranch conflict. `VIGIL.Schema.json` can continue specifying the record shape without becoming a network-dependent release oracle. The website is a consumer of a valid published number, not its source of truth.
- A publication manifest is **derived output**, not an external classification authority, and must not duplicate complete Incident JSON or become a second record database.

## 6. Explicit stop conditions / current status

**Already permitted in this draft:** Research, read-only comparison, design, isolated pure prototype in `docs/reviews`, and test-case specification. The research-only [versioning_dry_run_spike.py](versioning_dry_run_spike.py) is **not** a CI check and has **not yet been executed in the repository's Actions environment**. It never touches real records and does not decide substantive classification.

**Human Gate 1 request:** Does the maintainer approve the **PR-to-main-only version check; authored semantic change declaration; existing-main highest-applicable arithmetic; preservation of already-staged first versions; strict stale-blob rejection; and main-only derived manifest**, under the limitations and pass/fail examples above?

**If approved:** Implement production control and isolated permanent tests in small commits; run the new checks read-only against the actual 200-main / 206-ingestion snapshots; report exact errors and affected files; **STOP for Gate 2** before rewriting or renumbering any existing Incidents. Do not merge the draft architecture work into main merely to activate the rule. Feature PRs into ingestion remain authoring, not publication.

**If not approved:** Leave the research spike and proposed contract as draft material; keep current pipeline unchanged and continue only unaffected design/QA work.

## 7. Work-mode implementation handoff (only after the Gate 1 approval above)

**Repository:** `CAM-Initiative/Vigil`. **Start from the existing `work/incident-architecture-gate1-20261028` branch** (already targets `agent/incident-ecosystem-ingestion` via draft PR #178); do not branch from main or overwrite ingestion.

1. Read `AGENTS.md`, `vigil/AGENTS.md`, `vigil/MAINTAINERS.md`, existing VIGIL/schema/validation/CI rules and the four architecture review files; verify latest main and ingestion heads before touching code.
2. Work **only the expressly approved versioning controls**. Do not conflate this with #168 storage migration or #176 challenge marker schema changes. Preserve all canonical data untouched and never bulk-bump.
3. Implement Python pure parser/bump/change-declaration check and publication diff helper with **isolated synthetic fixtures**; test same-ID stale main changes, staged first publication INC213-like version, mapping minimum minor, mixed versions, no-op, successive ingestion commits, version collisions, reviewed major exceptions, and self-referential-manifest failure.
4. Integrate only the approved checker with final-main PR CI; keep ingestion branch PRs valid without requiring a published revision. Make generated manifest deterministic and non-self-referential in existing records job; verify taxonomy-publication ordering, builder outputs and repository permission.
5. Report existing 53 modified + six new cases read-only against current main, separating missing declarations from actual semantic disagreements. **Stop at Gate 2**; do not edit 59 records simply to turn checks green. Write tests/results into branch commits and link #175 / PR #178.
6. Use small commits; run full record and subsystem validations on the actual branch. If GitHub connector cannot execute tests, state precisely which tests remain unrun; don't claim passing CI until checks actually pass.
