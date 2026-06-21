---
id: readme-auditor
name: README Auditor
category: devops
difficulty: Beginner
tags:
  - devops
  - github-actions
  - rds
summary: |
  This Codex skill audits a project's README for completeness: project description, installation, usage, configuration, testing, contributing, license, security policy, and architecture overview.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits a project's README for completeness: project description, installation, usage, configuration, testing, contributing, license, security policy, and architecture overview. It produces a patch to fill the gaps.

## When to Use

Use when open-sourcing a project, before a public launch, when onboarding new contributors report confusion, or as part of an open-source program office review.

## Codex Instructions

1. Read the existing README.md and inventory the sections present.
2. Compare against the canonical README structure: Title, Badges, Description, Demo, Installation, Usage, Configuration, Testing, Contributing, License, Security Policy, Architecture, Credits, FAQ.
3. For each missing section, draft content using the codebase as the source of truth.
4. Verify the installation instructions work on a clean environment — if not, fix the README or the code.
5. Verify the usage examples are copy-pasteable and produce the documented output.
6. Add badges: CI status, code coverage, latest version, license — link to the actual services.
7. Add a Security Policy section: how to report a vulnerability, the SLA, the supported versions.
8. Add a Contributing section: development setup, coding standards, PR process, code of conduct.
9. Verify the License file exists and the README's license badge matches.
10. Output the patched README and a section-by-section audit report.

## Inputs Needed

- Repository path
- Existing README.md
- Target audience (developers, end users, both)
- Project's CI, coverage, and registry URLs for badges
- Security policy URL

## Expected Output

An audited README.md with all canonical sections filled, verified installation/usage instructions, and accurate badges. Plus an audit report listing what was added or fixed.

## Example Prompt

> Audit the README.md for this open-source Python library. We're preparing for v1.0 release. Verify installation (pip install), usage examples, testing instructions, contributing guide, license (Apache 2.0), and security policy. Add badges for CI (GitHub Actions), coverage (Codecov), and PyPI version. Fix any gaps.

## Safety Rules

- Never publish a security policy that promises a faster SLA than the team can deliver.
- Do not include internal-only setup steps in a public README.
- Stop and ask the user if a usage example's expected output is ambiguous.
- If the README references a private registry, replace with the public one or remove.
- Never claim a license that does not match the LICENSE file.
- If the project has known security caveats, document them in the README.
