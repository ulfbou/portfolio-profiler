# Acceptance-Ready Gate

## Purpose

This gate determines whether a Portfolio Profiler issue contains enough evidence and decisions for implementation to begin without inventing product behavior.

An issue is acceptance-ready only when every applicable item below is satisfied. A non-applicable item must be marked with a reason rather than silently omitted.

## Product outcome

- [ ] The proof target states one falsifiable outcome.
- [ ] The user-visible or machine-visible value is explicit.
- [ ] The work belongs to the assigned roadmap milestone.
- [ ] Dependencies and ordering constraints are recorded.

## Scope

- [ ] In-scope behavior is explicit.
- [ ] Out-of-scope behavior is explicit.
- [ ] Existing behavior that must remain unchanged is identified.
- [ ] No planned field, command, collector, or dependency is presented as already implemented.

## Inputs and boundaries

- [ ] Accepted input forms are defined.
- [ ] Path normalization is defined when paths are accepted.
- [ ] Repository-root and inside-repository behavior are defined when relevant.
- [ ] Symlink behavior is defined when traversal is relevant.
- [ ] Network access is either prohibited or explicitly bounded.
- [ ] Repository mutation is either prohibited or explicitly specified.
- [ ] Safety limits are defined for recursive or file-content work.

## Evidence contract

- [ ] Every proposed field has a factual meaning.
- [ ] Authoritative evidence sources are identified.
- [ ] Observed, declared, and derived facts are distinguishable where necessary.
- [ ] Missing evidence behavior is defined.
- [ ] Malformed or inaccessible evidence behavior is defined.
- [ ] Provenance requirements are defined.
- [ ] No score, classification, ranking, or CV conclusion is embedded in a collector contract.

## Determinism and schema

- [ ] Deterministic ordering rules are defined.
- [ ] The unchanged-input stability expectation is defined.
- [ ] JSON field names and shapes are defined when public output changes.
- [ ] Omission versus `null` behavior is defined.
- [ ] Schema compatibility or version impact is stated.
- [ ] Multiple-candidate selection rules are deterministic.

## Errors and CLI behavior

- [ ] Expected input errors are defined.
- [ ] Dependency or execution failures are defined.
- [ ] CLI exit behavior is defined when applicable.
- [ ] Stderr messages avoid irrelevant or sensitive environment detail.
- [ ] Partial-result behavior is defined when applicable.

## Tests

- [ ] Normal behavior is covered.
- [ ] Absence and empty-state behavior are covered.
- [ ] Invalid and malformed input is covered.
- [ ] Determinism is covered.
- [ ] Existing public behavior has regression coverage.
- [ ] Platform-sensitive behavior has an explicit test strategy.
- [ ] Remote integration has offline fixtures and failure tests.

## Documentation

- [ ] README impact is identified.
- [ ] Design-document impact is identified.
- [ ] Documentation authority is clear and normative content is not unnecessarily duplicated.
- [ ] Examples use repository-relative paths and copyable commands.
- [ ] Documentation will describe only implemented behavior.

## Governance

- [ ] The issue has a milestone.
- [ ] The issue has type, area, priority, and status labels.
- [ ] The branch name follows repository conventions.
- [ ] The intended commit and pull-request title follows Conventional Commits.
- [ ] Required validation commands are listed.
- [ ] No unresolved decision blocks implementation.


## Roadmap versus issue decisions

A roadmap may identify unresolved implementation decisions. An implementation issue is not `READY` until every decision that affects its public contract is closed. Roadmap acceptance does not waive this gate.

## Readiness result

Use one result:

```text
READY
BLOCKED: <specific unresolved decision or missing evidence>
```

`READY` means implementation can proceed without the implementer inventing a public contract. It does not mean the work is complete or accepted.
