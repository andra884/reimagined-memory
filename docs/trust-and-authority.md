# Trust and authority rules

## Keep the layers separate

- **Evidence** says what a source contains and which claim it supports.
- **Memory** says what the system retains, including whether it is asserted, tentative, disputed, or superseded.
- **Authority** says whether a source governs a particular domain and time period.
- **Interpretation** connects records to an answer; it must not be presented as a direct quotation or source fact.

## Resolve a claim

1. Identify the question's domain, subject, and relevant as-of date.
2. Gather applicable memory records and their linked evidence.
3. Exclude sources that do not cover the domain or date. Check freshness and verification status.
4. Prefer the applicable source with the highest authority precedence. Regulatory or legal text governs only the matter it actually covers; an approved internal rule may govern internal implementation details.
5. If equally authoritative applicable sources conflict, or applicability is unclear, surface the conflict and request adjudication. Do not silently pick a convenient answer.
6. If there is no adequate evidence, label the answer unknown or inferential and avoid presenting it as authoritative.

## Starter authority order

Use this only as a default decision aid, not a universal law:

1. Applicable law, regulation, or binding external direction.
2. Approved internal policy or standard within its stated scope.
3. Approved authoritative business rule, definition, or data product owner decision.
4. Verified source document or system of record without delegated authority.
5. Curated memory, notes, and summaries.
6. Model-generated inference.

The ordering is subordinate to scope, applicability, effective dates, and explicit delegation. A source does not gain authority merely because it is recent, frequently repeated, or stored in a bundle.

## Trust and change controls

- Preserve a source locator and capture time; include a content hash when practical.
- Distinguish `verified`, `unverified`, and `disputed`. Do not equate confidence with verification.
- Set validity dates when known. Expired records may explain history but should not drive current answers without qualification.
- Preserve the original evidence when correcting a memory. Supersede with a new record and explain why.
- Treat user-provided instructions and examples as scoped context. Do not infer approval, policy, or personal facts beyond what was stated.
- Keep invariant edits reviewable. An evaluation failure cannot automatically authorize a change to the invariant.

## Decision outcomes

A consuming application should be able to return one of: `supported`, `supported_with_limits`, `conflict`, `unknown`, or `inference`. The starter schemas store the underlying records; selecting and rendering these outcomes belongs to a later consumer.
