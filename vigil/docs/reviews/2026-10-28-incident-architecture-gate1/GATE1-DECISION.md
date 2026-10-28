# Gate 1 decision paper: Incident storage, versioning and challenged review posture

## Versioning Gate 1 decision/update — 28 October 2026

**Versioning control only:** The maintainer approved MAJOR/MINOR/PATCH semantics and separately approved the final-main-PR checker, reviewer-declared semantic change level, fresh-main comparison, initial staged version preservation and main-only deterministic manifest. The implementation is committed to draft PR #178, and 25 isolated tests passed in GitHub Actions. See [implementation checkpoint](VERSIONING-IMPLEMENTATION-CHECKPOINT.md) and [exact versioning-control disclosure](VERSIONING-GATE1-IMPLEMENTATION-REVIEW.md). **This does not approve storage-provenance schema (#168), review-challenge state (#176), record rewrites or Gate 2 migrations.** Existing paragraphs below are the historical Gate 1 design submitted before the versioning approval.


**28 October 2026 — versioning Gate 1 approved and implemented only on unmerged branch; storage/challenge semantics remain proposals.**

Related issues: [#168](https://github.com/CAM-Initiative/Vigil/issues/168), [#175](https://github.com/CAM-Initiative/Vigil/issues/175), [#176](https://github.com/CAM-Initiative/Vigil/issues/176), [#133](https://github.com/CAM-Initiative/Vigil/issues/133), [#173](https://github.com/CAM-Initiative/Vigil/issues/173). Source baseline is ingestion commit `0f008d983da72db962705fb9c732496e703cdb5e`, not `main`. All changes in this proposal are **hypothetical until explicitly approved** under `vigil/MAINTAINERS.md` Gate 1.

## 1. Executive recommendation and explicit decisions

**Recommended:** one integrated architecture, three independently approved control contracts:

1. **Compact current-state canonical provenance** with a stable, immutable, verifiable link to prior *full* review objects in Git. Retain the complete current AI review and every substantive accepted occurrence interpretation in the canonical Incident. Stop using indefinitely accumulated full historical `review_history` objects as the only record of earlier review chronology; use a compact review identity index and verified Git anchors after a five-record pilot. Do not move full historical objects into `docs/reviews` as a new permanent database.
2. **Publish one highest-applicable SemVer increment per changed Incident on main**, based on the previously published main version: **major** for exceptionally approved incompatible Incident identity/boundary redefinition, **minor** for material evidence or adjudicative changes, **patch** for non-substantive record maintenance, **none** for unrelated/no-record changes. Prefer a PR-prepared, reviewed candidate and a main-generated manifest; avoid bot-written canonical source changes. Exact proposal and examples: [INCIDENT-VERSION-NUMBERING.md](INCIDENT-VERSION-NUMBERING.md).
3. **Represent an independent audit challenge separately from the canonical source-clause adjudication outcome**. A challenged `resolved-no-mapping` clause remains historically and currently `resolved-no-mapping` until source-first adjudication, but is visibly *under review* in the approved public presentation. Prefer a small bounded clause-level challenge marker if a published status is required; do not overwrite `adjudication_status`.

These decisions are coupled operationally but **not automatically mutually authorised**. They can be separately approved/rejected, tested on fixtures and rolled back. Gate 2 is needed before changing five live Incidents or flagging 137 Incidents.

## 2. Current behaviour, proposed delta and why

| Contract | Current rule / evidence | Proposed rule | New pass / fail (illustrative) |
| --- | --- | --- | --- |
| Interpretive review provenance | `VIGIL.Schema.json` requires `interpretive_provenance.review_history` and `current_ai_review`; both `validate-vigil-records.py` and `validate-vigil-interpretive-provenance.py` require a non-empty embedded history containing the entire current review. Historical AI reviewers, model/platform, review date, scope, capabilities, limits, outcome are stored repeatedly. | Allow, for *explicitly migrated* records only, a fully specified `review_history_index` with exact immutable Git archival reference(s) and a full `current_ai_review`. Exactly one approved shape is active per record; legacy history remains valid until migration. | **Newly passes after approved schema change:** current full review + complete indexed and independently retrievable historical entries + source Git hash. **Newly fails:** compact index without pinned retrievable archive, missing reviewer identity, stale archive blob, changed review ID, provenance invented after occurrence, or simultaneous conflicting history shapes. **Still passes:** legacy unmodified 206 records. **Fails today:** any compact-index-only simulation. |
| Incident record version | `record_identity.version` exists; case-file projection includes it, but current PR/main workflow does not enforce a version-diff-to-main publication contract or a separate Incident release ledger. Generated-index bot updates on `main`; canonical records are explicitly protected from bot mutation. | For a final PR targeting `main`, compare substantive canonical Incident content to **published main**; require exactly one correctly computed **highest applicable major/minor/patch** candidate for each changed Incident, no bump for unchanged, no unchanged version for edited record, with a per-Incident semantic change-level declaration. Commit the candidate with the PR. It becomes published only on main merge. Append/update a generated release manifest on main, leaving canonical files intact. | **Newly fails:** edited Incident keeping old version, arbitrary bump on unchanged Incident, jump by several patch numbers for unmerged edits, stale candidate after main advanced, missing manifest correspondence. **Still passes:** unmodified working branch; unrelated index rebuild; independent unchanged Incidents. **Not validated today:** proposal-specific version checks. |
| Review challenge | `source_clause_analysis.clauses[].adjudication_status` admits `mapped`, `resolved-no-mapping`, `unresolved`, `taxonomy-gap`; `adjudication_coverage` derives from this. No independent challenge/status field. | Add a bounded review-posture marker **only after Gate 1**, orthogonal to adjudication (conceptual `re-adjudication-required` / `evidence-review-required` / `resolved`). Explicitly preserve the old disposition and add audit identity, reason, missing decisive fact and lifecycle closure proof. | **Newly passes:** challenged but still previously resolved no-mapping with explicit citation and a visible caveat; review-finalised retains no-mapping after genuine source-first testing. **Newly fails:** new challenge without exact matching baseline episode, a status falsely marked `mapped` only because of audit recommendation, an orphan marker, invalid transition, permanent challenge with no responsible closure. **Fails today:** unapproved extra canonical field, unless confined to temporary audit workspace. |

## 3. Five-record storage design, alternatives and risks (#168)

### Verified data

[Sizing and preservation simulation](SIZE-PILOT.json) uses actual full record bytes from the ingestion source commit. The five records total **415,314 bytes**, contain **88 historical review objects** occupying **108,774 bytes** when their arrays are independently pretty-printed, and include a complete copy of `current_ai_review` within each history.

Illustrative measured alternatives:

- **Retain current rules:** no size reduction; full review history remains a first-class canonical dependency and grows with every review.
- **Remove only duplicate latest review from history:** approximate **6,144 byte** reduction across five files, but **fails both current provenance validators** because the latest review must be in the history. This is not a recommended migration without a contract change.
- **Replace old full review objects with compact review identity index + immutable original Git anchor, retain full `current_ai_review`:** 415,314 → **320,108 bytes** (95,206 byte / **22.9%** reduction across pilot). This is *only an in-memory hypothesis*: current validators fail, no source files edited, no future-history archive contract implemented.

**Preferred option: third**, provided the pilot establishes real archive reconstruction, historical reviewer attribution and current public-renderer compatibility. The 22.9% is an estimate of this particular design, **not** proof that all five can be migrated without changing review validators, nor a corpus-wide saving estimate.

### Proposed future canonical shape (illustration only)

```json
{
  "interpretive_provenance": {
    "current_ai_review": {"review_id": "EXAMPLE", "reviewer_type": "AI analytical reviewer"},
    "review_history_index": [
      {"review_id": "EXAMPLE", "review_date": "YYYY-MM-DD", "reviewer_type": "AI analytical reviewer", "reviewer_model": "source-identified model"}
    ],
    "review_archive": {
      "source_commit": "<immutable commit>",
      "source_path": "vigil/records/incidents/VIGIL-INC-XXXXXX.json",
      "source_blob_sha": "<Git blob of historic full record>"
    }
  }
}
```

*Omitted existing provenance fields in the illustration continue to apply; this fragment is not a complete record or approved schema.*

The anchor must actually resolve the original exact historical review objects, not merely link to the active audit README or a mutable branch URL. Define a reconstruction algorithm that uses record path + source commit + blob SHA, checks all historical review IDs and their full fields, resolves supersession/chronology, and proves no history item has been replaced by one summary. It must support successive migrations and future reviews; a **single initial anchor is not a complete future-history model**.

Recommended future archival record: for each frozen review-history batch, record commit/path/blob and stable review IDs (and, if needed, hashes per review object); maintain one full, current review. Subsequent published versions have an immutable prior-version commit. Preserve non-published intermediate human decisions explicitly where squash merging otherwise would lose branch-only commits. An approved review index must not be a way to claim human approval from an AI-authored analysis.

**Never remove** canonical `source_records`, `vigil_assessment.factual_basis`, `source_clause_analysis` and its status/relationships/rationales, evidence of supported exclusions and missing decisive facts, mapping `classification_basis`, `boundary_adjudication`, harm evidence/dimensions, external requirement-specific explanations, the record's current provenance or source IDs. Historical process noise is a candidate for compacting; substantive supported findings are not.

#### Git history versus an immutable ledger

- **Git-pinned references (preferred first):** less duplication; naturally versioned; may fail if an archival commit is unreachable from retained refs, a repository is shallow-cloned, the prior state was only in a squashed branch, or external users require portable offline copies.
- **Dedicated governed immutable ledger (fallback if necessary):** guarantees explicit retrieval and portability but adds schema, storage, validator, privacy/source-protection, retention and duplication obligations. It must be outside temporary `docs/reviews`, with explicit Gate 1 and publication scope. Do not create it prematurely.
- **Long-lived docs/reviews packets as history (reject):** violates current review notice-board policy and creates a shadow adjudication authority. Temporary source-first matrices can live there only until decisions are promoted and the workspace retired.

### Risks and required counterexamples

- A prior review corrects the current finding but the corrected limitation exists only in the historical packet: **fail migration** until current canonical rationale includes the necessary substance.
- The referenced Git commit exists but the review object at that path/hash does not match indexed identity: **fail**.
- History sequence includes a reviewer/model identity not known to the original author: **must retain unknown**, never invent a platform/model.
- A full `current_ai_review` survives but authorship transparency on website disappears: **fail publication parity**.
- A public snapshot cannot reconstruct its historically cited reasoning without private tooling: **document accessibility/portability and provide a governed remedy**.
- A source or EXTREQ rationale is trimmed to meet a size target: **reject; size is not evidence fidelity**.

## 4. Incident publication and version contract (#175)

### Current state

`record_identity.version` values are not globally synchronised. For example, the same baseline has INC034 `1.1.23`, INC062 `1.1.21`, INC101 `0.1.24`, INC145 `0.1.16`, INC195 `0.1.4`. Those numbers are **per-record** version history, not the Incident ID or the taxonomy edition. The records workflow performs validation and generated-index commits; the taxonomy workflow runs after it on main. Canonical source edits by CI are presently prohibited.

### Preferred main-publication protocol

**Numbering authority:** [INCIDENT-VERSION-NUMBERING.md](INCIDENT-VERSION-NUMBERING.md) supersedes the earlier draft's patch-only default; the semantic bump is chosen from materiality, not from the count of file edits. **Verified baseline:** published main holds 200/200 versioned Incidents (128 major 0, 71 major 1, one major 2: INC032 `2.0.7`); the six new ingestion-only records INC210–INC215 have pre-existing staged versions (`0.1.0`–`0.1.1`); 53 other Incident files are modified relative to main. Do not synchronise Incident major to a global VIGIL dataset release or reset staged versions on first main publication. Historical numbers are grandfathered, not retroactively assigned new semantic meanings.

1. **Working branches:** substantive canonical Incident changes can accumulate as small commits, including branches merging into `agent/incident-ecosystem-ingestion`. They do **not** create separate public releases just by landing on that working branch.
2. **Final integration PR to main:** pin current `main` at PR review; compute changed Incident IDs by canonical payload while ignoring version/updated fields solely for diff detection. For each changed existing ID document the semantic change level and compute the **single highest required SemVer increment** from the **published main** version: `MAJOR: X.Y.Z → (X+1).0.0`, `MINOR: X.Y.Z → X.(Y+1).0`, `PATCH: X.Y.Z → X.Y.(Z+1)`; a newly created Incident starts at the template default `0.1.0`, but **a first-published existing staged Incident retains its actual approved authoring version** (e.g. INC213 `0.1.1`), not an automatic reset or exceptional downgrade. Do not derive from an ingestion-branch provisional number or the count of commits. See [explicit numbering contract](INCIDENT-VERSION-NUMBERING.md).
3. **Candidate stamping:** a reviewed preparation command changes only `record_identity.version` and the appropriate, actual review/update date on the final integration PR. No unrelated canonical files change. The prepared value is an **unpublished candidate** until merge.
4. **Pre-merge check:** compare against **fresh current main**, not stale PR base or other ingestion commits. If the same Incident changed on main after candidate preparation, **fail closed**, recompute from the new published version, rebase/reconcile the source-first content, and rerun review; do not automatically pick the bigger string or overwrite a competing decision.
5. **On main:** the merged canonical content with its prepared version is the published authoritative record. Generate an Incident publication manifest from the settled main commit and canonical file digests, and build navigation/HIM/case-file projections; avoid a CI step rewriting source records. Its manifest may be a generated artefact if the workflow contract explicitly admits it.
6. **No version change:** when no material canonical record payload changed. Pure website/rendering changes, docs/audit changes, already-generated index changes or changing taxonomy criterion definitions without touching Incident content do not bump Incident versions.
7. **Preserve mixed version lines:** apply the highest justified level **within each record's own existing version lineage**, not a global version. A patch can be `1.1.23 → 1.1.24`; a substantive new mapping can be `1.1.23 → 1.2.0`; a truly incompatible occurrence redefinition is normally a new Incident ID and only exceptionally `1.1.23 → 2.0.0`. The existing `0.1.0` template remains the proposed **creation default**, not a forced first-publication version; historic and ingestion-staged `0.x` editions are not automatically invalid or unpublished.

### Important two-branch edge case

A programme can pass through `work/...` → `agent/incident-ecosystem-ingestion` → `main`. If the same Incident is revised three times on the ingestion branch before publication, only **one** published, highest-applicable SemVer increment is required at the final main integration, unless it was published on main in the interim. Do not demand one bump per ingestion PR. Stage-specific preparation must not call a provisional candidate published.

The taxonomy may change and publish independently. The Incident's **applied taxonomy edition** continues to be recorded separately. Class recognition changes do not silently restamp or overwrite Incidents that were not substantively re-adjudicated.

### Manifest and downstream contract

Proposed per-commit manifest entry: `incident_id`, `published_version`, `canonical_path`, `content_sha256` (exact canonical file bytes), `source_commit`, `published_on`, `taxonomy_version_as_applied`, `him_version_as_applied`, plus an explicit supersession predecessor when known. Never store duplicate complete Incident JSON in this manifest. Distinguish the **published merge/input commit** from bot-generated manifest/index commits to avoid self-referential hashing or a loop of forever-new head SHAs. The manifest may identify the settled canonical content tree or a stable source input commit; the publication build itself must be idempotent.

For public website `version` / `v` keys, case files, catalogue update dispatch and generated indexes, verify a consistent settled-main snapshot. Include positive and negative tests for main advancement, edited same record from two branches, one PR changing two records, no-op, semantic edit to current review only, missing bump and arbitrary bump.

## 5. Challenged `resolved-no-mapping` status (#176)

### Audit claim and classification boundary

The frozen audit has 115 **reconsider-existing-class** and 115 **further-evidence-required** recommendations across **137 unique Incidents**. These are not 230 accepted changed dispositions, 230 separate Incidents or automatically 230 `unresolved` clauses. Existing `adjudication_status` is still an evidentiary outcome; the independent audit questions the reliability of final closure.

**Do not reuse** `mapped`, `unresolved`, `taxonomy-gap`, `ambiguous-boundary`, `classification_confidence` or `processing_review` merely as a generic queue marker. The current `adjudication_coverage` derivation must not be hijacked by audit status.

### Options

| Option | Consequence | Recommendation |
| --- | --- | --- |
| GitHub #133 + immutable temporary register only | Zero canonical revisions, excellent for internal triage; website still presents prior no-mapping as unchallenged unless a separate presentation layer is authorised. | Accept as **Stage 0** while designing/testing. |
| Small `review_challenge` object on the affected source clause | Public and canonical statement that a disposition is challenged; ~137 record edits and version revisions; needs schema, validator, builder and renderer contracts plus Gate 2 approval. | **Preferred after Gate 1** if the user-facing status must visibly change. |
| Permanent standalone review-status database | Can be independently updated but risks ambiguous source of truth and a second per-clause database; significant sync/retention risk. | Reject by default; assess only on demonstrated necessity. |
| Mass-convert to `unresolved` or `taxonomy-gap` | Wrongly changes evidentiary meaning for class reconsiderations and missing-source matters. | Reject. |

### Proposed bounded clause-level shape (illustrative only)

```json
{
  "episode_id": "E004",
  "adjudication_status": "resolved-no-mapping",
  "review_challenge": {
    "state": "re-adjudication-required",
    "basis": "source-first full-corpus review recommended testing an additional existing class",
    "audit_id": "VIGIL-INC-000XXX:E004",
    "audit_baseline_commit": "0f008d983da72db962705fb9c732496e703cdb5e",
    "opened_on": "2026-10-28"
  }
}
```

Every new field/value in this example is **proposed and currently unapproved**. The exact `audit_id`, current source-clause anchor, taxonomy digest and missing evidence would be copied from a verified version-pinned migration manifest, not generic boilerplate. State may be `re-adjudication-required` or `evidence-review-required`, with closure `accepted-changed` / `accepted-retained` / `completed-evidence-limited` recorded by a separately authorised decision. Avoid a perpetual array of audit-challenge objects in every Incident: make the field **current state**, and use Git for historical transitions.

If two flags apply to the same episode, represent both material questions explicitly without duplicate conflicting current states. If a source clause changed since baseline, fail identity matching and route to an individual human adjudication; a matching episode ID by itself is not proof of identical source content.

**Potential public label:** “Previously reviewed — no classification; re-adjudication in progress” or “Prior no-classification decision under evidence review”. This is a review disclosure, **not** VIGIL's Aligned/Not aligned/Boundary taxonomy judgement. Do not silently replace stage 02 source evidence or stage 03 mapping tables with audit text.

## 6. Corpus impact and bounded scope

- **Measured exact at baseline:** five size-pilot Incidents with 88 embedded historic reviews, 415,314 bytes source total.
- **Audit-challenge population measured:** 230 flagged clause episodes across 137 distinct Incidents; a proposed public canonical marker would change as many as 137 records before any reclassification (subject to exact current baseline join). No unapproved backfill.
- **Unmeasured:** corpus-wide full history index/savings, every website consumer of review_history, total count of records affected by new version validator, and exact interaction with changes that landed on main after audit. **Must run read-only discovery before approving a blanket migration.**
- **Deferred:** 446 retained no-mapping dispositions require independent QA sampling, not mass edits. Three taxonomy clarifications and two provisional class candidates are independent governance programmes; nothing here authorises taxonomy changes.

## 7. Human Gate 1 decision request

Please approve, reject or amend **each independently**:

- **A — Storage:** Allow a *pilot-only* dual-path provenance schema contract (legacy full `review_history` OR complete retrievable history index + immutable Git anchors, always full current review), contingent on measured source/website compatibility and a later separate Gate 2 for actual five records?
- **B — Revision:** Adopt explicit per-Incident SemVer levels—major for exceptionally approved incompatible identity/boundary, minor for substantive evidence/adjudication, patch for non-substantive maintenance, none for no canonical change—**once at the highest applicable level on final main integration**, with template creation default `0.1.0` and **preservation of staged versions at first publication**, manual semantic change declaration, strict stale-base checks and a main-only generated manifest? See [numbering proposal](INCIDENT-VERSION-NUMBERING.md).
- **C — Challenge:** Approve designing and fixture-testing a minimal current `review_challenge` marker orthogonal to `adjudication_status`, with a possible later human-approved mass flagging of the exact 230 source clauses?
- **D — Provenance:** Prefer pinned Git commit/path/blob recovery over a new permanent ledger **until a failed portability/reconstruction test demonstrates a need**? What historical review accessibility must offline readers have?
- **E — Publication:** Require public presentation of an active challenge, or restrict the first rollout to internal tracking until a website contract is separately approved?
- **F — Pilot:** Authorise *only after design approval* isolated fixtures and read-only validation, then separately present Gate 2 before writing the five pilot Incidents or any part of the 137-record population?

**STOP CONDITION:** No semantic schema, validator, builder, website publisher or production Incident changes until the relevant exact Gate 1 rule is explicitly approved. After implementing any approved controls, run the actual corpus read-only, show new fail/pass counts and obtain separate Gate 2 before broad edits. Failure of semantic preservation, archive reconstruction or version freshness blocks migration rather than just generating warnings.
