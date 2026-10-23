# Taxonomy v0.8.0 — first five cases, 23 October 2026

**Status:** current-edition source/criterion screen completed for five cases; **no automatic canonical edits, no full-corpus completion claim, no PR merge**.

The governed original decisions, sources, harm assessments and external-requirement interpretations remain intact. `TRANCHE-01-DECISIONS.json` contains exact v0.8.0 literal failure conditions, one-by-one evidence dispositions, success/exclusion reviews, prior packet references, outstanding tests and provenance.

| Incident | Current review outcome | Canonical change now? |
|---|---|---|
| INC-117 | **Existing FC-043 failure retained for bounded validity review.** Hugging Face confirms the guardrails blocked defensive forensic work; Anthropic's *pre-incident* Fable policy expressly lists incident response, log analysis and malware reverse engineering as benign tasks not intended for blocking. A conservative false-positive safety margin creates an important recognition/exclusion question, **not** grounds for an automatic downgrade. | No; retain canonical finding until full evidence-led scope test |
| INC-129 | Disputed FC-075 / FC-078 Boundary remains warranted. No antecedent governing state or reliable downstream validation-use comparator. | No |
| INC-196 | FC-049 instrumentality not demonstrated; self-reported compulsive retries are acknowledged. | No; evidence-limited human-review state retained |
| INC-197 | FC-049 and FC-086 missing actual optimisation or unsupported AI relational-authority claims. | No; evidence-limited human-review state retained |
| INC-198 | FC-049 retention mechanism and FC-087 specific duty/visible response unproved; illness context is not denied. | No; evidence-limited human-review state retained |

**Sources rechecked directly for INC-117:** [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline), [Hugging Face security disclosure](https://huggingface.co/blog/security-incident-july-2026), [Anthropic's Fable 5 cyber safeguard description](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework). The provider's *actual* prompt-by-prompt control decision and exact model variant remain unavailable. **But the pre-incident Fable 5 documentation places log analysis, SOC analysis, incident response and malware reverse engineering in the 'Benign use' category that classifiers are not intended to block.** The same document expressly acknowledges benign requests can be blocked because of a deliberately conservative safety margin. This substantial positive policy/context evidence was underweighted in the original tranche assessment. Anthropic's 6 October expanded CVP access tiers do not prove Hugging Face's July verification/allowlist status; an earlier CVP existed but July membership remains unknown.

INC-129's original OpenAI Alignment source could not be independently retrieved in the current web check. It is still cited as the original primary source through the historical canonical source entry, which carries earlier review and access limitations. No hidden trace was manufactured. The three Grok cases rely on preserved user post captures and their 19 October criterion adjudication packets, not a newly authenticated full model conversation.

## Campaign ledger and next work

This first tranche is **five of 200** reviewed at focused criterion level. INC-117 is a **material validity-scope crosscheck**, not a harmless old version string. The first review's implied need to downgrade the high-confidence finding has been withdrawn: public first-party reports and an applicable published benign-use policy provide affirmative evidence that must be weighed before any change. The rest are evidence-bounded retentions, not endorsements of definitive provider safety.

Open [issue #150](https://github.com/CAM-Initiative/Vigil/issues/150) retains the FC-049 taxonomy-boundary decision for INC-196–198; no new class is approved. FC-087 and episode-traceability follow-ups in issues #153 and #138 were marked closed after the prior evidence-limited reviews. Do not reopen them merely to obtain a preferred mapping.

**Next sequence:** apply the current v0.8.0 FC-043 recognition/exclusion test using available first-party policy and incident evidence, recording remaining private-classifier or allowlist ambiguity in the Incident/review. [Issue #163 was closed as not planned](https://github.com/CAM-Initiative/Vigil/issues/163) because no independently actionable access path exists; its closure does not resolve or overturn this Incident finding. change the canonical disposition **only if** a substantive before/after test warrants it; then apply the same test to the remaining provisional/disputed and older-edition cohorts. The paper must describe any current open classification dispute honestly rather than treating pre-reconciliation `main` as a final freeze.
