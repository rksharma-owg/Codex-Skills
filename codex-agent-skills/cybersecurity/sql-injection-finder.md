# SQL Injection Finder

## Purpose
This Codex skill detects SQL Injection (SQLi) vulnerabilities — classic, blind, second-order, and stored-procedure-based — across codebases in any language. It exists because SQLi remains in the OWASP Top 10 (A03:2021) two decades after it was first catalogued, and a single unsanitized `query()` call can expose an entire database. The skill focuses on taint-flow accuracy: real sinks, real sources, and real sanitizers, with a low false-positive rate.

## When to Use
Run this skill on any PR touching database access code, ORM raw query methods, stored procedures, or report builders. Also use it during onboarding of legacy code (especially PHP, classic ASP, or older Java), when migrating from raw SQL to an ORM, when a DAST tool flagged a parameter but the team cannot reproduce it, or before a compliance audit that requires evidence of SQLi-free code (PCI DSS Req. 6.2.4).

## Codex Instructions
1. Identify the data-access layer per language: `mysql_*`, `mysqli_*`, `PDO` (PHP); `Statement`, `PreparedStatement`, `EntityManager.createNativeQuery`, JPA `@Query` (Java); `sqlite3`, `psycopg2`, `SQLAlchemy` text/execute, `django.db.connection` (Python); `pg`, `mysql`, `mysql2`, Knex raw, Sequelize `query` (Node.js); `database/sql` + `db.Query` (Go); `SqlCommand` (C#/.NET).
2. Treat as **sources** all user-controllable inputs: HTTP request params, body, headers, cookies, path variables, GraphQL args, gRPC message fields, file uploads parsed into the request, and data returned from untrusted APIs.
3. Treat as **sinks** any SQL execution method: `query()`, `execute()`, `exec()`, `executeUpdate()`, `raw()`, `text()`, `CommandText` set with string concatenation, and stored-procedure calls with concatenated argument strings.
4. Treat as **sanitizers**: parameterized queries (`?`, `$1`, `:name`), prepared statements, ORM `where()` with bound params, allowlist-based identifier escaping (e.g., a regex of `^[a-zA-Z_]+$`), and `mysql_real_escape_string` (legacy — flag as weak, do not treat as full sanitizer).
5. For each sink, trace the dataflow back to a source; if the path traverses no sanitizer, classify as a confirmed SQLi.
6. Distinguish variants: classic (concatenation in `query()`), blind (response timing or error-based), second-order (data stored then concatenated later), stored-procedure (dynamic SQL inside `EXECUTE` / `sp_executesql`), and ORM raw (`Model.objects.raw()` in Django, `Session.createSQLQuery` in Hibernate).
7. Re-baseline severity: any SQLi on a public-facing endpoint with a privileged DB user is Critical; internal admin tooling is High; read-only replica with no PII is Medium.
8. Map each finding to CWE-89 (SQL Injection) and, for stored-procedure variants, CWE-564 (SQL Injection via Hibernate Query).
9. Propose a patch using the language's parameterized-query idiom; for cases where the SQL structure itself must vary (e.g., dynamic `ORDER BY`), propose an allowlist-based approach, not string concatenation.
10. Add a regression test per finding: a positive test (payload should not execute) and a Semgrep rule to catch reintroduction.
11. Emit `SQLI_FINDINGS.md` plus SARIF for upload to GitHub code scanning.

## Inputs Needed
- Repository path
- Language(s) and framework(s) — affects sink/source identification
- ORM in use (Hibernate, SQLAlchemy, Django ORM, Sequelize, Knex, Prisma, Entity Framework)
- Database user privilege level (read-only, read-write, DDL, superuser)
- Data classification of the underlying tables (PII, PCI, PHI, public)
- Public-facing vs. internal endpoint context (affects severity)
- Existing test fixtures with SQL payloads (to avoid re-flagging intentional tests)
- Prior DAST or pen-test findings (to cross-correlate)

## Expected Output
A markdown report `SQLI_FINDINGS.md` with sections: Executive Summary (total findings by severity, ORM used, total sinks scanned), Taint Flows (one subsection per finding with source → transformation → sink), Findings Table (ID, Severity, CWE, Sink File:Line, Source, Sanitizer Present?, Patch), Stored Procedure Analysis (if any), and Regression Tests. Severity scale: Critical (auth bypass, admin endpoint, sensitive table) / High (data exfiltration possible) / Medium (limited column access, internal) / Low (test/dev only). Emit `sqli.sarif`.

## Example Prompt
> Find SQL injection in `/home/z/my-project/reporting-service` (Python 3.11, Django 5, Postgres). The team uses `Model.objects.raw()` in a few places and we just had a pen tester find a second-order SQLi via the `notes` field. Trace data flows from request to DB, classify each finding, propose parameterized patches, and write `SQLI_FINDINGS.md` with SARIF. Skip `tests/` unless the vuln would be exploitable in CI.

## Safety Rules
- Never execute SQL payloads against a live database — static analysis only.
- Do not recommend `mysql_real_escape_string` or `addslashes` as sanitizers; they are weak and encoding-aware attackers bypass them.
- For dynamic identifiers (table names, column names, `ORDER BY`), require an allowlist, never escaping alone.
- Do not auto-apply patches to source; propose them in the report for human review.
- If the database user is `postgres` or `sa` (superuser), treat any SQLi as Critical regardless of endpoint exposure.
- Never include real PII or production data samples in the report's taint-flow snippets; substitute `[REDACTED]`.
- If the ORM's `raw()` method is called with a string built from a format function (`.format()`, f-string, `${}`), treat as Critical — these bypass parameterization even when the ORM is otherwise safe.
- Do not flag parameterized queries with `?`/`$1` placeholders as findings, even if the surrounding string uses concatenation for static SQL keywords.
