---
id: ir-tabletop-exercise-designer
name: IR Tabletop Exercise Designer
category: incident-response
difficulty: Advanced
tags:
  - incident-response
summary: |
  This Codex skill designs a tabletop exercise for the incident response team: scenario, inject sequence, expected actions, evaluation criteria, and a post-exercise debrief.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill designs a tabletop exercise for the incident response team: scenario, inject sequence, expected actions, evaluation criteria, and a post-exercise debrief. It targets the failure mode of an IR plan that looks good on paper but fails in practice.

## When to Use

Use quarterly to keep the IR team sharp, after a major process change (new tool, new team), before a compliance audit, or after a real incident reveals a process gap.

## Codex Instructions

1. Choose a scenario relevant to the org's threat model: ransomware, credential compromise, insider threat, supply chain attack, data breach.
2. Write a scenario brief: what is happening, what the team knows at the start, what is unknown.
3. Design a sequence of injects: new information introduced every 10-15 minutes (e.g., 'a second system is now compromised', 'a customer is asking on Twitter').
4. Define the expected actions for each inject: who should be notified, what should be contained, what should be communicated.
5. Define evaluation criteria: detection speed, containment speed, comms quality, escalation appropriateness.
6. Choose a facilitator (not a participant) who controls the injects and observes the team's responses.
7. Choose observers who take notes on the evaluation criteria.
8. Run the exercise for 60-90 minutes; do not let it run over — real incidents are time-boxed too.
9. Hold a debrief immediately after: what went well, what went poorly, what to change in the IR plan.
10. Output the exercise design, the observation notes, and the action items to update the IR plan.

## Inputs Needed

- Scenario choice (ransomware, cred compromise, etc.)
- Org's IR plan and severity matrix
- IR team roster and availability
- Facilitator and observers
- Recent incidents to inform the scenario

## Expected Output

A Markdown exercise design with: (1) Scenario Brief; (2) Inject Sequence with expected actions; (3) Evaluation Criteria; (4) Observation Notes; (5) Debrief Action Items to update the IR plan.

## Example Prompt

> Design a tabletop exercise for our IR team: ransomware scenario affecting the production database. 8 participants, 90 minutes. Injects every 15 minutes: backup discovered encrypted, attacker contacts via email, customer asks on Twitter, exec wants to pay ransom. Evaluate detection, containment, comms, escalation.

## Safety Rules

- Never use real customer data in the exercise scenario — use fake data.
- Do not let the exercise run into a real incident — have a clear 'this is an exercise' label.
- Stop and ask the user if a scenario is too sensitive (e.g., recent real incident may traumatize participants).
- If the exercise reveals a critical gap in the IR plan, address it before the next exercise.
- Never publish exercise materials externally — they reveal IR capabilities to attackers.
- If an exercise participant is also on call, have a backup on-call to handle any real incident.
