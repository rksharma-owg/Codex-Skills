# SAST Triage

## Purpose
This Codex skill triages raw Static Application Security Testing (SAST) output from tools like Semgrep, CodeQL, Snyk Code, SonarQube, and Fortify into a de-duplicated, prioritized, false-positive-aware queue that developers can actually act on. It exists because unfiltered SAST output overwhelms teams, produces alert fatigue, and routinely gets muted wholesale — defeating the purpose of static analysis. Triage is the missing layer between scanner output and developer action.

## When to Use
Activate this skill whenever a SAST tool produces more than ~30 findings on a codebase, when a new rule pack ships and floods the dashboard, when onboarding a previously unscanned legacy module, or as part of a sprint dedicated to "burning down" security debt. Also use it before promoting a PR from draft to review when CodeQL checks are failing on the PR.

## Codex Instructions
1. Ingest the raw SAST output (Semgrep JSON, CodeQL SARIF, Snyk JSON, SonarQube API export, Fortify FPR) and normalize each finding into a common schema: tool, rule ID, CWE, severity, file, start/end line, snippet, dataflow, and confidence.
2. De-duplicate findings that point to the same sink/source pair across multiple rules or tools; keep the highest-severity representation and record the merge in a `merged_from` field.
3. For each finding, fetch the surrounding code context (±10 lines) and the function signature to assess exploitability. Classify as True Positive, Likely True Positive, Needs Human Review, or False Positive.
4. Apply false-positive heuristics: tainted data already sanitized upstream (look for `escapeHtml`, parameterized query APIs, `safe-redirect` allowlist), test code paths (files under `test/`, `__tests__`, `*_spec.*`), demo/sample directories, framework-provided safe wrappers, and constants known to be benign.
5. Re-baseline severity using exploitability context: a SQL injection in a public-facing API is Critical; the same flaw in an internal-only CLI helper is High or Medium.
6. Group findings by remediation pattern so developers can fix 10 issues with one PR (e.g., "switch all `query()` calls to `querySafe()`").
7. Map each finding to OWASP Top 10 2021 and CWE; for Top-10 mappings, link to the OWASP cheat sheet for that category.
8. For each true positive, propose a minimal patch (≤5 lines) and, where possible, a Semgrep or CodeQL test that would prevent regression.
9. Produce the triaged report as `SAST_TRIAGE.md` and emit a re-importable SARIF file with triage annotations (`suppressed` for FPs, with `justification`).
10. Do not suppress findings without recording the suppression reason and the analyst (the prompt user) in the SARIF.

## Inputs Needed
- Raw SAST output file(s) or directory path
- Tool name(s) and version (Semgrep, CodeQL, Snyk Code, SonarQube, Fortify, Veracode)
- Repository path for code-context lookup
- Build/module map (so findings can be grouped by team ownership)
- List of known-safe functions/allowlists in the codebase (sanitizers, validators)
- Prior suppression file (`.semgrepignore`, `sonar-project.properties`, CodeQL `--suppress`)
- Threat model or attack-surface map (to score exploitability)
- Target environment (internet-facing, internal, air-gapped)

## Expected Output
A markdown report `SAST_TRIAGE.md` with: Executive Summary (input count, post-dedup count, TP/FP split, by-severity table), Findings Table (ID, Severity, CWE, OWASP Category, Tool:Rule, File:Line, Verdict, Remediation Pattern, Suggested Patch), False Positives (with suppression justification), Grouped Fix Plan (one section per remediation pattern with affected files), and Regression Prevention (suggested Semgrep/CodeQL rules). Severity scale: Critical / High / Medium / Low / Info. Also emit `triaged.sarif` with `suppressions` populated for FPs.

## Example Prompt
> Triage the Semgrep JSON at `/tmp/semgrep-results.json` for the repo at `/home/z/my-project/billing-api`. It's a Python FastAPI service, internet-facing. We have a known-safe validator at `app/validation.py::safe_int`. Map findings to OWASP Top 10 2021, group by fix pattern, and write `SAST_TRIAGE.md` plus a SARIF I can re-upload to GitHub. Flag anything in `tests/` as Info unless it's a real vuln.

## Safety Rules
- Do not modify source code or commit fixes autonomously — only propose patches in the report.
- Never suppress a finding marked Critical or in CISA KEV without explicit user confirmation in the prompt.
- Always record the suppression reason and analyst identity in the SARIF `suppressions` array.
- Do not infer exploitability from missing context — when in doubt, classify as Needs Human Review.
- Treat test code with suspicion; a vuln in a test harness can still be exploitable if the harness runs in CI with prod credentials.
- Do not delete or rewrite the raw input SAST file; triage is additive.
- If the same finding appears across multiple tools, surface the most severe representation but preserve all source IDs.
- Never auto-close findings in the upstream SAST platform's API; that requires a separate human-in-the-loop step.
