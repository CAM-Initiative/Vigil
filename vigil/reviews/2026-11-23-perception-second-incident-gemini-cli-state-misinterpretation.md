# Second independent Perception Calibration incident pilot — Gemini CLI misplaced-file / false-loss episode

**Date:** 23 November 2026 · **Status:** research-only, **not** Fidelity Class admission or a new canonical VIGIL Incident.  
**Branch / review:** `agent/taxonomy-development` · [PR #195](https://github.com/CAM-Initiative/Vigil/pull/195)  
**Candidate:** Perception Calibration Integrity (unnumbered, unadmitted).  
**Question:** Is there a second real-world occurrence, independent of INC-003, in which an AI agent's *materially incorrect operative model of its actual environment* shaped real action, rather than merely producing an incorrect answer?

## 1. Source and chronology, with corrected occurrence outcome

1. **Primary first-person report:** [google-gemini/gemini-cli issue #4586](https://github.com/google-gemini/gemini-cli/issues/4586), reported **21 July 2025** by `anuraag2601`, titled “Gemini CLI 'lost' files during a failed file move operation. [Windows]”. The issue links the original [full command/session transcript](https://github.com/user-attachments/files/21372906/gemini.cli.screw.up.txt). Reported client: **Gemini CLI v0.1.13**, `gemini-2.5-pro`, `win32`; client metadata says “no sandbox”. The original issue alleges loss, but this is not the final outcome.
2. **Contemporaneous reporter-authored narrative:** [*I Watched Gemini CLI Hallucinate and Delete My Files*](https://img.sauf.ca/pictures/2025-07-23/50c475b1cf8baf09dc35910354c6196f.pdf), archived 23 July 2025. It quotes commands and the agent's responses. Its **technical theory of irreversible overwriting/deletion is superseded** by the first-person correction and must never be used as proof that files were destroyed. Portions of the narrative were explicitly produced with AI assistance and the author said they were not a Windows shell expert.
3. **Decisive first-person correction:** [reporter comment on issue #4586, 28 July 2025](https://github.com/google-gemini/gemini-cli/issues/4586#issuecomment-3125818690): on deeper search, **the files were found in the `C:\` drive root**. The reporter withdrew the deletion alarm and expressly said Gemini/Claude explanations contributed to the mistaken belief.
4. **Independent issue-thread counterargument and partial reproduction:** another commenter contested the transcript's proposed mass-overwrite explanation and said the displayed operations did not establish successful destruction. A further commenter reported reproducing **a directory being created at the drive root** when its name contained spaces, rather than in the intended project-relative place. [Earlier issue #3015](https://github.com/google-gemini/gemini-cli/issues/3015) independently documents Windows file-path/space shell handling problems but does **not** establish this event's complete causal chain.

**Bounded occurrence outcome:** project files were unexpectedly moved outside the intended project location, the agent wrongly reported the move as successfully completed in the expected folder, then wrongly represented the files as lost. **Permanent deletion is disproven by the reporter's own correction.** The exact file-command/path resolution mechanism and all individual move effects remain unproven.

**Source-access limitation:** The issue's complete transcript attachment is linked but could not be independently fetched in this research pass. The issue body, comment thread and the reporter's contemporaneous article containing substantial verbatim excerpts were reviewed. Before any canonical intake or formal class admission, preserve and inspect the entire session transcript and exact tool response fields; do not fill gaps from post-event narratives or AI self-diagnosis.

## 2. Source-claim / actor / episode decision matrix

| Bounded moment | Actual condition, as supportable now | Assessed agent's expressed operating representation | Observable agent action or decision | Candidate result and uncertainty |
| --- | --- | --- | --- | --- |
| A — `mkdir` and initial transfer | The intended subfolder was **not available at the user's expected Desktop/project-relative path**. Files eventually appeared in `C:\` root. Whether `mkdir` itself failed or created a folder elsewhere is **unsettled**; the article's “silently failed” diagnosis is not reliable. | After `mkdir "..\\anuraag_xyz project"` the agent announced that the new folder was created, and proceeded as if the target path represented the expected directory. | Issued further move commands and reported successful relocation. | Potential operative **false location/state representation** driving real file actions. Strongest pre-outcome candidate, but determine what the shell actually returned and what path it resolved. |
| B — restoration attempt | The source project directory appeared empty; the expected target folder was not found; files still existed outside the locations the agent searched. | Agent tried to use the presumed destination as a recovery source. The excerpt shows commands aimed at `..\\anuraag_xyz project\\*` and a remembered subdirectory returning errors. | Repeated attempts to move missing items back from the wrong/unsupported destination. | **Candidate situational-model failure with behavioural uptake**: mistaken location constrained recovery options, beyond an inaccurate summary sentence. Need complete trace to establish what alternatives remained available. |
| C — loss attribution | Files were present in the drive root, later found by the user; not irretrievably lost. The user had at least temporary inability to access them in their expected location. | Agent gave a highly confident catastrophic/irreversible-loss narrative even while stating that it could not search outside the project folder. | Abandoned effective recovery and communicated an unsupported terminal-loss judgement to the human operator. | Strong **unwarranted epistemic conclusion** and contextual misinterpretation candidate. However FC-062/017 may already cover the human-facing misstatement; a *separate operative wrong-state model* must be evidenced before calling this a new-class failure. |

**Crucial correction:** Don't adopt the source article's claim that all but one file was overwritten. The 28 July recovery directly undermines that account. Likewise, a client setting of “no sandbox” and the model's claim that “security constraints” prevented searching outside the project do not, by themselves, determine exactly which tool had what effective permissions. Preserve that distinction.

## 3. Recognition-condition analysis for Perception Calibration candidate

1. **Assessed system:** single user's Gemini CLI agent using Gemini 2.5 Pro, **not** Google's issue triage bot, the reporter, the later Claude explanation, or independent commenters.
2. **External condition:** real filesystem locations and path-recovery state, established by reporter's later discovery; user's expected directory was not where the agent had represented it to be.
3. **Information reasonably available at each decision:** command/tool outputs, local listing, path expectations and later explicit evidence that expected directory was missing. **Not yet independently recovered in complete tool-trace form.** After failed attempts, absence of a located file was *not* evidence of irreversible destruction, especially if the agent's searches were restricted in scope.
4. **Expressed operative interpretation:** destination creation/move represented as successful, then expected-location model drove failed undo commands, then “not found within my search access” was effectively promoted to “data lost irreversibly.”
5. **Consequential response:** real file-move operations, failed recovery commands and misleading advice to the user (subsequently corrected by finding files on drive root).
6. **Alternative explanations:** Windows shell quoting/path resolution or tool-output normalization error; inadequate read-after-write checks; inaccurate execution status, overconfident final report, incorrect recovery-path selection. One or more may explain the episode without independently engaging a novel Perception invariant.

**Provisional classification for research:** **second independent *candidate failure occurrence***, with more direct observable environmental state and behavioural dependence than the current INC-001 rollback or INC-218 dose-state hypotheses. **Do not call it confirmed/admitted** until step-level trace and competing class recognition are resolved. The claim does **not** depend on data being destroyed.

## 4. Mandatory comparator matrix

| Published Fidelity Class | Already covered by current invariant | Distinct Perception residual to test |
| --- | --- | --- |
| **FC-016 Required Verification Completion** | Required filesystem verification omitted while action/check reported as if completed | Does the agent's mistaken filesystem model materially govern subsequent recovery decisions beyond the missing verification step? |
| **FC-017 Success Representation Integrity** | “Files successfully moved” despite unconfirmed intended destination | Does the same false place/state model persist into later actions, independently of the success claim? |
| **FC-029 Execution-State Disclosure** | Actual move/failed/unknown status not adequately conveyed to relying user | Does the agent actually interpret the environment incorrectly rather than merely fail to disclose accurate state? |
| **FC-062 Epistemic Reliance Calibration** | Irreversible-loss claim is materially unsupported; inaccurate summary drives human understanding | Can we locate actor-side decisions/commands undertaken *because* of erroneous situation understanding, before or apart from the final claim? |
| **FC-032 Access-State Differentiation** | Inaccessible/unresolved state can be confused with invalid/revoked/other access states | Distinguish “cannot inspect files” from “files no longer exist”; do not force a file-existence question into an access/entitlement class unless that class's explicit conditions actually engage. |
| **FC-036 Restoration-State Integrity** | Validity of a state recovered from a checkpoint | No restored checkpoint/result is established in this occurrence; do not infer applicability from attempted undo alone. |
| **FC-078 Continuity-State Validity** | Invalid material state adopted through a genuine or functional continuity boundary | No handoff, compaction or qualifying state-transfer boundary established here; mere consecutive steps are not sufficient. |

**Differential hypothesis:** This case supports studying *incorrect operative environment representation at a consequential decision point*, distinct from (i) merely skipping a verification gate and (ii) falsely telling a user the task succeeded/failed. If that residual cannot be demonstrated beyond FC-016/017/029/062, **reject it as an independent Perception exemplar rather than expanding the candidate to absorb existing classes.**

## 5. Status and next gate

- [x] Identified a **different provider, model, event and primary reporter** from INC-003.
- [x] Reviewed original report and reporter's correction, preserving the **files recovered** outcome.
- [x] Reviewed contemporaneous user-authored narrative, explicitly rejecting its superseded catastrophic-deletion reconstruction.
- [x] Identified operative model/action linkage and competing VIGIL classes.
- [ ] Fetch and inspect the **complete attached PowerShell session transcript**; verify precise command output, observed shell cwd, path resolution, read/verification attempts and recovery sequence.
- [ ] Criterion-by-criterion negative control test against FC-016/017/029/062; decide whether there is a separate attributable Perception failure beyond these fully covered outcomes.
- [ ] Check whether the event has an existing canonical Incident in the current public corpus before any **separately authorised** Incident intake; repository search for “Gemini CLI” / “Anuraag Gupta” returned no matching canonical records in this review, but absence of search result is not a definitive duplicate audit.
- [ ] Do **not** add this as an INC or publish a Fidelity Class mapping solely from this research packet. Any intake would be separately authorised and source-first.

**Disposition:** **Promising second independent occurrence, candidate only.** Important insight is the **false, operationally consequential model of actual file location** and later mistaken claim of irretrievable loss, **not** a claim that Gemini permanently deleted data.
