#!/usr/bin/env python3
"""One-shot migration helper for FM affected-system/source-platform separation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "vigil" / "VIGIL.Schema.json"
INDEX_SCHEMA = ROOT / "vigil" / "schemas" / "VIGIL.Index.Schema.json"
TEMPLATE_JSON = ROOT / "vigil" / "templates" / "failure-mode-record-template.json"
TEMPLATE_MD = ROOT / "vigil" / "templates" / "failure-mode-record-template.md"
EVIDENCE_GUIDANCE = ROOT / "vigil" / "docs" / "evidence-authoring-guidance.md"
BUILDER = ROOT / "vigil" / "scripts" / "build-vigil-records.py"
BUILDER_TEST = ROOT / "vigil" / "tests" / "test_build_vigil_records.py"


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"{path}: expected JSON object")
    return value


def dump_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}")
    return text.replace(old, new, 1)


def update_schema() -> None:
    schema = load_json(SCHEMA)
    rules = schema["system_context_rules"]["failure_mode_evidence_projection"]
    rules["source_fields"] = [
        "source_records[].system_or_product",
        "source_records[].model_or_algorithm",
    ]
    rules["record_context_fallback_fields"] = [
        "system_context.platform_or_vendor",
        "system_context.product_or_service",
        "system_context.specific_model_or_runtime",
        "system_context.model_or_product",
    ]
    rules["source_platform_rule"] = (
        "source_records[].source_platform identifies where evidence is hosted, published, or observed. "
        "It is source provenance and must not be treated as affected provider/product identity unless "
        "the affected-system fields independently establish the same system."
    )
    rules["traceability_rule"] = (
        "Each evidenced_systems entry preserves its projection_basis and the supporting source title; "
        "source_platform may be retained separately as evidence_source_platform so evidence host and "
        "affected system remain distinguishable."
    )
    rules["compatibility_rule"] = (
        "platform_or_vendor, product_or_service, and specific_model_or_runtime remain compatibility "
        "summary fields. Multi Vendor describes scope only and must not substitute for concrete "
        "evidenced_vendors, evidenced_products_or_services, or evidenced_models_or_runtimes arrays."
    )
    rules["no_narrative_inference_rule"] = (
        "Provider, product, model, and runtime identities must not be synthesized from narrative "
        "source_context, relevance_note, article titles, publisher prose, or the evidence-host "
        "source_platform field. Older records may use a concrete pre-existing FM system_context as a "
        "bounded fallback where source-level affected-system fields were not yet populated."
    )
    dump_json(SCHEMA, schema)


def update_index_schema() -> None:
    schema = load_json(INDEX_SCHEMA)
    props = schema["$defs"]["record_entry"]["properties"]
    props["evidence_scope"] = {"type": "string"}
    props["evidenced_vendors"] = {"$ref": "#/$defs/string_array"}
    props["evidenced_products_or_services"] = {"$ref": "#/$defs/string_array"}
    props["evidenced_models_or_runtimes"] = {"$ref": "#/$defs/string_array"}
    dump_json(INDEX_SCHEMA, schema)


def update_template_json() -> None:
    template = load_json(TEMPLATE_JSON)
    projection = template["system_context"]["evidence_projection"]
    projection["basis"] = "record-local affected-system metadata"
    projection["method"] = "structured source affected-system roll-up with record system-context fallback"
    projection["inference_boundary"] = (
        "Project affected provider, product, model, and runtime identity from structured system_or_product "
        "and model_or_algorithm source metadata. source_platform identifies the evidence host/publication "
        "surface and is not affected-system identity. Older records may use an existing concrete FM "
        "system_context as a bounded fallback. Do not infer system identity from narrative prose."
    )
    dump_json(TEMPLATE_JSON, template)


def update_template_md() -> None:
    text = TEMPLATE_MD.read_text(encoding="utf-8")
    start = text.index("## Evidence-backed system context")
    end = text.index("## Severity and triage model 2.0")
    section = '''## Evidence-backed system context

`system_context` separates **failure scope**, **affected-system identity**, and **evidence-source provenance**.

`source_records[].source_platform` identifies where evidence is hosted, published, or observed. It may therefore be `TikTok`, `Reddit`, `GitHub`, a news publisher, a status page, or another evidence surface. **Do not treat `source_platform` as the affected AI/platform vendor.**

Use these source-level fields for affected-system identity where the evidence package supports them:

* `system_or_product` — affected system, product, service, platform surface, or tool;
* `model_or_algorithm` — affected model, runtime, algorithm, or model family where established.

Failure-mode records maintain the normalized projection:

* `evidence_scope` — `single-provider`, `multi-provider`, `provider-unresolved`, `system-unresolved`, or `not-applicable`;
* `evidenced_vendors` — concrete affected providers/vendors established by structured metadata;
* `evidenced_products_or_services` — concrete affected products/services;
* `evidenced_models_or_runtimes` — concrete model/runtime names;
* `evidenced_systems` — traceable per-evidence system projections including `projection_basis`; and
* `evidence_projection` — derivation basis, method, reconciliation date, and inference boundary.

For older records created before `system_or_product` and `model_or_algorithm` were populated consistently, a **concrete pre-existing FM `system_context`** may be used as a bounded compatibility fallback. This fallback must remain linked to actual evidence records and must not be used to manufacture additional vendors or models.

`platform_or_vendor: "Multi Vendor"` is a scope summary only. It is valid when the normalized evidence supports more than one affected provider, but public interfaces should display the concrete `evidenced_vendors`, products, and models/runtimes rather than presenting `Multi Vendor`, `Other`, or `Unknown` as if those were system identities.

Do **not** mine narrative `source_context`, `relevance_note`, article titles, publisher prose, or social-media captions to manufacture affected-system identity. If structured metadata and the existing concrete FM context are insufficient, preserve `provider-unresolved` or `system-unresolved` and repair the evidence metadata separately.

'''
    TEMPLATE_MD.write_text(text[:start] + section + text[end:], encoding="utf-8")


def update_evidence_guidance() -> None:
    text = EVIDENCE_GUIDANCE.read_text(encoding="utf-8")
    marker = "* `source_platform`\n* `deployment_context`"
    replacement = "* `source_platform`\n* `deployment_context`"
    if marker not in text:
        raise RuntimeError("evidence guidance required-source marker not found")
    boundary = '''
### Evidence source platform versus affected system

`source_platform` is **source provenance**: it identifies the platform, publication surface, repository, status page, social network, or other location through which the evidence is supplied. It does not, by itself, identify the AI/platform system affected by the failure. A TikTok video about ChatGPT therefore has `source_platform: "TikTok"` while the affected system remains OpenAI / ChatGPT.

Where an external source identifies an affected system, populate these structured fields as well:

* `system_or_product` — the affected platform, product, service, tool, or system stated by the evidence;
* `model_or_algorithm` — the affected model, runtime, algorithm, or model family where established.

Do not infer either field from the publisher or hosting platform. Where the evidence does not establish a model, use the existing bounded uncertainty convention rather than guessing.

'''
    insert_after = "Use `source_records` as the canonical evidence block. Do not add `source_data`, `source_data.sources`, or flattened one-off URL fields to individual records.\n\n"
    if "### Evidence source platform versus affected system" not in text:
        text = replace_once(text, insert_after, insert_after + boundary, "evidence boundary insertion")
    old_multi = '''Keep `product_or_service` to one canonical value. For genuinely multi-vendor and multi-product records, use `product_or_service: "Other"` unless one canonical product clearly controls the record. Put specific product, model, surface, and incident claims in descriptive fields and source-level metadata.
'''
    new_multi = '''Keep `product_or_service` to one canonical compatibility value. For genuinely multi-vendor and multi-product records, use `product_or_service: "Other"` unless one canonical product clearly controls the record. Record the actual affected vendors/products/models in `system_or_product`, `model_or_algorithm`, and the FM evidence-backed system projection; do not use `source_platform` as a substitute.
'''
    text = replace_once(text, old_multi, new_multi, "multi-vendor guidance")
    EVIDENCE_GUIDANCE.write_text(text, encoding="utf-8")


def update_builder() -> None:
    text = BUILDER.read_text(encoding="utf-8")
    old_summary = '''            "primary_evidenced_vendors",
            "comparative_vendor_notes",
            "product_or_service",
'''
    new_summary = '''            "primary_evidenced_vendors",
            "evidence_scope",
            "evidenced_vendors",
            "evidenced_products_or_services",
            "evidenced_models_or_runtimes",
            "comparative_vendor_notes",
            "product_or_service",
'''
    if "\"evidenced_products_or_services\",\n            \"comparative_vendor_notes\"" not in text:
        text = replace_once(text, old_summary, new_summary, "system_summary fields")

    old_metadata = '''        "primary_evidenced_vendors": system.get("primary_evidenced_vendors", []),
        "product_or_service": system.get("product_or_service", ""),
'''
    new_metadata = '''        "primary_evidenced_vendors": system.get("primary_evidenced_vendors", []),
        "evidence_scope": system.get("evidence_scope", ""),
        "evidenced_vendors": system.get("evidenced_vendors", []),
        "evidenced_products_or_services": system.get("evidenced_products_or_services", []),
        "evidenced_models_or_runtimes": system.get("evidenced_models_or_runtimes", []),
        "product_or_service": system.get("product_or_service", ""),
'''
    if '"evidence_scope": system.get("evidence_scope"' not in text:
        text = replace_once(text, old_metadata, new_metadata, "index metadata fields")
    BUILDER.write_text(text, encoding="utf-8")


def update_builder_test() -> None:
    text = BUILDER_TEST.read_text(encoding="utf-8")
    marker = '''        self.assertEqual(aggregate["system_summary"]["specific_model_or_runtime"], "ChatGPT Advanced Voice Mode")
        self.assertEqual(aggregate["system_summary"]["interaction_mode"], "voice | multi-device")
'''
    replacement = '''        self.assertEqual(aggregate["system_summary"]["specific_model_or_runtime"], "ChatGPT Advanced Voice Mode")
        self.assertEqual(aggregate["system_summary"]["evidence_scope"], "single-provider")
        self.assertEqual(aggregate["system_summary"]["evidenced_vendors"], ["OpenAI"])
        self.assertEqual(aggregate["system_summary"]["evidenced_products_or_services"], ["ChatGPT"])
        self.assertEqual(
            aggregate["system_summary"]["evidenced_models_or_runtimes"],
            ["ChatGPT Advanced Voice Mode"],
        )
        self.assertEqual(aggregate["system_summary"]["interaction_mode"], "voice | multi-device")
'''
    if 'aggregate["system_summary"]["evidence_scope"]' not in text:
        text = replace_once(text, marker, replacement, "builder FM-0002 assertions")
    BUILDER_TEST.write_text(text, encoding="utf-8")


def main() -> int:
    update_schema()
    update_index_schema()
    update_template_json()
    update_template_md()
    update_evidence_guidance()
    update_builder()
    update_builder_test()
    print("Applied affected-system/source-platform contract v2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
