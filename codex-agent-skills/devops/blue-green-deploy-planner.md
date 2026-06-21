# Blue-Green Deploy Planner

## Purpose

This Codex skill designs a blue-green deployment strategy for a service: environment setup, traffic switch mechanism, health checks, rollback procedure, and database compatibility considerations. It targets zero-downtime deploys for stateless services and cautious strategies for stateful ones.

## When to Use

Use when moving from rolling updates to blue-green, before launching a high-traffic service, when a deploy caused an outage, or when introducing a breaking database change that needs zero-downtime migration.

## Codex Instructions

1. Map the service's deploy topology: load balancer, target groups, autoscaling groups, Kubernetes services.
2. Identify the traffic switch mechanism: AWS ALB weighted target groups, Istio VirtualService, Nginx upstream switch, Cloudflare load balancer.
3. Define the health check: endpoint, success threshold, evaluation window before traffic switch.
4. Define the rollback trigger: error rate > X%, p99 latency > Y%, manual abort within Z minutes.
5. Address database compatibility: the new version must run against the old schema (expand), and the old version must run against the new schema (contract).
6. Address background jobs: in-flight jobs at switch time must complete on the old version or be drained.
7. Address sessions: if stateful, ensure sticky sessions or session-store independence from the app version.
8. Define the monitoring dashboard that confirms the switch is healthy.
9. Document the rollback procedure with exact commands and the expected duration.
10. Output a deploy runbook and the infrastructure patch (e.g., Istio VirtualService, ALB listener rule).

## Inputs Needed

- Service repository path
- Deploy platform (Kubernetes + Istio, ECS + ALB, EC2 + Nginx)
- Database engine and whether schema changes are involved
- Current traffic volume and SLO
- Session/state handling (stateless, sticky sessions, external session store)

## Expected Output

A Markdown runbook with: (1) Deploy Topology diagram; (2) Pre-deploy checklist; (3) Switch Procedure with exact commands; (4) Monitoring Dashboard spec; (5) Rollback Procedure with timing; (6) Infrastructure Patch for the traffic switch mechanism.

## Example Prompt

> Design a blue-green deploy for this Kubernetes service using Istio. The service is stateless, uses Postgres, and we're shipping a schema-expand migration in the same release. SLO is 99.95% availability. Produce a runbook and the Istio VirtualService patch for the traffic switch.

## Safety Rules

- Never recommend a blue-green switch without a tested rollback path.
- Do not propose blue-green for a stateful service without addressing data migration explicitly.
- Stop and ask the user if the database change is breaking — blue-green alone cannot make it zero-downtime.
- If the service uses sticky sessions, verify the switch preserves session continuity.
- Never commit the traffic switch script with admin credentials — use short-lived OIDC tokens.
- If the deploy affects a payment or auth flow, require a second on-call engineer to confirm the switch.
