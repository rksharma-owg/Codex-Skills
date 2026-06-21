---
id: ssl-tls-certificate-rotator
name: SSL/TLS Certificate Rotator
category: devops
difficulty: Intermediate
tags:
  - csp
  - devops
  - mtls
  - tls
summary: |
  This Codex skill designs a certificate rotation plan for HTTPS endpoints, mTLS services, and internal PKI: identifies expiring certs, verifies the new cert chain, plans the deploy order (cert first, then key), and verifies the rotation via SSL Labs or openssl.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a certificate rotation plan for HTTPS endpoints, mTLS services, and internal PKI: identifies expiring certs, verifies the new cert chain, plans the deploy order (cert first, then key), and verifies the rotation via SSL Labs or openssl. It targets the failure mode of an expired cert causing an outage.

## When to Use

Use when introducing automated cert rotation (cert-manager, AWS Certificate Manager), before a cert expires (90-day Let's Encrypt, 1-year internal), after a key compromise, or when migrating from self-signed to a public CA.

## Codex Instructions

1. Inventory all TLS endpoints: public HTTPS, internal mTLS, database connections, queue connections.
2. For each endpoint, identify the certificate's CN/SAN, issuer, expiry date, and key algorithm.
3. Flag certificates expiring within 30 days for urgent rotation; 90 days for planned rotation.
4. Verify the new certificate's chain includes all intermediate CAs; test with openssl verify.
5. Plan the deploy order: deploy the new certificate (with the existing private key) first, then rotate the private key in a second deploy.
6. For mTLS, ensure both peers trust the new CA before rotating; otherwise, the connection breaks.
7. For internal PKI, verify the CRL/OCSP responder is reachable and the new cert is not revoked.
8. Define the verification step: SSL Labs scan for public endpoints, openssl s_client for internal.
9. Define the rollback step: redeploy the old cert if the new one fails verification.
10. Output the rotation runbook with exact commands and the monitoring alert that confirms the rotation.

## Inputs Needed

- Endpoint inventory (public and internal)
- Certificate manager (cert-manager, AWS ACM, GCP Certificate Manager)
- Internal PKI details (CA, CRL/OCSP)
- Whether mTLS is in use
- Existing monitoring for TLS expiry

## Expected Output

A Markdown rotation runbook per endpoint: (1) Certificate details (CN, SAN, issuer, expiry); (2) Deploy Order (cert first, key second); (3) Verification commands; (4) Rollback procedure; (5) Monitoring Alert spec for TLS expiry.

## Example Prompt

> Design a certificate rotation plan for our public HTTPS endpoints (5 domains, Let's Encrypt via cert-manager) and our internal mTLS service mesh (Istio with an internal CA). One cert expires in 20 days. Produce per-endpoint runbooks with deploy order, verification, and rollback.

## Safety Rules

- Never rotate the private key in the same deploy as the certificate — always two deploys.
- Do not disable mTLS to 'fix' a rotation failure — investigate the CA trust issue.
- Stop and ask the user if the internal CA's root is expiring soon — that requires a separate rotation.
- If the cert is for a payment domain, require a second engineer to confirm the rotation.
- Never log the private key at any level — log only the cert fingerprint.
- If the rotation fails, restore the old cert and key before investigating to minimize downtime.
