---
id: monitoring-alert-tuner
name: Monitoring Alert Tuner
category: devops
difficulty: Intermediate
tags:
  - devops
  - prometheus
summary: |
  This Codex skill reviews existing alerts and tunes them for precision (low false positives) and recall (low false negatives): adjusts thresholds based on historical data, groups correlated alerts, adds runbook links, and removes noisy alerts that have not paged in 90 days.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill reviews existing alerts and tunes them for precision (low false positives) and recall (low false negatives): adjusts thresholds based on historical data, groups correlated alerts, adds runbook links, and removes noisy alerts that have not paged in 90 days. It targets the failure mode of alert fatigue where on-call ignores pages.

## When to Use

Use during an alert fatigue review, after a missed incident (false negative), after a noisy week (false positives), or quarterly as part of SLO governance.

## Codex Instructions

1. Pull alert history for the last 90 days: fire time, resolve time, action taken (ack, silence, ignore).
2. Identify noisy alerts: fired > 10 times with no action, or ack-then-auto-resolved within 5 minutes.
3. Identify dead alerts: not fired in 90 days; evaluate whether the underlying condition is still meaningful.
4. For each noisy alert, propose a threshold change based on the p95 of the underlying metric.
5. Group correlated alerts (e.g., high latency on multiple endpoints) into a single alert with multiple dimensions.
6. Add a runbook link to every alert; flag alerts without a runbook as 'unactionable'.
7. Verify every alert has an SLO tie-in: alerts should fire when an SLO budget is being burned, not on absolute thresholds alone.
8. Propose multi-window multi-burn-rate alerts for SLO-based alerts (e.g., 2% budget burn in 1 hour, 5% in 6 hours).
9. Recommend silencing windows for known maintenance, and automated silencing for deploy windows.
10. Output an alert tuning report with proposed changes and a GitHub PR-ready patch for the alert rules.

## Inputs Needed

- Alert manager (Prometheus Alertmanager, PagerDuty, Opsgenie, Datadog Monitors)
- Alert rule files or definitions
- 90-day alert history export
- SLO definitions for the monitored services
- On-call schedule and escalation policy

## Expected Output

A Markdown report titled 'Alert Tuning Review' with: (1) Alert Inventory with fire count, action rate, runbook link; (2) Noisy Alerts with proposed threshold changes; (3) Dead Alerts for removal; (4) SLO-Based Alert Proposals; (5) PR-ready patch for the alert rules.

## Example Prompt

> Tune our Prometheus alerts. We have 80 alert rules, 30 of which fired in the last 90 days. Pull the alert history, identify noisy alerts (fired > 10 times with no action), dead alerts, and alerts without runbook links. Propose multi-window multi-burn-rate alerts aligned to our SLOs.

## Safety Rules

- Never disable an alert without a replacement — silence it temporarily instead.
- Do not remove a dead alert without verifying the underlying condition is no longer meaningful.
- Stop and ask the user if an alert's SLO tie-in is ambiguous.
- If tuning requires changing the SLO, flag it as a separate decision — alert tuning should follow SLO changes, not drive them.
- Never log alert payload contents that include customer data at INFO.
- If an alert pages on-call, require a second reviewer to approve the tuning change.
