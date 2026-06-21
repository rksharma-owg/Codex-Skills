# GitHub Dependabot Configurator

## Purpose

This Codex skill configures Dependabot for a repository: dependency ecosystems, update schedule, grouping, reviewers, assignees, and commit message conventions. It targets the failure mode of an outdated dependency that introduces a CVE.

## When to Use

Use when introducing Dependabot, when an audit reveals outdated dependencies, when Dependabot PRs are too noisy, or when standardizing across an org.

## Codex Instructions

1. Identify the dependency ecosystems: npm, pip, maven, gradle, docker, github-actions, terraform.
2. For each ecosystem, configure the schedule: daily, weekly (Monday for less noise), monthly.
3. Group updates to reduce PR noise: group minor and patch updates; keep major updates separate.
4. Set reviewers and assignees to the team that owns the dependency.
5. Set commit message conventions to match the project (conventional commits, etc.).
6. Configure security updates separately: always on, even if version updates are off.
7. Set open-pull-requests-limit to avoid overwhelming the PR queue (default 5, lower for small teams).
8. Author the .github/dependabot.yml file with the configuration.
9. Verify the config with dependabot dry-run (if available) or by waiting for the first run.
10. Recommend a process for triaging Dependabot PRs (SLA: critical CVE in 24h, high in 7d).

## Inputs Needed

- Dependency ecosystems in use
- Update schedule preference
- Reviewers/assignees per ecosystem
- Project's commit message convention
- PR noise tolerance (open-pull-requests-limit)

## Expected Output

A .github/dependabot.yml file with per-ecosystem config. Plus a triage SLA recommendation for the team.

## Example Prompt

> Configure Dependabot for our monorepo. Ecosystems: npm (weekly, group minor/patch), pip (weekly), docker (weekly), github-actions (weekly). Reviewers: @org/security for all. Open PR limit: 5. Commit message: conventional commits. Security updates always on. Triage SLA: critical 24h, high 7d.

## Safety Rules

- Never disable security updates to reduce noise — only version updates.
- Do not auto-merge Dependabot PRs without CI verification — the update may break the build.
- Stop and ask the user if a reviewer team's availability is unknown.
- If a Dependabot PR reveals a critical CVE, treat it as a security incident.
- Never log secrets in Dependabot PR templates or commit messages.
- If the project has a private registry, verify Dependabot has access via the repo's secrets.
