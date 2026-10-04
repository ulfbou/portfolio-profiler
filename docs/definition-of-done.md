# Definition of Done

## Purpose

This Definition of Done applies to Portfolio Profiler changes unless a stricter issue-specific gate exists.

A change is complete only when every applicable requirement has executable evidence. Non-applicable requirements must be recorded with a reason.

## Acceptance

- [ ] Every issue acceptance criterion has executable evidence.
- [ ] The proof target is satisfied.
- [ ] In-scope work is complete.
- [ ] Deferred work is explicit.
- [ ] No unsupported completion claim is present.

## Behavior and regression

- [ ] Existing public commands retain their documented behavior unless the issue explicitly changes it.
- [ ] Existing schema guarantees are preserved or intentionally versioned.
- [ ] Deterministic behavior is tested where promised.
- [ ] Missing and malformed evidence are handled according to contract.
- [ ] Collectors remain factual and role-neutral.
- [ ] No analyzed repository is modified unless the issue explicitly authorizes mutation.
- [ ] No network dependency is introduced outside explicit scope.

## Tests and validation

- [ ] The complete test suite passes.
- [ ] New public behavior has focused automated tests.
- [ ] Failure behavior has automated tests.
- [ ] Regression tests cover preserved guarantees.
- [ ] Python compilation succeeds.
- [ ] `git diff --check` succeeds.
- [ ] Validation leaves the repository in the expected state.

Minimum local sequence:

```bash
python3 -m pip install -e '.[test]'
python3 -m pytest
python3 -m compileall -q src tests
git diff --check
```

Additional commands required by the issue must be executed and recorded.

## Models and schema

- [ ] Public models are type annotated.
- [ ] Evidence models are immutable where practical.
- [ ] Serialization is explicit.
- [ ] Every emitted field has an implemented and tested source.
- [ ] No placeholder future section is emitted.
- [ ] Collection ordering is deterministic.
- [ ] Schema version impact is documented.

## Errors and diagnostics

- [ ] Expected failures use product errors where callers require stable handling.
- [ ] CLI exit behavior matches documentation.
- [ ] Diagnostics are concise and do not expose secrets.
- [ ] Low-level failures are translated without hiding actionable evidence.

## Documentation

- [ ] README entry points are accurate.
- [ ] Architecture and design documentation match implementation.
- [ ] Facts and recommendations are distinguishable.
- [ ] Commands are copyable.
- [ ] Paths are repository-relative where appropriate.
- [ ] GraphQL or other remote behavior is documented only when implemented.
- [ ] Normative requirements have one clear authority.

## Dependencies, security, and portability

- [ ] New dependencies are necessary and declared.
- [ ] File traversal has explicit safety boundaries where applicable.
- [ ] Symlink behavior is tested where applicable.
- [ ] Remote integration is rate-limit-aware, cached, and secret-safe where applicable.
- [ ] Platform support claims are backed by validation.

## Governance

- [ ] The pull request links its issue.
- [ ] The issue and pull request use the intended milestone.
- [ ] Required labels are applied.
- [ ] The pull-request title follows Conventional Commits.
- [ ] The pull-request body records commands actually executed.
- [ ] Regression review identifies preserved guarantees.
- [ ] Deferred work is listed.

## Completion result

Use one result:

```text
DONE
NOT DONE: <specific unmet requirement>
```

`DONE` means the change has passed the applicable implementation, evidence, documentation, regression, and governance gates. It does not by itself prove that a pull request has been merged or released.
