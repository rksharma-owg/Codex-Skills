---
id: developer-onboarding-doc-author
name: Developer Onboarding Doc Author
category: devops
difficulty: Intermediate
tags:
  - devops
  - docker
  - ecr
  - kubernetes
summary: |
  This Codex skill authors a developer onboarding document: environment setup, codebase tour, first PR guide, common pitfalls, and team norms.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill authors a developer onboarding document: environment setup, codebase tour, first PR guide, common pitfalls, and team norms. It targets the failure mode of a new hire who spends a week just getting their environment working.

## When to Use

Use when onboarding a new engineer, when existing onboarding docs are stale, or after an engineer reports onboarding friction.

## Codex Instructions

1. Document the environment setup: prerequisites (language version, package manager, Docker), install steps, verification commands.
2. Document the codebase tour: high-level architecture, key directories, the entry point, the request flow.
3. Document the first PR guide: pick a good first issue, the local dev loop, running tests, the PR template.
4. Document common pitfalls: tricky config, flaky tests, the dev database reset command.
5. Document team norms: branching strategy, commit message convention, code review SLA, on-call expectations.
6. Document the tools the team uses: Slack channels, JIRA board, the runbook portal, the status page.
7. Add a 'Who to ask' section: domain experts for each area.
8. Add a 30-60-90 day plan: what the new hire should achieve in their first 3 months.
9. Review the doc with a recent new hire for accuracy and friction points.
10. Output the onboarding doc in Markdown, ready to commit to the repo's docs/ folder.

## Inputs Needed

- Repository path
- Existing onboarding docs (if any)
- Team norms: branching, commits, code review, on-call
- Tools used: Slack, JIRA, runbook portal
- Domain experts for the 'Who to ask' section

## Expected Output

A Markdown onboarding doc with sections: Environment Setup, Codebase Tour, First PR Guide, Common Pitfalls, Team Norms, Tools, Who to Ask, 30-60-90 Day Plan. Ready to commit.

## Example Prompt

> Author an onboarding doc for new engineers joining our payments team. Stack: Go, gRPC, Postgres, Kafka, Kubernetes. Document environment setup (Go 1.21, Docker, kubectl), codebase tour (services/, proto/, deploy/), first PR guide, common pitfalls (local Kafka setup, dev DB reset), team norms (trunk-based, conventional commits), 30-60-90 plan.

## Safety Rules

- Never include production credentials or secrets in the onboarding doc.
- Do not document internal-only tools that the new hire should not have access to.
- Stop and ask the user if a setup step requires internal-only access (VPN, SSO).
- If the doc references a third-party service, verify the new hire will have access on day 1.
- Never publish the onboarding doc externally — it may reveal architecture details.
- If the doc references a 'good first issue' label, verify there are actually issues with that label.
