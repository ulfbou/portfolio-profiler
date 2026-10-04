# Portfolio Profiler Roadmap

## Purpose

This roadmap advances Portfolio Profiler from deterministic local repository evidence to evidence-backed portfolio and CV recommendations.

The governing sequence is:

```text
Local repository discovery
    -> Objective repository evidence
    -> Evidence classification
    -> Portfolio intelligence
    -> Role-oriented CV recommendations
```

Collectors remain factual and role-neutral. Classification, comparison, ranking, and CV interpretation remain downstream.

## Delivery principles

1. Collect evidence before scoring.
2. Prefer local evidence before remote enrichment.
3. Preserve deterministic output for unchanged input state.
4. Keep provenance sufficient to audit public claims.
5. Add schema fields only when their collectors exist.
6. Keep implementation, tests, documentation, and CLI behavior aligned.
7. Treat GitHub metadata as enrichment rather than the primary source.
8. Do not claim completion without executable evidence.
9. Separate missing evidence from negative evidence.
10. Avoid speculative frameworks until two or more concrete consumers justify them.

## Phase 0: Current-state stabilization

### Outcome

Establish a validated and documented baseline before introducing another collector.

### Work

- identify the controlling branch and its relationship to `master`;
- determine the actual issue, pull-request, check, and merge state;
- resolve any remaining `docs/pre-collector.md` conflict;
- execute the complete local validation sequence;
- update README status to a factual implemented-state description;
- document both implemented commands;
- distinguish current behavior from future plans;
- resolve or explicitly retain the M2 naming discrepancy;
- ensure no completed Git work is recreated as planned work.

### Validation

```bash
python3 -m pip install -e '.[test]'
python3 -m pytest
python3 -m compileall -q src tests
git diff --check
portfolio-profiler discover ..
portfolio-profiler profile .
```

### Exit criteria

- controlling repository and remote state are evidenced;
- all tests pass;
- compilation succeeds;
- diff checking succeeds;
- both public commands execute successfully against valid inputs;
- documented fields and exit behavior match implementation;
- no network access or repository mutation occurs during local profiling;
- documentation does not present GraphQL or other future collectors as implemented.

## M1: Pre-Collector Foundation

### Outcome

Discover local repositories and produce deterministic factual local profiles without a required network connection.

### Implemented baseline

- direct-child repository discovery;
- immutable repository identity;
- local Git evidence;
- composed schema `1.0` profile;
- deterministic JSON;
- explicit product errors;
- discovery, collector, and CLI tests.

### Remaining delivery

1. current-state stabilization;
2. README evidence;
3. documentation evidence;
4. local evidence schema consolidation;
5. checked-in validation automation;
6. first prototype release decision.

### M1 exit criteria

- discovery, Git, README, and documentation evidence are implemented and documented;
- every emitted field has an implemented collector and tests;
- unchanged repository state produces stable output;
- the complete test suite passes in a clean environment;
- one checked-in validation sequence protects pull requests;
- no scoring, classification, ranking, or CV logic exists in collectors;
- the package can be built and exercised from its built artifact;
- prototype release versioning is explicitly decided.

## M1.1: README evidence

### Proof target

Given a repository, Portfolio Profiler emits deterministic factual evidence about its selected root README without assessing quality, importance, or CV value.

### Required decisions

- recognized README filename variants;
- root-only search boundary;
- deterministic selection when multiple candidates exist;
- text decoding and malformed-input behavior;
- heading and fenced-code-block counting rules;
- topic-marker rules;
- source-path provenance.

### In scope

- existence;
- selected repository-relative path;
- byte size;
- line count;
- heading count;
- fenced code-block count;
- explicitly defined topic markers;
- deterministic serialization;
- focused tests;
- profile, CLI, README, and pre-collector alignment.

### Out of scope

- prose-quality scoring;
- generated improvement advice;
- general documentation scanning;
- repository ranking;
- CV conclusions.

### Exit criteria

- absence and ambiguity are represented explicitly;
- candidate selection and counts are deterministic and tested;
- provenance identifies the selected file;
- no subjective score is emitted;
- existing discovery and Git behavior remain unchanged.

## M1.2: Documentation evidence

### Proof target

Given a repository, Portfolio Profiler deterministically inventories supported documentation assets without evaluating author quality or repository maturity.

### Required decisions

- supported roots such as `docs/`, `adr/`, `specifications/`, and `architecture/`;
- supported extensions;
- symlink policy;
- excluded generated and dependency directories;
- inaccessible-path behavior;
- category precedence;
- safety limits for files and traversal.

### In scope

- normalized repository-relative paths;
- file counts by explicit category;
- deterministic ordering;
- source provenance;
- tests for absent roots, nested paths, mixed case, and symlinks;
- profile and documentation alignment.

### Exit criteria

