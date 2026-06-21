# GCP IAM Recommender

## Purpose

This Codex skill uses GCP's IAM Recommender and additional analysis to identify over-permissive IAM bindings, service accounts with unused keys, and workloads running with default service accounts. It maps each finding to least-privilege recommendations.

## When to Use

Use during GCP IAM review, when onboarding a new GCP project, after a security audit, or when reducing blast radius of compromised service accounts.

## Codex Instructions

1. Pull IAM policy bindings for the project (and folder/org level if accessible).
2. Identify bindings with role 'roles/owner' or 'roles/editor' — flag for review.
3. Identify service accounts with > 10 keys — flag unused keys for deletion.
4. Identify workloads (GKE, Compute Engine) running with the default service account — recommend a dedicated least-privilege SA.
5. Identify service accounts with no key age limit — recommend workload identity federation instead.
6. Use the IAM Recommender API to pull Google's least-privilege recommendations for each binding.
7. Cross-reference with Cloud Audit Logs to identify unused permissions in the last 90 days.
8. Identify external principals (user@external.com) with project access; verify the access is intended.
9. Recommend Workload Identity Federation for CI/CD pipelines instead of long-lived service account keys.
10. Output an IAM hygiene report with a prioritized remediation plan.

## Inputs Needed

- GCP project ID (and folder/org ID)
- Whether the user has resourcemanager.projects.getIamPolicy
- Cloud Audit Logs access for unused-permission analysis
- Existing workload identity federation setup
- Compliance requirement (if applicable)

## Expected Output

A Markdown report titled 'GCP IAM Hygiene Report' with: (1) Bindings Inventory; (2) Findings table — Principal | Role | Issue | Recommendation; (3) Service Account Key Audit; (4) Workload Identity Federation Recommendations.

## Example Prompt

> Review IAM for GCP project my-prod-project. Pull bindings, flag roles/owner and roles/editor, identify service accounts with > 10 keys, and pull IAM Recommender suggestions. We want to migrate all CI/CD to Workload Identity Federation. Produce a remediation plan.

## Safety Rules

- Never delete a service account key without confirming it is not used by a production service.
- Do not change a GKE workload's service account without a rolling restart plan.
- Stop and ask the user if a binding's principal is external — verify intent.
- If a service account has admin privileges, flag as Critical and require human sign-off.
- Never log service account key contents — log only the key ID and age.
- If a workload identity federation migration may break CI/CD, test in a non-prod project first.
