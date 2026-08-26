#!/usr/bin/env python3
"""Reconcile failure-mode affected-system context from structured VIGIL metadata.

The projection deliberately separates the platform on which evidence is published
(`source_platform`) from the AI/platform system affected by the failure. Affected
system identity is derived from structured `system_or_product` and
`model_or_algorithm` source metadata, with a bounded fallback to the FM's existing
concrete `system_context` for older records that pre-date those source fields.
Narrative prose is never mined to manufacture vendor/model identity.

The original corpus-wide migration occurred on 2026-08-15. For records created
after that migration, evidence_projection.reconciled_on is never allowed to
predate the record's canonical creation date.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
from collections import OrderedDict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FAILURES_ROOT = ROOT / "vigil" / "records" / "failures"
REVIEW_PATH = ROOT / "vigil" / "docs" / "reviews" / "FM-SYSTEM-CONTEXT-01-evidence-rollup-reconciliation.md"
MIGRATION_DATE = "2026-08-15"

EVIDENCE_ROLES = {
    "incident-evidence",
    "affected-party-evidence",
    "research-evidence",
    "verification-evidence",
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
    "not specified",
    "not limited to a single model or runtime",
    "as described by the incident record",
    "as described by source",
    "multiple products or services across evidenced vendors; use source_records for specifics.",
    "multiple evidenced access surfaces; specify details in source_records and deployment_context.",
}

GENERIC_PLATFORM_VALUES = {"Multi Vendor", "Other", "Unknown", "Not applicable"}

PROVIDER_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    ("OpenAI", ("openai", "chatgpt", "codex", "gpt-", "gpt ", "o4-mini", "o3")),
    ("Anthropic", ("anthropic", "claude")),
    ("Google", ("google", "gemini", "vertex ai", "ai studio")),
    ("Meta", ("meta ai", "llama", "meta")),
    ("xAI", ("xai", "grok", "x premium")),
    ("Microsoft", ("microsoft", "azure ai", "azure openai", "microsoft copilot")),
    ("GitHub", ("github copilot", "github")),
    ("Amazon", ("amazon", "aws", "bedrock")),
    ("Hugging Face", ("hugging face", "huggingface")),
    ("Mistral", ("mistral", "le chat")),
    ("DeepSeek", ("deepseek",)),
    ("Alibaba", ("alibaba", "qwen")),
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
    ("Snap", ("snapchat",)),
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
    ("GitHub Copilot", ("github copilot",)),
    ("Copilot", ("microsoft copilot",)),
    ("Azure OpenAI", ("azure openai",)),
    ("Amazon Bedrock", ("bedrock",)),
    ("Llama", ("llama",)),
    ("Qwen", ("qwen",)),
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

PRODUCT_PROVIDER = {
    "ChatGPT": "OpenAI",
    "Codex": "OpenAI",
    "OpenAI API": "OpenAI",
    "Claude": "Anthropic",
    "Claude Code": "Anthropic",
    "Claude Console": "Anthropic",
    "Claude API": "Anthropic",
    "Claude Cowork": "Anthropic",
    "Gemini": "Google",
    "Google AI Studio": "Google",
    "Vertex AI": "Google",
    "Grok": "xAI",
    "X": "xAI",
    "X Premium": "xAI",
    "GitHub Copilot": "GitHub",
    "Copilot": "Microsoft",
    "Azure OpenAI": "Microsoft",
    "Amazon Bedrock": "Amazon",
    "Llama": "Meta",
    "Qwen": "Alibaba",
    "Le Chat": "Mistral",
    "Perplexity": "Perplexity",
    "Replit Agent": "Replit",
    "Cursor": "Cursor",
    "Meta AI": "Meta",
    "Character.AI": "Character.AI",
    "Firefly": "Adobe",
    "Midjourney": "Midjourney",
    "Runway": "Runway",
    "TikTok": "TikTok",
    "Snapchat": "Snap",
}

# Only values already admitted by the closed compatibility schema belong here.
# Evidence-backed arrays are intentionally more expressive and may contain newer
# providers/products without changing the compatibility summary enums.
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


def extend_unique(target: list[str], values: list[str]) -> None:
    for value in values:
        add_unique(target, value)


def structured_text(value: dict[str, Any], *fields: str) -> str:
    return " | ".join(str(value.get(field, "")) for field in fields if isinstance(value.get(field), str))


def products_from_text(value: Any) -> list[str]:
    if not meaningful(value):
        return []
    text = f" {norm(value)} "
    products: list[str] = []
    for product, patterns in PRODUCT_PATTERNS:
        if any(pattern in text for pattern in patterns):
            add_unique(products, product)
    raw = norm(value)
    if raw == "x" or re.search(r"(?:^|[|/,;]\s*)x(?:\s*[|/,;]|$)", raw):
        add_unique(products, "X")
    if "x premium" in raw:
        add_unique(products, "X")
    return products


def providers_from_text(value: Any) -> list[str]:
    if not meaningful(value):
        return []
    text = norm(value)
    providers: list[str] = []
    for provider, patterns in PROVIDER_PATTERNS:
        if any(pattern in text for pattern in patterns):
            add_unique(providers, provider)
    for product in products_from_text(value):
        provider = PRODUCT_PROVIDER.get(product)
        if provider:
            add_unique(providers, provider)
    return providers


def split_model_values(value: Any) -> list[str]:
    if not meaningful(value):
        return []
    text = str(value).strip()
    result: list[str] = []
    for piece in re.split(r"\s*(?:/|;|\|)\s*", text):
        piece = piece.strip()
        if meaningful(piece):
            add_unique(result, piece)
    return result


def eligible_source(source: Any) -> bool:
    if not isinstance(source, dict):
        return False
    residence = source.get("source_residence", "unknown")
    role = source.get("source_role", "unknown")
    return residence in EVIDENCE_RESIDENCES and role in EVIDENCE_ROLES


def source_affected_identity(source: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    """Return affected-system identity from fields that describe the affected system.

    `source_platform` is intentionally excluded: it identifies where evidence is
    published/hosted and may be TikTok, Reddit, a news outlet, GitHub, etc.
    """
    affected_text = structured_text(source, "system_or_product", "model_or_algorithm")
    products = products_from_text(affected_text)
    providers = providers_from_text(affected_text)
    models = split_model_values(source.get("model_or_algorithm"))
    return providers, products, models


def context_identity(context: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    """Recover concrete identity from the FM's structured system_context."""
    specific = context.get("specific_model_or_runtime")
    model_or_product = context.get("model_or_product")
    product_or_service = context.get("product_or_service")
    platform = context.get("platform_or_vendor")

    declared_providers: list[str] = []
    for field in ("primary_evidenced_vendors", "vendor_cluster"):
        values = context.get(field)
        if isinstance(values, list):
            for value in values:
                if value in CONCRETE_LEGACY_PROVIDERS:
                    add_unique(declared_providers, str(value))

    high_products = products_from_text(specific)
    high_providers = providers_from_text(specific)
    mid_text = " | ".join(
        str(value) for value in (model_or_product, product_or_service) if meaningful(value)
    )
    mid_products = products_from_text(mid_text)
    mid_providers = providers_from_text(mid_text)

    providers: list[str] = []
    products: list[str] = []
    extend_unique(providers, declared_providers)

    if high_providers:
        extend_unique(providers, high_providers)
        extend_unique(products, high_products)
        for product in mid_products:
            mapped = PRODUCT_PROVIDER.get(product)
            if mapped is None or mapped in providers:
                add_unique(products, product)
    elif mid_providers:
        extend_unique(providers, mid_providers)
        extend_unique(products, high_products)
        extend_unique(products, mid_products)
    else:
        extend_unique(products, high_products)
        extend_unique(products, mid_products)
        if platform in CONCRETE_LEGACY_PROVIDERS:
            add_unique(providers, str(platform))

    for product in products:
        provider = PRODUCT_PROVIDER.get(product)
        if provider and (not high_providers or provider in high_providers):
            add_unique(providers, provider)

    if not providers and platform in CONCRETE_LEGACY_PROVIDERS:
        add_unique(providers, str(platform))

    models = split_model_values(specific)
    return providers, products, models