- inventory rules are explicit and tested;
- README evidence is not unintentionally double-counted;
- missing documentation remains a fact rather than a maturity judgment;
- no documentation-quality score is emitted.

## M1.3: Local schema consolidation

### Outcome

Compose every completed local collector into one versioned profile without placeholder sections.

### Required decisions

- whether adding evidence preserves schema `1.0` compatibility or requires a version increment;
- omission versus `null` semantics;
- field and collection naming conventions;
- deterministic collection ordering;
- unsupported-version behavior;
- canonical example documents.

### Exit criteria

- every field has an implemented source and test;
- future empty sections are absent;
- schema compatibility is intentional and documented;
- serialization remains deterministic;
- canonical examples are test fixtures rather than unverified prose.

## M1.4: Validation automation and prototype release

### Outcome

Pull requests and release candidates execute the same checked-in validation sequence.

### Minimum gate

```bash
python3 -m pip install -e '.[test]'
python3 -m pytest
python3 -m compileall -q src tests
git diff --check
```

### Additional release checks

- build package artifacts;
- install the built artifact in isolation;
- exercise CLI help and both implemented commands;
- verify package metadata and `__version__` consistency;
- verify the repository remains clean after validation.

### Version decision

The package declares `0.1.0`; governance defines prototype releases as `v0.x.y`. The release issue must establish whether `0.1.0` is unreleased metadata or the first prototype release.

## M2: Repository Evidence

### Outcome

Expand factual local profiles to engineering assets and release indicators.

The controlling milestone name is `M2 Repository Evidence`. GitHub enrichment is an M2 workstream. Evidence classification is the entry stage of M3 Portfolio Intelligence.

### Workstreams

1. Python project evidence;
2. .NET project evidence;
3. testing evidence;
4. DevOps evidence;
5. governance evidence;
6. release-readiness evidence;
7. build metadata.

### Python evidence

Candidate facts:

- `pyproject.toml` and recognized requirements or lock files;
- declared build backend;
- package roots;
- console entry points;
- declared Python requirement;
- dependency groups;
- recognized test directories.

Declarations must not be presented as runtime truth.

### .NET evidence

Candidate facts:

- solution and project files;
- target frameworks;
- project and package references;
- central package management;
- test-project indicators;
- shared build-property files.

Target frameworks are facts. Framework maturity is not a collector output.

### Testing evidence

Candidate facts:

- test directories and files;
- declared test dependencies;
- recognized framework markers;
- coverage configuration;
- test-project configuration.

Presence is evidence; completeness and quality are later analytical concerns.

### DevOps evidence

Candidate facts:

- GitHub workflows;
- Azure Pipelines definitions;
- build, validation, packaging, and release scripts;
- triggers;
- declared runtime versions;
- jobs and steps.

Workflow classification requires explicit rules and must not imply successful execution.

### Governance evidence

Candidate facts:

- contribution guidance;
- CODEOWNERS;
- issue and pull-request templates;
- governance documents;
- architecture-decision records;
- security and support policies;
- documented branch and release conventions.

Documented policy must remain distinguishable from observed enforcement.

### Release-readiness evidence

Candidate facts:

- version declarations;
- changelogs and release notes;
- local tags;
- packaging configuration;
- release workflows;
- artifact configuration;
- version consistency.

These are factual indicators, not a release-readiness score.

### M2 exit criteria

- supported collectors have explicit, tested contracts;
- provenance identifies authoritative sources;
- absent, malformed, and unsupported evidence are distinguishable;
- unsupported ecosystems are absent rather than represented by invented data;
- deterministic output is preserved;
- collectors remain factual and role-neutral.

### GitHub enrichment

#### Entry condition

Principal local collectors and the aggregate schema are stable.

#### Outcome

Enrich local profiles with evidence unavailable locally while preserving offline usefulness.

#### Candidate evidence

- repository metadata;
- stars and watchers;
- issues and pull requests;
- selected collaboration metadata;
- remote governance settings when explicitly supported.

#### Required architecture

- remote-source boundary;
- authenticated and unauthenticated behavior;
- cache keys and expiry;
- rate-limit observation;
- duplicate-query avoidance;
- incremental refresh;
- retry-after handling;
- partial-result policy;
- local-versus-remote provenance;
- fixtures that do not require live GitHub access;
- secret-safe diagnostics.

#### Exit criteria

- local profiling remains useful offline;
- remote failure does not corrupt local evidence;
- cached and live data are distinguishable;
- API use is limited to required evidence;
- rate-limit behavior is documented and tested.

## M3: Portfolio Intelligence

### Outcome

Transform evidence into explainable capability statements and compare repository profiles without changing collected facts.

### Evidence classification

Classification is the entry stage of M3, not a separate milestone.

#### Requirements

- versioned and reviewable rules;
- evidence references for every statement;
- explicit handling of missing evidence;
- deterministic results;
- separation from collector code.

Candidate capability statements include evidence of:

