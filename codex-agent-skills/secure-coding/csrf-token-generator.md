# CSRF Token Generator

## Purpose

This Codex skill implements or hardens Cross-Site Request Forgery protection by generating per-session, signed CSRF tokens, embedding them in forms and request headers, and validating them server-side with constant-time comparison. It supports both stateful (synchronizer token) and stateless (double-submit cookie) patterns and aligns with OWASP CSRF Prevention Cheat Sheet.

## When to Use

Use when adding CSRF protection to a new app, when migrating from session cookies to JWT-based auth (which changes CSRF exposure), when a pentest reports a CSRF finding, or when introducing SameSite=None cookies (e.g., for cross-origin embeds) that re-open CSRF risk.

## Codex Instructions

1. Inventory every state-changing endpoint: POST, PUT, PATCH, DELETE handlers and any GET that mutates server state.
2. Choose a strategy: synchronizer token for server-rendered apps, double-submit cookie for SPA + API, or SameSite=Strict cookies where supported.
3. For synchronizer tokens, generate a 256-bit cryptographically random token per session and bind it to the session ID via HMAC.
4. For double-submit, issue a CSRF cookie with SameSite=Lax and require the matching value in a custom header (X-CSRF-Token) on every state-changing request.
5. Implement constant-time comparison (crypto.timingSafeEqual, hmac.compare_digest) for token verification — never use === alone.
6. Reject any state-changing request missing the token or with a mismatched token using a generic 403 response.
7. Rotate the token on login and on privilege change; allow token reuse within a single session unless the threat model demands per-request tokens.
8. Configure CORS to disallow credentialed requests from arbitrary origins — CSRF protection is ineffective if CORS reflects the Origin header with credentials allowed.
9. Add tests for each state-changing endpoint: missing token, mismatched token, valid token, and cross-origin request rejection.
10. Document the chosen strategy and how to test it in the project's security README.

## Inputs Needed

- Web framework in use (Express, Django, Spring, Laravel, Next.js)
- Frontend framework (React, Vue, server-rendered templates)
- Cookie strategy (SameSite value, domain, path)
- CORS policy in effect
- Whether the app supports cross-origin embeds or subdomains

## Expected Output

A Markdown report titled 'CSRF Protection Plan' with: (1) Endpoint Inventory listing every state-changing route; (2) Strategy Decision — synchronizer vs double-submit with justification; (3) Patch Diff for token generation, validation middleware, and frontend integration; (4) Test Plan covering missing/mismatched/valid tokens and CORS interactions.

## Example Prompt

> Add CSRF protection to this Express + React app. We use SameSite=Lax session cookies and need double-submit tokens because the SPA calls the API from a different origin. Include the React side that injects X-CSRF-Token on POST/PUT/DELETE.

## Safety Rules

- Never disable CSRF protection on a state-changing route to 'fix' a bug — fix the integration instead.
- Do not log full CSRF tokens at INFO or higher; first 8 chars only for correlation.
- If SameSite=None is required for a cross-origin embed, require the synchronizer-token pattern instead of double-submit.
- Stop and ask the user before changing the CORS policy — incorrect CORS can break or expose the app.
- Never accept CSRF tokens from the request body when a header is also expected; choose one source of truth.
- Reject state-changing requests with no Origin or Referer header unless the user explicitly approves the relaxation.
