# Race Condition Finder

## Purpose

This Codex skill identifies Time-of-Check-to-Time-of-Use (TOCTOU) and other concurrency bugs in shared-state code paths: balance updates, inventory decrements, coupon redemption, rate limiter counters, and file-based locks. It maps each finding to CWE-362 (Race Condition) and CWE-367 and proposes language-native atomic primitives or database-level locking strategies.

## When to Use

Use during code review of any feature that mutates shared state, after a load test reveals inconsistent counts, when an auditor flags double-spend or duplicate-submission risk, or before launching a feature with financial or quota semantics.

## Codex Instructions

1. Identify code paths that read a value, branch on it, then write a derived value — the classic check-then-act pattern.
2. For each path, list the shared state (database row, in-memory counter, file, cache entry) and the concurrency primitive currently protecting it.
3. Determine whether the operation is atomic: a single SQL UPDATE with WHERE, an atomic compare-and-swap, a Redis MULTI/EXEC, or a language-level mutex.
4. For database operations, verify the transaction isolation level matches the requirement (READ COMMITTED is insufficient for balance updates; use SERIALIZABLE or SELECT FOR UPDATE).
5. For distributed systems, prefer idempotency keys and outbox patterns over distributed locks; verify lock TTL, fencing tokens, and retry behavior.
6. For file-based state, confirm the open uses O_CREAT|O_EXCL or an atomic rename, not a stat-then-create sequence.
7. For rate limiters, verify the counter is incremented atomically (Redis INCR with TTL, not a GET-then-SET).
8. Write a stress test that runs the operation concurrently (e.g., 100 parallel requests) and asserts the final state is consistent.
9. Produce a patch using the appropriate atomic primitive and document the chosen isolation level or lock strategy.
10. Flag any path that cannot be made atomic without an architecture change (e.g., multi-step business process) and propose an outbox or saga pattern.

## Inputs Needed

- Repository path or feature module
- Language and runtime (Node single-threaded, Python asyncio, Go goroutines, JVM threads)
- Database and isolation level in use
- Cache layer (Redis, Memcached) and concurrency model
- Whether the deployment is single-instance or multi-instance

## Expected Output

A Markdown report titled 'Race Condition Audit' with: (1) Race Inventory — Path | Shared State | Current Protection | Risk | Proposed Fix | CWE; (2) Patch Diff with atomic primitives; (3) Stress Test Plan showing concurrent execution and expected final state; (4) Architecture Notes for paths requiring saga/outbox patterns.

## Example Prompt

> Audit src/wallet/ in this Go service for race conditions. We use Postgres with the default isolation level — check every balance transfer and coupon redemption path. Propose SELECT FOR UPDATE or atomic UPDATE WHERE fixes.

## Safety Rules

- Never weaken an existing transaction isolation level without explicit user approval.
- Do not replace a database transaction with an in-memory mutex in a multi-instance deployment.
- Stop and ask the user if a distributed lock is required (the failure modes are subtle).
- Never log full transaction state at INFO; redact PII and account numbers.
- If a stress test reveals data corruption, treat it as a finding, not a test artifact.
- Do not auto-apply migration scripts that change isolation levels on production.
