# Test Data Faker

## Purpose

This Codex skill generates realistic but fake test data for an application: users, orders, payments, products. It uses Faker (Python, JS) or similar libraries, respects the schema, and produces data that exercises edge cases (unicode names, large payloads, boundary values).

## When to Use

Use when seeding a test database, when generating test fixtures, before a demo, or when an existing test data set is found to contain production PII.

## Codex Instructions

1. Identify the entities to fake: User, Order, Product, Payment, etc.
2. Identify the schema for each entity: fields, types, constraints (foreign keys, enums).
3. Choose the faker library: Faker (Python/JS/PHP), Bogus (.NET), Java Faker.
4. Generate realistic values: names with unicode, emails at example.com (RFC 2606), phone numbers in multiple formats.
5. Generate edge cases: empty strings, max-length strings, unicode, emojis, null where allowed.
6. Respect foreign keys: generate Orders that reference existing Users.
7. Avoid generating data that looks like real PII: use example.com domains, 555 phone numbers, fake SSNs (not in valid format).
8. Generate a realistic distribution: 80% normal users, 15% with one order, 5% with > 10 orders.
9. Output the test data as SQL inserts, JSON fixtures, or a script that generates and loads the data.
10. Verify the test data passes the application's own validators — if not, the validators may have a bug.

## Inputs Needed

- Entity schemas (from the ORM, database, or OpenAPI)
- Faker library preference
- Output format (SQL, JSON, script)
- Volume (small for unit tests, large for load tests)
- Edge cases to include

## Expected Output

A test data file (SQL, JSON) or a generation script that produces realistic, schema-valid, edge-case-inclusive fake data. Plus instructions to load the data into the test environment.

## Example Prompt

> Generate test data for our e-commerce app: 1000 Users (with unicode names, example.com emails), 10000 Orders (80% with 1-3 items, 15% with 5-10, 5% with > 20), 500 Products. Use Python Faker. Output as SQL inserts for Postgres. Include edge cases: empty cart, max-length product name, emoji in product description.

## Safety Rules

- Never generate data that could be mistaken for real PII — use example.com, 555 numbers, invalid SSN format.
- Do not use real customer data as a seed — always fake from scratch.
- Stop and ask the user if an entity's schema is ambiguous.
- If the generated data fails the application's validators, investigate the validators — they may have a bug or the schema may be stale.
- Never commit test data with real-looking credit card numbers — use the test card ranges (4111 1111 1111 1111).
- If the test data is shared with a third party (e.g., for a demo), verify it contains no proprietary business logic.
