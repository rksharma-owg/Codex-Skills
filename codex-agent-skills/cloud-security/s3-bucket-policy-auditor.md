# S3 Bucket Policy Auditor

## Purpose

This Codex skill audits S3 buckets for public exposure, missing encryption, missing versioning, missing access logs, and permissive bucket policies. It targets the failure mode of a misconfigured S3 bucket that exposes customer data to the internet.

## When to Use

Use after a public S3 bucket finding, when onboarding a new bucket, before a compliance audit, or quarterly as part of data security hygiene.

## Codex Instructions

1. Pull all S3 buckets and their configurations: policy, ACL, encryption, versioning, logging, public access block.
2. For each bucket, verify Block Public Access is enabled at the bucket level (and account level if possible).
3. Verify server-side encryption (SSE-S3, SSE-KMS) is enabled; flag buckets without encryption.
4. Verify versioning is enabled for buckets that store important data; flag buckets without versioning.
5. Verify access logging is enabled for buckets that store sensitive data; logs should go to a separate logging bucket.
6. Verify the bucket policy does not allow Principal '*' with Action 's3:GetObject' (public read).
7. Verify the bucket policy does not allow Principal '*' with Action 's3:PutObject' (public write — data injection risk).
8. Verify lifecycle rules exist for buckets with logs or backups to manage cost and retention.
9. Verify Object Lock is enabled for buckets that require WORM (compliance archives).
10. Output an audit report with a per-bucket finding table and a remediation plan.

## Inputs Needed

- AWS account ID
- Bucket inventory (or scope: all buckets, specific bucket)
- Compliance requirement (PCI, HIPAA, GDPR)
- Whether buckets are managed via IaC
- Whether S3 Object Lock is required

## Expected Output

A Markdown report titled 'S3 Bucket Audit' with: (1) Bucket Inventory; (2) Findings table — Bucket | Issue | Severity | Fix; (3) Remediation Plan with exact bucket policy patches; (4) Account-Level Block Public Access recommendation.

## Example Prompt

> Audit all S3 buckets in our production AWS account. We're subject to HIPAA. Verify encryption, versioning, access logging, Block Public Access, and Object Lock where applicable. Flag any bucket policy with Principal '*'.

## Safety Rules

- Never enable public access on a bucket to 'fix' a sharing issue — use presigned URLs.
- Do not disable versioning on a bucket that may be needed for ransomware recovery.
- Stop and ask the user if a bucket's retention policy is unknown — destroying logs may violate compliance.
- If a bucket contains regulated data, verify KMS key rotation is enabled.
- Never log object contents — log only keys and sizes.
- If a bucket is found publicly writable, treat it as a security incident — restrict immediately and review CloudTrail for unauthorized writes.
