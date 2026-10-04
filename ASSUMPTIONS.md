# Assumptions and open design choices

This starter makes only the following working assumptions:

- **JSON + JSON Schema** are the interchange format because they are widely readable and easy to validate. No storage format is selected.
- Each bundle is self-contained and links records by stable string IDs. IDs are opaque and should not be reused.
- **Memory** is a governed assertion or recollection, not automatically a source of truth. A memory can be tentative, disputed, superseded, or expired.
- **Evidence** is recorded at claim level. A citation or locator helps retrieval, but does not by itself prove that the source is authentic or current.
- Authority precedence is scoped to a domain and effective date. A numeric precedence is a tie-break aid, not a substitute for applicability review.
- `extensions.ev.invariants` and `extensions.ev.cases` are a proposed EV-style convention in this starter. No compatibility with an independently published EV extension is asserted.
- “OKF-oriented” means portable, inspectable knowledge records with extension points. This repository does not claim conformance to a finalized OKF specification.
- The included reporting-governance example is synthetic and illustrative, not Wells Fargo policy or regulatory guidance.

Decisions deferred until there is a concrete consumer: identity and access model, sensitivity labels, cryptographic signatures, provenance hashes, versioning protocol, merge semantics, retention/deletion, authority adjudication, eval runner interface, and runtime/API.
