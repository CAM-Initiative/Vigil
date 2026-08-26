#!/usr/bin/env python3
"""Focused tests for evidence-backed FM system-context reconciliation."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "vigil" / "scripts" / "reconcile-fm-system-context.py"
SPEC = importlib.util.spec_from_file_location("reconcile_fm_system_context", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def source(platform: str, system: str = "", model: str = "", *, title: str = "Source", url: str = "https://example.invalid/source", context: str = "") -> dict:
    return {
        "source_residence": "external",
        "source_role": "incident-evidence",
        "source_platform": platform,
        "system_or_product": system,
        "model_or_algorithm": model,
        "deployment_context": context,
        "source_title": title,
        "source_url": url,
    }


def base_record(sources: list[dict], context: dict | None = None) -> dict:
    return {
        "id": "VIGIL-2026-FM-9999",
        "record_type": "failure_mode",
        "source_records": sources,
        "system_context": context or {
            "platform_or_vendor": "Multi Vendor",
            "product_or_service": "Other",
            "specific_model_or_runtime": "Unknown",
            "model_or_product": "Unknown",
            "interface_surface": "Multiple surfaces",
        },
    }


def test_multi_provider_rollup_uses_affected_system_fields() -> None:
    record = base_record([
        source("OpenAI Help Center", "OpenAI account access / ChatGPT / Codex / OpenAI API"),
        source("Business Insider", "Claude / Claude Code / Claude API", "Claude / Claude Code"),
    ])
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic"]
    assert "ChatGPT" in projected["evidenced_products_or_services"]
    assert "Codex" in projected["evidenced_products_or_services"]
    assert "Claude Code" in projected["evidenced_products_or_services"]
    assert projected["evidenced_models_or_runtimes"] == ["Claude", "Claude Code"]
    assert projected["platform_or_vendor"] == "Multi Vendor"


def test_evidence_host_is_not_affected_vendor() -> None:
    record = base_record(
        [source("TikTok", title="TikTok observation")],
        context={
            "platform_or_vendor": "OpenAI",
            "product_or_service": "ChatGPT",
            "specific_model_or_runtime": "ChatGPT Advanced Voice Mode",
            "model_or_product": "ChatGPT",
            "interface_surface": "voice | multi-device",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_products_or_services"] == ["ChatGPT"]
    assert projected["evidenced_models_or_runtimes"] == ["ChatGPT Advanced Voice Mode"]
    assert projected["platform_or_vendor"] == "OpenAI"
    assert projected["product_or_service"] == "ChatGPT"
    assert "TikTok" not in projected["evidenced_vendors"]
    assert "TikTok" not in projected["evidenced_products_or_services"]
    assert projected["evidenced_systems"][0]["projection_basis"] == "record-system-context-fallback"
    assert projected["evidenced_systems"][0]["source_title"] == "VIGIL-2026-FM-9999 historical system_context"
    assert "evidence_source_platform" not in projected["evidenced_systems"][0]


def test_publisher_and_narrative_are_not_mined() -> None:
    record = base_record([
        source("Reuters", "", "", context="OpenAI ChatGPT and Anthropic Claude are discussed here.")
    ])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == []
    assert projected["evidenced_products_or_services"] == []
    assert projected["evidence_scope"] == "system-unresolved"


def test_x_affected_system_can_use_record_context_fallback() -> None:
    record = base_record(
        [source("X Help Center")],
        context={
            "platform_or_vendor": "xAI",
            "product_or_service": "X",
            "specific_model_or_runtime": "Not applicable",
            "model_or_product": "X Premium / X verification / X recommender affordances",
            "interface_surface": "X profile",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["xAI"]
    assert "X" in projected["evidenced_products_or_services"]
    assert "X Premium" in projected["evidenced_products_or_services"]
    assert projected["platform_or_vendor"] == "xAI"


def test_specific_model_beats_polluted_host_compatibility_fields() -> None:
    record = base_record(
        [source("TikTok")],
        context={
            "platform_or_vendor": "TikTok",
            "product_or_service": "TikTok",
            "specific_model_or_runtime": "ChatGPT Advanced Voice Mode",
            "model_or_product": "TikTok",
            "interface_surface": "voice | multi-device",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_products_or_services"] == ["ChatGPT"]
    assert projected["platform_or_vendor"] == "OpenAI"
    assert projected["product_or_service"] == "ChatGPT"


def test_uncertainty_is_not_a_model_and_provider_cluster_survives() -> None:
    record = base_record(
        [source("OpenAI Status", "ChatGPT and OpenAI APIs", "not specified")],
        context={
            "platform_or_vendor": "Multi Vendor",
            "vendor_cluster": ["OpenAI", "Anthropic"],
            "primary_evidenced_vendors": ["OpenAI", "Anthropic"],
            "product_or_service": "Other",
            "specific_model_or_runtime": "Not limited to a single model or runtime",
            "model_or_product": "OpenAI and Anthropic frontier AI platform services",
            "interface_surface": "multiple access surfaces",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic"]
    assert projected["evidenced_models_or_runtimes"] == []
    fallback = [
        item for item in projected["evidenced_systems"]
        if item["projection_basis"] == "record-system-context-fallback"
    ]
    assert len(fallback) == 1
    assert fallback[0]["providers_or_vendors"] == ["Anthropic"]
    assert fallback[0]["source_title"] == "VIGIL-2026-FM-9999 historical system_context"
    assert "evidence_source_platform" not in fallback[0]


def test_qwen_maps_to_alibaba() -> None:
    record = base_record([source("Research paper", "Qwen models", "Qwen3 235B")])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["Alibaba"]
    assert projected["evidenced_products_or_services"] == ["Qwen"]
    assert projected["platform_or_vendor"] == "Alibaba"
    assert projected["product_or_service"] == "Qwen"


def test_explicit_affected_identity_is_authoritative_and_disables_legacy_fallback() -> None:
    primary = source("Nature Communications", "mixed model evaluation", "prose summary")
    primary["affected_system_identity"] = {
        "providers_or_vendors": ["OpenAI", "Anthropic", "Google", "Meta", "xAI", "DeepSeek", "Alibaba"],
        "products_or_services": [],
        "models_or_runtimes": ["GPT-4o", "Claude 4 Sonnet", "Gemini 2.5 Flash", "Qwen3 235B"],
    }
    record = base_record(
        [primary],
        context={
            "platform_or_vendor": "Multi Vendor",
            "vendor_cluster": ["OpenAI", "Anthropic"],
            "primary_evidenced_vendors": ["OpenAI", "Anthropic"],
            "product_or_service": "Other",
            "specific_model_or_runtime": "Legacy prose runtime label",
            "model_or_product": "stateful systems",
            "interface_surface": "multi-turn",
        },
    )
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic", "Google", "Meta", "xAI", "DeepSeek", "Alibaba"]
    assert projected["evidenced_models_or_runtimes"] == ["GPT-4o", "Claude 4 Sonnet", "Gemini 2.5 Flash", "Qwen3 235B"]
    assert "Legacy prose runtime label" not in projected["evidenced_models_or_runtimes"]
    assert projected["evidenced_systems"][0]["projection_basis"] == "source-explicit-affected-system-identity"


def test_supporting_source_can_opt_out_of_affected_system_projection() -> None:
    primary = source("Research paper", "ChatGPT", "GPT-4o", title="Primary")
    supporting = source("Provider announcement", "OpenAI API safety systems", "Private Safety Processing", title="Supporting")
    supporting["affected_system_projection"] = False
    projected = MODULE.project_system_context(base_record([primary, supporting]))
    assert projected["evidenced_vendors"] == ["OpenAI"]
    assert projected["evidenced_models_or_runtimes"] == ["GPT-4o"]
    assert [item["source_title"] for item in projected["evidenced_systems"]] == ["Primary"]


def test_reconciliation_is_idempotent() -> None:
    record = base_record([source("Vendor documentation", "ChatGPT", "GPT-5")])
    assert MODULE.reconcile_record(record) is True
    assert MODULE.reconcile_record(record) is False


def main() -> int:
    test_multi_provider_rollup_uses_affected_system_fields()
    test_evidence_host_is_not_affected_vendor()
    test_publisher_and_narrative_are_not_mined()
    test_x_affected_system_can_use_record_context_fallback()
    test_specific_model_beats_polluted_host_compatibility_fields()
    test_uncertainty_is_not_a_model_and_provider_cluster_survives()
    test_qwen_maps_to_alibaba()
    test_explicit_affected_identity_is_authoritative_and_disables_legacy_fallback()
    test_supporting_source_can_opt_out_of_affected_system_projection()
    test_reconciliation_is_idempotent()
    print("FM system-context reconciliation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
