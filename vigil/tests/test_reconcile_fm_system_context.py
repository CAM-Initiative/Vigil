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


def base_record(sources: list[dict]) -> dict:
    return {
        "id": "VIGIL-2026-FM-9999",
        "record_type": "failure_mode",
        "source_records": sources,
        "system_context": {
            "platform_or_vendor": "Multi Vendor",
            "product_or_service": "Other",
            "specific_model_or_runtime": "Unknown",
            "interface_surface": "Multiple surfaces",
        },
    }


def test_multi_provider_rollup() -> None:
    record = base_record([
        source("OpenAI", "OpenAI account access / ChatGPT / Codex / OpenAI API"),
        source("Anthropic", "Claude / Claude Code / Claude API", "Claude / Claude Code"),
    ])
    projected = MODULE.project_system_context(record)
    assert projected["evidence_scope"] == "multi-provider"
    assert projected["evidenced_vendors"] == ["OpenAI", "Anthropic"]
    assert "ChatGPT" in projected["evidenced_products_or_services"]
    assert "Codex" in projected["evidenced_products_or_services"]
    assert "Claude Code" in projected["evidenced_products_or_services"]
    assert projected["evidenced_models_or_runtimes"] == ["Claude", "Claude Code"]
    assert projected["platform_or_vendor"] == "Multi Vendor"


def test_publisher_is_not_affected_vendor() -> None:
    record = base_record([source("Wired", "", "", context="Article discusses OpenAI and Anthropic.")])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == []
    assert projected["evidenced_products_or_services"] == []
    assert projected["evidence_scope"] == "system-unresolved"


def test_narrative_is_not_mined() -> None:
    record = base_record([source("Reuters", "", "", context="OpenAI ChatGPT was discussed in narrative context.")])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == []
    assert projected["evidenced_products_or_services"] == []


def test_x_platform_maps_to_existing_xai_provider_and_x_product() -> None:
    record = base_record([source("X")])
    projected = MODULE.project_system_context(record)
    assert projected["evidenced_vendors"] == ["xAI"]
    assert projected["evidenced_products_or_services"] == ["X"]
    assert projected["platform_or_vendor"] == "xAI"
    assert projected["product_or_service"] == "X"


def test_reconciliation_is_idempotent() -> None:
    record = base_record([source("OpenAI", "ChatGPT", "GPT-5")])
    assert MODULE.reconcile_record(record) is True
    assert MODULE.reconcile_record(record) is False


def main() -> int:
    test_multi_provider_rollup()
    test_publisher_is_not_affected_vendor()
    test_narrative_is_not_mined()
    test_x_platform_maps_to_existing_xai_provider_and_x_product()
    test_reconciliation_is_idempotent()
    print("FM system-context reconciliation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
