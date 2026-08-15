#!/usr/bin/env python3
# Apply the permanent evidence-backed FM system-context contract.

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "vigil" / "VIGIL.Schema.json"
TEMPLATE_JSON_PATH = ROOT / "vigil" / "templates" / "failure-mode-record-template.json"
TEMPLATE_MD_PATH = ROOT / "vigil" / "templates" / "failure-mode-record-template.md"
VALIDATOR_PATH = ROOT / "vigil" / "scripts" / "validate-vigil-records.py"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "vigil-records.yml"

SCOPE_VALUES = [
    "single-provider",
    "multi-provider",
    "provider-unresolved",
    "system-unresolved",
    "not-applicable",
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError(f"{path}: expected JSON object")
    return value


def dump_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one marker, found {count}")
    return text.replace(old, new, 1)


def update_schema() -> None:
    schema = load_json(SCHEMA_PATH)
    schema["version"] = "3.3-evidence-backed-system-context"
    rules = schema.setdefault("system_context_rules", {})
    rules["description"] = (
        "system_context describes the observed/proposed system, platform, product, service, "
        "runtime, interface, deployment, or governance corpus. For failure modes, compatibility "
        "summary fields are supplemented by an evidence-backed system roll-up derived from "
        "record-local structured source metadata."
    )
    rules["failure_mode_evidence_projection"] = {
        "required_fields": [
            "evidence_scope",
            "evidenced_vendors",
            "evidenced_products_or_services",
            "evidenced_models_or_runtimes",
            "evidenced_systems",
            "evidence_projection",
        ],
        "allowed_evidence_scope_values": SCOPE_VALUES,
        "source_fields": [
            "source_records[].source_platform",
            "source_records[].system_or_product",
            "source_records[].model_or_algorithm",
        ],
        "traceability_rule": (
            "Each evidenced_systems entry preserves the source title and, where present, source URL "
            "that establishes the projected provider, product, model, or runtime identity."
        ),
        "no_narrative_inference_rule": (
            "Provider, product, model, and runtime identities must not be synthesized from narrative "
            "source_context, relevance_note, article titles, or publisher identity where the structured "
            "system metadata does not establish them."
        ),
        "compatibility_rule": (
            "platform_or_vendor, product_or_service, and specific_model_or_runtime remain compatibility "
            "summary fields. Multi Vendor is an evidence-scope summary and must not substitute for the "
            "concrete evidenced_vendors, evidenced_products_or_services, or evidenced_models_or_runtimes arrays."
        ),
        "public_projection_rule": (
            "Public interfaces should prefer evidence-backed arrays and source-traceable evidenced_systems "
            "over placeholder compatibility values such as Multi Vendor, Other, or Unknown."
        ),
        "unresolved_rule": (
            "Insufficient structured system metadata remains explicitly unresolved; narrative evidence may "
            "support later human reconciliation but must not be silently converted into a system identity."
        ),
    }
    dump_json(SCHEMA_PATH, schema)


def update_template_json() -> None:
    template = load_json(TEMPLATE_JSON_PATH)
    template["system_context"] = {
        "system_type": "unknown",
        "platform_or_vendor": "Unknown",
        "vendor_cluster": [],
        "primary_evidenced_vendors": [],
        "product_or_service": "Unknown",
        "specific_model_or_runtime": "Unknown",
        "interface_surface": "Unknown",
        "model_or_product": "Unknown",
        "interaction_mode": "unknown",
        "embodiment_status": "unknown",
        "deployment_context": "unknown",
        "user_role": "unknown",
        "affected_population": "unknown",
        "evidence_scope": "system-unresolved",
        "evidenced_vendors": [],
        "evidenced_products_or_services": [],
        "evidenced_models_or_runtimes": [],
        "evidenced_systems": [],
        "evidence_projection": {
            "basis": "record-local source_records",
            "method": "deterministic structured-metadata roll-up",
            "reconciled_on": "YYYY-MM-DD",
            "inference_boundary": (
                "Project provider, product, model, and runtime identity only from structured source_platform, "
                "system_or_product, and model_or_algorithm metadata. Do not infer system identity from narrative prose."
            ),
        },
    }
    dump_json(TEMPLATE_JSON_PATH, template)


def update_template_markdown() -> None:
    text = TEMPLATE_MD_PATH.read_text(encoding="utf-8")
    start = text.index("## Multi Vendor authoring")
    end = text.index("## Severity and triage model 2.0")
    replacement = '''## Evidence-backed system context

`system_context` separates **scope** from **identity**.

Use `platform_or_vendor: "Multi Vendor"` only as a compatibility summary when structured evidence establishes more than one affected provider. It is not a substitute for naming the providers and systems VIGIL actually knows.

Failure-mode records must maintain the evidence-backed projection:

* `evidence_scope` — `single-provider`, `multi-provider`, `provider-unresolved`, `system-unresolved`, or `not-applicable`;
* `evidenced_vendors` — concrete providers/vendors established by structured evidence metadata;
* `evidenced_products_or_services` — concrete products/services established by structured evidence metadata;
* `evidenced_models_or_runtimes` — concrete model/runtime names established by structured evidence metadata;
* `evidenced_systems` — source-traceable per-evidence system identities; and
* `evidence_projection` — the derivation basis, method, reconciliation date, and inference boundary.

The maintained projection is derived from `source_records[].source_platform`, `source_records[].system_or_product`, and `source_records[].model_or_algorithm`. Do **not** mine narrative `source_context`, `relevance_note`, article titles, or publisher identity to manufacture a provider/model identity that the structured evidence does not establish.

For genuinely multi-provider records, keep the compatibility fields (`platform_or_vendor: "Multi Vendor"` and usually `product_or_service: "Other"`) for existing filters, but populate the evidence-backed arrays with the actual evidenced systems. Public interfaces should prefer those concrete arrays over placeholder compatibility values.

Example:

```json
"system_context": {
  "platform_or_vendor": "Multi Vendor",
  "product_or_service": "Other",
  "specific_model_or_runtime": "Claude; Claude Code; ChatGPT; Codex",
  "evidence_scope": "multi-provider",
  "evidenced_vendors": [
    "OpenAI",
    "Anthropic"
  ],
  "evidenced_products_or_services": [
    "ChatGPT",
    "Codex",
    "OpenAI API",
    "Claude",
    "Claude Code",
    "Claude API"
  ],
  "evidenced_models_or_runtimes": [
    "Claude",
    "Claude Code",
    "ChatGPT",
    "Codex"
  ],
  "evidenced_systems": [
    {
      "providers_or_vendors": ["OpenAI"],
      "products_or_services": ["ChatGPT", "Codex", "OpenAI API"],
      "models_or_runtimes": [],
      "source_title": "Official source title",
      "source_url": "https://example.invalid/source"
    }
  ]
}
```

If structured source metadata is insufficient, preserve `provider-unresolved` or `system-unresolved`. Do not silently fill gaps from narrative context.

'''
    TEMPLATE_MD_PATH.write_text(text[:start] + replacement + text[end:], encoding="utf-8")


VALIDATOR_CONSTANTS = '''
FM_EVIDENCE_SCOPE_VALUES = {
    "single-provider",
    "multi-provider",
    "provider-unresolved",
    "system-unresolved",
    "not-applicable",
}
FM_EVIDENCE_CONTEXT_REQUIRED = {
    "evidence_scope",
    "evidenced_vendors",
    "evidenced_products_or_services",
    "evidenced_models_or_runtimes",
    "evidenced_systems",
    "evidence_projection",
}
FM_EVIDENCE_PROJECTION_REQUIRED = {
    "basis",
    "method",
    "reconciled_on",
    "inference_boundary",
}
'''

VALIDATOR_HELPER = r'''
def _unique_non_empty_strings(
    path: Path,
    label: str,
    value: Any,
    errors: list[str],
) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{path}: {label} must be an array")
        return []
    if any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{path}: {label} must contain only non-empty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{path}: {label} must not contain duplicates")
    return value


def validate_fm_evidence_system_context(
    path: Path,
    context: dict[str, Any],
    errors: list[str],
) -> None:
    missing = sorted(field for field in FM_EVIDENCE_CONTEXT_REQUIRED if field not in context)
    if missing:
        errors.append(
            f"{path}: FM system_context missing evidence-backed fields: {', '.join(missing)}"
        )
        return

    scope = context.get("evidence_scope")
    if scope not in FM_EVIDENCE_SCOPE_VALUES:
        errors.append(
            f"{path}: system_context.evidence_scope {scope!r} is invalid; expected one of "
            f"{', '.join(sorted(FM_EVIDENCE_SCOPE_VALUES))}"
        )

    vendors = _unique_non_empty_strings(
        path, "system_context.evidenced_vendors", context.get("evidenced_vendors"), errors
    )
    products = _unique_non_empty_strings(
        path,
        "system_context.evidenced_products_or_services",
        context.get("evidenced_products_or_services"),
        errors,
    )
    models = _unique_non_empty_strings(
        path,
        "system_context.evidenced_models_or_runtimes",
        context.get("evidenced_models_or_runtimes"),
        errors,
    )

    systems = context.get("evidenced_systems")
    union_vendors: list[str] = []
    union_products: list[str] = []
    union_models: list[str] = []
    if not isinstance(systems, list):
        errors.append(f"{path}: system_context.evidenced_systems must be an array")
        systems = []
    else:
        for index, system in enumerate(systems):
            label = f"system_context.evidenced_systems[{index}]"
            if not isinstance(system, dict):
                errors.append(f"{path}: {label} must be an object")
                continue
            source_title = system.get("source_title")
            if not isinstance(source_title, str) or not source_title.strip():
                errors.append(f"{path}: {label}.source_title must be a non-empty string")
            for optional_field in ("source_url", "deployment_context"):
                value = system.get(optional_field)
                if value is not None and (not isinstance(value, str) or not value.strip()):
                    errors.append(f"{path}: {label}.{optional_field} must be a non-empty string when present")
            entry_vendors = _unique_non_empty_strings(
                path, f"{label}.providers_or_vendors", system.get("providers_or_vendors"), errors
            )
            entry_products = _unique_non_empty_strings(
                path, f"{label}.products_or_services", system.get("products_or_services"), errors
            )
            entry_models = _unique_non_empty_strings(
                path, f"{label}.models_or_runtimes", system.get("models_or_runtimes"), errors
            )
            if not (entry_vendors or entry_products or entry_models):
                errors.append(f"{path}: {label} must identify at least one provider, product, model, or runtime")
            for item in entry_vendors:
                if item not in union_vendors:
                    union_vendors.append(item)
            for item in entry_products:
                if item not in union_products:
                    union_products.append(item)
            for item in entry_models:
                if item not in union_models:
                    union_models.append(item)

    if vendors != union_vendors:
        errors.append(
            f"{path}: system_context.evidenced_vendors must equal the ordered union of evidenced_systems providers"
        )
    if products != union_products:
        errors.append(
            f"{path}: system_context.evidenced_products_or_services must equal the ordered union of "
            "evidenced_systems products"
        )
    if models != union_models:
        errors.append(
            f"{path}: system_context.evidenced_models_or_runtimes must equal the ordered union of "
            "evidenced_systems models/runtimes"
        )

    if scope == "multi-provider" and len(vendors) < 2:
        errors.append(f"{path}: multi-provider evidence_scope requires at least two evidenced_vendors")
    if scope == "single-provider" and len(vendors) != 1:
        errors.append(f"{path}: single-provider evidence_scope requires exactly one evidenced_vendor")
    if scope in {"provider-unresolved", "system-unresolved", "not-applicable"} and vendors:
        errors.append(f"{path}: {scope} evidence_scope must not contain evidenced_vendors")
    if scope in {"system-unresolved", "not-applicable"} and (products or models or systems):
        errors.append(f"{path}: {scope} evidence_scope must not contain concrete evidenced systems")
    if scope == "provider-unresolved" and not (products or models):
        errors.append(
            f"{path}: provider-unresolved evidence_scope requires an evidenced product/model with unresolved provider"
        )

    platform = context.get("platform_or_vendor")
    if platform == "Multi Vendor" and scope != "multi-provider":
        errors.append(f"{path}: platform_or_vendor 'Multi Vendor' requires evidence_scope 'multi-provider'")
    if scope == "multi-provider" and platform != "Multi Vendor":
        errors.append(f"{path}: multi-provider evidence_scope requires platform_or_vendor 'Multi Vendor'")

    if vendors:
        for compatibility_field in ("vendor_cluster", "primary_evidenced_vendors"):
            value = context.get(compatibility_field)
            if value != vendors:
                errors.append(
                    f"{path}: system_context.{compatibility_field} must equal evidenced_vendors for reconciled FMs"
                )

    projection = context.get("evidence_projection")
    if not isinstance(projection, dict):
        errors.append(f"{path}: system_context.evidence_projection must be an object")
    else:
        missing_projection = sorted(
            field for field in FM_EVIDENCE_PROJECTION_REQUIRED if is_blank(projection.get(field))
        )
        if missing_projection:
            errors.append(
                f"{path}: system_context.evidence_projection missing required fields: "
                f"{', '.join(missing_projection)}"
            )
        reconciled_on = projection.get("reconciled_on")
        if isinstance(reconciled_on, str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", reconciled_on):
            errors.append(
                f"{path}: system_context.evidence_projection.reconciled_on must use YYYY-MM-DD"
            )


'''

def update_validator() -> None:
    text = VALIDATOR_PATH.read_text(encoding="utf-8")
    if "FM_EVIDENCE_SCOPE_VALUES = {" not in text:
        marker = "SYSTEM_CONTEXT_REQUIRED = {\n"
        start = text.index(marker)
        close = text.index("}\nID_PREFIX = {", start)
        insertion_point = close + 2
        text = text[:insertion_point] + "\n" + VALIDATOR_CONSTANTS + text[insertion_point:]

    if "def validate_fm_evidence_system_context(" not in text:
        marker = "def validate_runtime_conformance("
        position = text.index(marker)
        text = text[:position] + VALIDATOR_HELPER + text[position:]

    call = "        validate_fm_evidence_system_context(path, system_context, errors)\n"
    if call not in text:
        marker = '    elif record_type == "failure_mode":\n        add_missing(errors, path, record, FM_REQUIRED)\n'
        replacement = marker + call
        text = replace_once(text, marker, replacement, "FM validator call")

    VALIDATOR_PATH.write_text(text, encoding="utf-8")


def update_workflow() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    check_block = '''      - name: Test FM system-context reconciliation
        run: python vigil/tests/test_reconcile_fm_system_context.py

      - name: Check FM system-context reconciliation
        run: python vigil/scripts/reconcile-fm-system-context.py --check

'''
    if "Check FM system-context reconciliation" not in text:
        marker = '''      - name: Test VIGIL record validator
        run: python vigil/scripts/test_validate_vigil_records.py

'''
        text = replace_once(text, marker, marker + check_block, "VIGIL records workflow")
    WORKFLOW_PATH.write_text(text, encoding="utf-8")


def main() -> int:
    update_schema()
    update_template_json()
    update_template_markdown()
    update_validator()
    update_workflow()
    print("Applied evidence-backed FM system-context contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