def baseline_context(path: Path, baseline_ref: str | None) -> dict[str, Any] | None:
    if not baseline_ref:
        return None
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{baseline_ref}:{relative}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    try:
        record = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    context = record.get("system_context") if isinstance(record, dict) else None
    return context if isinstance(context, dict) else None


def canonical_record_date(record: dict[str, Any]) -> str:
    identity = record.get("record_identity")
    created = identity.get("created") if isinstance(identity, dict) else None
    recorded = record.get("date_recorded")
    for value in (created, recorded):
        if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:.*)?", value):
            return value[:10]
    return MIGRATION_DATE


def record_reconciliation_date(record: dict[str, Any]) -> str:
    """Return a deterministic projection date that cannot predate the record."""
    return max(MIGRATION_DATE, canonical_record_date(record))


def projection_entry(
    source: dict[str, Any],
    providers: list[str],
    products: list[str],
    models: list[str],
    projection_basis: str,
) -> dict[str, Any]:
    entry: OrderedDict[str, Any] = OrderedDict()
    entry["providers_or_vendors"] = providers
    entry["products_or_services"] = products
    entry["models_or_runtimes"] = models
    entry["projection_basis"] = projection_basis
    if meaningful(source.get("source_platform")):
        entry["evidence_source_platform"] = str(source["source_platform"]).strip()
    if meaningful(source.get("deployment_context")):
        entry["deployment_context"] = str(source["deployment_context"]).strip()
    entry["source_title"] = str(source.get("source_title", "")).strip() or "Untitled evidence source"
    if meaningful(source.get("source_url")):
        entry["source_url"] = str(source["source_url"]).strip()
    return dict(entry)


