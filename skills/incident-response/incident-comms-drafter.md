---
id: incident-comms-drafter
name: Incident Comms Drafter
category: incident-response
difficulty: Intermediate
tags:
  - argo
  - incident-response
summary: |
  This Codex skill drafts customer-facing and internal communications during an incident: status page updates, customer emails, executive summaries, and internal all-hands messages.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill drafts customer-facing and internal communications during an incident: status page updates, customer emails, executive summaries, and internal all-hands messages. It targets the failure mode of inconsistent or unclear comms during a high-stress incident.

## When to Use

Use during an active incident (every 30 minutes for SEV1, hourly for SEV2), when the on-call is too busy to draft comms, or when the comms lead needs a starting point.

## Codex Instructions

1. Gather the incident's current state: severity, customer-visible impact, mitigation in progress, ETA if known.
2. Draft a status page update: one sentence on the impact, one on what we're doing, one on ETA (or 'no ETA yet').
3. Draft a customer email for SEV1: acknowledge the impact, apologize, explain what we're doing, commit to a follow-up with RCA.
4. Draft an executive summary: severity, impact (users, revenue), mitigation status, ETA, comms sent.
5. Draft an internal all-hands message: brief, links to the incident channel and status page.
6. Use a calm, factual tone — no jargon, no blame, no speculation about root cause until confirmed.
7. Avoid false promises: 'we expect to resolve in 30 minutes' is OK; 'we will definitely resolve in 30 minutes' is not.
8. Send updates on a regular cadence even if there is no new info — silence breeds speculation.
9. Send a resolution update when the incident is mitigated, and a post-incident update after the RCA.
10. Output the comms drafts ready to paste into the status page, email tool, and chat.

## Inputs Needed

- Current incident state (severity, impact, mitigation, ETA)
- Status page platform (Statuspage.io, Atlassian Statuspage)
- Customer email tool (Customer.io, SendGrid)
- Executive distribution list
- Internal all-hands channel

## Expected Output

Comms drafts: status page update, customer email (for SEV1), executive summary, internal all-hands message. Each is ready to paste.

## Example Prompt

> Draft comms for our SEV1 checkout outage. Status: 5000 users affected, $50k/hr revenue impact, rollback in progress, ETA 15 min. Status page is Statuspage.io. Customer email via SendGrid. Exec summary to leadership@. Internal all-hands to #engineering.

## Safety Rules

- Never speculate about root cause in customer comms until confirmed by RCA.
- Do not share internal hostnames, IP addresses, or tool names in customer comms.
- Stop and ask the user if the impact estimate is uncertain — better to say 'some users' than a wrong number.
- If the incident involves data exposure, coordinate with legal before sending customer comms.
- Never send a comms update without the IC's approval.
- If the status page is down, use a backup channel (social media, partner status pages) and document the workaround.
