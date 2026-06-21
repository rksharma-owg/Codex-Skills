---
id: dangerous-function-replacer
name: Dangerous Function Replacer
category: secure-coding
difficulty: Intermediate
tags:
  - cwe
  - secure-coding
  - semgrep
summary: |
  This Codex skill scans for and replaces known-dangerous standard library functions with safe equivalents across languages: C (strcpy → snprintf, sprintf → snprintf, gets → fgets, strtok → strtok_r), Python (eval, exec, pickle.loads, os.system), Node (eval, Function, child_process.exec with shell), PHP (mysql_query, unserialize on user data), and Ruby (eval, send with user input).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill scans for and replaces known-dangerous standard library functions with safe equivalents across languages: C (strcpy → snprintf, sprintf → snprintf, gets → fgets, strtok → strtok_r), Python (eval, exec, pickle.loads, os.system), Node (eval, Function, child_process.exec with shell), PHP (mysql_query, unserialize on user data), and Ruby (eval, send with user input).

## When to Use

Use during onboarding of a legacy codebase, when adding SAST gates to CI, before a security audit, or when hardening a module that handles untrusted input. Also useful as a periodic sweep to prevent regressions.

## Codex Instructions

1. Build a per-language mapping of dangerous functions to safe equivalents (e.g., Python eval → ast.literal_eval where input is a literal, else reject).
2. Scan the target scope for each dangerous function call and capture the call site, arguments, and surrounding context.
3. For each call site, determine whether the input is user-controlled, developer-controlled, or constant — only the latter two are safe.
4. For shell calls (os.system, child_process.exec), replace with the argument-array API (subprocess.run with list, execFile) to avoid shell injection.
5. For deserialization (pickle.loads, unserialize, ObjectInputStream.readObject), replace with a safe format (JSON with schema validation) or wrap in a restricted unpickler that allowlists classes.
6. For eval/exec on dynamic expressions, replace with a parser/interpreter that operates on a safe AST (ast.literal_eval, jsonpath, jinja sandboxed environment).
7. For each replacement, verify the safe equivalent preserves the original behavior on valid inputs — write a regression test.
8. Flag any call site where the safe equivalent does not exist (e.g., eval needed for legitimate code generation) and propose an architecture change.
9. Output a replacement map and a patch; include a CI rule (semgrep, eslint-plugin-security, bandit) to prevent regression.
10. Document the rationale for each replacement so reviewers can verify the security gain.

## Inputs Needed

- Repository path and target language
- List of dangerous functions of concern (or 'all' for the standard set)
- SAST tool in use (semgrep, bandit, eslint-plugin-security, brakeman)
- Whether the code path handles untrusted input
- Existing tests for the affected call sites

## Expected Output

A Markdown report titled 'Dangerous Function Replacement Report' with: (1) Call Site Inventory — File:Line | Function | Input Source | Risk | Replacement | CWE; (2) Patch Diff with safe rewrites; (3) Regression Test Plan; (4) CI Rule Snippet to prevent regressions (semgrep or eslint config).

## Example Prompt

> Scan this PHP codebase for dangerous functions: mysql_query, unserialize on user input, eval, exec. Replace each with safe equivalents (PDO prepared statements, JSON decode, no-eval alternative, escapeshellarg). Add semgrep rules to prevent regression.

## Safety Rules

- Never replace eval with a sandboxed eval that still executes arbitrary code — only a parser-based alternative is acceptable.
- Do not weaken type checks while replacing functions; the safe equivalent must reject invalid input the same way.
- Stop and ask the user if the original function is required for a legitimate use case (e.g., DSL evaluation).
- Never auto-commit replacements in legacy code without running the full test suite.
- If a safe equivalent requires a schema change (e.g., pickle → JSON), produce a migration plan rather than a breaking patch.
- Do not introduce new dependencies without explicit user approval.
