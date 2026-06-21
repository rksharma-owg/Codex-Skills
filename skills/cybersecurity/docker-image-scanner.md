---
id: docker-image-scanner
name: Docker Image Scanner
category: cybersecurity
difficulty: Intermediate
tags:
  - cis
  - cwe
  - cybersecurity
  - docker
  - ecr
  - pci
  - soc-2
  - trivy
summary: |
  This Codex skill scans container images for OS-package CVEs, misconfigurations, exposed secrets, risky defaults, and bloated layers that increase attack surface.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill scans container images for OS-package CVEs, misconfigurations, exposed secrets, risky defaults, and bloated layers that increase attack surface. It exists because containers are the deployment unit for most modern services, and a single vulnerable base image (e.g., `debian:bullseye` with an unpatched `openssl`) or a `COPY .env` mistake can ship a Critical to production. Scanning at build time catches issues SBOM-only audits miss.

## When to Use
Run this skill in CI on every image build, before promoting an image from `dev` to `staging` or `prod` registry, when bumping a base image tag, when a new CVE drops for a package you ship (e.g., `xz-utils`, `log4j`, `openssl`), or during a container hardening sprint to reduce image size and surface. Also use it when auditing a third-party image pulled from Docker Hub before allowing it into your environment.

## Codex Instructions
1. Identify the Dockerfile(s) and image references: `FROM` lines, multi-stage `AS` aliases, build args, and any `docker-compose.yml` `image:` fields.
2. Build the image locally (or accept a pre-built image tarball / registry reference); use `--label` to embed an OCI source annotation if rebuilding.
3. Run `trivy image --format json --severity CRITICAL,HIGH,MEDIUM,LOW <image>` and capture OS-package, language-package, and misconfig findings.
4. Run `grype <image>` as a second source; reconcile by `package@version:distro` tuples.
5. Run `dockle <image>` for CIS Docker Benchmark checks: non-root user, HEALTHCHECK present, `.dockerignore` hygiene, no `latest` tag, `apt-get` cache cleaned, no secrets in `ENV` or `LABEL`.
6. Run `dive <image>` to flag wasted bytes, duplicate files across layers, and layers that re-add files removed later (a common source of leaked secrets that are "deleted" but still in history).
7. Inspect each layer's filesystem for `.env`, `*.pem`, `*.key`, `id_rsa`, `.npmrc`, `.pypirc`, `.git-credentials`, and any `/root/.ssh/` content; treat any hit as Critical.
8. Cross-check base image tags against the official image's digest pinning guidance; flag `:latest` and unpinned digests as Medium (reproducibility and supply-chain risk).
9. Map findings to CWE: CWE-1104 (Use of Unmaintained Third-Party Components), CWE-732 (Incorrect Permission Assignment for Critical Resource), CWE-798 (Hardcoded Credentials), CWE-250 (Execution with Unnecessary Privileges).
10. Recommend a hardened Dockerfile snippet per finding class: pin digests, use `USER nonroot`, add `HEALTHCHECK`, use multi-stage `COPY --from=builder`, and `RUN rm -rf /var/lib/apt/lists/*`.
11. Emit the report as `CONTAINER_SCAN.md` plus a SARIF for GitHub code scanning and a CycloneDX SBOM of the image contents.

## Inputs Needed
- Dockerfile path or pre-built image reference (`registry/repo:tag` or tarball)
- Build context directory (if rebuilding)
- Build arguments and secrets-handling approach (BuildKit `--secret`, `--mount=type=secret`)
- Target registry and promotion path (`dev` → `staging` → `prod`)
- Base image allowlist (if your org restricts to a private mirror)
- Compliance driver (PCI DSS, FedRAMP, SOC 2) if the report feeds an audit
- Prior suppression / exception list (so accepted risks aren't re-flagged)
- Whether the image runs as root by design (e.g., some init containers) — affects non-root finding severity

## Expected Output
A markdown report `CONTAINER_SCAN.md` with sections: Executive Summary (image ref, digest, total findings by severity, base image used, image size), Layer Analysis (per-layer size, wasted bytes, files of concern), Findings Table (ID, Severity, CWE, Type [OS-Pkg/Lang-Pkg/Misconfig/Secret], Package or Rule, Installed, Fixed, Recommendation), CIS Docker Benchmark Results (pass/fail per control), and Hardened Dockerfile (a rewrite proposal). Severity scale: Critical / High / Medium / Low / Info. Emit `container.sarif` and `image.sbom.cdx.json`.

## Example Prompt
> Scan the image built from `/home/z/my-project/analytics-api/Dockerfile` (build context `/home/z/my-project/analytics-api`). It's a Python 3.12 slim-based service we ship to ECR. Run trivy + grype + dockle, check every layer for secrets, and propose a hardened Dockerfile that pins the base image by digest and runs as non-root. Write `CONTAINER_SCAN.md` and emit SARIF + CycloneDX SBOM.

## Safety Rules
- Do not push the image to any registry without explicit user approval in the prompt.
- Never execute the container (`docker run`) as part of scanning; static and filesystem-only analysis only.
- Do not embed real build secrets in the rebuild; use BuildKit `--secret` or skip the rebuild.
- If a Critical secret is found in a layer, treat the image as compromised and recommend immediate rotation — do not just delete the layer.
- Do not flag intentional root usage in init containers without confirming the user's intent.
- Never pull base images from registries other than the org's approved mirror unless the user explicitly allows Docker Hub.
- Keep image digests in the report — never round or truncate them.
- Do not auto-fix the Dockerfile and commit; propose the hardened version in the report for human review.
