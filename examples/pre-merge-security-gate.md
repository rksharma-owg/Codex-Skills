---
id: pre-merge-security-gate
name: Pre-Merge Security Gate
purpose: Catch secrets, vulnerable dependencies, and OWASP Top 10 issues before a PR merges.
skills:
  - secret-scanner
  - dependency-vulnerability-auditor
  - sast-triage
  - owasp-top-10-remediator
---

# Pre-Merge Security Gate

## Goal

Run a four-skill security gate on every PR before merge. Catches hardcoded secrets, vulnerable dependencies, SAST findings, and OWASP Top 10 issues. Designed to run in CI as a blocking check, with output routed to the PR as a comment.

## Skills Used

1. **[`secret-scanner`](../skills/cybersecurity/secret-scanner.md)** — finds hardcoded credentials in the diff and history.
2. **[`dependency-vulnerability-auditor`](../skills/cybersecurity/dependency-vulnerability-auditor.md)** — flags CVEs in the lockfile.
3. **[`sast-triage`](../skills/cybersecurity/sast-triage.md)** — triages SAST findings (CodeQL/Semgrep) for true positives.
4. **[`owasp-top-10-remediator`](../skills/cybersecurity/owasp-top-10-remediator.md)** — proposes patches for OWASP Top 10 issues.

## Inputs

- Repository path (cloned in CI)
- PR diff (base branch and head branch)
- Lockfile (package-lock.json, requirements.txt, go.sum)
- SAST scan output (CodeQL SARIF or Semgrep JSON)

## Steps

1. **Scan for secrets.** Activate `secret-scanner` on the PR diff. If any Critical finding, fail the gate and comment on the PR.
2. **Audit dependencies.** Activate `dependency-vulnerability-auditor` on the lockfile. If any Critical or High CVE in a production dependency, fail the gate.
3. **Triage SAST.** Activate `sast-triage` with the SAST scan output. Filter to true positives; if any Critical, fail the gate.
4. **Propose remediation.** Activate `owasp-top-10-remediator` on the true-positive SAST findings. Generate a patch and attach to the PR as a suggestion.

## Expected Output

A PR comment with four sections: Secrets, Dependencies, SAST Findings, Remediation Patch. The PR is blocked if any section has a Critical finding.

## Example Invocation

> Run the pre-merge-security-gate workflow on PR #458 (base: main, head: feature/wallet-transfer). Lockfile: package-lock.json. SAST: CodeQL SARIF at .codeql/results.sarif. Comment findings on the PR and block merge if any Critical.

## Safety Notes

- Never log secrets found by the scanner — redact to first 4 chars.
- The remediation patch is a suggestion; the author must review before applying.
- If a SAST finding is in code that handles payments or PII, escalate to security review even if not Critical.
