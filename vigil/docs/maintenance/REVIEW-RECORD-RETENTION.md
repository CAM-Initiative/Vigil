# Dated review-artefact retention policy — VIGIL 1.0.0

**Status:** Active repository curation instruction; NOT an adjudication criterion. No canonical Incident, taxonomy, HIM or EXTREQ decision changes are authorised by housekeeping.

## Principle

The active repository is a citable research corpus and maintained governance system, not a full development diary. Retain accepted rules, evidence necessary to reconstruct governed decisions, and material limits. Do not retain every intermediate execution product. Removing a dated review from the working tree does not imply that its analysis was wrong, independently verified or superseded on its merits; Git history preserves it.

## Retention precedence

1. **RETAIN:** Canonical Incident/source/taxonomy/HIM/EXTREQ records, operative maintainer rules, approved methodological and adjudication decisions, current per-Incident source-and-criterion packets (including rejected/negative candidates), irreproducible source-access records and historical FC identity crosswalks.
2. **CONSOLIDATE THEN RETIRE:** A dated proposal or audit whose unique accepted decision has been relocated to the governing document. State its replacement path, original Git object and limits; structural CI is not evidence of semantic approval.
3. **HISTORY ONLY:** Superseded pilots, reproducible snapshots, execution logs and redundant intermediate outputs that have no required live reference. Delete from the branch only after an exact reference/dependency scan; retain the pre-deletion Git commit.
4. **HOLD:** Anything referenced by a canonical Incident, code, test, workflow, current reconciliation packet or live review, or containing unique nonreproducible source/decision evidence. Ambiguity means hold, not delete.

## Deletion gate

- Enumerate exact paths and Git object IDs at the current PR head; examine code, canonical review references, Markdown links, relative paths, workflow and test use.
- Check for unique per-episode recognition, exclusion or missing-evidence decisions and source-access provenance. A filename, age or passing validator alone cannot establish redundancy.
- Freeze all current taxonomy v0.8.0 campaign packets until their decisions are accepted and the release campaign completed.
- Pin the parent commit and state replacement locations in one reviewable PR; never rewrite Git history, silently rewrite a review_reference or change main directly.
- Re-run the retention audit and CI; new dangling required references must be zero. A new release checksum must be built from approved merged main, never an old PR-head snapshot.
- Ordinary evidence uncertainty belongs in Incident records and dated reviews, not a new GitHub Issue unless independently actionable work is actually required.

## Future working artefacts

Console logs, one-off test outputs, large interim inventories, copied canonical JSON and progress scratch files belong in untracked workspaces or CI artefacts. Promote only accepted, dated decision evidence and a compact validation summary into the scientific tree. The existing dry-run inventory is vigil/releases/siai-2026/audit_repository_retention.py.
