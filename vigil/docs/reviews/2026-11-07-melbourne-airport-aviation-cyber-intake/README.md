# Melbourne Airport / aviation cyber intake screen — 7 November 2026

**Status:** Research-only intake screen. No new canonical Incident allocated; no Fidelity Class or Harm Impact conclusion.

**Branch:** `agent/incident-ecosystem-ingestion`

## Scope and source separation

Three superficially similar aviation stories were screened. They must not be combined as one occurrence or attributed to a single assessed system.

### A. Collins Aerospace MUSE ransomware — 19 September 2025

- **Source authority:** RTX's SEC Form 8-K of 24 September 2025 explicitly confirms ransomware on systems supporting MUSE. The systems operate on customer-specific networks outside RTX's enterprise network. Airlines used backup or manual processes and experienced delays and cancellations. Primary: https://www.sec.gov/Archives/edgar/data/101829/000010182925000036/rtx-20250919.htm
- **Affected geography:** Reliable contemporary reporting identifies European airports (including Heathrow, Brussels and Berlin). It does not establish Melbourne Airport as an affected airport. https://www.abc.net.au/news/2025-09-21/cyber-attack-collins-aerospace-disrupts-europe-airports/105798264 ; https://ia.acs.org.au/article/2025/ransomware-causes-mayhem-at-european-airports.html
- **Investigation:** UK National Crime Agency announced a suspect's arrest and conditional bail on 24 September 2025. No later definitive actor attribution was established in this screen. https://www.nationalcrimeagency.gov.uk/news/uk-arrest-following-aerospace-cyber-incident/
- **Later allegation:** Everest claimed responsibility in October 2025; this is a threat-actor claim, not independently proven attribution. https://australianaviation.com.au/2025/10/russia-linked-group-claims-responsibility-for-european-airport-hack/
- **AI evidence:** No reliable source identified an AI system that performed or materially directed the attack. A contemporary cyber researcher challenged reports of AI-assisted hacking. https://australianaviation.com.au/2025/09/suspect-arrested-in-europe-airport-hack
- **Intake disposition:** Confirmed cyber incident, **not admitted as an AI-system Incident** on available evidence. Do not allocate a VIGIL Incident solely because the targeted supplier also serves defence or aviation organisations. Require source-grounded AI participation. Do not represent manual fallback or airport defenders as AI-agent Aligned mappings.

### B. SITA APP system outage — 2 November 2026

- **Source:** A Melbourne Airport spokesperson described a *worldwide outage* of SITA's Advance Passenger Processing system, with temporary delays at international check-in; operations returned to normal. https://www.brisbanetimes.com.au/national/australia-news-live-qantas-seeks-answers-on-data-breach-storm-prompts-asthma-warning-property-values-fall-further-20261102-p61aft.html
- **Unresolved mechanism:** The available reporting does **not** confirm a cyberattack, ransomware, malicious actor or AI involvement. An outage alone is not evidence of a hack.
- **Intake disposition:** Not admitted. Do not conflate with the 2025 MUSE ransomware incident or the 2026 Amadeus booking-platform breach.

### C. Melbourne Airport AI agents and OneDrive-sensitive-information surfacing — disclosed 4 May 2026

- **Source:** iTnews reports statements by Melbourne Airport head of data analytics Irfan Khan at the Sydney Microsoft AI Tour. The airport integrated agents with SharePoint procedures and incident-report generation. Khan reportedly stated that agents had surfaced sensitive personal information inadvertently shared from OneDrive accounts; the airport reconsidered access permissions. https://www.itnews.com.au/news/melbourne-airport-calls-in-ai-agents-for-incident-response-625534
- **Evidence actually established:** A report of an airport executive's description of AI agents surfacing sensitive content, and subsequent reconsideration of permissions. This is **not** evidence of a malicious external hack or of a verified onward disclosure to unauthorised recipients.
- **Unresolved before canonical admission:** Exact bounded episode/date; participating assessed agent/model/provider; authorised user and access rules; source information classification and whether disclosure crossed a real authority boundary; who received the surfaced information; whether there were multiple distinct occurrences; whether any protective correction was actually implemented and effective; occurrence-level harm.
- **Pre-taxonomy propositions:** (1) agents used airport SOP and report workflows — context for deployment; (2) agents surfaced personal information from OneDrive — reported AI conduct; (3) the information was inadvertently shared in OneDrive — source-permission/context condition; (4) the airport reconsidered permissions — human/institutional response, **context-only**, not a success mapping for the agent.
- **Intake disposition:** **Evidence-limited candidate, not a confirmed hack.** Seek original talk/recording, a direct airport disclosure or technical follow-up before allocating an Incident. If eventually admitted, assess the agent as the originating system, not OneDrive/SharePoint as independent defenders; do not presume FC-089 (Protected Information Access Integrity) or any other mapping before recognition-condition review.

## Repo/duplicate screen

GitHub default-branch code searches for `Melbourne Airport`, `Collins Aerospace` and `OneDrive` found no named canonical Incident; ingestion-branch spot-check of INC-214 through INC-224 revealed no matching entry. This is **not** an exhaustive content scan of every ingestion-branch Incident. Full branch-specific duplicate screening remains required before any allocation.

## Next gate

Do not allocate a new `VIGIL-INC` ID or publish a Case File from this intake screen. Reopen when a source identifies a distinct AI-associated aviation cyber occurrence or materially resolves candidate C's authorised-access boundary. Retain the distinction between human attackers, assessed AI agents, airport operators, suppliers and independent defensive controls. This note is a temporary review packet subject to normal closeout/retention rules.
