---
id: gdpr-data-flow-mapper
name: GDPR Data Flow Mapper
category: cloud-security
difficulty: Advanced
tags:
  - cloud-security
  - gdpr
  - rds
  - s3
summary: |
  This Codex skill maps the flow of personal data through an application: collection points, storage locations, processors (third parties), retention periods, and cross-border transfers.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill maps the flow of personal data through an application: collection points, storage locations, processors (third parties), retention periods, and cross-border transfers. It supports GDPR Article 30 record-of-processing and DSAR response.

## When to Use

Use when launching a feature that processes personal data, before a GDPR audit, when responding to a DSAR, or when onboarding a new third-party processor.

## Codex Instructions

1. Identify the personal data types processed: name, email, IP, location, behavioral, special category.
2. Map collection points: web forms, mobile app inputs, cookies, third-party imports.
3. Map storage locations: databases, object storage, log aggregators, data warehouses, backups.
4. Map processors: third parties that process personal data on the org's behalf (analytics, CRM, email).
5. Map retention periods: how long each data type is kept, the legal basis, the deletion mechanism.
6. Map cross-border transfers: data leaving the EU/EEA, the transfer mechanism (SCCs, adequacy decision, BCRs).
7. Identify the legal basis for each processing purpose: consent, contract, legitimate interest, legal obligation.
8. Document the data flow in a diagram and a register, ready for the supervisory authority's review.
9. Flag any data flow without a documented legal basis or retention period — these are compliance gaps.
10. Output the data flow map, the processing register, and the gap list.

## Inputs Needed

- Application architecture and data flow
- List of third-party processors with their DPA
- Existing privacy policy and consent records
- Retention policy
- Cross-border transfer mechanisms in use

## Expected Output

A Markdown GDPR Data Flow Report with: (1) Personal Data Inventory; (2) Collection Points; (3) Storage Map; (4) Processors List with DPA references; (5) Retention Matrix; (6) Cross-Border Transfers; (7) Legal Basis per purpose; (8) Compliance Gaps.

## Example Prompt

> Map the GDPR data flow for our SaaS app. Personal data: name, email, IP, usage behavior. Storage: Postgres, S3 logs, Snowflake warehouse. Processors: Stripe (payments), Segment (analytics), SendGrid (email). Retention: 24 months for usage data, indefinite for accounts. Identify gaps and produce the Article 30 register.

## Safety Rules

- Never process personal data without a documented legal basis.
- Do not transfer personal data outside the EU/EEA without a valid transfer mechanism.
- Stop and ask the user if a processor's DPA is not in place — processing must pause.
- If the map reveals personal data in logs, plan to redact or purge immediately.
- Never log full personal data records at INFO — redact or pseudonymize.
- If the map reveals a missing retention policy, escalate to DPO before continuing to process.
