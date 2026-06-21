---
id: terraform-plan-reviewer
name: Terraform Plan Reviewer
category: devops
difficulty: Advanced
tags:
  - checkov
  - devops
  - iam
  - s3
  - terraform
  - tfsec
summary: |
  This Codex skill reviews a Terraform plan output to identify risky changes: resource destruction, replacement (force-new), permission widening, public exposure of private resources, and untagged resources.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill reviews a Terraform plan output to identify risky changes: resource destruction, replacement (force-new), permission widening, public exposure of private resources, and untagged resources. It produces a human-readable risk assessment for the PR reviewer.

## When to Use

Use on every Terraform PR, before applying changes to production, after a major provider upgrade, or when a junior engineer is the PR author.

## Codex Instructions

1. Parse the terraform plan output (JSON or text) and extract the resource change list.
2. Classify each change: create, update in-place, replace (force-new), destroy.
3. For destroy and replace operations, identify dependent resources and estimate blast radius.
4. For IAM changes, verify no permission is widened (e.g., Action: '*' on Resource: '*'); flag any Principal: '*' or wildcard policy.
5. For S3/bucket changes, verify no public-read ACL or policy is introduced.
6. For security group changes, verify no 0.0.0.0/0 ingress on privileged ports.
7. For database changes, verify no public accessibility flag is set to true.
8. Verify all created resources have the project's mandatory tags (owner, env, cost-center).
9. Cross-reference with the project's terraform linter (tflint, checkov, tfsec) findings.
10. Output a risk assessment with a go/no-go recommendation and a list of items requiring human confirmation.

## Inputs Needed

- Terraform plan output file (terraform plan -out=tfplan, then terraform show -json tfplan)
- Target environment (dev, staging, prod)
- Project tagging policy
- Existing IaC scanners (tflint, checkov, tfsec)
- Whether this is a multi-region or multi-account deployment

## Expected Output

A Markdown report titled 'Terraform Plan Review' with: (1) Change Summary table — Resource | Action | Risk | Blast Radius; (2) Risk Highlights: destroys, replacements, permission widenings, public exposures; (3) Recommendation: Go / Go with conditions / No-go; (4) Manual Verification Checklist.

## Example Prompt

> Review the terraform plan in tfplan.json for the prod environment. Flag any resource destruction, IAM permission widening, public S3 exposure, and untagged resources. We use checkov and tfsec — cross-reference their findings. Give me a go/no-go recommendation.

## Safety Rules

- Never recommend 'Go' for a plan that destroys stateful resources (databases, buckets with data) without explicit user sign-off.
- Do not silence a checkov or tfsec finding by adding a skip comment without justification.
- Stop and ask the user if a force-new replacement's blast radius is unknown.
- If the plan affects IAM permissions for production, require a second reviewer.
- Never auto-apply the plan — produce the review only.
- Flag any plan that removes a tag, as this can break cost allocation and access control.
