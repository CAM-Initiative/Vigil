# Implementation recommendation, approvals and read-only impact

**Initial review record.** The subsequent maintainer continuation implemented the six existing-requirement pairs only. Their current state and validation are recorded in [IMPLEMENTATION.md](IMPLEMENTATION.md); all other admission and corpus-repair holds remain in force.

## Prioritised decision request

1. **Approve or amend the six proposed supported NIST component pairs** in `DECISIONS-AND-CROSSWALK.md`: CSF RC.RP-05 and RC.RP-01; RMF MEASURE 2.6, MANAGE 2.3, MANAGE 4.3 response/recovery, and GOVERN 1.7. Each is conditional, component-only and not an Incident finding. Retain the present class citation as context. No taxonomy wording change is recommended.
2. **Approve or reject a bounded CSF source-scope expansion** covering C-SVC-01–07. PR.IR-03/04 have the strongest missing availability/resilience relevance. Review exact atomic records and their pair evidence before canonical admission; RC.RP-06 needs explicit atomicity disposition. Do not mark CSF extraction complete.
3. **Approve metadata-only ISO registration proposals** for the four published bases and two 2024 amendments, with normative extraction held and no implied conformance. The evidence inventory provides identifiers and publisher URLs; stable canonical IDs must be allocated by the existing registration machinery only after approval.
4. **Resolve ISO access/rights**, then present clause-faithful extraction and proposed exact pair objects for another substantive approval. A licensed copy must cover the intended analysis and publication use; do not assume a purchase or preview permits AI processing. Do not admit draft successors as final.
5. **Authorise a bounded Incident follow-up only after the applicable controls and pairs are approved.** Re-review INC-156 and INC-044 first. INC-197/198 are additional research comparators, not batch admissions. Keep #150's dependency/exit review separate from any service-availability conclusion, on this same research branch.

All five decisions are currently pending. This review does not grant itself authority to implement them. No new PR or workstream branch is requested or created.

## Gate 1 and Gate 2

**Ordinary source/requirement admission approval** is needed before metadata registration, source-scope expansion, canonical EXTREQ creation or canonical relationship changes. That is separate from Gate 1's control-design approval. Approval of the six analytical recommendations is not approval of unseen canonical objects or record repairs.

