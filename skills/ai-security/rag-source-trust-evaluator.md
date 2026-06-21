---
id: rag-source-trust-evaluator
name: RAG Source Trust Evaluator
category: ai-security
difficulty: Advanced
tags:
  - ai-security
summary: |
  This Codex skill evaluates the trustworthiness of retrieval sources in a RAG pipeline: source provenance, freshness, content integrity, and indirect injection risk.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill evaluates the trustworthiness of retrieval sources in a RAG pipeline: source provenance, freshness, content integrity, and indirect injection risk. It targets the failure mode of a RAG that retrieves from compromised or low-trust sources and propagates the content to the LLM.

## When to Use

Use when designing a RAG pipeline, when adding a new data source, after an indirect injection incident, or when publishing a RAG feature to external users.

## Codex Instructions

1. Inventory the RAG's retrieval sources: internal documents, web search, user uploads, third-party APIs.
2. For each source, classify trust: high (internal curated), medium (user-curated), low (open web, user uploads).
3. For low-trust sources, design a sanitization step: strip markdown instructions, strip HTML, encode special characters before the content reaches the LLM.
4. For each source, define a freshness SLA: how often it is updated, how stale content is detected.
5. For internal documents, verify provenance: who created the document, when, with what authority.
6. For web sources, verify the URL is on an allowlist; reject content from user-supplied URLs without approval.
7. For user uploads, run a malware scan and an indirect-injection scan before indexing.
8. Design content integrity: hash each retrieved chunk and log it so the LLM's response can be traced to its sources.
9. Design a 'source citation' requirement: the LLM must cite the source for every factual claim.
10. Output a RAG trust report and the sanitization patch for the retrieval pipeline.

## Inputs Needed

- RAG architecture (retrieval sources, embedding store, LLM)
- Source inventory with provenance and freshness
- Whether user uploads are allowed
- Existing content moderation for retrieved chunks
- Source citation requirement

## Expected Output

A Markdown report titled 'RAG Source Trust Evaluation' with: (1) Source Inventory with trust classification; (2) Sanitization Plan per source; (3) Content Integrity design (hashing, logging); (4) Source Citation policy; (5) Pipeline Patch for sanitization and citation.

## Example Prompt

> Evaluate the trust of sources in our RAG customer support bot. Sources: internal KB articles (high trust), Confluence (medium), user-uploaded PDFs (low), web search (low). Design sanitization for low-trust sources, content integrity logging, and a citation requirement. Produce a patch for the retrieval pipeline.

## Safety Rules

- Never feed unmoderated user uploads to the LLM — scan first.
- Do not allow the LLM to retrieve from user-supplied URLs without an allowlist.
- Stop and ask the user if a source's trust classification is ambiguous.
- If a source is found compromised, purge its chunks from the embedding store immediately.
- Never log full retrieved chunks at INFO — they may contain PII; log only the chunk ID and source.
- If the RAG handles regulated content, verify the source's data residency.
