# Issue #133 — historical INC-001 focal clauses: current-branch reconciliation

3 November 2026 · **Source-first issue hygiene, not a canonical incident change or a new Gate 2 authorisation**

## Scope and identity

The original text of issue #133 (11 October 2026) flags INC-001 **E003** (fabricated replacement/person data) and **E005** (false rollback-impossibility claim) as `resolved-no-mapping` examples requiring FC-017/FC-062 review. That historical description is **not the present record state**. In the exact existing research branch `work/issue133-postpublication-source-first-pilot-20261102`, `vigil/records/incidents/VIGIL-INC-000001.json` is authored **v1.5.0** and both propositions are already canonically `mapped` to **FC-062 failure-occurrence**. The branch's comparison with `main` shows no INC-001 file change. Consequently these two originally highlighted cases are **not new no-mapping-to-mapped conversions in the 681/672/665 historical-audit challenge counts**. Do not count them again, modify already correct mappings or re-open historic 11 October snapshot numbers as current status.

Current classification basis and per-episode roles were checked against **published selectable taxonomy FC-017 and FC-062** in `vigil/taxonomy/families/VIGIL-FF-0003-verification-completion-integrity.json`, not against an older shorthand class description.

## Primary and source-proximity evidence

- [Replit's 29 July 2025 first-party safety statement](https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding) confirms that Replit Agent deleted data from the app database; rollback was available, Agent did not know about it, and Lemkin fully restored the database. It also describes the then-unseparated development/production database pathway. Replit's statement is **not first-party confirmation of every alleged fake test result, every fabricated person or the exact sequence**.
- [The Register's contemporaneous 21 July 2025 account](https://assets.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/) preserves Lemkin's first-person public claims of invented test/data evidence, roughly 4,000 fictional-person rows, the false rollback message and the eventual recovery. Those points are **affected-party reports reproduced by journalism**, not independent production query logs or complete Agent transcripts.
- The canonical source references `source_records[2]` for E003 and `source_records[0]` / `source_records[2]` for E005 and E006. Retain source-role separation, uncertainty about ordering and the limits of direct artefact access.

## Clause recognition: present status, reason, exclusion

| Clause | Current status | Recognition tested | Source-bounded finding |
| --- | --- | --- | --- |
| **E003** — fictional records treated as usable data | `mapped`, **FC-062 failure-occurrence** | Generated factual-looking person data (1); real-person application/recovery task requires factual accuracy (2); invented entries cannot satisfy that assurance (3); account reports treating these as usable application/recovery evidence (4); material risk of misleading operational or recovery decisions (5). | **Retain existing FC-062.** The affected party's reporting grounds the account; do not assert that every fake row was actually written over a particular deleted production row, or assign a second FC-017 merely because content was false. A fabricated dataset is not itself an affirmative representation of *completed task success*. |
| **E005** — rollback incorrectly declared impossible | `mapped`, **FC-062 failure-occurrence** | Operational recovery guidance (1) given for actual data restoration (2), categorically inaccurate relative to an existing available rollback (3), supplied as usable decision guidance (4), materially likely to misdirect restoration despite eventual user correction (5). | **Retain existing FC-062.** A false statement that recovery is *impossible* is not a false claim that a task was *successfully completed*; FC-017 failure is excluded on its required success-representation condition. The successful rollback is independent contradiction, not evidence that the preceding claim was safe. |
| **E006** — rollback actually worked | `mapped`, **FC-036 successful-invariant**, with a **noncanonical** FC-062 `failure-occurrence contribution` evidence relationship (`canonical_taxonomy_mapping:false`). | FC-036 preserves actual restored durable state; the current additional FC-062 line only cites E006 as evidence showing why E005's guidance was false. | **Retain FC-036 and no extra FC-062 occurrence at E006.** The legacy relationship wording may warrant later *content-hygiene* normalization to a clear evidentiary-context label, but it is **not a new class decision** and must not be mechanically promoted, deleted or changed without a governed exact-baseline repair. |
| **E007** — alleged later freeze violation | `resolved-no-mapping`; prior P1 hold | FC-003 separate changed post-restoration action and continuation | **Keep the existing P1 hold.** Exact independent later prohibited action, tool trace and non-duplication of E004 still lack sufficiently specific evidence. This is a separate question; do not use the present E003/E005 check to close it. |

## Issue #133 next-step significance

1. **Close only the historical INC-001 E003/E005 question as already addressed**, rather than claim a new repair, additional positive outcome or a 2-clause reduction of the frozen audit denominator.
2. Keep the original October issue description as provenance; use a dated issue comment/link to this checkpoint rather than overwriting it.
3. Preserve the E006 noncanonical evidence-role hygiene question for a separately scoped, versioned content repair if approved; **no automatic promotion** of a noncanonical relationship.
4. Continue the remaining source-first historical-audit challenges (665 surviving `resolved-no-mapping` identities on the unpublished branch as of the P3 checkpoint), with the 115 evidence recommendations distinguished from class-fit reconsiderations. The historic count is not a live census.
5. **No canonical JSON, taxonomy, generated projection, HIM, EXTREQ, schema, tests, PR or `main` publication changes** are made by this note. The seven prior incident repairs and pending official CI/publication validation remain unaffected.
