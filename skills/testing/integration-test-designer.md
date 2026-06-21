---
id: integration-test-designer
name: Integration Test Designer
category: testing
difficulty: Intermediate
tags:
  - docker
  - github-actions
  - jest
  - pytest
  - testing
summary: |
  This Codex skill designs integration tests that verify multiple components work together: API endpoint to database, queue producer to consumer, service to external API.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs integration tests that verify multiple components work together: API endpoint to database, queue producer to consumer, service to external API. It uses test containers (Testcontainers, docker-compose) for real dependencies and produces a runnable test suite.

## When to Use

Use when introducing a new service boundary, before refactoring a multi-service flow, when adding a queue or external API integration, or to catch regressions that unit tests miss.

## Codex Instructions

1. Identify the integration boundary to test: API endpoint to database, producer to queue consumer, service to external API.
2. Choose the test environment: Testcontainers for ephemeral dependencies, docker-compose for multi-service, mock-server for external APIs.
3. Define the test scenarios: happy path, error from dependency, timeout from dependency, partial failure.
4. For each scenario, define the setup (seed data, mock responses), the action (call the endpoint), and the assertion (response, side effect).
5. Use real dependencies where possible (real Postgres, real Redis) to catch integration bugs that mocks miss.
6. For external APIs, use a mock server (WireMock, nock) that returns canned responses and verifies the request.
7. Clean up state between tests: truncate tables, purge queues — never rely on test order.
8. Run the suite in CI on every PR; flag tests longer than 30 seconds for optimization.
9. Output the test suite, the docker-compose or Testcontainers config, and the CI integration snippet.

## Inputs Needed

- Integration boundary to test
- Test framework (pytest, Jest, Go testing)
- Testcontainers or docker-compose availability
- External APIs and their mock servers
- CI environment (GitHub Actions, GitLab CI)

## Expected Output

A test suite with setup, scenarios, and assertions. Plus a Testcontainers or docker-compose config and a CI integration snippet.

## Example Prompt

> Design integration tests for the order placement flow: POST /orders -> validate -> write to Postgres -> publish to Kafka -> consumer writes to fulfillment service. Use Testcontainers for Postgres and Kafka, mock the fulfillment service with WireMock. Cover happy path, DB error, Kafka timeout. Pytest + testcontainers-python.

## Safety Rules

- Never run integration tests against a shared staging database — use ephemeral containers.
- Do not use production credentials in test config — use Testcontainers defaults.
- Stop and ask the user if a test scenario's external API cannot be mocked.
- If a test leaves state behind, fix the cleanup — leaked state causes flaky tests.
- Never log full request/response bodies at INFO if they contain PII.
- If the test reveals a production bug, file it and add a regression test.
