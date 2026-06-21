---
id: github-codeowners-generator
name: GitHub CODEOWNERS Generator
category: github-automation
difficulty: Beginner
tags:
  - github-automation
summary: |
  This Codex skill generates or updates the CODEOWNERS file: maps directories and file patterns to the responsible teams or individuals, ensuring PRs auto-request the right reviewers.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates or updates the CODEOWNERS file: maps directories and file patterns to the responsible teams or individuals, ensuring PRs auto-request the right reviewers.

## When to Use

Use when introducing CODEOWNERS, when reorganizing the codebase, when a team's responsibility changes, or when reviews are not reaching the right people.

## Codex Instructions

1. Read the codebase's directory structure and identify the ownership boundaries.
2. Consult the org chart or team leads to identify the owner of each major directory.
3. Author the CODEOWNERS file at .github/CODEOWNERS (or /CODEOWNERS, or docs/CODEOWNERS — the first found wins).
4. Use team accounts (@org/team) rather than individuals where possible — survives reorgs.
5. Order rules from most specific to least specific — GitHub uses the last matching rule.
6. Add a default owner at the root level (@org/all-engineers) to catch files outside specific directories.
7. Verify the file with GitHub's CODEOWNERS validator (settings/code-review page in the repo).
8. Test by opening a PR that touches a file in each major directory — verify the right reviewer is requested.
9. Recommend enabling 'Require review from code owners' in the branch protection rule.
10. Output the CODEOWNERS file and the branch protection recommendation.

## Inputs Needed

- Codebase directory structure
- Team-to-directory ownership map (from org chart or team leads)
- GitHub org's team structure
- Existing branch protection rules

## Expected Output

A CODEOWNERS file at .github/CODEOWNERS, plus a recommendation to enable 'Require review from code owners' in branch protection.

## Example Prompt

> Generate a CODEOWNERS file for our monorepo. Directories: src/payments (team: @org/payments), src/auth (@org/security), src/web (@org/frontend), src/mobile (@org/mobile), infra/ (@org/platform). Add @org/all-engineers as default. Verify with GitHub's validator.

## Safety Rules

- Never assign an individual as the owner of a critical directory — use a team.
- Do not leave a directory without an owner — it can be merged without review.
- Stop and ask the user if a directory's owner is ambiguous — better to ask than guess.
- If a team is deprecated, update CODEOWNERS before the team is dissolved.
- Never use CODEOWNERS to bypass review — every directory should have an owner.
- If the CODEOWNERS file is for a public repo, verify the team handles external PRs (some teams are internal-only).
