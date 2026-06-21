---
id: dockerfile-hardener
name: Dockerfile Hardener
category: devops
difficulty: Intermediate
tags:
  - cis
  - devops
  - docker
  - ecr
  - pci
  - snyk
  - trivy
summary: |
  This Codex skill rewrites Dockerfiles to follow container security best practices: multi-stage builds, distroless or alpine base images, non-root user, read-only filesystem, no setuid binaries, minimal installed packages, pinned digests, HEALTHCHECK, and explicit USER directive.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill rewrites Dockerfiles to follow container security best practices: multi-stage builds, distroless or alpine base images, non-root user, read-only filesystem, no setuid binaries, minimal installed packages, pinned digests, HEALTHCHECK, and explicit USER directive. It maps each fix to CIS Docker Benchmark.

## When to Use

Use before pushing a new image to a registry, after a container security scan (Trivy, Snyk Container) reports findings, when preparing for a compliance audit (PCI, FedRAMP), or when reducing image size for faster deploys.

## Codex Instructions

1. Read the existing Dockerfile and identify the base image, build stages, runtime stage, user, exposed ports, and entrypoint.
2. Replace untagged base images (FROM node) with pinned digests (FROM node:20-alpine@sha256:...).
3. Split the build into a build stage (compilers, dev dependencies) and a runtime stage (runtime-only deps, distroless or alpine base).
4. Add a non-root user with a known UID (e.g., 10001) and switch to it with USER before the ENTRYPOINT.
5. Remove setuid binaries, shells, and debug tools from the runtime image unless explicitly required.
6. Add a HEALTHCHECK instruction using the app's health endpoint, with sensible start-period and retries.
7. Minimize installed packages: use --no-install-recommends for apt, --no-cache for apk, and clean package caches in the same RUN.
8. Set read-only filesystem where the app supports it (docker run --read-only) and document any writable paths (e.g., /tmp) with tmpfs mounts.
9. Verify the rebuilt image with Trivy or Snyk Container; output a before/after CVE count.
10. Output a hardened Dockerfile and the docker run command with the recommended security flags.

## Inputs Needed

- Existing Dockerfile path
- Application language and runtime
- Container registry and base image policy (allowed registries, allowed base images)
- Whether the app supports read-only filesystem
- Health check endpoint availability

## Expected Output

A Markdown report titled 'Dockerfile Hardening Report' with: (1) Findings table — CIS Rule | Current | Recommendation; (2) Hardened Dockerfile ready to commit; (3) Trivy scan output before/after; (4) Recommended docker run command with --read-only, --cap-drop=ALL, --security-opt=no-new-privileges.

## Example Prompt

> Harden the Dockerfile in this Node.js app. We use ECR and require distroless base images. Add a non-root user, HEALTHCHECK on /healthz, pin digests, and produce a docker run command with --read-only and --cap-drop=ALL. Run Trivy before and after.

## Safety Rules

- Never weaken the base image policy to 'fix' a build failure — escalate to the user.
- Do not remove a package that the app actually depends on without verifying with the user.
- Stop and ask the user if the app does not support read-only filesystem (some legacy apps write to unexpected paths).
- Never commit an image with a known Critical CVE — block the push.
- If switching to distroless breaks the entrypoint (no shell), document the required code change to the app.
- Do not use 'latest' tag for any base image — always pin to a specific version and digest.
