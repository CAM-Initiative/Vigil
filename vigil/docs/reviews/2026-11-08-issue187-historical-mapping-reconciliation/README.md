# Issue #187 — INC-129 six-class correction

**Current status, 8 November 2026:** The canonical working Incident v0.4.0 has **six `ambiguous-boundary` mappings**: FC-075, FC-078, FC-076, FC-077, FC-080 and FC-081. The source-grounded explanation, not a fourth role or new subtype, explains that the preceding governing context is missing and successful holding or failure cannot be established. This is a working-branch correction awaiting validation and publication.

**Root cause:** The 19 October reviewer correctly observed that no operational success or failure had been proven for four class relationships, but incorrectly treated that absence as missing *class engagement*. It removed four materially engaged Boundaries, replacing them with unadmitted conceptual crosswalks.

**Historical evidence:** [18 October six-boundary record](https://github.com/CAM-Initiative/Vigil/blob/d8cf1d85056929eb7748551bec1ec2b40cc6899b/vigil/records/incidents/VIGIL-INC-000129.json); [19 October removal commit](https://github.com/CAM-Initiative/Vigil/commit/81b5e0c2c41289b3f49668856148623ce18797b3); [the historical four explicit removal decisions](https://github.com/CAM-Initiative/Vigil/blob/81b5e0c2c41289b3f49668856148623ce18797b3/vigil/docs/reviews/2026-10-19-boundary-diagnostic/corpus-repair/CHANGE-REGISTER.json).

**Current decision:** See [concise six-class disposition](../2026-11-08-issue187-inc129-six-boundary-decision.json) and [root-cause report](../2026-11-08-issue187-inc129-six-class-reconciliation.md), plus the canonical `classification_basis` / `boundary_adjudication` on each of six mappings. Class exemplars in the four taxonomy family files remain admitted as **ambiguous**, not successfully held.

**Systemic concern:** The same 19 October register removed 25 ambiguous mappings across the corpus (four on this Incident, 21 on others). Those 21 require an evidence-first review under the corrected admission-versus-disposition rule. Some may have been legitimately excluded; no mass restoration has been performed.

The earlier investigation checkpoints and detailed criterion ledgers are preserved in Git history for forensic reproducibility, not as current contradictory instructions. No external governance or Harm Impact findings were changed. Tracker: https://github.com/CAM-Initiative/Vigil/issues/187.
