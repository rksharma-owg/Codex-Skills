---
id: incident-runbook-generator
name: Incident Runbook Generator
category: devops
difficulty: Intermediate
tags:
  - devops
  - ecr
  - rds
summary: |
  This Codex skill generates a per-service incident runbook from the service's observability signals, dependencies, and known failure modes.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates a per-service incident runbook from the service's observability signals, dependencies, and known failure modes. Each runbook covers detection, triage, mitigation, resolution, and post-incident steps, tailored to the on-call engineer's workflow.

## When to Use

Use when onboarding a new service to on-call, after a major incident reveals a missing runbook, during a service's first SLO rollout, or quarterly as part of runbook freshness reviews.

## Codex Instructions

1. Read the service's architecture: dependencies (databases, queues, upstream APIs), critical paths, and SLOs.
2. Read the service's alerts and dashboards; identify the alert-to-symptom mapping.
3. For each alert, generate a runbook entry: symptom, likely cause, triage command, mitigation step, escalation.
4. Add a 'Service Overview' section: what it does, who owns it, key dependencies, recent changes.
5. Add a 'Detection' section: which dashboard to look at, which log query to run, which trace filter to apply.
6. Add a 'Triage' section: decision tree to isolate the failing component (app vs database vs upstream).
7. Add a 'Mitigation' section: rollback command, feature-flag toggle, traffic shift, queue drain.
8. Add a 'Resolution' section: permanent fix steps, verification, and SLO recovery confirmation.
9. Add a 'Post-Incident' section: incident report template, follow-up actions, JIRA ticket creation.
10. Output the runbook in Markdown, ready to commit to the service repo or runbook portal.

## Inputs Needed

- Service repository path
- Service architecture and dependency diagram
- List of current alerts and dashboards
- SLO targets
- On-call escalation policy

## Expected Output

A Markdown runbook with sections: Service Overview, Detection, Triage, Mitigation, Resolution, Post-Incident. Each alert has a sub-section with the symptom-to-action mapping. Ready to commit.

## Example Prompt

> Generate an incident runbook for the payments service. Dependencies: Postgres, Stripe API, internal ledger service. Alerts: high 5xx rate, p99 > 1s, queue depth > 1000. SLO: 99.9% availability, p99 < 500ms. Output a Markdown runbook ready for the on-call portal.

## Safety Rules

- Never include production credentials or secrets in the runbook.
- Do not document a destructive mitigation (DROP TABLE, delete namespace) without a warning label.
- Stop and ask the user if a mitigation step's blast radius is unknown.
- If the runbook references a runbook for a dependency, link to it rather than duplicating content.
- Never publish the runbook to a public wiki without redacting internal hostnames and dashboards.
- Flag any alert that lacks a clear mitigation — escalate to the service owner.
