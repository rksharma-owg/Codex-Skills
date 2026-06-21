# Incident Timeline Builder

## Purpose

This Codex skill reconstructs an incident timeline from logs, alerts, chat messages, and commit history: detection time, page time, ack time, mitigation start, mitigation complete, resolution. It produces a clean timeline for the post-incident report.

## When to Use

Use during the post-incident review, when the timeline in chat is messy, or when the incident report needs a clean timeline for executives.

## Codex Instructions

1. Gather sources: alert manager history, on-call chat (Slack/PagerDuty), deploy logs, commit history, dashboard annotations.
2. Normalize timestamps to UTC; convert to the team's local time zone for the report.
3. Identify key events: first alert, page, ack, mitigation start, mitigation complete, resolution, comms sent.
4. Order events chronologically; note the gap between detection and page (MTTD) and between page and resolution (MTTR).
5. For each event, capture the source (alert ID, chat link, commit SHA) for traceability.
6. Flag any gaps longer than 5 minutes where no event was recorded — these are blind spots to investigate.
7. Flag any events that occurred out of expected order (e.g., mitigation before ack).
8. Produce a Markdown timeline table with columns: Time (UTC), Time (Local), Event, Source, Notes.
9. Add an executive summary at the top: total duration, MTTD, MTTR, customer impact.
10. Output the timeline ready to paste into the post-incident report.

## Inputs Needed

- Incident time window (start, end)
- Alert manager history (PagerDuty, Opsgenie)
- On-call chat export (Slack export)
- Deploy logs and commit history
- Dashboard annotations (Grafana, Datadog)

## Expected Output

A Markdown timeline table with: Time (UTC), Time (Local), Event, Source, Notes. Plus an executive summary with MTTD, MTTR, and total duration.

## Example Prompt

> Build a timeline for the incident on 2024-01-15 from 14:30 to 15:30 UTC. Sources: PagerDuty incident ABC123, Slack channel #inc-2024-01-15, deploy log in ArgoCD, commits in main since 14:00. Note gaps > 5 min and out-of-order events. We're in US/Eastern.

## Safety Rules

- Never publish internal chat content in an external incident report — paraphrase and redact.
- Do not include customer names or PII in the timeline.
- Stop and ask the user if a timestamp's source is ambiguous.
- If the timeline reveals a delay in paging, flag it as a process gap to address.
- Never log full alert payloads at INFO — they may contain sensitive config.
- If the timeline is being shared with regulators, verify it is complete and accurate.
