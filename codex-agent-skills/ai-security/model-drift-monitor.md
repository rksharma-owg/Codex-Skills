# Model Drift Monitor

## Purpose

This Codex skill designs a monitoring system for ML model drift: input drift (feature distribution shift), output drift (prediction distribution shift), and concept drift (the relationship between input and output changes). It alerts when drift exceeds a threshold, triggering model retraining or rollback.

## When to Use

Use when deploying a model to production, after a model performance degradation incident, or quarterly as part of MLOps hygiene.

## Codex Instructions

1. Identify the model's input features and output predictions to monitor.
2. Capture a baseline distribution of inputs and outputs from a stable production period (e.g., 30 days).
3. Choose drift metrics: Population Stability Index (PSI) for tabular, KL divergence for probabilities, Wasserstein distance for embeddings.
4. Set up streaming aggregation: compute the metric daily on the production traffic.
5. Define thresholds: PSI > 0.25 indicates significant drift; PSI > 0.10 warrants investigation.
6. Define alert routing: drift alert pages the model owner, not the on-call SRE.
7. Define the response playbook: investigate the cause (data pipeline bug, user behavior change, upstream model change), then decide retrain vs rollback vs accept.
8. For concept drift, monitor a downstream business metric (conversion rate, fraud rate) as a proxy when ground truth labels are delayed.
9. Add a dashboard showing drift trends over time per feature.
10. Output the monitoring implementation, alert thresholds, and response playbook.

## Inputs Needed

- Model architecture (tabular, vision, NLP, embeddings)
- Production traffic volume and feature schema
- Available ground-truth labels (real-time, delayed, none)
- Monitoring stack (Prometheus, Datadog, Evidently AI)
- Model owner and retraining cadence

## Expected Output

A Markdown design document with: (1) Drift Metrics per feature; (2) Monitoring Implementation in Python; (3) Alert Rules with thresholds; (4) Response Playbook; (5) Dashboard spec.

## Example Prompt

> Design a drift monitor for our fraud detection model (XGBoost on tabular features). Baseline: 30 days of stable production traffic. Metric: PSI per feature, alert if PSI > 0.25. Ground truth labels are delayed 7 days. Monitoring via Prometheus + Evidently AI. Produce the implementation, alert rules, and response playbook.

## Safety Rules

- Never auto-retrain a model without human review of the drift cause.
- Do not lower a drift threshold to 'fix' alert noise — investigate the cause.
- Stop and ask the user if a drift cause is ambiguous (data bug vs real distribution shift).
- If the model is regulated (credit scoring), drift may trigger compliance reporting — flag this.
- Never log full prediction payloads at INFO — they may contain PII.
- If drift is caused by an upstream model change, coordinate the rollback across both teams.
