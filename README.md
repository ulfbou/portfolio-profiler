# Portfolio Profiler

Portfolio Profiler is a Python-based repository intelligence tool that discovers, profiles, and compares software repositories within a personal portfolio.

Its first implementation phase is the Pre-Collector, which gathers objective repository evidence for later classification, portfolio analysis, and CV recommendations.

## Status

Implementation in progress. The current durable baseline is described in `docs/current-state.md`; planned delivery is described in `docs/roadmap.md`.

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

## Planned evidence areas

- README evidence;
- documentation evidence;
- Python and .NET project structure;
- testing assets;
- DevOps assets;
- governance assets;
- release-readiness indicators;
- rate-limit-aware GitHub enrichment.

See `docs/roadmap.md` for sequencing and milestone gates.
