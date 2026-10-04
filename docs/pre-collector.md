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
    â†“
Collectors
    â†“
Evidence Model
    â†“
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

# Evidence Categories

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
- section count
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
- documentation density

---

## Technology Analysis

Detect:

### .NET

- solution files
- project files
- target frameworks
- package management

Particular attention should be given to:

```text
net10.0
```

as this represents the most mature project family currently expected within the portfolio.

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

# GitHub Integration

GitHub metadata is enrichment, not the primary data source.

The collector should remain useful without network access.

---

# GraphQL Strategy

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

# Outputs

Each repository produces:

```text
repo-profile.json
```

The portfolio produces:

```text
portfolio-profile.json
```

No ranking is performed by the Pre-Collector.

The output represents factual evidence only.

---

# Future Stages

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