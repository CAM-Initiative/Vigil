# INC-219–224 — independent external governance requirement review

**Status:** Completed available-source, occurrence-specific EXTREQ candidate review; **none retained** (six separately reasoned outcomes). Prepared 21 November 2026 on `work/inc219-224-external-requirements-20261121` from `main` at `eb5dea093c7c6470f1b671526e7f543779cb87bd`.

This packet **supersedes only the earlier *unperformed external-review status*** documented in the 4–5 November intake checklists. Those older checklists correctly record their historical states and have **not been rewritten**. No prior Incident finding or source evidence was deleted.

## Method and outcome

Followed `vigil/docs/maintenance/EXTERNAL-REQUIREMENT-ADJUDICATION.md`. Independently inspected the six published Incident sources/source episodes, the published requirement index (1,130 rows), the exact shortlisted canonical source/version requirement shards, and the supported FC↔EXTREQ relationships. Each candidate was tested against its actual actor, controlled object, lifecycle and qualifying conditions rather than assuming class similarity or polarity determines external relevance.

The authoritative requirement register is **not** a list of legal duties imposed on these institutions; selected NIST controls are generally voluntary frameworks. The presence of a supported FC↔EXTREQ relationship is necessary but not sufficient for an occurrence result.

| Incident | Existing FC state | External review | Decision |
|---|---|---|---|
| 219 Railway | Unclassified; no canonical AI-actor FC | Reviewed–none retained | Attacker access and AI-assisted fan-outs are reported, but the relevant credential/data actions are not independently assigned to an identified model; do not map provider/defender controls to attacker AI |
| 220 Binance | Unclassified; no canonical AI-actor FC | Reviewed–none retained | Use of an internal AI tool as an attacker pivot is reported, but the model's specific choices, token handling and applicable permissions are undisclosed |
| 221 CRAFTY FALCON | Unclassified; no canonical AI-actor FC | Reviewed–none retained | Four offensive frameworks are named across a campaign; no per-framework, per-victim actor/action joins or eligible FC mapping |
| 222 Accenture–IE | Provisional FC-062, low confidence | Reviewed–none retained | Publication factual/citation errors documented; AI-generated content and applicable GAI-output monitoring or AI TEVV requirement not evidenced |
| 223 ContextEcho | Provisional FC-062, low confidence | Reviewed–none retained | Specific arXiv bibliography mismatch documented; AI generation of the reference and GAI-output monitoring requirement scope not established |
| 224 Authenticity Debt | Provisional FC-062, low confidence | Reviewed–none retained | Original/reference corrections documented; no independently supported AI production or GAI-output/TEVV obligation; reported malicious URL remains an allegation |

The exact per-Incident candidate/requirement/episode tests, exclusions and reopen conditions are in [completion-audit.json](completion-audit.json).

### Technical-security leads

Registered NIST SP 800-53 Rev. 5.2.0 AC-3 (`EXTREQ-FA4D888041BED657`, reviewed against FC-089) and IA-5(g) (`EXTREQ-F42FEC4FD1482D57`, FC-090), and NIST CSF 2.0 PR.AA-05 (`EXTREQ-186266B5896332A7`) / PR.IR-01 (`EXTREQ-9BFEC90D284F0A9C`, FC-002) are inspected **candidate leads**, not published INC-219–221 assessments. The episodes lack a canonical AI-actor mapping, and the control implementer is not necessarily the assessed attacker.

### Citation-reliability leads

Registered NIST AI 600-1 MP-2.3-003 (`EXTREQ-C478F33DE187ACEF`), MS-2.5-003 (`EXTREQ-EAAE2B5FD25DB4E5`) and MP-2.3-001 (`EXTREQ-4D5BF8BEA4A413B0`) have supported FC-062 relationships, but speak about **GAI-generated system outputs**, with monitoring/testing or fact-checking requirements conditional on the stated programme. NIST AI RMF MAP 2.3 (`EXTREQ-4A55F4250F95C5E2`) concerns scientific-integrity and TEVV considerations in AI system risk mapping, not generic journal citation standards. None can be made an occurrence finding from the present publication evidence. **The observed publication mistakes themselves are not contested by this disposition.**

### Evidence holds and provenance

Direct public-source checks included Railway's 10 November technical postmortem, Binance's first-party attack account, CERT-In's public advisory, GPTZero's cited bibliography comparison, and source-register entries for ContextEcho and the mismatched arXiv references. Publisher attribution, restricted forensic evidence and individual model traces were not invented. No material new canonical FC, harm, publication narrative or EXTREQ result was justified by this targeted review.

The six earlier review packets continue to document what was known on their dates. This working packet is temporary; do not cite it as a permanent authority or delete it before an evidence-preserving closeout. Human acceptance, final PR approval and a real reproducible CI run remain separate.

**No PR has been opened or approved by this work.**
