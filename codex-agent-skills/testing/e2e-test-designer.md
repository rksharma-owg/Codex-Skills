# E2E Test Designer

## Purpose

This Codex skill designs end-to-end tests that verify a user flow through the application: login -> navigate -> perform action -> verify outcome. It uses Playwright, Cypress, or Selenium, with realistic test data and a clean test environment.

## When to Use

Use when launching a new user flow, after a UI refactor, when adding a critical path test (signup, checkout), or to catch regressions that integration tests miss.

## Codex Instructions

1. Identify the user flow to test: signup, checkout, password reset, search, etc.
2. Choose the test framework: Playwright (recommended, modern), Cypress (popular, JS-only), Selenium (legacy, multi-language).
3. Define the test environment: a staging instance with seeded data, isolated from production.
4. Define the test data: realistic but fake users, products, orders — never reuse production data.
5. Write the test steps: navigate, fill form, click, wait for state, assert on result.
6. Use stable selectors: data-testid attributes preferred over CSS classes or text (which change).
7. Handle async: use Playwright's auto-waiting; avoid explicit sleeps.
8. Add a cleanup step: delete the test user or reset the state after the test.
9. Run the suite in CI on every PR; flag tests longer than 60 seconds for optimization.
10. Output the test file, the test data fixtures, and the CI integration.

## Inputs Needed

- User flow to test
- Test framework (Playwright, Cypress, Selenium)
- Test environment URL (staging)
- Test data fixtures or seed scripts
- CI environment

## Expected Output

An E2E test file in the chosen framework, test data fixtures, and a CI integration snippet. The test should run end-to-end in staging without manual intervention.

## Example Prompt

> Design a Playwright E2E test for the user signup flow: visit /signup, fill email + password, click submit, verify email arrives (mock the email service), click the verification link, verify the user is logged in. Use fake test data. Run in CI on every PR.

## Safety Rules

- Never run E2E tests against production — use staging.
- Do not reuse production user credentials in tests — create test users.
- Stop and ask the user if the test environment cannot be reset between runs.
- If a test reveals a real bug, file it and add a regression test.
- Never log screenshots that contain PII — mask before logging.
- If the test uses an external service (email, SMS), mock it to avoid sending real messages.
