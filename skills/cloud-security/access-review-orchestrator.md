---
id: access-review-orchestrator
name: Access Review Orchestrator
category: cloud-security
difficulty: Intermediate
tags:
  - cloud-security
  - iam
  - iso-27001
  - soc-2
summary: |
  This Codex skill orchestrates a quarterly access review: pulls the current access list (who has access to what), sends to managers for review, captures decisions (keep, modify, revoke), and produces an audit trail.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill orchestrates a quarterly access review: pulls the current access list (who has access to what), sends to managers for review, captures decisions (keep, modify, revoke), and produces an audit trail. It targets the compliance requirement for periodic access reviews.

## When to Use

Use quarterly for SOC 2 / ISO 27001 compliance, after an org restructure, when an employee changes roles, or when a former employee's access was discovered.

## Codex Instructions

1. Pull the current access list from each system: cloud IAM, SaaS apps, databases, SSH keys, VPN.
2. Group access by user and by system; identify privileged access (admin, root, write).
3. Send the access list to each user's manager for review, with a deadline (e.g., 5 business days).
4. Capture decisions: keep, modify (reduce privileges), revoke.
5. For 'revoke' decisions, execute the revocation and capture the timestamp and executor.
6. For 'modify' decisions, execute the privilege reduction and capture the new access level.
7. For 'keep' decisions, capture the manager's justification.
8. Produce an audit trail: who reviewed, what was decided, what was executed, when.
9. Flag any user with access who has left the org (compare to HR's termination list).
10. Output the review report and the audit trail for the compliance evidence file.

## Inputs Needed

- Systems in scope (cloud IAM, SaaS apps, databases, SSH, VPN)
- Manager-to-user mapping (from HR or org chart)
- HR's termination list (for leaver access check)
- Review tool (spreadsheet, access review tool like Saviynt)
- Compliance evidence storage

## Expected Output

A Markdown access review report with: (1) Access Inventory by system; (2) Reviewer assignments and deadlines; (3) Decisions captured (keep/modify/revoke); (4) Executed changes with timestamps; (5) Audit trail; (6) Leaver access findings.

## Example Prompt

> Orchestrate a quarterly access review for our 50 engineers. Systems: AWS IAM (3 accounts), GitHub (org), Datadog, PagerDuty, Postgres (production). Send each user's access to their manager with a 5-day deadline. Capture decisions, execute revocations, produce the audit trail for our SOC 2 evidence file.

## Safety Rules

- Never skip a user in the review — incomplete reviews are audit findings.
- Do not auto-keep access without manager review — every access must be reviewed.
- Stop and ask the user if a manager is unavailable (vacation, left org) — reassign the review.
- If the review reveals a leaver with active access, revoke immediately and treat as an incident.
- Never log access credentials during the review — log only the access level.
- If the review reveals excessive privileged access, escalate to the security team.