- .NET development;
- Python development;
- release engineering;
- governance;
- architecture;
- testing and validation practices.

### Portfolio analysis requirements

- load and validate multiple profiles;
- handle schema compatibility explicitly;
- identify duplicate repositories;
- represent profile freshness;
- compare evidence breadth through declared rules;
- handle ties deterministically;
- emit machine-readable results;
- render human-reviewable findings.

### M3 exit criteria

- every classification and comparison is traceable to evidence;
- missing evidence is not treated as negative evidence;
- no unsupported attribution of personal ability is produced;
- output is reproducible for unchanged profiles and rules.

## M4: CV Relevance

### Outcome

Map portfolio evidence and classifications to an explicitly selected target role.

### Candidate roles

- software developer;
- senior developer;
- solution architect;
- technical lead.

### In scope

- suggest repositories to feature;
- identify evidence-backed talking points;
- map evidence to explicit role requirements;
- identify evidence gaps;
- distinguish demonstrated evidence from recommended future work.

### Safeguards

- recommendations remain reviewable suggestions;
- factual evidence remains immutable;
- every recommendation includes its evidence basis;
- no experience or capability is fabricated;
- missing evidence is not presented as proof of missing skill;
- role mappings are explicit and versioned.

### M4 exit criteria

- target role is an explicit input;
- recommendations cite repositories and supporting evidence;
- users can inspect why each recommendation was produced;
- collection and classification outputs remain unchanged by presentation needs.

## Cross-cutting requirements

### Provenance

Introduce provenance proportionately when a collector needs it. It should identify:

- source file or command;
- local or remote origin;
- observed, declared, or derived status;
- producing collector version when required for auditability.

Do not introduce a generic provenance graph without concrete consumers.

### Schema evolution

Define:

- compatibility expectations;
- omission and `null` semantics;
- deterministic ordering;
- unknown-version behavior;
- canonical examples;
- version-change rules.

### Errors

Extend product errors only when callers need a distinct response. Do not build a speculative exception framework.

### Safety and performance

Before broad recursive scanning, define:

- excluded directories;
- symlink behavior;
- file-size and traversal limits;
- binary detection;
- inaccessible-path behavior;
- malformed-text behavior;
- bounded work;
- secret-safe diagnostics.

### Portability

Before broad support claims, establish and validate the supported operating-system, Python, and Git matrix.

## Delivery order

```text
Current-state stabilization
    -> README evidence
    -> Documentation evidence
    -> Local schema consolidation
    -> Validation automation
    -> M1 prototype release
    -> Python and .NET evidence
    -> Testing, DevOps, governance, and release evidence
    -> M2 complete
    -> GitHub enrichment
    -> Evidence classification
    -> Portfolio analysis
    -> CV recommendations
```

## Explicit deferrals

Until concrete need is demonstrated, defer:

- generic collector protocols;
- plugin architecture;
- service containers;
- dependency-injection frameworks;
- generic evidence base classes;
- speculative caching outside remote integration;
- unused future profile fields;
- contributor ranking and bus-factor estimates;
- maturity scores in collectors;
- autonomous CV claims.

## Roadmap authority and issue readiness

Roadmap acceptance establishes product boundaries, milestone outcomes, sequencing, and required decision points. It does not resolve every implementation contract.

M1.1 through M1.4 remain valid roadmap work while their implementation issues remain `BLOCKED` until they pass `docs/acceptance-ready.md`. Their issues must close filename, traversal, decoding, schema, provenance, error, safety, and portability decisions before implementation begins.

## Documentation PR merge bar

The following must be true before this roadmap documentation change merges:

- repository and remote state are reconciled and recorded in the pull-request body;
- candidate-state authority wording remains accurate until merge;
- milestone names match `docs/github-governance.md`;
- evidence classification is inside M3 Portfolio Intelligence;
- GitHub enrichment is inside M2 Repository Evidence;
- `docs/pre-collector.md` separates implemented and planned behavior;
- the `net10.0` maturity claim is removed;
- README `section count` terminology is replaced by `heading count`;
- undefined `documentation density` is removed;
- README status is factual and both implemented commands are documented;
- the canonical validation sequence is aligned across contributing guidance, the pull-request template, and the Definition of Done;
- absent operating-system and Git support contracts are disclosed rather than invented;
- discovery input failures use `RepositoryInputError`;
- the complete repository diff passes validation.

Merge into `master` is the authority boundary. Before merge, all changed documents remain candidate state.

## Follow-up issues

The documentation pull request does not need to complete these later decisions:

- rename a live GitHub milestone if reconciliation proves that its name conflicts with governance;
- add CI and decide the operating-system, Python, and Git support matrix;
- decide schema-version compatibility before README or documentation evidence issues become acceptance-ready;
- decide whether public output remains streamed JSON or gains an explicit file sink;
- close each M1.1 through M1.4 implementation contract through the acceptance-ready gate.
