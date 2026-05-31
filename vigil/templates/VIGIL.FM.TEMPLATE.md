# VIGIL Failure Mode Record Template

## Record Purpose

A **Failure Mode Record** captures a confirmed, strongly evidenced, or clearly recurring failure pattern in an AI system, platform system, robotics system, agentic workflow, UX layer, governance process, or public legitimacy layer.

A Failure Mode Record is used when the issue is no longer merely an early warning signal.

Use this record type when:

* a system behaviour has failed in a recognizable way;
* harm, risk, procedural breakdown, safety degradation, or governance instability is evident;
* the same pattern may recur across systems, platforms, contexts, or jurisdictions;
* the record requires triage, mitigation, classification, escalation, or CAM proposal development;
* source evidence should be preserved with the failure diagnosis.

Do **not** use a Failure Mode Record for speculative developments, weak signals, general news, or jurisdictional monitoring where no failure has yet occurred. Those belong in Observation Records.

---

## 1. Record Identity

**Field:** `id`
**Format:** `VIGIL-YYYY-FM-0000`
**Purpose:** Stable identifier for the failure mode.

Example:

```text
VIGIL-2026-FM-0001
```

**Field:** `record_type`
**Value:** `failure_mode`

**Field:** `record_state`
**Purpose:** Light workflow state of the failure mode.

Suggested values:

```text
active
triage-required
under-review
linked-to-proposal
mitigation-identified
closed-superseded
closed-no-action
```

Recommended default:

```text
triage-required
```

---

## 2. Failure Mode Title

**Field:** `title`
**Purpose:** Concise name for the failure pattern.

Good example:

```text
Non-arbitrated multi-agent voice participation
```

Bad example:

```text
Observed social-platform example in which two OpenAI ChatGPT agents operating in Advanced Voice Mode...
```

Titles should be short, reusable, and classification-friendly.

---

## 3. Failure Summary

**Field:** `summary`
**Purpose:** Brief factual description of the failure pattern.

This should answer:

```text
What failed?
What system or context was involved?
What made it a failure rather than only an observation?
```

Do not include full CAM repair logic here.

---

## 4. Failure Mode Definition

**Field:** `failure_mode_definition`
**Purpose:** Defines the reusable failure pattern.

This should be abstract enough to apply beyond one source, but specific enough to distinguish the failure from adjacent patterns.

Example:

```text
A failure mode in which two or more synthetic agents respond to the same human input in a shared interaction space without turn-taking, speaker hierarchy, yielding behaviour, or arbitration protocol.
```

---

## 5. Failure Trigger / Threshold

**Field:** `failure_threshold`
**Purpose:** Explains why the record qualifies as a Failure Mode rather than an Observation.

This is important.

Suggested framing:

```text
This becomes a failure mode when the observed behaviour produces or plausibly produces confusion, contradictory outputs, duplicated guidance, safety degradation, identity ambiguity, consent ambiguity, procedural instability, or operational harm.
```

This field prevents weak signals from being prematurely upgraded.

---

## 6. Evidence Confidence

**Field:** `evidence_confidence`
**Purpose:** Confidence in the evidence supporting the failure mode.

Suggested values:

```text
verified
corroborated
unverified
anecdotal
disputed
unknown
```

A failure mode can still be `unverified` if the observed pattern is clear but the source is not independently corroborated. Use caution.

---

## 7. Source Records

**Field:** `source_records`
**Purpose:** Preserves the rich evidentiary source package.

Each source should preserve:

```text
source title
author, reporter, publisher, or account
date published or observed
source URL
archive URL
retrieval date
source type
source platform
system or product involved
model or algorithm
deployment context
source context
source URL status
relevance note
```

Failure Mode Records must not flatten source evidence into a single URL.

---

## 8. System Context

**Field:** `system_context`
**Purpose:** Describes the system class, platform, product, deployment environment, or interaction context in which the failure occurs.

Useful fields include:

```text
system type
platform or vendor
model, product, or system
interaction mode
embodiment status
deployment context
user role
affected population
```

---

## 9. Failure Classification

**Field:** `failure_classification`
**Purpose:** Describes the failure type, harm vector, severity, likelihood, and affected interests.

This is required for Failure Mode Records.

Suggested fields:

```text
failure family
failure subtype
harm vectors
severity
likelihood
confidence
affected rights or interests
failure scope
recurrence pattern
```

Suggested severity values:

