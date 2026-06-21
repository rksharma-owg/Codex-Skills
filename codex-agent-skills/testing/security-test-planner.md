# Security Test Planner

## Purpose

This Codex skill designs a security test plan: SAST, SCA, secret scanning, DAST, IAST, and penetration testing scope. It defines the tools, the scope, the frequency, and the gates (what blocks a release).

## When to Use

Use when launching a security testing program, before a compliance audit, when onboarding a new tool, or after a security incident reveals a gap.

## Codex Instructions

1. Inventory the application's attack surface: source code, dependencies, containers, infrastructure, APIs, runtime.
2. Choose SAST: CodeQL, Semgrep, SonarQube — run on every PR and nightly.
3. Choose SCA: Dependabot, Snyk, OSV-Scanner — run on every PR and nightly.
4. Choose secret scanning: Gitleaks, TruffleHog, GitHub Secret Scanning — run on every commit and on git history.
5. Choose DAST: OWASP ZAP, Burp Suite — run nightly on staging.
6. Choose IAST (if applicable): Contrast, Seeker — run in staging during integration tests.
7. Define the gates: Critical SAST finding blocks release; Critical CVE in production dependency blocks release; Critical secret in git history blocks release.
8. Define the frequency: PR gates (SAST, SCA, secret scan), nightly (DAST), quarterly (pen test).
9. Define the escalation: who is paged for a Critical finding, the SLA to fix (24h for Critical, 7d for High).
10. Output the security test plan document and the CI integration snippets for each tool.

## Inputs Needed

- Application's tech stack and attack surface
- Existing security tools (or 'none' for greenfield)
- Compliance requirement (PCI ASV scan, SOC 2 pen test)
- Release cadence (daily, weekly, monthly)
- Security team's on-call schedule

## Expected Output

A Markdown security test plan with: (1) Attack Surface Inventory; (2) Tool Selection per layer; (3) Frequency Matrix; (4) Release Gates; (5) Escalation Matrix; (6) CI Integration snippets.

## Example Prompt

> Design a security test plan for our Node.js + React SaaS app. Stack: TypeScript, Postgres, AWS EKS. Tools: CodeQL, Snyk, Gitleaks, OWASP ZAP. Run SAST/SCA/secret scan on every PR, DAST nightly on staging. Define release gates and escalation SLAs. We're targeting SOC 2.

## Safety Rules

- Never weaken a release gate to ship faster — escalate to the user instead.
- Do not run DAST against production without explicit sign-off.
- Stop and ask the user if a tool's license or data residency is unclear.
- If a Critical finding is reported, treat it as a security incident until proven otherwise.
- Never log secret scan results that include the secret value — redact.
- If the security test plan reveals a gap in compliance, escalate to compliance before the next audit.
