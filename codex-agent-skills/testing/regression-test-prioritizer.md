# Regression Test Prioritizer

## Purpose

This Codex skill analyzes a PR diff and selects the subset of existing tests most likely to catch regressions caused by this change. It reduces CI time by running only relevant tests on a PR while running the full suite nightly.

## When to Use

Use when CI time exceeds 15 minutes, when the test suite is too large to run on every PR, or as part of a test impact analysis initiative.

## Codex Instructions

1. Build a coverage map: for each test, which source files does it cover? Use coverage data from a recent full run.
2. For a PR diff, identify the changed source files.
3. Look up the tests that cover the changed files; this is the impacted test set.
4. Add tests that cover the changed files' direct dependents (callers) — changes can break callers.
5. Add tests marked as 'smoke' or 'critical' regardless of coverage — always run these.
6. Run the impacted set on the PR; run the full suite nightly.
7. Track the false-negative rate: did any nightly run catch a regression that the impacted set missed? If so, refine the coverage map.
8. Output the impacted test list for the PR and the CI integration snippet.
9. Recommend a tool: Testsplit (commercial), pytest-testmon (Python), Jest --findRelatedTests (JS).
10. Document the trade-off: faster CI vs slightly higher risk of a missed regression.

## Inputs Needed

- PR diff (changed files)
- Coverage map (test -> source files) from a recent full run
- Test framework
- CI time budget
- Smoke/critical test list

## Expected Output

An impacted test list for the PR, a CI integration snippet that runs only these tests, and a nightly job spec for the full suite.

## Example Prompt

> Prioritize tests for PR #678 in this Python/pytest project. The PR changes src/billing/refunds.py and src/billing/credits.py. Use the coverage map from last night's full run to identify impacted tests. Add the smoke tests in tests/smoke/. Run only impacted tests on the PR, full suite nightly.

## Safety Rules

- Never skip the smoke tests — always run them on every PR.
- Do not disable the nightly full suite — it catches what the impacted set misses.
- Stop and ask the user if the coverage map is stale (> 7 days old).
- If a nightly run catches a regression that the impacted set missed, add the missed test to the impacted set for similar future changes.
- Never exclude a test from the impacted set just to speed up CI — verify it is truly unrelated.
- If the project has flaky tests, fix the flakiness before relying on prioritization — flaky tests make coverage maps unreliable.
