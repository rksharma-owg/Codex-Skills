# Postmortem Author

## Purpose

This Codex skill authors a blameless postmortem document for a resolved incident: summary, timeline, impact, root cause, contributing factors, what went well, what went poorly, action items. It targets the failure mode of a postmortem that is filed and forgotten.

## When to Use

Use within 5 business days of a SEV1 or SEV2 incident resolution, when the team has fresh context, or when the incident-response process requires a postmortem.

## Codex Instructions

1. Gather the incident timeline, the RCA, the comms log, and the action items list.
2. Write a one-paragraph summary: what happened, when, the impact, the resolution.
3. Insert the timeline table from the Incident Timeline Builder skill.
4. Write the impact section: users affected, revenue impact, data exposure, regulatory impact, brand impact.
5. Write the root cause section from the RCA: the systemic cause, not just the trigger.
6. Write the contributing factors: things that made it worse or longer.
7. Write 'what went well': detection worked, rollback was fast, comms were clear — be specific.
8. Write 'what went poorly': detection was slow, rollback failed first time, comms were late — be specific, no blame.
9. Write the action items: each with an owner, due date, and issue tracker link.
10. Recommend a review date (30 days) to verify action items are complete.

## Inputs Needed

- Incident timeline (from Incident Timeline Builder)
- RCA (from Root Cause Analyzer)
- Comms log (status page, customer emails, exec summaries)
- Action items with owners
- Project's postmortem template

## Expected Output

A Markdown postmortem with sections: Summary, Timeline, Impact, Root Cause, Contributing Factors, What Went Well, What Went Poorly, Action Items. Ready to publish to the internal postmortem archive.

## Example Prompt

> Author a postmortem for the 2024-01-15 checkout outage. Use the timeline from #inc-2024-01-15, the RCA doc, and the comms log. Be blameless. Action items: 5 items with owners and due dates. Publish to docs/postmortems/2024-01-15-checkout-outage.md.

## Safety Rules

- Never blame an individual in the postmortem — focus on systemic causes.
- Do not publish the postmortem externally without redacting customer-identifying info and internal hostnames.
- Stop and ask the user if an action item's owner is unknown — unowned actions don't get done.
- If the postmortem reveals a regulatory non-compliance, notify compliance before publishing.
- Never mark an action item as complete without verifying the implementation.
- If the postmortem is for a security incident, coordinate with security before publishing.
