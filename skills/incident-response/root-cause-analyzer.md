---
id: root-cause-analyzer
name: Root Cause Analyzer
category: incident-response
difficulty: Advanced
tags:
  - incident-response
  - rds
summary: |
  This Codex skill performs a 5-Whys or fishbone root cause analysis on an incident: iteratively asks 'why' until reaching a systemic cause, identifies contributing factors, and proposes preventive actions.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill performs a 5-Whys or fishbone root cause analysis on an incident: iteratively asks 'why' until reaching a systemic cause, identifies contributing factors, and proposes preventive actions. It targets the failure mode of 'we fixed the symptom' without addressing the root cause.

## When to Use

Use during the post-incident review, within 5 business days of the incident, when the team has fresh context but is no longer in firefighting mode.

## Codex Instructions

1. Gather the incident timeline: detection, triage, mitigation, resolution.
2. State the incident's observable symptom in one sentence (e.g., 'checkout returned 500 for 47 minutes').
3. Ask 'why did this happen?' and capture the answer; if the answer is a symptom, ask 'why' again.
4. Repeat the 'why' chain 5 times (or until reaching a systemic cause: a process gap, a missing test, a tooling limitation).
5. Identify contributing factors: things that did not cause the incident but made it worse or longer (slow detection, no rollback, single point of failure).
6. Identify the systemic root cause: the underlying process or tooling gap that, if fixed, prevents the entire class of incidents.
7. Propose preventive actions: code changes, test additions, monitoring improvements, process changes.
8. Assign owners and due dates to each preventive action; track in the issue tracker.
9. Capture the analysis in the project's post-incident report template.
10. Output the RCA document with the 5-Whys chain, contributing factors, root cause, and preventive actions.

## Inputs Needed

- Incident timeline and notes
- Post-incident report template
- Access to logs, dashboards, and code at the time of the incident
- Team availability for the review meeting
- Issue tracker for preventive actions

## Expected Output

A Markdown RCA document with: (1) Incident Summary; (2) Timeline; (3) 5-Whys Chain; (4) Contributing Factors; (5) Systemic Root Cause; (6) Preventive Actions with owners and due dates.

## Example Prompt

> Run an RCA on the checkout outage from 2024-01-15. Timeline: 14:32 first 500, 14:35 on-call paged, 14:50 rollback started, 14:55 resolved. Symptom: checkout 500 for 23 minutes. Do 5-Whys, identify contributing factors and systemic root cause, propose preventive actions with owners.

## Safety Rules

- Never blame an individual in the RCA — focus on systemic causes.
- Do not close the RCA without assigning owners to preventive actions.
- Stop and ask the user if the 5-Whys chain is ambiguous — better to escalate than guess.
- If the root cause reveals a security gap, treat it as a security finding with a separate remediation timeline.
- Never publish the RCA externally without redacting customer-identifying info.
- If the RCA reveals a regulatory non-compliance, notify compliance before closing.
