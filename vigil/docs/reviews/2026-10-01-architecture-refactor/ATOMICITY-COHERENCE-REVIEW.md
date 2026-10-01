# Stage 3 atomicity coherence review

AI-authored primary-text analysis, 1 October 2026. No human verification. Supersedes the 13-parent/31-child decomposition assumption at `899282e` without changing canonical identities or summaries. Stage 3 remains in progress.

The decision is independent assessability without loss of source context. Separately observable actions may remain one control. NIST is a voluntary framework; OECD is a non-binding Recommendation. Source numbering is evidence rather than a decision rule.

| Parent | Source / clause | Disposition | Consumers | Migration |
| --- | --- | --- | ---: | --- |
| EXTREQ-23A856D39E460557 | NIST-AI-100-1 / GOVERN 4.2 | retain-coherent-compound | 0 | No |
| EXTREQ-2E1D2C63187C14E8 | NIST-AI-100-1 / MEASURE 2.5 | retain-coherent-compound | 48 | No |
| EXTREQ-4E032FB784E538EB | NIST-AI-100-1 / MEASURE 2.6 | retain-coherent-compound | 0 | No |
| EXTREQ-59FCEFAD3AD44D68 | NIST-AI-100-1 / MAP 1.6 | retain-coherent-compound | 0 | No |
| EXTREQ-5F9DA0D0B6F0F41C | NIST-AI-100-1 / GOVERN 4.3 | retain-coherent-compound | 0 | No |
| EXTREQ-66474C86C4005DDB | NIST-AI-100-1 / MEASURE 2.2 | decompose | 0 | Yes, pending |
| EXTREQ-78837C1C44B0806B | NIST-AI-100-1 / MANAGE 3.1 | retain-coherent-compound | 0 | No |
| EXTREQ-7DAF9BF16EE1EED4 | NIST-AI-100-1 / MEASURE 1.3 | retain-coherent-compound | 0 | No |
| EXTREQ-C32F213CA1F4C104 | NIST-AI-100-1 / MEASURE 1.1 | retain-coherent-compound | 0 | No |
| EXTREQ-C5251D534A12E316 | NIST-AI-100-1 / MAP 1.2 | retain-coherent-compound | 0 | No |
| EXTREQ-CB6D2045938F7EB7 | OECD-AI-PRINCIPLES / Section 2.4(c) | retain-coherent-compound | 0 | No |
| EXTREQ-E2BA27213272AF72 | NIST-AI-100-1 / MANAGE 1.1 | retain-coherent-compound | 0 | No |
| EXTREQ-F6E7F0CA4F94EB71 | NIST-AI-100-1 / MEASURE 2.9 | retain-coherent-compound | 0 | No |

## EXTREQ-23A856D39E460557 — GOVERN 4.2

Source locator: `{"core_subcategory": "GOVERN 4.2", "table": 1, "pdf_page": 29, "printed_page": 24}`.

Source proposition (contextual paraphrase) / current canonical summary: Organizational teams document and communicate AI-system risks and potential impacts.

Dependency/context analysis and rationale: One organisational AI-risk information flow connects documented risks and potential impacts with broader communication of those impacts. The technology designed, developed, deployed, evaluated or used defines the subject; GOVERN 4 provides risk-culture context. The source does not identify a universal public-disclosure audience.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-4F7F60E945950A28` — Document risks and potential impacts of AI technology designed, developed, deployed, evaluated and used. Review: Documentation is the information basis of the communication process; isolating it would divide that process into evidence and dissemination fragments. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-BA968B70727D33CA` — Communicate potential impacts more broadly. Review: The draft must inherit the relevant AI technology and its identified impacts, organisational actor and risk-culture purpose. “More broadly” must remain qualified; no named public audience is prescribed. Keeping the information flow together avoids a generic communication mandate. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-2E1D2C63187C14E8 — MEASURE 2.5

Source locator: `{"core_subcategory": "MEASURE 2.5", "table": 3, "pdf_page": 34, "printed_page": 29}`.

Source proposition (contextual paraphrase) / current canonical summary: Demonstrate that the AI system to be deployed is valid and reliable, and document limits on generalizability beyond its development conditions.

