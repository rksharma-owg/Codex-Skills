---
id: migration-reviewer
name: Migration Reviewer
category: devops
difficulty: Intermediate
tags:
  - devops
summary: |
  This Codex skill reviews database migrations for safety: backward compatibility with running app versions, idempotency, lock duration on large tables, data-loss risk, rollback strategy, and zero-downtime deployability.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill reviews database migrations for safety: backward compatibility with running app versions, idempotency, lock duration on large tables, data-loss risk, rollback strategy, and zero-downtime deployability. It targets the common failure mode of a migration that works in staging but blocks production for hours.

## When to Use

Use on every migration PR, before a major schema change, when introducing a new ORM, or when an on-call engineer reports a migration-caused incident.

## Codex Instructions

1. Parse the migration file(s) in the PR and identify the DDL/DML operations (add column, drop column, rename, type change, backfill, index create).
2. For each operation, check backward compatibility: adding a NOT NULL column without a default breaks old app versions; renaming a column breaks old ORM mappings.
3. Estimate lock duration: an ALTER TABLE on a 100M-row Postgres table can lock for hours; recommend the pg_repack or expand-and-contract pattern.
4. Verify idempotency: a migration re-run after partial failure must not error (use IF NOT EXISTS, IF EXISTS).
5. Check for data loss: DROP COLUMN without a backup is irreversible; recommend a two-phase drop (deprecate, then drop after a release cycle).
6. Verify a rollback migration exists and is tested.
7. Check that any data backfill is batched (LIMIT + OFFSET or cursor) to avoid long transactions.
8. Verify the migration is wrapped in a transaction where the database engine supports it (Postgres yes, MySQL partial).
9. Verify the migration does not depend on app code that has not been deployed yet.
10. Output a migration safety report with a go/no-go recommendation and a rollback runbook.

## Inputs Needed

- Migration file path(s) in the PR
- Database engine and version (Postgres 15, MySQL 8, etc.)
- Largest affected table size (rows and GB), if known
- Current production app version vs the version this migration supports
- ORM in use (Alembic, Knex, Prisma Migrate, Flyway)

## Expected Output

A Markdown report titled 'Migration Safety Review' with: (1) Operations table — Op | Object | Risk | Lock Est. | Backward Compatible? | Rollback Available?; (2) Recommendation: Go / Go with conditions / No-go; (3) Rollback Runbook with exact commands; (4) Deploy Sequencing notes (when to deploy app vs migration).

## Example Prompt

> Review migrations/20240115_add_phone_to_users.ts. We use Postgres 15 with Alembic; the users table has 80M rows. Is this migration safe for zero-downtime deploy? Provide a rollback runbook.

## Safety Rules

- Never auto-apply migrations to production — produce a runbook for the on-call engineer.
- Do not approve a destructive migration (DROP COLUMN, DROP TABLE) without an explicit user sign-off.
- Stop and ask the user if the largest table size is unknown — assumptions here cause production outages.
- If a migration requires app coordination (expand-and-contract), document the deploy sequence explicitly.
- Never log full row data during a backfill — log only progress counts.
- If the migration engine does not support transactional DDL (MySQL), flag the partial-failure risk explicitly.
