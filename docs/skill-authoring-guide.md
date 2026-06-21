# Skill Authoring Guide

This guide covers how to write a high-quality Codex agent skill that meets the library's quality bar.

## Before You Start

1. **Search the catalog.** Open [`/catalog/index.md`](../catalog/index.md) and search for your topic. If a similar skill exists, improve it rather than create a duplicate.
2. **Pick the right category.** The 8 categories are:
   - `cybersecurity` — finding and fixing vulnerabilities
   - `secure-coding` — hardening code at the source (and PR review)
   - `cloud-security` — cloud posture, IAM, compliance
   - `incident-response` — incidents, forensics, postmortems, DSAR
   - `ai-security` — LLM and agent security
   - `devops` — CI/CD, containers, observability, architecture, engineering docs
   - `testing` — unit, integration, load, fuzz, contract, E2E, security
   - `github-automation` — Actions, releases, branch protection, OIDC
3. **Open an issue** describing the skill you plan to add. A maintainer will confirm fit before you spend time writing.

## Authoring

### 1. Start from the template

Copy [`/templates/skill-template.md`](../templates/skill-template.md) to `skills/<category>/<your-skill-id>.md`.

### 2. Fill in the frontmatter

```yaml
---
id: my-new-skill              # kebab-case, must match filename (without .md)
name: My New Skill            # Title Case
category: devops              # one of 8
difficulty: Intermediate      # Beginner | Intermediate | Advanced
tags:                         # up to 10, lowercase, kebab-case
  - ci
  - github-actions
  - docker
summary: |                    # one paragraph, under 80 words
  This skill does X for Y. It exists because Z. Use it when W.
last_reviewed: 2026-06-21     # today's date
---
```

### 3. Write each section

**`## Purpose`** — 2-4 sentences. What does this skill do? Why does it exist? Reference real standards (OWASP, CWE, NIST, CIS) where applicable.

**`## When to Use`** — 2-4 sentences. Concrete trigger conditions. "Before merging a PR that touches X", "during pre-prod security review", "when triaging a SAST alert on a legacy module".

**`## Codex Instructions`** — 6-12 numbered steps. This is the heart of the skill. Each step should be a concrete action Codex can take. Reference real tools (`semgrep`, `trivy`, `kubectl`, `aws cli`) and standards (`CWE-89`, `OWASP ASVS V5`). Cover: how to scope, what to look for, how to prioritize, how to format output, what NOT to do.

**`## Inputs Needed`** — 4-8 bullets. What must the user provide? Repo path, target file, language, CI context, threat model, etc.

**`## Expected Output`** — Be specific. "A Markdown report with sections: Executive Summary, Findings Table (ID, Severity, CWE, Location, Recommendation), False Positives, Next Steps." Mention severity scales (Critical/High/Medium/Low/Info) and any required schemas.

**`## Example Prompt`** — A realistic prompt a user would paste. Use a quote block (`>`). Include repo path, target scope, and what the user wants. 2-4 sentences.

**`## Safety Rules`** — 4-8 bullets. Specific to this skill. Cover: never modify production data, require explicit approval before remediation commits, don't exfiltrate secrets, validate findings before reporting, scope limitations, never auto-disable security controls, ethical use boundaries.

### 4. Validate

```bash
python scripts/validate.py --skill skills/<category>/<your-skill-id>.md
```

Fix any errors before opening a PR.

### 5. Rebuild the catalog

```bash
python scripts/build_catalog.py
```

This regenerates `/catalog/index.md` and `/catalog/index.json` with your new skill.

### 6. Open a PR

Commit message: `Add <skill name> skill`. Link the issue from step 2.

## Common Mistakes to Avoid

- **Generic instructions.** "Check for security issues" is not actionable. "Run `semgrep --config p/owasp-top-ten` on the src/ directory and triage Critical findings" is.
- **Placeholder content.** "TODO: add steps here" will be rejected. Write the full skill before opening a PR.
- **Vague safety rules.** "Be careful with production data" is too vague. "Never commit remediation patches without explicit user approval — always produce a diff for review" is specific.
- **Missing example prompt.** A skill without a usable example prompt is half a skill. Write one that a real user could paste with minimal editing.
- **Wrong category.** A skill about reviewing PRs belongs in `secure-coding` (if focused on security review) or `devops` (if focused on engineering workflow), not `cybersecurity`. When in doubt, open an issue and ask.
