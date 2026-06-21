---
id: error-message-sanitizer
name: Error Message Sanitizer
category: secure-coding
difficulty: Intermediate
tags:
  - asvs
  - ecr
  - owasp
  - secure-coding
summary: |
  This Codex skill audits error messages, stack traces, and exception payloads to ensure they do not leak sensitive information: stack paths, SQL fragments, internal hostnames, environment variables, secrets, or PII.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits error messages, stack traces, and exception payloads to ensure they do not leak sensitive information: stack paths, SQL fragments, internal hostnames, environment variables, secrets, or PII. It aligns with OWASP ASVS V7 (Error Handling) and produces patches that route detailed errors to logs while returning generic messages to clients.

## When to Use

Activate during API hardening, after a pentest reports information disclosure, when introducing a new error-handling middleware, or before exposing a previously internal API to a public audience.

## Codex Instructions

1. Inventory every error response path: HTTP error handlers, exception-to-response mappers, GraphQL error formatter, gRPC status mappers.
2. For each path, classify the information exposed: stack trace, file path, SQL query, internal hostname, version string, environment variable, secret value, PII.
3. Define a sanitized error envelope: a correlation ID, a generic message ('Internal error'), an HTTP status code, and an optional error code (no internal details).
4. Route the full exception detail to the structured logger at ERROR level, with the correlation ID linking client and server logs.
5. Verify that 404 responses do not differ between 'resource exists but forbidden' and 'resource does not exist' to prevent enumeration.
6. Verify that 401 vs 403 distinctions do not leak whether a username exists (return 401 for both bad username and bad password).
7. For GraphQL, configure the error formatter to redact the `extensions.exception` field in production.
8. For frameworks that auto-leak stack traces in development (Django DEBUG=True, Express err.stack), ensure production config disables this.
9. Add a test that triggers every error path and asserts the response contains no internal detail.
10. Produce a patch for the error middleware, a logging config, and a test plan.

## Inputs Needed

- Repository path
- Framework in use (Express, Django, Spring, FastAPI, Apollo)
- Current error-handling middleware configuration
- Production vs development environment flags
- Structured logger in use (pino, structlog, logback, serilog)

## Expected Output

A Markdown report titled 'Error Disclosure Audit' with: (1) Disclosure Inventory — Path | Leaked Info | Severity | Fix; (2) Patch Diff for the error envelope and logger integration; (3) Test Plan listing error-triggering requests and expected sanitized responses; (4) Correlation ID Strategy for log linking.

## Example Prompt

> Audit this FastAPI app for error disclosure. We're about to expose the API publicly — make sure every 4xx/5xx response returns only a correlation ID and generic message, with full details going to structlog at ERROR level. Add tests for each error path.

## Safety Rules

- Never log secrets or PII at any level — redact before logging.
- Do not disable stack traces in development — only in production.
- Stop and ask the user if the error envelope must include machine-readable error codes for client SDKs.
- Never return a 200 with an error body to 'simplify client code' — use the correct HTTP status.
- If the framework's default error formatter cannot be fully sanitized, propose a custom formatter rather than a partial fix.
- Do not weaken authentication or authorization error distinctions (401 vs 403) without a security review.
