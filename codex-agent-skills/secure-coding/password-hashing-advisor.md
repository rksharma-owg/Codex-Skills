# Password Hashing Advisor

## Purpose

This Codex skill reviews password storage to ensure hashing uses Argon2id (preferred), bcrypt with cost >= 12, or scrypt with approved parameters, and that salts are unique per-user and stored alongside the hash. It flags MD5, SHA-1, SHA-256 (unsalted or fast), and any homebrew crypto, and produces migration plans for legacy hashes.

## When to Use

Activate during auth-system refactors, after a credential-stuffing incident, when onboarding an acquired product's user database, or before a compliance audit (PCI 8.2.1, HIPAA access control). Also useful when migrating from a deprecated algorithm to Argon2id.

## Codex Instructions

1. Locate the password hashing call sites: registration, login, password reset, password change, and any admin password reset tooling.
2. Identify the algorithm in use and its parameters (bcrypt cost, scrypt N/r/p, Argon2id m/t/p, PBKDF2 iterations + hash).
3. Verify that a fresh random salt of at least 16 bytes is generated per password and stored with the hash.
4. Compare parameters against OWASP Password Storage Cheat Sheet: Argon2id m=19456 t=2 p=1, bcrypt cost >= 12, scrypt N=2^17 r=8 p=1, PBKDF2 >= 600000 iterations with SHA-256.
5. For legacy hashes, design an upgrade-on-login migration: wrap the old hash inside a new Argon2id hash, store a marker, and re-hash on next successful login.
6. Verify that timing attacks are mitigated by always running the hash function even when the user does not exist (return the same slow path).
7. Confirm that error messages do not leak whether the username exists vs the password is wrong.
8. Add a pepper only if the secret can be stored in a HSM or KMS — never hardcode a pepper in source.
9. Produce a migration runbook for legacy hashes and a patch for new hashes; include a load-test estimate of CPU cost.
10. Flag any code path that returns a plaintext password, logs a password, or stores a password in session state.

## Inputs Needed

- Auth module path
- Language and crypto library (bcrypt, argon2-cffi, libsodium, javax.crypto)
- Current algorithm and parameters in use
- Total user count and login QPS (affects parameter tuning)
- KMS or HSM availability for pepper storage

## Expected Output

A Markdown report titled 'Password Storage Audit' with: (1) Algorithm Matrix — Path | Algorithm | Params | Salt | Verdict | OWASP Ref; (2) Migration Plan for legacy hashes with the wrap-and-upgrade flow; (3) Patch Diff for new hashes; (4) Performance Estimate showing CPU cost at target QPS.

## Example Prompt

> Review src/auth/password.ts in this Node app. We use bcrypt with cost 10 — upgrade to Argon2id with OWASP-recommended parameters. Provide a migration plan for existing hashes without forcing a mass password reset.

## Safety Rules

- Never log plaintext or hashed passwords at any log level.
- Do not propose a pepper unless a KMS is available to store it.
- Never disable or weaken existing hashing to 'fix' a login latency issue without explicit user approval.
- Stop and ask the user before changing parameters that would invalidate existing hashes (e.g., switching from bcrypt to Argon2id without the wrap-and-upgrade flow).
- Do not commit any sample password values in tests — use clearly fake values like 'correct horse battery staple'.
- Never expose hash comparison timing in error responses — always return the same failure path.
