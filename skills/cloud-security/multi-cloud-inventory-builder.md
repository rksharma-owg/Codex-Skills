---
id: multi-cloud-inventory-builder
name: Multi-Cloud Inventory Builder
category: cloud-security
difficulty: Intermediate
tags:
  - cloud-security
  - csp
  - iam
  - rds
  - s3
summary: |
  This Codex skill builds a unified inventory of resources across AWS, Azure, and GCP: compute, storage, network, IAM, and databases.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill builds a unified inventory of resources across AWS, Azure, and GCP: compute, storage, network, IAM, and databases. The inventory feeds cost optimization, security posture management, and compliance audits. It targets the failure mode of shadow resources that no one knows exist.

## When to Use

Use when onboarding to a CSPM (Cloud Security Posture Management) tool, before a multi-cloud audit, or quarterly to catch shadow resources.

## Codex Instructions

1. Configure read-only credentials for each cloud (AWS IAM role, Azure service principal, GCP service account).
2. Pull compute inventory: EC2/VMs/Compute Engine instances, containers, serverless functions.
3. Pull storage inventory: S3/Blob/Cloud Storage buckets, EBS/disks, file shares.
4. Pull network inventory: VPCs, subnets, security groups, load balancers, public IPs.
5. Pull IAM inventory: users, roles, service accounts, policies, access keys.
6. Pull database inventory: RDS, Cloud SQL, Azure SQL, self-managed DBs.
7. Normalize resource attributes: ARN, region, tags, owner, creation time, last-used time.
8. Identify orphaned resources: unattached disks, idle load balancers, unused elastic IPs, IAM keys not used in 90 days.
9. Export the inventory to a structured format (JSON, CSV, or a database) for tooling integration.
10. Output a summary report with cloud-by-cloud counts, top 10 orphaned resources, and a tagging compliance check.

## Inputs Needed

- Cloud accounts in scope (AWS account IDs, Azure subscription IDs, GCP project IDs)
- Read-only IAM credentials for each cloud
- CSPM tool in use (Wiz, Prisma Cloud, Defender for Cloud) or 'standalone'
- Tagging policy (required tags, owner attribute)
- Output format (JSON, CSV, database)

## Expected Output

A Markdown summary report with: (1) Resource Counts per cloud; (2) Orphaned Resources table; (3) Tagging Compliance matrix; (4) Recommended CSPM integration; (5) Structured inventory export (JSON/CSV).

## Example Prompt

> Build a unified inventory across our AWS (3 accounts), Azure (2 subscriptions), and GCP (5 projects) environments. Use read-only credentials. Identify orphaned resources (unattached disks, idle LBs, unused IAM keys > 90 days) and produce a tagging compliance report. Export the inventory as JSON.

## Safety Rules

- Never use admin credentials for inventory — read-only is sufficient and safer.
- Do not log credentials or sensitive resource metadata (e.g., database contents).
- Stop and ask the user if a resource's owner tag is missing — do not assume.
- If the inventory reveals an unexpected external principal, escalate to security.
- Never expose the inventory publicly — it is an attacker reconnaissance goldmine.
- If the inventory is shared with a third-party CSPM, verify the data sharing agreement.
