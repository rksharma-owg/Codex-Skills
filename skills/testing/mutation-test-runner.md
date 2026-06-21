---
id: mutation-test-runner
name: Mutation Test Runner
category: testing
difficulty: Advanced
tags:
  - mutmut
  - stryker
  - testing
summary: |
  This Codex skill runs mutation testing on a codebase to evaluate test suite quality: introduces small code mutations (change + to -, remove null check, flip boolean), runs the test suite, and reports the mutation score (percentage of mutations caught by tests).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill runs mutation testing on a codebase to evaluate test suite quality: introduces small code mutations (change + to -, remove null check, flip boolean), runs the test suite, and reports the mutation score (percentage of mutations caught by tests).

## When to Use

Use when evaluating test suite quality, before refactoring critical code, after a bug escaped to production (indicating weak tests), or as part of a quality initiative.

## Codex Instructions

1. Choose the mutation testing tool for the language: Stryker (JS/TS), mutmut (Python), PIT (Java), go-mutesting (Go).
2. Identify the target scope: a critical module, a recently refactored area, or the whole codebase (slow).
3. Configure the tool: mutators to apply (arithmetic, boundary, conditional, return value), timeout per mutant.
4. Run the mutation test; this is slow — schedule accordingly.
5. Analyze the results: mutation score, surviving mutants, killed mutants, timeout mutants.
6. For each surviving mutant, add a test that would have killed it — this improves the test suite.
7. For each timeout mutant, investigate whether the mutant caused an infinite loop (a sign of fragile code).
8. Set a mutation score threshold (e.g., 70%) below which CI fails — but only on critical modules to avoid blocking all PRs.
9. Output the mutation report and the test improvements that kill surviving mutants.

## Inputs Needed

- Target codebase or module
- Language and mutation tool
- Existing test suite (with coverage)
- Acceptable mutation score threshold
- CI time budget (mutation testing is slow)

## Expected Output

A Markdown report titled 'Mutation Testing Report' with: (1) Mutation Score per module; (2) Surviving Mutants with the mutation and the test that would kill it; (3) Test Improvements diff; (4) CI Integration recommendation.

## Example Prompt

> Run mutation testing on src/billing/ in this TypeScript project using Stryker. Target 70% mutation score. For each surviving mutant, propose a test improvement. Recommend a CI integration that runs Stryker on the billing module for every PR.

## Safety Rules

- Never run mutation testing on production code paths that may be affected — it mutates source files in place temporarily.
- Do not block all PRs on mutation score — only critical modules.
- Stop and ask the user if a surviving mutant reveals a real bug (it often does).
- If the mutation run takes > 1 hour, scope it down to a smaller module.
- Never commit a mutation — the tool reverts, but verify with git status after the run.
- If the test improvements themselves reveal a misunderstanding of the contract, escalate to the user.
