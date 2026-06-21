---
id: iso-27001-control-implementer
name: ISO 27001 Control Implementer
category: cloud-security
difficulty: Advanced
tags:
  - cloud-security
  - iso-27001
  - rds
  - snyk
  - tls
summary: |
  This Codex skill designs implementations for ISO 27001 Annex A controls: A.5 (policies), A.6 (organization), A.7 (HR), A.8 (asset management), A.9 (access control), and the technical controls in A.10-A.18.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs implementations for ISO 27001 Annex A controls: A.5 (policies), A.6 (organization), A.7 (HR), A.8 (asset management), A.9 (access control), and the technical controls in A.10-A.18. It targets the failure mode of a policy that exists but is not implemented.

## When to Use

Use when pursuing ISO 27001 certification, after a major process change, when onboarding a new control, or annually for the surveillance audit.

## Codex Instructions

1. Identify the Annex A controls in scope (the Statement of Applicability defines this).
2. For each control, document the current implementation: policy, procedure, technical control, evidence.
3. For each control not implemented, design the implementation: who, what, when, how.
4. For access control (A.9), verify MFA, RBAC, periodic access reviews, privileged access management.
5. For cryptography (A.10), verify the encryption standards, key management, and key rotation.
6. For operations security (A.12), verify change management, vulnerability management, backup, logging.
7. For communications security (A.13), verify network segmentation, TLS, secure email.
8. For system acquisition and development (A.14), verify secure SDLC, code review, testing.
9. For supplier relationships (A.15), verify supplier agreements, supplier monitoring.
10. Output the control implementation plan with per-control status and evidence.

## Inputs Needed

- Statement of Applicability (SoA)
- Existing policies and procedures
- Technical control inventory
- Prior surveillance audit report (if available)
- Control owners and their availability

## Expected Output

A Markdown ISO 27001 Control Implementation Report with: (1) Control Status matrix (Implemented/Partial/Gap); (2) Per-control implementation details with evidence; (3) Implementation Plan for gaps; (4) Evidence Collection plan for the next audit.

## Example Prompt

> Implement ISO 27001 Annex A controls for our SaaS company pursuing first-time certification. SoA includes A.5, A.8, A.9, A.12, A.14. Verify current implementation of access control (Okta MFA, quarterly reviews), operations security (change mgmt via PRs, vuln scanning via Snyk), and identify gaps. Produce the implementation plan.

## Safety Rules

- Never mark a control as 'implemented' without evidence — the auditor will reject it.
- Do not weaken a control to 'simplify' the audit — gaps must be remediated.
- Stop and ask the user if a control's implementation is ambiguous — escalate to the owner.
- If a control depends on a supplier, verify the supplier's ISO 27001 certificate is current.
- Never share the control implementation externally without redacting sensitive details.
- If the implementation reveals a critical gap (e.g., no backup), remediate immediately.
