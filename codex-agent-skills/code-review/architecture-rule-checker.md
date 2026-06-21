# Architecture Rule Checker

## Purpose

This Codex skill enforces architectural layering rules: domain layer must not depend on infrastructure, controllers must not call repositories directly, cross-module imports must go through declared public APIs, and cyclic dependencies between modules are forbidden. It complements linters by encoding team-specific architecture decisions as code.

## When to Use

Use when introducing architecture decision records (ADRs), after a refactor that restructures modules, before a major release to verify no architecture drift, or as a CI gate on PRs that touch cross-module code.

## Codex Instructions

1. Read the project's architecture rules (from ADRs, a dependency-cruiser config, an ArchUnit config, or a team doc).
2. Build the module dependency graph by parsing imports/requires for the target language.
3. Verify each rule: layer A must not import from layer B; module X must not import from module Y outside its public API; no cycles.
4. For each violation, capture the offending import statement, the source and target module, and the rule violated.
5. Distinguish between intentional exceptions (documented in the config) and true violations.
6. Rank violations by severity: cycle (high), layer bypass (high), cross-module non-public import (medium), naming violation (low).
7. Propose a fix for each violation: move the code to the correct layer, introduce a public API in the target module, or invert the dependency via an interface.
8. Output a violations report and a config snippet for the project's architecture rule tool (dependency-cruiser, ArchUnit, eslint-plugin-boundaries).
9. Flag any violation that cannot be auto-fixed without an architecture decision (e.g., introducing a new abstraction).
10. Suggest CI integration so the rules run on every PR.

## Inputs Needed

- Repository path
- Architecture rule spec (ADR folder, dependency-cruiser config, ArchUnit config)
- Language and module system
- Existing architecture tooling, if any
- Module boundary definitions (folders, package.json workspaces, Go modules)

## Expected Output

A Markdown report titled 'Architecture Rule Violations' with: (1) Module Dependency Graph summary; (2) Violations table — Rule | Source Module | Target Module | Severity | Fix; (3) Config Snippet for the architecture rule tool ready to commit; (4) CI Integration Steps.

## Example Prompt

> Check this TypeScript monorepo against our layering rules: domain must not import from infra, controllers must not import from repositories directly, no cross-module imports outside declared public APIs in src/index.ts. Use dependency-cruiser. Suggest CI integration with GitHub Actions.

## Safety Rules

- Never auto-apply architecture fixes that change public APIs without explicit user approval.
- Do not weaken architecture rules to 'fix' violations — propose the correct fix instead.
- Stop and ask the user if a module boundary is ambiguous (e.g., shared utilities).
- If a cycle requires an interface extraction across modules, document the proposed abstraction before patching.
- Never disable a rule globally to silence a violation — use a scoped exception with a justification comment.
- Do not modify the dependency-cruiser or ArchUnit config without showing the diff to the user.
