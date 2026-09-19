# VIGIL Incident Harm Transmutation Audit — 2026-09-19

## Execution identity

- Branch: `fix/ambiguous-boundary-classification-role`
- Verified starting remote HEAD: `f6fdac35adeb47896fec97990ecc544fb0dcb641`
- Execution date: 2026-09-19
- Methodology: `VIGIL-HIM 1.0.0`
- Canonical scope: all 145 active JSON records under `vigil/records/incidents/`

The review began from each Incident's existing `source_records`, then used bounded external searches where the preserved evidence did not adequately address later public, legal, regulatory, affected-party, security or operational consequences. All eleven VIGIL-HIM dimensions were reconsidered. Overall severity remains the highest supported materialised-harm dimension; dimensions were neither averaged nor accumulated.

Media coverage was treated as evidence, not harm by default. Adverse headlines were used only where they established a reputational or dignitary consequence. Provider disclosure, correction and responsible security reporting were preserved as governance-positive acts and were not treated as admissions of blame.

## Results

| Measure | Result |
| --- | ---: |
| Active Incidents reviewed | 145 |
| Starting S1 records actively revalidated | 20 |
| Starting SU records actively revalidated | 13 |
| Canonical Incident records changed | 13 |
| New external harm-evidence sources added | 6 |
| Existing INC-000129 media sources regularised as harm-evidence | 5 |
| Overall severity changes | 5 |
| Human-review outcomes | 9 |

| Outcome | Count | Meaning |
| --- | ---: | --- |
| A | 128 | Harm assessment confirmed |
| B | 1 | Evidence expanded or regularised; severity unchanged |
| C | 2 | Harm dimension changed; overall severity unchanged |
| D | 5 | Overall severity changed |
| E | 9 | Human review required; evidence remains insufficient for a defensible band |

### Severity transitions

| Previous | Revised | Count | Incidents |
| --- | --- | ---: | --- |
| SU | S3 | 2 | `VIGIL-INC-000061`, `VIGIL-INC-000148` |
| SU | S4 | 1 | `VIGIL-INC-000065` |
| S1 | S3 | 2 | `VIGIL-INC-000131`, `VIGIL-INC-000135` |

The dimensions most often changed were service, operational and infrastructure (2) and privacy and confidentiality (2), followed by psychological wellbeing, reputation and dignity, and financial and economic evidence status (1 each). Eighteen of the twenty starting S1 records remain S1; the exceptions are INC-000131 and INC-000135. Ten of the thirteen starting SU records remain SU; INC-000061, INC-000065 and INC-000148 now have supported materialised-harm bands.

## Source-vocabulary reconciliation

The schema is advanced from `5.5-him-evidence-derived` to `5.6-him-harm-evidence`. `harm-evidence` is now a controlled `source_role` for sources used to establish a materialised consequence or a harm-assessment boundary. The canonical media artefact type remains `news article`; `news report` was not introduced.

The contract expressly separates public framing from technical truth: a source may establish that an organisation was portrayed as dangerous, deceptive or out of control without proving that the underlying system was technically dangerous, deceptive or autonomous. Harm-assessment `evidence_refs` continue to resolve to substantive `source_records`; record cross-references and taxonomy mappings remain ineligible.

## S1 and SU revalidation

Every starting S1 record was checked for positive bounded-occurrence evidence. Controlled simulations and evaluations were retained at S1 only where the evidence affirmatively bounded the occurrence away from external people, systems or deployed services. Records with a directly measured S1 consequence retained their supported dimension. Absence of reporting was not used as the basis for S1.

Every starting SU record was rechecked against existing sources and bounded later evidence. Four records gained a defensible materialised consequence or a more accurate dimension status; the remaining evidence gaps were preserved rather than converted to no harm.

## Human follow-up

The following records retain outcome E. Their sources suggest a possible consequence, but causal attribution, affected population, duration, scale or threshold facts remain insufficient for a defensible band:

