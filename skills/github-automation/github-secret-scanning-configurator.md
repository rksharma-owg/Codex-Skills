---
id: github-secret-scanning-configurator
name: GitHub Secret Scanning Configurator
category: github-automation
difficulty: Intermediate
tags:
  - ecr
  - github-automation
summary: |
  This Codex skill configures GitHub's secret scanning and push protection for a repository: enables scanning, configures custom patterns for org-specific secrets, and sets up alert routing.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill configures GitHub's secret scanning and push protection for a repository: enables scanning, configures custom patterns for org-specific secrets, and sets up alert routing. It targets the failure mode of a secret committed to git history.

## When to Use

Use when enabling secret scanning, after a secret exposure incident, when onboarding a new secret format (internal API keys), or as part of a security baseline.

## Codex Instructions

1. Enable GitHub Secret Scanning in the repo's security settings (requires public repo or GitHub Advanced Security).
2. Enable Push Protection to block commits containing known secrets at the client side.
3. Identify org-specific secret formats that GitHub's default patterns don't catch: internal API keys, customer tokens.
4. Author custom patterns as regex with a capture group for the secret, a confidence level, and a test case.
5. Configure alert routing: who gets notified when a secret is found, the SLA to rotate.
6. Configure the remediation runbook: how to rotate the secret, how to purge from git history, who to notify.
7. Test by committing a fake secret that matches a custom pattern — verify the alert fires.
8. Verify push protection blocks the commit on the client side (git push is rejected).
9. Document the secret scanning setup in the repo's security policy.
10. Output the configuration (custom patterns, alert routing) and the runbook.

## Inputs Needed

- Repository (public or GitHub Advanced Security)
- List of org-specific secret formats
- Alert routing (who, the SLA)
- Existing remediation runbook

## Expected Output

A Markdown configuration report with: (1) Default patterns enabled; (2) Custom patterns with regex and test cases; (3) Alert Routing config; (4) Remediation Runbook; (5) Test results.

## Example Prompt

> Configure secret scanning for our org's repos. Enable default patterns (AWS, GCP, Stripe, etc.) and push protection. Add custom patterns for our internal API key format (prefix 'sk_int_', 32 alphanumeric). Alert routing: page security on-call for any secret, SLA to rotate is 1 hour. Test with a fake commit.

## Safety Rules

- Never disable push protection to 'fix' a blocked commit — rotate the secret and commit without it.
- Do not log the secret value in the alert or the runbook — log only the secret type and location.
- Stop and ask the user if a custom pattern's regex is ambiguous — false positives cause alert fatigue.
- If a real secret is found in history, treat it as a security incident — rotate and purge.
- Never share secret scanning alerts in public channels.
- If the repo is public, verify the secret scanning covers all branches and the full history.
