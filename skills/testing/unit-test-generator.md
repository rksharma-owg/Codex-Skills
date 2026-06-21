---
id: unit-test-generator
name: Unit Test Generator
category: testing
difficulty: Beginner
tags:
  - jest
  - junit
  - pytest
  - testing
summary: |
  This Codex skill generates unit tests for a target function or class: identifies branches, generates inputs that cover each branch (including edge cases), asserts on the contract (return value, side effects, exceptions), and produces a test file ready to run.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates unit tests for a target function or class: identifies branches, generates inputs that cover each branch (including edge cases), asserts on the contract (return value, side effects, exceptions), and produces a test file ready to run.

## When to Use

Use when adding tests to legacy code, before refactoring a function without tests, when increasing coverage on a critical module, or as part of TDD when the user provides the function signature.

## Codex Instructions

1. Read the target function or class and identify its public contract: inputs, outputs, exceptions, side effects.
2. Identify branches: each if/else, each case in a switch, each loop with a break, each exception throw.
3. Generate test cases that cover each branch: at least one test per branch, plus edge cases (empty, null, boundary values).
4. Generate property-based tests for functions with invariants (e.g., sort returns the same elements).
5. Mock external dependencies: database, HTTP, filesystem, clock — use the project's mocking framework.
6. Assert on the return value AND side effects (function called with expected args, state mutated correctly).
7. Name tests descriptively: test_<function>_<scenario>_<expectedOutcome>.
8. Run the tests and ensure they pass; if a test fails, fix the test or surface a bug.
9. Compute coverage before and after; flag any uncovered branches.
10. Output the test file and a coverage delta report.

## Inputs Needed

- Target function or class path
- Test framework (Jest, pytest, Go testing, JUnit)
- Mocking framework (unittest.mock, jest.mock, testify-mock)
- Coverage tool (coverage.py, jest --coverage, go test -cover)
- Existing tests to extend (or 'none' for new file)

## Expected Output

A test file in the project's framework with descriptive test names, branch coverage, edge cases, and proper mocking. Plus a coverage delta report showing before/after.

## Example Prompt

> Generate unit tests for src/billing/calculateRefund.ts in this Jest project. Cover every branch, edge cases (zero amount, negative amount, full refund, partial refund), and mock the database call. Run the tests and report coverage delta.

## Safety Rules

- Never generate tests that hit real databases or external APIs — always mock.
- Do not weaken assertions to make a test pass — fix the bug or document the gap.
- Stop and ask the user if a function's contract is ambiguous.
- If a generated test fails, investigate before deleting it — it may have found a real bug.
- Never commit tests with hardcoded credentials or PII.
- If the function is part of a regulated module, verify the tests cover the compliance scenarios.
