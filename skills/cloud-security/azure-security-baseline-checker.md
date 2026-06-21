---
id: azure-security-baseline-checker
name: Azure Security Baseline Checker
category: cloud-security
difficulty: Intermediate
tags:
  - cloud-security
  - ecr
  - iso-27001
  - rds
  - soc-2
  - vault
summary: |
  This Codex skill checks an Azure subscription against the Azure Security Benchmark: MFA on all accounts, no legacy auth, disk encryption, NSG on subnets, Key Vault for secrets, Defender for Cloud enabled, and activity log alerts for sensitive operations.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill checks an Azure subscription against the Azure Security Benchmark: MFA on all accounts, no legacy auth, disk encryption, NSG on subnets, Key Vault for secrets, Defender for Cloud enabled, and activity log alerts for sensitive operations.

## When to Use

Use when onboarding a new Azure subscription, before a compliance audit, or quarterly as part of Azure security hygiene.

## Codex Instructions

1. Pull the subscription's security posture via Microsoft Defender for Cloud Secure Score.
2. Verify all user accounts have MFA enforced (Azure AD Conditional Access).
3. Verify legacy authentication (POP3, IMAP, SMTP) is blocked for Exchange Online.
4. Verify all VM disks are encrypted (Azure Disk Encryption or platform-managed key).
5. Verify every subnet has a Network Security Group with default-deny inbound.
6. Verify Key Vault is used for all secrets (storage account keys, DB passwords, certificates).
7. Verify Microsoft Defender for Cloud is enabled for all relevant resource types (VMs, SQL, Storage, Containers).
8. Verify activity log alerts exist for sensitive operations: rule creation, security group changes, key vault access.
9. Verify Azure Policy assignments enforce the baseline (e.g., 'Audit no disk encryption').
10. Output a baseline compliance report with a per-control finding table.

## Inputs Needed

- Azure subscription ID
- Tenant ID
- Whether the user has Reader + Security Reader roles
- Compliance requirement (ISO 27001, SOC 2, FedRAMP)
- Existing Azure Policy assignments

## Expected Output

A Markdown report titled 'Azure Security Baseline' with: (1) Control Matrix — Control | Status | Affected Resources | Fix; (2) Defender for Cloud Secure Score breakdown; (3) Azure Policy Recommendations; (4) Remediation Plan.

## Example Prompt

> Check Azure subscription abcd1234-... against the Azure Security Benchmark. Verify MFA, disk encryption, NSG on subnets, Key Vault usage, Defender for Cloud, and activity log alerts. We're targeting ISO 27001 compliance. Produce a remediation plan.

## Safety Rules

- Never modify Conditional Access policies in production without explicit user approval.
- Do not enable Defender for Cloud paid tiers without confirming the budget impact.
- Stop and ask the user if a VM's disk encryption cannot be enabled (legacy VM size).
- If a Key Vault is found with public access, restrict it immediately and notify the owner.
- Never log Key Vault secret values — log only the secret name and version.
- If the subscription is in a multi-tenant environment, verify cross-tenant access policies.
