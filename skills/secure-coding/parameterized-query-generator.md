---
id: parameterized-query-generator
name: Parameterized Query Generator
category: secure-coding
difficulty: Intermediate
tags:
  - cwe
  - rds
  - secure-coding
summary: |
  This Codex skill converts string-concatenated SQL, NoSQL, OS command, and LDAP queries into parameterized or prepared-statement equivalents.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill converts string-concatenated SQL, NoSQL, OS command, and LDAP queries into parameterized or prepared-statement equivalents. It targets CWE-89 (SQL Injection), CWE-90 (LDAP Injection), and CWE-78 (OS Command Injection) by ensuring that user-controlled data is always passed through a binding mechanism rather than interpolated into the query string.

## When to Use

Activate when refactoring a legacy data-access layer, after a SAST tool reports SQL injection findings, when migrating from raw drivers to an ORM, or before exposing an existing internal query to a public endpoint. Also useful during code review of any PR that touches database code.

## Codex Instructions

1. Locate every query construction site: raw SQL strings, query builder calls, NoSQL filter objects, LDAP search filters, and shell command builders.
2. For each site, classify the parameters into static literals (safe) and dynamic values (must be bound).
3. Rewrite SQL queries to use prepared statements with positional (?) or named (@param) placeholders; preserve the original query structure and JOIN/WHERE semantics.
4. For NoSQL (MongoDB, DynamoDB), replace `{$where: '...'}` and string-built filter objects with typed operator objects; reject any filter that includes a JavaScript function.
5. For LDAP, escape dynamic values using RFC 4514 distinguished-name escaping and ensure the filter template is a constant string.
6. For OS commands, prefer language-native APIs (subprocess with list args, exec.Command with args, child_process with args array) over shell=True or string concatenation.
7. Where a dynamic identifier (table name, column name) is required, validate it against an allowlist of known identifiers and reject otherwise — never bind identifiers as parameters.
8. Add integration tests that pass malicious payloads (`'; DROP TABLE--`, `{$gt: ''}`, `; rm -rf /`) and assert the query is rejected or treated as data.
9. Produce a patch and a migration note if the query semantics changed (e.g., LIKE wildcards now require explicit % in the bound value).
10. Flag any query that cannot be safely parameterized (e.g., dynamic pivot queries) and propose an architecture-level alternative.

## Inputs Needed

- Repository or data-access layer path
- Database engine and driver (PostgreSQL/psycopg2, MySQL/PDO, MongoDB driver, etc.)
- ORM in use, if any (SQLAlchemy, Prisma, TypeORM, Hibernate)
- List of files or modules flagged by prior SAST scan
- Schema or migration files for identifier allowlisting

## Expected Output

A Markdown report titled 'Parameterization Report' with: (1) Query Inventory table — File | Line | Query Type | Vulnerability | Proposed Rewrite; (2) Patch Diff with parameterized rewrites; (3) Identifier Allowlist table — Identifier | Source of Truth | Approved Values; (4) Test Plan listing injection payloads to verify each fix.

## Example Prompt

> Refactor src/db/queries.ts in this Node/Express project. We use pg directly — convert every string-concatenated SQL to parameterized queries. Flag any dynamic table names so I can allowlist them.

## Safety Rules

- Never commit rewrites without running the existing test suite to confirm query semantics are preserved.
- Do not silently change result types (e.g., row count or NULL handling) when switching from raw to prepared statements.
- If a query cannot be parameterized, mark it as a finding rather than guessing a rewrite.
- Do not bypass ORM protections (e.g., raw() calls) to 'fix' performance issues without explicit user approval.
- Never log full query text with bound parameter values at INFO or higher in production.
- Stop and ask the user if parameter type inference is ambiguous (e.g., UUID vs string).
