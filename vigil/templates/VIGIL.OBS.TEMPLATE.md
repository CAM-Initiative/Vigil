# VIGIL Observation Record Template

## Record Purpose

An **Observation Record** captures an observed signal, event, report, source item, public development, platform behaviour, system behaviour, jurisdictional development, or early warning input that may be relevant to AI governance, robotics governance, platform governance, UX safety, public legitimacy, or CAM.

An Observation Record is **not automatically a failure mode**.

Use this record type when:

* something relevant has been observed;
* the evidence may be incomplete, emerging, disputed, or provisional;
* the record may later support a Failure Mode record;
* the record may later support a CAM Proposal;
* the record should be preserved as source evidence before its governance meaning is fully known.

Do **not** use an Observation Record to write repair logic, final conclusions, or CAM patch instructions. Those belong in Proposal or Patch Note records.

---

# 1. Record Identity

## VIGIL ID

**Field:** `id`
**Format:** `VIGIL-YYYY-OBS-0000`
**Purpose:** Stable identifier for the observation.

Example:

```text
VIGIL-2026-OBS-0005
```

## Record Type

**Field:** `record_type`
**Value:** `observation`
**Purpose:** Confirms that this record is an observation / early warning signal, not a confirmed failure mode or CAM proposal.

## Legacy Record Type

**Field:** `legacy_record_type`
**Purpose:** Preserves any previous classification used before the schema reset.

Example:

```text
failure-mode-observation
```

Use only where helpful for migration compatibility.

## Status

**Field:** `status`
**Purpose:** Current workflow state of the observation.

Suggested values:

```text
open
watching
triaged
linked-to-failure-mode
routed
closed-no-action
closed-actioned
```

Recommended default:

```text
open
```

## Date Recorded

**Field:** `date_recorded`
**Purpose:** Date the observation was entered into VIGIL.

Format:

```text
YYYY-MM-DD
```

---

# 2. Observation Summary

## Summary

**Field:** `summary`
**Purpose:** Brief factual description of what was observed.

This should answer:

```text
What happened?
Where was it observed?
What system, platform, jurisdiction, source, or behaviour is involved?
```

Do not include repair logic here.

Good example:

```text
A public news report states that agentic AI systems are being used in military targeting workflows, raising early warning questions about human oversight, accountability, and autonomous escalation pathways.
```

Bad example:

```text
CAM should amend Annex K to prohibit this.
```

That belongs in a Proposal.

---

# 3. Why It Matters to CAM

## CAM Relevance Note

**Field:** `why_it_matters_to_CAM`
**Purpose:** Explains why the observation may matter to CAM governance.

This field may describe relevance to:

* governance continuity;
* safety;
* legitimacy;
* rights or interests;
* human oversight;
* identity;
* cognitive integrity;
* platform governance;
* public accountability;
* robotics or embodied systems;
* jurisdictional developments;
* future CAM proposals.

This field should not treat CAM mapping as the public classification. CAM relevance is internal interpretive routing, not the primary external meaning of the observation.

---

# 4. Evidence Confidence

## Evidence Confidence

**Field:** `evidence_confidence`
**Purpose:** Describes the confidence level of the observation.

Suggested values:

```text
verified
corroborated
unverified
anecdotal
disputed
unknown
```

Use conservative values. If the source is public but not independently confirmed, use:

```text
unverified
```

If multiple independent sources support the same observation, use:

```text
corroborated
```

---

# 5. Source Records

## Source Records

**Field:** `source_records`
**Purpose:** Preserves the rich evidentiary source package.

This is one of the most important fields in an Observation Record.

Each source should preserve:

```text
source title
author, reporter, publisher, or account
date published or observed
source URL
archive URL, if any
retrieval date
source type
source platform
system or product involved
model or algorithm, if known
deployment context, if known
source context
source URL status
relevance note
```

The source record should allow an external third party to understand:

```text
Who said it?
Where was it published?
What does the source show?
What system or platform is involved?
Why is this source relevant to the observation?
Can the source still be accessed?
```

Do not flatten this into a single URL field.

---

# 6. Source Data Summary

## Source Data

**Field:** `source_data`
**Purpose:** Provides machine-readable source metadata for filtering, indexing, and external ingestion.

This section should summarise the primary source while preserving the full source package in `source_records` and `source_data.sources`.

Recommended fields:

```text
source type
source URL
source platform
source author or account
date observed
date published
archive status
evidence availability
evidence confidence
reproducibility
primary source URL
primary source platform
primary source author/account
sources array
```

Important rule:

```text
source_data.sources must preserve the same rich source records as source_records.
```

The `sources` array should not be a lossy summary.

---

# 7. System Context

## System Context

**Field:** `system_context`
**Purpose:** Describes the system, platform, product, deployment environment, or interaction context involved in the observation.

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

Suggested system types:

```text
assistant
agentic system
recommender
moderation system
platform
robotics
weapon system
cognitive interface
wearable
infrastructure system
other
```

Suggested interaction modes:

```text
chat
voice
API
platform feed
automated decision
physical
multi-device
human-machine teaming
other
```

Suggested embodiment statuses:

```text
non-embodied
embodied
mixed
unknown
not applicable
```

---

# 8. Jurisdictional Context

## Jurisdictional Context

**Field:** `jurisdictional_context`
**Purpose:** Captures legal, regulatory, geographic, sectoral, or cross-border relevance.

This section should be cautious. Do not overstate jurisdictional relevance.

Useful fields include:

```text
primary jurisdiction
secondary jurisdictions
regulatory surface
sector
cross-border relevance
public interest relevance
```

Examples of regulatory surfaces:

```text
AI safety
consumer protection
platform governance
data protection
privacy
defence
robotics safety
workplace safety
children’s rights
human rights
competition
public administration
medical / health
education
financial services
```

If unclear, use:

```text
unknown
to be assessed
to be confirmed
```

---

# 9. Linked Records

## Linked Records

**Field:** `linked_records`
**Purpose:** Connects the observation to related VIGIL records.

Possible links:

```text
other observations
external references
research
standards
```

Important rules:

```text
Do not create a failure mode link for an observation note. Failures MUST be reported as failures.
```

---

# 10. CAM Internal Routing

## CAM Internal

**Field:** `cam_internal`
**Purpose:** Preserves CAM-specific routing metadata.

This is useful for CAM maintainers but should not be the primary public classification.

Fields may include:

```text
related or similar instruments
related or similar annexes
related or similar domains
governance layer
patch status
validator or automation impact
```

Important rule:

```text
Relevant CAM instruments are internal routing metadata, not the primary public meaning of the observation.
```

Use conservative values where uncertain.

Recommended default patch status:

```text
not routed
```

---

# 11. Next Action

## Next Action

**Field:** `next_action`
**Purpose:** Describes the immediate registry action.

For observations, this should usually be one of:

```text
watch for further corroboration
classify against existing failure modes
create a new failure mode if later confirmed
link to an existing proposal if relevant
monitor jurisdictional developments
archive source evidence
```

Avoid writing CAM repair instructions here.

Good example:

```text
Monitor for corroborating reports and classify against existing failure modes if operational harm, escalation, or governance failure becomes clear.
```

Bad example:

```text
Amend Annex K immediately.
```

---

# 12. Observation Record Rules

An Observation Record must:

```text
preserve source evidence;
remain factual and cautious;
separate observation from interpretation;
avoid premature failure-mode classification;
avoid premature CAM proposal logic;
support external ingestion;
support later linkage to failure modes, proposals, or patch notes;
retain uncertainty where uncertainty exists.
```

An Observation Record must not:

```text
delete or flatten rich source data;
treat CAM affected instruments as the public classification;
invent jurisdictional relevance;
invent harm outcomes;
create a failure mode before the failure is clear;
create a proposal before repair logic exists;
claim certainty where the source does not support it.
```

---

# 13. Minimal Human-Readable Template

## Record

```text
ID:
Record Type:
Status:
Date Recorded:
Title:
Summary:
Why It Matters to CAM:
Evidence Confidence:
Next Action:
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

## Jurisdictional Context

```text
Primary Jurisdiction:
Secondary Jurisdictions:
Regulatory Surface:
Sector:
Cross-Border Relevance:
Public Interest Relevance:
```

## Failure Classification

```text
Linked Failure Mode IDs:
Failure Family:
Harm Vectors:
Severity:
Likelihood:
Confidence:
Affected Rights or Interests:
```

## Linked Records

```text
Related Observations:
Failure Modes:
Proposals:
Patch Notes:
External References:
```

## CAM Internal Routing

```text
Affected Instruments:
Affected Annexes:
Affected Domains:
Governance Layer:
Patch Status:
Validator / Automation Impact:
```
