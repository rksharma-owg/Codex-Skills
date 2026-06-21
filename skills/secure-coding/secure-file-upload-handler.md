---
id: secure-file-upload-handler
name: Secure File Upload Handler
category: secure-coding
difficulty: Intermediate
tags:
  - s3
  - secure-coding
summary: |
  This Codex skill designs or audits file upload pipelines to prevent malicious file execution, path traversal via filename, DoS via oversized uploads, and stored XSS via SVG/HTML uploads.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs or audits file upload pipelines to prevent malicious file execution, path traversal via filename, DoS via oversized uploads, and stored XSS via SVG/HTML uploads. It enforces allowlist MIME types, server-side magic-byte verification, randomized storage filenames, sandboxed processing, and per-user quota tracking.

## When to Use

Activate when adding a new upload feature, after a pentest flags upload handling, when migrating uploads from local disk to object storage, or before enabling uploads of risky types (SVG, PDF, Office documents, archives).

## Codex Instructions

1. Inventory every upload endpoint: form-based multipart, base64 in JSON, presigned S3 URLs, drag-and-drop SPA components.
2. For each endpoint, define an allowlist of approved MIME types and file extensions — never use a blacklist.
3. Verify the file's true type by reading magic bytes (python-magic, file --mime-type, Apache Tika), not by trusting the Content-Type header or filename extension.
4. Generate a random, unguessable storage filename (UUIDv4 or 32-byte random hex) and discard the user-supplied filename from the storage path.
5. Store uploads outside the web root or in an object store with no public read by default; serve through a controller that enforces authz.
6. For image uploads, re-encode the image server-side (Pillow, sharp, ImageMagick with a security policy) to strip embedded payloads and EXIF metadata.
7. For PDF/Office uploads, run an antivirus scan (ClamAV) and consider sandboxed rendering to detect malicious macros.
8. Enforce maximum upload size at the web server (nginx client_max_body_size, Express limit) before the request reaches the app.
9. Track per-user upload quota and reject over-quota uploads early with a 413 or 429 response.
10. For SVG uploads, either disable them, sanitize with DOMPurify, or serve with Content-Disposition: attachment and Content-Type: image/svg+xml (never as text/html).
11. Produce a configuration patch for the web server, the upload controller, and the storage layer; include a test plan covering each attack vector.

## Inputs Needed

- Upload endpoint paths and frameworks
- Approved file types and max size
- Storage backend (local disk, S3, GCS, Azure Blob)
- Antivirus / sandboxing tools available (ClamAV, nsjail, gVisor)
- Image processing library in use
- Whether uploads are public or auth-gated

## Expected Output

A Markdown report titled 'File Upload Security Plan' with: (1) Endpoint Inventory — Route | Allowed Types | Max Size | Storage; (2) Patch Diff for the controller, web server config, and storage policy; (3) Attack Surface Table — vector (magic-byte spoof, oversized, path traversal, SVG XSS, polyglot) | mitigation; (4) Test Plan listing payloads to verify each control.

## Example Prompt

> Design a secure image upload endpoint for this Express app. Allow JPEG/PNG/WebP up to 5 MB, store on S3 with random filenames, re-encode with sharp to strip metadata. Block SVG entirely. Show the controller, the multer config, and the S3 upload code.

## Safety Rules

- Never store uploaded files under the web root with their original filename.
- Do not execute uploaded files in any context — even a 'preview' must use sandboxed rendering.
- Do not disable antivirus scanning to 'fix' upload latency without explicit user approval.
- Stop and ask the user if a requested file type is high-risk (SVG, PDF with JS, Office docs with macros).
- Never log raw file contents; log only metadata (filename, size, type, hash).
- Reject archive formats (zip, tar, rar) unless an extraction bomb protection (max decompressed size, max entries) is in place.