| Incident | Unresolved evidence boundary |
| --- | --- |
| `VIGIL-INC-000012` | The source establishes dependence-oriented system language but does not establish resulting user distress, dependency or impairment sufficient to band psychological harm. |
| `VIGIL-INC-000028` | The user report indicates possible retained or contaminated memory context, but the accessible evidence cannot establish scope, persistence or materialised downstream impact. |
| `VIGIL-INC-000033` | The report describes a possible prompt-injection evasion technique, but the originating technical report, sample, affected scanner and operational consequence were not recovered. |
| `VIGIL-INC-000037` | The public URL does not expose enough of the prompt, transformed prompt, refusal or runtime state to band any materialised impact. |
| `VIGIL-INC-000040` | The reporting establishes legal model-access transactions and later suspected-distillation suspensions, but does not establish a materialised societal, democratic or other downstream harm. |
| `VIGIL-INC-000063` | The evidence establishes inaccurate health guidance but no resulting treatment decision, injury or clinical outcome from which to band materialised health harm. |
| `VIGIL-INC-000081` | The observed fare differences and broader surveillance-pricing concerns do not establish a causal pricing input, aggregate overcharge or realised loss that can be banded. |
| `VIGIL-INC-000101` | OpenAI established a globally deployed sycophantic behaviour and rollback, but did not publish a materially harmed cohort or occurrence-level downstream psychological consequence that can be banded. |
| `VIGIL-INC-000139` | Privacy/confidentiality harm is materially implicated by the reported unauthorized modification of personal data and access to invoices, but the public evidence does not disclose the affected-person count, data sensitivity, duration, containment or downstream misuse needed to select a defensible VIGIL-HIM severity threshold. |

INC-000140 remains SU but is assigned outcome C rather than E because the reassessment deterministically changes the financial dimension from `unreported` to `insufficient-evidence`: a C$812.02 award is established, while the conversion source and rate date required for the USD-denominated thresholds are not.

## Worked examples

### INC-000129 — technical containment and public consequence

The bounded training rollout still has no observed behavioural consequence attributable to the inserted persona. Separately, five independently published articles associated the disclosed occurrence with rogue-AI, revolt, megalomania and loss-of-control framing. Those articles evidence the already-adjudicated bounded organisational reputational injury; they are not proof that the model was technically rogue. This pass regularises their role as `harm-evidence` and preserves the existing S3 reputation-and-dignity assessment. OpenAI's disclosure remains a governance-positive act even though disclosure produced a material reputational consequence.

### INC-000135 — responsible security research and confidentiality harm

The researchers acted within an authorised bug-bounty context, stopped, disclosed the vulnerabilities and enabled remediation. Those facts constrain severity and responsibility. They do not erase the realised access to authentication material, affected accounts and a private repository. The privacy-and-confidentiality dimension therefore changes from not-applicable to S3, while no malicious exploitation or model-weight theft is inferred.

### INC-000065 — harm without resolving disputed responsibility

Independent reporting establishes wide-reaching sexualised false depiction, death threats, police protection, a criminal complaint, public demonstrations and national legal-reform pressure. That evidence supports S4 dignitary harm. The record continues to preserve the accused party's denial and does not adjudicate who created or distributed the synthetic images.

## Incident-by-Incident review ledger

