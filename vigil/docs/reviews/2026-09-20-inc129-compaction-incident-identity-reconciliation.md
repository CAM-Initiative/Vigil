# INC-129 Compaction Incident Identity Reconciliation

**Date:** 2026-09-20  
**Repository:** `CAM-Initiative/Vigil`  
**Branch:** `fix/inc129-compaction-incident-consolidation`

## Problem

Post-publication rereading established that VIGIL had incorrectly converted worked examples from OpenAI's single 18 July 2026 Astra-family compaction-summary incident into separate canonical Incident identities.

OpenAI's report presents one incident and then describes multiple examples from that incident. VIGIL had nevertheless retained:

- `VIGIL-INC-000129` — persona/identity example;
- `VIGIL-INC-000136` — BREACH ALERT example;
- `VIGIL-INC-000137` — medical-research restriction example.

The split confused **taxonomy unit of analysis** with **Incident identity**. Different examples can support different failure or successful-invariant mappings without becoming different Incidents.

## Decision

`VIGIL-INC-000129` is the sole canonical Incident for the OpenAI Astra-family self-generated compaction-summary incident reported for 18 July 2026.

The BREACH ALERT, persona/identity and medical-research material are preserved as structured reported examples inside INC-129.

`VIGIL-INC-000136` and `VIGIL-INC-000137` are removed from the active Incident corpus. They are not renumbered, overwritten or eligible for reuse. Their historical contents remain recoverable through Git history.

## Preserved example-level analysis

| Example | Preserved analysis |
| --- | --- |
| BREACH ALERT | FC-000001 successful-invariant example: successor recognised the summary instruction as untrusted and preserved source-authority separation. |
| Persona / identity | FC-000075 failure-occurrence; FC-000074 and FC-000005 successful-invariant relationships; FC-000076 and FC-000077 ambiguous-boundary relationships; clause-level source analysis retained. |
| Medical research | FC-000036 failure-occurrence and FC-000001 failure-occurrence: restored task state contained invented restrictions and the successor treated them as binding. |

At the canonical Incident level, FC-000001 is recorded once as a failure-occurrence because the medical-research example satisfies the class. The BREACH ALERT FC-000001 success remains an explicitly bounded taxonomy exemplar within the same Incident and must not be interpreted as a whole-Incident success.

## Severity

The existing INC-129 S3 overall severity is retained. The controlling reputation-dignity assessment arises from materialised adverse public framing following disclosure of the incident, while the controlled training examples themselves do not establish external production harm.

## Active-tree treatment

The repair follows the VIGIL maintainer contract:

- no duplicate or retired Incident payloads are retained in the active tree;
- historical split records remain recoverable through Git history;
- active taxonomy references are redirected to INC-129;
- historical review/audit files that accurately described the repository before this repair are not rewritten;
- generated indexes are to be rebuilt from the corrected canonical record set.

## Preventive rule

Maintainer guidance now states explicitly that multiple examples, rollouts or taxonomy outcomes within one provider incident must not receive separate Incident IDs solely because their analytical outcomes differ. Taxonomy granularity is not Incident-identity authority.

## Historical IDs

`VIGIL-INC-000136` and `VIGIL-INC-000137` remain consumed historical identifiers and MUST NOT be reallocated.
