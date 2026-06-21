# GitHub OIDC Cloud Federation Setup

## Purpose

This Codex skill sets up OIDC federation between GitHub Actions and a cloud provider (AWS, GCP, Azure) so workflows can authenticate without long-lived secrets. It targets the failure mode of a leaked AWS access key in a GitHub Actions log.

## When to Use

Use when introducing GitHub Actions, when migrating from long-lived keys to OIDC, after a key exposure incident, or as part of a zero-trust initiative.

## Codex Instructions

1. Identify the cloud provider and the role the workflow needs to assume.
2. Configure the cloud provider's identity provider: add GitHub Actions as an OIDC provider with the issuer URL https://token.actions.githubusercontent.com.
3. Configure the trust policy on the cloud role: restrict the subject to the specific repo and ref (e.g., repo:org/repo:ref:refs/heads/main).
4. Restrict the subject further if the workflow should only run on a specific environment.
5. Grant the role only the permissions the workflow needs — least privilege.
6. Update the GitHub Actions workflow to request the OIDC token and assume the role (aws-actions/configure-aws-credentials, google-github-actions/auth, azure/login).
7. Remove the long-lived key from the repo's secrets and from the cloud provider.
8. Test the workflow to verify it can authenticate and access the required resources.
9. Monitor the cloud's audit log for the role's usage to detect any unexpected access.
10. Output the cloud-side config (Terraform), the workflow YAML, and a verification checklist.

## Inputs Needed

- Cloud provider (AWS, GCP, Azure)
- GitHub repo and the workflow's trigger (push, PR, schedule)
- Permissions the workflow needs in the cloud
- Whether the workflow runs on a specific environment
- Existing long-lived secrets to remove

## Expected Output

Cloud-side config (Terraform for AWS IAM role + trust policy, GCP Workload Identity Pool, Azure Federated Identity), updated GitHub Actions workflow YAML, and a verification checklist.

## Example Prompt

> Set up OIDC federation between our GitHub Actions and AWS account 123456789012. The deploy workflow (push to main) needs to assume role arn:aws:iam::...:role/github-actions-deploy with S3 and ECR permissions. Restrict the trust to repo:org/repo:ref:refs/heads/main. Remove the AWS_ACCESS_KEY_ID secret after verification.

## Safety Rules

- Never use a wildcard subject (repo:org/*) in the trust policy — restrict to specific repos.
- Do not grant the role admin permissions — least privilege always.
- Stop and ask the user if the workflow's permissions are ambiguous.
- If the federation breaks a deploy, restore the long-lived key temporarily and investigate.
- Never log the OIDC token at any level — it is a short-lived credential.
- If the cloud account is in a regulated environment, verify the federation meets the compliance requirements.
