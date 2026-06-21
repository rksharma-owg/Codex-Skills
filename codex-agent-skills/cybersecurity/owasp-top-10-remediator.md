# OWASP Top 10 Remediator

## Purpose
This Codex skill maps a codebase's security findings to the OWASP Top 10 2021 categories (A01 Broken Access Control through A10 SSRF) and proposes concrete, minimal-patch remediations grounded in OWASP cheat sheets, ASVS, and NIST guidance. It exists because "fix the OWASP Top 10" is the most common board-level directive yet the hardest to operationalize — most teams need a translator between scanner output and actual code changes that pass review.

## When to Use
Activate this skill when preparing for a penetration test, after a breach or near-miss tied to an OWASP category, when onboarding a new service into the security review queue, or as part of a quarterly "OWASP Top 10 sprint." Also use it after a SAST/DAST scan to translate raw findings into OWASP-aligned remediation work items.

## Codex Instructions
1. Accept as input either a list of findings (SAST/DAST report) or a codebase to analyze directly; if the latter, run `semgrep --config p/owasp-top-ten` and `semgrep --config p/default` to seed findings.
2. Categorize each finding into exactly one OWASP Top 10 2021 category: A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection, A04 Insecure Design, A05 Security Misconfiguration, A06 Vulnerable & Outdated Components, A07 Identification & Authentication Failures, A08 Software & Data Integrity Failures, A09 Security Logging & Monitoring Failures, A10 SSRF.
3. For each category present, link the relevant OWASP cheat sheet (`https://cheatsheetseries.owasp.org/cheatsheets/<category>.html`) and ASVS v4.0.x control(s) that apply.
4. Prioritize by OWASP risk rating methodology: impact × likelihood, weighted by the OWASP Top 10 prevalence factors; explain the math in the report so the user can challenge the ranking.
5. For each finding, produce a minimal patch (≤10 lines) that addresses the root cause, not a symptom. Prefer framework-native defenses (Spring Security, Django decorators, Express middleware, ASP.NET Core attributes) over custom code.
6. Where a finding requires architectural change (e.g., A04 Insecure Design — missing rate limiting on a sensitive endpoint), propose an ADR-style design note rather than a patch, and link to the relevant NIST SP 800-63B or 800-204D section.
7. For A06 (vulnerable components), defer to the dependency-vulnerability-auditor skill output if available; do not re-run that scan here.
8. For A09 (logging failures), verify the presence of: authentication events, authorization decisions (denied and allowed), input validation failures, and admin actions. Recommend a logging schema aligned with Apache Lesser General Public License's `audit-log` or your existing SIEM schema.
9. Map each remediation to a regression test: a unit test for the patched function, plus a Semgrep rule that would catch reintroduction.
10. Emit the report as `OWASP_REMEDIATION.md` with one section per OWASP category present, plus an executive summary listing category coverage.

## Inputs Needed
- Repository path
- Optional: SAST/DAST findings file to seed categorization
- Language/framework (Spring Boot, Django, Express, Rails, .NET, etc.) — affects cheat-sheet selection
- Threat model or data-classification map (PII, PHI, PCI) — affects severity
- Existing security middleware / library list (e.g., Spring Security, Helmet.js) so recommendations don't conflict
- Compliance driver (PCI DSS Req. 6, HIPAA Security Rule, SOC 2 CC7) if audit-ready remediation is needed
- ASVS target level (L1 verification, L2, L3) if you want ASVS-mapped remediation
- Prior OWASP remediation reports for the same codebase (to track deltas)

## Expected Output
A markdown report `OWASP_REMEDIATION.md` with sections: Executive Summary (which of A01–A10 are present, by-severity counts, top 3 priorities), then one section per present category containing: Findings Table (ID, Severity, CWE, File:Line, Description), Root Cause Analysis, OWASP Cheat Sheet Reference (URL), ASVS Control(s), Proposed Patch (code block), Regression Test (code block), and Semgrep Rule. Close with a Verification Checklist the user can hand to QA. Severity scale: Critical / High / Medium / Low / Info.

## Example Prompt
> Analyze `/home/z/my-project/loan-origination-api` (Spring Boot 3 + Java 21) against OWASP Top 10 2021. We had a pen test last week and the report flagged A01, A03, and A07 issues — I'll paste the pen-test JSON into your context. Propose minimal patches that pass Spring Security review, map to ASVS L2, and add a Semgrep regression rule for each fix. Write `OWASP_REMEDIATION.md`.

## Safety Rules
- Do not commit patches directly; propose them in the report for human review.
- Never downgrade an OWASP Top 10 finding because the team is "busy" — capture the risk acceptance in the report but keep the severity.
- For A02 (Cryptographic Failures), never recommend a custom crypto algorithm or a non-standard mode; always point to NIST-approved primitives.
- For A07 (AuthN failures), never recommend weakening MFA or password policy to ship faster; cite NIST SP 800-63B.
- For A05 (Misconfiguration), do not disable security headers (CSP, HSTS, X-Frame-Options) even if they break a feature — propose a CSP that allows the feature.
- If a finding requires an architectural change, flag it as A04 Insecure Design and propose an ADR, not a patch.
- Do not run the codebase's tests or build pipeline to "verify" patches — that is a separate step.
- Always include the OWASP cheat sheet URL verbatim so the user can audit the source of the recommendation.
