# Current State

## Authority

This document records the durable implemented baseline represented by the source carrier used to prepare this documentation change. Until the change is merged into `master`, the new and changed documents remain candidate state rather than authoritative repository state.

Volatile branch, issue, pull-request, check, milestone, conflict, and merge state belongs in pull-request reconciliation evidence. It is not maintained here as durable product state.

## Product boundary

Portfolio Profiler is a Python repository-intelligence tool for discovering, profiling, and comparing repositories in a personal portfolio.

The product progression is:

```text
Repository
    -> Pre-Collector
    -> Evidence profiles
    -> Evidence classification
    -> Portfolio analysis
    -> CV recommendations
```

The Pre-Collector gathers facts. It does not decide repository importance, CV relevance, hiring value, maturity, capability, or rank.

## Implemented repository surface

The source carrier contains:

- Python 3.11+ package metadata using Hatchling;
- package version `0.1.0`;
- a `portfolio-profiler` console entry point;
- pytest test dependencies;
- immutable repository, Git, and composed profile models;
- deterministic direct-child repository discovery;
- deterministic local Git evidence collection;
- explicit profile composition;
- governance, contribution, coding, and documentation guidance;
- focused discovery, Git collector, and CLI tests.

## Implemented commands

```bash
portfolio-profiler discover ROOT
portfolio-profiler profile REPOSITORY
```

Successful commands emit indented JSON with sorted keys and a final newline to standard output.

The implemented CLI uses:

```text
0  successful collection
2  invalid input or CLI-level value and operating-system errors
3  Git unavailable or Git evidence collection failure
```

## Implemented discovery contract

Repository discovery:

- accepts `str` or `Path`;
- expands `~`;
- resolves the search root;
- requires a directory;
- examines the root and its direct child directories;
- recognizes `.git` as either a directory or file;
- returns an immutable tuple;
- sorts by repository name and path;
- does not recurse below direct children.

Discovery uses filesystem markers only. A stale `.git` file or another marker that Git cannot validate may be discovered and later rejected by `profile`. This is intentional: discovery is a cheap filesystem observation, while profiling uses Git as the authoritative validation boundary.

## Implemented Git evidence

The profile schema is `1.0` and contains repository identity plus:

```text
currentCommit
rootCommits
branch
detachedHead
dirty
trackedFileCount
commitCount
```

The Git collector:

- accepts the repository root or a directory inside a repository;
- resolves the top-level repository through local Git;
- invokes Git without a shell;
- performs no fetch or network operation;
- represents detached HEAD as `branch: null` and `detachedHead: true`;
- sorts multiple root commits;
- counts NUL-delimited tracked paths;
- observes tracked and untracked working-tree changes;
- fails explicitly when Git is unavailable, the path is invalid, or valid HEAD evidence cannot be collected.

## Implemented tests

The source carrier tests:

- direct-child discovery and stable ordering;
- root repository detection;
- `.git` directory and file markers;
- home expansion;
- stable discovery JSON;
- stable profile output for unchanged state;
- current commit and root commits;
- multiple sorted roots;
- branch and detached HEAD;
- clean and dirty states;
- string and relative input paths;
- missing, file, non-repository, and empty-repository failures;
- missing Git;
- nonzero Git exits;
- corrupt-repository failure classification;
- CLI exit behavior.

## Output boundary

The implemented CLI streams JSON to standard output. The names `repo-profile.json` and `portfolio-profile.json` are not current output contracts. M1 schema consolidation will decide whether file-writing behavior is introduced or standard-output streaming remains the only public output boundary.

## Portability boundary

Python 3.11 or later is declared. Supported operating systems and Git versions have not yet been established. No broader support claim is made until the validation-automation issue defines and verifies a support matrix.

## Remote-state boundary

A repository script that contains GitHub CLI commands is evidence of intended automation only. It does not prove that an issue, milestone, pull request, check, or merge exists.

The documentation pull request must record reconciliation evidence for:

```bash
git status --short
git branch --show-current
git log --oneline --decorate -10
git diff --stat master...HEAD
git diff --check master...HEAD
gh pr list --repo ulfbou/portfolio-profiler --state all
gh issue list --repo ulfbou/portfolio-profiler --state all
```

Verified remote identifiers belong in the pull-request body unless they have lasting architectural or historical value.
