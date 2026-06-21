---
id: data-retention-policy-enforcer
name: Data Retention Policy Enforcer
category: incident-response
difficulty: Intermediate
tags:
  - gdpr
  - hipaa
  - incident-response
  - pci
  - rds
  - soc-2
summary: |
  This Codex skill designs and implements a data retention policy: per-data-type retention periods, automated deletion mechanisms, legal hold exceptions, and audit logging of deletions.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs and implements a data retention policy: per-data-type retention periods, automated deletion mechanisms, legal hold exceptions, and audit logging of deletions. It targets the compliance requirement to not keep data longer than necessary.

## When to Use

Use when launching a new data type, before a GDPR/CCPA audit, when a customer requests deletion, or when storage costs from over-retention become significant.

## Codex Instructions

1. Inventory the data types: user accounts, transaction records, logs, analytics events, backups.
2. For each data type, define the retention period based on legal, business, and compliance requirements.
3. Define the deletion mechanism: hard delete, anonymization, archival to cold storage.
4. Implement automated deletion jobs: scheduled, idempotent, with audit logging.
5. Implement a legal hold mechanism: when a hold is active, deletion is paused for the affected data.
6. Define the customer deletion flow (right to be forgotten): verify identity, delete or anonymize, confirm.
7. Verify backups: deleted data must age out of backups within the backup retention period.
8. Verify logs: deleted data must be redacted or purged from logs (challenging — design for it).
9. Document the retention policy in a single source of truth, accessible to the privacy team.
10. Output the retention policy, the deletion job design, and the audit log schema.

## Inputs Needed

- Data type inventory
- Legal and compliance retention requirements (GDPR, HIPAA, PCI, SOC 2)
- Existing deletion mechanisms
- Legal hold process (when is it triggered, who authorizes)
- Backup retention periods

## Expected Output

A Markdown Data Retention Policy with: (1) Data Type to Retention Period matrix; (2) Deletion Mechanism per data type; (3) Legal Hold process; (4) Customer Deletion flow; (5) Audit Log schema; (6) Implementation Plan for automated deletion jobs.

## Example Prompt

> Design a data retention policy for our SaaS app. Data types: user accounts (delete on request), transactions (7 years for tax), application logs (90 days), analytics events (24 months), backups (30 days). Implement automated deletion jobs in Python, with legal hold support. GDPR-compliant customer deletion flow.

## Safety Rules

- Never delete data subject to a legal hold — pause deletion and notify legal.
- Do not weaken retention to 'save storage' — retention is a compliance requirement.
- Stop and ask the user if a data type's retention is ambiguous — over-retention is a compliance risk.
- If a deletion job fails, alert immediately — failed deletions are audit findings.
- Never log full data records before deletion — log only the ID and the deletion timestamp.
- If the customer deletion flow cannot fully delete (e.g., backups), document the residual risk to the customer.
