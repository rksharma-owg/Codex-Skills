---
id: github-release-automator
name: GitHub Release Automator
category: github-automation
difficulty: Intermediate
tags:
  - argo
  - docker
  - github-actions
  - github-automation
summary: |
  This Codex skill automates the GitHub release process: tag creation, release notes generation, asset upload, and the release announcement.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill automates the GitHub release process: tag creation, release notes generation, asset upload, and the release announcement. It targets the failure mode of a manual release process that is error-prone and inconsistent.

## When to Use

Use when releasing a library or app on GitHub, when moving from manual to automated releases, or when standardizing release notes across multiple repos.

## Codex Instructions

1. Identify the release trigger: a tag push, a manual workflow_dispatch, or a merge to a release branch.
2. Generate the release notes: use GitHub's auto-generated notes, or compile from PR titles since the last release.
3. Bump the version in the project's version file (package.json, VERSION, Cargo.toml).
4. Build the release artifacts: binaries (cross-compile if needed), archives, checksums.
5. Create the GitHub release using the gh CLI or the actions/create-release action.
6. Upload the artifacts to the release using actions/upload-release-asset.
7. Publish to the package registry: npm, PyPI, crates.io, Docker Hub — gated on the release's stability.
8. Announce the release: Slack, mailing list, blog post — using a template.
9. Verify the release on the public page and the package registry.
10. Output the release workflow YAML and the announcement template.

## Inputs Needed

- Repository and language
- Release trigger (tag, manual, merge)
- Package registry (npm, PyPI, crates.io, Docker Hub)
- Version file (package.json, VERSION)
- Announcement channels (Slack, email, blog)

## Expected Output

A GitHub Actions release workflow YAML, an announcement template, and a runbook for the manual trigger.

## Example Prompt

> Automate the release for our Python library on GitHub. Trigger: workflow_dispatch with a version input. Steps: bump version in pyproject.toml, build sdist and wheel, create GitHub release with auto-generated notes, upload to PyPI, announce on Slack. Use OIDC for PyPI trusted publishing.

## Safety Rules

- Never publish to a package registry without OIDC or a short-lived token — long-lived tokens are a supply-chain risk.
- Do not skip the version bump — it causes registry conflicts.
- Stop and ask the user if the release trigger is ambiguous (tag vs merge).
- If the release fails partway, document the rollback (unpublish if the registry allows, or yank).
- Never log the package registry token at any level.
- If the library is a transitive dependency of critical infrastructure, require a second reviewer for the release.
