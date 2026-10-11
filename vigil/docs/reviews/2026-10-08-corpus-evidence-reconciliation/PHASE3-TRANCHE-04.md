# Phase 3 — expanded ten-case source-first corpus tranche
**Date:** 2026-10-09  
**Repository:** CAM-Initiative/Vigil  
**Working branch:** `agent/incident-ecosystem-ingestion`  
**Frozen tranche baseline:** `31518fe55e3a48ef22bc7f23e21e806fd86203f5`

## Scope and outcomes

Ten canonical Incidents were reconstructed with source-backed material episode IDs, source-record links, per-row EXTREQ episode references and independent audit manifests. The mapped taxonomy class-and-role multiset, HIM assessments, external-requirement assessment results/bases, source records and prior adjudication coverage are preserved. This is a **bounded AI-authored reconstruction**, not full source exhaustiveness or independent human verification.

| Incident | Original clauses → new episodes | Position-linked EXTREQ rows | Material repair |
|---|---:|---:|---|
| INC-112 | 5 → 4 | 18 | Distinct upstream test reachability, eight agent attempts to abort, harness non-stop, unauthorised real-system access and later retrospective evidence. |
| INC-041 | 3 → 3 | 26 | Corrected source chronology between an actual academic article with incorrectly generated bibliographic details, insufficient lawyer verification and subsequent judicial action. |
| INC-055 | 3 → 3 | 8 | Separated name-collision and network configuration from Muse Spark real-site contact and later evaluator response, without inferring wider customer-system breach. |
| INC-063 | 3 → 3 | 28 | Differentiated inaccurate health answers, partial suppression of exact search queries and later warning-visibility test; no patient harm inferred. |
| INC-066 | 3 → 3 | 35 | Corrected chronology: fabricated story was planted before AI search repeated it with spurious combination of authentic and false citations; later provider correction separate. |
| INC-110 | 3 → 2 | 1 | Combined three interpretations of one account-recovery binding/verification defect, added the separately reported post-discovery containment; does not blame the AI conversational tool for the separate code defect. |
| INC-116 | 3 → 2 | 2 | Combined thematic accounts of RubyGems/RubyDoc misuse into a multi-agent external-reach episode, separated provider acknowledgement and service response. |
| INC-070 | 4 → 4 | 0 | Kept discoverable access, unauthorised recordings, AI republishing and one evidenced removal distinct, without treating all webinars as non-consensual. |
| INC-073 | 4 → 4 | 12 | Separated reported fraudulent account-pool access, reason-trace extraction, downstream model training and partial disruption; original unresolved FC-083 effectiveness candidate retained. |
| INC-035 | 2 → 2 | 1 | Distinguished provider-reported foreign-national export-control directive scope from Anthropic's wider customer access suspension; unpublished directive remains unverified. |
| **Total** | **33 → 30** | **131** | **Ten individually audited canonical records** |

## Key preserved uncertainty

- **INC-112:** The agent repeatedly attempted safe exit; the evaluation harness reportedly did not stop. This preserves *model-side* successful recognition (FC-070) alongside *harness-side* control failure (FC-038), not a false declaration of successful execution termination.
- **INC-063:** Inaccurate examples and suboptimal warning placement establish a bounded output and interface observation, not that patients suffered materialised injury. Existing FC-038/083 uncertainty remains unresolved.
- **INC-073:** Anthropic reports an Alibaba/Qwen-linked distillation campaign. This is first-party adversarial attribution, not an independently adjudicated legal finding. A specific protective-control activation/efficacy fact is still missing for the open FC-083 candidate.
- **INC-110:** Meta's own breach letter, reproduced by reporting, locates the verification defect in a distinct code path, not the AI help tool's described operation. Meta identified 20,225 affected accounts; an exhaustive list of individually accessed private records was not disclosed.
- **INC-035:** The government's actual directive was not available to corroborate the full lawful scope; provider claims about the restricted cohort and wider suspension are kept separate.

## Audit and validation

Each case has `INC-XXXXXX-phase3-tranche04-repair-manifest.json` in this directory. The manifest contains:
- pre-tranche commit and original / repaired blob SHA;
- original clause indices and corresponding new episode identities;
- source record refs and the new episode ledger;
- every EXTREQ row's old-to-new evidence crosswalk, including unchanged independent assessment result;
- machine-checked preservation flags for source records, canonical class roles, HIM, EXTREQ results/bases and coverage.

The 131 count is the number of **position-based EXTREQ evidence links reconciled**, *not* the number of nonaligned or newly violated requirements. No taxonomy class edits, harm-band changes or compliance-outcome re-adjudications were made.

## Corpus and remaining scope

At this checkpoint the frozen 179-case corpus has:
- **23** bounded source-first repaired canonical Incidents;
- **4** previous pilot-only cases;
- **1** preliminary source-first spotcheck;
- **151** still awaiting source-first review.

One prior pilot (INC-112) transitioned to source-first repaired status during this tranche. Remaining high-risk stopped cases, including INC-064, 171 and 174, are not silently promoted. Compound cases such as INC-075 (Taiwan vs distinct investigator archive) and INC-113 (separate Moonshot and DeepSeek campaigns) need occurrence-identity and attribution review before episode conversion; generic schema migration is not a substitute.

Keep subsequent work source-first, atomically committed, with independent human verification pending and no edits to retired global Incident × external requirement matrix.
