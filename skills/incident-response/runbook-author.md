---
id: runbook-author
name: Runbook Author
category: incident-response
difficulty: Intermediate
tags:
  - ecr
  - helm
  - incident-response
  - rds
summary: |
  This Codex skill authors operational runbooks for an on-call engineer: service overview, common alerts, triage steps, mitigation, escalation, and post-incident actions.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill authors operational runbooks for an on-call engineer: service overview, common alerts, triage steps, mitigation, escalation, and post-incident actions. It targets the failure mode of an alert that pages on-call but has no documented response.

## When to Use

Use when onboarding a new service to on-call, after a major incident reveals a missing runbook, or quarterly as part of runbook freshness reviews.

## Codex Instructions

1. Read the service's architecture, SLOs, alerts, and dashboards.
2. Author a Service Overview: what it does, who owns it, key dependencies, recent changes.
3. For each alert, author a section: symptom, likely cause, triage command, mitigation step, escalation.
4. Use decision trees for triage: 'If X then Y, else Z' — make the path explicit.
5. Include exact commands the on-call can copy-paste: kubectl, aws cli, sql queries — not 'look at the dashboard'.
6. Include a rollback section: exact commands to roll back a deploy, restart a service, or revert a config.
7. Include an escalation section: who to page, when, and the paging criteria.
8. Include a post-incident section: incident report template, follow-up JIRA creation.
9. Review the runbook with the service owner and the on-call team for accuracy.
10. Output the runbook in Markdown, ready to commit to the service repo or runbook portal.

## Inputs Needed

- Service architecture and dependency diagram
- List of alerts and dashboards
- SLO targets
- On-call escalation policy
- Recent incident reports (for patterns)

## Expected Output

A Markdown runbook with sections: Service Overview, Alerts (with per-alert triage), Rollback, Escalation, Post-Incident. Each alert has copy-pasteable commands and a decision tree.

## Example Prompt

> Author a runbook for the payments service. Alerts: high 5xx, p99 > 1s, queue depth > 1000. Dependencies: Postgres, Stripe, internal ledger. SLO: 99.9% availability, p99 < 500ms. Include rollback commands (helm rollback, kubectl scale), escalation (page payments on-call, then SRE), and a post-incident template.

## Safety Rules

- Never include production credentials or secrets in the runbook.
- Do not document a destructive mitigation (DROP TABLE) without a warning label.
- Stop and ask the user if a mitigation step's blast radius is unknown.
- If the runbook references another service's runbook, link to it rather than duplicating.
- Never publish the runbook to a public wiki without redacting internal hostnames.
- Flag any alert that lacks a clear mitigation — escalate to the service owner.
