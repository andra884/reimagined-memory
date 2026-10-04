# Evaluation hooks

The EV-style starter has two pieces:

- `extensions.ev.invariants` in a bundle contains non-negotiable constraints.
- `cases.jsonl` records named behavioral cases that an application-specific runner can execute against a model, retrieval pipeline, or policy layer.

A case is a hook, not a test result. This repository does not include a model runner; consumers should bind each case to their own prompt, fixture, expected outcome, and trace capture. On failure, retain the failing input and evidence trace. Never edit an invariant automatically to make a failed run pass.

Run `python evals/check_bundle.py` to check the example bundle's record IDs, evidence links, authority links, invariant IDs, and eval case references. This validates package integrity only; it does not establish factual correctness or model behavior.
