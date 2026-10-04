# Contributing to Portfolio Profiler

Portfolio Profiler collects repository evidence and portfolio intelligence.

## Principles

- Evidence before scoring.
- Claim-code parity.
- Conventional Commits.
- PR-only changes to `master` after bootstrap.
- No unverifiable claims.
- Deterministic collection where practical.
- Respect API and GraphQL rate limits when remote integration exists.

## Required standards

- Follow `docs/coding-standards.md`.
- Follow `docs/documentation-standards.md`.
- Use `docs/acceptance-ready.md` before implementation begins.
- Use `docs/definition-of-done.md` before claiming completion.
- Keep implementation, tests, documentation, and CLI behavior aligned.

## Canonical local validation

```bash
python3 -m pip install -e '.[test]'
python3 -m pytest
python3 -m compileall -q src tests
git diff --check
```

Issues may require additional validation. Pull requests must record the commands actually executed and their results.
