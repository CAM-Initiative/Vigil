# Incident architecture Gate 1 — coordinated design and pilot

**28 October 2026 · Proposal, not approval.**

**Repository:** `CAM-Initiative/Vigil`  
**Working branch:** `work/incident-architecture-gate1-20261028`, created **from the existing ingestion branch** `agent/incident-ecosystem-ingestion` at commit `0f008d983da72db962705fb9c732496e703cdb5e`, not from `main`.  
**Published taxonomy authority for related corpus audit:** v0.9.0.  
**Issues:** [#168](https://github.com/CAM-Initiative/Vigil/issues/168) canonical size/retention, [#175](https://github.com/CAM-Initiative/Vigil/issues/175) per-Incident revision/versioning, [#176](https://github.com/CAM-Initiative/Vigil/issues/176) challenged no-mapping findings; coordinator [#133](https://github.com/CAM-Initiative/Vigil/issues/133).

## Purpose

Prepare one integrated, source- and repository-grounded **Gate 1 decision** before many incident re-adjudication passes. Cover:

1. **Lightweight canonical Incident records** while retaining full accepted evidence/chronology, classification reasoning, exclusions, meaningful uncertainty, HIM and external-governance determinations.
2. **Independently versioned Incident publications**: stable `VIGIL-INC-NNNNNN` identity; one highest-applicable **major/minor/patch** revision per changed Incident on authorised `main` publication, and no revision for unaffected records. [The numbering specification](INCIDENT-VERSION-NUMBERING.md) defines every change level and the first-published version separately from the taxonomy numbering rules.
3. **Challenged classification review posture**: report the independent audit's challenge without manufacturing a new taxonomy disposition or deleting a previously supported finding.

## Frozen inputs and measured pilot

The completed [full-corpus taxonomy-gap audit](https://github.com/CAM-Initiative/Vigil/blob/work/full-corpus-taxonomy-gap-audit-20261028/vigil/docs/reviews/2026-10-28-full-corpus-taxonomy-gap-audit/README.md) identifies 681 reviewed no-mapping clause episodes, 115 recommended existing-class reconsiderations and 115 evidence-review recommendations across 137 unique Incidents. These are **audit recommendations, not 230 demonstrated errors or approved canonical reclassifications**.

The five already named storage-pilot records are `INC034`, `INC062`, `INC101`, `INC145`, `INC195`. All five were read on the pinned ingestion commit. See [SIZE-PILOT.json](SIZE-PILOT.json) for exact source blob SHAs, current versions and a **non-applied in-memory** representation experiment. Their combined source JSON measures **415,314 bytes**; embedded `review_history` arrays measure **108,774 bytes** (separately serialised), including the current review copied into the arrays. An illustrative proposal preserving the full current review and index entries to each historic review, anchored to the immutable original Git blob, is **95,206 bytes / 22.9% smaller** across those five files if approved. This is a *simulation*, not evidence that validators or publication currently support it.

## Current governance boundary

- `vigil/VIGIL.Schema.json` and `vigil/scripts/validate-vigil-interpretive-provenance.py` currently require a non-empty embedded `review_history` containing the full `current_ai_review`. An index/anchor substitution **fails current rules**.
- The existing records workflow `.github/workflows/vigil-records.yml` validates/builds the public indexes on PR and on `main`, but **refuses to mutate canonical source records in automation**. Generated indexes are separately committed on main.
- Taxonomy releases have their own main-only publication ledger; Incident versions presently vary independently (`0.1.x` and `1.1.x` in this pilot). Reuse existing `record_identity.version`, not a conflicting new number.
- `vigil/docs/maintenance/REVIEW-RECORD-RETENTION.md` says `vigil/docs/reviews/` is a **temporary notice board**, never a second authoritative review database. Historical source remains in immutable Git/PR history. Future durable methodology belongs in `vigil/docs/maintenance/` only after approval.
- `vigil/MAINTAINERS.md` Gate 1 demands the current/proposed control, pass/fail delta, affected fields and published surfaces, impact count, risks and enforcement rationale **before semantic schema/validator/publisher changes**. Gate 2 is separate for mass Incident repairs.

## Work products and status

- [SIZE-PILOT.json](SIZE-PILOT.json): exact five-record size baselines and illustrative alternatives; metadata only; no complete records copied.
- [GATE1-DECISION.md](GATE1-DECISION.md): integrated options, preferred design, rejection cases, current/proposed semantics and explicit approval questions.
- [INCIDENT-VERSION-NUMBERING.md](INCIDENT-VERSION-NUMBERING.md): **explicit version meanings and worked examples**—new Incident `0.1.0`; major for exceptionally approved identity/scope change; minor for substantive evidence or classification/HIM/EXTREQ change; patch for record maintenance; no bump for unrelated changes. One highest increment from fresh main, never from the number of ingestion-branch edits.
- [IMPLEMENTATION-PLAN.md](IMPLEMENTATION-PLAN.md): staged gates, fixture tests, dependencies, failure handling, review/retirement procedure and rollback.

**No production schema, validator, builder, workflow, canonical Incident, classification, HIM, EXTREQ or taxonomy changes are authorised or included in this design branch.** The branch is a live review workspace; at closeout promote only accepted general methodology to `vigil/docs/maintenance/` and retire temporary packets with pinned recovery SHA under the existing retention rule.

## Programme boundaries

- Do not mechanically change `resolved-no-mapping` to `unresolved` or `taxonomy-gap` for the 230 challenged clauses; evidence-based classification and *review posture* are independent.
- Do not make an announced mitigation into a proved successful invariant, or assign a defender/police control to the attacking AI without the correct assessed-system perspective.
- Do not let a storage reduction remove accepted clause-level rationale, Boundary adjudication, source-episode relationships, independently assessed external requirements or Harm Impact.
- Do not perform version bumps for temporary review artefacts or publication-index-only updates.
- Do not represent AI-authored review packets as an independent blinded human audit or the 230 recommendations as a measured taxonomy false-negative rate.