```text
low
moderate
high
critical
to be assessed
```

Suggested likelihood values:

```text
rare
possible
likely
recurring
unknown
to be assessed
```

Suggested failure scope values:

```text
single-instance
recurrent
systemic
cross-platform
jurisdiction-specific
unknown
```

---

## 10. Triage

**Field:** `triage`
**Purpose:** Describes what should happen next.

Suggested fields:

```text
triage_priority
triage_owner
triage_status
mitigation_status
escalation_required
recommended_next_step
```

Suggested triage priorities:

```text
low
medium
high
urgent
to be assessed
```

Suggested triage statuses:

```text
new
needs-review
under-review
proposal-needed
proposal-linked
mitigation-identified
closed
```

---

## 11. Linked Records

**Field:** `linked_records`
**Purpose:** Connects the failure mode to related records.

Possible links:

```text
related observations
related failure modes
related proposals
related patch notes
external references
research
standards
```

Important rule:

```text
A Failure Mode may link back to one or more Observation Records, but it does not require one.
```

If the failure was first captured directly as a failure, no OBS precursor is needed.

---

## 12. Jurisdictional Context

**Field:** `jurisdictional_context`
**Purpose:** Captures legal, regulatory, geographic, sectoral, or cross-border relevance.

Failure Mode Records may have stronger jurisdictional significance than Observation Records, but uncertainty should still be preserved.

Useful fields include:

```text
primary jurisdiction
secondary jurisdictions
regulatory surface
sector
cross-border relevance
public interest relevance
```

---

## 13. CAM Internal Routing

**Field:** `cam_internal`
**Purpose:** Preserves CAM-specific routing metadata.

Unlike Observation Records, Failure Mode Records may identify **affected** CAM areas because the failure is now triage-relevant.

Fields may include:

```text
affected instruments
affected annexes
affected domains
governance layer
proposal_needed
linked_proposals
patch_note_needed
validator_or_automation_impact
```

Important rule:

```text
CAM routing is still internal metadata, but failure modes may justify stronger affected-instrument language than observations.
```

---

## 14. Failure Mode Record Rules

A Failure Mode Record must:

```text
describe a recognizable failure pattern;
preserve source evidence;
explain why the threshold from observation to failure has been crossed;
include triage information;
support linkage to proposals or patch notes;
retain uncertainty where uncertainty exists;
avoid inventing evidence, jurisdiction, severity, or harm.
```

A Failure Mode Record must not:

```text
be used for weak signals only;
flatten source records;
pretend a CAM proposal has been adopted;
treat speculative harm as confirmed harm;
create patch notes before a patch exists;
overwrite uncertainty with certainty.
```

---

# Minimal Human-Readable Template

## Record

```text
ID:
Record Type:
Record State:
Date Recorded:
Title:
Summary:
Failure Mode Definition:
Failure Threshold:
Evidence Confidence:
```

## Source Package

```text
Source Title:
Author / Publisher / Account:
Source Date:
Source URL:
Archive URL:
Retrieved Date:
Source Type:
Source Platform:
System or Product:
Model or Algorithm:
Deployment Context:
Source Context:
Source URL Status:
Relevance Note:
```

## System Context

```text
System Type:
Platform or Vendor:
Model / Product / System:
Interaction Mode:
Embodiment Status:
Deployment Context:
User Role:
Affected Population:
```

## Failure Classification

```text
Failure Family:
Failure Subtype:
Harm Vectors:
Severity:
Likelihood:
Confidence:
Affected Rights or Interests:
Failure Scope:
Recurrence Pattern:
```

## Triage

```text
Triage Priority:
Triage Owner:
Triage Status:
Mitigation Status:
Escalation Required:
Recommended Next Step:
```

## Jurisdictional Context

```text
Primary Jurisdiction:
Secondary Jurisdictions:
Regulatory Surface:
Sector:
Cross-Border Relevance:
Public Interest Relevance:
```

## Linked Records

```text
Related Observations:
Related Failure Modes:
Related Proposals:
Related Patch Notes:
External References:
Research:
Standards:
```

## CAM Internal Routing

```text
Affected Instruments:
Affected Annexes:
Affected Domains:
Governance Layer:
Proposal Needed:
Linked Proposals:
Patch Note Needed:
Validator / Automation Impact:
```

The core difference from OBS is this: **Failure Mode gets `failure_threshold`, `failure_classification`, and `triage`; OBS does not.**
