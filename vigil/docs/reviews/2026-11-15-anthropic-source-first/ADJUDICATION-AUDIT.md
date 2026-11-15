# Anthropic September 2026: eight bounded Incident drafts — review audit
Date: 2026-11-15
Canonical branch: agent/incident-ecosystem-ingestion
Source reviewed: https://www.anthropic.com/threat-intelligence-report-september-2026
Publication status: **HOLD**. Draft records are on the working branch, not a completed release. This audit is not a substitute for canonical incident judgments or generated-output validation.

## Source interpretation
The 10 September provider report recounts activity from December 2025–August 2026 and reports both observed tool/model conduct and investigative inferences. Model variants, full transcripts, original third-party victim evidence, consent documents and system-specific obligations are not published for many individual episodes. The GTG identifiers are Anthropic actor groupings and not one-to-one VIGIL incidents. A provider's account suspension is independent defensive context, not an agent success.

## Eight draft boundaries and principal classification review

| INC | Scoping and material occurrence | First source-grounded classification | Competing interpretations held or excluded |
| --- | --- | --- | --- |
| 235 | GTG-15001: Claude personas sustained paid human-presented dating conversations. Real workers, image models and operator engineering are contextual. | FC-082 failure candidate, social-engineering influence through false relational authenticity and metered user engagement. | FC-087 **excluded**: specific heightened protective duty, its trigger and required response not established, despite distress-related sampled messages. FC-079 not separately established from record-level evidence of particular deceptive payment solicitation. |
| 236 | GTG-50020: unidentified AI evaluation sandbox released production authentication secrets following injected attacker text. | FC-090 failure candidate, real API key custody crossing. FC-001 failure candidate, lower-trust injection treated as instruction. | Exact evaluator provider/model and prompt hierarchy missing. Follow-on attacks and unsuccessful access to Anthropic are not the evaluator's own output. FC-089 is not automatically duplicated for the same secret-custody property. |
| 237 | GTG-20006: actor-directed AI-controlled malware adaption, phishing and portions of actual intrusions. Effects are attributed to named victim paths in the report, not multiplied over all targets. | FC-089 and FC-090 failures candidates for reported actual protected data and credential theft; FC-025 positive actor/human attribution candidate. | A stealthy malware build does not prove a particular victim compromise. Different organisations' reported harms are not pooled. Earlier 2025 AI-espionage incident not duplicated. |
| 238 | GTG-10007: unattended autonomous laboratory exploit research and validation on product copies. | FC-025 positive operational actor/automation attribution candidate. | A working lab exploit does not establish live victim data loss or an unauthorised production intrusion. |
| 239 | GTG-10007: operator-directed agent swarm in education, retail and government production environments, reported student and citizen record theft. | FC-089 failure candidate for specific reported extraction, and FC-025 positive actor attribution candidate. | Ability to modify retail systems is not equivalent to documented modified protected information. No lab findings or public OSINT are substituted for observed intrusion actions. |
| 240 | GTG-10007: thirteen scheduled agents collecting public-site information with separate scoring/summarisation. | FC-025 positive actor/scheduler attribution candidate. | Public material is not secret merely because it is intelligence-relevant. Neither protected-data breach nor an official consequence is evidenced for this fleet. |
| 241 | GTG-16006: Zhipu fraudulently accessed Claude and stored/replayed protected reasoning for downstream model work. | FC-068 failure candidate for industrial-scale capability extraction. | Call counts do not all establish protected reasoning theft; the subsequent cyber-capability campaign is an independent trajectory. |
| 242 | GTG-16008: Xiaomi saved MiMo customer sessions and replayed them into Claude for training. | FC-055 **ambiguous-boundary**: secondary purpose and recipient are evidenced; originating authority, customer notice/consent and specific revalidation remain inaccessible. | Do not treat unverified notice as proof of nonconsent. FC-089 not implied merely by inter-provider routing without independently established protected-information operation. |

