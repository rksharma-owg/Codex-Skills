---
id: observability-bootstrap
name: Observability Bootstrap
category: devops
difficulty: Intermediate
tags:
  - devops
  - ecr
  - grafana
  - pci
  - prometheus
summary: |
  This Codex skill bootstraps the three pillars of observability — structured logging, metrics, and distributed tracing — for a service, using the project's chosen stack (OpenTelemetry, Prometheus, Loki, Tempo, Datadog).
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill bootstraps the three pillars of observability — structured logging, metrics, and distributed tracing — for a service, using the project's chosen stack (OpenTelemetry, Prometheus, Loki, Tempo, Datadog). It produces a working instrumentation patch and a Grafana dashboard skeleton.

## When to Use

Use when launching a new service, when migrating from ad-hoc logging to OpenTelemetry, before an SLO rollout, or when an on-call engineer reports insufficient signals during an incident.

## Codex Instructions

1. Identify the target language/framework and the chosen observability stack.
2. Add structured logging with a correlation ID (trace ID) propagated from incoming requests and emitted on outgoing calls.
3. Add OpenTelemetry tracing instrumentation for HTTP/gRPC handlers, database calls, and external API calls.
4. Add Prometheus metrics: RED metrics (Rate, Errors, Duration) for HTTP, USE metrics (Utilization, Saturation, Errors) for resources.
5. Add business metrics specific to the service (orders_per_minute, payment_failure_rate, active_sessions).
6. Configure the OpenTelemetry Collector endpoint and exporter (OTLP, Jaeger, Tempo).
7. Add a /metrics endpoint protected by an internal-only NetworkPolicy or auth.
8. Generate a Grafana dashboard JSON with panels for the RED metrics, error rate, p50/p95/p99 latency, and business KPIs.
9. Add alerts: high error rate, high p99 latency, low throughput (suggests service down), high resource utilization.
10. Output the instrumentation patch, the dashboard JSON, and the alert rules.

## Inputs Needed

- Service repository path
- Language and framework
- Observability stack (OpenTelemetry + Prometheus/Loki/Tempo, Datadog, New Relic)
- SLO targets (latency p95, error rate budget)
- Existing dashboard folder for the Grafana dashboard

## Expected Output

A Markdown report with: (1) Instrumentation Patch (code diff); (2) Grafana Dashboard JSON ready to import; (3) Alert Rules in PrometheusRule or Datadog monitor format; (4) Verification Steps to confirm signals are flowing.

## Example Prompt

> Bootstrap observability for this Go service. Use OpenTelemetry for traces (export to Tempo), Prometheus for metrics, and structured logging to Loki. Generate RED metrics, a Grafana dashboard, and alerts for high error rate and p99 latency > 500ms.

## Safety Rules

- Never log PII or secrets in structured logs — add a redaction layer.
- Do not enable high-cardinality metrics (e.g., user_id as a label) — they explode Prometheus storage.
- Stop and ask the user if the SLO targets are unknown — defaults may not match business expectations.
- If the service handles regulated data (PHI, PCI), verify the observability stack's data residency.
- Never expose the /metrics endpoint publicly — protect it with NetworkPolicy or auth.
- Do not sample traces at 100% in production without confirming the vendor's ingestion cost.
