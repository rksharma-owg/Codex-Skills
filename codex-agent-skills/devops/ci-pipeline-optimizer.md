# CI Pipeline Optimizer

## Purpose

This Codex skill analyzes a CI pipeline (GitHub Actions, GitLab CI, CircleCI) and produces an optimization plan: caching strategy, parallelization, matrix pruning, conditional jobs, and step merging. The goal is to cut median CI time by 30-60% without sacrificing test coverage or safety.

## When to Use

Use when CI time exceeds 15 minutes, when developer throughput is dropping due to PR feedback latency, before adding a new job that risks pushing CI over the budget, or quarterly as part of engineering efficiency reviews.

## Codex Instructions

1. Parse the pipeline definition file (.github/workflows/*.yml, .gitlab-ci.yml, .circleci/config.yml).
2. Build a job dependency graph and identify the critical path — the longest sequential chain.
3. Identify cacheable steps: package manager downloads (npm, pip, maven), Docker layer cache, language build cache (.next, target/, build/).
4. Identify parallelizable jobs: matrix axes that can be split, independent test suites that can run concurrently.
5. Identify conditional jobs: jobs that always run but rarely produce useful output (e.g., a deploy job on every PR).
6. Identify redundant steps: repeated checkout, repeated dependency install, repeated lint across jobs.
7. Compute expected time savings for each optimization using historical CI run data if available.
8. Propose a new pipeline YAML that preserves all current coverage while applying the optimizations.
9. Verify the proposed pipeline against the platform's syntax validator (actionlint, gitlab-ci-lint).
10. Output a before/after comparison and a phased rollout plan to avoid a big-bang change.

## Inputs Needed

- Pipeline definition file path
- CI platform (GitHub Actions, GitLab CI, CircleCI, Jenkins)
- Historical CI run data or access to the CI dashboard
- Current median CI time and target
- Concurrency limits on the CI runner pool

## Expected Output

A Markdown report titled 'CI Pipeline Optimization' with: (1) Current State Analysis — critical path, cacheable steps, parallelizable jobs; (2) Proposed Pipeline YAML ready to commit; (3) Expected Savings table — Optimization | Time Saved (min) | Risk; (4) Phased Rollout Plan.

## Example Prompt

> Optimize .github/workflows/ci.yml in this repo. Current median run is 22 minutes, target is 10. We have 8 parallel runners. Identify cacheable steps, parallelizable jobs, and produce a new workflow YAML. Use actionlint to validate the syntax.

## Safety Rules

- Never disable a test job to 'optimize' — only parallelize or cache.
- Do not remove a security scan job (SAST, SCA, secret scan) without explicit user approval.
- Stop and ask the user if a conditional job is part of a compliance requirement.
- Never commit cache-busting changes without showing the diff to the user.
- If the optimization requires a paid CI feature (larger runners, more parallelism), flag the cost explicitly.
- Do not introduce a third-party action without verifying its maintainer and license.
