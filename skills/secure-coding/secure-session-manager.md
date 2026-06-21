---
id: secure-session-manager
name: Secure Session Manager
category: secure-coding
difficulty: Intermediate
tags:
  - asvs
  - ecr
  - hipaa
  - jwt
  - owasp
  - pci
  - secure-coding
summary: |
  This Codex skill audits and hardens session management: cookie flags, session ID entropy, rotation on authentication, idle and absolute timeouts, server-side invalidation, and CSRF protection pairing.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill audits and hardens session management: cookie flags, session ID entropy, rotation on authentication, idle and absolute timeouts, server-side invalidation, and CSRF protection pairing. It maps every finding to OWASP ASVS V3 (Session Management) and produces actionable patches for the framework in use.

## When to Use

Use this skill when implementing login/logout flows, after a session-fixation or session-hijacking pentest finding, when rotating session secrets during an incident, or before launching a feature that grants long-lived sessions (remember-me, mobile tokens, SSO).

## Codex Instructions

1. Locate the session middleware configuration: cookie settings, session store, ID generator, timeout values, and regeneration logic.
2. Verify the session cookie has Secure=true, HttpOnly=true, SameSite=Lax or Strict, and a __Host- prefix where applicable.
3. Confirm session ID entropy is at least 128 bits from a cryptographically secure RNG (crypto.randomBytes, secrets.token_urlsafe, SystemRandom).
4. Check that a new session ID is issued after every privilege change: login, role elevation, MFA enrollment, password reset.
5. Validate idle timeout (<= 30 minutes for high-risk apps per ASVS V3.5.1) and absolute timeout (<= 24 hours for sensitive apps).
6. Ensure server-side session state can be revoked on logout by deleting the store entry, not just clearing the client cookie.
7. Confirm that session IDs are never logged, never placed in URLs, and never sent over insecure channels.
8. Pair session cookies with CSRF tokens tied to the session; verify the SameSite setting matches the CSRF strategy.
9. For distributed deployments, verify session store serialization and that secrets are rotated via a key chain (old + new) to allow graceful rotation.
10. Output a configuration diff and a test plan covering fixation, timeout, revocation, and cross-origin cookie behavior.

## Inputs Needed

- Repository path containing session/auth code
- Framework and session library (express-session, Django sessions, Spring Session, next-auth)
- Session store backend (Redis, Postgres, in-memory, JWT)
- Threat model or compliance requirement (PCI, HIPAA, ASVS level)
- Whether the app is served from a subdomain (affects __Host- prefix)

## Expected Output

A Markdown report titled 'Session Management Audit' with: (1) Configuration Matrix — Property | Current | Recommended | ASVS Ref | Severity; (2) Patch Diff for cookie flags, rotation, timeouts; (3) Session Lifecycle Diagram showing when IDs are regenerated; (4) Test Plan covering session fixation, idle timeout, logout revocation, and SameSite enforcement.

## Example Prompt

> Audit src/auth/ in this Next.js app using next-auth with JWT sessions. Check cookie flags, rotation on login, idle timeout (should be 30 min), and logout revocation. Recommend patches aligned to ASVS V3.

## Safety Rules

- Never log full session IDs or JWT payloads — only the first 8 characters for correlation.
- Do not weaken SameSite from Strict to Lax to 'fix' a redirect flow without an explicit user decision.
- When rotating session secrets, always support a key chain to avoid mass logout.
- Never auto-apply session store schema migrations on production — produce a runbook instead.
- Stop and ask the user if the deployment topology (multi-region, CDN edge) affects cookie scope.
- Do not introduce long-lived 'remember-me' tokens without bound device tracking and rotation.
