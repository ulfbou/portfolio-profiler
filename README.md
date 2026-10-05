# Portfolio Profiler

Portfolio Profiler is a Python-based repository intelligence tool that discovers, profiles, and compares software repositories within a personal portfolio.

Its primary purpose is to collect objective evidence from repositories and transform that evidence into actionable portfolio insights.

Its first implementation phase is the Pre-Collector, which gathers objective repository evidence for later classification, portfolio analysis, and CV recommendations.

## Status

Implementation in progress. The current durable baseline is described in `docs/current-state.md`; planned delivery is described in `docs/roadmap.md`.

## Goals

- Discover repositories and portfolio assets.
- Collect objective repository evidence.
- Avoid subjective scoring during collection.
- Produce structured evidence profiles.
- Support future CV, portfolio, and interview-oriented analysis.

## Implemented commands

### Discover repositories

```bash
portfolio-profiler discover ROOT
```

Discovers Git repository markers at `ROOT` and among its direct child directories. Discovery is a filesystem observation and does not fully validate each marker through Git.

### Profile one repository

```bash
portfolio-profiler profile REPOSITORY
```

Resolves and validates the containing local Git repository, then emits repository identity and deterministic local Git evidence as JSON to standard output.

The profile currently includes current and root commit identities, branch or detached-HEAD state, working-tree cleanliness, tracked-file count, and reachable commit count.

Invalid repository input exits with status 2. Git unavailability or Git evidence collection failure exits with status 3.

## Design principles

- Evidence before scoring.
- Local analysis before API analysis.
- Deterministic and reproducible collection.
- Structured machine-readable output.
- Collectors gather facts rather than opinions.
- Classification, ranking, and CV interpretation remain downstream.

## Evidence areas

Portfolio Profiler covers the following evidence areas:

- repository metadata;
- Git activity;
- README analysis;
- documentation analysis;
- .NET solution structure;
- Python project structure;
- testing assets;
- DevOps assets;
- governance assets;
- release-readiness signals.

Repository identity and local Git evidence are partially implemented. The remaining evidence areas and GitHub enrichment are planned.

## Output

The Pre-Collector produces structured repository profiles that can later be consumed by evidence classification, portfolio analysis, and CV recommendation systems.

The currently implemented commands emit JSON to standard output. No output filename is currently part of the public contract.

See `docs/roadmap.md` for sequencing and milestone gates.
