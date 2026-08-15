#!/usr/bin/env python3
"""Reconcile failure-mode system context from record-local evidence metadata.

This is a bounded, deterministic migration. It does not browse, infer systems from
narrative prose, or change evidence. It projects concrete provider/product/model
metadata already present in each FM's source_records into system_context so public
interfaces do not collapse known systems into placeholder values such as
"Multi Vendor", "Other", or "Unknown".
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FAILURES_ROOT = ROOT / "vigil" / "records" / "failures"
REVIEW_PATH = ROOT / "vigil" / "docs" / "reviews" / "FM-SYSTEM-CONTEXT-01-evidence-rollup-reconciliation.md"
RECONCILIATION_DATE = "2026-08-15"

EVIDENCE_ROLES = {
    "incident-evidence",
    "affected-party-evidence",
    "research-evidence",
    "verification-evidence",
    "standards-or-regulatory-basis",
    "direct-testimony",
    "unknown",
}
EVIDENCE_RESIDENCES = {"external", "user-supplied", "unknown"}

PLACEHOLDERS = {
    "",
    "unknown",
    "other",
    "not applicable",
    "not-applicable",
    "n/a",
    "na",
    "none",
    "as described by the incident record",
    "as described by source",
    "multiple products or services across evidenced vendors; use source_records for specifics.",
    "multiple evidenced access surfaces; specify details in source_records and deployment_context.",
}

PROVIDER_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    ("OpenAI", ("openai", "chatgpt", "codex", "gpt-")),
    ("Anthropic", ("anthropic", "claude")),
    ("Google", ("google", "gemini", "vertex ai", "ai studio")),
    ("Meta", ("meta ai", "meta", "llama")),
    ("xAI", ("xai", "grok", "x premium")),
    ("Microsoft", ("microsoft", "copilot", "azure ai", "azure openai")),
    ("GitHub", ("github", "github copilot")),
    ("Amazon", ("amazon", "aws", "bedrock")),
    ("Hugging Face", ("hugging face", "huggingface")),
    ("Mistral", ("mistral", "le chat")),
    ("DeepSeek", ("deepseek",)),
    ("Perplexity", ("perplexity",)),
    ("Cohere", ("cohere",)),
    ("Nvidia", ("nvidia",)),
    ("Apple", ("apple",)),
    ("Replit", ("replit",)),
    ("Cursor", ("cursor",)),
    ("Character.AI", ("character.ai",)),
    ("Stability AI", ("stability ai", "stable diffusion")),
    ("Runway", ("runway",)),
    ("Midjourney", ("midjourney",)),
    ("Adobe", ("adobe", "firefly")),
    ("TikTok", ("tiktok",)),
    ("Snap", ("snapchat", "snap")),
]

PRODUCT_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    ("ChatGPT", ("chatgpt",)),
    ("Codex", ("codex",)),
    ("OpenAI API", ("openai api",)),
    ("Claude Code", ("claude code",)),
    ("Claude Console", ("claude console",)),
    ("Claude API", ("claude api", "anthropic api")),
    ("Claude Cowork", ("claude cowork",)),
    ("Claude", ("claude",)),
    ("Gemini", ("gemini",)),
    ("Google AI Studio", ("google ai studio", "ai studio")),
    ("Vertex AI", ("vertex ai",)),
    ("Grok", ("grok",)),
    ("X Premium", ("x premium",)),
    ("X", (" x ", "x profile", "x status", "x help center")),
    ("GitHub Copilot", ("github copilot",)),
    ("Copilot", ("copilot",)),
    ("Azure OpenAI", ("azure openai",)),
    ("Amazon Bedrock", ("bedrock",)),
    ("Llama", ("llama",)),
    ("Le Chat", ("le chat",)),
    ("Perplexity", ("perplexity",)),
    ("Replit Agent", ("replit agent",)),
    ("Cursor", ("cursor",)),
    ("Meta AI", ("meta ai",)),
    ("Character.AI", ("character.ai",)),
    ("Firefly", ("firefly",)),
    ("Midjourney", ("midjourney",)),
    ("Runway", ("runway",)),
    ("TikTok", ("tiktok",)),
    ("Snapchat", ("snapchat",)),
]

CONCRETE_LEGACY_PROVIDERS = {
    "OpenAI", "xAI", "Anthropic", "Meta", "Google", "DeepSeek", "Kimi", "Sesame",
    "Cohere", "Perplexity", "Mistral", "Microsoft", "GitHub", "TikTok", "Apple",
    "Amazon", "Nvidia", "Hugging Face", "Stability AI", "Runway", "Midjourney",
    "Adobe", "Character.AI", "Replit", "Notion", "Cursor", "Replika", "Nomi",
    "Chai", "Chub.ai", "Candy AI", "Kindroid", "Pi", "HammerAI", "Snap",
    "Google Play",
}

CANONICAL_SINGLE_PRODUCTS = {
    "ChatGPT", "Claude", "Gemini", "Grok", "Copilot", "Codex", "Claude Code",
    "Deep Research", "Perplexity Assistant", "Llama", "Le Chat", "GitHub Copilot",
    "TikTok", "X", "Replit Agent", "Cursor", "Midjourney", "Runway", "Firefly",
    "Character.AI", "Replika", "Nomi", "Chai", "Chub.ai", "Candy AI", "Kindroid",
    "Pi", "HammerAI", "Snapchat", "Google Play",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise TypeError(f"{path}: expected JSON object")
    return value


def dump_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def norm(value: Any) -> str:
    return re.sub(r"\s+", " ", value.strip()).lower() if isinstance(value, str) else ""


def meaningful(value: Any) -> bool:
    text = norm(value)
    if not text or text in PLACEHOLDERS:
        return False
    if text.startswith("as described by "):
        return False
    if "identified in the incident record" in text:
        return False
    return True


def add_unique(target: list[str], value: str) -> None:
    if value and value not in target:
        target.append(value)


def structured_text(source: dict[str, Any], *fields: str) -> str:
    return " | ".join(str(source.get(field, "")) for field in fields if isinstance(source.get(field), str))


def providers_from_source(source: dict[str, Any]) -> list[str]:
    platform_text = norm(source.get("source_platform"))
    if platform_text == "x":
        return ["xAI"]
    direct: list[str] = []
    for provider, patterns in PROVIDER_PATTERNS:
        if any(pattern in platform_text for pattern in patterns):
            add_unique(direct, provider)
    if direct:
        return direct

    text = norm(structured_text(source, "system_or_product", "model_or_algorithm"))
    inferred: list[str] = []
    for provider, patterns in PROVIDER_PATTERNS:
        if any(pattern in text for pattern in patterns):
            add_unique(inferred, provider)
    return inferred


def products_from_source(source: dict[str, Any]) -> list[str]:
    text = f" {norm(structured_text(source, 'source_platform', 'system_or_product', 'model_or_algorithm'))} "
    products: list[str] = []
    for product, patterns in PRODUCT_PATTERNS:
        if any(pattern in text for pattern in patterns):
            if product == "Claude" and "claude code" in text and not re.search(r"(^|[|/,;]\s*)claude(\s*[|/,;]|$)", text):
                continue
            if product == "Copilot" and "github copilot" in text and "microsoft copilot" not in text:
                continue
            add_unique(products, product)
    return products


def models_from_source(source: dict[str, Any]) -> list[str]:
    value = source.get("model_or_algorithm")
    if not meaningful(value):
        return []
    text = str(value).strip()
    pieces = [piece.strip() for piece in re.split(r"\s*(?:/|;|\|)\s*", text) if meaningful(piece)]
    result: list[str] = []
    for piece in pieces:
        add_unique(result, piece)
    return result


def eligible_source(source: Any) -> bool:
    if not isinstance(source, dict):
        return False
    residence = source.get("source_residence", "unknown")
    role = source.get("source_role", "unknown")
    return residence in EVIDENCE_RESIDENCES and role in EVIDENCE_ROLES


def project_system_context(record: dict[str, Any]) -> dict[str, Any]:
    context = copy.deepcopy(record.get("system_context") or {})
    vendors: list[str] = []
    products: list[str] = []
    models: list[str] = []
    evidenced_systems: list[dict[str, Any]] = []

    for source in record.get("source_records", []):
        if not eligible_source(source):
            continue
        source_vendors = providers_from_source(source)
        source_products = products_from_source(source)
        source_models = models_from_source(source)
        if not (source_vendors or source_products or source_models):
            continue

        for value in source_vendors:
            add_unique(vendors, value)
        for value in source_products:
            add_unique(products, value)
        for value in source_models:
            add_unique(models, value)

        entry: OrderedDict[str, Any] = OrderedDict()
        entry["providers_or_vendors"] = source_vendors
        entry["products_or_services"] = source_products
        entry["models_or_runtimes"] = source_models
        if meaningful(source.get("deployment_context")):
            entry["deployment_context"] = str(source["deployment_context"]).strip()
        entry["source_title"] = str(source.get("source_title", "")).strip()
        if meaningful(source.get("source_url")):
            entry["source_url"] = str(source["source_url"]).strip()
        evidenced_systems.append(dict(entry))

    if len(vendors) > 1:
        evidence_scope = "multi-provider"
    elif len(vendors) == 1:
        evidence_scope = "single-provider"
    elif products or models:
        evidence_scope = "provider-unresolved"
    elif norm(context.get("platform_or_vendor")) == "not applicable":
        evidence_scope = "not-applicable"
    else:
        evidence_scope = "system-unresolved"

    context["evidence_scope"] = evidence_scope
    context["evidenced_vendors"] = vendors
    context["evidenced_products_or_services"] = products
    context["evidenced_models_or_runtimes"] = models
    context["evidenced_systems"] = evidenced_systems
    context["evidence_projection"] = {
        "basis": "record-local source_records",
        "method": "deterministic structured-metadata roll-up",
        "reconciled_on": RECONCILIATION_DATE,
        "inference_boundary": (
            "Provider, product, model, and runtime names are projected only from structured "
            "source_platform, system_or_product, and model_or_algorithm metadata. Narrative "
            "source_context and relevance_note text are not mined for additional system claims."
        ),
    }

    if len(vendors) > 1:
        context["platform_or_vendor"] = "Multi Vendor"
        context["vendor_cluster"] = vendors
        context["primary_evidenced_vendors"] = vendors
    elif len(vendors) == 1:
        context["platform_or_vendor"] = vendors[0]
        context["vendor_cluster"] = vendors
        context["primary_evidenced_vendors"] = vendors
    else:
        legacy = context.get("platform_or_vendor")
        if legacy in CONCRETE_LEGACY_PROVIDERS:
            context.setdefault("vendor_cluster", [legacy])
            context.setdefault("primary_evidenced_vendors", [])
        else:
            if legacy == "Multi Vendor":
                context["platform_or_vendor"] = "Unknown"
            context["vendor_cluster"] = []
            context["primary_evidenced_vendors"] = []

    if len(products) == 1 and products[0] in CANONICAL_SINGLE_PRODUCTS:
        context["product_or_service"] = products[0]
    elif len(products) > 1:
        context["product_or_service"] = "Other"

    if len(models) == 1:
        context["specific_model_or_runtime"] = models[0]
    elif len(models) > 1:
        context["specific_model_or_runtime"] = "; ".join(models)

    if products:
        context["model_or_product"] = "; ".join(products)

    return context


def reconcile_record(record: dict[str, Any]) -> bool:
    if record.get("record_type") != "failure_mode":
        return False
    projected = project_system_context(record)
    if projected == record.get("system_context"):
        return False
    record["system_context"] = projected
    return True


def failure_files() -> list[Path]:
    return sorted(FAILURES_ROOT.rglob("VIGIL-*-FM-*.json"))


def render_report(records: list[dict[str, Any]], changed_ids: list[str]) -> str:
    scopes: dict[str, int] = {}
    with_vendors = 0
    with_products = 0
    with_models = 0
    multi_provider: list[str] = []
    unresolved: list[str] = []
    for record in records:
        context = record.get("system_context", {})
        scope = str(context.get("evidence_scope", "missing"))
        scopes[scope] = scopes.get(scope, 0) + 1
        if context.get("evidenced_vendors"):
            with_vendors += 1
        if context.get("evidenced_products_or_services"):
            with_products += 1
        if context.get("evidenced_models_or_runtimes"):
            with_models += 1
        if scope == "multi-provider":
            multi_provider.append(str(record.get("id")))
        if scope in {"provider-unresolved", "system-unresolved"}:
            unresolved.append(str(record.get("id")))

    lines = [
        "# FM-SYSTEM-CONTEXT-01 — Evidence-backed system-context reconciliation",
        "",
        f"**Reconciliation date:** {RECONCILIATION_DATE}",
        "",
        "**Scope:** All canonical VIGIL failure-mode records. This is a deterministic metadata projection from each FM's own `source_records`; it does not add external evidence, browse sources, infer vendor/model identity from narrative prose, or modify Layer 1 external requirements.",
        "",
        "## Outcome",
        "",
        f"- Failure modes reviewed: **{len(records)}**",
        f"- Failure modes changed by reconciliation: **{len(changed_ids)}**",
        f"- Failure modes with evidenced providers/vendors: **{with_vendors}**",
        f"- Failure modes with evidenced products/services: **{with_products}**",
        f"- Failure modes with evidenced models/runtimes: **{with_models}**",
        "",
        "### Evidence scope",
        "",
        "| Scope | Records |",
        "| --- | ---: |",
    ]
    for scope in sorted(scopes):
        lines.append(f"| `{scope}` | {scopes[scope]} |")
    lines += [
        "",
        "## Contract",
        "",
        "The maintained `system_context` block now separates compatibility summary fields from evidence-backed roll-ups:",
        "",
        "- `evidence_scope` describes whether record-local evidence resolves zero, one, or multiple providers.",
        "- `evidenced_vendors` lists providers/vendors established by structured source metadata.",
        "- `evidenced_products_or_services` lists concrete products/services established by structured source metadata.",
        "- `evidenced_models_or_runtimes` preserves concrete model/runtime names present in `model_or_algorithm`.",
        "- `evidenced_systems` preserves source-level traceability to the evidence record that established each system claim.",
        "- `platform_or_vendor`, `product_or_service`, and `specific_model_or_runtime` remain compatibility summary fields and must not substitute for the evidence-backed arrays in public interfaces.",
        "",
        "No system identity is inferred from narrative `source_context`, `relevance_note`, article title, or publisher identity alone.",
        "",
        "## Multi-provider failure modes",
        "",
    ]
    lines += [f"- `{record_id}`" for record_id in multi_provider] or ["- None"]
    lines += [
        "",
        "## Unresolved system identity",
        "",
        "The following records retain insufficient structured source metadata to identify a provider or system deterministically. They are not silently filled from narrative context:",
        "",
    ]
    lines += [f"- `{record_id}`" for record_id in unresolved] or ["- None"]
    lines += ["", "## Changed records", ""]
    lines += [f"- `{record_id}`" for record_id in changed_ids] or ["- None"]
    lines.append("")
    return "\n".join(lines)


def run(check: bool, write_report: bool) -> int:
    changed_paths: list[Path] = []
    changed_ids: list[str] = []
    records: list[dict[str, Any]] = []

    for path in failure_files():
        record = load_json(path)
        changed = reconcile_record(record)
        records.append(record)
        if changed:
            changed_paths.append(path)
            changed_ids.append(str(record.get("id")))
            if not check:
                dump_json(path, record)

    report = render_report(records, changed_ids)
    if write_report and not check:
        REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
        REVIEW_PATH.write_text(report, encoding="utf-8")

    if check and changed_paths:
        print("FM system-context reconciliation is stale:")
        for path in changed_paths:
            print(f"- {path.relative_to(ROOT)}")
        return 1

    print(
        "FM system-context reconciliation "
        f"{'check' if check else 'write'} complete: "
        f"{len(records)} records reviewed, {len(changed_paths)} changed."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when any FM system_context differs from the deterministic projection.")
    parser.add_argument("--write-report", action="store_true", help="Write the repository reconciliation review report.")
    args = parser.parse_args()
    return run(args.check, args.write_report)


if __name__ == "__main__":
    raise SystemExit(main())
