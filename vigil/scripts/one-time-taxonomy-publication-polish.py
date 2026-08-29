#!/usr/bin/env python3
"""Apply the approved textbook publication polish to render_taxonomy.py once."""
from pathlib import Path

PATH = Path("vigil/taxonomy/render_taxonomy.py")
text = PATH.read_text(encoding="utf-8")

start = text.index("def case_study_context(example: dict) -> dict[str, str]:")
end = text.index("\ndef publication_class_html", start)
new_case_block = r'''def _case_date(value: object) -> date:
    try:
        return date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return date.min


def _compact_names(values: list[object]) -> str:
    names = [str(value).strip() for value in values if str(value).strip()]
    if not names:
        return ""
    if len(names) <= 3:
        return ", ".join(names)
    return ", ".join(names[:3]) + f" + {len(names) - 3} more"


def case_study_context(example: dict) -> dict[str, object]:
    failure_mode_id = str(example.get("failure_mode_id", ""))
    if not failure_mode_id:
        return {}
    record_path = FAILURE_RECORDS / f"{failure_mode_id}.json"
    if not record_path.exists():
        return {}
    record = load(record_path)
    system_context = record.get("system_context") if isinstance(record.get("system_context"), dict) else {}
    source_records = record.get("source_records")
    if not isinstance(source_records, list):
        source_records = []

    placeholder_vendors = {
        "", "unknown", "unknown vendor", "unknown provider", "other", "not applicable",
        "n/a", "provider unresolved", "provider-unresolved", "system unresolved", "system-unresolved",
        "multi vendor", "multi-vendor",
    }
    summary_provider = str(system_context.get("platform_or_vendor") or "").strip()
    vendors = system_context.get("evidenced_vendors")
    concrete_vendors = vendors if isinstance(vendors, list) else []
    vendor_known = summary_provider.lower() not in placeholder_vendors or bool(concrete_vendors)
    if summary_provider and summary_provider.lower() not in placeholder_vendors:
        provider = summary_provider
    else:
        provider = _compact_names(concrete_vendors)

    summary_product = str(system_context.get("product_or_service") or "").strip()
    product_placeholders = {"", "unknown", "other", "not applicable", "n/a", "multi product", "multi-product"}
    products = system_context.get("evidenced_products_or_services")
    concrete_products = products if isinstance(products, list) else []
    if summary_product and summary_product.lower() not in product_placeholders:
        product = summary_product
    else:
        product = _compact_names(concrete_products)

    evidence_sources = [
        source for source in source_records
        if isinstance(source, dict)
        and source.get("source_date")
        and "evidence" in str(source.get("source_role", "")).lower()
    ]
    dated_sources = [source for source in source_records if isinstance(source, dict) and source.get("source_date")]
    source_pool = evidence_sources or dated_sources
    evidence_source = max(source_pool, key=lambda source: _case_date(source.get("source_date")), default=None)
    source_date = evidence_source.get("source_date") if evidence_source else None

    failure_classification = record.get("failure_classification") if isinstance(record.get("failure_classification"), dict) else {}
    severity = str(failure_classification.get("severity") or "SU").upper()
    return {
        "provider": provider,
        "product": product,
        "date": publication_date(source_date),
        "source_date": str(source_date or ""),
        "severity": severity,
        "vendor_known": vendor_known,
    }


def _severity_rank(value: object) -> int:
    return {"S0": 0, "S1": 1, "S2": 2, "S3": 3, "S4": 4, "SU": 5}.get(str(value).upper(), 6)


def select_family_case_examples(data: dict, case_examples: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """Select at most three publication-grade exemplars for one failure family.

    Eligibility is deliberately stricter than the underlying VIGIL reverse mapping:
    high-confidence taxonomy fit and a known affected vendor are required. Ranking is
    severity first, then newest evidence publication date, with deterministic ID ties.
    """
    candidates: list[dict] = []
    for class_index, item in enumerate(data.get("classes", [])):
        class_id = str(item.get("class_id", ""))
        for example in case_examples.get(class_id, []):
            if str(example.get("classification_confidence", "")).lower() != "high":
                continue
            context = case_study_context(example)
            if not context.get("vendor_known"):
                continue
            candidates.append({
                "class_id": class_id,
                "class_index": class_index,
                "example": example,
                "context": context,
                "role_rank": 0 if str(example.get("classification_role", "primary")).lower() == "primary" else 1,
            })

    # A single FM can map to more than one class. It should occupy only one of the
    # family-wide three Case Study slots; prefer its primary mapping when available.
    best_by_failure: dict[str, dict] = {}
    for candidate in candidates:
        failure_mode_id = str(candidate["example"].get("failure_mode_id", ""))
        previous = best_by_failure.get(failure_mode_id)
        candidate_key = (candidate["role_rank"], candidate["class_index"])
        previous_key = (previous["role_rank"], previous["class_index"]) if previous else None
        if previous is None or candidate_key < previous_key:
            best_by_failure[failure_mode_id] = candidate

    ranked = sorted(
        best_by_failure.values(),
        key=lambda candidate: (
            _severity_rank(candidate["context"].get("severity")),
            -_case_date(candidate["context"].get("source_date")).toordinal(),
            str(candidate["example"].get("failure_mode_id", "")),
        ),
    )[:3]

    selected: dict[str, list[dict]] = {}
    for candidate in ranked:
        selected.setdefault(candidate["class_id"], []).append(candidate["example"])
    return selected


def case_examples_html(examples: list[dict]) -> str:
    if not examples:
        return ""
    studies = []
    for example in examples:
        basis = str(example.get("classification_basis", "")).strip()
        context = case_study_context(example)
        meta = " · ".join(
            esc(value)
            for value in (context.get("provider"), context.get("product"), context.get("date"))
            if value
        )
        studies.append(
            "<article class=\"case-study\">"
            f"<h5>{esc(example.get('title', ''))}</h5>"
            + (f"<p class=\"case-study-meta\">{meta}</p>" if meta else "")
            + (f"<p class=\"case-study-what\"><strong>What happened</strong><br>{esc(basis)}</p>" if basis else "")
            + f"<p class=\"case-study-ref\"><code>{esc(example.get('failure_mode_id', ''))}</code></p>"
            + "</article>"
        )
    return "<section class=\"case-studies\"><h4>Case Studies</h4>" + "".join(studies) + "</section>"

'''
text = text[:start] + new_case_block + text[end:]

