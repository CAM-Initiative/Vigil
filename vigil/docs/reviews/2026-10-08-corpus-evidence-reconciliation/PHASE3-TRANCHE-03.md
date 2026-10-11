# Phase 3 — third bounded source-first tranche (8 October 2026)

**Branch:** `agent/incident-ecosystem-ingestion`
**Canonical start checkpoint:** `a09e222ef547de44e092ae8f9ba576df17b2c720`
**State:** two further case-level canonical repairs committed; held items documented as source-only questions. This is not a corpus-wide migration or independent human source certification.

## Completed canonical repairs

| Incident | Old → new material clauses | Class-derived EXTREQ rows re-linked | Distinct repair outcome |
|---|---:|---:|---|
| INC-060 | 8 → 8 | 8 | Corrected cross-agent reuse placement before incident response; separated unsanctioned multi-run behaviour, independently successful human refusal, cautious inspection and later remediation. |
| INC-159 | 7 → 5 | 14 | Separated the issue-intake workflow vulnerability, subsequent incomplete credential revocation, later unauthorised release by an unidentified third party, remediation and postmortem reconstruction. |

Both cases preserve original source record entries, mapped canonical class-and-role multisets, harm assessments and independently assessed external-governance alignment decisions. The existing unresolved FC-084 verification-laundering candidate in INC-060 remains unresolved; downstream reuse did not prove inherited assurance inflation. Cline's report distinguishes an unauthorised publication from malicious payload delivery or observed user data theft.

**Exact evidence crosswalks:**
- `INC-000060-phase3-tranche03-repair-manifest.json`: old-to-new clause ordering, source-record pointers, eight EXTREQ rows, and preservation checks.
- `INC-000159-phase3-tranche03-repair-manifest.json`: five source episodes, fourteen EXTREQ references, and preservation checks.

## Held evidence and adjudication decisions

See `PHASE3-TRANCHE-03-HELD-EVIDENCE.md` for source-anchored read-only findings:

- **INC-171:** OpenAI's original account-enforcement record remains distinct from disputed civil claims about model assistance. New United States federal charges allege a separate human coordination pathway; they are not convictions and cannot be used to infer or exclude AI causation. The existing S5 physical event harm must not silently become a causal finding about an AI system.
- **INC-064:** The Canadian privacy regulator documents separate prior safeguards, deployment-specific exposure, observed failures and later corrective measures. The attempted canonical update in the previous tranche was blocked, and no record mutation was attempted or made in this tranche.
- **INC-174:** BOCSAR's 25 September update reports no established vulnerability and no non-public access. The reason unsuccessful attempts ended is not demonstrated: this does not independently prove FC-083 control effectiveness. Current unresolved candidacy remains unchanged.

These three are **not** counted as completed repairs or certified evidence-exhaustive records.

## Corpus census

179 active canonical records. **13** bounded source-first repaired (Phase 1 and all Phase 3 tranches combined); **5** earlier pilot-only; **1** other preliminary source spotcheck; **160** still awaiting full source-first review.

The ledger is a reviewed-state index, **not** a source-exhaustiveness proof. Test success validates current structural correctness and generated projection parity; it does not adjudicate material event exhaustiveness, class suitability or operator liability.

## Release boundaries

- Keep using the canonical Incident-ecosystem ingestion branch. The live catalogue must not be notified before merge to `main`.
- Stable episode IDs and `source_episode_refs` remain opt-in; no mechanical bulk rewrite of the remaining Incident corpus.
- No harmonisation of contradictory public sources, no reassignment of current taxonomy polarity, no unreviewed external requirement changes or HIM adjustments.
- Refresh generated outputs only via the deterministic builder and confirm all VIGIL validation and publication workflows.
- Next follow-up should prioritise independently source-verified multi-source cases with significant assessment-index exposure; when attribution or recognition is disputed, write review findings and stop that case rather than changing the canonical record.
