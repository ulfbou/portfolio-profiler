# Pre-Collector

## Purpose

The Pre-Collector gathers repository evidence.

It does not determine:

- repository importance
- CV relevance
- hiring value

Those decisions belong to later analysis stages.

The sole responsibility of the Pre-Collector is to establish objective facts.

---

# High-Level Flow

```text
Repository
    ↓
Collectors
    ↓
Evidence Model
    ↓
Repository Profile
```

---

# Collection Strategy

Prefer local sources whenever possible.

Priority order:

1. Filesystem
2. Git metadata
3. Documentation
4. Build metadata
5. GitHub GraphQL

This minimizes API usage and allows repositories to be analyzed offline.

---

# Planned Evidence Categories

The following categories describe planned collector scope unless explicitly identified as implemented below. Each collector requires an acceptance-ready issue before implementation.

## Repository Identity

Examples:

- repository name
- description
- primary language
- repository age

---

## README Analysis

Collect:

- existence
- size
- heading count
- code block count

Detect topics such as:

- architecture
- governance
- roadmap
- validation
- release process

---

## Documentation Analysis

Scan:

```text
docs/
adr/
specifications/
architecture/
```

Collect:

- file counts
- document categories

---

## Technology Analysis

Detect:

### .NET

- solution files
- project files
- target frameworks
- package management

Target frameworks are collected as declared facts. Framework maturity is not a collector output.

### Python

Detect:

- pyproject.toml
- requirements files
- package structure
- CLI entry points

---

## Testing Analysis

Collect:

- test projects
- test files
- testing frameworks

Examples:

```text
xUnit
pytest
unittest
```

---

## DevOps Analysis

Detect:

```text
.github/workflows
azure-pipelines
build scripts
release scripts
```

Classify workflows into:

- build
- test
- validation
- packaging
- release

---

## Governance Analysis

Detect assets such as:

```text
CONTRIBUTING.md
CODEOWNERS
governance/
standards/
adr/
```

Collect governance indicators without assigning scores.

---

## Release Readiness Indicators

Look for:

- versioning
- changelogs
- packaging
- release workflows
- release notes

These indicate maturity but are not used to determine repository ranking.

---

# Planned GitHub Integration

GitHub metadata is enrichment, not the primary data source.

The collector should remain useful without network access.

---

# Planned GraphQL Strategy

GraphQL usage must be rate-limit aware.

Required capabilities:

- inspect current rate limit status
- cache responses
- avoid duplicate queries
- support incremental refresh
- support retry-after behavior

GraphQL should only be queried when information cannot be obtained locally.

Examples:

- stars
- watchers
- issues
- pull requests
- repository metadata

---

# Planned Output Evolution

The current CLI emits JSON to standard output. No output filename is currently part of the public contract.

M1 schema consolidation will decide whether output remains streamed JSON or gains an explicit file sink. The names `repo-profile.json` and `portfolio-profile.json` are planned possibilities, not current contracts.

No ranking is performed by the Pre-Collector.

The output represents factual evidence only.

---

## Planned Future Stages

## Evidence Classification

Transform evidence into capability statements.

Examples:

- demonstrates .NET development
- demonstrates release engineering
- demonstrates governance
- demonstrates architecture

## Portfolio Analysis

Examples:

- strongest architecture repository
- strongest documentation repository
- strongest DevOps repository
- closest to prototype release

## CV Analysis

Map evidence to target roles.

Examples:

- software developer
- senior developer
- solution architect
- technical lead

The Pre-Collector remains role-neutral and evidence-focused.

## Implemented Repository Discovery Contract

`portfolio-profiler discover ROOT` examines `ROOT` and its direct child directories. It recognizes `.git` as either a file or directory and returns deterministically ordered repository identities.

Repository discovery uses filesystem markers only and may report paths that `profile` later rejects. Discovery is intentionally cheaper than Git validation.

## Implemented Local Git Evidence Contract
`portfolio-profiler profile REPOSITORY` resolves the repository root and observes local Git state through one non-shell command adapter. It performs no fetch and does not modify the repository. Evidence models are immutable, factual, and explicitly serialized. Root commit identities are sorted, detached HEAD is represented by a null branch and `detachedHead: true`, and unchanged repository state produces identical JSON bytes.
