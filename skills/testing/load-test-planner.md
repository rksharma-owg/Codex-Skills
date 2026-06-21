---
id: load-test-planner
name: Load Test Planner
category: testing
difficulty: Advanced
tags:
  - jmeter
  - k6
  - locust
  - testing
summary: |
  This Codex skill designs a load test: defines the workload model (read/write ratio, request mix), the load profile (ramp, steady, spike), the SLOs to verify, the metrics to capture, and the analysis to perform.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a load test: defines the workload model (read/write ratio, request mix), the load profile (ramp, steady, spike), the SLOs to verify, the metrics to capture, and the analysis to perform. It produces a k6, Locust, or JMeter script ready to run.

## When to Use

Use before launching a new service, when capacity planning for a marketing event, after a performance regression, or to verify SLO compliance under load.

## Codex Instructions

1. Define the workload model: which endpoints, what read/write ratio, what payload sizes.
2. Define the load profile: ramp-up duration, steady-state load (RPS or concurrent users), spike duration, ramp-down.
3. Define the SLOs to verify: p99 latency, error rate, throughput.
4. Choose the load test tool: k6 (Go-based, scriptable in JS), Locust (Python), JMeter (Java, GUI).
5. Generate the load test script with the workload model and load profile.
6. Define the metrics to capture: per-endpoint RPS, latency percentiles, error rate, server-side CPU/memory.
7. Define the analysis: identify the bottleneck (CPU, memory, DB, network), the saturation point, the SLO compliance.
8. Define the abort conditions: error rate > 1%, p99 latency > 2x SLO.
9. Schedule the test in a staging environment that mirrors production; never load test production without explicit approval.
10. Output the load test script, the runbook, and the report template.

## Inputs Needed

- Target service and endpoints
- Production traffic pattern (or estimate) to model
- SLO targets (p99 latency, error rate, throughput)
- Staging environment capacity (should mirror production)
- Load test tool (k6, Locust, JMeter)

## Expected Output

A load test script in k6/Locust/JMeter syntax, a runbook with execution commands and abort conditions, and a report template for analysis.

## Example Prompt

> Design a k6 load test for our e-commerce checkout API. Workload: 70% GET /product, 20% POST /cart, 10% POST /checkout. Load profile: ramp to 1000 RPS over 5 min, hold 30 min, ramp down. SLO: p99 < 500ms, error rate < 0.1%. Staging mirrors production. Abort if p99 > 1s. Produce the script and runbook.

## Safety Rules

- Never load test production without explicit user sign-off.
- Do not exceed the staging environment's capacity — results will be misleading.
- Stop and ask the user if the workload model is unknown — defaults may not match real traffic.
- If the test causes a staging outage, abort and investigate before re-running.
- Never log full request payloads at INFO if they contain PII.
- If the test reveals a production capacity gap, flag it for capacity planning before the next launch.
