# Cloud Network Segmentation Planner

## Purpose

This Codex skill designs a network segmentation strategy for a cloud workload: VPC design, subnet tiers (public, private, data), security group rules, NetworkPolicy for Kubernetes, and firewall rules for east-west traffic. It targets the failure mode of a flat network where a compromise spreads laterally.

## When to Use

Use when designing a new VPC, after a pentest reports lateral movement risk, when migrating to micro-segmentation, or when introducing sensitive workloads (payments, PII) to an existing VPC.

## Codex Instructions

1. Map the workloads to tiers: public-facing (load balancers, CDNs), app (services), data (databases, caches), management (bastions, CI runners).
2. Design subnets: each tier in its own subnet, across multiple AZs for HA.
3. Design security groups: default deny inbound; allow only the specific port and source (security group reference) needed.
4. Design NetworkPolicy for Kubernetes: default deny ingress and egress; allow specific pod-to-pod communication by namespace and label.
5. Design egress controls: NAT gateway for outbound internet, VPC endpoints for AWS service access, no public IPs on private subnets.
6. Design transit: VPC peering or Transit Gateway for multi-VPC; verify no overlapping CIDRs.
7. Design inspection: AWS Network Firewall or Palo Alto at the egress for deep packet inspection if required.
8. Document the allowed flows in a matrix: source, destination, port, protocol, justification.
9. Plan the migration from the current flat network to the segmented network in phases to avoid disruption.
10. Output the segmentation design and the IaC patch (Terraform) for the new network.

## Inputs Needed

- Cloud provider (AWS, Azure, GCP)
- Current network topology
- Workload inventory with sensitivity classification
- Compliance requirement (PCI cardholder data environment isolation)
- Existing VPC peering or Transit Gateway setup

## Expected Output

A Markdown design document with: (1) Workload Tier Mapping; (2) Subnet Design across AZs; (3) Security Group Rules table; (4) NetworkPolicy YAML for Kubernetes; (5) Allowed Flows Matrix; (6) Migration Plan; (7) Terraform Patch for the new network.

## Example Prompt

> Design network segmentation for our AWS production VPC. We have a payments service (PCI scope), a user service (PII), and a public web tier. Three AZs. We use EKS for the app tier. Produce the subnet design, security groups, NetworkPolicy YAML, and a phased migration plan from our current flat VPC.

## Safety Rules

- Never apply segmentation changes to production without a maintenance window.
- Do not isolate a workload from its dependencies without verifying the flow matrix.
- Stop and ask the user if a PCI scope isolation is required — that may need a separate VPC.
- If the migration breaks an existing monitoring or security tool, plan an alternative before cutting over.
- Never open 0.0.0.0/0 on a privileged port in any security group rule.
- If a workload needs internet egress, route through a NAT gateway with flow logs enabled.
