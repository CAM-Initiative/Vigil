# VIGIL Proposal Record Template

## Record Purpose

A **Proposal Record** captures a CAM-specific governance development, repair recommendation, instrument amendment idea, template improvement, registry change, interface update, validator change, automation improvement, doctrinal clarification, or operational design proposal.

A Proposal Record is not a source observation and is not itself a patch note.

Use this record type when:

* CAM governance development is being proposed;
* an observation or failure mode suggests that CAM may need a repair, expansion, or clarification;
* a registry, template, validator, automation, interface, or instrument should be updated;
* a proposal exists even without a specific observation;
* a governance idea needs to be preserved before implementation.

A Proposal may be linked to:

* one or more Observation Records;
* one or more Failure Mode Records;
* research sources;
* standards;
* CAM instruments;
* future Patch Note Records.

Do **not** use a Proposal Record to claim that a patch has already been implemented. That belongs in a Patch Note.

---

# 1. Record Identity

## VIGIL ID

**Field:** `id`
**Format:** `VIGIL-YYYY-PROP-0000`
**Purpose:** Stable identifier for the proposal.

Example:

```text
VIGIL-2026-PROP-0006
```

## Record Type

**Field:** `record_type`
**Value:** `proposal`
**Purpose:** Confirms that this record is a CAM-specific proposal, not an observation, failure mode, or patch note.

## Record State

**Field:** `record_state`
**Purpose:** Light workflow state of the proposal.

Suggested values:

```text
draft
active
under-review
accepted-for-drafting
implemented
superseded
withdrawn
closed-no-action
```

Recommended default:

```text
draft
```

## Date Recorded

**Field:** `date_recorded`
**Purpose:** Date the proposal was entered into VIGIL.

Format:

```text
YYYY-MM-DD
```

---

# 2. Proposal Title

**Field:** `title`
**Purpose:** Concise name for the proposed governance development.

Good example:

```text
Synthetic speaker arbitration requirement for multi-agent voice systems
```

Bad example:

```text
Observed social-platform example in which two OpenAI ChatGPT agents...
```

The title should name the proposed governance repair or development, not retell the source event.

---

# 3. Proposal Summary

**Field:** `summary`
**Purpose:** Brief description of the proposed CAM change.

This should answer:

```text
What is being proposed?
What governance gap, failure, or development need does it address?
What kind of CAM change may be required?
```

The summary may describe repair logic, but should not claim implementation.

---

# 4. Proposal Rationale

**Field:** `proposal_rationale`
**Purpose:** Explains why the proposal is needed.

This field may refer to:

* linked observations;
* linked failure modes;
* research;
* public developments;
* platform behaviour;
* robotics or embodied-system risk;
* jurisdictional developments;
* CAM doctrinal gaps;
* operational or validator needs.

The rationale should distinguish:

```text
evidence
interpretation
CAM-specific development need
```

---

# 5. Proposal Type

**Field:** `proposal_type`
**Purpose:** Classifies the kind of proposal.

Suggested values:

```text
instrument-amendment
new-instrument
template-update
schema-update
validator-update
automation-update
interface-update
registry-update
taxonomy-update
crosswalk-update
doctrinal-clarification
operational-guidance
research-follow-up
other
```

A proposal may include more than one type where necessary.

---

# 6. Proposal Scope

**Field:** `proposal_scope`
**Purpose:** Describes where the proposal may apply.

Suggested fields:

```text
scope_summary
cam_domains
cam_instruments
cam_annexes
registry_components
automation_components
interface_components
external_relevance
```

Use conservative language. A proposal may be relevant to CAM without yet identifying every affected instrument.

---

# 7. Source and Evidence Basis

**Field:** `source_records`
**Purpose:** Preserves the sources, observations, research, or other materials that informed the proposal.

Proposal source records may include:

```text
linked observation record
linked failure mode record
research thread
standard
jurisdictional source
news report
platform artifact
repository issue
governance note
```

Do not flatten rich source context.

If a proposal is purely anticipatory or design-based, source records may be empty, but the proposal should explain this in `proposal_rationale`.

---

# 8. Linked Records

**Field:** `linked_records`
**Purpose:** Connects the proposal to other VIGIL records and external materials.

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

Important rules:

```text
A proposal may exist without an observation.
A proposal may exist without a failure mode.
A proposal must not list itself as a patch note.
A proposal should link to a Patch Note only after implementation exists.
```

---

# 9. CAM Internal Routing

**Field:** `cam_internal`
**Purpose:** Preserves CAM-specific routing metadata.

Fields may include:

```text
target instruments
target annexes
target domains
governance layer
proposal owner
drafting status
validator or automation impact
interface impact
registry impact
```

Because Proposal Records are CAM-specific, this section is central. However, it should still distinguish proposed routing from implemented changes.

Suggested drafting status values:

```text
not started
drafting needed
in drafting
ready for review
accepted
implemented
superseded
withdrawn
```

---

# 10. Implementation Notes

**Field:** `implementation_notes`
**Purpose:** Captures non-binding notes about how the proposal might be implemented.

This may include:

* suggested insertion points;
* template changes;
* schema changes;
* validator changes;
* automation implications;
* interface changes;
* migration concerns;
* dependencies.

Important rule:

```text
Implementation notes are not patch notes.
```

They describe possible implementation, not completed implementation.

---

# 11. External Relevance

**Field:** `external_relevance`
**Purpose:** Describes whether the proposal may be useful beyond CAM.

Suggested fields:

```text
relevant_to_platforms
relevant_to_regulators
relevant_to_robotics
relevant_to_ux
relevant_to_standards
relevant_to_researchers
external_summary
```

This is useful for industry-facing repair notes later, but should not turn the Proposal into a Patch Note.

---

# 12. Next Action

**Field:** `next_action`
**Purpose:** Describes the immediate next step.

Suggested values:

```text
draft CAM clause
review linked evidence
map affected instruments
prepare patch note after implementation
update schema/template
update validator
update interface
hold for further observation
no action currently required
```

---

# 13. Proposal Record Rules

A Proposal Record must:

```text
describe a CAM-specific governance development or repair idea;
preserve its evidence or rationale;
distinguish proposed changes from implemented changes;
link to observations or failure modes where relevant;
support later patch-note generation;
avoid claiming adoption before implementation;
retain uncertainty where uncertainty exists.
```

A Proposal Record must not:

```text
replace an Observation Record;
replace a Failure Mode Record;
claim a patch has occurred;
list itself as a patch note;
invent affected instruments;
flatten source data;
treat external relevance as proof of adoption.
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
Proposal Rationale:
Proposal Type:
Next Action:
```

## Proposal Scope

```text
Scope Summary:
CAM Domains:
CAM Instruments:
CAM Annexes:
Registry Components:
Automation Components:
Interface Components:
External Relevance:
```

## Source / Evidence Basis

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
Target Instruments:
Target Annexes:
Target Domains:
Governance Layer:
Proposal Owner:
Drafting Status:
Validator / Automation Impact:
Interface Impact:
Registry Impact:
```

## Implementation Notes

```text
Suggested Insertion Points:
Template Changes:
Schema Changes:
Validator Changes:
Automation Changes:
Interface Changes:
Migration Concerns:
Dependencies:
```

## External Relevance

```text
Relevant to Platforms:
Relevant to Regulators:
Relevant to Robotics:
Relevant to UX:
Relevant to Standards:
Relevant to Researchers:
External Summary:
```
