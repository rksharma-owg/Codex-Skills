---
id: guardduty-finding-triager
name: GuardDuty Finding Triager
category: cloud-security
difficulty: Intermediate
tags:
  - cloud-security
  - cloudtrail
  - guardduty
  - iam
summary: |
  This Codex skill triages AWS GuardDuty findings: classifies each as true positive, false positive, or benign-but-actionable; correlates with CloudTrail and VPC Flow Logs; and recommends a response (contain, monitor, dismiss).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill triages AWS GuardDuty findings: classifies each as true positive, false positive, or benign-but-actionable; correlates with CloudTrail and VPC Flow Logs; and recommends a response (contain, monitor, dismiss). It targets the failure mode of a noisy GuardDuty feed that on-call ignores.

## When to Use

Use during daily GuardDuty review, after a spike in findings, when tuning finding types to suppress benign ones, or as part of an incident response workflow.

## Codex Instructions

1. Pull the GuardDuty findings in the time window; group by finding type and resource.
2. For each finding, read the detail: API call, source IP, account, resource ARN, service, severity.
3. For high-severity findings (High), treat as a potential incident and prioritize.
4. For each finding, correlate with CloudTrail: was the API call part of normal business activity (e.g., a deploy script)?
5. For network-based findings (Recon, UnauthorizedAccess:EC2), correlate with VPC Flow Logs to identify the source.
6. For IAM findings (CredentialExfiltration, AnomalousBehavior), check the principal's recent activity.
7. Classify each finding: True Positive (incident), False Positive (benign config), Benign-Actionable (tune to suppress).
8. For True Positives, follow the CloudTrail Forensics Helper skill for deep investigation.
9. For Benign-Actionable, propose a suppression rule with a documented justification.
10. Output a triage report with per-finding classification and recommended actions.

## Inputs Needed

- AWS account and region
- GuardDuty findings export (CSV or via API)
- CloudTrail access for correlation
- Existing suppression rules and their justifications
- On-call engineer's availability for high-severity findings

## Expected Output

A Markdown report titled 'GuardDuty Triage Report' with: (1) Findings Summary table — ID | Type | Severity | Resource | Classification | Action; (2) True Positives with detailed investigation; (3) Suppression Rule Proposals for benign findings; (4) Trend analysis for recurring findings.

## Example Prompt

> Triage the last 24 hours of GuardDuty findings in our production account. We have 47 findings across 12 types. Classify each as true/false positive or benign-actionable, propose suppression rules for benign ones, and escalate any high-severity true positives to incident response.

## Safety Rules

- Never suppress a finding without a documented justification and a time-bound review.
- Do not dismiss a finding as false positive without CloudTrail correlation.
- Stop and ask the user if a finding's severity is ambiguous.
- If a finding indicates credential exfiltration, revoke the credentials immediately — do not wait for triage.
- Never log sensitive finding details (API call args, IPs) in a public channel.
- If a finding suggests data exfiltration, follow the breach response process.
