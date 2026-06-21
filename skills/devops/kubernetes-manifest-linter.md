---
id: kubernetes-manifest-linter
name: Kubernetes Manifest Linter
category: devops
difficulty: Intermediate
tags:
  - checkov
  - cis
  - devops
  - ecr
  - helm
  - kube-score
  - kubeconform
  - kubernetes
summary: |
  This Codex skill reviews Kubernetes manifests (Deployment, Service, Ingress, ConfigMap, Secret) against security and reliability best practices: resource requests/limits, liveness/readiness probes, securityContext (runAsNonRoot, readOnlyRootFilesystem, drop ALL capabilities), networkPolicy, PodDisruptionBudget, and affinity rules.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill reviews Kubernetes manifests (Deployment, Service, Ingress, ConfigMap, Secret) against security and reliability best practices: resource requests/limits, liveness/readiness probes, securityContext (runAsNonRoot, readOnlyRootFilesystem, drop ALL capabilities), networkPolicy, PodDisruptionBudget, and affinity rules.

## When to Use

Use before applying manifests to production, when onboarding a new service, after a pod-security incident, or when preparing for a CIS Kubernetes Benchmark audit.

## Codex Instructions

1. Read all manifest YAML files in the target directory or chart.
2. For each workload (Deployment, StatefulSet, DaemonSet), verify resource requests and limits are set for CPU and memory.
3. Verify liveness and readiness probes are configured with sensible thresholds (failureThreshold, periodSeconds).
4. Verify securityContext at pod and container level: runAsNonRoot=true, runAsUser != 0, readOnlyRootFilesystem=true, allowPrivilegeEscalation=false, capabilities.drop=[ALL].
5. Verify NetworkPolicy restricts ingress and egress to known sources; flag any namespace with default allow-all.
6. Verify PodDisruptionBudget exists for every Deployment with >= 2 replicas to protect node drains.
7. Verify image references use digests rather than tags for production workloads.
8. Verify Secret references point to existing Secrets; flag any Secret with sensitive data in plaintext (use SealedSecrets or external secrets instead).
9. Run kubeconform or kube-score to cross-reference findings.
10. Output a hardened manifest patch and a findings table mapped to CIS Kubernetes Benchmark.

## Inputs Needed

- Manifest directory or Helm chart path
- Kubernetes version in use
- Cluster pod security policy (privileged, baseline, restricted)
- Ingress controller and whether NetworkPolicy is enforced
- Existing CI linting (kubeconform, kube-score, checkov)

## Expected Output

A Markdown report titled 'Kubernetes Manifest Audit' with: (1) Findings table — Workload | Issue | CIS Ref | Severity | Fix; (2) Patched Manifest YAML ready to apply; (3) Pod Security Admission labels recommendation (restricted vs baseline); (4) Apply plan with kubectl diff output.

## Example Prompt

> Audit the manifests in deploy/k8s/ against CIS Kubernetes Benchmark. We run Kubernetes 1.28 with restricted pod security. Verify securityContext, resource limits, probes, NetworkPolicy, and PodDisruptionBudget. Produce a patched manifest and a kubectl diff.

## Safety Rules

- Never auto-apply manifests to a production cluster — produce a diff for human review.
- Do not weaken securityContext to 'fix' a pod that requires root — escalate to the user.
- Stop and ask the user if a workload legitimately needs a privileged security context.
- Never commit a Secret with plaintext data — flag it and propose SealedSecret or ExternalSecret.
- If the cluster does not enforce NetworkPolicy, flag the gap as an infrastructure finding.
- Do not change the image tag to a digest in a chart that uses image-pull automation without verifying compatibility.
