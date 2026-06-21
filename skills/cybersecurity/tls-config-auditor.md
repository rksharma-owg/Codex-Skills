---
id: tls-config-auditor
name: TLS Config Auditor
category: cybersecurity
difficulty: Intermediate
tags:
  - csp
  - cwe
  - cybersecurity
  - hipaa
  - mtls
  - nist
  - pci
  - tls
  - vault
summary: |
  This Codex skill audits TLS/SSL configuration across load balancers, web servers, API gateways, sidecar proxies, language-runtime HTTPS clients, and certificate inventories.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill audits TLS/SSL configuration across load balancers, web servers, API gateways, sidecar proxies, language-runtime HTTPS clients, and certificate inventories. It exists because weak TLS — outdated protocols (TLS 1.0/1.1), deprecated cipher suites, missing OCSP stapling, absent HSTS, expired or mis-issued certificates, and SHA-1 signatures — remains one of the most cited PCI DSS and FedRAMP findings, and because the rise of automated tools (testssl.sh, sslyze) means low-effort attackers can fingerprint your TLS posture in seconds.

## When to Use
Run this skill before deploying a new TLS-terminating endpoint, when deprecating TLS 1.0/1.1 (regulatory deadlines like PCI DSS 4.0), after a certificate expiry incident, when adopting mTLS for service-to-service auth, or as part of a quarterly TLS posture audit. Also use it when a tool like SSL Labs reports a grade below A and the team needs a prioritized remediation plan.

## Codex Instructions
1. Identify TLS-terminating surfaces: nginx/Apache/Caddy configs, AWS ALB/NLB/CloudFront listeners, Azure App Gateway/Front Door, GCP HTTPS Load Balancer, Envoy/Istio/Linkerd sidecars, K8s Ingress (nginx-ingress, Traefik, HAProxy), application servers (Node `https.Server`, Go `http.Server` with `TLSConfig`, Java `SSLContext`, Python `ssl.SSLContext`), and CDNs (Cloudflare, Fastly, Akamai).
2. For each surface, capture: protocols enabled (SSLv3, TLS 1.0, 1.1, 1.2, 1.3), cipher suites offered, certificate chain (issuer, validity, signature algorithm, key type and size, SAN list), OCSP stapling on/off, HSTS header presence and `max-age`, session resumption mechanism, and `client-auth` mode (none, optional, required).
3. Run `testssl.sh --severity HIGH --json <host:port>` and `sslyze --json_out=<file> <host>` for live endpoints; reconcile findings.
4. Apply theMozilla SSL Configuration Generator's "Intermediate" (default) or "Modern" profile as the benchmark, depending on the user's compatibility requirement. Flag any deviation.
5. Flag Critical findings: SSLv3 or TLS 1.0 enabled, RC4/3DES ciphers, SHA-1 cert signatures, RSA key <2048 bits or ECDSA key <256 bits, expired certificate, wildcard cert used where SAN-specific should be, missing HSTS on a public-facing endpoint, private key in source.
6. Flag High findings: TLS 1.1 enabled, CBC-mode ciphers with no AEAD preference, missing OCSP stapling on a public endpoint, certificate validity >397 days (CA/Browser Forum cap), no certificate transparency (SCT) embedded, weak DH parameter (<2048 bits).
7. Flag Medium findings: TLS 1.2 without 1.3 enabled, AES-CBC preferred over AES-GCM, no session tickets rotated, HSTS `max-age` < 1 year, no HSTS `preload`.
8. Map findings to CWE: CWE-326 (Inadequate Encryption Strength), CWE-327 (Use of Broken Crypto), CWE-295 (Improper Certificate Validation), CWE-319 (Cleartext Transmission of Sensitive Information).
9. Cross-reference with compliance: PCI DSS 4.0 Req. 4.2.1 (strong cryptography + TLS 1.2+), NIST SP 800-52 Rev. 2 (TLS 1.2/1.3 only), FedRAMP TLS baseline, HIPAA Security Rule §164.312(e)(1) transmission security.
10. Recommend a hardened config snippet per surface using the Mozilla generator's profile; for mTLS, recommend SPIFFE/SPIRE or Istio's identity model over static client certs.
11. Inventory certificate expiry dates and emit a 30/60/90-day expiry calendar; recommend automated rotation via ACM, cert-manager, or Step CA.

## Inputs Needed
- Target surface(s): host:port list, config files, or both
- Browser compatibility requirement (Modern / Intermediate / Old — affects cipher recommendations)
- Compliance driver (PCI DSS 4.0, NIST SP 800-52, FedRAMP, HIPAA, FIPS 140-2/3)
- Certificate inventory source (ACM, cert-manager, Vault PKI, manual)
- mTLS in use? (affects client-auth and trust-chain recommendations)
- Whether HSTS preload is acceptable (30-day rollback window — affects production)
- Existing testssl.sh / sslyze / SSL Labs scan output (to avoid re-running)
- Threat model: internet-facing vs. internal; if internal, what's the trust boundary?

## Expected Output
A markdown report `TLS_AUDIT.md` with sections: Executive Summary (surfaces audited, by-severity counts, top risks, Mozilla profile target), Per-Surface Findings (one subsection per surface: protocols, ciphers, cert details, HSTS, OCSP, with a snippet of the current config and the recommended config), Certificate Inventory (subject, issuer, expiry, signature, key type/size, SANs, CT presence), Compliance Mapping (PCI DSS / NIST 800-52 / FedRAMP / HIPAA controls), and Expiry Calendar (30/60/90/180-day buckets with rotation recommendations). Severity scale: Critical (SSLv3/TLS 1.0, expired cert, SHA-1 cert, key <2048) / High (TLS 1.1, weak ciphers, missing HSTS public) / Medium (no OCSP stapling, no TLS 1.3) / Low (cosmetic). Emit `tls-findings.json` for GRC upload.

## Example Prompt
> Audit TLS on our public-facing endpoints. Live targets: `api.example.com:443`, `www.example.com:443`, `admin.example.com:443`. We also have nginx configs at `/home/z/my-project/edge/nginx/`. We're PCI DSS 4.0 scoped and need to disable TLS 1.0/1.1 by Q3. Run testssl + sslyze, map to NIST SP 800-52 Rev. 2, give me a hardened nginx config for each server block, and write `TLS_AUDIT.md` with a cert expiry calendar.

## Safety Rules
- Do not modify production TLS configs or rotate certificates autonomously; propose changes in the report.
- Never download or store private keys from the targets; key analysis is based on cert chain only.
- If a private key is found in source or config during the audit, treat as Critical and reference CWE-798 — do not copy the key into the report.
- Do not run DoS-grade scans; use testssl's default rate (no `--parallel` >4) and respect `Retry-After`.
- For expired certificates, recommend immediate rotation and flag any service-to-service dependency that would break.
- For HSTS preload recommendations, require the user to acknowledge the 30-day rollback window before including `preload` in the recommended header.
- Never recommend SSLv3, TLS 1.0, or TLS 1.1 as a compatibility fallback; recommend the Mozilla "Old" profile only as a last-resort with explicit risk acceptance documented.
- For FIPS-mode environments, recommend only FIPS-validated cipher suites and modules; do not recommend ChaCha20-Poly1305 unless the module's FIPS certificate includes it.
