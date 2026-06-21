---
id: dns-config-auditor
name: DNS Config Auditor
category: devops
difficulty: Intermediate
tags:
  - devops
  - rds
  - s3
summary: |
  This Codex skill audits DNS configuration for security and reliability: DNSSEC, CAA records (to restrict certificate authorities), SPF/DKIM/DMARC for email, CNAME flattening, low TTLs for failover, and stale records.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits DNS configuration for security and reliability: DNSSEC, CAA records (to restrict certificate authorities), SPF/DKIM/DMARC for email, CNAME flattening, low TTLs for failover, and stale records. It targets the failure mode of a misconfigured DNS that allows hijacking or phishing.

## When to Use

Use before launching a new domain, after a DNS provider migration, when an email deliverability issue arises, or as part of a domain security audit.

## Codex Instructions

1. Enumerate all DNS records for the target domain (A, AAAA, CNAME, MX, TXT, NS, SOA, CAA, DNSKEY, RRSIG).
2. Verify DNSSEC is enabled and the DS record at the parent zone matches the child's DNSKEY.
3. Verify CAA records restrict certificate issuance to authorized CAs (e.g., letsencrypt.org only).
4. Verify SPF (TXT), DKIM (TXT or CNAME), and DMARC (TXT) are configured for email authentication.
5. Verify DMARC policy is at least p=quarantine for the apex domain and p=reject for subdomains used for email.
6. Verify TTLs match the use case: low TTL (60-300s) for failover endpoints, higher TTL (3600s) for stable records.
7. Identify stale records: CNAMEs pointing to deleted services, A records pointing to released IPs.
8. Identify subdomain takeover risk: CNAMEs to services that no longer exist (Azure, Heroku, S3).
9. Verify the apex domain has an MX record only if it receives email; otherwise, null MX (MX 0 .).
10. Output a DNS audit report with findings and a remediation plan.

## Inputs Needed

- Domain name
- DNS provider (Route 53, Cloudflare, NS1)
- Email provider (Gmail, Microsoft 365, SendGrid) — affects SPF/DKIM
- Authorized certificate authorities
- Whether subdomains are managed by other teams

## Expected Output

A Markdown report titled 'DNS Security Audit' with: (1) Records Inventory; (2) Findings table — Record | Issue | Severity | Fix; (3) Remediation Plan with exact record updates; (4) Subdomain Takeover Risk assessment.

## Example Prompt

> Audit DNS for example.com. We use Cloudflare for DNS, Gmail for email, and Let's Encrypt for certificates. Verify DNSSEC, CAA records, SPF/DKIM/DMARC, and identify any subdomain takeover risks. Produce a remediation plan with exact record updates.

## Safety Rules

- Never delete a DNS record without confirming it is unused — deletion can cause outages.
- Do not weaken DMARC policy to 'fix' an email deliverability issue without investigating the root cause.
- Stop and ask the user if a subdomain is owned by another team — they may have legitimate records.
- If DNSSEC is being enabled, document the DS record propagation time and rollback procedure.
- Never publish a CAA record that allows a CA you do not have an account with — it widens attack surface.
- Do not recommend a low TTL on the apex NS records without coordinating with the registrar.
