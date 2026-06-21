---
id: github-repo-settings-auditor
name: GitHub Repo Settings Auditor
category: github-automation
difficulty: Intermediate
tags:
  - dependabot
  - ecr
  - github-automation
summary: |
  This Codex skill audits a GitHub repo's settings for security and consistency: visibility, default branch, branch protection, secrets, webhooks, collaborators, integrations, and the minimum admin count.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits a GitHub repo's settings for security and consistency: visibility, default branch, branch protection, secrets, webhooks, collaborators, integrations, and the minimum admin count. It targets the failure mode of a misconfigured repo that allows unauthorized access.

## When to Use

Use when onboarding a new repo, before a public launch, after a security incident, or quarterly as part of repo hygiene.

## Codex Instructions

1. Pull the repo's settings via the GitHub API: visibility, default branch, allow_force_pushes, allow_squash_merge, etc.
2. Verify the visibility matches the intended state (public repos should be intentional).
3. Verify branch protection is enabled on the default branch with required reviews and status checks.
4. Verify the minimum admin count: at least 2 admins to avoid a bus-factor lockout.
5. Inventory secrets: are any unused? Are any rotated recently?
6. Inventory webhooks: are they pointing to active endpoints? Are they using secrets?
7. Inventory collaborators: are they still with the org? Are their permissions appropriate?
8. Inventory GitHub Apps and integrations: are they still in use? Are they from trusted publishers?
9. Verify Dependabot security alerts are enabled.
10. Verify secret scanning and push protection are enabled.
11. Output an audit report with findings and a remediation plan.

## Inputs Needed

- GitHub repo name(s)
- GitHub token with admin:repo and read:org scopes
- Org-wide policy on visibility, branch protection, etc.
- Whether the repo is public or private

## Expected Output

A Markdown audit report with: (1) Settings Inventory; (2) Findings table — Area | Issue | Severity | Fix; (3) Remediation Plan; (4) Verification commands to re-check after fixes.

## Example Prompt

> Audit the settings of our 25 GitHub repos. Verify visibility (public must be intentional), branch protection on main (2 reviews, status checks, no force push), minimum 2 admins, unused secrets, stale webhooks, ex-employee collaborators. Enable Dependabot, secret scanning, push protection where missing.

## Safety Rules

- Never expose the GitHub token in logs.
- Do not change repo visibility without explicit user approval — public-to-private can break consumers.
- Stop and ask the user if a collaborator's continued access is ambiguous.
- If the audit reveals a public repo with sensitive content, treat it as a security incident.
- Never log webhook secrets or integration tokens.
- If the repo is part of a regulated workflow, verify the settings meet the compliance requirements.