| Incident | Previous | Revised | Controlling dimension(s) | Action | Basis |
| --- | --- | --- | --- | :---: | --- |
| `VIGIL-INC-000001` | S3 | S3 | property-asset-damage, service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000002` | S3 | S3 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000003` | S3 | S3 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000004` | S3 | S3 | property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000005` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000006` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000007` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000008` | S4 | S4 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000009` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000010` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000011` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000012` | SU | SU | — | E | The source establishes dependence-oriented system language but does not establish resulting user distress, dependency or impairment sufficient to band psychological harm. |
| `VIGIL-INC-000013` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000014` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000015` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000016` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000017` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000018` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000019` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000020` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000021` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000022` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000023` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000024` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000025` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000026` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000027` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000028` | SU | SU | — | E | The user report indicates possible retained or contaminated memory context, but the accessible evidence cannot establish scope, persistence or materialised downstream impact. |
| `VIGIL-INC-000029` | S5 | S5 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000030` | S5 | S5 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000031` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000032` | S3 | S3 | property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000033` | SU | SU | — | E | The report describes a possible prompt-injection evasion technique, but the originating technical report, sample, affected scanner and operational consequence were not recovered. |
| `VIGIL-INC-000034` | S2 | S2 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000035` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000036` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000037` | SU | SU | — | E | The public URL does not expose enough of the prompt, transformed prompt, refusal or runtime state to band any materialised impact. |
| `VIGIL-INC-000038` | S4 | S4 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000039` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000040` | SU | SU | — | E | The reporting establishes legal model-access transactions and later suspected-distillation suspensions, but does not establish a materialised societal, democratic or other downstream harm. |
| `VIGIL-INC-000041` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000042` | S2 | S2 | reputation-dignity | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000043` | S2 | S2 | psychological-wellbeing, reputation-dignity | C | Affected-party reporting establishes transient acute distress; psychological-wellbeing is now S2 alongside the existing S2 dignitary finding. |
| `VIGIL-INC-000044` | S3 | S3 | psychological-wellbeing, service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000045` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000047` | S4 | S4 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000048` | S4 | S4 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000049` | S3 | S3 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000050` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000051` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000052` | S2 | S2 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000053` | S3 | S3 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000054` | S4 | S4 | reputation-dignity | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000055` | S3 | S3 | property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000056` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000057` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000058` | S2 | S2 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000059` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000060` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000061` | SU | S3 | service-operational-infrastructure | D | Official SASSA evidence establishes material disruption of the eLife certification and social-grant access workflow; suspension attribution remains bounded. |
| `VIGIL-INC-000062` | S4 | S4 | physical-health-safety | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000063` | SU | SU | — | E | The evidence establishes inaccurate health guidance but no resulting treatment decision, injury or clinical outcome from which to band materialised health harm. |
| `VIGIL-INC-000064` | S5 | S5 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000065` | SU | S4 | reputation-dignity | D | Independent reporting establishes severe, wide-reaching dignitary consequences while preserving the accused party's denial and unresolved perpetrator attribution. |
| `VIGIL-INC-000066` | S3 | S3 | reputation-dignity | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000067` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000068` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000069` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000070` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000072` | S3 | S3 | property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000073` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000074` | S3 | S3 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000075` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000076` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000077` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000078` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000079` | S2 | S2 | reputation-dignity, societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000080` | S3 | S3 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000081` | SU | SU | — | E | The observed fare differences and broader surveillance-pricing concerns do not establish a causal pricing input, aggregate overcharge or realised loss that can be banded. |
| `VIGIL-INC-000082` | S3 | S3 | privacy-confidentiality, reputation-dignity | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000083` | S3 | S3 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000084` | S3 | S3 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000085` | S3 | S3 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000086` | S3 | S3 | property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000088` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000089` | S3 | S3 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000090` | S4 | S4 | service-operational-infrastructure, societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000091` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000092` | S2 | S2 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000093` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000094` | S3 | S3 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000095` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000096` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000097` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000098` | S3 | S3 | reputation-dignity, service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000099` | S3 | S3 | societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000100` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000101` | SU | SU | — | E | OpenAI established a globally deployed sycophantic behaviour and rollback, but did not publish a materially harmed cohort or occurrence-level downstream psychological consequence that can be banded. |
| `VIGIL-INC-000102` | S4 | S4 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000103` | S4 | S4 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000104` | S4 | S4 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000105` | S3 | S3 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000106` | S3 | S3 | reputation-dignity, societal-democratic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000107` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000108` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000109` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000110` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000111` | S3 | S3 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000112` | S3 | S3 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000113` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000114` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000115` | S3 | S3 | rights-liberty | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000116` | S4 | S4 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000117` | S3 | S3 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000118` | S4 | S4 | privacy-confidentiality | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000119` | S4 | S4 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000120` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000121` | S2 | S2 | service-operational-infrastructure | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000122` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000123` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000124` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000125` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000126` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000127` | S4 | S4 | privacy-confidentiality, property-asset-damage | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000129` | S3 | S3 | reputation-dignity | B | Five pre-existing media sources are regularised as harm-evidence; the existing S3 reputational assessment and all taxonomy relationships are unchanged. |
| `VIGIL-INC-000130` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000131` | S1 | S3 | privacy-confidentiality | D | The first-party disclosure establishes actual unauthorized use of an exposed API credential; the training context limits but does not erase that materialised misuse. |
| `VIGIL-INC-000132` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000133` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000134` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000135` | S1 | S3 | privacy-confidentiality | D | Actual credential, account and private-repository access is a bounded confidentiality consequence despite authorised research, responsible disclosure and remediation. |
| `VIGIL-INC-000136` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000137` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000138` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000139` | SU | SU | — | E | Privacy/confidentiality harm is materially implicated by the reported unauthorized modification of personal data and access to invoices, but the public evidence does not disclose the affected-person count, data sensitivity, duration, containment or downstream misuse needed to select a defensible VIGIL-HIM severity threshold. |
| `VIGIL-INC-000140` | SU | SU | — | C | The C$812.02 award is now explicit insufficient financial evidence; no USD conversion source and rate date support a band, so SU remains. |
| `VIGIL-INC-000141` | S3 | S3 | physical-health-safety | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000142` | S1 | S1 | financial-economic | A | The existing assessed S1 consequence remains supported and no higher materialised consequence was recovered. |
| `VIGIL-INC-000143` | S3 | S3 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000144` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000145` | S1 | S1 | — | A | Positive bounded-occurrence evidence continues to support no materialised downstream harm; no contrary later consequence was recovered. |
| `VIGIL-INC-000146` | S2 | S2 | financial-economic | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000147` | S2 | S2 | psychological-wellbeing | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |
| `VIGIL-INC-000148` | SU | S3 | service-operational-infrastructure | D | A live pilot across more than 100 restaurants, recurring order failures and termination support material service-workflow disruption with bounded recovery. |
| `VIGIL-INC-000149` | S2 | S2 | reputation-dignity | A | Existing evidence and highest-supported dimension remain defensible; review found no later consequence crossing a higher threshold. |

