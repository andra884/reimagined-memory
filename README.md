# reimagined-memory

A small, portable starter for memory that can be inspected, trusted, evaluated, and revised without losing its evidence or authority boundaries.

The package separates **what is remembered** (memory), **why it is believed** (evidence), and **which source governs a decision** (authority). It is designed as a human-readable, OKF-oriented bundle with an explicit EV-style evaluation extension point. It does not assume a model, database, retrieval engine, or regulatory certification.

## Start here

- `schemas/`: JSON Schema contracts for memory records, evidence, and authority records.
- `examples/regulatory-reporting/bundle.json`: one synthetic bundle showing linked records and EV-style invariants.
- `docs/trust-and-authority.md`: source handling and conflict rules.
- `evals/`: starter eval cases and a dependency-free bundle integrity check.
- `ASSUMPTIONS.md`: scope and decisions intentionally left open.

Run the starter check with Python 3.10+:

```sh
python evals/check_bundle.py
```

## Core contract

A memory record is a versioned assertion with a type, scope, status, time bounds, evidence links, and an authority reference when one exists. An evidence record identifies a source and the exact claim it supports, plus verification and freshness metadata. An authority record describes a source's domain, precedence, and effective period. These are separate records so a useful recollection cannot silently become policy.

### Trust rules

1. Preserve provenance and scope; never upgrade a paraphrase or inference into a source fact.
2. Prefer the highest applicable authority for the question and effective date. Authority is domain-scoped, not universal.
3. If evidence is missing, stale, out of scope, or conflicting, mark the gap and abstain from a definitive answer.
4. Keep source assertion, interpretation, and derived conclusion distinguishable.
5. Treat EV `invariants` as non-negotiable checks: evaluations may report a failure, but must not rewrite or waive the invariant to pass.
6. Record corrections as new versions with a reason and links; do not silently erase history.

See [trust and authority rules](docs/trust-and-authority.md) for operational detail.

## Must-have foundations

- Stable IDs, explicit schemas, provenance links, and temporal scope.
- Authority and trust rules, including conflict and abstention behavior.
- Invariants and evaluation cases that can fail visibly.
- A minimal example that validates its links.

## Later features

Storage adapters, retrieval and ranking, embeddings, ingestion pipelines, model-specific prompts, permission enforcement, signed evidence, automated freshness checks, richer eval runners, and production monitoring. Add these only with stated requirements and threat model.

## Package shape

```text
schemas/       portable record contracts
docs/          trust and governance rules
examples/      small, self-contained bundle
evals/         evaluation contract and starter integrity check
```

## Status

This is a starter contract, not a deployed memory service or certification. The OKF/EV terms here describe an intended packaging direction and a lightweight extension convention; see [assumptions](ASSUMPTIONS.md) before treating either as a formal external standard.
