---
id: incident-response-orchestration
name: Incident Response Orchestration
purpose: Walk an on-call engineer from alert to postmortem for a SEV1/SEV2 incident.
skills:
  - incident-severity-classifier
  - incident-timeline-builder
  - forensic-snapshot-collector
  - compromised-credential-responder
  - root-cause-analyzer
  - incident-comms-drafter
  - postmortem-author
---

# Incident Response Orchestration

## Goal

A seven-skill workflow that walks an on-call engineer from the initial alert through containment, forensics, RCA, customer comms, and postmortem. Designed for SEV1 and SEV2 incidents where a structured response prevents mistakes under stress.

## Skills Used

1. **[`incident-severity-classifier`](../skills/incident-response/incident-severity-classifier.md)** — SEV1-4 classification with response actions.
2. **[`incident-timeline-builder`](../skills/incident-response/incident-timeline-builder.md)** — reconstructs the timeline from logs, alerts, chat.
3. **[`forensic-snapshot-collector`](../skills/incident-response/forensic-snapshot-collector.md)** — captures disk/memory/network snapshots.
4. **[`compromised-credential-responder`](../skills/incident-response/compromised-credential-responder.md)** — revokes creds, audits unauthorized access.
5. **[`root-cause-analyzer`](../skills/incident-response/root-cause-analyzer.md)** — 5-Whys to systemic cause.
6. **[`incident-comms-drafter`](../skills/incident-response/incident-comms-drafter.md)** — status page, customer email, exec summary.
7. **[`postmortem-author`](../skills/incident-response/postmortem-author.md)** — blameless postmortem document.

## Inputs

- Initial alert (PagerDuty, GuardDuty, manual report)
- Affected systems inventory
- CloudTrail / audit log access
- On-call schedule and IC contact

## Steps

1. **Classify.** Activate `incident-severity-classifier`. Capture the SEV level, response actions, and who to page.
2. **Build timeline.** Activate `incident-timeline-builder` for the incident window. Capture the timeline to `timeline.md`.
3. **Collect forensics.** If security incident, activate `forensic-snapshot-collector` BEFORE any isolation or rebuild.
4. **Respond to compromise.** If credentials are involved, activate `compromised-credential-responder` to revoke and audit.
5. **Run RCA.** After mitigation, activate `root-cause-analyzer`. Capture to `rca.md`.
6. **Draft comms.** Activate `incident-comms-drafter`. Send status page updates every 30 min for SEV1, hourly for SEV2.
7. **Author postmortem.** Within 5 business days, activate `postmortem-author` using the timeline, RCA, and comms log.

## Expected Output

- `timeline.md` — the incident timeline
- `forensics.md` — snapshot inventory with chain of custody
- `rca.md` — 5-Whys and systemic root cause
- `comms/` — status page updates, customer email, exec summaries
- `postmortem.md` — the blameless postmortem

## Example Invocation

> Run the incident-response-orchestration workflow for the GuardDuty finding at 2024-01-15 03:00 UTC (UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration). Affected: EC2 i-abc123, role web-app. IC: jane. Produce all artifacts under incidents/2024-01-15/.

## Safety Notes

- Never delay credential revocation to "investigate first" — revoke, then investigate.
- Forensic snapshots must be captured BEFORE isolation or rebuild.
- The postmortem is blameless — focus on systemic causes, not individuals.
