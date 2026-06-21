---
id: cloud-backup-recovery-planner
name: Cloud Backup Recovery Planner
category: cloud-security
difficulty: Intermediate
tags:
  - cloud-security
  - gdpr
  - hipaa
  - pci
  - rds
  - s3
  - terraform
summary: |
  This Codex skill designs a backup and recovery plan for cloud workloads: RPO and RTO targets, backup types (snapshot, incremental, continuous), storage tiering, encryption, cross-region replication, restore testing, and retention policy.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a backup and recovery plan for cloud workloads: RPO and RTO targets, backup types (snapshot, incremental, continuous), storage tiering, encryption, cross-region replication, restore testing, and retention policy. It targets the failure mode of backups that exist but fail to restore when needed.

## When to Use

Use when launching a new stateful workload, after a backup restore failure, when preparing for a disaster recovery audit, or when introducing cross-region replication.

## Codex Instructions

1. Inventory stateful workloads: databases (RDS, Cloud SQL, self-managed), object storage (S3, GCS), file systems (EFS, NFS), queues with persistent state.
2. For each workload, define RPO (acceptable data loss) and RTO (acceptable downtime) targets.
3. Choose backup types: continuous (Point-in-Time Recovery for DBs), snapshots (hourly/daily), incremental (for cost optimization).
4. Choose storage tiering: hot (Standard) for the last 7 days, warm (Infrequent Access) for 30 days, cold (Glacier, Archive) for 1+ year.
5. Verify backups are encrypted with a KMS key distinct from the production data key (separation of duties).
6. Plan cross-region replication for DR: at least one region away from the primary, with a documented failover runbook.
7. Define retention: comply with regulatory minimums (e.g., 7 years for financial records) without over-retaining PII.
8. Schedule monthly restore tests in an isolated environment; verify the restore produces a working system.
9. Define the restore runbook: which backup, which region, which step-by-step commands, verification queries.
10. Output the backup plan and the IaC patch for backup policies (AWS Backup, GCP Backup, Azure Backup).

## Inputs Needed

- Workload inventory with criticality classification
- RPO/RTO targets per workload (or business-level targets to derive)
- Compliance retention requirements (PCI, HIPAA, GDPR)
- DR strategy (pilot light, warm standby, multi-region active-active)
- Existing backup tooling (AWS Backup, Velero, native DB snapshots)

## Expected Output

A Markdown backup plan with: (1) Workload RPO/RTO matrix; (2) Backup Configuration per workload; (3) Retention Policy; (4) Cross-Region Replication design; (5) Monthly Restore Test Plan; (6) Restore Runbook per workload; (7) IaC Patch.

## Example Prompt

> Design a backup and recovery plan for our AWS production workloads: RDS Postgres (transactions, RPO 5min, RTO 1hr), S3 (documents, RPO 24hr, RTO 4hr), EFS (user uploads, RPO 1hr, RTO 2hr). Cross-region replication to us-west-2. Monthly restore tests. HIPAA-compliant retention. Produce the plan and AWS Backup Terraform patch.

## Safety Rules

- Never delete a backup without confirming it is past retention — destroying backups may violate compliance.
- Do not recommend cross-region replication without verifying the destination region's compliance posture.
- Stop and ask the user if a workload's RPO/RTO is unknown — defaults may not match business needs.
- If a restore test fails, treat it as a finding — investigate before relying on the backup.
- Never log backup contents — log only the backup ID, size, and KMS key.
- If the workload handles regulated data, verify the backup's KMS key is in the same compliance boundary.
