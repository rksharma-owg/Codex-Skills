---
id: github-actions-workflow-author
name: GitHub Actions Workflow Author
category: github-automation
difficulty: Intermediate
tags:
  - docker
  - ecr
  - github-actions
  - github-automation
  - jest
  - trivy
summary: |
  This Codex skill authors a GitHub Actions workflow YAML for a CI/CD pipeline: triggers, jobs, steps, caching, secrets, environment protection, and concurrency.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill authors a GitHub Actions workflow YAML for a CI/CD pipeline: triggers, jobs, steps, caching, secrets, environment protection, and concurrency. It targets the failure mode of a workflow that is slow, insecure, or fails silently.

## When to Use

Use when introducing CI/CD, when adding a new pipeline (release, security, nightly), when migrating from another CI, or when optimizing an existing workflow.

## Codex Instructions

1. Identify the pipeline's goal: build, test, lint, security scan, deploy, release.
2. Define the triggers: push (branches), pull_request (branches), schedule (cron), workflow_dispatch (manual), workflow_call (reusable).
3. Define the jobs: build, test, lint, scan, deploy — with their dependencies (needs:).
4. Define the runner: ubuntu-latest for most, self-hosted for special hardware, matrix for multi-version.
5. Use caching: actions/cache for dependencies, docker/build-push-action cache-from for images.
6. Use secrets: ${{ secrets.NAME }} — never hardcode; mark secrets as masked in logs.
7. Use environments for protection: production environment with required reviewers, deployment branches.
8. Set concurrency to cancel superseded runs: concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }.
9. Set timeout-minutes to prevent runaway jobs.
10. Validate the YAML with actionlint before committing.
11. Output the workflow YAML and a README explaining the pipeline.

## Inputs Needed

- Pipeline goal (build, test, deploy, etc.)
- Repository and language
- Triggers (push, PR, schedule, manual)
- Deployment environments and protection requirements
- Existing secrets in the repo

## Expected Output

A GitHub Actions workflow YAML file in .github/workflows/, validated with actionlint. Plus a README snippet explaining the pipeline.

## Example Prompt

> Author a GitHub Actions workflow for a Node.js service. Triggers: PR to main, push to main. Jobs: lint (eslint), test (jest), build (docker), scan (trivy), deploy to staging on main, deploy to production on tag. Use environment protection for production (required reviewers). Concurrency to cancel superseded runs. Validate with actionlint.

## Safety Rules

- Never use pull_request_target for untrusted code — it has write access to secrets.
- Do not log secrets at any level — GitHub masks them, but only if they are properly declared.
- Stop and ask the user if a deployment environment's protection is ambiguous.
- If the workflow uses a third-party action, pin to a SHA, not a tag — tags can be moved.
- Never store long-lived credentials in secrets — use OIDC federation where possible.
- If the workflow has a scheduled trigger, verify the cron expression matches the intent.
