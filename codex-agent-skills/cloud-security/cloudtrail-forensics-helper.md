# CloudTrail Forensics Helper

## Purpose

This Codex skill queries AWS CloudTrail logs to investigate a security incident: identifies the source IP, user agent, API calls, and resources affected by a suspicious activity. It produces an evidence timeline and a list of affected resources requiring rotation or rebuild.

## When to Use

Use during an active incident (unauthorized API call, suspicious login, data exfiltration alert), after a GuardDuty finding, or during a post-incident forensic review.

## Codex Instructions

1. Confirm the incident scope: which API call, which principal, which time window, which region.
2. Use CloudTrail Lake or Athena to query the relevant events; filter by eventName, userIdentity.arn, sourceIPAddress, and eventTime.
3. Build a timeline of API calls made by the suspicious principal in the time window.
4. Identify the source IP and user agent; correlate with known locations and tools.
5. Identify affected resources: instances started, S3 objects accessed, IAM roles assumed, secrets accessed.
6. Cross-reference with VPC Flow Logs and S3 access logs if network or object-level detail is needed.
7. Identify credentials used: access keys, session tokens; flag any that may have been exfiltrated.
8. Identify persistence mechanisms: new IAM users, roles, keys, or lambda functions created by the principal.
9. Output an evidence timeline and a list of resources requiring rotation, rebuild, or deletion.
10. Recommend containment steps: revoke credentials, isolate instances, restore from known-good backups.

## Inputs Needed

- AWS account ID and region
- Suspicious activity description (API call, principal, time)
- CloudTrail log delivery (S3 bucket, Athena database, CloudTrail Lake)
- Time window to investigate
- Whether VPC Flow Logs and S3 access logs are available

## Expected Output

A Markdown report titled 'CloudTrail Forensics Report' with: (1) Incident Scope; (2) Evidence Timeline; (3) Source IP and User Agent analysis; (4) Affected Resources table; (5) Persistence Mechanisms found; (6) Containment and Recovery actions.

## Example Prompt

> Investigate a GuardDuty finding in AWS account 123456789012 at 2024-01-15 03:00 UTC: UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration. Principal: role/web-app. Build the API call timeline, identify affected resources, and recommend containment steps.

## Safety Rules

- Never delete CloudTrail logs during an investigation — preserve evidence.
- Do not alert the attacker by changing resources they may be monitoring — coordinate with incident response.
- Stop and ask the user if a credential rotation may break a production service — plan the rotation.
- If the investigation reveals a data breach, follow the breach notification process before sharing the report externally.
- Never log access keys or session tokens in the report — redact.
- If the source IP is internal, escalate to internal security — it may be an insider threat.
