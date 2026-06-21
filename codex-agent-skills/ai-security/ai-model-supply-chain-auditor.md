# AI Model Supply Chain Auditor

## Purpose

This Codex skill audits the supply chain of AI models used by an application: model provenance (Hugging Face, OpenAI, internal), license compatibility, training data disclosure, known vulnerabilities in model files (pickle deserialization, malicious weights), and version pinning. It targets the failure mode of a malicious model that executes code on load.

## When to Use

Use when introducing a new model, after a model vulnerability advisory, when open-sourcing a model, or as part of an AI governance review.

## Codex Instructions

1. Inventory all models used by the application: foundation models (OpenAI, Anthropic), open-weight models (Hugging Face, Ollama), fine-tuned models, embeddings models.
2. For each model, capture provenance: repository, version/commit hash, license, intended use.
3. Verify the license is compatible with the application's license (e.g., Llama license, Apache 2.0, GPL).
4. Verify the model file format: PyTorch pickle (.pt, .pth) is unsafe to load from untrusted sources; prefer safetensors.
5. Run a model scan: picklescan for malicious pickle payloads, modelscan for known malicious weights.
6. Verify version pinning: the model is pinned to a specific commit hash, not a moving tag like 'main'.
7. Verify the model's training data disclosure aligns with the application's data policy.
8. Verify the model's output is monitored for drift, bias, and unexpected behavior.
9. Verify the model card is reviewed for known limitations and intended use.
10. Output a model supply chain report with a per-model risk assessment.

## Inputs Needed

- Model inventory (foundation, open-weight, fine-tuned, embeddings)
- Model registry in use (Hugging Face Hub, internal registry)
- Application's license and use case
- Existing model scanning tools (picklescan, modelscan)
- Whether the application is regulated (affects model documentation requirements)

## Expected Output

A Markdown report titled 'AI Model Supply Chain Audit' with: (1) Model Inventory; (2) Per-model Risk Assessment — Provenance | License | Format | Scan Result | Version Pin; (3) Findings table; (4) Remediation Plan; (5) Ongoing Monitoring Recommendations.

## Example Prompt

> Audit the AI models in our application. We use OpenAI gpt-4 (API), all-MiniLM-L6-v2 from Hugging Face (embeddings), and an internal fine-tuned BERT. Verify provenance, license, format (prefer safetensors), run picklescan, verify version pinning. We're Apache 2.0 licensed.

## Safety Rules

- Never load a model from an untrusted source without scanning first.
- Do not use a model with a license incompatible with the application.
- Stop and ask the user if a model's training data is undisclosed and the application is regulated.
- If picklescan finds a malicious payload, quarantine the model and investigate.
- Never log full model weights — log only the model ID, version, and hash.
- If the model is fine-tuned on customer data, verify the data-sharing agreement allows it.