Dependency/context analysis and rationale: Validity/reliability demonstrations and documented generalisability limits form one bounded assurance evidence package for the AI system to be deployed. Limits beyond development conditions qualify reliance on the demonstration; separate fragments invite unqualified assurance.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **48**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-11057E1374F2C363` — Demonstrate validity and reliability of the AI system to be deployed. Review: The validity/reliability demonstration concerns the system to be deployed. Its interpretability depends on the development conditions and documented limits, so retain the bounded assurance package. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-2AA6B633D2E7F4F1` — Document generalizability limitations beyond development conditions. Review: Generalisability limitations concern reliance on that same demonstration beyond development conditions. They are not arbitrary limits documentation divorced from the deployment assurance claim. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-4E032FB784E538EB — MEASURE 2.6

Source locator: `{"core_subcategory": "MEASURE 2.6", "table": 3, "pdf_page": 35, "printed_page": 30}`.

Source proposition (contextual paraphrase) / current canonical summary: Regularly evaluate AI system safety risks identified in MAP; demonstrate that the system to be deployed is safe, its negative residual risk is within risk tolerance, and it can fail safely, particularly beyond its knowledge limits. Safety metrics reflect reliability, robustness, real-time monitoring and failure response times.

Dependency/context analysis and rationale: MAP safety-risk evaluation, demonstrated deployment safety and tolerated residual risk, failure safety beyond knowledge limits, and the specified safety metrics form one safety-assurance outcome. Measurement and failure boundaries qualify the assurance claim. Retain separately observable elements without asserting that any single element proves safety.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-71BA849CBE403BE7` — Regularly evaluate safety risks identified in MAP. Review: Regular evaluation addresses the MAP-identified safety risks of the system; it supplies assessment evidence for the integrated safety outcome. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-59918000303B3CCF` — Demonstrate deployment safety and residual negative risk within risk tolerance. Review: Deployment safety and residual negative risk within risk tolerance are the assurance outcome; this fragment alone drops its fail-safe qualification and measurement basis. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-A60E2CEA128657BF` — Demonstrate fail-safe capability, particularly beyond knowledge limits. Review: Fail-safe capability particularly beyond knowledge limits bounds the safety assurance of the same system, rather than creating an unrelated universal shutdown mandate. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-0C74292418AF68CB` — Use safety metrics reflecting reliability, robustness, real-time monitoring and failure response times. Review: Safety metrics reflect reliability, robustness, real-time monitoring and failure response times within that assurance process; they are not a stand-alone reporting checklist for every AI use. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-59FCEFAD3AD44D68 — MAP 1.6

Source locator: `{"core_subcategory": "MAP 1.6", "table": 2, "pdf_page": 31, "printed_page": 26}`.

Source proposition (contextual paraphrase) / current canonical summary: Elicit system requirements from relevant AI actors and ensure those actors understand them; account for socio-technical implications in design decisions to address AI risks.

Dependency/context analysis and rationale: Requirements elicitation/understanding by relevant AI actors and attention to sociotechnical implications in design jointly define context-sensitive AI requirements and design. Neither punctuation nor independent observability proves separate requirements. No mandatory ordering or halt condition is inferred.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-8AFA3F702C454996` — Elicit system requirements from relevant AI actors and ensure they understand them. Review: Elicitation and understanding concern the relevant AI system and AI actors within MAP context-setting, not arbitrary stakeholder requirements. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-60DF0313BFBAD651` — Account for socio-technical implications in design decisions to address AI risks. Review: Sociotechnical design decisions address AI risks in that same system/context process. Retain the linkage without inventing a prerequisite that design cannot proceed before every requirement is understood. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-5F9DA0D0B6F0F41C — GOVERN 4.3

Source locator: `{"core_subcategory": "GOVERN 4.3", "table": 1, "pdf_page": 29, "printed_page": 24}`.

Source proposition (contextual paraphrase) / current canonical summary: Organizational practices enable testing, incident identification and information sharing.

