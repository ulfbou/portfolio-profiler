# Coding Standards

## Core Principles
1. Readability is part of correctness.
2. Evidence collectors must produce reproducible results.
3. Local repository analysis is preferred over remote API calls.
4. GitHub API usage must be cached and rate-limit aware.
5. Public behavior must be tested.

## Python
- Python 3.11+.
- Type annotate public APIs.
- Use dataclasses for portfolio models.
- Prefer immutable data structures.
- Keep collection, analysis and reporting separated.

## Collectors
- Collect facts, not opinions.
- Do not assign CV scores in collectors.
- Preserve provenance for collected evidence.