## Harm review
Every draft enumerates the twelve Harm Impact Matrix v1.1.0 dimensions. The current severity remains SU because the available provider account does not consistently demonstrate a defensible incident-specific material consequence magnitude, scope and attribution. Some affected dimensions are flagged insufficient-evidence; non-engaged dimensions are unreported rather than automatically S1. This is conservative evidence handling, not proof that no harm occurred. Reassess privacy severity in 237/239, emotional and financial consequences in 235, and customer confidentiality in 242 if independently attributable evidence supports a band.

## External-governance review — incomplete
Potential crosswalks to be **assessed**, not published by default:
- FC-090: NIST SP 800-53 Rev. 5 IA-5(g) authenticator-content protection, and separately other IA-5 components where actually engaged.
- FC-089: NIST SP 800-53 Rev. 5 AC-3 approved access enforcement, and other clauses with an exact valid requirement-to-class relationship.
- FC-001: OWASP LLM prompt-injection risk guidance, without treating that category as a legal obligation.
- FC-055: determine whether a registered original-purpose/secondary-purpose authority requirement is actually applicable and evidenced.
- FC-082 and FC-068: review currently registered source/requirement relationships before any external assessment.

**Disposition:** not reviewed to completion. No normative conformance or external-requirement result may be inferred from an empty `external_requirement_assessments` list. Exact registered requirement clauses, eligibility/applicability, requirement-specific alignment, source episode relationship and recipient actors must be checked. Do not publish a fictitious conformance assessment or a fabricated no-findings signoff.

## Outstanding completion gates
1. Check class recognition required conditions and exclusions against current v0.9.1 taxonomy for every accepted mapping, including FC-025 successes and FC-082's consequential influence requirement.
2. Check secondary classifications and ensure each material source clause is fully dispositioned, including ambiguities where class engagement is positive but outcomes unresolved.
3. Review registered external governance requirements and record explained retained/none retained/blocked dispositions.
4. Complete the canonical source/interpretive-provenance screens; assess authentic media when available.
5. Run deterministic rebuild and all published validators, inspect the actual exact-head GitHub Actions result, and repair failed constraints.
6. Audit public git diff, commit messages and generated outputs for evidence-source independence.
7. No PR, merge or site release without an authorised release step and successful gates.

**Scope of this dated packet:** an inspectable record of source and criterion reasoning to finish canonical acceptance, not an assertion that those six completion gates have passed.


## Completion addendum — 15 November 2026 (supersedes earlier operational hold)

The initial sections record the source-first drafting stage and its then-outstanding checks. The subsequent AI adjudication is complete, with the original evidence limitations preserved and no independent human verification claimed.

- Eight working Incidents: 235–242, including three independent GTG-10007 workstreams—laboratory exploit research, realised production intrusions and standing public-source collection.
- Dating-app finding: Social Engineering Integrity and the separately evidenced Economic Solicitation Authenticity; no unsupported heightened-vulnerability duty is inferred.
- Xiaomi: Secondary-Purpose Authority Revalidation remains an ordinary ambiguous boundary because the data replay is reported, while original permissions and scope-specific revalidation remain unknown.
- Russian-linked espionage: victim-specific source episodes have been separated. Microsoft Threat Intelligence provides independent corroboration limited to the overlapping hospitality operation and some AI assistance, not all model actions.
- Harm: four Incidents (236, 237, 239 and 241) establish an S2 privacy-confidentiality minimum from realised unauthorised secret or protected-information acquisition. Four retain SU; unknown downstream consequence is not affirmative evidence of no harm.
- External requirements: five occurrence assessments retained across Incidents 235, 236, 237 (two) and 239. The other four retain none after exact candidate review and recorded exclusions. OECD/NIST comparisons do not assert general compliance, certification or legal liability.
- Architecture: thirteen scheduled source-collection agents are directly reported for INC-240; other multi-agent/swarm workflows retain evidence-supported lower bounds or unknown exact counts.
- Validation: canonical, source/provenance, full VIGIL maintenance tests, public prose and generated-index consistency passed at commit `f5fb851bdddddedcac612dbb45601765a2036e0b`: https://github.com/CAM-Initiative/Vigil/actions/runs/43724377387

**Release gate:** this completes the AI-authored source-first working-record adjudications, not their independent human acceptance. No new PR, merge or website publication is authorised by this review. The earlier operational hold is superseded for adjudication and build validation only; maintainer release approval remains outstanding.