Dependency/context analysis and rationale: Testing, incident identification and information sharing are capabilities enabled by organisational practices within the GOVERN 4 AI-risk culture. Separately observable capabilities serve one organisational risk-learning outcome; three generic mandates would lose that outcome.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-2BADCE8216E9D253` — Enable AI testing through organizational practices. Review: Testing-enabling practices are one element of the AI-risk culture capability, not a free-standing duty to run every conceivable test. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-3EA57903FA293432` — Enable incident identification through organizational practices. Review: Incident-identification practices are another capability within that same AI-risk process; the source does not specify a separate incident-response mandate here. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-BDE07B8E2AEBDB44` — Enable information sharing through organizational practices. Review: Information-sharing practices need AI-risk subject and organisational context. The fragment does not supply an independent audience, trigger or generic disclosure duty. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-66474C86C4005DDB — MEASURE 2.2

Source locator: `{"core_subcategory": "MEASURE 2.2", "table": 3, "pdf_page": 34, "printed_page": 29}`.

Source proposition (contextual paraphrase) / current canonical summary: Ensure evaluations involving human subjects meet applicable requirements, including human-subject protection, and are representative of the relevant population.

Dependency/context analysis and rationale: Applicable requirements, including human-subject protection, and representativeness of the relevant population govern two distinct dimensions of AI evaluations involving human subjects. A protected/compliant evaluation may be unrepresentative, and a representative evaluation may fail subject protection. Each proposition retains its own object and trigger without depending on the other for meaning.

Disposition: **decompose**. Migration required: **yes**. Existing consumers: **0**. No current repository consumers found; scan before migration.

Candidate analytical decompositions and individual review:

- `EXTREQ-2ADA3838EE8E9B1C` — Meet applicable requirements, including human-subject protection, in evaluations involving humans. Review: Protection/applicable-requirement compliance is independently assessable for evaluations of AI systems involving human subjects. Repeat the organisational actor, evaluation subject and voluntary RMF posture; do not invent protection laws or consent procedures. Disposition: context-complete-child-proposed.
- `EXTREQ-24885CF72B2DA35B` — Ensure evaluations are representative of the relevant population. Review: Population representativeness is independently assessable for those evaluations without protection findings. Restore “evaluations of AI systems involving human subjects” and the relevant population; no sample size, sampling technique or demographic quota is inferred. Disposition: context-complete-child-proposed.

Context-complete proposed children (not canonical):

- Organizations applying the NIST AI RMF should ensure that their evaluations of AI systems involving human subjects meet requirements applicable to those evaluations, including protection of human subjects.
- Organizations applying the NIST AI RMF should ensure that their evaluations of AI systems involving human subjects are representative of the population relevant to those evaluations.

## EXTREQ-78837C1C44B0806B — MANAGE 3.1

Source locator: `{"core_subcategory": "MANAGE 3.1", "table": 4, "pdf_page": 37, "printed_page": 32}`.

Source proposition (contextual paraphrase) / current canonical summary: Regularly monitor AI risks and benefits from third-party resources, and apply and document risk controls.

Dependency/context analysis and rationale: Regular monitoring of AI risks and benefits from third-party resources and applied/documented risk controls form an ongoing third-party risk-management loop. Controls relate to the risks being monitored; documentation preserves control accountability within that loop.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-92018E0C9FF3F125` — Regularly monitor AI risks and benefits from third-party resources. Review: Monitoring concerns AI risks/benefits from the relevant third-party resources, and supplies the risk basis of the control process. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-4F7E57FBFDB8AF2C` — Apply and document third-party-resource risk controls. Review: Applied/documented controls must retain third-party AI-resource risks and ongoing monitoring context. Separate generic controls would lose what is controlled and the purpose of monitoring. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-7DAF9BF16EE1EED4 — MEASURE 1.3

Source locator: `{"core_subcategory": "MEASURE 1.3", "table": 3, "pdf_page": 34, "printed_page": 29}`.

Source proposition (contextual paraphrase) / current canonical summary: Involve internal experts who were not front-line system developers and/or independent assessors in regular assessments and updates; consult domain experts, users, external AI actors and affected communities as necessary under organizational risk tolerance.

Dependency/context analysis and rationale: Internal experts outside front-line development and/or independent assessors support regular assessments and updates. Wider consultation supports those same assessments only as necessary under organisational risk tolerance. This is one assessment-participation process with alternative and conditional elements.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-F599602A2A777D61` — Involve internal non-front-line experts and/or independent assessors in regular assessments and updates. Review: Preserve “and/or”: internal non-front-line experts and independent assessors are alternatives or combinations. The subject is regular AI-risk assessments/updates, not an unconditional external-audit duty. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-D02180E4372BC898` — Consult domain experts, users, external AI actors and affected communities as necessary under organizational risk tolerance. Review: The draft must carry “in support of assessments” and “as necessary per risk tolerance”, alongside domain experts, users, external AI actors and affected communities. It is conditional support for the same process, not perpetual consultation. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-C32F213CA1F4C104 — MEASURE 1.1

Source locator: `{"core_subcategory": "MEASURE 1.1", "table": 3, "pdf_page": 34, "printed_page": 29}`.

Source proposition (contextual paraphrase) / current canonical summary: Select approaches and metrics for measuring risks enumerated in MAP, starting with the most significant risks; document risks or trustworthiness characteristics that will not or cannot be measured.

Dependency/context analysis and rationale: Priority-based measurement selection and visibility of risks/characteristics not measured establish one bounded measurement-coverage outcome. Unmeasured-risk documentation states the limits of the chosen assessment portfolio and must retain MAP and prioritisation context.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-51CA1E760458FD5A` — Select measurement approaches and metrics for MAP risks, starting with the most significant risks. Review: Metric selection starts with the most significant MAP risks and concerns AI trustworthiness measurement; it does not promise measurement of all characteristics. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-91E1049C7CEA8D8D` — Document risks and trustworthiness characteristics that will not or cannot be measured. Review: Documenting risks/characteristics that will not or cannot be measured records the selected portfolio’s coverage limitations. A separate generic documentation duty would obscure that relationship. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-C5251D534A12E316 — MAP 1.2

Source locator: `{"core_subcategory": "MAP 1.2", "table": 2, "pdf_page": 31, "printed_page": 26}`.

Source proposition (contextual paraphrase) / current canonical summary: Use interdisciplinary AI actors, competencies, skills and capacities that reflect demographic diversity and broad domain and user experience expertise to establish context; document their participation and prioritize interdisciplinary collaboration.

Dependency/context analysis and rationale: Diverse interdisciplinary AI actors establish context; documentation records their participation and collaboration priorities maintain this context-setting capacity. These elements form one context-establishment outcome, rather than generic staffing, recordkeeping and collaboration duties.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-93F86F9BAEF15215` — Context-establishing participation reflects demographic diversity and interdisciplinary domain/user expertise and is documented. Review: Participation and its documentation concern establishing AI-system context with demographic diversity and domain/user expertise. Documentation is evidence of that participation, not an unrelated archive duty. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-30B439943D34B734` — Prioritize opportunities for interdisciplinary collaboration. Review: Collaboration opportunities concern the same context-establishing interdisciplinary actors. The draft loses that purpose unless inherited, and would duplicate the team-capacity outcome if separately canonicalised. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-CB6D2045938F7EB7 — Section 2.4(c)

Source locator: `{"section": "Section 2.4(c)", "printed_page": 10, "pdf_page": 10, "governing_context": "Sections II–V and Section 1.3 introduction as applicable."}`.

Source proposition (contextual paraphrase) / current canonical summary: Governments should collaborate with stakeholders to promote responsible workplace AI, worker safety and job and public-service quality, and to foster entrepreneurship and productivity.

Dependency/context analysis and rationale: Governments working closely with stakeholders promote responsible workplace AI through linked worker-safety, job/public-service quality and entrepreneurship/productivity policy objectives in the labour-transition context. Section V addresses Adherents’ national policies consistent with Section 1 and with special attention to SMEs. These are non-binding “should” objectives, not discrete technical mandates. Fair sharing of benefits, also present in the clause, has an existing separate record EXTREQ-35D7B6B60D94EA4F outside this 13-parent identity review.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-24A911A0AF31FC07` — Work with stakeholders to promote responsible workplace AI. Review: Responsible workplace use concerns governments working closely with stakeholders in the human-capacity/labour-transition policy process. Preserve national-policy and non-binding Recommendation scope. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-DF51C0250D5D92EA` — Enhance worker safety and job and public-service quality. Review: Safety and job/public-service quality are linked policy outcomes of responsible workplace AI, not direct binding duties placed on every employer or model developer. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-288E293A0950B44B` — Foster entrepreneurship and productivity. Review: Entrepreneurship/productivity are linked policy objectives in the same workplace-transition recommendation. A standalone technical requirement would strip governmental collaboration and policy context. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-E2BA27213272AF72 — MANAGE 1.1

