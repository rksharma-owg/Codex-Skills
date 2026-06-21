---
id: changelog-generator
name: Changelog Generator
category: github-automation
difficulty: Beginner
tags:
  - github-automation
summary: |
  This Codex skill generates a changelog from git history and PR metadata: groups changes by type (Added, Changed, Fixed, Removed, Security), writes user-facing descriptions, and respects Keep a Changelog format.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates a changelog from git history and PR metadata: groups changes by type (Added, Changed, Fixed, Removed, Security), writes user-facing descriptions, and respects Keep a Changelog format.

## When to Use

Use when releasing a new version, when the changelog is out of sync with the codebase, when automating release notes, or when publishing a library update.

## Codex Instructions

1. Read the git log between the previous release tag and HEAD.
2. Read the PR metadata for each merged PR: title, body, labels, linked issue.
3. Classify each change by type: Added (new feature), Changed (modification), Fixed (bug fix), Removed (deprecation), Security (vuln fix).
4. Write a user-facing description for each change — not the PR title, but what the user experiences.
5. Group changes by type following Keep a Changelog format.
6. Link each change to the PR or issue for traceability.
7. Highlight breaking changes prominently at the top.
8. Highlight security fixes with a Security section and a CVE link if applicable.
9. Append the new release section to CHANGELOG.md; do not overwrite previous releases.
10. Output the updated CHANGELOG.md and a release notes draft for GitHub Releases.

## Inputs Needed

- Previous release tag
- Repository path
- PR label conventions (feature, bug, security, breaking)
- CHANGELOG.md path
- Whether to publish GitHub Release notes

## Expected Output

An updated CHANGELOG.md with the new release section in Keep a Changelog format, plus a release notes draft ready to paste into GitHub Releases.

## Example Prompt

> Generate a changelog for v2.3.0 from the git log since v2.2.0. We use conventional commits (feat:, fix:, BREAKING CHANGE:). Group by Added/Changed/Fixed/Security. Append to CHANGELOG.md. Also produce a GitHub Release notes draft with breaking changes highlighted.

## Safety Rules

- Never publish a security fix in the changelog without coordinating the advisory release.
- Do not include internal-only changes (refactors, test additions) in user-facing release notes.
- Stop and ask the user if a change's classification is ambiguous.
- If the changelog reveals an undocumented breaking change, flag it before publishing.
- Never include customer names or internal hostnames in the changelog.
- If the release fixes a CVE, link to the advisory and credit the reporter if they request it.
