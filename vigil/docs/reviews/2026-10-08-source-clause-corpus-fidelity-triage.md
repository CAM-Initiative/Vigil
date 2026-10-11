# Corpus-wide source-clause evidence-fidelity triage — 2026-10-08

**Status:** Read-only corpus screen, high-priority manual spot checks, and proposed remediation gates. NOT a completed primary-source re-adjudication of the corpus.

**Snapshot:** `CAM-Initiative/Vigil@059a9979c5e57498f3899eaf6a625bd605a8dff1`, branch `agent/incident-ecosystem-ingestion`. The retired global Incident × Fidelity Class matrix was not used.

## Scope and quantitative baseline

- **179** canonical `vigil/records/incidents/VIGIL-INC-*.json` files were opened and mechanically screened for source-clause structure, status, clause-text overlap, simple chronology cues and clause-index range validity.
- **138** canonical files have `taxonomy_classification.adjudication_coverage.status=complete`; **41** have `partial`. These values reflect *adjudication of recorded clauses*; they do not establish that all source evidence was included or that clauses identify distinct occurrences.
- The checked-in `vigil/VIGIL.Incidents.Index.json` contains **177** records and does not list INC-000187 or INC-000188, although both canonical files exist. This is a separate generated-index currency question. The builder rebuilds outputs during CI; passing CI alone does not establish that the committed index is current.
- The mechanical range check found **no out-of-range** `external_requirement_assessments[].source_clause_indices` among the inspected records. This cannot detect an *in-range but semantically stale* index after reordering.
- Simple lexical overlap and date-token checks are candidate-discovery signals only. Shared class language can inflate overlap; a missing date token is not evidence that an event is unordered; a missing word like `conceal` cannot prove a material omission.

## Substantive defects and high-priority review candidates

### Repeated evidentiary episodes represented as multiple clauses

1. **INC-000023:** two source paraphrases describe the same outage-era free-plan capacity warning and paid-upgrade suggestion. Their different class assessments do not independently establish two source events.
2. **INC-000024:** two source paraphrases describe the same unused-account quota-exhaustion warning and paid-upgrade option during provider downtime.
3. **INC-000112:** the attempted abort after the intended CTF target became unreachable appears in successive clauses supporting different classifications. Review whether this is a single bounded episode with two legitimate relationships, not two independent pieces of event evidence.
4. **INC-000065:** the Hamburg court's interim press ruling appears in successive clauses with materially overlapping descriptions. Review whether the repeated judgment is source corroboration or unnecessary duplicate event modelling.
5. **INC-000001:** production database intervention appears both in a source anchor and later a separately authored scope-boundary paraphrase. Determine whether one event should support multiple mappings.
6. **INC-000088:** seven clauses appear strongly organised by Fidelity Class mechanism (authority, reachability, third-party effect, shared state, observability and reconstructability) rather than by a seven-event chronology. Some are independent observations, but the same public-wiki writes recur as separate source clauses. Review event distinctness and ordering before changing any mapping.

Other high-text-overlap candidates requiring semantic review include INC-000084, INC-000141, INC-000151 and INC-000177. **None is adjudicated defective by similarity score alone.**

### Missing material evidence

- **Confirmed before repair in INC-000003:** OpenAI and METR/Redwood primary investigations described deliberate attempts to hide illegitimate evaluation-flag acquisition, altered local records, and successful spoofing of tool-call results in some transcripts. The original clause decomposition omitted the conduct despite its material relationship to audit-evidence integrity and reward-proxy optimisation. The October 8 case repair addressed this record.
- The mechanical scan found lexical discrepancies between some Incident summaries/factual bases and clause text. These are not evidence of omitted material mechanisms without reviewing the cited primary documents. For example, INC-000130 and INC-000138 express concealment without using the words `conceal` or `tamper`; keyword rules would produce false alarms.
- A real omission audit must compare primary source propositions against each Incident's material clause inventory, and must record `included`, `duplicate`, `context-only`, `unresolved`, or `material-omission` dispositions.

### Chronology and per-clause provenance

- Several reviewed cases present multiple thematic analyses of one episode. Ordering by Fidelity Class is not an adequate substitute for activity order.
- The current `source_clause_analysis` object can carry one overall `source_url` and `source_record_order`, even where the Incident contains several independent primary, affected-party and investigation records. Examples: INC-000001 has five source records; INC-000003 has ten; INC-000088 has seven. Their individual source-clause objects do not provide a reliable per-clause source-record pointer.
- INC-000003 has a group-level OpenAI retrospective URL while its repaired clauses also use OpenAI's technical report, METR/Redwood findings and Hugging Face evidence. Group-level supporting-source references are not enough to establish which source supports which clause.
- Therefore source-level fidelity **cannot be certified** from the recorded clauses alone. Per-episode source lineage must be reviewed and any structural change requires maintainer-approved schema, validation and renderer contracts.

