# GitHub Branch Protection Designer

## Purpose

This Codex skill designs branch protection rules for a repository: required reviews, required status checks, required linear history, force-push protection, deletion protection, and signed commits. It targets the failure mode of an unprotected main branch that can be pushed to directly.

## When to Use

Use when setting up a new repo, when tightening security before a public launch, when an audit reveals unprotected branches, or when standardizing protection across an org.

## Codex Instructions

1. Identify the branches to protect: main, release/*, develop — typically main at minimum.
2. Require pull request reviews: at least 1 approval, dismiss stale reviews, require code owner review.
3. Require status checks: CI (build, test, lint), security scans (SAST, SCA) — must pass before merge.
4. Require branches to be up to date before merge — avoids merge-time surprises.
5. Require linear history: rebase or squash merges, no merge commits — keeps history clean.
6. Require signed commits: GPG or SSH signing — prevents impersonation.
7. Restrict force pushes: never on protected branches.
8. Restrict deletions: never on protected branches.
9. Use the GitHub API or terraform-github-provider to apply the rules consistently across repos.
10. Output the branch protection rules in a config file (Terraform, GitHub API JSON) ready to apply.

## Inputs Needed

- Repository name(s)
- Required status checks (CI jobs that must pass)
- Required reviewers (count, code owners)
- Whether signed commits are required
- Org-wide standardization (Terraform or per-repo)

## Expected Output

A branch protection config in Terraform or GitHub API JSON, ready to apply. Plus a summary of the rules for the repo's README.

## Example Prompt

> Design branch protection for our main branch. Require 2 approvals, dismiss stale reviews, require code owner review. Require status checks: ci/test, ci/lint, security/sast, security/sca. Require up-to-date branch. Require linear history (squash). Require signed commits. No force push, no deletion. Apply via Terraform across 12 repos.

## Safety Rules

- Never disable force-push protection on a protected branch — it allows history rewriting.
- Do not lower the required approval count to 'speed up' PRs — escalate to the user instead.
- Stop and ask the user if a required status check is ambiguous (e.g., is it blocking or informational).
- If signed commits are required, verify all contributors have signing set up before enforcing.
- Never expose the GitHub token used to apply the rules in logs.
- If the protection is for a public repo, verify the rules don't block external contributors from submitting PRs.
