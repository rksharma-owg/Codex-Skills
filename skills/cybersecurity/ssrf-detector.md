---
id: ssrf-detector
name: SSRF Detector
category: cybersecurity
difficulty: Intermediate
tags:
  - cwe
  - cybersecurity
  - oauth
  - owasp
  - pci
  - rds
  - saml
  - soc-2
summary: |
  This Codex skill detects Server-Side Request Forgery (SSRF) vulnerabilities — classic, blind, and the cloud-metadata variant that powered the Capital One 2019 breach.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill detects Server-Side Request Forgery (SSRF) vulnerabilities — classic, blind, and the cloud-metadata variant that powered the Capital One 2019 breach. It exists because SSRF (OWASP A10:2021) is now a top-10 risk as cloud adoption grew, and a single endpoint that fetches a user-supplied URL can exfiltrate IMDSv1 credentials, scan internal networks, pivot to Redis/Elasticsearch on localhost, or abuse internal admin APIs. The skill focuses on taint from request-controlled URLs to outbound HTTP clients, with IMDS-specific hardening.

## When to Use
Run this skill on any PR that adds URL-fetching functionality: webhook delivery, image proxying, URL preview cards, PDF/image generation from a URL, RSS/Atom fetchers, SAML/OAuth metadata fetch, link checkers, or "import from URL" features. Also use it during cloud migration (when IMDS exposure changes), after a bug bounty SSRF report, or before launching an internal-facing feature that proxies to a third-party API.

## Codex Instructions
1. Identify outbound HTTP clients per language: `requests`, `httpx`, `urllib`, `aiohttp` (Python); `axios`, `node-fetch`, `got`, `request`, `http`/`https` modules (Node.js); `OkHttp`, `HttpClient`, `RestTemplate`, `WebClient` (Java); `net/http` (Go); `Guzzle`, `cURL` (PHP); `HttpClient` (.NET).
2. Treat as **sources**: any user-controllable value used to construct a URL — request params, body fields, headers (including `Host` and `X-Forwarded-For` in some configs), file contents the user uploaded, database columns populated from user input, and SAML/OAuth metadata URLs.
3. Treat as **sinks**: any HTTP client call where the URL is constructed from a source. Also flag DNS-rebinding-prone flows where the URL is validated then re-resolved before the request (`TOCTOU`).
4. Treat as **sanitizers**: allowlist-based host validation (regex or set membership), IP-type checks (deny private/loopback/link-local ranges per RFC 1918, RFC 6598, RFC 4193, `127.0.0.0/8`, `169.254.0.0/16`), DNS resolution pinned to the validated IP (no re-resolution), and cloud-metadata endpoint denial (`169.254.169.254`, `fd00:ec2::254` on AWS).
5. For each sink, trace the source; if no sanitizer is in the path, classify as SSRF. Distinguish blind SSRF (no response visible to attacker) from full SSRF (response returned).
6. Re-baseline severity by cloud context: SSRF on AWS EC2 with IMDSv1 enabled is Critical (credential theft); on GCP/Azure with metadata endpoint reachable, Critical; on bare-metal/on-prem with no metadata service, High; SSRF to an internal-only admin API, High; SSRF to a third-party SaaS that returns errors only, Medium.
7. Detect cloud-metadata-specific sinks: any code that constructs URLs from user input and runs in a Lambda, EC2, ECS, Cloud Run, Cloud Function, or Azure VM context. Treat `169.254.169.254`, `[fd00:ec2::254]`, `metadata.google.internal`, `169.254.169.254/metadata/instance` as Critical if reachable.
8. Detect DNS-rebinding vectors: if the code validates the hostname by DNS lookup but then passes the original hostname to the HTTP client (which re-resolves), flag as High. Recommend pinning the resolved IP via `socket.getaddrinfo` + custom transport.
9. Map each finding to CWE-918 (SSRF).
10. Propose a patch per finding: use an allowlist of hostnames where possible; for arbitrary-URL features, require IP-type validation post-resolution and IP pinning; for cloud deployments, recommend IMDSv2 enforcement at the instance level (IMDSv2 requires a token, defeating most SSRF-to-metadata attacks).
11. Emit `SSRF_FINDINGS.md` plus SARIF.

## Inputs Needed
- Repository path
- Language/runtime and HTTP client library
- Cloud environment (AWS EC2/ECS/Lambda, GCP Cloud Run/Functions, Azure VM/Functions, on-prem, k8s)
- IMDS version (IMDSv1, IMDSv2, or "unknown" — treat unknown as IMDSv1)
- Network topology notes: which internal services are reachable from the app (Redis, Elasticsearch, internal admin APIs)
- Existing URL-validation utility in the codebase (so you don't flag a sanitized path)
- Whether the app is internet-facing
- Threat model or compliance driver (PCI DSS, SOC 2, FedRAMP)

## Expected Output
A markdown report `SSRF_FINDINGS.md` with sections: Executive Summary (cloud context, IMDS version, total findings by severity, top risks), Taint Flows (source → URL construction → HTTP client, with snippet), Cloud Metadata Exposure Analysis (reachable? IMDSv2 enforced?), Findings Table (ID, Severity, CWE, Sink File:Line, Source, Sanitizer Present?, Patch), and Hardening Recommendations (allowlist, IP pinning, IMDSv2 enforcement, egress firewall rules). Severity scale: Critical (SSRF to cloud metadata) / High (SSRF to internal admin API or DB) / Medium (SSRF to arbitrary external host) / Low (SSRF with allowlist bypass but no sensitive target). Emit `ssrf.sarif`.

## Example Prompt
> Detect SSRF in `/home/z/my-project/url-preview-service` (Python 3.11, FastAPI, `httpx`, deployed to AWS ECS Fargate). The service takes a `?url=` parameter and returns OpenGraph metadata. We use IMDSv2 on the tasks but I want a second check. Trace taint from request param to `httpx.get`, classify each finding, propose allowlist + IP-pinning patches, and write `SSRF_FINDINGS.md` with SARIF.

## Safety Rules
- Never send an actual HTTP request to user-supplied URLs or to `169.254.169.254` as part of validation — static analysis only.
- Treat IMDSv1 as a Critical-level configuration issue even if no SSRF is found; recommend IMDSv2 in the hardening section.
- Do not recommend egress-deny-all as a complete fix — pair it with allowlist validation at the application layer.
- For DNS-rebinding findings, require post-resolution IP pinning, not just pre-request hostname validation.
- Do not auto-apply patches; propose them in the report.
- If the codebase runs in a Lambda and the SSRF target is `localhost`/`127.0.0.1`, downgrade to Medium only if you confirm no in-Lambda runtime API exists (rare); otherwise keep at High.
- Never include real metadata responses or credentials in the report — they should not be fetched at all.
- Recommend IMDSv2 with hop-limit = 1 unless the user explicitly states a higher hop is needed for a container orchestration pattern.
