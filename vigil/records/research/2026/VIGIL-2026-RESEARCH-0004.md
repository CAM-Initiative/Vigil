---
{
  "id": "VIGIL-2026-RESEARCH-0004",
  "record_type": "research",
  "record_state": "active",
  "date_recorded": "2026-07-30",
  "title": "Expenditure Horizons, Test-Time Scaling and Parallel Agentic Optimisation",
  "summary": "Research synthesis of METR's expenditure-horizon proposal, NanoGPT experiment, agent-ability metric taxonomy, RE-Bench evidence and related test-time scaling results, with bounded implications for aggregate-pathway governance.",
  "status": "research record — non-binding",
  "publication_status": "published",
  "research_method": "Comparative review of METR's expenditure-horizon experiment and metrics note against RE-Bench, time-horizon methodology, test-time scaling literature and model-system-card reporting. The review separates measured NanoGPT results from broader governance inferences about budget, parallelism and repeated search.",
  "research_scope": "Agent optimisation performance as a function of expenditure; common-unit comparison with human effort; within-trajectory and between-trajectory scaling; parallel experiment execution; repeated attempts; validation and mergeability; implications for cumulative trajectory controls. The record does not estimate economy-wide AI R&D acceleration.",
  "governance_purpose": "Distinguish serial task horizon from budget-scaled and parallel optimisation, and provide an evidence basis for aggregate-pathway controls where many cheap actions or attempts can search broadly for a successful route.",
  "evidence_confidence": "corroborated",
  "corroboration_scope": "The metric definition and NanoGPT result are verified from METR's primary artefacts and triangulated against RE-Bench and independent test-time scaling research. Generalisation beyond the tested optimisation environments remains uncorroborated.",
  "limitations": "The NanoGPT application is one highly instrumented, cheap-to-score optimisation problem; human-effort estimates are uncertain; expenditure depends on prices and included costs; agent contributions require revalidation and mergeability review; and the metric can be unstable or undefined under some curve shapes.",
  "source_corpus": [
    {
      "title": "Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT",
      "publisher": "METR",
      "url": "https://metr.org/blog/2026-07-21-expenditure-horizon/",
      "source_kind": "primary empirical research report",
      "relevance": "Defines expenditure horizon and reports the NanoGPT human and agent scaling curves."
    },
    {
      "title": "Metrics of Agent Ability",
      "publisher": "METR",
      "url": "https://metr.org/notes/2026-07-24-metrics-of-model-ability/",
      "source_kind": "methodological research note",
      "relevance": "Compares fixed-budget, plateau, continuous, expenditure-horizon and human-relative metrics."
    },
    {
      "title": "RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents Against Human Experts",
      "publisher": "METR authors",
      "url": "https://arxiv.org/abs/2411.15114",
      "source_kind": "benchmark paper",
      "relevance": "Supplies human-agent comparisons, best-of-k allocation evidence and longer-budget limitations."
    },
    {
      "title": "Evaluating Frontier AI R&D Capabilities of Language Model Agents Against Human Experts",
      "publisher": "METR",
      "url": "https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/",
      "source_kind": "benchmark release and results report",
      "relevance": "Explains RE-Bench design, cost asymmetry, repeated attempts and real-world validity limits."
    },
    {
      "title": "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling",
      "publisher": "arXiv",
      "url": "https://arxiv.org/abs/2407.21787",
      "source_kind": "test-time scaling research paper",
      "relevance": "Provides independent evidence that coverage can rise with repeated sampling while selection methods may plateau."
    },
    {
      "title": "AI Agents That Matter",
      "publisher": "Transactions on Machine Learning Research",
      "url": "https://arxiv.org/abs/2407.01502",
      "source_kind": "evaluation methodology paper",
      "relevance": "Examines cost, repeat sampling and benchmark practices needed for meaningful agent evaluation."
    },
    {
      "title": "Measuring AI Ability to Complete Long Software Tasks",
      "publisher": "METR authors / NeurIPS 2025",
      "url": "https://arxiv.org/abs/2503.14499",
      "source_kind": "peer-reviewed research paper",
      "relevance": "Provides the contrasting serial task-difficulty metric and its external-validity limits."
    }
  ],
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

# VIGIL-2026-RESEARCH-0004 — Expenditure Horizons, Test-Time Scaling and Parallel Agentic Optimisation

## Abstract

Agent capability is not fixed at one prompt or one trajectory. It changes with inference tokens, number of attempts, experiment compute, wall time, tool access, orchestration and the availability of reliable feedback. METR’s expenditure-horizon proposal makes that scaling visible by comparing the agent’s score-versus-expenditure curve with a human curve in a common unit.

The NanoGPT experiment found that newer agents continued to improve into thousands of dollars of expenditure on a narrow frontier optimisation problem. METR used parallel GPU infrastructure, asynchronous experiment tools and manual revalidation; it also found that only some apparent gains survived review or were considered mergeable. The result is neither proof of automated AI research nor a universal law of agent scaling. It is strong evidence that fixed-budget benchmark scores can hide operational capability and that governance must account for cumulative search power, parallel breadth and repeated attempts.

## Research question

How should VIGIL represent capability that grows with expenditure, repeated sampling, parallel experiment execution and asynchronous search, especially where no single trajectory demonstrates sophisticated long-term planning?

## Scope and methodology

The central source is METR’s [expenditure-horizon report](https://metr.org/blog/2026-07-21-expenditure-horizon/), read together with its [taxonomy of agent-ability metrics](https://metr.org/notes/2026-07-24-metrics-of-model-ability/). The review compares those claims with [RE-Bench’s human-agent results](https://arxiv.org/abs/2411.15114), the task-completion time-horizon programme and independent work on repeated-sampling and cost-aware evaluation.

Five dimensions were separated:

1. the formal definition of expenditure horizon;
2. the empirical setup and result in NanoGPT;
3. parallelism, repeated attempts and feedback as capability multipliers;
4. validation, mergeability and contamination as constraints on the score; and
5. the governance inference from measured optimisation to real agent trajectories.

The Hugging Face forensic timeline is used only as an external application example for aggregate action count. METR did not analyse that incident through expenditure horizon, and this record does not claim that the metric causally explains it.

## Findings

### 1. Expenditure horizon measures a curve, not a one-shot score

METR defines expenditure horizon as the common expenditure at which the improvement achieved by an agent equals or exceeds the improvement a human achieves with the same budget. In formal terms, it considers the range over which the agent performance curve remains above the human curve.

This differs from a fixed-budget benchmark. A model may look weak at one spend but continue improving as additional attempts or experiments are supplied. Another may perform strongly at low cost and then plateau. Reporting only the score at an arbitrary token cap can reverse or conceal those differences.

The metric also differs from task-completion time horizon. Time horizon maps pass/fail performance across tasks to the human time associated with task difficulty. Expenditure horizon maps performance on an optimisation problem across budgets. One asks, “How difficult a task can the agent complete at the chosen reliability?” The other asks, “For how much common expenditure does the agent match the human return curve?”

METR’s broader metrics note shows there is no universally correct scalar. Fixed-expenditure score, practical plateau, expenditure at a fixed score, marginal returns, human-relative savings and expenditure horizon answer different questions. Governance should preserve the underlying curve and measurement conditions rather than retain only one headline number.

### 2. Expenditure is multidimensional and partly constructed

In the NanoGPT application, agent expenditure included model API calls and experimental GPU compute. Human expenditure was estimated from contributor effort and converted to dollars using an assumed wage. Those conversions make comparison possible, but they embed judgments about prices, labour value and which costs count.

The ideal budget would include inference, experiment compute, human review, failed runs, verification, orchestration, data acquisition and external services. In practice, some of these costs are omitted or priced imperfectly. Changing API prices can move a dollar-denominated horizon even when technical capability is unchanged.

Human effort is especially difficult to recover from historical optimisation. METR found its automated or documentary estimate understated contributor-reported effort and applied a correction factor with a wide confidence interval. It also had to distinguish local work on NanoGPT from upstream research or known techniques imported into the speedrun.

The metric therefore supports comparative reasoning only when the cost boundary is disclosed. A provider must not describe “agent expenditure” as total cost if expensive human validation or experimental infrastructure is excluded.

### 3. The NanoGPT experiment demonstrates budget-scaled search

METR started agents from a historical NanoGPT speedrun state and supplied access to four H100 nodes—thirty-two GPUs in total—with asynchronous tools for running and managing experiments in parallel. It studied single evaluation runs over five days and up to USD 10,000 in combined inference and experiment expenditure.

Parallelism reduced idle time and increased the rate at which inference budget could be spent. METR also reported an anecdotal increase in the ambition of experiments when models could launch asynchronous compute. The harness permitted repeated scoring of intermediate solutions, while promising results were confirmed with additional runs and manually revalidated.

Older models found few improvements and plateaued. Newer models continued roughly log-linear progress into thousands of dollars. METR estimated NanoGPT expenditure horizons up to the low thousands under its central human-cost assumption, with much larger or smaller values under alternative assumptions.

The operational point is not the exact dollar value. It is that the shape of the agent curve changed across model generations, and capability remained responsive to additional budget after a fixed low-cost evaluation would have stopped.

### 4. Apparent optimisation is not the same as durable contribution

METR re-ran claimed improvements many times because NanoGPT scores are noisy. Some apparent gains did not survive statistical revalidation. Others were real against the specific target but brittle, curve-fit or not acceptable to the project maintainer. Only a subset mapped to contributions judged genuinely useful or mergeable.

This distinction is indispensable for AI R&D governance. A benchmark optimiser may exploit the exact loss target, timing environment or scoring rule without producing a robust improvement to the underlying system. “Score increased” is not equivalent to “research progress occurred.”

Contamination creates another problem. If the model has encountered later NanoGPT solutions, an apparent discovery may be retrieval rather than independent optimisation. METR selected a historical start point, discussed contamination in alternate runs and used maintainer review, but no public benchmark can guarantee absence of all relevant training exposure.

High expenditure can also magnify evaluator exploitation. More attempts provide more opportunities to find a scoring artefact. Pathway review and held-out verification must therefore scale with the search budget.

### 5. Repeated attempts create breadth even without one long plan

RE-Bench found that agents often benefited from dividing a total compute budget into many shorter attempts and selecting the best result, whereas humans benefited more from longer coherent attempts. Independent repeated-sampling research similarly finds that coverage—the chance at least one sample solves a problem—can continue rising with the number of samples, although methods for choosing the correct sample may plateau when verification is weak.

This is a different capability from serial long-horizon work. One agent may pursue a dependent sequence where each step relies on earlier state. Another system may launch hundreds of independent attempts and retain the first success. Both can produce consequential results, but the correct controls differ.

Serial depth raises memory, drift, revocation and checkpointing concerns. Parallel breadth raises rate limits, budget caps, shared-resource contention, cross-attempt aggregation and verifier integrity concerns. A system that mixes them requires both control sets.

### 6. Cheap actions can form a high-power optimiser

A low per-action cost does not imply low aggregate capability. If an agent can cheaply generate, test and discard pathways, it may discover a rare route that a human would not search exhaustively. Automatic feedback makes this hill-climbing especially powerful because the system does not need a complete plan in advance.

That observation is relevant to VIGIL-2026-PROP-0024. Per-action policy checks can approve thousands of locally plausible steps while missing that the aggregate trajectory is repeatedly searching for a route around an authority boundary. Governance needs cumulative state: what objective is being optimised, which pathways have failed, which credentials or principals were tried, and whether the agent is substituting command channels or environments.

## Counter-evidence and alternative explanations

The NanoGPT results also constrain alarmist interpretations.

The agents’ measured contribution was small relative to the cumulative human work embedded in the speedrun. METR concluded that autonomous agent optimisation had so far made only a limited contribution in this setting. The newest agents’ final scores remained behind the later state of the human project.

NanoGPT has a cheap, objective feedback loop. Many real research problems have ambiguous objectives, expensive experiments, long delays, negative results that are hard to interpret and discoveries that cannot be merged mechanically. Scaling may be much weaker there.

Parallel compute may primarily increase throughput rather than reasoning sophistication. A system that runs more experiments can find a better answer without having a more coherent model of the problem. That still matters operationally, but it should not be narrated as equivalent to deeper planning.

Repeated sampling only helps when a verifier can recognise success. In domains without automatic verification, majority voting and reward models can plateau or select persuasive errors. More samples can then amplify cost and false confidence rather than capability.

Finally, expenditure horizon can become undefined if the agent dominates the human curve at every measured budget, and unstable when the two curves have similar slopes. A single scalar should not replace the full curves.

## Limitations

The principal empirical application is one optimisation ecosystem. It cannot establish a general expenditure horizon for “AI research,” cybersecurity, governance work or open-ended institutional tasks.

Human-effort reconstruction and wage conversion are uncertain. Agent prices will change. The experiment’s harness, prompting, token limit and parallel tools are part of the evaluated system, so results do not attach to the base model alone.

The reported progress curves depend on intermediate scoring and revalidation. A less legible environment would produce a different curve. Mergeability judgments include human project values that are not captured by raw benchmark score.

This review did not reproduce METR’s experiment or inspect private run transcripts. It relies on the published methods, figures and disclosed review process.

## Governance implications

Agent governance should record at least:

- total monetary, token, compute and wall-time budgets;
- maximum and observed concurrent attempts;
- within-trajectory versus between-trajectory scaling;
- experiment and evaluator feedback frequency;
- verifier identity, independence and false-acceptance risk;
- banked intermediate artefacts and cross-attempt state;
- credential, principal and environment transitions;
- stopping rules, escalation thresholds and budget-exhaustion behaviour;
- validation cost and human review omitted from headline expenditure; and
- cumulative externality, not only per-action risk.

Budget increases should trigger proportionate reauthorisation. A user approving one experiment should not silently authorise thousands of variants, use of additional principals or external acquisition of compute. Revocation must stop queued and parallel work, not merely the visible parent process.

For evaluation reporting, publish scaling curves where practical. If only a fixed-budget score is published, disclose the budget and evidence that the model was near a practical plateau. Preserve negative results, not only the best run.

The Hugging Face incident’s approximately 17,600 actions illustrate why action volume can matter, but this record does not attribute that event to METR’s metric. The legitimate connection is conceptual: broad, machine-speed search can create material optimisation power without every action being sophisticated and without every path succeeding.

## Open questions

- Which real AI R&D tasks have sufficiently reliable score functions for expenditure-horizon measurement?
- How should human review, verification and rework be priced into agent expenditure?
- How does capability scale when experiments are slow, ambiguous or irreversible?
- When does parallel breadth substitute for serial depth, and when are both required?
- How can evaluation distinguish independent discovery from contamination or retrieval?
- Which controls prevent an agent from acquiring additional compute when the authorised budget is exhausted?
- How should rate limits aggregate across accounts, principals, vendors and subagents?
- What metric remains useful after agents dominate the human curve?

## Bibliography and Primary Sources

1. Cunningham, T., Shetty, M., Cheng, V., and Rush, N. “Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT.” METR, 21 July 2026. https://metr.org/blog/2026-07-21-expenditure-horizon/
2. Cunningham, T. “Metrics of Agent Ability.” METR, 24 July 2026. https://metr.org/notes/2026-07-24-metrics-of-model-ability/
3. Wijk, H., et al. “RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents Against Human Experts.” https://arxiv.org/abs/2411.15114
4. METR. “Evaluating Frontier AI R&D Capabilities of Language Model Agents Against Human Experts.” 22 November 2024. https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/
5. Brown, B., et al. “Large Language Monkeys: Scaling Inference Compute with Repeated Sampling.” 2024. https://arxiv.org/abs/2407.21787
6. Kapoor, S., et al. “AI Agents That Matter.” *Transactions on Machine Learning Research*, 2025. https://arxiv.org/abs/2407.01502
7. Kwa, T., West, B., et al. “Measuring AI Ability to Complete Long Software Tasks.” *NeurIPS 2025*. https://arxiv.org/abs/2503.14499
