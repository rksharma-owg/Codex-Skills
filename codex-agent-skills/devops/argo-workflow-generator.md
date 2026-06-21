# Argo Workflow Generator

## Purpose

This Codex skill generates Argo Workflow YAML for batch, ETL, and ML pipelines with retry strategies, artifact passing, parameter propagation, exit handlers for cleanup, and conditional steps. It targets the failure mode of hand-rolled workflow YAML that breaks on the first retry or fan-out.

## When to Use

Use when introducing Argo Workflows for the first time, when refactoring cron jobs into Argo, when adding ML training pipelines, or when a workflow's retry logic needs hardening.

## Codex Instructions

1. Understand the pipeline goal from the user: input source, processing steps, output destination, schedule.
2. Define each step as a Template with a container image, command, args, and resource requests.
3. Add retryStrategy with a sensible limit (3-5), backoff (exponential), and retryPolicy (OnFailure or OnError).
4. Use artifacts (S3, GCS) to pass large data between steps; use parameters for small metadata.
5. Use dag or steps to express dependencies; prefer dag for complex fan-out.
6. Add an exit handler Template for cleanup (delete temp files, notify Slack) that runs on both success and failure.
7. Use when conditions for conditional steps (e.g., only run validation if previous step succeeded).
8. Set activeDeadlineSeconds to prevent runaway workflows; set ttlStrategy to clean up old workflows.
9. Verify the workflow YAML with argo lint and a dry-run (argo submit --dry-run).
10. Output the workflow YAML, a values file for environment-specific config, and a README explaining how to submit.

## Inputs Needed

- Pipeline description: input, steps, output, schedule
- Container images for each step
- Artifact repository (S3 bucket, GCS bucket)
- Argo Workflows version
- Notification targets (Slack webhook, PagerDuty) for the exit handler

## Expected Output

A Markdown report with: (1) Workflow YAML ready to submit; (2) values.yaml for environment-specific overrides; (3) README with submit and monitor commands; (4) Test Plan listing manual verification steps.

## Example Prompt

> Generate an Argo Workflow that pulls daily CSV exports from S3, validates rows with Great Expectations, transforms with dbt, and loads to Snowflake. Add retry strategy, exit handler that pings Slack, and activeDeadlineSeconds of 2 hours. Use Argo 3.4 syntax.

## Safety Rules

- Never hardcode credentials in the workflow YAML — use Kubernetes Secrets referenced via env vars.
- Do not set resource requests so high that the workflow monopolizes the cluster.
- Stop and ask the user if the workflow should be idempotent (rerunning it must not duplicate data).
- Never log sensitive data (PII, credentials) in step stdout.
- If the workflow writes to production, require an explicit approval step before the write.
- Do not disable the activeDeadlineSeconds to 'fix' a slow step — investigate the slowness.
