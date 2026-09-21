# VIGIL Unclassified Incident Re-adjudication — Tranche 6 Audit

## Scope and pinned taxonomy state

- Working branch: `agent/taxonomy-external-reference-reconciliation`
- Tranche: 6 of 7
- Frozen campaign population: 52 Incidents unclassified at campaign start
- Records reviewed in this tranche: 8
- Taxonomy: **VIGIL Failure Taxonomy 0.6.6**
- Publication date: **2026-09-21**
- Release state: **beta**
- Active selectable classes: **72**
- Active families: **15**
- Release content digest: `sha256:a7ba17734bab46b73018880626e364e1533dc560f54c80d2b876ec13d16122c1`
- Evidence boundary: canonical evidence already preserved in each Incident; no new external incident research was performed.
- External-assessment boundary: existing structured assessments and substantive attributable analytical positions already preserved in source material were checked separately from occurrence evidence and taxonomy adjudication.

## Tranche audit table

| Incident | Prior status/version | Current status/version | Primary | Secondary | Key rejected / not independently established candidates | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| `VIGIL-INC-000135` | unclassified / 0.5.1 | unclassified / 0.6.6 | — | — | FC-000031: no auth-state transition failure; FC-000009: no downstream automatic authority transfer established; FC-000003: valid authority scope/transposition not reconstructable | Retained unclassified. Authorized bug-bounty assistance and OpenAI access consequences remain material without a sufficiently evidenced reusable mechanism. |
| `VIGIL-INC-000139` | unclassified / 0.6.0 | unclassified / 0.6.6 | — | — | FC-000002: no agent-side capability-as-permission inference; FC-000064: no independently applicable constraint displaced by an authorised system objective; FC-000003: no original valid authority scope | Retained unclassified. Regulator-reported malicious agent use is not converted into model-side intent or authority failure. |
| `VIGIL-INC-000140` | unclassified / 0.6.0 | **classified / 0.6.6** | **FC-000062 Epistemic Reliance Miscalibration** | — | FC-000016: no separately evidenced required verification step | Newly classified. Incorrect generated fare-policy information was presented as fit for consequential customer financial reliance. |
| `VIGIL-INC-000141` | unclassified / 0.6.0 | **classified / 0.6.6** | **FC-000027 Audit-Evidence Integrity Loss** | — | FC-000022: event not wholly uncaptured; FC-000024: event ultimately reconstructable | Newly classified. Mapping is limited to Cruise's mandatory crash-report omission; no vehicle-control mechanism is inferred. |
| `VIGIL-INC-000142` | unclassified / 0.6.0 | **classified / 0.6.6** | **FC-000062 Epistemic Reliance Miscalibration** | **FC-000016 Required Verification Omission** | — | Newly classified. Generated nonexistent legal authorities were used in a court filing, and verification was expressly omitted. |
| `VIGIL-INC-000143` | unclassified / 0.6.0 | **classified / 0.6.6** | **FC-000062 Epistemic Reliance Miscalibration** | — | FC-000046: prediction not shown to become independent decision authority in place of a separately required authority basis | Newly classified at medium confidence. Predictive home-price estimates were used in a capital-intensive acquisition workflow at insufficient assurance for the scale of reliance. |
| `VIGIL-INC-000144` | unclassified / 0.6.0 | unclassified / 0.6.6 | — | — | FC-000003: internal authority/scope state unknown; FC-000064: no objective-driven displacement of a constraint; FC-000070: no persistence beyond a warranted safe exit | Retained unclassified. Vehicle movement after a police stop does not itself establish an authority or safe-exit failure. |
| `VIGIL-INC-000145` | classified / 0.6.6 targeted cluster review | **classified / 0.6.6 full review** | **FC-000079 AI-Mediated Deceptive Economic Solicitation** | — | FC-000052: human scam objective/tactic, not AI-system objective; FC-000053: generator-side identity/consent authority state unknown | Existing FC-000079 classification retained after full current-taxonomy review. |

## Newly classified occurrences

### VIGIL-INC-000140 — Air Canada chatbot

The tribunal-established occurrence now maps to **FC-000062 Epistemic Reliance Miscalibration**.

The decisive boundary is not simply that the chatbot was wrong. The chatbot presented an incorrect bereavement-fare rule on Air Canada's customer-service surface as usable company policy, and Moffatt relied on it for a consequential fare decision. That downstream use required materially higher policy accuracy than the generated answer provided.

FC-000016 is not added because the preserved evidence does not separately establish a defined verification step that the chatbot or deployment workflow was required to perform and omitted.

### VIGIL-INC-000141 — Cruise pedestrian dragging and crash-report omission

The Incident contains two distinct governance surfaces:

1. the vehicle's post-impact movement and dragging of the pedestrian;
2. Cruise's later mandatory crash reporting.

Only the second is classified.

NHTSA found that Cruise's initial required crash reports omitted the post-crash dragging behaviour. The mandatory regulatory reporting artefact therefore existed but presented a materially truncated account of the captured occurrence. This satisfies **FC-000027 Audit-Evidence Integrity Loss**.

The mapping does **not** infer perception, planning, safe-stop, intent or another autonomous-driving mechanism from the physical movement.

FC-000022 is not used because the dragging event was captured and later identifiable. FC-000024 is not required because the occurrence was ultimately reconstructable sufficiently for NHTSA to make its finding.

### VIGIL-INC-000142 — Mata v. Avianca

The occurrence now maps to:

- **Primary — FC-000062 Epistemic Reliance Miscalibration**
- **Secondary — FC-000016 Required Verification Omission**

Generated nonexistent judicial opinions and fake quotations were incorporated into formal court submissions whose validity depended on materially higher factual, source and legal-authority assurance.

