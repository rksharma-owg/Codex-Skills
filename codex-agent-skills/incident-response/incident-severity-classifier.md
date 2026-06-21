# Incident Severity Classifier

## Purpose

This Codex skill classifies a reported incident by severity (SEV1 through SEV4) based on impact (users affected, revenue loss, data exposure) and urgency (is it getting worse, is there a workaround). It produces the classification plus the required response (page IC, notify executives, open war room).

## When to Use

Use at the start of every incident, when the on-call is unsure whether to escalate, or as part of an incident-response process audit.

## Codex Instructions

1. Gather the initial report: what is broken, who reported it, when did it start, what is the user-visible symptom.
2. Assess impact: number of users affected, revenue impact (dollars per hour), data exposure (PII, PHI, secrets), regulatory impact.
3. Assess urgency: is the impact growing, is there a workaround, is it during business hours or peak traffic.
4. Classify the severity using the project's matrix: SEV1 (critical, all hands), SEV2 (major, IC + on-call), SEV3 (minor, on-call), SEV4 (low, ticket).
5. For SEV1: page the IC, notify executives, open a war room (Slack channel, Zoom bridge), start the incident clock.
6. For SEV2: page the on-call and the service owner, open a Slack channel, start the incident clock.
7. For SEV3: assign to the on-call, open a ticket, monitor for escalation.
8. For SEV4: open a ticket, no page.
9. Document the classification rationale in the incident channel for later review.
10. Output the classification, the response actions, and the initial incident timeline entry.

## Inputs Needed

- Initial incident report
- Project's severity matrix
- On-call schedule and contact info
- IC and executive contact info (for SEV1)
- Customer count and revenue impact estimation method

## Expected Output

A Markdown incident classification with: (1) Severity (SEV1-4) with rationale; (2) Response Actions list (who to page, what to open); (3) Initial Incident Timeline entry; (4) Communication Plan (internal, customer, regulatory).

## Example Prompt

> Classify this incident: 'Checkout page returns 500 for all users since 14:32 UTC. Estimated 5000 users affected, $50k/hour revenue impact. No workaround. Starting to affect mobile app too.' Use our SEV1-4 matrix. Tell me who to page and what to open.

## Safety Rules

- Never under-classify an incident to avoid escalation — when in doubt, classify up.
- Do not delay paging the IC for a potential SEV1 — page first, down-classify later if needed.
- Stop and ask the user if the impact is unknown — assume worst case until verified.
- If the incident involves data exposure, follow the breach notification process in parallel.
- Never discuss the incident in unsecured channels (personal Slack, SMS).
- If the incident affects a regulated workflow (payments, healthcare), notify compliance immediately.
