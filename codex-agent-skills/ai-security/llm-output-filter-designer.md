# LLM Output Filter Designer

## Purpose

This Codex skill designs output filters for an LLM application: content moderation (toxicity, PII, regulated content), format validation (JSON schema, regex), and safety guards (no tool invocation without approval). It targets the failure mode of an LLM that returns harmful or malformed output to end users.

## When to Use

Use when launching an LLM feature, after a content moderation incident, when adding structured output (JSON), or before exposing the LLM to a regulated audience (children, patients).

## Codex Instructions

1. Identify the LLM's output surfaces: direct user-facing text, structured data (JSON for tool calls), code, markdown.
2. For each surface, define the acceptable content policy: no PII, no hate speech, no sexual content, no self-harm, no instructions for harmful activities.
3. Choose a moderation stack: OpenAI Moderation API, Azure Content Safety, Perspective API, or a custom classifier.
4. For structured output, define a JSON schema and validate every LLM response with jsonschema or Zod before passing to the consumer.
5. For tool calls, require human-in-the-loop approval for sensitive tools (payments, data deletion, external messaging).
6. Implement regex filters for common leakage patterns: API keys, credit card numbers, SSNs, email addresses.
7. Implement a fallback response when the filter rejects: a safe default message and an alert to the engineering team.
8. Log every filter rejection with the input (redacted), the rejection reason, and the time — for trend analysis.
9. Add unit tests for the filter with known-good and known-bad outputs.
10. Output the filter implementation, the moderation policy, and the test plan.

## Inputs Needed

- LLM application architecture and output surfaces
- Content moderation policy (what is acceptable, what is not)
- Structured output schemas (JSON Schemas) for tool calls
- Sensitive tools that require human approval
- Existing moderation tooling

## Expected Output

A Markdown design document with: (1) Output Surfaces map; (2) Content Policy; (3) Filter Implementation in the app's language; (4) JSON Schema definitions; (5) Test Plan with sample good/bad outputs; (6) Logging and Alerting spec.

## Example Prompt

> Design output filters for our LLM-powered customer support chat. The LLM returns plain text to users and JSON tool calls (refund, escalate). Filter for PII (SSN, credit card), hate speech, and require human approval for refunds > $100. Use OpenAI Moderation API. Produce the implementation in TypeScript.

## Safety Rules

- Never disable a filter to 'fix' a false positive — tune the threshold instead.
- Do not log the raw LLM output if it contains PII — redact before logging.
- Stop and ask the user if the content policy is ambiguous — defaults may not match business expectations.
- If the filter is bypassable via encoding (base64, ROT13), add a normalization step before filtering.
- Never auto-approve a sensitive tool call without human review, even if the filter passes.
- If the LLM is used by minors, follow COPPA / age-appropriate design code.
