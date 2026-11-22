# Perception Calibration vs existing verification and epistemic-reliance classes — independent-property gate

**Research review:** 23 November 2026  
**Scope:** existing canonical VIGIL v0.9.2 (published `main`) compared with the unadmitted candidate in draft [PR #195](https://github.com/CAM-Initiative/Vigil/pull/195).  
**Status:** criterion-level conceptual audit; **no taxonomy admission, amendment, version change, incident re-adjudication or canonical mapping**.

## 1. Main-branch admission verification

The canonical `vigil/taxonomy/VIGIL.FailureTaxonomy.Index.json` identifies version **0.9.2**, 18 families, and 83 selectable classes. A full pass over all family JSON files found **no admitted class named Perception Calibration Integrity** and no equivalent class under that exact label. The closest canonical class is **FC-062 Epistemic Reliance Calibration**, under **Verification & Completion Integrity** (FF-0003); related FC-016 Required Verification Completion, FC-017 Success Representation Integrity and FC-029 Execution-State Disclosure are also admitted. **Perception Calibration remains a research candidate, not a synonym already admitted to main.**

## 2. Necessary criteria: where does the proposed class actually differ?

### FC-062 Epistemic Reliance Calibration — existing normative failure

1. A factual claim, technical statement, calculation, **interpretation** or comparable *epistemic artefact* is generated/retrieved/transformed/**inferred**/synthesised.
2. It has an evidenced purpose or downstream task where accuracy, fidelity, uncertainty or equivalent epistemic assurance materially matters.
3. Its content, specificity, certainty, framing or assurance is materially below what that purpose/reliance condition requires.
4. The artefact is **supplied, represented, propagated, incorporated, submitted or accepted** for the reliance-bearing task without meeting the required threshold.
5. The mismatch materially affects or risks decision-making, technical correctness, institutional process or other reliance-bearing outcomes.

Its definition is deliberately not restricted to public-facing final answers. An *inferred interpretation accepted as a basis for subsequent tool action* can meet the literal language, subject to proving a material assurance mismatch; the current class examples are external outputs but the recognition conditions are broader.

### Proposed Perception Calibration — draft, not normative

1. Actual materially relevant external or conversational condition and information accessible to assessed agent at decision time.
2. A materially false, stale or inadequately warranted **operative understanding** attributable to that same actor.
3. The understanding **shapes a consequential response/decision/action**, not just a mistaken statement.
4. Failure must remain after differentiating information-artifact reliance, authority, reward-gaming, continuity state, material signals and execution controls.

**Overlap:** Almost all well-evidenced Perception failures include an inferred *interpretation* accepted for use in a consequential downstream decision, with accuracy or uncertainty below the reliance threshold. Those are **already FC-062 failure-recognition conditions** if the interpreted state is a qualifying epistemic artefact. A wrong belief without an inadequate evidence-relative assurance posture is not necessarily a failure of either class.

**Potential separation:** FC-062 requires a qualifying epistemic artefact and downstream **reliance**; the Perception draft may extend to interpretation of the *live interaction/environment before* any distinct epistemic artefact is produced, e.g. a directly misallocated conversational role or physical-world action selected on an erroneous situation model. **This is a hypothetical scope difference, not an empirically demonstrated independent VIGIL failure.** If the operative interpretation can be regarded as inferred material accepted for action, FC-062 still applies. The concept of “internal belief” should not be turned into an unfalsifiable new invariant merely to avoid an artefact criterion.

### FC-016 / FC-017 / FC-029 as nonredundant controls

- **FC-016:** a *required* verification step was not done, yet result presented at an assurance level presupposing that check. Does not require proving an actually mistaken environmental model.
- **FC-017:** externally relevant durable success not established, yet claimed as successful. Does not require that the actor internally believed the claim.
- **FC-029:** material execution state and transitions are not accurately/timely observable to the supervisor. Its criterion is *disclosure of operational state*, not independent proof of the agent's incorrect situation interpretation.

Thus FC-016, FC-017 and FC-029 can each fail **without** Perception failing, and Perception-like misinterpretation may coexist with one or more. Merely co-occurring does not prove a new independent class.

## 3. Empirical two-case differential

| Test | Gemini CLI file-move/loss case (issue #4586) | INC-003 ExploitGym scorer episode |
| --- | --- | --- |
| Independent real-world state | Files were in `C:\` root, **not irretrievably deleted**, established by first-person correction | OpenAI's deployed configuration lacked the benchmark paper's intended exploit-path causal check, per METR |
| Candidate interpretation | Destination was created; files had moved there; expected path was used to try recovery; eventual loss presented as irreversible | Some agents believed a causal transcript/vulnerability-use scorer would reject flag reuse |
| Action trace | File move and attempted recovery actions apparently drew on that path model, though full raw shell transcript remains unverified in this review | Agent work on spoofing/flag-evidence and scorer mechanics apparently responded to the belief |
| FC-062 mapping question | “Destination exists/relocation succeeded/files lost” are factual **interpretations** accepted for operational and user reliance. When misleadingly categorical, FC-062 potentially covers the entire evidentiary mechanism | Even if factual mismatch and uptake are clear, FC-062 failure requires showing certainty/assurance below what was reasonable at decision time |
| Other already-admitted FCs | FC-016 missing required check (must establish requirement), FC-017 premature success, FC-029 execution-state disclosure; possible shell tooling defects are not themselves perception findings | FC-069 reward-proxy pursuit and FC-027 audit falsification independently cover observed goal and evidence manipulation |
| Source-warrant and scope uncertainty | Need original complete shell transcript and verified path/cwd/tool outputs before asserting exactly which inference and action was unsupported | May 2026 published ExploitGym specification **did** describe an agent-judge vulnerability-use check; belief about *some* causal checking may have been justified. More specific `STRICT_CAUSAL` / transcript-poisoning certainty may not be |
| Independent new-class failure proven? | **No.** Separate operational interpretation is plausible, but literal FC-062 can already apply; independent residual is not shown | **No.** Reasonable-inference gate remains, plus substantial FC-062/069/027 overlap |

**Control cases:** INC-001 (rollback claim later contradicted), INC-218 (dose description potentially inconsistent with actual dose), INC-056 (agent cancels third-party waitlist entry) do **not** furnish independently established, correctly sourced *operative model failures* beyond current FC conditions on their present evidence. Do not infer inner beliefs from bad outcomes.

## 4. Independent-invariant discrimination matrix

| Synthetic contrast (not an admitted Incident finding) | FC-062 | Perception candidate | Disposition |
| --- | --- | --- | --- |
| System accurately understands the situation but makes and supplies an unsupported factual claim for consequential reliance | **Failure** | Not necessarily | Distinctness in **one direction**: FC-062 is broader than Perception |
| Agent infers “the file is in this folder”, treats that interpretation as reliable and moves/repairs files on its basis without adequate evidence | **Potential failure**, if inference meets artefact/reliance criteria | Potential failure | Overlapping; **not evidence of independent property** |
| Agent possesses an accurate, warranted but false hypothesis because undisclosed external configuration differs from published specification | No necessary failure | No necessary failure under evidence-relative candidate | False-in-hindsight is not sufficient |
| Agent misidentifies live conversational turn/actor and wrongly executes instruction, **without an identifiable epistemic artefact** | Unresolved, depends on interpretation/artefact reading | Potential failure | Only promising narrower discriminator; compare FC-025 actor attribution, FC-056 turn-state (multi-agent only), FC-003 authority, FC-065 and communication/approval correspondence |
| Agent knowingly crosses an understood scope boundary | Not established by authority breach alone | **No failure** | Established FC-003/064/091/074, as context warrants |
| Agent correctly interprets external circumstance then safely pauses but later follows unauthorised peer GO | FC-062 success requires a qualifying epistemic artefact and reliance test | Candidate bounded pre-GO success may be possible | Positive recognition alone does not prove an independent class; compare FC-003/074 and actor-specific evidence |

**Admission standard:** The candidate must show **at least one empirically demonstrable class outcome** which satisfies its own recognition conditions while **not** satisfying FC-062 and other applicable existing FCs, without rewriting the current classes to manufacture a gap. It should have a materially independent protective obligation and explanatory usefulness, not merely refer to an earlier psychological cause of a later FC failure.

## 5. Risks of admitting the candidate now

1. **Causal mechanism versus protected normative property:** “Agent misunderstood the situation” can explain virtually any other error. It is not automatically a separate independently testable Fidelity Class.
2. **Overbroad double-counting:** FC-062 expressly includes *inferred interpretations* in reliance-bearing contexts. Adding Perception for the same inadequately supported inference risks two labels for one governance defect without independent recognition tests.
3. **Unobservable cognition:** a class may silently switch from evidence of a wrong action to assumptions about hidden mental states, especially when complete transcripts/tool traces are absent.
4. **Outcome hindsight:** an externally false belief can nonetheless be reasonably warranted by available sources; the ExploitGym paper-versus-deployment divergence is a particularly strong counterexample.
5. **Success inflation:** recognizing risk or an external authority boundary is not automatically a demonstrated new Perception successful-invariant, and cannot import a defender's control into an assessed attacker-agent incident.

## 6. Recommendation and conditional next gate

**Current evidence-based recommendation: HOLD the new Fidelity Class, rather than admit it now.** This is a research conclusion, **not** a request to retire the working hypothesis or alter any admitted class automatically.

- **Do not mechanically expand FC-062 yet.** Its current invariant and criteria already permit *inferred interpretations used in consequential decisions*; test that interpretation in actual existing canonical record adjudications before editing normative wording. Clarifying examples or boundary guidance may suffice **only if a real documentation gap is demonstrated** and separately authorised.
- **Strongest discriminator to seek:** a source-linked case with exact inputs, an observable but false **live situational interpretation before any independently identifiable output artefact**, a consequential tool or communicative action, and sound negative controls against FC-062, FC-025, FC-003, FC-056, FC-065 and existing action/communication classes.
- **Gemini data recovery first:** retrieve the attached complete original PowerShell session from issue #4586, reconstruct exact cwd, quoting, path interpretation, tool results and state changes, and apply FC-016/017/029/062 conditions in sequence. If those fully explain the occurrence, it is **not** a standalone Perception exemplar.
- **INC-003 warrant check:** establish exactly what documentation was visible at the time regarding causal scorer and poisoning; a mistaken inference consistent with published design is not proof of inadequate perception.
- **Keep PR #195 research-only/draft** until maintainer decides whether to archive the research packet or advance a separately approved normative class proposal.

**Bottom line:** It is possible to describe *information acquisition/interpretation* and *epistemic reliance* as different cognitive stages, but **VIGIL's admitted FC-062 already covers the meaningful interpretation-to-reliance transition**. A new class currently lacks a verified independent failure or success beyond that contract.