## Preserved boundaries

- No Failure Taxonomy family, class, mapping position, mapping role, basis or confidence was changed.
- No severity was inferred from taxonomy classification, and no taxonomy classification was inferred from severity.
- Existing direct quotations and evidentiary disputes were preserved.
- No incident, occurrence, evidence, assessment or adjudication date was changed merely because of this review.
- Modified canonical records received the execution date in `record_identity.updated` and one patch-version increment.
- Syndicated or duplicative reporting was not accumulated as separate harm events.

## Generated outputs and validation

Generated Incident projections were rebuilt only after canonical records were complete. `vigil/VIGIL.Incidents.Index.json` changed to reflect the revised severities and source summaries. `vigil/VIGIL.Registry.Index.json` and `vigil/taxonomy/generated/VIGIL.FailureTaxonomy.CaseFileExamples.json` were rebuilt and remained byte-identical because this pass did not change their projected fields. A second rebuild produced identical SHA-256 hashes for all three generated artefacts.

All repository-prescribed checks passed:

- `python vigil/scripts/build-vigil-public-records.py`
- `python vigil/tests/test_build_vigil_records.py` — 6 tests
- `python vigil/tests/test_validate_vigil_record_rules.py` — 20 tests
- `python vigil/tests/test_validate_vigil_records.py` — 7 tests
- `python vigil/tests/test_validate_vigil_public_records.py` — 1 test
- `python vigil/tests/test_vigil_pipeline_state.py`
- `python vigil/tests/test_vigil_source_provenance.py`
- `python vigil/tests/test_registry_source_roles.py` — 6 tests
- `python vigil/tests/test_public_prose_quality.py` — 1 test
- `python vigil/tests/test_authorship_provenance.py` — 5 tests
- `python vigil/scripts/validate-vigil-records.py` — 145 records
- `python vigil/scripts/validate-vigil-public-records.py` — 145 public entries
- `python vigil/scripts/validate-vigil-source-provenance.py` — 258 active sources
- `python vigil/scripts/validate-vigil-interpretive-provenance.py` — 145 records
- `python vigil/scripts/validate-vigil-system-components.py` — 145 records
- `python vigil/scripts/validate-authorship-provenance.py`
- `python vigil/taxonomy/validate_taxonomy.py` — 15 families and 70 classes

Artefact disposition at closure: canonical Incident records and `VIGIL.Schema.json` remain **LIVE**; public indexes remain **GENERATED**; this document is the retained **AUDIT**; no supporting artefact was retired.
