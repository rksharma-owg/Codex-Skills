# Cloud Secret Manager Migrator

## Purpose

This Codex skill migrates secrets from scattered sources (env vars, .env files, hardcoded values, Kubernetes Secrets in plaintext) to a centralized secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, HashiCorp Vault) with zero downtime and a verifiable rollback.

## When to Use

Use when introducing a secrets manager, when consolidating secrets after an acquisition, or when remediating a finding that secrets are stored in plaintext.

## Codex Instructions

1. Inventory current secrets: env vars, .env files, Kubernetes Secrets, hardcoded values in source.
2. Choose the target secret manager based on cloud provider and existing tooling.
3. For each secret, plan the migration: create in the manager, update the app to fetch at startup, verify, remove the old source.
4. For apps that cannot fetch at startup (legacy), use a sidecar or init container that writes the secret to a tmpfs file.
5. For Kubernetes, use the External Secrets Operator to sync from the manager to a Kubernetes Secret, with the Secret remaining the source of truth for the app.
6. Plan the rotation strategy for each secret (key-chain for zero-downtime).
7. Define the rollback procedure: revert the app to read from the old source if the manager is unavailable.
8. Verify the manager's IAM permissions: only the app's role can read the specific secret.
9. Add monitoring: alert if the app fails to fetch the secret at startup.
10. Output a migration runbook with per-secret steps and a verification checklist.

## Inputs Needed

- Target secret manager (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Vault)
- Current secret sources (env vars, .env, K8s Secrets, hardcoded)
- App's runtime and whether it supports fetching secrets at startup
- IAM/identity provider for the app (IRSA, Workload Identity, Pod Identity)
- Existing rotation strategy

## Expected Output

A Markdown migration runbook with: (1) Secret Inventory; (2) Per-secret Migration Steps; (3) External Secrets Operator config (if Kubernetes); (4) Verification Checklist; (5) Rollback Procedure; (6) Monitoring Alert spec.

## Example Prompt

> Migrate secrets from .env files and Kubernetes Secrets to AWS Secrets Manager for our EKS-hosted services. Use IRSA for auth and External Secrets Operator for sync. Plan zero-downtime migration for the database password (key-chain pattern) and rollback if Secrets Manager is unavailable.

## Safety Rules

- Never commit a secret value to git during migration — use the manager's CLI or console.
- Do not delete the old secret source until the new one is verified in use.
- Stop and ask the user if the app cannot fetch at startup — the sidecar approach adds complexity.
- If the secret is a TLS private key, verify the new manager's access logs are enabled.
- Never log secret values during migration — log only the secret ARN and version.
- If the migration affects production auth, schedule during low-traffic hours and notify on-call.
