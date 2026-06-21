---
id: secret-scanner
name: Secret Scanner
category: cybersecurity
difficulty: Beginner
tags:
  - cwe
  - cybersecurity
  - ecr
  - github-actions
  - hipaa
  - jwt
  - pci
  - rds
  - soc-2
summary: |
  This Codex skill hunts for hardcoded credentials, API keys, private keys, tokens, and other sensitive material committed to source code, config files, build artifacts, and shell history.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill hunts for hardcoded credentials, API keys, private keys, tokens, and other sensitive material committed to source code, config files, build artifacts, and shell history. It exists because secrets in git history remain one of the most exploited initial-access vectors (per the Verizon DBIR and GitHub's own secret-scanning telemetry), and removing them from the tip of a branch is insufficient — secrets must be purged from history, rotated, and revoked.

## When to Use
Activate this skill before opening a PR that introduces new config, env files, deployment scripts, or third-party SDKs. Use it during onboarding of an acquired codebase, when rotating a leaked credential, or as part of a periodic secrets audit ahead of a SOC 2 evidence collection window. It is also useful when triaging a GitHub secret-scanning alert that flagged a commit but the team is unsure whether the match is a true positive or a test fixture.

## Codex Instructions
1. Scope the scan to the repository path provided; exclude `vendor/`, `node_modules/`, `.git/objects/`, and lockfile diffs unless explicitly requested.
2. Run a pattern-based sweep using regex signatures for AWS access keys (`AKIA[0-9A-Z]{16}`), Google API keys (`AIza[0-9A-Za-z\-_]{35}`), Stripe keys (`sk_live_`, `rk_live_`), Slack tokens (`xox[baprs]-`), GitHub PATs (`ghp_`, `gho_`, `ghu_`, `ghs_`), private key headers (`-----BEGIN .*PRIVATE KEY-----`), and JWTs (three base64url segments).
3. Run entropy-based detection on quoted strings longer than 20 characters in `*.env`, `*.yml`, `*.yaml`, `*.json`, `*.tf`, `*.conf`, and `*.ini` files, flagging Shannon entropy > 4.5.
4. Cross-check matches against known test/example values (e.g., `AKIAIOSFODNN7EXAMPLE`, `example.com` tokens, `redacted`) and drop them from the findings list, recording them in a False Positives section.
5. Use `git log -p --all -S '<secret-prefix>'` to determine the first commit that introduced each true-positive secret and list every branch and tag still containing it.
6. Categorize each finding by severity: Critical (live cloud provider keys, production DB passwords, signing keys), High (third-party API tokens with write scope), Medium (test/stage credentials), Low (read-only public API keys), Info (placeholder-looking strings needing human confirmation).
7. Map each finding to CWE-798 (Use of Hard-coded Credentials) and, where applicable, CWE-540 (Inclusion of Sensitive Information in Source Code).
8. Recommend remediation per finding: rotate via the provider's console, revoke the leaked token, scrub history with `git filter-repo` or BFG, and add the secret to the org's push-protection denylist.
9. Produce the report in the repository root as `SECRET_SCAN_REPORT.md` unless the user requests stdout only.
10. Do NOT attempt to validate secrets by calling the provider API — that risks logging the secret and triggering intrusion alerts.

## Inputs Needed
- Repository absolute path (or `.` for current working directory)
- Optional: specific subdirectory or glob to narrow scope
- Optional: branch or commit range (defaults to `--all`)
- Language/runtime stack (to tune parser and ignore lists)
- Existing `.gitignore` and secret-scan allowlist, if any
- CI context (e.g., GitHub Actions, GitLab CI) — affects remediation path
- Threat model or compliance driver (SOC 2, PCI, HIPAA) if findings will feed an audit
- Whether history scrubbing is authorized (affects recommendations)

## Expected Output
A markdown report titled `SECRET_SCAN_REPORT.md` with these sections: Executive Summary (counts by severity, top impacted files), Findings Table (columns: ID, Severity, Secret Type, CWE, File:Line, First Commit, Branches Containing, Remediation), False Positives (with reason for exclusion), History Scrub Plan (commands to run, branch-by-branch), and Next Steps (rotation checklist, push-protection rollout). Severity scale is Critical / High / Medium / Low / Info. Every Critical finding must include a specific rotation link or console path.

## Example Prompt
> Scan `/home/z/my-project/payments-api` for committed secrets across all branches and tags. We just onboarded this repo from an acquisition and need to know before we push it to our internal GitHub Enterprise. Run pattern + entropy detection, skip `vendor/`, and write the report to `SECRET_SCAN_REPORT.md`. Flag anything that looks like a live AWS, Stripe, or Datadog key as Critical.

## Safety Rules
- Never call any provider's API to "verify" a discovered secret — treat validation as out of scope.
- Do not include the full secret value in the report; mask everything except the last 4 characters.
- Do not modify, rotate, or revoke secrets autonomously; only recommend actions for a human to execute.
- Do not push history-rewrite commands to a remote without explicit user approval in the prompt.
- Skip scanning `.git/objects/pack/` raw packfiles — results are unreliable and noisy.
- If a finding appears to be a customer-provided secret (e.g., in a support ticket attachment), stop and ask the user how to proceed rather than scanning further.
- Never transmit discovered secrets to any external service, including telemetry or LLM context beyond what is strictly required for the report.
