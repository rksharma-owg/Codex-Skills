---
id: chaos-experiment-designer
name: Chaos Experiment Designer
category: devops
difficulty: Advanced
tags:
  - devops
summary: |
  This Codex skill designs chaos engineering experiments: hypothesis, blast radius, steady-state definition, injection action, abort conditions, and rollback.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs chaos engineering experiments: hypothesis, blast radius, steady-state definition, injection action, abort conditions, and rollback. It targets the failure mode of a chaos experiment that causes an outage because the blast radius was not bounded or the abort condition was missing.

## When to Use

Use when introducing chaos engineering, before a major release to verify resilience, after an incident to verify the fix, or quarterly as part of resilience testing.

## Codex Instructions

1. Identify the resilience hypothesis: 'If a database replica fails, the service continues serving with elevated latency but no errors.'
2. Define the steady state: SLO metrics, error rate, p99 latency, throughput — measured before, during, and after the experiment.
3. Bound the blast radius: experiment in staging, or in production on a single AZ or a single pod, never the whole fleet.
4. Choose the injection: kill a pod, saturate the network, drain a node, fail a dependency, increase CPU load.
5. Define the abort conditions: error rate > 1%, p99 latency > 2x baseline, manual abort by the engineer.
6. Define the rollback: undo the injection, restore the dependency, scale the service back.
7. Schedule the experiment with the on-call engineer aware and a communication plan for affected users.
8. Run a dry-run first to verify the monitoring captures the steady state correctly.
9. Run the experiment for a bounded duration (5-15 minutes) and capture the steady-state metrics.
10. Output a chaos experiment plan ready to execute with the team's chaos tooling (Gremlin, Chaos Mesh, Litmus).

## Inputs Needed

- Target service and the resilience hypothesis
- Chaos tooling available (Gremlin, Chaos Mesh, Litmus, AWS FIS)
- SLO and steady-state metrics for the service
- Blast radius tolerance (staging only, single AZ, single pod)
- On-call schedule and communication plan

## Expected Output

A Markdown experiment plan with: (1) Hypothesis; (2) Steady-State Definition with metric thresholds; (3) Injection Action and target; (4) Abort Conditions; (5) Rollback Procedure; (6) Communication Plan; (7) Execution Schedule; (8) Success Criteria.

## Example Prompt

> Design a chaos experiment to verify our payments service survives a Postgres read-replica failure. Hypothesis: error rate stays < 0.1%, p99 latency stays < 1s. Blast radius: staging only. Injection: terminate the read replica. Abort conditions: error rate > 1% or p99 > 2s. Use Chaos Mesh.

## Safety Rules

- Never run a chaos experiment in production without explicit user sign-off and a communication plan.
- Do not run an experiment with an unbounded blast radius — always bound to a single AZ or pod.
- Stop and ask the user if the abort conditions are ambiguous — better to abort than to investigate.
- If the experiment affects customers, schedule it during low-traffic hours and notify support.
- Never disable monitoring or alerting during an experiment — those are how you detect the abort condition.
- If a rollback fails, treat it as a production incident and follow the incident runbook.
