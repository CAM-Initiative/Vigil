#!/usr/bin/env python3
"""Verify opt-in VIGIL interpretive review history against pinned Git objects.

This verifies *present* integrity and retained-ref reachability. It cannot
certify that a remote Git ref will remain protected in the future. A separate
Gate 2 archival-retention decision is required before canonical migration.
No canonical files, Git refs or archives are written by this module.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Any

REVIEW_REQUIRED = {
    "review_id", "reviewer_type", "reviewer_platform", "reviewer_model",
    "review_date", "review_scope", "capability_profile", "known_limitations",
    "review_outcome",
}
INDEX_FIELDS = {"review_id", "review_date", "reviewer_type", "reviewer_platform",
                "reviewer_model", "review_sha256", "archive_batch_id"}
BATCH_FIELDS = {"batch_id", "source_commit", "source_path", "source_blob_sha",
                "retention_ref", "review_ids"}
HEX_HASH = re.compile(r"^[0-9a-f]{64}$")
GIT_SHA = re.compile(r"^[0-9a-f]{40}(?:[0-9a-f]{24})?$")
BATCH_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,95}$")
REF_NAME = re.compile(r"^refs/(?:heads|tags)/[A-Za-z0-9][A-Za-z0-9_.\-/]{0,180}$")
RECORD_ID = re.compile(r"^VIGIL-INC-[0-9]{6}$")


def review_digest(review: dict[str, Any]) -> str:
    """Stable full-object digest; not the digest of a shortened representation."""
    data = json.dumps(review, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def _git(root: Path, *args: str) -> str:
    # User-provided refs are fully validated before invoking Git.
    result = subprocess.run(["git", "-C", str(root), *args],
                            capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(f"Git object unavailable or unverified ({' '.join(args[:2])}): "
                         f"{result.stderr.strip()[:250]}")
    return result.stdout.strip()


def _valid_review(review: Any, label: str, errors: list[str]) -> bool:
    if not isinstance(review, dict):
        errors.append(f"{label}: full review is not an object")
        return False
    missing = REVIEW_REQUIRED - set(review)
    if missing:
        errors.append(f"{label}: missing fields {sorted(missing)}")
    if not isinstance(review.get("review_id"), str) or not review.get("review_id"):
        errors.append(f"{label}: review_id missing")
    value = review.get("review_date")
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        errors.append(f"{label}: invalid ISO review_date")
    else:
        try:
            date.fromisoformat(value)
        except ValueError:
            errors.append(f"{label}: invalid calendar review_date")
    return not missing and isinstance(review.get("review_id"), str) and bool(review.get("review_id"))


def compact_provenance_errors(
    record: dict[str, Any],
    *,
    root: Path | None = None,
    verify_git: bool = True,
) -> list[str]:
    """Fail closed for every compact field, reviewer and archive reference.

    Use verify_git=False only to collect structural diagnostics; canonical
    validation MUST always call the default which verifies every Git object.
    """
    errors: list[str] = []
    ident = record.get("id")
    if not isinstance(ident, str) or RECORD_ID.fullmatch(ident) is None:
        return ["compact provenance: invalid canonical Incident ID"]
    provenance = record.get("interpretive_provenance")
    if not isinstance(provenance, dict):
        return ["compact provenance: interpretive_provenance must be object"]
    if "review_history" in provenance:
        errors.append("compact provenance: review_history conflicts with compact index")
    index = provenance.get("review_history_index")
    batches = provenance.get("review_archive_batches")
    current = provenance.get("current_ai_review")
    if not isinstance(index, list) or not index:
        errors.append("compact provenance: review_history_index must be nonempty")
        return errors
    if not isinstance(batches, list):
        errors.append("compact provenance: review_archive_batches must be array")
        return errors
    _valid_review(current, "current_ai_review", errors)
    if not isinstance(current, dict) or current.get("reviewer_type") != "AI analytical reviewer":
        errors.append("compact provenance: current reviewer must be AI analytical reviewer")
    current_id = current.get("review_id") if isinstance(current, dict) else None
    created = (record.get("record_identity") or {}).get("created") or record.get("date_recorded")
    try:
        created_day = date.fromisoformat(str(created)[:10])
    except ValueError:
        errors.append("compact provenance: invalid record creation date")
        created_day = None

    seen_ids: set[str] = set()
    parsed: dict[str, dict[str, Any]] = {}
    current_entries = []
    previous_day = None
    for n, entry in enumerate(index):
        label = f"review_history_index[{n}]"
        if not isinstance(entry, dict) or set(entry) != INDEX_FIELDS:
            errors.append(f"{label}: exact identity/digest/archive fields required")
            continue
        rid = entry["review_id"]
        if not isinstance(rid, str) or not rid or rid in seen_ids:
            errors.append(f"{label}: missing or duplicate review_id")
            continue
        seen_ids.add(rid)
        parsed[rid] = entry
        if not isinstance(entry["review_sha256"], str) or HEX_HASH.fullmatch(entry["review_sha256"]) is None:
            errors.append(f"{label}: invalid review_sha256")
        for key in ("reviewer_type", "reviewer_platform", "reviewer_model"):
            # Unknown source attributes must remain null, not be invented.
            if entry[key] is not None and not isinstance(entry[key], str):
                errors.append(f"{label}: {key} must preserve original string or null")
        try:
            if not isinstance(entry["review_date"], str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry["review_date"]):
                raise ValueError("invalid date")
            day = date.fromisoformat(entry["review_date"])
            if created_day and day < created_day:
                errors.append(f"{label}: review predates creation")
            if previous_day and day < previous_day:
                errors.append(f"{label}: review chronology is reversed")
            previous_day = day
        except ValueError:
            errors.append(f"{label}: invalid review_date")
        if rid == current_id:
            current_entries.append(entry)
            if entry["archive_batch_id"] is not None:
                errors.append(f"{label}: current review must resolve from active full review, not archived copy")
            if isinstance(current, dict) and any(entry[k] != current.get(k) for k in
                                                ("review_id", "reviewer_type", "reviewer_platform",
                                                 "reviewer_model", "review_date")):
                errors.append(f"{label}: current review metadata mismatch")
            if isinstance(current, dict) and entry["review_sha256"] != review_digest(current):
                errors.append(f"{label}: full current review digest mismatch")
        elif not isinstance(entry["archive_batch_id"], str):
            errors.append(f"{label}: historical review must name a recoverable archive batch")
    if len(current_entries) != 1 or not isinstance(index[-1], dict) or index[-1].get("review_id") != current_id:
        errors.append("compact provenance: exactly one current review must be the final indexed review")

    batch_ids: set[str] = set()
    archived: dict[str, dict[str, Any]] = {}
    source_path = f"vigil/records/incidents/{ident}.json"
    if root is None:
        root = Path(__file__).resolve().parents[2]
    for n, batch in enumerate(batches):
        label = f"review_archive_batches[{n}]"
        if not isinstance(batch, dict) or set(batch) != BATCH_FIELDS:
            errors.append(f"{label}: exact Git archive fields required")
            continue
        bid = batch["batch_id"]
        if not isinstance(bid, str) or BATCH_ID.fullmatch(bid) is None or bid in batch_ids:
            errors.append(f"{label}: missing/duplicate/unsafe batch ID")
            continue
        batch_ids.add(bid)
        commit, blob, retention = (batch[k] for k in
                                    ("source_commit", "source_blob_sha", "retention_ref"))
        ids = batch["review_ids"]
        if (not isinstance(commit, str) or GIT_SHA.fullmatch(commit) is None or
            not isinstance(blob, str) or GIT_SHA.fullmatch(blob) is None or
            batch["source_path"] != source_path or not isinstance(retention, str) or
            REF_NAME.fullmatch(retention) is None or ".." in retention or
            not isinstance(ids, list) or not ids or
            any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids))):
            errors.append(f"{label}: invalid Git source/retention-ref/covered review IDs")
            continue
        covered = {i for i in ids}
        if current_id in covered:
            errors.append(f"{label}: active review must not be archived as a historical index entry")
        if not verify_git:
            continue
        try:
            actual_blob = _git(root, "rev-parse", f"{commit}:{source_path}")
            if actual_blob != blob:
                raise ValueError("pinned source blob does not match recorded blob SHA")
            # Resolve a full Git commit, not a mutable tag value or an isolated orphan blob.
            _git(root, "cat-file", "-e", f"{commit}^{{commit}}")
            reachable = subprocess.run(
                ["git", "-C", str(root), "merge-base", "--is-ancestor", commit, retention],
                capture_output=True, text=True, check=False)
            if reachable.returncode:
                raise ValueError("source commit not reachable from named retained ref")
            original = json.loads(_git(root, "show", f"{commit}:{source_path}"))
            if original.get("id") != ident:
                raise ValueError("archived source Incident ID mismatch")
            source_provenance = original.get("interpretive_provenance") or {}
            historic = source_provenance.get("review_history")
            if not isinstance(historic, list):
                historic = []
            # A later compact snapshot retains its full then-current review.
            # Older reviews stay pinned by their original archive batches.
            prior_current = source_provenance.get("current_ai_review")
            if isinstance(prior_current, dict) and prior_current.get("review_id") not in [
                r.get("review_id") for r in historic if isinstance(r, dict)
            ]:
                historic = [*historic, prior_current]
            if not historic:
                raise ValueError("archived source has no full review objects")
            recovered = {r.get("review_id"): r for r in historic
                         if isinstance(r, dict) and isinstance(r.get("review_id"), str)}
            if len(recovered) != len(historic):
                raise ValueError("archive contains missing or duplicated review IDs")
            for rid in covered:
                if rid not in recovered:
                    raise ValueError(f"historical review {rid!r} absent from pinned Git object")
                if rid in archived:
                    raise ValueError(f"historical review {rid!r} declared in multiple batches")
                archived[rid] = recovered[rid]
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{label}: failed immutable archive verification: {exc}")
    if verify_git:
        for rid, entry in parsed.items():
            if rid == current_id:
                continue
            if entry.get("archive_batch_id") not in batch_ids:
                errors.append(f"{rid}: archive batch ID does not resolve")
                continue
            review = archived.get(rid)
            if review is None:
                errors.append(f"{rid}: complete historical review cannot be reconstructed")
                continue
            _valid_review(review, rid, errors)
            for key in ("review_id", "reviewer_type", "reviewer_platform", "reviewer_model", "review_date"):
                if entry.get(key) != review.get(key):
                    errors.append(f"{rid}: original {key} differs from compact index")
            if entry.get("review_sha256") != review_digest(review):
                errors.append(f"{rid}: original full review digest differs from index")
            archive_source = next((b for b in batches if isinstance(b, dict)
                                   and b.get("batch_id") == entry.get("archive_batch_id")), None)
            if isinstance(archive_source, dict) and rid not in archive_source.get("review_ids", []):
                errors.append(f"{rid}: not covered by declared archive batch")
        if set(archived) != set(parsed) - {current_id}:
            errors.append("compact provenance: archive coverage does not match all historical review identities")
    else:
        for rid, entry in parsed.items():
            if rid != current_id and entry.get("archive_batch_id") not in batch_ids:
                errors.append(f"{rid}: missing declared batch")
    return errors
