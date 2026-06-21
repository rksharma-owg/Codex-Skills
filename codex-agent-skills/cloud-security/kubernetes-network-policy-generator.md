# Kubernetes NetworkPolicy Generator

## Purpose

This Codex skill generates NetworkPolicy YAML for a Kubernetes namespace based on the actual observed traffic between pods. It uses a default-deny baseline and adds allow rules only for observed flows, producing a least-privilege policy without breaking the app.

## When to Use

Use when introducing NetworkPolicy to a namespace, after a pentest reports lateral movement risk, or when onboarding a sensitive workload to an existing cluster.

## Codex Instructions

1. Enable network flow logs (Cilium, Calico, AWS VPC CNI flow logs) for the namespace for 7-14 days.
2. Aggregate the observed flows: source pod, destination pod, port, protocol.
3. Generate a default-deny NetworkPolicy for ingress and egress in the namespace.
4. For each observed flow, generate an allow rule: source label selector, destination label selector, port.
5. Group allow rules by destination pod to reduce policy count.
6. Add explicit allow for DNS (kube-system:coredns on UDP 53) — every pod needs DNS.
7. Add explicit allow for metrics scraping if Prometheus is used (monitoring namespace on the metrics port).
8. Apply the policies in audit mode first (Cilium audit mode, Calico log-only) to catch any missed flows.
9. After 7 days of audit, switch to enforce mode and monitor for dropped packets.
10. Output the NetworkPolicy YAML and a rollout plan (audit -> enforce).

## Inputs Needed

- Kubernetes namespace and CNI (Cilium, Calico, AWS VPC CNI)
- Network flow logs from the namespace (7-14 days)
- Prometheus or other infrastructure that needs to scrape pods
- Whether the namespace uses an egress NAT or VPC endpoints
- Existing NetworkPolicies in the namespace

## Expected Output

A Markdown report with: (1) Observed Flows table; (2) Default-Deny NetworkPolicy YAML; (3) Allow Rules YAML grouped by destination; (4) Audit Mode Plan; (5) Enforcement Plan with monitoring.

## Example Prompt

> Generate NetworkPolicies for the 'payments' namespace in our EKS cluster using Cilium. We have 7 days of flow logs in S3. Default deny ingress and egress, allow only observed flows plus DNS and Prometheus scraping on port 9090. Output an audit-to-enforce rollout plan.

## Safety Rules

- Never apply enforce-mode policies directly without an audit period — pods will drop traffic.
- Do not allow egress to 0.0.0.0/0 in any policy — use specific CIDRs or FQDN egress (Cilium).
- Stop and ask the user if an observed flow to an unexpected destination is legitimate.
- If a policy breaks a pod, fall back to audit mode and investigate before re-enforcing.
- Never log full packet contents in flow logs — log only 5-tuple metadata.
- If the namespace has a pod that legitimately needs broad egress (e.g., a proxy), document it with a justification comment.
