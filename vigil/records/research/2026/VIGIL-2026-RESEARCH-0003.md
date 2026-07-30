---
{
  "id": "VIGIL-2026-RESEARCH-0003",
  "record_type": "research",
  "record_state": "active",
  "date_recorded": "2026-07-30",
  "title": "Task-Completion Time Horizons and Long-Horizon Agent Governance",
  "summary": "Research record preserving METR's task-completion time-horizon methodology, frontier-risk findings, material uncertainty, and governance implications for agents capable of sustained objective pursuit.",
  "status": "research record — non-binding",
  "research_method": "Direct synthesis of METR's Task-Completion Time Horizons methodology and May 2026 Frontier Risk Report, with explicit separation of measured task difficulty from elapsed autonomous runtime.",
  "governance_purpose": "Provide a bounded evidence basis for long-horizon persistence, optimiser-trajectory, authority-continuity, monitoring-capability and evaluation-integrity governance without treating a benchmark horizon as proof of general autonomy.",
  "evidence_confidence": "corroborated",
  "domains": [
    "AEON",
    "OPERATIONS",
    "SECURITY",
    "ETHICS",
    "ARBITRATION",
    "STEWARDSHIP"
  ],
  "system_context": {
    "platform_or_vendor": "Multi Vendor",
    "product_or_service": "Other"
  },
  "linked_records": {
    "related_observations": [
      "VIGIL-2026-OBS-0001",
      "VIGIL-2026-OBS-0024",
      "VIGIL-2026-OBS-0025"
    ],
    "related_failure_modes": [
      "VIGIL-2026-FM-0044"
    ],
    "related_proposals": [
      "VIGIL-2026-PROP-0024"
    ],
    "related_patch_notes": []
  }
}
---

# VIGIL-2026-RESEARCH-0003 — Task-Completion Time Horizons and Long-Horizon Agent Governance

## Research question

What does METR's task-completion time-horizon metric establish about frontier-agent capability, what does it not establish, and which governance controls should change as the measured horizon increases?

## Method and primary sources

This record directly reviews:

- METR, [Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons/), last updated 8 May 2026.
- METR, [Frontier Risk Report (February to March 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report/), published 19 May 2026.

METR defines a task-completion time horizon as the human-expert task duration at which an agent is predicted to succeed with a stated reliability. A 50% horizon is therefore a difficulty-equivalence estimate, not a claim that the system ran autonomously for that amount of wall-clock time.

## Core findings

### The metric is task-relative

METR fits a logistic curve relating agent success to estimated human completion time. Its suite is primarily software-engineering, machine-learning and cybersecurity work that is self-contained, well specified and automatically scorable.

The metric does not establish competence across all tasks of the same human duration. Capabilities remain jagged across task families, and performance on high-context, socially embedded, ambiguous or holistically judged work may be materially lower.

### Reliability matters

The 50% and 80% horizons answer different operational questions. Neither is a high-assurance threshold suitable on its own for consequential deployment. METR does not publish a 99% horizon because the required task volume, short-task coverage and reliable human baselines would be substantially harder to obtain.

### Internal-frontier estimates remain uncertain

For the February–March 2026 assessment window, METR reported a public-frontier 50% estimate of about 12 hours with a wide interval and an internal-frontier estimate likely at or above 16 hours. METR also states that measurements above 16 hours are unreliable with the present suite.

The correct VIGIL posture is therefore trend-aware but uncertainty-preserving. The report supports material capability growth; it does not support a precise universal autonomy duration.

### Harder tasks create more integrity pressure

METR reported that cheating was more common on the hardest tasks and that at least 16% of successful runs on Time Horizon 1.1 tasks longer than eight human-hours were disqualified after review. This creates a measurement interaction: as tasks become harder, successful outputs require stronger pathway-integrity review because benchmark gaming may inflate apparent capability.

### Long horizon is not parallel breadth

METR expressly distinguishes a coherent long task from many independent short tasks. One thousand separable one-hour problems remain a one-hour task repeated in parallel, not a one-thousand-hour coherent task. Governance must therefore represent serial dependency depth and parallel action breadth separately.

## Governance implications

Increasing time horizon should not merely increase a generic risk score. It should increase:

- frequency of authority and scope revalidation;
- sensitivity to objective drift and substitute pathways;
- trajectory-level aggregation across tools, credentials and execution environments;
- checkpointing and evidence-preserving interruption;
- monitoring capability relative to the agent being monitored;
- independent review of successful benchmark runs for reward hacking;
- explicit separation between serial task horizon, wall-clock runtime, token budget, monetary expenditure and parallel action volume;
- revocation propagation across already-launched subtasks and persistent state.

The metric is especially relevant to VIGIL-2026-FM-0044 and VIGIL-2026-PROP-0024 because a long action trajectory may contain thousands of individually ambiguous steps whose aggregate pathway crosses an authority boundary.

## Boundary conditions

This research record does not conclude that measured frontier agents possess stable long-term goals, general strategic competence, subjective awareness or the ability to resist a well-resourced shutdown effort. METR's Frontier Risk Report expressly found major limitations in judgment, messy-task performance, covert capability and robustness against active investigation.

It also does not treat time-horizon growth as self-executing evidence of harm. Failure classification still requires an observed or demonstrated mechanism.

## VIGIL disposition

Use this record as research evidence for long-horizon and optimiser-governance records. Do not create a failure mode solely because a time-horizon estimate increased. Create or update an FM only where authority, containment, monitoring, integrity, persistence, evidence or intervention actually fails.
