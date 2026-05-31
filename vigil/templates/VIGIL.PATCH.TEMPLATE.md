# VIGIL Patch Note Record Template

## Record Purpose

A **Patch Note Record** captures an implemented CAM-specific change, repair, update, amendment, registry correction, template update, schema update, validator update, automation update, interface update, crosswalk update, or documentation change.

A Patch Note is not an Observation, Failure Mode, or Proposal.

Use this record type when:

* a CAM-related change has actually been implemented;
* a proposal has been adopted or partially implemented;
* a failure mode has resulted in a concrete repair;
* a registry, schema, template, validator, automation, interface, or instrument has changed;
* maintainers need a public and machine-readable record of what changed and why.

Do **not** use a Patch Note for proposed changes, possible changes, speculative routing, or early warning observations. Those belong in Proposal, Failure Mode, or Observation records.

---

# 1. Record Identity

## VIGIL ID

**Field:** `id`
**Format:** `VIGIL-YYYY-PATCH-0000`
**Purpose:** Stable identifier for the patch note.

Example:

```text
VIGIL-2026-PATCH-0001
```

## Record Type

**Field:** `record_type`
**Value:** `patch_note`

**Field:** `record_state`
**Purpose:** Current state of the patch note.

Suggested values:

```text
implemented
partially-implemented
superseded
reverted
deprecated
```

Recommended default:

```text
implemented
```

## Date Recorded

**Field:** `date_recorded`
**Purpose:** Date the patch note was entered into VIGIL.

## Date Implemented

**Field:** `date_implemented`
**Purpose:** Date the actual change was implemented.

---

# 2. Patch Title

**Field:** `title`
**Purpose:** Concise name for the implemented change.

Good example:

```text
Observation template updated to preserve source evidence without failure-mode classification
```

Bad example:

```text
Maybe we should fix the observation schema
```

Patch notes should describe what changed, not what might change.

---

# 3. Patch Summary

**Field:** `summary`
**Purpose:** Brief description of the implemented change.

This should answer:

```text
What changed?
Where did it change?
Why was the change made?
What record, failure, proposal, or source prompted it?
```

---

# 4. Change Classification

**Field:** `change_classification`
**Purpose:** Describes what kind of patch was implemented.

Suggested patch types:

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
documentation-update
source-data-repair
migration-repair
doctrinal-clarification
operational-guidance
other
```

Suggested change scopes:

```text
minor
moderate
major
structural
emergency
```

Suggested implementation modes:

```text
manual
semi-automated
automated
validator-enforced
interface-only
documentation-only
```

---

# 5. Change Details

**Field:** `change_details`
**Purpose:** Describes the concrete before/after change.

Useful fields:

```text
before_state
after_state
files_changed
records_changed
schemas_changed
templates_changed
scripts_changed
workflows_changed
interface_components_changed
```

This section should be factual. Do not include speculative future work except under `remaining_work`.

---

# 6. Linked Records

**Field:** `linked_records`
**Purpose:** Connects the patch note to records that prompted or explain the change.

Possible links:

```text
related observations
related failure modes
related proposals
related patch notes
external references
research
standards
commits
pull requests
issues
```

Important rules:

```text
A Patch Note may link to one or more Proposals.
A Patch Note may link to one or more Failure Modes.
A Patch Note may link to one or more Observations.
A Patch Note must not claim to implement a Proposal unless the change actually occurred.
```

---

# 7. Source and Evidence Basis

**Field:** `source_records`
**Purpose:** Preserves source material supporting the patch note.

For Patch Notes, source records may include:

```text
linked proposal
linked failure mode
linked observation
GitHub commit
GitHub pull request
issue
workflow run
validator report
migration report
manual maintainer note
external source
```

The source package should make the change auditable.

---

# 8. CAM Internal Routing

**Field:** `cam_internal`
**Purpose:** Identifies the CAM or VIGIL components actually changed.

Fields may include:

```text
changed instruments
changed annexes
changed domains
changed registry components
changed templates
changed schemas
changed validators
changed automations
changed interface components
governance layer
```

Unlike Observation Records, Patch Notes can use “changed” or “affected” language because an actual implementation has occurred.

---

# 9. Implementation Verification

**Field:** `implementation_verification`
**Purpose:** Records how the patch was verified.

Useful fields:

```text
verification_status
validation_commands_run
tests_run
workflow_status
manual_review_status
known_failures
verification_notes
```

Suggested verification statuses:

```text
verified
partially-verified
not-verified
manual-review-only
failed-validation
unknown
```

---

# 10. Impact Summary

**Field:** `impact_summary`
**Purpose:** Explains the effect of the patch.

Useful fields:

```text
public_effect
cam_effect
interface_effect
automation_effect
validator_effect
external_relevance
backward_compatibility
migration_impact
```

This section should be practical and readable.

---

# 11. Remaining Work

**Field:** `remaining_work`
**Purpose:** Captures what is still unresolved after the patch.

Use this field for:

```text
follow-up proposals
known gaps
manual review needed
future automation
interface follow-up
schema follow-up
validator follow-up
records requiring cleanup
```

Do not hide remaining work. Patch Notes are allowed to say “partial repair.”

---

# 12. Patch Note Rules

A Patch Note must:

```text
record an implemented change;
identify what changed;
link to relevant proposals, failures, observations, commits, or sources;
preserve source evidence;
describe verification status;
distinguish completed work from remaining work;
support public accountability and future automation.
```

A Patch Note must not:

```text
describe a merely proposed change;
claim implementation without evidence;
replace a Proposal Record;
replace a Failure Mode Record;
replace an Observation Record;
invent validation results;
hide known unresolved work;
flatten source data.
```

---

# Minimal Human-Readable Template

## Record

```text
ID:
Record Type:
Record State:
Date Recorded:
Date Implemented:
Title:
Summary:
```

## Change Classification

```text
Patch Type:
Change Scope:
Implementation Mode:
```

## Change Details

```text
Before State:
After State:
Files Changed:
Records Changed:
Schemas Changed:
Templates Changed:
Scripts Changed:
Workflows Changed:
Interface Components Changed:
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
Commits:
Pull Requests:
Issues:
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

## CAM Internal Routing

```text
Changed Instruments:
Changed Annexes:
Changed Domains:
Changed Registry Components:
Changed Templates:
Changed Schemas:
Changed Validators:
Changed Automations:
Changed Interface Components:
Governance Layer:
```

## Implementation Verification

```text
Verification Status:
Validation Commands Run:
Tests Run:
Workflow Status:
Manual Review Status:
Known Failures:
Verification Notes:
```

## Impact Summary

```text
Public Effect:
CAM Effect:
Interface Effect:
Automation Effect:
Validator Effect:
External Relevance:
Backward Compatibility:
Migration Impact:
```

## Remaining Work

```text
Follow-Up Proposals:
Known Gaps:
Manual Review Needed:
Future Automation:
Interface Follow-Up:
Schema Follow-Up:
Validator Follow-Up:
Records Requiring Cleanup:
```
