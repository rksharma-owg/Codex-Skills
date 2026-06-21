---
id: input-validation-hardener
name: Input Validation Hardener
category: secure-coding
difficulty: Intermediate
tags:
  - asvs
  - cwe
  - ecr
  - secure-coding
summary: |
  This Codex skill audits every entry point where untrusted data crosses a trust boundary (HTTP handlers, gRPC methods, queue consumers, CLI args, file imports) and rewrites the validation layer to use allowlist schemas, canonicalization, length limits, and type coercion.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits every entry point where untrusted data crosses a trust boundary (HTTP handlers, gRPC methods, queue consumers, CLI args, file imports) and rewrites the validation layer to use allowlist schemas, canonicalization, length limits, and type coercion. It targets the root cause of injection, path traversal, and logic-bug vulnerabilities that ASVS V5 requires to be closed at the perimeter.

## When to Use

Activate this skill before merging any new endpoint, when adding fields to an existing public API, after a pentest reports injection findings, or when onboarding a legacy module that has no schema validation. It is also useful during threat-modeling follow-ups to harden data flows identified as high risk.

## Codex Instructions

1. Enumerate every entry point in the target scope: HTTP routes, gRPC service methods, message queue handlers, scheduled job parameters, CLI arguments, and external file imports.
2. For each entry point, identify the input schema (JSON body, query string, headers, multipart fields) and locate the current validation code, if any.
3. Map each input field to a primitive type and apply canonicalization first (URL-decode, Unicode-normalize, trim) before any allowlist check, to defeat encoded bypasses.
4. Define an allowlist schema per field: exact regex for strings, bounded ranges for numbers, fixed enumerations for status fields, and explicit allowed MIME types for uploads.
5. Reject on the first failed check rather than accumulating errors, and return a generic 400 response without echoing user input back in the error body.
6. Where validation is currently done with blacklist regex or string-replace, replace it with allowlist checks and document why the blacklist was unsafe.
7. For numeric inputs used in money, time, or array-index contexts, enforce additional semantic bounds (e.g., amount > 0, timestamp within +/- 1 year of now, index < array length).
8. Generate or update the schema definitions (JSON Schema, Pydantic, Zod, Joi, OpenAPI) so the same validation rule is reused by the framework and the docs.
9. Add unit tests that exercise both valid inputs and the canonical bypass payloads (UTF-8 overlong, double-encoding, null bytes, oversized payloads).
10. Produce a diff-ready patch and a findings table; never silently mutate production code without showing the proposed changes.

## Inputs Needed

- Repository path or specific module/directory to scan
- Language and framework (e.g., Python/FastAPI, Node/Express, Go/Echo)
- Existing schema definitions (OpenAPI, Protobuf, Pydantic models) if any
- List of untrusted entry points to prioritize, or 'all' for full sweep
- Known business constraints (max upload size, allowed currencies, locale)

## Expected Output

A Markdown report titled 'Input Validation Hardening Report' with three sections: (1) Executive Summary listing entry points scanned and hardening coverage; (2) Findings Table with columns Entry Point | Field | Current Validation | Risk | Proposed Allowlist | CWE; (3) Patch Diff showing concrete code changes ready to apply. Each finding references CWE-20 (Improper Input Validation) and the relevant ASVS V5.x control.

## Example Prompt

> Scan src/api/ in this FastAPI project and harden input validation across all POST/PUT routes. Show me the diff and a findings table. Don't commit yet — I'll review first.

## Safety Rules

- Never auto-commit hardening changes — always produce a patch for human review.
- Do not strip existing authentication or authorization checks while rewriting validation.
- Preserve backward compatibility for existing API clients unless explicitly told to make a breaking change.
- Do not log raw user input at INFO or higher; redact PII and secrets.
- If the input is used in a SQL query, filesystem path, or shell command, also route it through the relevant secure-coding skill (parameterized queries, path allowlist, no-shell).
- Stop and ask the user if a field has ambiguous business semantics that block allowlist definition.
