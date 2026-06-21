---
id: authz-bypass-finder
name: Authz Bypass Finder
category: cybersecurity
difficulty: Intermediate
tags:
  - cwe
  - cybersecurity
  - jwt
  - mtls
  - oauth
  - owasp
  - pci
  - rds
  - tls
summary: |
  This Codex skill detects authorization (authz) bypass vulnerabilities — broken object-level authorization (BOLA/IDOR), broken function-level authorization (BFLA), missing tenant isolation in multi-tenant SaaS, and forced browsing to admin endpoints.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill detects authorization (authz) bypass vulnerabilities — broken object-level authorization (BOLA/IDOR), broken function-level authorization (BFLA), missing tenant isolation in multi-tenant SaaS, and forced browsing to admin endpoints. It exists because Broken Access Control is #1 on the OWASP Top 10 2021 (A01), accounts for the largest share of web-app bug bounty payouts, and is the class most likely to cause a regulator-reportable breach involving PII exfiltration. Authz flaws are subtle, escape functional tests, and are routinely introduced by refactor.

## When to Use
Run this skill on any PR touching route handlers, middleware, multi-tenant data access, role checks, or admin-only features. Also use it during onboarding of an acquired codebase, when adding a new role to the RBAC matrix, when introducing a new tenant-isolation pattern (row-level security, schema-per-tenant), or after a pen test flags an IDOR. Also use it before exposing a previously internal API to the public internet.

## Codex Instructions
1. Build a route inventory: enumerate every HTTP route handler (Express routes, FastAPI decorators, Spring `@RequestMapping`, Django URL conf, Rails routes, ASP.NET controllers, Go `http.HandleFunc`). For each, capture: HTTP method, path, declared auth requirement (anonymous, authenticated, role-required), and the handler's first data-access call.
2. Identify the authorization enforcement pattern(s) in use: middleware (Express `app.use(authn)`, Django decorator, Spring Security `@PreAuthorize`), per-handler checks (`if req.user.id !== resource.owner_id`), or row-level security at the DB (PostgreSQL RLS, Prisma `extends` with tenant filter).
3. For every route that returns or mutates a resource identified by an ID (`/api/orders/:id`, `/api/users/:userId/documents/:docId`), verify that the handler enforces that the authenticated principal owns or is authorized for that resource. Flag any handler that fetches by ID without an ownership check as BOLA (Critical if the resource is PII/PCI/PHI, High otherwise).
4. For every admin route (`/admin/*`, `@PreAuthorize("hasRole('ADMIN')")`), verify the role check happens before the data-access call, not after. Flag any admin handler where the role check is missing or applied inconsistently across HTTP methods on the same path (BFLA).
5. For multi-tenant services, verify tenant isolation: every DB query must include a `tenant_id` filter (or rely on RLS). Flag any query that loads by global primary key without a tenant filter — this is a Critical cross-tenant data leak. Detect Prisma/SQLAlchemy/Hibernate patterns that bypass the tenant filter (e.g., `Model.objects.get(pk=id)` instead of `Model.objects.get(pk=id, tenant_id=current_tenant)`).
6. Detect forced-browsing vectors: any static file or template served from a path constructed with user input (`/files/<user_input>`), especially when combined with `..` traversal — these are authz bypasses masquerading as path traversal.
7. Detect mass-assignment authz bypasses: any handler that binds user input directly to a model update (`User.update(req.body)`) without an allowlist — an attacker can set `role: 'admin'` or `tenant_id: <other>`.
8. Detect JWT-claim-trust issues: any handler that trusts a `role` or `tenant_id` claim from the JWT without re-checking against a server-side source of truth — tokens can be stolen or mis-issued.
9. Re-baseline severity: BOLA exposing PII/PHI/PAN = Critical; BOLA exposing internal business data = High; BFLA on admin endpoint = High; missing tenant filter on multi-tenant SaaS = Critical; mass-assignment allowing role escalation = Critical.
10. Map findings to CWE: CWE-639 (Authorization Bypass Through User-Controlled Key — BOLA/IDOR), CWE-285 (Improper Authorization — BFLA), CWE-284 (Improper Access Control — tenant isolation), CWE-915 (Improperly Controlled Modification of Dynamically-Determined Object Attributes — mass assignment).
11. Propose a patch per finding: prefer framework-native guards (Spring Security `@PreAuthorize`, Django's `get_object_or_404(Model, pk=id, owner=request.user)`), enforce tenant filter at the ORM/Repository layer so developers cannot forget it, and add an integration test that asserts a 403/404 when a user from tenant A requests a resource in tenant B.
12. Emit `AUTHZ_AUDIT.md` plus SARIF.

## Inputs Needed
- Repository path
- Framework(s) (Express, FastAPI, Spring Boot, Django, Rails, ASP.NET, Go net/http)
- Authn model: session, JWT, OAuth, mTLS — affects how `current_user` is derived
- Authz model: RBAC, ABAC, ReBAC, per-object ownership, tenant-scoped
- Multi-tenant pattern (shared DB with `tenant_id`, schema-per-tenant, DB-per-tenant) — affects isolation recommendations
- Data classification per resource (PII, PHI, PAN, internal) — affects severity
- Existing middleware/role matrix documentation (so the audit can flag deviations)
- Threat model: internet-facing vs. internal; trusted clients vs. untrusted

## Expected Output
A markdown report `AUTHZ_AUDIT.md` with sections: Executive Summary (total routes, by-auth-requirement counts, total findings by severity, top risks), Route Inventory (every route with declared vs. actual auth requirement — flag mismatches), BOLA Findings (one subsection per finding: route, ID source, ownership check present?, patch), BFLA Findings, Tenant Isolation Findings (per query lacking tenant filter), Mass-Assignment Findings, and Regression Test Plan (per-finding integration tests). Severity scale: Critical (BOLA on PII, cross-tenant leak, mass-assign role escalation) / High (BOLA internal, BFLA admin) / Medium (missing audit log on authz decision) / Low (inconsistent 401 vs 404). Emit `authz.sarif`.

## Example Prompt
> Audit authz in `/home/z/my-project/saas-billing-api` (FastAPI + SQLAlchemy, multi-tenant with `tenant_id` on every table, JWT auth with `tenant_id` claim). We just had a pen tester report a BOLA on `/api/invoices/{id}` and I want a full sweep. Build a route inventory, verify tenant isolation on every query, flag any handler that fetches by PK without a tenant filter, propose SQLAlchemy event-listener-based tenant enforcement, and write `AUTHZ_AUDIT.md` with SARIF.

## Safety Rules
- Do not execute requests against live endpoints to "verify" a bypass — static analysis only.
- Never recommend trusting client-supplied `role`, `tenant_id`, or `user_id` fields without server-side re-validation.
- For multi-tenant SaaS, any handler missing a tenant filter on a tenant-scoped table is Critical — do not downgrade for "we'll fix it next sprint."
- For mass-assignment findings, never recommend a denylist; always recommend an allowlist of updatable fields.
- Do not auto-apply patches that change route behavior; propose them for review and require an integration test.
- If JWT claim trust is the bypass, recommend server-side source-of-truth lookup, not adding more claims to the token.
- Never recommend disabling RLS or tenant filters to debug a query — recommend temporary `SET ROLE` for the debug session.
- For BOLA on PII/PHI/PAN, treat as Critical and recommend immediate rotation of access logs for the affected endpoint — attackers may have already exfiltrated.
