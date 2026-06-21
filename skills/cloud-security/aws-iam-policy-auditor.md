---
id: aws-iam-policy-auditor
name: AWS IAM Policy Auditor
category: cloud-security
difficulty: Intermediate
tags:
  - cis
  - cloud-security
  - cloudtrail
  - iam
  - terraform
summary: |
  This Codex skill audits AWS IAM policies (managed and inline) for over-permissive statements: Action '*', Resource '*', Principal '*', missing conditions, and privilege escalation paths.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits AWS IAM policies (managed and inline) for over-permissive statements: Action '*', Resource '*', Principal '*', missing conditions, and privilege escalation paths. It maps each finding to CIS AWS Benchmark and produces least-privilege policy patches.

## When to Use

Use during IAM policy review, after a CloudTrail alert on suspicious API calls, before granting a third-party tool access, or quarterly as part of IAM hygiene.

## Codex Instructions

1. Pull all IAM policies in scope (customer-managed, inline on roles/users/groups) via AWS API or IaC files.
2. Parse each policy and identify statements with Action '*' or Resource '*'.
3. Identify statements with Effect Allow and no Condition (broadly trusted).
4. Cross-reference with CloudTrail access logs (IAM Access Analyzer) to find unused actions and resources.
5. Identify privilege escalation paths: iam:CreatePolicy, iam:PutRolePolicy, sts:AssumeRole chains that allow a principal to escalate to admin.
6. Identify cross-account access: Principal with an external AWS account ARN; verify the trust relationship is intended.
7. For each finding, propose a least-privilege replacement using the actions observed in CloudTrail over the last 90 days.
8. Verify the proposed policy with the IAM Policy Simulator against the service's test cases.
9. Rank findings by severity: Critical (admin in production), High (data exfiltration), Medium (privilege escalation), Low (unused permissions).
10. Output the audit report and the patched policies ready to apply.

## Inputs Needed

- AWS account ID and region scope
- IAM policy source (live AWS API, CloudFormation, Terraform)
- CloudTrail access logs or IAM Access Analyzer output
- Whether the account is production
- Existing permission boundaries

## Expected Output

A Markdown report titled 'IAM Policy Audit' with: (1) Policy Inventory; (2) Findings table — Policy | Statement | Issue | Severity | Proposed Least-Privilege; (3) Privilege Escalation Paths; (4) Patched Policy JSON ready to apply.

## Example Prompt

> Audit all IAM policies in AWS account 123456789012. Pull from Terraform in infra/ and cross-reference with IAM Access Analyzer findings from the last 90 days. Flag every Action '*' and propose least-privilege replacements. Verify each patch with the IAM Policy Simulator.

## Safety Rules

- Never apply a policy change in production without a dry-run in staging.
- Do not remove a permission without verifying it is truly unused via CloudTrail — services may use it on rare paths.
- Stop and ask the user if a cross-account trust is ambiguous — it may be intentional.
- If a role has admin privileges, flag it as Critical and require human sign-off before any change.
- Never log AWS access keys or session tokens.
- If the audit reveals a credential exposure, treat it as a security incident — rotate immediately.
