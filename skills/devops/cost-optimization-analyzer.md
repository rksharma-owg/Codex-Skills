---
id: cost-optimization-analyzer
name: Cost Optimization Analyzer
category: devops
difficulty: Intermediate
tags:
  - devops
  - s3
summary: |
  This Codex skill analyzes a cloud deployment's cost drivers: oversized compute instances, idle load balancers, over-provisioned databases, missing savings plans, unattached EBS volumes, and over-retained S3 objects.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill analyzes a cloud deployment's cost drivers: oversized compute instances, idle load balancers, over-provisioned databases, missing savings plans, unattached EBS volumes, and over-retained S3 objects. It produces a prioritized list of cost-saving actions with estimated monthly savings.

## When to Use

Use during a FinOps review, before a budget overrun, when onboarding a new account to a savings plan, or quarterly as part of cost governance.

## Codex Instructions

1. Pull cost data from the cloud provider's cost explorer (AWS Cost Explorer, GCP Billing, Azure Cost Management) for the last 90 days.
2. Identify the top 10 cost drivers by service and tag.
3. For each compute service, compare instance size to actual utilization (CPU, memory, network); flag instances with < 30% utilization for > 30 days.
4. For each database, compare provisioned capacity to actual load; flag oversized instances and unused read replicas.
5. Identify unattached EBS volumes and unassociated Elastic IPs; estimate savings from release.
6. Identify S3 buckets with objects older than 90 days in Standard storage; propose lifecycle transition to Infrequent Access or Glacier.
7. Identify load balancers with < 100 requests/day; consider replacing with a cheaper alternative or removing.
8. Estimate savings from Reserved Instances, Savings Plans, or Committed Use Discounts for steady-state workloads.
9. Rank findings by monthly savings and implementation effort.
10. Output a cost optimization report with a prioritized action plan.

## Inputs Needed

- Cloud provider and account ID
- Cost data export (CSV from Cost Explorer, BigQuery billing export)
- Tagging policy (to attribute cost to teams)
- Current commitments (RIs, Savings Plans)
- Constraints: cannot change instance type for stateful workloads, etc.

## Expected Output

A Markdown report titled 'Cost Optimization Analysis' with: (1) Top 10 Cost Drivers; (2) Findings table — Resource | Issue | Monthly Savings | Effort | Risk; (3) Action Plan grouped by effort (quick wins, medium, large); (4) Commitment Strategy for steady-state workloads.

## Example Prompt

> Analyze AWS account 123456789012's cost for the last 90 days. We use AWS Cost Explorer with the 'team' tag. Identify oversized EC2 instances (< 30% CPU for 30 days), unattached EBS volumes, and S3 lifecycle opportunities. Estimate monthly savings and rank by ROI.

## Safety Rules

- Never recommend downsizing a stateful workload (database, queue) without a performance test.
- Do not recommend releasing a resource that is part of a disaster recovery plan.
- Stop and ask the user if a resource's owner tag is missing — do not assume.
- If the savings require a Savings Plan commitment, flag the commitment duration and break clause.
- Never expose cost data in a public report — keep it internal.
- Do not recommend deleting logs or backups to save cost — propose a cheaper storage tier instead.
