---
id: mcp-server-security-auditor
name: MCP Server Security Auditor
category: ai-security
difficulty: Advanced
tags:
  - ai-security
  - mcp
  - model-context-protocol
  - agent-security
summary: |
  Audits Model Context Protocol (MCP) servers and tool implementations for input validation vulnerabilities, unconstrained batch sizes, credential leaks, unbounded resource consumption, and authorization boundary bypasses.
last_reviewed: 2026-09-07
---

## Purpose

This skill guides a security engineer or coding agent in performing a comprehensive security audit of Model Context Protocol (MCP) server implementations. It identifies attack surfaces including unbounded tool arguments, unvalidated batch payloads, silent failures, information disclosure via verbose error messages, and missing permission gates on destructive actions.

## When to Use

Use when developing or deploying an MCP server for AI coding agents, auditing third-party MCP servers before connecting them to agent workspaces, preparing an MCP server for public release or production use, or responding to suspected prompt injection or credential exfiltration incidents.

## Codex Instructions

1. **Protocol & Transport Review:** Verify whether the server uses stdio, streamable HTTP, or WebSockets. Confirm that transport boundaries enforce authentication headers (e.g., bearer tokens), TLS in transit, and origin verification where applicable.
2. **Batch & Payload Caps:** Check JSON-RPC request parsing. Ensure a strict ceiling on batch request sizes (e.g., maximum 100 requests per batch) and verify that empty batches and oversized batches return distinct, actionable error codes (e.g., `-32600`).
3. **Input Schema Validation:** Inspect tool definitions in `tools/list` and execution handlers in `tools/call`. Verify every argument is validated with a strict JSON schema or Pydantic/Zod model. Ensure strings are checked for non-empty values and bounded lengths; numbers are bounded by minimum and maximum values.
4. **Path Traversal & Command Injection:** For filesystem and command-execution tools, verify path canonicalization. Ensure checks prevent both POSIX root paths, Windows drive letters (`C:\`), UNC paths (`\\server\share`), and directory traversal sequences (`../` and `..\`).
5. **Rate Limiting & Denial of Service:** Audit per-client and per-IP rate limits. Verify that heavy operations (FTS search, file ingestion, LLM summarization) include strict timeouts (`asyncio.wait_for`) and return structured error codes rather than hanging connections.
6. **Error Sanitization:** Ensure errors thrown during tool execution do not leak sensitive server paths, stack traces, database schemas, or raw API tokens. Use standard JSON-RPC error codes (`-32700`, `-32600`, `-32601`, `-32602`, `-32603`).
7. **Idempotency & Destructive Gates:** For state-changing tools (create, update, delete, deploy), verify whether idempotency keys are supported and whether human-in-the-loop confirmation or token approval is required before execution.
8. **Audit Logging & Telemetry:** Check that tool calls log invocation timestamps, tool names, sanitized parameters, caller identity, and duration without logging raw API keys, tokens, or PII.

## Inputs Needed

- MCP server source code and manifest (`pyproject.toml`, `package.json`, or Dockerfile)
- Tool definitions (`tools/list` implementation) and call dispatcher (`tools/call`)
- Transport configuration (stdio command vs HTTP host/port bindings)
- Target agent runtime environment (Claude Code, Cursor, Codex, custom agent SDK)

## Expected Output

A comprehensive MCP Security Audit Report containing:
1. **Executive Summary & Risk Score:** Overall risk rating (Critical, High, Medium, Low).
2. **Tool Surface Inventory:** Table of tools, read/write/destructive classification, and input schema strictness.
3. **Vulnerability Findings:** Identified issues with CVSS score, reproduction steps, code references, and remediation code diffs.
4. **Hardening Checklist:** Actionable configuration fixes for transport, rate limiting, and schema validation.

## Example Prompt

> Audit our Python FastMCP server in `src/mcp_server.py`. We expose 5 tools: `read_file`, `execute_query`, `run_command`, `fetch_url`, and `update_record`. Identify any missing parameter validation, check for command injection or directory traversal, verify JSON-RPC error handling, and provide concrete remediation patches for any vulnerabilities found.

## Safety Rules

- Never log or display sensitive credentials, API keys, or database passwords discovered during the audit.
- Do not execute live exploit payloads against production MCP servers without authorization.
- Always classify tools with destructive capabilities (file deletion, database drops, deployments) as requiring explicit human confirmation.
- Ensure all proposed code remediations preserve standard JSON-RPC 2.0 protocol conformance.
