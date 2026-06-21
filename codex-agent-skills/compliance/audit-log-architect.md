# Audit Log Architect

## Purpose

This Codex skill designs an audit logging system that meets compliance requirements (SOC 2, HIPAA, PCI): what to log, the log format, tamper-evidence, retention, and access control. It targets the failure mode of logs that exist but are insufficient for an audit.

## When to Use

Use when launching a new system, before a compliance audit, after a log-related audit finding, or when introducing a SIEM.

## Codex Instructions

1. Identify the auditable events: authentication, authorization, data access, configuration changes, admin actions.
2. Define the log format: timestamp (UTC), actor (user, service), action, resource, result, IP, request ID.
3. Define tamper-evidence: append-only storage (CloudWatch Log Insights with delete protection, S3 with object lock).
4. Define retention: 1 year for SOC 2, 6 years for HIPAA, 1 year for PCI — whichever is longest.
5. Define access control: only the security team can read audit logs; no one can modify.
6. Define the SIEM integration: forward audit logs to Splunk, Datadog, or a SIEM for correlation and alerting.
7. Define alerting: alert on suspicious patterns (admin action outside business hours, mass data export).
8. Define the audit trail for a sample event: from the user action to the log entry to the SIEM alert.
9. Verify the log format is parseable and the SIEM dashboards work.
10. Output the audit log design, the implementation plan, and the SIEM integration.

## Inputs Needed

- Compliance requirements (SOC 2, HIPAA, PCI)
- Existing logging infrastructure
- SIEM in use (Splunk, Datadog, ELK)
- Audit log storage (CloudWatch, S3 with object lock)
- Security team's access to audit logs

## Expected Output

A Markdown Audit Log Design with: (1) Auditable Events list; (2) Log Format spec; (3) Tamper-Evidence mechanism; (4) Retention Policy; (5) Access Control matrix; (6) SIEM Integration; (7) Alerting rules; (8) Sample Audit Trail.

## Example Prompt

> Design an audit logging system for our SaaS app targeting SOC 2 + HIPAA. Events: login, data access, admin actions, config changes. Format: JSON with timestamp, actor, action, resource, IP, request ID. Tamper-evidence via S3 object lock. Retention 6 years. Forward to Splunk. Alert on admin actions outside business hours.

## Safety Rules

- Never log credentials, secrets, or full PII in audit logs — redact or hash.
- Do not store audit logs on the same system as the production data — a compromise can alter both.
- Stop and ask the user if a compliance retention requirement is ambiguous.
- If the audit logs are found modifiable, treat it as a security finding — fix immediately.
- Never expose audit logs to non-security teams without a redaction layer.
- If the SIEM is unavailable, audit logs must still be retained in the primary store.