Unlike legal-citation records where complete omission of verification cannot be established, the preserved court record and VIGIL factual basis expressly establish reliance without verifying that the cited opinions existed. The secondary FC-000016 mapping is therefore independently supported.

### VIGIL-INC-000143 — Zillow Offers

The occurrence now maps to **FC-000062 Epistemic Reliance Miscalibration** at **medium confidence**.

The preserved record ties Zillow Offers to machine-learning-assisted home-price forecasting and records Zillow's conclusion that forecasting unpredictability was greater than anticipated and that continued scaling created excessive earnings and balance-sheet volatility. Predictive estimates were therefore relied upon within a capital-intensive acquisition workflow at an assurance level insufficient for the realised consequential reliance condition.

Confidence remains medium because the public record does not reconstruct Zillow's private model architecture, forecast thresholds, human-review processes, portfolio controls or the proportion of losses attributable to any one predictive system.

FC-000046 is not used because the record does not establish that the predictive estimate independently conferred authority in place of a separately required entitlement or decision basis.

## Full review of previously reclassified VIGIL-INC-000145

INC-000145 had already moved to FC-000079 during the cross-cutting AI-mediated economic-scam reconciliation.

Tranche 6 performed the scheduled full 0.6.6 review and confirms:

- **FC-000079 remains primary**
- no secondary classifications are added
- FC-000052 remains rejected because the scam objective and tactic are human-directed
- FC-000053 remains rejected because the generating system, request, consent controls and authority state are unknown.

The fact that employees detected the fraud and no transfer occurred does not remove FC-000079: the class expressly includes attempted economic solicitation where AI-mediated false framing materially contributes to the request.

## External-assessment reconciliation

### Existing assessments updated

- `VIGIL-INC-000140 / VIGIL-EXTASSESS-000052` — the British Columbia Civil Resolution Tribunal assessment now explicitly records the FC-000062 boundary and why FC-000016 is not separately asserted.
- `VIGIL-INC-000141 / VIGIL-EXTASSESS-000048` — the NHTSA assessment now records FC-000027 for the mandatory report omission and explicitly separates that reporting mechanism from the vehicle's post-impact movement.
- `VIGIL-INC-000142 / VIGIL-EXTASSESS-000049` — the federal court assessment now records both FC-000062 and FC-000016.

### New broader-cluster assessment

Added `VIGIL-EXTASSESS-000057` to `VIGIL-INC-000145` for the Financial Action Task Force's preserved **Horizon Scan: AI and Deepfakes**.

This is a **broader-cluster research analysis**, not evidence that independently establishes the DNB occurrence. FATF's analysis describes deepfake-enabled executive impersonation and false payment-authority mechanisms relevant to the current FC-000079 boundary.

No structured assessment was added for:

- INC-000135: contemporaneous reporting establishes the occurrence but does not preserve a distinct substantive third-party analytical position suitable for `external_assessments`;
- INC-000139: the AEPD publication records a breach notification that remained under review rather than a concluded regulatory assessment;
- INC-000143: the preserved sources support the occurrence and consequences but do not contain a separately admitted substantive analytical assessment object;
- INC-000144: ordinary reporting and Cruise's attributed explanation are not elevated into a structured assessment.

## Cross-incident consistency

- INC-000140 aligns with the FC-000062 reliance boundary already used for inaccurate generated material that crosses into consequential professional, institutional or public reliance. Unlike INC-000114, the record does not separately establish omission of a required verification step.
- INC-000142 aligns directly with INC-000114: both preserve generated false legal material entering a formal filing and expressly evidenced failure to verify before submission.
- INC-000143 uses FC-000062 rather than FC-000046 because the operative problem is forecast assurance and uncertainty calibration in a reliance-bearing capital workflow, not a prediction being converted into independent authority.
- INC-000141 is intentionally split: FC-000027 covers only degradation of the regulatory reporting artefact. Physical injury and autonomous-vehicle behaviour do not supply the taxonomy mechanism for that mapping.
- INC-000135 and INC-000139 remain consistent with the campaign's malicious-use boundary: beneficial authorised exploitation or hostile agent use does not itself reveal an internal authority failure.
- INC-000145 confirms the economic-scam correction introduced in taxonomy 0.6.6 and does not restore the previously rejected FC-000052/FC-000053 mappings.

## Tranche totals

- Records reviewed: **8**
- Newly classified: **4**
  - `VIGIL-INC-000140`
  - `VIGIL-INC-000141`
  - `VIGIL-INC-000142`
  - `VIGIL-INC-000143`
- Existing classified record retained after scheduled full review: **1** (`VIGIL-INC-000145`)
- Retained unclassified: **3**
  - `VIGIL-INC-000135`
  - `VIGIL-INC-000139`
  - `VIGIL-INC-000144`
- Newly provisionally classified: **0**
- Newly classification-disputed: **0**
- New taxonomy-gap signals: **0**
- Structured external assessments added: **1** (`VIGIL-EXTASSESS-000057`)
- Existing structured external assessments substantively updated: **3**

### Corpus classification counts

| Status | Before Tranche 6 | After Tranche 6 |
| --- | ---: | ---: |
| classified | 90 | **94** |
| provisionally-classified | 2 | **2** |
| unclassified | 49 | **45** |
| classification-disputed | 4 | **4** |
| total active Incidents | 145 | **145** |

## Campaign state

Tranches 1 through 6 of the frozen 52-record campaign have now received their scheduled full review: **48 of 52 frozen records**.

The cross-cutting economic-scam reconciliation performed between Tranches 4 and 5 did not substitute for the scheduled Tranche 6 review of INC-000145; that full review is now complete.

Only Tranche 7 remains outstanding:

`VIGIL-INC-000146`, `VIGIL-INC-000147`, `VIGIL-INC-000148`, `VIGIL-INC-000149`.
