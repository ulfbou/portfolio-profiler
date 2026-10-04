# Portfolio Profiler

Portfolio Profiler is a Python-based repository intelligence tool that discovers, profiles, and compares software repositories within a personal portfolio.

Its primary purpose is to collect objective evidence from repositories and transform that evidence into actionable portfolio insights.

The first implementation phase is the Pre-Collector.

## Goals

- Discover repositories and portfolio assets.
- Collect objective repository evidence.
- Avoid subjective scoring during collection.
- Produce structured evidence profiles.
- Support future CV, portfolio, and interview-oriented analysis.

## Design Principles

- Evidence before scoring.
- Local analysis before API analysis.
- Deterministic and reproducible collection.
- Rate-limit-aware GitHub integration.
- Structured machine-readable outputs.

## Initial Evidence Areas

- Repository metadata
- Git activity
- README analysis
- Documentation analysis
- .NET solution structure
- Python project structure
- Testing assets
- DevOps assets
- Governance assets
- Release readiness signals

## Output

The Pre-Collector produces repository profiles that can later be consumed by higher-level portfolio analysis and CV recommendation systems.

## Status

Planned.

## Local Git Profile
Collect deterministic local Git evidence without network access:
```bash
portfolio-profiler profile REPOSITORY
```
The versioned JSON profile contains repository identity, current and root commit identities, branch or detached-HEAD state, working-tree cleanliness, tracked-file count, and reachable commit count. Invalid repository input exits with status 2; unavailable Git or collection failure exits with status 3.
