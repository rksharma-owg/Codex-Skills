---
id: iac-misconfig-detector
name: IaC Misconfig Detector
category: cybersecurity
difficulty: Intermediate
tags:
  - checkov
  - cis
  - csp
  - cwe
  - cybersecurity
  - helm
  - iam
  - iso-27001
  - kubernetes
  - nist
summary: |
  This Codex skill detects misconfigurations in Infrastructure-as-Code (Terraform, CloudFormation, Pulumi, Helm, Kustomize, ARM, Bicep, Ansible, Serverless Framework) before they reach the cloud.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill detects misconfigurations in Infrastructure-as-Code (Terraform, CloudFormation, Pulumi, Helm, Kustomize, ARM, Bicep, Ansible, Serverless Framework) before they reach the cloud. It exists because Gartner estimates that through 2026, 99% of cloud security failures will be the customer's fault — and the overwhelming majority originate in IaC that ships an S3 bucket public, a security group open to `0.0.0.0/0`, an unencrypted disk, or an over-permissive IAM policy. Catching these pre-deploy is dramatically cheaper than remediating in the cloud.

## When to Use
Run this skill on every PR that touches `*.tf`, `*.tf.json`, `template.yaml`, `*.json` CloudFormation, `Chart.yaml`, `values.yaml`, `*.bicep`, or `playbook.yml`. Also use it before a `terraform apply` in a new environment, during cloud migration planning, when adopting a new module from the Terraform Registry, or as part of a CSPM (Cloud Security Posture Management) audit reconciliation.

## Codex Instructions
1. Detect the IaC framework(s) by file extension and manifest: `.tf`/`.tf.json` (Terraform), `template.yaml`/`*.json` with `Resources` (CloudFormation), `Chart.yaml` (Helm), `*.bicep` (Bicep), `playbook.yml` (Ansible), `serverless.yml` (Serverless Framework), `Pulumi.yaml` (Pulumi).
2. Run `checkov -d <path> --framework <fw> --output json` and `tfsec <path>` (now part of Trivy) as parallel scanners; reconcile findings by resource address.
3. Run `kubectl score` and `kube-linter` against rendered Helm charts (use `helm template` first).
4. Run `cfn-nat` or `cfn-lint` against CloudFormation templates with the security ruleset enabled.
5. For each finding, capture: resource address (`aws_s3_bucket.public`), provider, rule ID (e.g., `CKV_AWS_20`), severity, CIS / NIST 800-53 control mapping, and the offending attribute.
6. Build the cloud-specific checks for the target provider (AWS, Azure, GCP, Kubernetes, OCI) — do not run AWS checks against an Azure IaC tree.
7. Cross-reference IAM policies with `parliament` (AWS) or `azjson` (Azure) to detect `Action: "*"` on `Resource: "*"`, missing conditions, and privilege-escalation-prone actions (e.g., `iam:PassRole`, `sts:AssumeRole`, `lambda:CreateFunction`).
8. Re-baseline severity based on environment: a public S3 bucket in `dev` is High; in `prod` with PII is Critical. If environment is unspecified, default to prod-equivalent.
9. Recommend a corrected snippet per finding; where possible, point to the matching module from the Terraform Registry or AWS-native module that resolves the issue by construction.
10. Map each finding to CWE: CWE-284 (Improper Access Control), CWE-732 (Incorrect Permission Assignment), CWE-311 (Missing Encryption of Sensitive Data), CWE-693 (Protection Mechanism Failure).
11. Emit the report as `IAC_SCAN.md` plus SARIF for upload to GitHub code scanning.

## Inputs Needed
- IaC root directory path
- Framework(s) in use (or accept auto-detection)
- Target cloud provider(s): AWS, Azure, GCP, Kubernetes, OCI, Alibaba
- Target environment: dev, staging, prod, sandbox (affects severity)
- Existing state file or remote state backend (read-only — for `terraform plan` correlation)
- Module allowlist (if your org restricts which Terraform Registry modules may be used)
- Compliance driver (CIS Benchmarks, NIST 800-53, PCI DSS, ISO 27001, FedRAMP)
- Prior exception list (so accepted risks aren't re-flagged in CI)

## Expected Output
A markdown report `IAC_SCAN.md` with sections: Executive Summary (frameworks scanned, resource count, findings by severity and CIS/NIST control), Findings Table (ID, Severity, CWE, Rule ID, Resource Address, File:Line, Issue, Fix Snippet), IAM Analysis (policies flagged for over-permission, privilege-escalation risk), Kubernetes-Specific (if applicable: privileged containers, hostPath, no liveness probe), and Compliance Mapping (CIS Benchmark / NIST 800-53 control coverage). Severity scale: Critical / High / Medium / Low / Info. Emit `iac.sarif`.

## Example Prompt
> Scan the Terraform in `/home/z/my-project/infra-live/prod` (AWS-only, us-east-1). We're about to `terraform apply` a new VPC and S3 data lake. Map findings to CIS AWS Benchmark v3 and NIST 800-53 Rev. 5. Flag any IAM policy with `Resource: "*"` as Critical. Write `IAC_SCAN.md` and emit SARIF for GitHub code scanning.

## Safety Rules
- Never run `terraform apply`, `pulumi up`, `helm install`, or any mutating cloud command — read-only analysis only.
- Do not modify IaC files in place; propose fixes as snippets in the report.
- Treat remote state as read-only; do not write or lock state files.
- If a finding would expose PII or regulated data (PCI, PHI) at Critical severity, do not downgrade it for any reason.
- Do not auto-suppress findings in `checkov`/`tfsec` suppression comments without explicit user approval.
- Map every IAM finding through `parliament` before reporting; raw `Action: "*"` findings can be benign in scoped admin roles.
- If the target environment is unspecified, default to the most conservative severity (prod + internet-facing).
- Never include real AWS account IDs, Azure subscription IDs, or project IDs in the report — mask them.
