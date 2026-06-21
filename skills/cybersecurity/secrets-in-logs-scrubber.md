---
id: secrets-in-logs-scrubber
name: Secrets in Logs Scrubber
category: cybersecurity
difficulty: Intermediate
tags:
  - cwe
  - cybersecurity
  - docker
  - ecr
  - gdpr
  - github-actions
  - hipaa
  - jwt
  - pci
  - rds
summary: |
  This Codex skill audits application logs, CI/CD pipeline logs, container logs, and observability pipelines (stdout, file, ELK, Splunk, Datadog, Loki, CloudWatch) for leaked secrets, PII, and regulated data — and proposes a scrubbing/redaction pipeline that runs before logs leave the host.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill audits application logs, CI/CD pipeline logs, container logs, and observability pipelines (stdout, file, ELK, Splunk, Datadog, Loki, CloudWatch) for leaked secrets, PII, and regulated data — and proposes a scrubbing/redaction pipeline that runs before logs leave the host. It exists because logs are the most common exfiltration channel in real breaches (per Mandiant M-Trends) and because most logging libraries ship with no redaction by default, leaving API keys, JWTs, passwords, SSNs, and PANs in plain text in indexes that operators, SREs, and sometimes attackers can read.

## When to Use
Run this skill when adding a new logging pipeline, after a log-integration incident (e.g., a developer queries Datadog for `authorization:` and finds 4,000 leaked tokens), during PCI DSS or HIPAA audit prep, when introducing a new PII field into the data model, or when migrating from one SIEM to another. Also use it as a periodic compliance check on hot log indices.

## Codex Instructions
1. Identify all log emission surfaces: application logs (winston, pino, log4j, logback, structlog, slf4j, zap, serilog), access logs (nginx, envoy, ALB), CI/CD logs (GitHub Actions, GitLab CI, Jenkins), container stdout/stderr captured by Docker/k8s, and observability SDK calls (Datadog `dogstatsd`, OpenTelemetry attributes, Sentry breadcrumbs, Honeycomb events).
2. Run a pattern-based sweep over a representative log sample (≥10,000 lines if available) using signatures for: AWS keys, Stripe keys, Slack tokens, GitHub PATs, private keys, JWTs, `password=`, `Authorization: Bearer`, `api_key=`, `set-cookie:`, email addresses, US SSNs, credit-card PANs (Luhn-validated), IBANs, phone numbers (E.164).
3. Run entropy-based detection on quoted strings >20 chars with Shannon entropy >4.5; cross-check against known benign high-entropy fields (UUIDs, request IDs, hashes).
4. For each finding, capture: log source, sample line (masked), pattern matched, count in sample window, projected daily volume (if log rate is provided).
5. Categorize by data class: secrets (Critical), PII regulated under GDPR/HIPAA (High), PCI PAN (Critical, requires PCI DSS 3.4 response), authentication tokens (Critical), internal-only sensitive data (Medium), non-regulated PII (Low).
6. Map each finding to CWE-532 (Insertion of Sensitive Information into Log File) and, where applicable, CWE-532 + CWE-359 (Exposure of Private Personal Information).
7. Propose a layered scrubbing pipeline: (a) library-level redaction (winston `format`, logback `<MaskingPatternLayout>`, structlog `processor`, zap `Encoder`); (b) log-shipper-level redaction (Fluentd `grep`/`record_transformer`, Vector `remap` VRL, Filebeat processors, Logstash `mutate`); (c) SIEM-level query-time masking (Splunk `SEDC`, Datadog sensitive-data scanner, ELK `ingest` pipeline).
8. Recommend an allowlist-over-denylist approach: define the set of fields that ARE allowed in logs (request ID, route, status code, duration); redact everything else by default. This is far more robust than enumerating every secret type.
9. Recommend a regression check: a CI job that runs `gitleaks` or `trufflehog` against a sample of CI logs from the last 7 days and fails on any finding.
10. Emit `LOGS_SCRUB_REPORT.md` with the findings table, the proposed redaction config per layer, and the CI regression-check definition.

## Inputs Needed
- Log source(s): application, access, CI/CD, container, observability
- Representative log sample (file path or paste), ideally ≥10k lines
- Logging library/stack in use (winston, log4j, Fluentd, Vector, Splunk, Datadog, Loki, CloudWatch)
- Compliance driver (PCI DSS, HIPAA, GDPR, CCPA, SOC 2)
- Data-classification map of fields the app handles (PII, PHI, PAN, secrets)
- SIEM/log-index retention window
- Existing redaction config (so the audit can flag gaps, not redo work)
- Whether logs are exported to a third-party (Datadog, Splunk Cloud, New Relic) — affects exposure severity

## Expected Output
A markdown report `LOGS_SCRUB_REPORT.md` with sections: Executive Summary (log sources audited, total findings by data class, top 3 leak patterns), Sample Findings Table (ID, Severity, CWE, Data Class, Pattern, Log Source, Sample Count, Projected Daily Volume, Sample Line [masked]), Layered Redaction Plan (library, shipper, SIEM — with concrete config snippets per layer), Allowlist-over-Denylist Schema (the recommended allowed-fields list), and CI Regression Check (the job definition). Severity scale: Critical (secrets, PAN, live tokens) / High (regulated PII/PHI in volume) / Medium (internal-sensitive) / Low (non-regulated PII, low volume). Also emit `redaction-rules.yaml` containing the recommended shipper-level rules.

## Example Prompt
> Audit our logging for leaked secrets and PII. Sample is at `/tmp/prod-logs-sample.json` — 50k JSON lines from our FastAPI app shipping via Fluentd to Datadog. We're PCI DSS scoped and handle customer email + phone. Identify what's leaking, propose a Fluentd `record_transformer` redaction config plus a Datadog sensitive-data-scanner rule set, and emit `LOGS_SCRUB_REPORT.md` plus `redaction-rules.yaml`.

## Safety Rules
- Never include real secret values or real PII in the report; mask everything except the last 2 characters, and substitute `[REDACTED-PII]` for SSNs/PANs/PHI.
- Do not query production SIEM APIs to gather samples; require the user to provide a sample.
- Do not modify production logging pipelines or redaction configs autonomously; propose them for review.
- If PCI PAN is detected in logs, treat as Critical regardless of volume and reference PCI DSS Req. 3.4 (mask PAN on display).
- If PHI is detected, reference HIPAA 45 CFR §164.312(b) audit controls and §164.502 use/disclosure limits.
- Do not recommend redacting audit logs themselves in a way that breaks non-repudiation (e.g., do not redact the actor identity or the action taken in a security audit log).
- For CI logs, treat any leaked OIDC token, GitHub PAT, or cloud AssumeRole credential as Critical and recommend immediate rotation.
- Never transmit the log sample to any external endpoint — analysis is local only.