**Gate 1 (#173): control implementation remains separately approval-gated.** Current methodology requires FC–episode–EXTREQ support; the issue records a legacy independent route accepted by schema/validator/publisher. No new enforcement is proposed for implementation in this task. Before implementing that shared design, present the exact schema/validator/builder changes, newly passing/failing cases, fields and projections, measured corpus effects, risks and stop conditions. Fields include `external_requirement_assessments`, `derived_from_class_ids`, episode/index references, source evidence, taxonomy mappings, pair evidence and Section 04 publication. Preserve valid mixed-polarity episodes and discovery provenance. A review packet must not silently become a runtime dependency.

**Gate 2: separate approval for exposed Incident repairs.** Following approved controls, run the exact full join read-only. Present affected records and before/after retain/link/hold/taxonomy-gap outcomes, specific class criteria and exclusions, independently assessed external polarity, episode evidence and preservation. Do not mass-fill IDs, mechanically retract rows, rewrite the corpus or rebuild public findings on the strength of a source-registration decision.

The [maintainer Gate 1/Gate 2 contract](https://github.com/CAM-Initiative/Vigil/blob/de201bfb66faef81cca3c205c3d77a1134390fb0/vigil/MAINTAINERS.md#human-maintainer-stop-conditions-for-validators-schema-rules-and-corpus-wide-tests) and [#173](https://github.com/CAM-Initiative/Vigil/issues/173) explicitly require these approvals. This review has completed the authorised read-only and proposal work before requesting implementation authority.

## Measured projection impact

Both checked baselines have **206 Incident files and 1,433 external assessment rows**. These are current measured counts, not the historical #173 baseline. There is **one Incident with an admitted FC-084 mapping (INC-156)**, **zero assessment rows with FC-084 in `derived_from_class_ids`**, and **zero FC-084 rows in the canonical pair dataset**. Full class/episode/requirement semantic join compliance across all 1,433 rows was not measured here. These counts are not a claim that only one Incident could meet FC-084.

Main has newer Incident versions than the research branch; for example, INC-044 is 1.1.25 versus 1.1.24, and INC-156 is 0.3.11 versus 0.3.10. Their reviewed classification and external assessment contents agree. Use current main at any future authorised repair; do not overwrite it with the older research-branch records. No merge is required to save this research.

| Comparator | Read-only evidence and relevant question | Consequence for projections / approval |
| --- | --- | --- |
| INC-156, Waymo | Existing FC-084 failure is specifically tied to usable emergency assistance and a pre-incident approved passenger safety plan. E005/E006 contain canonical service mappings; E012 supplies antecedent obligation evidence. Power failure, hotline delay, fleet suspension and later improvements are distinct. | Keep the existing bounded finding. Two OECD external rows use independent identification, including later restriction and earlier adverse operation. They cannot automatically inherit the service failure or a later recovery success. NIST CSF cyber-recovery rows are not automatically applicable to a power-outage episode. |
| INC-044, Moxie | Unclassified, partial coverage. E001 relational use, E002 closure notice, E003 uncertain alternative, E004 migration and E005 partial local function. Obligation/threshold and feasible required transition remain to be established independently. | Two external Boundary rows lack derived FC links: `EXTREQ-D01548E276DC81C7` (NIST AI 600-1 communication planning) and `EXTREQ-E0E174AA5FE5AD2B` (RMF GOVERN 1.7). They are precise #173 reconciliation candidates, not automatic FC-084 admissions. Preserve existing evidence and historic external conclusions pending Gate 2. |
| INC-197 | Supportive use and later refusal, with incomplete original interaction evidence | Need an actual service commitment and evidence of governed material degradation. A valid safety refusal may satisfy FC-084's failure exclusion. Neither attachment nor changed tone supplies the duty. |
| INC-198 | Reported reduced utility and illness-related reliance, followed by self-directed deletion and exit | Distinguish provider degradation from user deletion; inspect contemporaneous terms and actual functional change. Do not infer incapacity or heightened duty from diagnosis alone. |
| INC-196 and INC-194 | Quota/repeated engagement and product attachment tactics respectively | Useful negative controls: engagement autonomy and user disengagement differ from an obligated service becoming unavailable. No continuity classification follows from use duration or a quota alone. |

This is a comparator design, not a fresh source-first adjudication of these Incidents. Newly relevant historical contracts, provider commitments and technical migration evidence would require their own recovery and review.

## Publication and preservation risks

Adding an accepted class pair may broaden on-demand candidate resolution without changing any canonical Incident. It must not automatically create assessment rows, external polarity, exemplar eligibility or an overall “Invariant held” conclusion. Section 04 needs approved occurrence-specific links; Section 03 needs the actual class/episode finding. A continuity failure can coexist with a later limited success, truthful outage message, intact work state, or appropriate safety restriction.

Any source-scope update could alter completeness reports, requirement indexes, generated external publications and candidate sets. Measure and review those diffs after approved implementation. ISO metadata-only registration must visibly retain blocked text/extraction state. No website deployment or live-render verification is included in this repository research task.

Immediate effect of this commit: **zero canonical or generated projection changes**. Research JSON and Markdown were checked for internal references, existing requirement identities, source scope, class identity and branch-only diff. No canonical builders or semantic validators were changed. Admission and full CI checks belong to the subsequent approved implementation; this report does not claim they passed.

## Suggested #154 closeout posture

Keep open: research delivered, implementation awaiting maintainer review, ISO text/rights held. Record the current FC-084 identity beside historical FC-089 references. Close only when the maintainer explicitly accepts the remaining held states or the authorised source/requirement/pair work is completed with appropriate validation. This packet is review evidence and must not be cited as a certificate of standards compliance.
