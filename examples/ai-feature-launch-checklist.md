---
id: ai-feature-launch-checklist
name: AI Feature Launch Checklist
purpose: Hardening pipeline for a new LLM feature before public launch.
skills:
  - prompt-injection-tester
  - llm-output-filter-designer
  - rag-source-trust-evaluator
  - ai-agent-tool-gatekeeper
  - ai-pii-redactor
  - llm-evaluation-harness-builder
---

# AI Feature Launch Checklist

## Goal

A six-skill hardening pipeline that takes an LLM feature from "works in dev" to "safe to launch publicly". Catches prompt injection, designs output filters, audits RAG sources, gates agent tools, redacts PII, and builds an eval harness to catch regressions.

## Skills Used

1. **[`prompt-injection-tester`](../skills/ai-security/prompt-injection-tester.md)** — red-teams the LLM for direct, indirect, and tool-output injection.
2. **[`llm-output-filter-designer`](../skills/ai-security/llm-output-filter-designer.md)** — designs content moderation, format validation, and safety guards.
3. **[`rag-source-trust-evaluator`](../skills/ai-security/rag-source-trust-evaluator.md)** — audits RAG retrieval sources for trust and injection risk.
4. **[`ai-agent-tool-gatekeeper`](../skills/ai-security/ai-agent-tool-gatekeeper.md)** — designs tool-call allowlist, validation, and human-in-the-loop.
5. **[`ai-pii-redactor`](../skills/ai-security/ai-pii-redactor.md)** — designs PII redaction before logging and before sending to LLM.
6. **[`llm-evaluation-harness-builder`](../skills/ai-security/llm-evaluation-harness-builder.md)** — builds the eval harness to catch regressions on every change.

## Inputs

- LLM application endpoint or test harness
- System prompt (for white-box testing)
- Tools/plugins the LLM can invoke
- Retrieval sources (uploaded docs, web search)
- Compliance scope (GDPR, COPPA, none)

## Steps

1. **Red-team for injection.** Activate `prompt-injection-tester`. Run direct, indirect, and tool-output injection payloads. Block launch on any Critical finding.
2. **Design output filters.** Activate `llm-output-filter-designer`. Implement content moderation, JSON schema validation, human-in-the-loop for sensitive tools.
3. **Audit RAG sources.** Activate `rag-source-trust-evaluator`. Verify sanitization for low-trust sources, content integrity logging, citation requirement.
4. **Gate agent tools.** Activate `ai-agent-tool-gatekeeper`. Classify tools by blast radius, require approval for High-blast, add audit logging.
5. **Add PII redaction.** Activate `ai-pii-redactor`. Redact PII before LLM input, before output, before logging.
6. **Build eval harness.** Activate `llm-evaluation-harness-builder`. Establish baseline scores, set regression thresholds, integrate into CI.

## Expected Output

- `injection-test-report.md` — payloads tested, findings, mitigations
- `output-filter-design.md` — filter implementation, schemas, test plan
- `rag-trust-report.md` — source inventory, sanitization plan
- `tool-gatekeeper-design.md` — tool classification, gatekeeper code
- `pii-redaction-design.md` — redactor implementation, test plan
- `eval-harness/` — harness code, baseline scores, dashboard spec

## Example Invocation

> Run the ai-feature-launch-checklist workflow for our customer support LLM at https://api.example.com/chat. Tools: refund_order, lookup_order, escalate. Retrieval: internal KB (high trust), Confluence (medium), user uploads (low). Compliance: GDPR. Block launch on any Critical finding.

## Safety Notes

- Never launch with an unresolved Critical injection finding.
- High-blast tools (refund, delete) require human-in-the-loop approval, no exceptions.
- The eval harness must run on every prompt or model change as a CI gate.