def record_context_fallback_entry(
    record_id: str,
    providers: list[str],
    products: list[str],
    models: list[str],
) -> dict[str, Any]:
    return {
        "providers_or_vendors": providers,
        "products_or_services": products,
        "models_or_runtimes": models,
        "projection_basis": "record-system-context-fallback",
        "source_title": f"{record_id} historical system_context",
    }


def project_system_context(
    record: dict[str, Any],
    fallback_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = copy.deepcopy(record.get("system_context") or {})
    fallback = copy.deepcopy(fallback_context or context)

    vendors: list[str] = []
    products: list[str] = []
    models: list[str] = []
    evidenced_systems: list[dict[str, Any]] = []
    eligible_sources: list[dict[str, Any]] = []

    for source in record.get("source_records", []):
        if not eligible_source(source):
            continue
        eligible_sources.append(source)
        source_vendors, source_products, source_models = source_affected_identity(source)
        if not (source_vendors or source_products or source_models):
            continue
        extend_unique(vendors, source_vendors)
        extend_unique(products, source_products)
        extend_unique(models, source_models)
        evidenced_systems.append(
            projection_entry(
                source,
                source_vendors,
                source_products,
                source_models,
                "source-affected-system-metadata",
            )
        )

    fallback_vendors, fallback_products, fallback_models = context_identity(fallback)
    if eligible_sources:
        missing_vendors = [value for value in fallback_vendors if value not in vendors]
        missing_products = [value for value in fallback_products if value not in products]
        missing_models = [value for value in fallback_models if value not in models]
        if missing_vendors or missing_products or missing_models:
            extend_unique(vendors, missing_vendors)
            extend_unique(products, missing_products)
            extend_unique(models, missing_models)
            evidenced_systems.append(
                record_context_fallback_entry(
                    str(record.get("id", "VIGIL failure mode")),
                    missing_vendors,
                    missing_products,
                    missing_models,
                )
            )

    if len(vendors) > 1:
        evidence_scope = "multi-provider"
    elif len(vendors) == 1:
        evidence_scope = "single-provider"
    elif products or models:
        evidence_scope = "provider-unresolved"
    elif norm(fallback.get("platform_or_vendor")) == "not applicable":
        evidence_scope = "not-applicable"
    else:
        evidence_scope = "system-unresolved"

    context["evidence_scope"] = evidence_scope
    context["evidenced_vendors"] = vendors
    context["evidenced_products_or_services"] = products
    context["evidenced_models_or_runtimes"] = models
    context["evidenced_systems"] = evidenced_systems
    context["evidence_projection"] = {
        "basis": "record-local affected-system metadata",
        "method": "structured source affected-system roll-up with record system-context fallback",
        "reconciled_on": record_reconciliation_date(record),
        "inference_boundary": (
            "Affected provider, product, model, and runtime identity is projected from structured "
            "system_or_product and model_or_algorithm source metadata, with bounded fallback to an "
            "existing concrete FM system_context for older records. source_platform identifies where "
            "evidence is hosted or published and is not treated as affected-system identity. Narrative "
            "source_context, relevance_note, article titles, and publisher prose are not mined for identity."
        ),
    }

    if len(vendors) > 1:
        context["platform_or_vendor"] = "Multi Vendor"
    elif len(vendors) == 1:
        context["platform_or_vendor"] = (
            vendors[0] if vendors[0] in CONCRETE_LEGACY_PROVIDERS else "Other"
        )
    else:
        legacy_platform = fallback.get("platform_or_vendor")
        context["platform_or_vendor"] = (
            legacy_platform
            if isinstance(legacy_platform, str) and legacy_platform not in {"Multi Vendor", "Other"}
            else "Unknown"
        )
    context["vendor_cluster"] = vendors
    context["primary_evidenced_vendors"] = vendors

    if len(products) == 1 and products[0] in CANONICAL_SINGLE_PRODUCTS:
        context["product_or_service"] = products[0]
    elif products:
        context["product_or_service"] = "Other"
    else:
        legacy_product = fallback.get("product_or_service")
        if isinstance(legacy_product, str) and legacy_product.strip():
            context["product_or_service"] = legacy_product

    if models:
        context["specific_model_or_runtime"] = "; ".join(models)
    else:
        legacy_model = fallback.get("specific_model_or_runtime")
        if isinstance(legacy_model, str) and legacy_model.strip():
            context["specific_model_or_runtime"] = legacy_model

    if products:
        context["model_or_product"] = "; ".join(products)
    else:
        legacy_model_product = fallback.get("model_or_product")
        if isinstance(legacy_model_product, str) and legacy_model_product.strip():
            context["model_or_product"] = legacy_model_product

    return context


def reconcile_record(
    record: dict[str, Any],
    fallback_context: dict[str, Any] | None = None,
) -> bool:
    if record.get("record_type") != "failure_mode":
        return False
    projected = project_system_context(record, fallback_context=fallback_context)
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
        f"**Original migration date:** {MIGRATION_DATE}",
        "",
        "**Scope:** All canonical VIGIL failure-mode records. The projection separates evidence publication/hosting platform from the affected AI/platform system. It does not add external evidence, browse sources, or infer affected-system identity from narrative prose. Layer 1 external requirements are not modified by this reconciliation.",
        "",
        "## Current corpus state",
        "",
        f"- Failure modes reviewed: **{len(records)}**",
        f"- Failure modes with evidenced providers/vendors: **{with_vendors}**",
        f"- Failure modes with evidenced products/services: **{with_products}**",
        f"- Failure modes with evidenced models/runtimes: **{with_models}**",
        f"- Records changed in this execution: **{len(changed_ids)}**",
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
        "## Projection contract",
        "",
        "- `source_platform` identifies where evidence is hosted or published; it is not an affected-system field.",
        "- `source_records[].system_or_product` and `source_records[].model_or_algorithm` are the source-level affected-system fields when that source establishes affected-system identity.",
        "- Source roles that do not establish the affected system, such as `contextual-background`, are not included in the affected-system roll-up.",
        "- Existing concrete FM `system_context` values provide a bounded compatibility fallback for older evidence packages that pre-date those source fields.",
        "- `evidenced_vendors`, `evidenced_products_or_services`, and `evidenced_models_or_runtimes` are the public-facing normalized roll-ups.",
        "- `evidenced_systems` preserves source traceability and records whether an identity came from source affected-system metadata or the record-context fallback.",
        "- Detailed model/runtime names are intentionally open-ended; closed compatibility fields remain constrained to the schema's admitted values.",
        "- Narrative `source_context`, `relevance_note`, article titles, and publisher prose are not mined to manufacture system identity.",
        "",
        "The 2026-08-15 transmutation applied this contract across the then-current FM corpus. Subsequent records use a deterministic per-record reconciliation date that is never earlier than the record's canonical creation date.",
        "",
        "## Multi-provider failure modes",
        "",
    ]
    lines += [f"- `{record_id}`" for record_id in multi_provider] or ["- None"]
    lines += [
        "",
        "## Unresolved system identity",
        "",
        "These records still lack sufficient structured affected-system metadata or a concrete pre-existing FM system context. They remain unresolved rather than being filled from narrative evidence:",
        "",
    ]
    lines += [f"- `{record_id}`" for record_id in unresolved] or ["- None"]
    lines += ["", "## Records changed in this execution", ""]
    lines += [f"- `{record_id}`" for record_id in changed_ids] or ["- None"]
    lines.append("")
    return "\n".join(lines)


def run(check: bool, write_report: bool, baseline_ref: str | None) -> int:
    changed_paths: list[Path] = []
    changed_ids: list[str] = []
    records: list[dict[str, Any]] = []

    for path in failure_files():
        record = load_json(path)
        fallback = baseline_context(path, baseline_ref)
        changed = reconcile_record(record, fallback_context=fallback)
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
    parser.add_argument(
        "--baseline-ref",
        help="Optional historical ref whose pre-transmutation system_context should be used as the compatibility fallback during a migration run.",
    )
    args = parser.parse_args()
    return run(args.check, args.write_report, args.baseline_ref)


if __name__ == "__main__":
    raise SystemExit(main())
