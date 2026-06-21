# HIPAA PHI Handler

## Purpose

This Codex skill designs the handling of Protected Health Information (PHI) in an application: minimum necessary access, encryption at rest and in transit, audit logging, Business Associate Agreements (BAAs) with vendors, and breach notification readiness.

## When to Use

Use when launching a healthcare feature, when onboarding a new vendor that touches PHI, after a PHI exposure incident, or before a HIPAA compliance audit.

## Codex Instructions

1. Identify where PHI is collected, stored, processed, and transmitted in the application.
2. Verify encryption at rest: AES-256 with KMS-managed keys for all PHI storage (databases, S3, EBS).
3. Verify encryption in transit: TLS 1.2+ for all PHI transmission, including internal service-to-service.
4. Implement minimum necessary access: role-based access control, with PHI access logged per access.
5. Implement audit logging: who accessed what PHI when, retained for 6 years per HIPAA.
6. Verify BAAs are in place with all vendors that touch PHI (cloud provider, analytics, email).
7. Implement a breach notification process: detect, assess, notify affected individuals within 60 days, HHS notification.
8. Implement a data retention policy: PHI is kept only as long as needed, then securely deleted.
9. Plan for the patient's right to access, amend, and request restriction of their PHI.
10. Output the PHI handling design, the access control matrix, and the breach notification runbook.

## Inputs Needed

- Application architecture and PHI flow
- Vendors that touch PHI (with BAA status)
- Existing encryption and access control implementation
- Audit logging infrastructure
- Retention policy and legal hold process

## Expected Output

A Markdown PHI Handling Report with: (1) PHI Inventory and flow; (2) Encryption Matrix (at rest, in transit); (3) Access Control Matrix; (4) Audit Logging design; (5) BAA Status per vendor; (6) Breach Notification Runbook; (7) Retention and Deletion policy.

## Example Prompt

> Design PHI handling for our telehealth app. PHI flow: intake form (web), video consult (Twilio), EHR sync (Epic FHIR), storage (Postgres, S3). Vendors: AWS, Twilio, Epic. Verify encryption, RBAC with audit logging, BAA status, breach notification process. We're preparing for a HIPAA compliance audit.

## Safety Rules

- Never store PHI unencrypted at rest.
- Do not transmit PHI over a non-TLS channel.
- Stop and ask the user if a vendor's BAA is not in place — processing must pause.
- If PHI is found in logs, treat it as a breach and follow the notification process.
- Never log full PHI records at any level — redact or pseudonymize.
- If the application handles mental health or substance abuse records, additional 42 CFR Part 2 requirements apply.
