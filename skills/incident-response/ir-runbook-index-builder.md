---
id: ir-runbook-index-builder
name: IR Runbook Index Builder
category: incident-response
difficulty: Intermediate
tags:
  - ecr
  - incident-response
summary: |
  This Codex skill builds and maintains an index of incident response runbooks: by scenario (malware, cred compromise, data breach), by severity (SEV1-4), and by service.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill builds and maintains an index of incident response runbooks: by scenario (malware, cred compromise, data breach), by severity (SEV1-4), and by service. It targets the failure mode of an on-call who cannot find the right runbook during an incident.

## When to Use

Use when launching an IR program, after creating new runbooks, or quarterly to verify runbook freshness.

## Codex Instructions

1. Inventory all runbooks in the project's runbook portal (Confluence, Notion, internal wiki).
2. For each runbook, capture: title, scenario, severity, affected services, last reviewed date, owner.
3. Build a master index sorted by scenario (malware, cred compromise, data breach, ransomware, DoS, insider).
4. Build a secondary index sorted by service (payments, auth, web, mobile).
5. Build a severity index: which runbooks apply to SEV1, SEV2, SEV3.
6. Flag runbooks older than 6 months as 'needs review'; flag runbooks without an owner.
7. Cross-reference with recent incidents: were the right runbooks used? Were they helpful?
8. Recommend a quarterly review cadence: each owner reviews their runbooks for accuracy.
9. Add a 'first 5 minutes' quick-reference card for the most common scenarios.
10. Output the index in Markdown, ready to publish to the runbook portal's home page.

## Inputs Needed

- Runbook portal (Confluence, Notion, internal wiki)
- List of all runbooks with metadata
- Recent incident reports to cross-reference
- Service inventory
- Owners' availability for quarterly review

## Expected Output

A Markdown runbook index with: (1) By Scenario; (2) By Service; (3) By Severity; (4) Runbooks Needing Review; (5) First-5-Minutes Quick Reference; (6) Quarterly Review Schedule.

## Example Prompt

> Build an index for our 47 IR runbooks in Confluence. Capture title, scenario, severity, services, owner, last reviewed. Flag any older than 6 months. Cross-reference with the last 12 incidents to verify the right runbooks were used. Add a 'first 5 minutes' quick reference for malware, cred compromise, and data breach.

## Safety Rules

- Never publish internal runbook URLs in an external index.
- Do not include credentials or secrets in the index — link to the secret manager instead.
- Stop and ask the user if a runbook's owner is unknown — unowned runbooks decay.
- If the index reveals a missing runbook for a known scenario, flag it for creation.
- Never publish the index externally — it reveals IR capabilities.
- If a runbook is found to be inaccurate, mark it as 'under review' and notify the owner.
