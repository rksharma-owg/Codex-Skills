---
id: api-doc-generator
name: API Documentation Generator
category: devops
difficulty: Intermediate
tags:
  - devops
  - oauth
summary: |
  This Codex skill generates API documentation from an OpenAPI, Protobuf, or GraphQL contract: endpoint reference, request/response examples, authentication flows, error codes, and SDK code samples in multiple languages.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates API documentation from an OpenAPI, Protobuf, or GraphQL contract: endpoint reference, request/response examples, authentication flows, error codes, and SDK code samples in multiple languages.

## When to Use

Use when publishing a new API, when adding endpoints to an existing API, when the docs are out of sync with the contract, or before a public API launch.

## Codex Instructions

1. Read the contract file (OpenAPI YAML/JSON, .proto, .graphql).
2. Generate an endpoint reference: method, path, summary, parameters, request body, response codes, response schema.
3. Generate request and response examples for each endpoint — real, copy-pasteable examples, not placeholders.
4. Generate authentication docs: how to obtain a token, how to pass it (header, query, cookie), token expiration.
5. Generate error code docs: each documented error code with a description, example response, and remediation.
6. Generate SDK code samples in at least three languages (curl, Python, JavaScript) for each endpoint.
7. Generate a getting started guide: authentication, first call, pagination, error handling.
8. Generate a changelog by diffing against the previous contract version.
9. Choose a publishing tool: Redoc, Stoplight Elements, Mintlify, ReadMe — or Markdown for a static site.
10. Output the documentation in the chosen format, ready to publish.

## Inputs Needed

- Contract file (OpenAPI, Protobuf, GraphQL SDL)
- Target audience (internal, partner, public)
- Publishing tool (Redoc, Mintlify, Markdown)
- SDK languages to include in code samples
- Previous contract version for changelog

## Expected Output

API documentation in the chosen format, including endpoint reference, examples, auth docs, error codes, SDK samples, getting started guide, and changelog.

## Example Prompt

> Generate API docs from openapi.yaml for our public payments API. Audience: external developers. Publishing via Mintlify. Code samples in curl, Python, JavaScript, Go. Include a changelog diffing against the previous version on main. Cover authentication (OAuth2 client credentials), pagination (cursor), and error codes.

## Safety Rules

- Never publish internal-only endpoints in public docs — filter them out.
- Do not include real customer data in examples — use clearly fake values (Acme Corp, example.com).
- Stop and ask the user if an endpoint's documentation is ambiguous — better to ask than to publish wrong info.
- If the contract has breaking changes, document the migration path explicitly.
- Never log API keys in code samples — use placeholders.
- If the API handles regulated data, add the compliance disclaimer to the docs.
