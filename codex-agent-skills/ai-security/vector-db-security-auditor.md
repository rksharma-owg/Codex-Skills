# Vector DB Security Auditor

## Purpose

This Codex skill audits a vector database (Pinecone, Weaviate, Milvus, pgvector) for security: authentication, authorization (per-namespace ACLs), encryption (at rest, in transit), data isolation (multi-tenant), and access logging. It targets the failure mode of a vector DB that allows cross-tenant retrieval.

## When to Use

Use when deploying a vector DB, after a multi-tenant isolation test, before exposing the DB to a partner integration, or as part of a security audit.

## Codex Instructions

1. Identify the vector DB in use and its deployment (managed service, self-hosted).
2. Verify authentication: API keys, OIDC, mTLS — flag any anonymous access.
3. Verify authorization: per-namespace or per-collection ACLs; verify a tenant cannot query another tenant's vectors.
4. Verify encryption at rest: KMS-managed keys, customer-managed keys for regulated data.
5. Verify encryption in transit: TLS 1.2+, certificate pinning for managed services.
6. Verify access logging: who queried what vectors when; logs should be retained per the compliance policy.
7. Verify multi-tenant isolation: vectors are tagged with tenant_id; queries are filtered by tenant_id; the filter is enforced server-side, not client-side.
8. Verify the embedding model is not leaking metadata (some embedding models encode source text in the vector — verify with a retrieval test).
9. Verify backups are encrypted and access-controlled.
10. Output an audit report with findings and a remediation plan.

## Inputs Needed

- Vector DB (Pinecone, Weaviate, Milvus, pgvector, Qdrant)
- Deployment model (managed, self-hosted, embedded)
- Multi-tenant requirements (single-tenant, per-namespace, per-collection)
- Compliance requirement (SOC 2, HIPAA)
- Existing access logging

## Expected Output

A Markdown report titled 'Vector DB Security Audit' with: (1) Configuration Inventory; (2) Findings table — Area | Issue | Severity | Fix; (3) Multi-Tenant Isolation Test Results; (4) Remediation Plan.

## Example Prompt

> Audit our Pinecone deployment for a multi-tenant RAG application. Verify API key auth, per-namespace ACLs, encryption at rest (customer-managed KMS), TLS in transit, and access logging. Test that tenant A cannot retrieve tenant B's vectors. We're SOC 2 compliant. Produce findings and remediation plan.

## Safety Rules

- Never disable authentication to 'fix' a connectivity issue.
- Do not weaken per-tenant isolation to 'simplify' the application — the filter must be server-side.
- Stop and ask the user if a tenant's data residency is regulated.
- If the embedding model is found to leak source text, switch to a different model or add a post-processing step.
- Never log full vector contents — log only the vector ID and tenant.
- If a backup is found unencrypted, restrict access immediately and re-encrypt.
