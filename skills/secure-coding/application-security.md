---
id: application-security
name: Application Security (Comprehensive)
category: secure-coding
difficulty: Advanced
tags:
  - application-security
  - authentication
  - authorization
  - input-validation
  - data-protection
  - secure-config
  - supply-chain
  - threat-modeling
  - monitoring
  - compliance
summary: |
  Comprehensive application-security skill covering auth, input validation, data protection, monitoring, secure config, supply chain, and threat modeling.
last_reviewed: 2026-06-21
---

# Application Security (Comprehensive)

## Purpose

A consolidated application-security reference covering the seven pillars of secure application design: authentication, input validation, data protection, secure configuration, supply-chain integrity, threat modeling, and monitoring/compliance. Use this skill when you need end-to-end coverage rather than a single narrow check.

## When to Use

Activate this skill when starting a new application-security program, when preparing for a SOC 2 / ISO 27001 audit, when onboarding a new engineering team to security expectations, or as a reference checklist during architecture review.

## Reference Modules

This skill is backed by reference documents in [`/shared/application-security/`](../../shared/application-security/):

- [`auth.md`](../../shared/application-security/auth.md) — Authentication & authorization patterns
- [`input-validation.md`](../../shared/application-security/input-validation.md) — Input validation & output encoding
- [`data-protection.md`](../../shared/application-security/data-protection.md) — Encryption, key management, PII handling
- [`secure-config.md`](../../shared/application-security/secure-config.md) — Secrets, env vars, config hardening
- [`supply-chain.md`](../../shared/application-security/supply-chain.md) — Dependency hygiene, SBOM, signed artifacts
- [`monitoring-compliance.md`](../../shared/application-security/monitoring-compliance.md) — Audit logging, alerting, compliance evidence
- [`threat-modeling.md`](../../shared/application-security/threat-modeling.md) — STRIDE, attack trees, data-flow mapping

## Codex Instructions

1. Identify the scope of the review: full application, a new feature, or a specific subsystem.
2. Walk through each of the seven reference modules; for each, identify the applicable controls and any gaps.
3. For each gap, document: the missing control, the risk, the proposed remediation, the owner, and the priority.
4. Cross-reference with the narrow skills in `/skills/secure-coding/` and `/skills/cybersecurity/` for deep-dive remediation.
5. Produce a single Application Security Review report covering all seven pillars, ready for the audit or architecture review.

## Inputs Needed

- Application architecture diagram
- Tech stack (language, framework, data stores, third-party services)
- Compliance scope (SOC 2, ISO 27001, PCI, HIPAA)
- Existing security controls documentation
- Threat model (if one exists)

## Expected Output

A Markdown Application Security Review report with: (1) Scope; (2) Per-pillar findings — pillar | control | status | gap | remediation | owner | priority; (3) Cross-cutting recommendations; (4) Audit-ready evidence index.

## Example Prompt

> Run a comprehensive application-security review of our Next.js + Postgres + Stripe SaaS app. We're preparing for SOC 2. Walk through all seven pillars (auth, input validation, data protection, secure config, supply chain, threat modeling, monitoring) and produce a review report with prioritized remediation items.

## Safety Rules

- Never auto-apply remediation without explicit approval — produce the review only.
- Do not log secrets or PII during the review.
- If a finding indicates an active compromise, escalate to incident-response skills immediately.
- Cross-reference compliance findings with the relevant /skills/cloud-security/ compliance mapper.
