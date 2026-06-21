---
id: compromised-credential-responder
name: Compromised Credential Responder
category: incident-response
difficulty: Advanced
tags:
  - cloudtrail
  - iam
  - incident-response
  - oauth
  - rds
  - s3
summary: |
  This Codex skill orchestrates the response to a compromised credential: identify the scope (which systems the credential can access), revoke the credential, audit for unauthorized access, and reset all related credentials.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill orchestrates the response to a compromised credential: identify the scope (which systems the credential can access), revoke the credential, audit for unauthorized access, and reset all related credentials. It targets the failure mode of revoking one credential but missing others the attacker may have obtained.

## When to Use

Use when a credential (password, API key, session token, SSH key) is confirmed compromised, when a user reports a phishing click, or when an internal threat intel feed flags a leaked credential.

## Codex Instructions

1. Identify the compromised credential type: user password, API key, session token, SSH key, service account key.
2. Identify the scope: which systems, cloud accounts, and data the credential can access.
3. Revoke the credential immediately: password reset, API key deletion, session token invalidation, SSH key removal.
4. Audit CloudTrail, audit logs, and access logs for the time window since the credential was likely compromised (assume at least 30 days).
5. Identify unauthorized access: logins from unusual IPs, API calls not in the user's normal pattern, data downloads.
6. Identify persistence the attacker may have created: new IAM users, new SSH keys, new OAuth grants, new API keys.
7. Reset all related credentials: other credentials the user has, credentials for systems the attacker accessed.
8. Notify the user (if user credential) and the security team; for a service account, notify the service owner.
9. If the credential was used for customer data access, follow the breach notification process.
10. Output a response report with the scope, revocation actions, audit findings, and reset list.

## Inputs Needed

- Compromised credential type and value (or hash for verification)
- Estimated time of compromise
- Systems the credential can access
- CloudTrail and access log availability
- Breach notification process (if applicable)

## Expected Output

A Markdown response report with: (1) Credential Scope; (2) Revocation Actions with timestamps; (3) Audit Findings (unauthorized access, persistence); (4) Reset List (related credentials reset); (5) Notification Log; (6) Breach Notification status.

## Example Prompt

> Respond to a compromised AWS access key for user jdoe. Key was likely leaked 14 days ago based on a GitHub commit. Identify scope (jdoe has access to S3 buckets and RDS), revoke the key, audit CloudTrail for the last 14 days for unauthorized access, check for attacker-created persistence (new IAM users, new keys), reset jdoe's other credentials, and assess breach notification needs.

## Safety Rules

- Never delay revoking a compromised credential to 'investigate first' — revoke, then investigate.
- Do not log the compromised credential's value — log only the ID and a hash.
- Stop and ask the user if the credential's scope is unknown — assume broad access until verified.
- If the credential was used to access customer data, follow the breach notification process in parallel.
- Never notify the user via the compromised channel (e.g., email if email account is compromised).
- If the compromise is an insider threat, coordinate with HR and legal before confronting the user.
