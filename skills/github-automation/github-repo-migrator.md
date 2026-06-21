---
id: github-repo-migrator
name: GitHub Repo Migrator
category: github-automation
difficulty: Intermediate
tags:
  - codeql
  - dependabot
  - ecr
  - github-automation
summary: |
  This Codex skill migrates a repo from one GitHub org to another (or from another platform): clones the source, preserves history, recreates settings, secrets, webhooks, and integrations.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill migrates a repo from one GitHub org to another (or from another platform): clones the source, preserves history, recreates settings, secrets, webhooks, and integrations. It targets the failure mode of a migration that loses history or settings.

## When to Use

Use when consolidating orgs, when acquiring a company and migrating their repos, when moving from Bitbucket/GitLab to GitHub, or when splitting a monorepo.

## Codex Instructions

1. Inventory the source repo: branches, tags, history, releases, issues, PRs, settings, secrets, webhooks, integrations.
2. Choose the migration tool: GitHub's repo migration API (for org-to-org), ghs (for GitLab/Bitbucket to GitHub), or git clone + manual setup.
3. Migrate the git history with git clone --mirror to preserve all branches and tags.
4. Migrate issues and PRs with the migration API or a tool like ghs — preserve comments and metadata.
5. Recreate the settings: visibility, default branch, branch protection, topics, description.
6. Recreate secrets manually (they cannot be migrated programmatically for security reasons) — coordinate with the secret owners.
7. Recreate webhooks with their secret values — coordinate with the webhook endpoint owners.
8. Reinstall GitHub Apps and integrations.
9. Verify the migration: branch count, tag count, history depth, issue count, PR count match the source.
10. Decommission the source repo after verification — set to read-only, then archive after a grace period.

## Inputs Needed

- Source repo (org/repo or platform URL)
- Destination org/repo
- Migration tool preference (API, ghs, manual)
- Inventory of settings, secrets, webhooks, integrations
- Grace period before decommissioning the source

## Expected Output

A Markdown migration report with: (1) Source Inventory; (2) Migration Steps executed; (3) Verification Results (counts match); (4) Recreated Settings/Secrets/Webhooks/Integrations; (5) Decommission Plan for the source.

## Example Prompt

> Migrate our repo org-a/legacy-app to org-b/legacy-app. Use GitHub's migration API for git history and issues. Recreate settings (private, main branch, branch protection with 2 reviews), secrets (6 secrets, coordinate with owners), webhooks (3 webhooks to internal services), integrations (Dependabot, CodeQL). Verify counts match. Decommission source after 30-day grace period.

## Safety Rules

- Never migrate secrets programmatically — they must be recreated by their owners.
- Do not delete the source repo immediately — keep read-only for a grace period.
- Stop and ask the user if a webhook's endpoint owner is unknown.
- If the migration reveals a public source repo with sensitive content, treat it as a security incident.
- Never log webhook secrets or integration tokens during the migration.
- If the repo is part of a regulated workflow, verify the migration does not break compliance (e.g., audit log continuity).
