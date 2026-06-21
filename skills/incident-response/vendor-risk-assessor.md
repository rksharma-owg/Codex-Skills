---
id: vendor-risk-assessor
name: Vendor Risk Assessor
category: incident-response
difficulty: Advanced
tags:
  - incident-response
  - iso-27001
  - soc-2
summary: |
  This Codex skill assesses a vendor's security and compliance posture before onboarding: questionnaire, evidence review (SOC 2, ISO 27001), penetration test results, incident history, and the risk score.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill assesses a vendor's security and compliance posture before onboarding: questionnaire, evidence review (SOC 2, ISO 27001), penetration test results, incident history, and the risk score. It targets the failure mode of onboarding a vendor who later causes a breach.

## When to Use

Use when onboarding a new vendor that touches sensitive data, annually for critical vendors, after a vendor incident, or when a vendor's posture changes (e.g., acquisition).

## Codex Instructions

1. Identify the vendor's scope: what data they will access, what systems they will integrate with, what they will process.
2. Send the vendor a security questionnaire (SIG, CAIQ, or custom) covering access control, encryption, logging, incident response, business continuity.
3. Request evidence: SOC 2 Type 2 report, ISO 27001 certificate, pen test report, breach notification history.
4. Review the evidence: is it current (within 12 months), is it comprehensive (covers the in-scope service), is it the auditor's final report (not a draft).
5. Score the vendor on each risk dimension: data sensitivity, integration depth, vendor's posture, vendor's concentration risk.
6. Compute a composite risk score and a recommendation: Approve, Approve with conditions, Reject.
7. For 'Approve with conditions', specify the conditions (e.g., 'MFA required for admin access', 'annual re-assessment').
8. Verify the vendor's incident notification SLA is in the contract (e.g., notify within 72 hours of a breach).
9. Schedule annual re-assessment for critical vendors; quarterly for vendors handling regulated data.
10. Output the vendor risk assessment and the onboarding decision.

## Inputs Needed

- Vendor's scope of work and data access
- Vendor's completed questionnaire
- Vendor's compliance evidence (SOC 2, ISO 27001)
- Org's risk tolerance and approval thresholds
- Existing vendor inventory (for concentration risk)

## Expected Output

A Markdown Vendor Risk Assessment with: (1) Vendor Scope; (2) Questionnaire Responses summary; (3) Evidence Review notes; (4) Risk Score per dimension; (5) Composite Score and Recommendation; (6) Conditions (if any); (7) Re-assessment Schedule.

## Example Prompt

> Assess the vendor Acme Analytics before onboarding. Scope: receives user behavior events (PII: user ID, email). Questionnaire: completed, MFA yes, encryption yes, IR plan yes. Evidence: SOC 2 Type 2 (current), ISO 27001 (current), no public breaches. Score the risk and recommend approve/reject with conditions.

## Safety Rules

- Never approve a vendor handling regulated data without their SOC 2 or ISO 27001 evidence.
- Do not weaken the assessment to 'speed up onboarding' — escalate to the risk owner.
- Stop and ask the user if the vendor's scope is ambiguous (e.g., unclear if they will see PHI).
- If the vendor has a recent breach, escalate to the security team before approving.
- Never share the assessment externally — it contains vendor-confidential info.
- If the vendor's evidence is stale (> 12 months), require re-evidence before approval.
