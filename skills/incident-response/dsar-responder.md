---
id: dsar-responder
name: DSAR Responder
category: incident-response
difficulty: Intermediate
tags:
  - gdpr
  - incident-response
  - rds
  - s3
summary: |
  This Codex skill orchestrates the response to a Data Subject Access Request (DSAR): verify identity, locate all the user's personal data, export or delete per the request, and respond within the legal deadline (30 days for GDPR, 45 for CCPA).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill orchestrates the response to a Data Subject Access Request (DSAR): verify identity, locate all the user's personal data, export or delete per the request, and respond within the legal deadline (30 days for GDPR, 45 for CCPA).

## When to Use

Use when a user submits a DSAR (export, delete, correct), when the privacy team needs to track DSARs, or when an audit reveals DSAR response gaps.

## Codex Instructions

1. Receive the DSAR: user identity, request type (access, deletion, correction), submission channel.
2. Verify the user's identity: confirm via the account's primary email or a separate identity check.
3. Log the DSAR with a deadline (30 days for GDPR, 45 for CCPA).
4. Locate the user's personal data across all systems: primary database, analytics, logs, backups, third-party processors.
5. For an access request, export the data in a portable format (JSON, CSV) with a manifest.
6. For a deletion request, delete or anonymize the data across all systems; document systems where deletion is not possible (e.g., backups).
7. For a correction request, update the data and propagate to all systems.
8. Coordinate with third-party processors to fulfill the request on their side.
9. Verify the request is complete: a sample check across systems to confirm no residual data.
10. Respond to the user within the deadline with the result (export link, deletion confirmation, correction confirmation).

## Inputs Needed

- DSAR details (user, request type, submission channel)
- Identity verification mechanism
- Data inventory (where personal data is stored)
- Third-party processors that handle personal data
- DSAR tracking tool (OneTrust, Transcend, custom)

## Expected Output

A Markdown DSAR Response Report with: (1) DSAR details and deadline; (2) Identity verification result; (3) Data location results across systems; (4) Action taken (export, deletion, correction); (5) Third-party coordination status; (6) Verification check results; (7) Response sent to user with timestamp.

## Example Prompt

> Respond to a DSAR from user jdoe@example.com: delete my account and all my data. Verify identity via the account email. Locate data across Postgres, Snowflake, S3 logs, Segment, SendGrid. Delete or anonymize, coordinate with processors, verify no residual data, respond within 30 days.

## Safety Rules

- Never fulfill a DSAR without verifying the user's identity.
- Do not delete data subject to a legal hold — pause the deletion and notify legal.
- Stop and ask the user if the data location is incomplete — partial deletion is a compliance risk.
- If the deletion cannot be completed (e.g., backups), document the residual data and notify the user.
- Never log full personal data records during the DSAR — log only the user ID and the action taken.
- If the DSAR deadline cannot be met, notify the user and the supervisory authority before the deadline.