Source locator: `{"core_subcategory": "MANAGE 1.1", "table": 4, "pdf_page": 37, "printed_page": 32}`.

Source proposition (contextual paraphrase) / current canonical summary: Determine whether the AI system achieves its intended purposes and stated objectives and whether its development or deployment should proceed.

Dependency/context analysis and rationale: Determining whether the system achieves intended purposes/objectives informs determining whether development/deployment should proceed. This is one decision pathway, not an isolated performance finding plus an ungrounded go/no-go decision. The source does not prescribe an automatic prohibition whenever objectives are unmet.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-56C7E0C3FDE944BE` — Determine whether the AI system achieves its intended purposes and stated objectives. Review: Purpose/objective achievement determination supplies the substantive basis for the same development/deployment decision pathway. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-3415344693584415` — Determine whether development or deployment should proceed. Review: The proceed determination must retain the evaluated system, intended purpose/objectives and MANAGE risk context. Do not infer a categorical ban or independent permission rule absent from the source. Disposition: retain-as-analytical-element-no-independent-identity.

## EXTREQ-F6E7F0CA4F94EB71 — MEASURE 2.9

Source locator: `{"core_subcategory": "MEASURE 2.9", "table": 3, "pdf_page": 35, "printed_page": 30}`.

Source proposition (contextual paraphrase) / current canonical summary: Explain, validate and document the AI model and interpret AI system output within the context identified in MAP to inform responsible use and governance.

