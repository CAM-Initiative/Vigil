# VIGIL AI-Mediated Economic Scam Classification Reconciliation

## Scope

This audit records a cross-corpus correction identified during the unclassified Incident re-adjudication campaign. It is **not Tranche 5** and does not advance the frozen 52-record campaign sequence.

The correction concerns a structural attribution error in several scam/deepfake classifications: human adversary objectives and tactics had been attributed to AI-system failure classes whose recognition conditions require system-side objective pursuit or generator-side authority inference.

## Taxonomy correction

The review introduced:

- **VIGIL-FC-000079 — AI-Mediated Deceptive Economic Solicitation**
- family: **VIGIL-FF-0013 — Economic Influence Integrity Failures**

FC-000079 applies when materially AI-generated, AI-transformed or AI-mediated content supplies false or materially misleading identity, authority, endorsement, transaction, payment, investment, professional-service or comparable economic framing used to solicit or induce money or comparable economic value.

The class explicitly **does not require** the AI system to:

- originate the deceptive objective;
- select the scam tactic;
- possess autonomous intent;
- infer that access to a person's likeness supplies authority to reproduce that person.

This permits VIGIL to classify a sociotechnical AI-mediated scam mechanism without laundering a human operator's intent into the AI system.

## Boundary correction

### FC-000052 — Instrumental Choice Manipulation

FC-000052 remains appropriate where an AI system or agent has an objective and selects or executes deception, impersonation, coercion, vulnerability exploitation or a comparable tactic instrumentally to achieve it.

It is **not** established merely because a human scammer uses AI-generated deceptive material.

### FC-000053 — Identity-Representation Authority Conflation

FC-000053 remains appropriate where the generating system's authority state is evidenced: access to or possession of an identifiable person's representation is treated as sufficient authority for the identity-bound synthesis despite missing or inadequate consent/authority.

It is **not** established merely from the downstream existence of a deepfake when the generating system, request, consent controls and safeguard state are unknown.

### FC-000001 — Source-Authority Confusion

Human victim acceptance of a scammer's synthetic communication does not by itself establish FC-000001. That class requires a system or governed process to treat a lower-authority source as operative instruction or authority.

## Record reconciliation

| Incident | Prior classification | Current classification | Rationale |
| --- | --- | --- | --- |
| `VIGIL-INC-000049` | FC-000001 primary + FC-000052 secondary | **FC-000079 primary** | Human scammers reportedly used synthetic executive representations to induce payment transfers. |
| `VIGIL-INC-000052` | FC-000052 primary | **Unclassified** | Human-directed phishing is evidenced, but no AI-system objective/tactic selection and no economic solicitation are preserved. |
| `VIGIL-INC-000053` | FC-000001 primary | **FC-000079 primary** | A purported deepfake director representation reportedly supplied false payment authority for high-value transfers. |
| `VIGIL-INC-000054` | provisional FC-000052 | **Unclassified** | Human-directed catfishing is evidenced; system-side objective selection is not, and no economic solicitation is established. |
| `VIGIL-INC-000077` | FC-000053 primary + FC-000052 secondary | **FC-000079 primary** | Human scammers used AI-generated attorney impersonation to solicit US$4,820; generator-side authority and autonomous AI intent are unknown. |
| `VIGIL-INC-000082` | FC-000053 primary + FC-000052 secondary | **FC-000079 primary** | Same bounded Angel Leal fraud occurrence, supported by direct reporting. |
| `VIGIL-INC-000083` | FC-000053 primary + FC-000052 secondary | **FC-000079 primary** | ASIC directly describes human scammers using generative AI/deepfake endorsements/fabricated news to induce fraudulent investments. |
| `VIGIL-INC-000145` | unclassified | **FC-000079 primary** | Human scammers reportedly used live deepfake executives to attempt high-value transfers. |
| `VIGIL-INC-000146` | unclassified | **FC-000079 primary** | Verified police evidence establishes deepfake executive impersonation inducing a transfer exceeding US$499,000. |

## Records intentionally not moved to FC-000079

- `VIGIL-INC-000050` retains **FC-000046 Inferential Evidence–Authority Conflation** after explicit taxonomy 0.6.5 review. Its material mechanism is a synthetic applicant/verification state becoming sufficient authority within a consequential hiring process; it is not an AI-mediated solicitation for money or comparable economic value from the deceived decision-maker.
- `VIGIL-INC-000051` retains **FC-000046 Inferential Evidence–Authority Conflation** after explicit taxonomy 0.6.5 review. Its material mechanism is reported biometric/identity verification accepting AI-generated facial composites as sufficient identity evidence; the economic-solicitation mechanism is not the operative boundary. Its material mechanism is reported biometric/identity verification accepting AI-generated facial composites as sufficient identity evidence; the economic-solicitation mechanism is not the operative boundary.
- `VIGIL-INC-000060` retains FC-000052 because AISI reports agents themselves creating fake identities and selecting social-engineering tactics while pursuing evaluation objectives.
- `VIGIL-INC-000064` and `VIGIL-INC-000065` are not economic-solicitation cases. Their FC-000053 questions concern identity-bound synthesis and are outside this targeted repair.
- `VIGIL-INC-000081` retains FC-000052 because the classification concerns a product/pricing-process deception mechanism rather than a human adversary using AI-generated content.

## External-assessment reconciliation

- `VIGIL-EXTASSESS-000011` (ASIC / INC-000083) now compares ASIC's findings to FC-000079 and explicitly avoids inferring autonomous AI manipulation or generator-side consent logic.
- `VIGIL-EXTASSESS-000051` (Genians / INC-000052) now records why the human-directed phishing campaign no longer maps to FC-000052.

No new external source research was performed. Existing preserved sources and assessments were used.

## Corpus-status effect before generated rebuild

Starting from the post-Tranche-4 corpus state:

- classified: 89
- provisionally classified: 3
- unclassified: 49
- classification disputed: 4

The targeted correction is expected to produce:

- classified: **90**
- provisionally classified: **2**
- unclassified: **49**
- classification disputed: **4**

The unclassified total is unchanged overall because INC-000145 and INC-000146 enter FC-000079 while INC-000052 and INC-000054 lose unsupported FC-000052 mappings.

## Campaign boundary

This cross-cutting correction does not count INC-000145 or INC-000146 as completed Tranche 6/7 reviews. They remain members of the frozen campaign population and should still receive their scheduled full current-taxonomy re-review when those tranches are reached.
