---
id: llm-evaluation-harness-builder
name: LLM Evaluation Harness Builder
category: ai-security
difficulty: Advanced
tags:
  - ai-security
  - grafana
summary: |
  This Codex skill builds an evaluation harness for an LLM application: test cases for accuracy, safety, fairness, robustness, and cost; automated scoring (LLM-as-judge, regex, exact match); regression detection; and a dashboard.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill builds an evaluation harness for an LLM application: test cases for accuracy, safety, fairness, robustness, and cost; automated scoring (LLM-as-judge, regex, exact match); regression detection; and a dashboard. It targets the failure mode of an LLM change that silently degrades quality.

## When to Use

Use before launching an LLM feature, when changing the prompt or model, after a fine-tune, or as a CI gate on prompt changes.

## Codex Instructions

1. Define the evaluation dimensions: accuracy (does the answer match the expected?), safety (does it produce harmful content?), fairness (does it perform equally across demographics?), robustness (does it handle adversarial input?), cost (token usage per response).
2. Curate test cases per dimension: at least 50 per dimension for meaningful coverage.
3. Choose automated scoring methods: exact match, regex, LLM-as-judge (with a strong model and a clear rubric), or human-graded for ambiguous cases.
4. Build the harness: input -> LLM call -> score -> aggregate.
5. Run the baseline evaluation on the current model/prompt to establish reference scores.
6. Run the harness on every change (model swap, prompt edit, retrieval change) and compare to baseline.
7. Set thresholds: regression > 5% on any dimension blocks the change.
8. Add cost tracking: input tokens, output tokens, dollar cost per response, p95 latency.
9. Output a dashboard (Streamlit, Grafana) showing per-dimension scores, trend over time, and cost.
10. Recommend a CI integration: run the harness on every PR that touches the prompt or model.

## Inputs Needed

- LLM application endpoint or test harness
- Test case format (CSV, JSONL)
- Scoring method per dimension (LLM-as-judge, regex, human)
- Judge model if using LLM-as-judge (GPT-4, Claude)
- Regression thresholds

## Expected Output

A Markdown design document with: (1) Evaluation Dimensions and test case counts; (2) Harness Implementation in Python; (3) Baseline Scores; (4) Dashboard spec; (5) CI Integration snippet; (6) Cost Tracking plan.

## Example Prompt

> Build an eval harness for our RAG customer support bot. Dimensions: accuracy (50 test Q&A pairs), safety (50 adversarial prompts), fairness (50 across 4 demographics), robustness (50 perturbations), cost. Use GPT-4 as judge with a clear rubric. Block changes with > 5% regression on any dimension. Streamlit dashboard.

## Safety Rules

- Never use real customer data in test cases without redaction.
- Do not auto-merge a change with a safety regression, even if accuracy improves.
- Stop and ask the user if a regression threshold is ambiguous.
- If the LLM-as-judge shows bias, switch to human grading for that dimension.
- Never log full LLM outputs at INFO if they contain PII — redact first.
- If the eval harness itself calls a paid API, set a daily cost budget to avoid surprise bills.
