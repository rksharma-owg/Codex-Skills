---
id: helm-chart-auditor
name: Helm Chart Auditor
category: devops
difficulty: Intermediate
tags:
  - devops
  - ecr
  - helm
  - kubeconform
  - kubernetes
  - rds
summary: |
  This Codex skill reviews Helm charts for security and reliability: values.yaml defaults (privileged securityContext, public LoadBalancer, missing resource limits), template logic (no auto-generated passwords logged, no plaintext secrets), Chart.yaml versioning, and the README's documented values.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill reviews Helm charts for security and reliability: values.yaml defaults (privileged securityContext, public LoadBalancer, missing resource limits), template logic (no auto-generated passwords logged, no plaintext secrets), Chart.yaml versioning, and the README's documented values.

## When to Use

Use before publishing a chart to a registry, when adopting a community chart for production, after a chart-related incident, or when forking a community chart to add internal defaults.

## Codex Instructions

1. Read Chart.yaml and verify the apiVersion (v2 for modern charts), version semver, and appVersion.
2. Read values.yaml and identify defaults that are insecure in production (privileged securityContext, service type LoadBalancer, no resource limits, no probes).
3. Read each template file and verify no auto-generated password is logged via helm hooks or NOTES.txt.
4. Verify Secret values are referenced from existing Secrets or external secret stores, not hardcoded in values.yaml.
5. Verify NetworkPolicy and PodDisruptionBudget templates exist or are documented as out-of-scope.
6. Verify the chart's README documents every value with type, default, and description.
7. Run helm lint and helm template to validate the chart renders without errors.
8. Run kubeconform on the rendered output to verify Kubernetes API compliance.
9. Output a chart audit report with a findings table and a patched values.yaml with secure defaults.
10. Recommend a CI integration (helm-chart-testing, chart-testing-action) to prevent regressions.

## Inputs Needed

- Chart directory path
- Kubernetes version targeted by the chart
- Production cluster's pod security policy
- Whether the chart is published (affects default security posture)
- Existing CI tooling (helm lint, kubeconform, chart-testing)

## Expected Output

A Markdown report titled 'Helm Chart Audit' with: (1) Chart Metadata summary; (2) Findings table — File | Issue | Severity | Fix; (3) Patched values.yaml with secure production defaults; (4) CI Integration Snippet using chart-testing.

## Example Prompt

> Audit the chart in charts/web-app/. We plan to publish it to our internal OCI registry and deploy to a restricted pod-security cluster. Verify securityContext defaults, NetworkPolicy templates, and the README. Produce patched values.yaml and a chart-testing CI snippet.

## Safety Rules

- Never auto-publish a chart to a public registry without explicit user approval.
- Do not change a chart's appVersion without verifying compatibility with the chart's templates.
- Stop and ask the user if a default is intentionally insecure for development convenience.
- If a chart depends on a subchart with known CVEs, flag the subchart and version constraint.
- Never log auto-generated credentials in NOTES.txt — instruct the user to retrieve them from a Secret.
- Do not weaken a security default to satisfy a downstream consumer — document the secure default instead.
