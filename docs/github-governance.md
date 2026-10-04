# GitHub Governance

## Branch Strategy

### master

The default branch.

After bootstrap:

- direct commits are prohibited
- all changes arrive through pull requests

### feature/*

Feature implementation.

Examples:

```text
feature/pre-collector
feature/graphql-client
feature/evidence-model
```

### fix/*

Bug fixes.

Examples:

```text
fix/readme-parser
fix/rate-limit-cache
```

### docs/*

Documentation-only work.

Examples:

```text
docs/governance
docs/pre-collector
```

### spike/*

Time-boxed investigations.

Examples:

```text
spike/github-graphql
spike/repository-ranking
```

---

## Pull Requests

Every change to master requires:

- linked issue
- milestone assignment
- validation evidence
- Conventional Commit title

---

## Labels

### Type

```text
type:feature
type:bug
type:docs
type:test
type:refactor
type:governance
```

### Status

```text
status:ready
status:in-progress
status:blocked
```

### Priority

```text
priority:high
priority:medium
priority:low
```

### Area

```text
area:collector
area:analysis
area:github
area:documentation
area:governance
```

---

## Milestones

### M1 Pre-Collector Foundation

Repository discovery.

Collect:

- filesystem evidence
- git evidence
- readme evidence
- documentation evidence

### M2 Repository Evidence

Collect:

- testing evidence
- DevOps evidence
- governance evidence
- release-readiness evidence

### M3 Portfolio Intelligence

Cross-repository analysis.

Examples:

- strongest architecture repository
- strongest documentation repository
- strongest governance repository

### M4 CV Relevance

Role-oriented recommendations.

Examples:

- software developer
- senior developer
- solution architect

---

## Releases

Prototype releases:

```text
v0.x.y
```

Production releases:

```text
v1.x.y
```

---

## Project Governance Principles

Portfolio Profiler follows:

- Evidence before scoring
- Claim-code parity
- Conventional Commits
- Repository-first analysis
- Rate-limit-aware GitHub integration
- Reproducible collection
- Objective evidence preservation

Repository collectors gather facts.

Analysis and ranking occur in later stages.