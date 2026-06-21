---
id: ai-pii-redactor
name: AI PII Redactor
category: ai-security
difficulty: Intermediate
tags:
  - ai-security
  - anthropic
  - gdpr
  - hipaa
  - openai
  - presidio
summary: |
  This Codex skill designs a PII redaction layer for an LLM application: detects PII in user input and LLM output (SSN, email, phone, credit card, names), redacts or masks before logging, before sending to the LLM, and before returning to the user.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a PII redaction layer for an LLM application: detects PII in user input and LLM output (SSN, email, phone, credit card, names), redacts or masks before logging, before sending to the LLM, and before returning to the user. It targets the failure mode of an LLM that echoes or logs PII.

## When to Use

Use when launching an LLM feature that may receive PII, when integrating with a third-party LLM API, or when preparing for a GDPR/CCPA compliance audit.

## Codex Instructions

1. Inventory the PII types the application may handle: direct (SSN, email, phone) and indirect (names, addresses, account numbers).
2. Choose a PII detection library: Presidio, AWS Comprehend, Azure AI Language, spaCy + custom rules.
3. Configure detectors for each PII type with appropriate confidence thresholds.
4. For LLM input, redact PII before sending to the LLM (replace with placeholders); restore after the LLM responds if the LLM's response references the placeholder.
5. For LLM output, scan for PII and redact before returning to the user or logging.
6. For logging, redact PII before any log line is written; log only the PII type and a hash for correlation.
7. Implement a deny list of patterns that must always be redacted (e.g., credit card regex).
8. Implement a fallback: if the detector is unsure, redact conservatively.
9. Add unit tests with sample PII payloads; verify the redacted output contains no PII.
10. Output the redaction implementation, the detector config, and the test plan.

## Inputs Needed

- PII types in scope (regional: SSN for US, NHS for UK, Aadhaar for India)
- LLM API in use (OpenAI, Anthropic, internal) — affects data residency
- Logging stack (CloudWatch, Datadog, ELK)
- Existing PII detection tooling
- Whether the LLM is fine-tuned (affects where redaction must occur)

## Expected Output

A Markdown design document with: (1) PII Inventory; (2) Detector Configuration per PII type; (3) Redaction Implementation in the app's language; (4) Logging Strategy with redaction; (5) Test Plan with sample payloads.

## Example Prompt

> Design a PII redaction layer for our customer support LLM. PII types: SSN, credit card, email, phone, names. Use Presidio. Redact before sending to OpenAI and before logging to Datadog. Restore placeholders in the LLM response only if the response references the placeholder. Produce the Python implementation.

## Safety Rules

- Never log raw PII at any level — even DEBUG.
- Do not send unredacted PII to a third-party LLM API without a data processing agreement.
- Stop and ask the user if a PII type is region-specific and the detector config is unknown.
- If the redactor fails to detect PII, treat it as a finding — tune the detector.
- Never expose redacted PII in error messages to the end user.
- If the application is regulated (HIPAA, GDPR), verify the redaction meets the regulatory standard.
