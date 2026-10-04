#!/usr/bin/env python3
"""Dependency-free integrity checks for the starter example bundle."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "examples/regulatory-reporting/bundle.json"
CASES = ROOT / "evals/cases.jsonl"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def unique_ids(records: list[dict], label: str) -> set[str]:
    ids = [record.get("id") for record in records]
    if any(not isinstance(value, str) or not value for value in ids):
        fail(f"{label} records need non-empty string IDs")
    if len(ids) != len(set(ids)):
        fail(f"{label} IDs must be unique")
    return set(ids)


def main() -> None:
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    memories = bundle.get("memories", [])
    evidence = bundle.get("evidence", [])
    authorities = bundle.get("authorities", [])
    memory_ids = unique_ids(memories, "memory")
    evidence_ids = unique_ids(evidence, "evidence")
    authority_ids = unique_ids(authorities, "authority")

    for memory in memories:
        if not memory.get("statement") or not memory.get("scope", {}).get("domain"):
            fail(f"{memory.get('id')}: statement and scope.domain are required")
        missing = set(memory.get("evidence_ids", [])) - evidence_ids
        if missing:
            fail(f"{memory['id']}: unknown evidence IDs: {sorted(missing)}")
        authority = memory.get("authority_id")
        if authority and authority not in authority_ids:
            fail(f"{memory['id']}: unknown authority ID {authority}")

    for record in evidence:
        unknown = set(record.get("supports", [])) - memory_ids
        if unknown:
            fail(f"{record['id']}: unknown memory IDs: {sorted(unknown)}")

    ev = bundle.get("extensions", {}).get("ev", {})
    invariant_ids = unique_ids(ev.get("invariants", []), "invariant")
    case_ids = set()
    for line_number, line in enumerate(CASES.read_text(encoding="utf-8").splitlines(), 1):
        case = json.loads(line)
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in case_ids:
            fail(f"eval case line {line_number}: ID missing or duplicated")
        case_ids.add(case_id)
        if not isinstance(case.get("expect"), dict):
            fail(f"{case_id}: expect must be an object")

    unknown_cases = set(ev.get("cases", [])) - case_ids
    if unknown_cases:
        fail(f"bundle references unknown eval cases: {sorted(unknown_cases)}")
    for invariant in ev.get("invariants", []):
        if not invariant.get("statement") or invariant.get("severity") not in {"error", "warning"}:
            fail(f"{invariant.get('id')}: invariant needs statement and valid severity")

    print(
        f"PASS: {len(memories)} memories, {len(evidence)} evidence records, "
        f"{len(authorities)} authorities, {len(invariant_ids)} invariants, "
        f"{len(case_ids)} eval cases; bundle links are intact."
    )


if __name__ == "__main__":
    main()
