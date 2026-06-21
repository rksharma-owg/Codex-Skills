---
id: secrets-rotation-planner
name: Secrets Rotation Planner
category: devops
difficulty: Intermediate
tags:
  - devops
  - ecr
  - jwt
  - kubernetes
  - pci
  - rds
  - tls
  - vault
summary: |
  This Codex skill designs a rotation plan for a service's secrets (database passwords, API keys, signing keys) that supports zero-downtime rotation via a key-chain pattern, verifies the new secret is in use, and only then removes the old one.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a rotation plan for a service's secrets (database passwords, API keys, signing keys) that supports zero-downtime rotation via a key-chain pattern, verifies the new secret is in use, and only then removes the old one. It targets the failure mode of a rotation that breaks the service because old and new secrets are not simultaneously valid.

## When to Use

Use when introducing a new secret type, after a secret exposure incident, when onboarding a secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager), or as part of a compliance requirement (PCI 3.2.1 requires 90-day rotation).

## Codex Instructions

1. Inventory the service's secrets: type (DB password, API key, signing key, TLS private key), source (env var, file, secrets manager), consumers (app instances, sidecars, jobs).
2. Classify each secret by rotation impact: zero-downtime capable (key chain), requires restart, requires deploy.
3. For each zero-downtime-capable secret, design the key-chain pattern: add the new secret while keeping the old valid, deploy code that prefers the new, verify the new is in use, then remove the old.
4. For secrets that require restart, plan a rolling restart after the new secret is in the manager.
5. For secrets that require deploy, plan the deploy with the new secret reference.
6. Define the verification step: a metric or log line that confirms the new secret is being used.
7. Define the rollback step: re-add the old secret to the manager if the new one fails.
8. Document the rotation runbook with exact commands, expected duration, and verification queries.
9. Schedule the rotation in the team's calendar; recommend automation (Lambda, Cloud Function) for recurring rotations.
10. Output the rotation runbook and any code patches required to support the key-chain pattern.

## Inputs Needed

- Service repository path
- Secrets manager in use (Vault, AWS Secrets Manager, GCP Secret Manager, Kubernetes Secrets)
- Inventory of current secrets with their consumers
- Rotation frequency requirement
- Whether the consumers support multiple simultaneous secrets

## Expected Output

A Markdown rotation runbook per secret type: (1) Inventory; (2) Rotation Strategy (key-chain, restart, deploy); (3) Step-by-step commands; (4) Verification query; (5) Rollback procedure; (6) Code Patch if the key-chain pattern requires app changes.

## Example Prompt

> Design a zero-downtime rotation plan for the payments service. Secrets: Postgres password (AWS Secrets Manager), Stripe API key (env var), JWT signing key (file). All consumers are stateless Go services with multiple replicas. Produce per-secret runbooks and any code patches needed for the key-chain pattern.

## Safety Rules

- Never remove the old secret before verifying the new one is in use.
- Do not log secret values at any level — log only the secret ID and version.
- Stop and ask the user if a consumer cannot support the key-chain pattern — the rotation must be a deploy.
- If the secret is a TLS private key, coordinate with the certificate authority's validity window.
- Never automate rotation without a tested rollback — manual rotation first, automation second.
- If the rotation affects production auth, schedule it during low-traffic hours and notify on-call.
