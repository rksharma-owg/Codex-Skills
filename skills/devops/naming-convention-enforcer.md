---
id: naming-convention-enforcer
name: Naming Convention Enforcer
category: devops
difficulty: Intermediate
tags:
  - devops
  - jest
summary: |
  This Codex skill audits identifiers against the project's naming conventions and produces safe-rename patches: variables (camelCase vs snake_case), constants (UPPER_SNAKE), private members (leading underscore), boolean predicates (is/has/can prefix), interface names (no leading I unless configured), and test files (*.test.ts, *_test.go).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits identifiers against the project's naming conventions and produces safe-rename patches: variables (camelCase vs snake_case), constants (UPPER_SNAKE), private members (leading underscore), boolean predicates (is/has/can prefix), interface names (no leading I unless configured), and test files (*.test.ts, *_test.go).

## When to Use

Use when onboarding a new team member, before publishing a library's public API, when introducing a linter to a legacy codebase, or after merging two codebases with different conventions.

## Codex Instructions

1. Read the project's naming convention spec (could be in CONTRIBUTING.md, .editorconfig, or eslint config).
2. For each identifier, classify it: variable, constant, private member, public method, interface, type, enum, file, test file.
3. Verify the casing matches the convention for its class.
4. Verify boolean predicates use the agreed prefix (is, has, can, should) to improve readability at call sites.
5. Verify interface names follow the project's convention (no leading I in TypeScript by default, leading I in C# by default).
6. Verify test files match the test runner's pattern (*.test.ts for Jest, *_test.go for Go).
7. For each violation, compute a safe rename: same scope, no shadowing, no public API breakage.
8. Use the language's rename refactoring tool (gopls, tsserver, rope) to ensure all references are updated.
9. Run the test suite after each rename to confirm no regressions.
10. Output a rename report and a patch; flag any rename that would break the public API of a published library.

## Inputs Needed

- Repository path
- Naming convention spec (file path or inline)
- Language and rename tool available (tsserver, gopls, rope, jdtls)
- Whether the package is published (affects public API breakage tolerance)
- Test suite path

## Expected Output

A Markdown report titled 'Naming Convention Audit' with: (1) Violations table — Identifier | Type | Current | Convention-Compliant | Public API?; (2) Patch Diff with renames; (3) Test Run Output; (4) Breaking Change List for any renames that affect published APIs.

## Example Prompt

> Enforce naming conventions in this TypeScript project. camelCase for variables and functions, PascalCase for types and interfaces (no leading I), UPPER_SNAKE for constants, is/has prefix for booleans. Use tsserver to rename. Don't break the published exports in src/index.ts.

## Safety Rules

- Never rename a published public API symbol without a major version bump and a deprecation path.
- Do not rename test fixtures or snapshot files in a way that breaks CI.
- Stop and ask the user if a rename collides with a reserved keyword or a builtin.
- Never rename database columns or table names via this skill — that requires a migration.
- If a rename crosses module boundaries and the project uses a DI container, verify the binding key is updated.
- Do not auto-rename if the test suite is red before the rename — fix the tests first.