old_classes = '''    aliases = " · ".join(f"<code>{esc(x)}</code>" for x in family.get("aliases", [])) or "None recorded"\n    classes = "".join(publication_class_html(item, f"{chapter_number}.{index}", class_lookup, (case_examples or {}).get(item["class_id"], [])) for index, item in enumerate(data["classes"], start=1))\n'''
new_classes = '''    aliases = " · ".join(f"<code>{esc(x)}</code>" for x in family.get("aliases", [])) or "None recorded"\n    selected_case_examples = select_family_case_examples(data, case_examples or {})\n    classes = "".join(publication_class_html(item, f"{chapter_number}.{index}", class_lookup, selected_case_examples.get(item["class_id"], [])) for index, item in enumerate(data["classes"], start=1))\n'''
if old_classes not in text:
    raise SystemExit("publication family class-render block not found")
text = text.replace(old_classes, new_classes, 1)

# Use the dominant emerald/forest green sampled from the canonical CAM footer artwork.
for old_green in ("#0b4a3b", "#073f34", "#063d32"):
    text = text.replace(old_green, "#022c1b")

# Plain-English callouts use the forest-green publication accent, not a gold stripe.
text = text.replace("border-left:2.2pt solid #b8943f", "border-left:3pt solid #022c1b")

# Remove the generated line/circle embellishment from the cover and make descriptor separators typographic.
cover_rule = '    <div class="cover-rule"><span></span></div>\n'
if cover_rule not in text:
    raise SystemExit("cover rule markup not found")
text = text.replace(cover_rule, "", 1)
old_descriptors = '    <p class="cover-descriptors">Failure Families<span class="dot">•</span>Failure Classes<span class="dot">•</span><br>Classification Boundaries<span class="dot">•</span>Recognition Criteria</p>'
new_descriptors = '    <p class="cover-descriptors">Failure Families · Failure Classes<br>Classification Boundaries · Recognition Criteria</p>'
if old_descriptors not in text:
    raise SystemExit("cover descriptor markup not found")
text = text.replace(old_descriptors, new_descriptors, 1)
text = text.replace("background:#022c1b;color:#fff;border-top:1.1mm solid #b8943f;", "background:#022c1b;color:#fff;")
text = text.replace(";border-right:.35pt solid rgba(214,177,84,.75);", ";")

# Reuse the established deterministic Case File use-and-reliance notice on page 2.
old_imprint = '''  <p>This technical reference provides the maintained classification structure for governance failure families and failure classes, including classification boundaries and recognition criteria.</p>\n  <div class="copyright"><strong>Copyright © 2026 Dr Michelle O'Rourke.</strong><div class="website">cam-initiative.org</div></div>'''
new_imprint = '''  <p>This technical reference provides the maintained classification structure for governance failure families and failure classes, including classification boundaries and recognition criteria.</p>\n  <section class="reliance-notice">\n    <h2>Use and reliance notice</h2>\n    <p>This report is provided for research and informational purposes. It does not constitute legal, regulatory, security, assurance, certification, risk, or other professional advice, and should not be relied upon as a substitute for independent assessment. Third parties remain responsible for verifying the cited source material, the current state of the underlying VIGIL Observatory records and taxonomy, the applicability of the analysis to their circumstances, and any decision or action taken in reliance on this report.</p>\n  </section>\n  <div class="copyright"><strong>Copyright © 2026 Dr Michelle O'Rourke.</strong><div class="website">cam-initiative.org</div></div>'''
if old_imprint not in text:
    raise SystemExit("publication imprint insertion point not found")
text = text.replace(old_imprint, new_imprint, 1)

old_copyright_css = '.copyright{margin-top:auto;font-size:9pt;color:#504a40}.copyright strong{color:#022c1b}.website{margin-top:2mm;color:#022c1b}'
new_copyright_css = '.reliance-notice{margin-top:auto;padding-top:6mm;border-top:.6pt solid #d8d5cc}.reliance-notice h2{font-family:Helvetica,Arial,sans-serif;font-size:9pt;font-weight:700;color:#022c1b;margin:0 0 2.5mm}.reliance-notice p{font-size:8.3pt;line-height:1.45;color:#504a40;margin:0}.copyright{margin-top:5mm;font-size:9pt;color:#504a40}.copyright strong{color:#022c1b}.website{margin-top:2mm;color:#022c1b}'
if old_copyright_css not in text:
    raise SystemExit("copyright CSS block not found")
text = text.replace(old_copyright_css, new_copyright_css, 1)

# The old cover-rule and dot CSS can no longer render, but remove it as well so the publication contract is unambiguous.
text = text.replace('.cover-rule{display:flex;align-items:center;gap:4mm;margin:0 0 6mm;width:138mm}.cover-rule:before,.cover-rule:after{content:"";height:.45pt;background:#b8943f;flex:1}.cover-rule span{width:2mm;height:2mm;background:#b8943f;border-radius:50%}\n', '')
text = text.replace('.cover-descriptors .dot{color:#b8943f;padding:0 2.2mm}', '')

PATH.write_text(text, encoding="utf-8")
print("Applied taxonomy publication polish")