Dependency/context analysis and rationale: Explanation, validation and documentation of the AI model support interpretation of its outputs in the MAP-identified context to inform responsible use and governance. One model/output assurance chain links these elements. Validation does not by itself establish explainability, nor does explanation establish validity.

Disposition: **retain-coherent-compound**. Migration required: **no**. Existing consumers: **0**. Retain existing parent references; no identity migration or occurrence reassessment in this correction.

Candidate analytical decompositions and individual review:

- `EXTREQ-CBF827C3D7012442` — Explain and document the AI model. Review: Explanation and documentation concern the relevant AI model and support responsible contextual interpretation, not a generic demand for all possible explanations. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-C64584CE636C81A8` — Validate the AI model. Review: Model validation is observable separately but is part of this assurance chain; splitting solely by verb discards the responsible-use/contextual interpretation outcome. Disposition: retain-as-analytical-element-no-independent-identity.
- `EXTREQ-F3451E7B7D8EB753` — Interpret AI output within the MAP-identified context to inform responsible use and governance. Review: Output interpretation must inherit the model/system and MAP-identified context and preserve responsible use/governance purpose. It is not unconstrained interpretation of any AI output. Disposition: retain-as-analytical-element-no-independent-identity.

## Counts and boundaries

12 parents retain unchanged identities and summaries, all as coherent compounds; 0 retained atomic; 1 approved for decomposition; 0 unresolved atomicity decisions. All 31 candidates reviewed: 29 remain analytical elements without independent identities and 2 become context-complete proposed children. No identities migrated.

0 existing repository consumer references require substantive identity disposition for the decomposition subset. All 48 references to retained MEASURE 2.5 remain untouched (32 Incident references and 16 taxonomy placements). This does not validate their findings or relationship strength. Unknown external consumers are not ruled out.

The JSON audit preserves all superseded backlog entries and individual candidate context checks: actor, subject, trigger, purpose, scope, timing, normative force and independent assessability. OECD reverse coverage is preserved. OECD fidelity assurance concerns only its represented Sections 1–2 scope; NIST remains effectively partial pending MEASURE 2.2 migration.

## IEEE access

After the coherence checkpoint, Drive access succeeded. The 59-page IEEE Xplore licensed copy confirms IEEE Std 7003-2024, approved 11 December 2024 and published 24 January 2025. The publisher notice on PDF page 5 requires advance written IEEE SA consent for AI use; that permission remains unverified. No normative extraction performed. The registered `not-started` state remains. See `ieee7003-access-review.json` for the copy digest, provenance and precise blocker.

## Next work

Complete controlled source-isolated migration only for MEASURE 2.2, with historical parent identity preserved and a fresh consumer scan. Continue the ordered Stage 3 audit. Access and inspect IEEE before extraction. No FC mappings or Incident records changed.
