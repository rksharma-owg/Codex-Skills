---
id: cloud-workload-identity-migrator
name: Cloud Workload Identity Migrator
category: cloud-security
difficulty: Advanced
tags:
  - cloud-security
  - ecr
  - eks
  - github-actions
  - kubernetes
summary: |
  This Codex skill migrates workloads from long-lived service account keys to workload identity federation (AWS IRSA, GCP Workload Identity, Azure Managed Identity, Kubernetes OIDC federation).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill migrates workloads from long-lived service account keys to workload identity federation (AWS IRSA, GCP Workload Identity, Azure Managed Identity, Kubernetes OIDC federation). It targets the failure mode of a leaked service account key that grants persistent access to an attacker.

## When to Use

Use when introducing workload identity, after a key exposure incident, when migrating CI/CD from long-lived keys to OIDC federation, or as part of a zero-trust initiative.

## Codex Instructions

1. Inventory workloads using long-lived keys: CI/CD pipelines (GitHub Actions, GitLab CI), Kubernetes pods with service account keys, on-prem apps with cloud keys.
2. For each workload, identify the cloud role and permissions the key grants.
3. Choose the identity federation mechanism: AWS IRSA for EKS, GCP Workload Identity for GKE, OIDC federation for GitHub Actions, Managed Identity for Azure.
4. Configure the trust relationship: the workload's OIDC issuer is the only trusted principal.
5. Update the workload to obtain short-lived credentials via AssumeRoleWithWebIdentity or the equivalent.
6. Verify the workload can access the required cloud resources with the new short-lived credentials.
7. Remove the long-lived key from the workload and the cloud provider.
8. Monitor for any code path that still references the old key (env vars, files); clean up.
9. Document the migration in the team's runbook so future workloads follow the pattern.
10. Output a migration runbook with per-workload steps and verification queries.

## Inputs Needed

- Workload inventory (CI/CD, Kubernetes, on-prem apps)
- Cloud provider(s) and current auth method (long-lived keys, instance profiles)
- OIDC issuer URL for the workload (GitHub Actions, GitLab CI, internal OIDC)
- Cloud role and permissions required by each workload
- Existing IRSA / Workload Identity setup

## Expected Output

A Markdown migration runbook with: (1) Workload Inventory; (2) Per-workload Migration Steps; (3) Trust Relationship config; (4) Verification Queries; (5) Key Deletion Checklist; (6) Monitoring Alert spec for failed credential exchange.

## Example Prompt

> Migrate our GitHub Actions CI/CD from long-lived AWS access keys to OIDC federation. We have 12 workflows using the same key with admin access. Configure the trust relationship for github.com/<org>, create least-privilege roles per workflow, and produce the migration runbook with verification and key deletion steps.

## Safety Rules

- Never delete a long-lived key before verifying the workload can obtain short-lived credentials.
- Do not grant the new role broader permissions than the old key — least privilege always.
- Stop and ask the user if the workload's OIDC issuer is unknown — federation cannot be set up without it.
- If the migration breaks a production deploy, restore the key and investigate.
- Never log the short-lived credentials — log only the role ARN and the request ID.
- If the workload runs outside a supported platform (legacy on-prem), recommend a secrets manager with rotation instead of federation.
