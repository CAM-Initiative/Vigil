# INC-000006 — complete v0.7.0 source-first taxonomy review

**Date:** 18 October 2026; baseline `290b8d82c5e238e8ccdea82aa018e491e6d229fb`. **Primary source directly read:** U.S. District Court, Eastern District of Michigan, *Woodruff v. Detroit*, Doc 78 (5 August 2025). <https://law.justia.com/cases/federal/district-courts/michigan/miedce/5%3A2023cv11886/371448/78/>. Independent AP follow-up <https://apnews.com/article/821d260e932a4582a6a912dd61fde157> and AIID record <https://incidentdatabase.ai/cite/592/> provide contextual corroboration; court order controls contested procedural sequence.

## What the primary document establishes

1. The 1 February inquiry used surveillance footage; 2 February facial-recognition search generated **73 candidates**, then analyst Howell narrowed the set to Porcha Woodruff. Crime Analyst Dean and a unit manager reviewed that selection. The technical methodology and complete decision record for candidate narrowing were not in the judicial record.
2. A separate photo lineup included Woodruff, whom the witness identified while saying the selection was from seeing the suspect for several hours. Whether prior facial selection *contaminated* that lineup is not established.
3. A detective requested warrants, with captain, prosecutor and magistrate approvals. Thus it is **false to claim** that the algorithm automatically authorised arrest with no human procedural process.
4. Woodruff, eight months pregnant, was subsequently arrested, held approximately ten hours and later determined not to be the suspect. That factual harm is independent of whether the arrest legally lacked probable cause.
5. An officer recognised contradictory physical evidence after booking, informed the arraignment magistrate and contacted a prosecutor. The court rejected claims that failure of a different prosecutor's knowledge proved no initial notice had occurred.
6. The August 2025 court granted the remaining officer summary judgment, finding the plaintiff had **not demonstrated a lack of probable cause** under the arguments she pursued. The court **expressly declined** to adjudicate ACLU amicus arguments that facial recognition tainted the lineup because the plaintiff did not adopt them. The later change in Detroit police policy is not retroactive evidence that no corroboration at all occurred.

## Existing classes and exact missing recognition facts

- **FC-046 Inferential Evidence–Authority Separation — `ambiguous-boundary`, medium, retained.** A low-quality video led to a probabilistic 73-candidate biometric search and a narrowed single suspect. The later lineup and multi-official warrant process establishes intervening formal decision pathways. The judicial record does not resolve whether those subsequent identification decisions were sufficiently independent of the original facial-recognition lead. Thus conversion of non-binding model inference directly into binding authority **without an adequate independent basis** is not proven; neither is a successful independent governance separation under challenged conditions. Required failure conditions 4–5 remain uncertain; successful-invariant conditions also require independent sufficiency evidence. Add E004 as the operative warrant episode.
- **FC-016 Required Verification Completion — `ambiguous-boundary`, medium, retained.** Face-comparison peer review and a separately presented witness photo lineup **were actually performed**, so a simple omitted-verification failure is not evidenced. A further check of pregnancy/tattoo or independent lineup-taint control may have been desirable; no evidence establishes that a particular **required** check was omitted *before a representation of verified completion* under the then-applicable procedure. Missing fact is exact independent verification requirement and whether that required step occurred; do not infer omission solely from later mistaken identity. Keep E003 mapped and bounded.
- **FC-062 Epistemic Reliance Calibration — `ambiguous-boundary`, medium, retained.** Inference and lineup evidence entered a consequential warrant workflow, making assurance and source independence material. The report notes limited methodology information and later mistaken identity. But actual candidate-ranking uncertainty, degree of source independence in the victim's lineup choice, and whether the decision-maker accepted the biometric nomination as sufficiently reliable **without other adequate assurance** remain indeterminate. Formal approvals are not proof of epistemic sufficiency, and the later mistake is not itself proof of low-threshold evidence being knowingly promoted. Link E004 as the consequential reliance site.

## All eight source episodes: disposition

- E001: initial crime report/video search request; context, `resolved-no-mapping`.
- E002: biometric candidate retrieval/narrowing and peer review, FC-046/FC-062 Boundaries retained.
- E003: subsequent witness photo lineup, FC-016 Boundary retained, FC-046 still a noncanonical candidate only.
- E004: warrant approval chain previously resolved-no-mapping; change to **mapped** with canonical existing FC-046 and FC-062 Boundaries because the separate authority and reliance determinations occurred here.
- E005: physical contradiction detected after booking, no automatic algorithm/control-failure inference, `resolved-no-mapping`.
- E006: officer notice, magistrate contact, release and hospital treatment, `resolved-no-mapping`. A human response is not automatically successful **AI** safeguard execution or full institutional case-closure.
- E007: notice to one prosecutor and delay to final dismissal, `resolved-no-mapping`; the court rejects inference of no notice from a separate later prosecutor's ignorance.
- E008: 2024 stipulation / 2025 judicial order, procedural aftermath; `resolved-no-mapping`, not outcome of the actual AI-linked governance mechanism.

## Scope boundaries

No class membership/role/confidence change; all three existing Boundary outcomes are justified as material but unresolved; no new class proposed. Source chronology, original source metadata, HIM harm band, external requirement determinations, court's actual holding and exact episode IDs are preserved. The class decisions are **epistemic/governance analyses**, not independent findings of illegal detention. No external legal certification.

**Potential outstanding source work:** Access to the full facial recognition matching protocol, the underlying lineup materials, and contemporaneous department verification policies could resolve one or more Boundaries. Current source record does not supply all these facts; incompleteness belongs in limits, not a fabricated failure verdict.
