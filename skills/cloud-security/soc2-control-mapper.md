---
id: soc2-control-mapper
name: SOC 2 Control Mapper
category: cloud-security
difficulty: Advanced
tags:
  - cloud-security
  - cloudtrail
  - soc-2
summary: |
  This Codex skill maps an org's controls to the SOC 2 Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill maps an org's controls to the SOC 2 Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy. It identifies gaps and produces the control description for the auditor.

## When to Use

Use when preparing for a SOC 2 audit, after a major process change, when onboarding a new control (e.g., a new SIEM), or annually for the SOC 2 Type 2 renewal.

## Codex Instructions

1. Inventory the org's controls: policies, procedures, technical controls, monitoring.
2. For each SOC 2 criterion (CC1-CC9, A, PI, C, P), identify the controls that satisfy it.
3. For each control, document: description, evidence (logs, configs, tickets), frequency (continuous, monthly), owner.
4. Identify gaps: criteria without an implemented control — these must be remediated before the audit.
5. Identify weak controls: implemented but with insufficient evidence — these need monitoring improvements.
6. Map controls to the auditor's testing approach: inquiry, observation, inspection, re-performance.
7. Document the control description in the auditor's format (often a spreadsheet or Workiva).
8. Plan the evidence collection: who gathers what, when, for the audit period.
9. Recommend a continuous monitoring approach to avoid the audit-time crunch.
10. Output the control map, the gap list, and the evidence collection plan.

## Inputs Needed

- SOC 2 criteria in scope (Security only, or Security + Availability + Privacy)
- Existing control inventory (policies, procedures, tools)
- Prior year's SOC 2 report (if available)
- Auditor's testing approach document
- Control owners and their availability

## Expected Output

A Markdown SOC 2 Control Map with: (1) Criteria to Control matrix; (2) Control Descriptions with evidence and frequency; (3) Gap List with remediation plan; (4) Evidence Collection Plan.

## Example Prompt

> Map our controls to SOC 2 Security + Availability criteria. Inventory: MFA via Okta, SSO, CloudTrail logging, AWS Config, PagerDuty on-call, quarterly access reviews, annual pen test. Identify gaps and weak controls, document descriptions in our auditor's (Vanta) format, plan evidence collection for Jan-Dec 2024.

## Safety Rules

- Never mark a control as 'implemented' without evidence — the auditor will reject it.
- Do not weaken a control to 'simplify' the audit — gaps must be remediated, not hidden.
- Stop and ask the user if a control's evidence is missing — escalate to the owner.
- If the map reveals a critical gap (e.g., no MFA on a production system), remediate immediately.
- Never share the control map externally without redacting sensitive details.
- If a control depends on a third party (e.g., cloud provider), verify the third party's SOC 2 report is current.
