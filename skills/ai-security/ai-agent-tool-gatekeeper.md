---
id: ai-agent-tool-gatekeeper
name: AI Agent Tool Gatekeeper
category: ai-security
difficulty: Advanced
tags:
  - ai-security
  - ecr
summary: |
  This Codex skill designs a tool-call gatekeeper for an LLM agent that can invoke tools: allowlist of tools per agent, parameter validation, rate limiting, human-in-the-loop approval for sensitive tools, and audit logging.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a tool-call gatekeeper for an LLM agent that can invoke tools: allowlist of tools per agent, parameter validation, rate limiting, human-in-the-loop approval for sensitive tools, and audit logging. It targets the failure mode of a prompt injection causing an LLM to invoke a destructive tool.

## When to Use

Use when adding tools to an LLM agent, after an agent performed an unintended action, before exposing an agent to external users, or when adding a sensitive tool (payments, data deletion, infrastructure changes).

## Codex Instructions

1. Inventory the tools the agent can invoke: read-only (search, lookup), write (send email, post message), destructive (delete, refund, deploy).
2. Classify each tool by blast radius: Low (read-only), Medium (write, reversible), High (destructive, irreversible).
3. For Low tools, allow automatic invocation with rate limiting (e.g., 10 calls/minute).
4. For Medium tools, require audit logging and an alert if invoked more than N times in M minutes.
5. For High tools, require human-in-the-loop approval via Slack, email, or a web dashboard.
6. Validate tool parameters with a JSON schema before invocation; reject invalid calls.
7. Implement a tool-call allowlist per agent: agent X can call tools Y and Z but not W.
8. Implement audit logging: timestamp, agent ID, tool, parameters (redacted), approver, result.
9. Implement a circuit breaker: if a tool fails N times in M minutes, pause the agent.
10. Output the gatekeeper implementation, the tool classification, and the audit log schema.

## Inputs Needed

- Agent inventory and the tools each can invoke
- Tool parameter schemas (JSON Schema)
- Approval channel (Slack, email, web dashboard)
- Rate limit policy per tool
- Audit log storage (SIEM, log warehouse)

## Expected Output

A Markdown design document with: (1) Tool Inventory with blast radius classification; (2) Gatekeeper Implementation in the agent's language; (3) JSON Schemas for tool parameters; (4) Approval Workflow for High-blast tools; (5) Audit Log Schema; (6) Rate Limit and Circuit Breaker config.

## Example Prompt

> Design a tool gatekeeper for our support agent. Tools: lookup_order (Low), send_email (Medium), refund_order (High, requires human approval if > $100), delete_account (High, always requires approval). Implement in Python. Approval via Slack. Audit log to our SIEM. Rate limit 10 calls/minute per tool.

## Safety Rules

- Never allow automatic invocation of a destructive tool without human approval.
- Do not log tool parameters that contain PII or secrets — redact before logging.
- Stop and ask the user if a tool's blast radius is ambiguous.
- If the gatekeeper is bypassed via a new code path, treat it as a security incident.
- Never grant an agent a tool it does not need — least privilege.
- If the agent is exposed to external users, require approval for all Medium and High tools regardless of parameters.
