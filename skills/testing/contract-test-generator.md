---
id: contract-test-generator
name: Contract Test Generator
category: testing
difficulty: Intermediate
tags:
  - github-actions
  - testing
summary: |
  This Codex skill generates contract tests for an API: verifies the server's response matches the OpenAPI/Protobuf contract, and verifies the client handles all documented error responses.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates contract tests for an API: verifies the server's response matches the OpenAPI/Protobuf contract, and verifies the client handles all documented error responses. It targets the failure mode of a client that breaks when the server adds a new error response.

## When to Use

Use when introducing contract testing, when splitting a monolith into services, when exposing an API to external consumers, or when a client breaks due to an undocumented server response.

## Codex Instructions

1. Identify the contract format: OpenAPI (REST), Protobuf (gRPC), GraphQL SDL.
2. Choose the contract testing tool: Pact (consumer-driven), Schemathesis (OpenAPI fuzzing), Dredd (OpenAPI validation), Postman + contract assertions.
3. For consumer-driven contract testing, capture the consumer's expectations as Pact files; verify the provider against them.
4. For OpenAPI contract validation, generate requests from the schema, send to the server, and assert the response matches the schema.
5. For each documented error response (4xx, 5xx), verify the client handles it gracefully.
6. Generate tests for boundary cases: missing required fields, extra fields, wrong types, oversized payloads.
7. Run the contract tests in CI on every provider PR; if a consumer's Pact fails, block the provider merge.
8. Publish the contract to a Pact Broker or equivalent so consumers can verify against the latest provider contract.
9. Output the contract test suite, the CI integration, and the broker publishing step.

## Inputs Needed

- Contract file (OpenAPI, .proto, GraphQL SDL)
- API provider's base URL (staging or test)
- Contract testing tool (Pact, Schemathesis, Dredd)
- Pact Broker or equivalent (if consumer-driven)
- Consumers to test against (if known)

## Expected Output

A contract test suite in the chosen tool, a CI integration snippet that runs the suite on every provider PR, and (for consumer-driven) a Pact Broker publishing step.

## Example Prompt

> Generate contract tests for our OpenAPI 3.1 spec at openapi.yaml. Use Schemathesis to fuzz the API and assert responses match the schema. Run in GitHub Actions on every PR to main. Also generate Pact files for our two known consumers (web, mobile) and publish to our Pact Broker.

## Safety Rules

- Never run contract tests against production — use staging or a test environment.
- Do not weaken the contract to 'fix' a failing test — fix the server.
- Stop and ask the user if a consumer's expectations are ambiguous.
- If a contract test reveals an undocumented error response, add it to the contract rather than silencing the test.
- Never log full request/response bodies at INFO if they contain PII.
- If a provider change breaks a consumer's Pact, coordinate the migration before merging.
