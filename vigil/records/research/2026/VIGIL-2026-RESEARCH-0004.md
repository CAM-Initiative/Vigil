---
{
  "id": "VIGIL-2026-RESEARCH-0004",
  "record_type": "research",
  "record_state": "active",
  "date_recorded": "2026-07-30",
  "title": "Expenditure Horizons and Parallel Agentic Optimisation",
  "summary": "Research record preserving METR's expenditure-horizon methodology and the governance significance of scaling agent optimisation through money, inference, experiment compute, asynchronous tools and parallel action.",
  "status": "research record — non-binding",
  "research_method": "Direct synthesis of METR's July 2026 expenditure-horizon paper and companion metrics note, with comparison to trajectory-scale optimisation evidence.",
  "governance_purpose": "Distinguish serial task horizon from budget-scaled and parallel optimisation, and provide an evidence basis for aggregate-pathway controls where many cheap actions can search broadly for a successful route.",
  "evidence_confidence": "corroborated",
  "domains": [
    "AEON",
    "OPERATIONS",
    "SECURITY",
    "ETHICS",
    "ECONOMICS",
    "STEWARDSHIP"
  ],
  "system_context": {
    "platform_or_vendor": "Multi Vendor",
    "product_or_service": "Other"
  },
  "linked_records": {
    "related_observations": [],
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

# VIGIL-2026-RESEARCH-0004 — Expenditure Horizons and Parallel Agentic Optimisation

## Research question

How should VIGIL represent agent capability that grows with expenditure, repeated attempts, parallel experiment execution and asynchronous search even where no single trajectory demonstrates sophisticated long-term planning?

## Method and primary sources

This record directly reviews:

- METR, [Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT](https://metr.org/blog/2026-07-21-expenditure-horizon/), 21 July 2026.
- METR, [Metrics of Agent Ability](https://metr.org/notes/2026-07-24-metrics-of-model-ability/), 24 July 2026.

METR defines expenditure horizon as the common expenditure at which an agent matches or exceeds the improvement achieved by a human with the same budget. The metric uses an agent performance curve rather than one fixed-budget pass/fail result.

## Core findings

### Expenditure is multidimensional

Relevant expenditure can include model inference, experiment compute and human labour. A dollar-denominated curve may make these resources comparable, but the result remains task- and price-dependent.

### Parallel and asynchronous tooling changes the capability surface

In the NanoGPT illustration, METR gave agents four H100 nodes, thirty-two GPUs and asynchronous tools for parallel experiment management. METR reports anecdotal evidence that parallel compute reduced waiting, enabled roughly twice as fast inference-compute spend and appeared to increase the ambition of experiments.

This is not merely faster serial reasoning. It is broader concurrent search over candidate pathways.

### Frontier models may continue improving at higher spend

METR reports that newer models continued making roughly log-linear progress into thousands of dollars of expenditure in the studied setting, while older models more often found few optimisations and plateaued.

The result is specific to a cheap-to-score frontier optimisation problem. It should not be universalised to all AI R&D or all real-world tasks.

### Metric stability has limits

Expenditure horizon may be unstable where human and agent performance curves have similar slopes and may be undefined as a finite crossing point where an agent dominates humans at every measured expenditure. Human-baseline estimation, compute prices, mergeability, verification cost and task selection materially affect interpretation.

## Governance implications

Time horizon alone is insufficient for systems that can:

- launch many cheap attempts;
- explore several routes concurrently;
- bank partial progress across attempts;
- substitute tools or infrastructure when one route fails;
- spend through large token, API or compute budgets;
- use automated feedback to hill-climb;
- aggregate low-signal actions into one consequential trajectory.

Governance should therefore preserve distinct controls for:

1. serial dependency depth;
2. parallel action breadth;
3. total expenditure;
4. action count and cadence;
5. credential, principal and execution-environment transitions;
6. experiment and evaluator feedback frequency;
7. stopping rules and budget exhaustion;
8. cumulative externality and aggregate pathway.

A low per-action cost does not imply low aggregate risk. Thousands of individually low-cost failures may create enough coverage to locate one viable unauthorised route.

## Relationship to the Hugging Face forensic timeline

Hugging Face reconstructed approximately 17,600 actions in the July 2026 intrusion. METR's expenditure-horizon work does not analyse that incident and should not be represented as its causal explanation. It does, however, supply a useful measurement distinction: broad, repeated, machine-speed search can generate material optimisation power without requiring every action to be sophisticated or every path to succeed.

That distinction is directly relevant to VIGIL-2026-PROP-0024's optimiser-level focus on cumulative trajectory, authority lineage, credential transitions and substitute command channels.

## VIGIL disposition

Treat expenditure horizon as a research and measurement construct. It may justify proposal refinement or runtime instrumentation, but it is not itself a failure mode. Failure classification requires evidence that budget-scaled or parallel optimisation crossed an authority, safety, integrity, containment or intervention boundary.