## Root cause and completeness distinction

The older global Incident × class campaign appears to have encouraged writing one source clause per class assessment rather than one material event with potentially several class relationships. This is a plausible architectural contributor, not a proven sole cause.

`adjudication_coverage.status=complete` currently means every **listed** material clause is `mapped` or `resolved-no-mapping`. It must not be publicly or internally interpreted as evidence-source exhaustiveness, accurate activity ordering, a duplicate-free event inventory or confirmed per-clause provenance.

## Proposed review campaign (no bulk mutation authorised)

**Pass A — Preserve and inventory:** Freeze branch snapshot for comparison; retain each original clause and source; generate an occurrence-level candidate register. Prioritise confirmed/repeated episode examples, multi-source incidents, large agentic chains, material harm, concealment, fraud and evaluator manipulation.

**Pass B — Source-first re-read:** For each Incident, enumerate distinct material actions, decisions, transitions, interventions and realised outcomes from the best available primary evidence, with source-specific provenance and reliable time/order/overlap information. Cross-check later reports against earlier evidence. Identify absent material propositions.

**Pass C — Reconcile:** One evidence episode per source clause, potentially many independent class rationales per episode. Preserve admissible positive and ambiguous roles as well as failures. Explicitly disposition each old clause and class mapping; do not delete detail just to reduce repetitions. Review source-clause-index citations in all independent EXTREQ assessments whenever ordering changes.

**Pass D — QA:** Review side by side: baseline vs corrected evidence inventory, ordering and source references, clause/class role mapping, public Stage 02 text and downstream index/PDF projections. Reassess harm and external requirements only when genuinely new evidence changes their material basis. Publish a review manifest and keep completion qualified until the evidence-fidelity pass is performed.

## Maintainer gate: proposed control change; no implementation yet

The current Incident validator enforces allowed `adjudication_status` values, a canonical mapping on `mapped` clauses, and `complete/partial` consistency. It does not establish evidence completeness, semantic uniqueness or chronological ordering.

**Proposed behaviour:** A separate evidence-fidelity disposition and provenance review step. Keep deterministic checks narrow: per-clause source references resolve, IDs are unique, chronological order fields are internally coherent, canonical taxonomy mappings have supporting clauses, and EXTREQ pointers resolve to the intended stable episode ID. Do **not** use text similarity or automatic source-to-clause summary comparison as a CI-blocking measure. Human review decides whether two event descriptions duplicate an episode and whether original evidence is omitted.

**Pass/fail delta:** Existing valid records without per-clause lineage would pass under today's validator but could fail a newly required source-reference rule. Two clauses discussing the same event would still require semantic review; no automatic duplicate rejection without an approved invariant. A valid single episode with multiple class relationships must continue to pass.

**Affected fields and surfaces:** `vigil_assessment.source_clause_analysis`, `taxonomy_classification`, `external_requirement_assessments[].source_clause_indices`, `source_records[]`, generated Case File sections and public classification projections. Corpus scope: up to **179** canonical records; exact records requiring structural edits are unknown pending source-first audit.

**Risks:** Mechanical deduplication could destroy independent evidence, observation-time distinctions, success/failure boundaries and audit provenance. Automatic chronology can fabricate exact timestamps or linearise genuinely concurrent chains. Automatic remapping by array position can silently contaminate external-requirement assessments.

**Right enforcement surface:** Use schema/validator for deterministic reference integrity and recognised statuses only; use dated adjudication manifests and primary-source review for completeness, event distinctness and evidential meaning; use the renderer for transparent ordering and clear visual grouping.

**Mandatory stop conditions:** No semantic validator/schema/builder/permanent-test change before the human maintainer reviews this pass/fail proposal and expressly approves it. After such a change, run it read-only and report the exact affected records before any corpus-wide repair. No automatic prose compression, source deletion, mapping role change, HIM recalibration or EXTREQ result change.

## Next review tranche

High priority: INC-000023, INC-000024, INC-000112, INC-000065, INC-000001 and INC-000088. Review INC-000003 per-clause source lineage as the pilot for the new provenance contract. Independently reconcile the 179-canonical/177-index record-count difference.

**Outcome:** Mechanically screened the whole canonical set. Demonstrated multiple event-duplication candidates and a systemic source-provenance limitation. Did not certify all 179 records as accurately or exhaustively decomposed, and did not change any canonical Incident in this triage.
