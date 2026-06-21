---
id: architecture-decision-record-author
name: Architecture Decision Record Author
category: devops
difficulty: Intermediate
tags:
  - devops
  - gdpr
  - pci
  - rds
summary: |
  This Codex skill authors Architecture Decision Records (ADRs) for significant technical decisions: context, decision, consequences, alternatives considered.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill authors Architecture Decision Records (ADRs) for significant technical decisions: context, decision, consequences, alternatives considered. It targets the failure mode of a decision made in a Slack thread that no one remembers six months later.

## When to Use

Use when making a significant technical decision (new framework, data store, API style), when reversing a previous decision, or when onboarding engineers ask 'why did we choose X?'.

## Codex Instructions

1. Capture the decision context: what problem are we solving, what constraints exist, what's the timeline.
2. Capture the decision: what we decided, in one paragraph.
3. Capture the alternatives considered: each alternative with its pros and cons.
4. Capture the consequences: positive (what we gain), negative (what we lose), neutral (what changes but doesn't matter).
5. Capture the compliance and security implications: does this affect PCI, GDPR, audit?
6. Capture the reversibility: is this decision easy to reverse, hard, or one-way door?
7. Capture the stakeholders: who was consulted, who approved, who is accountable.
8. Use the project's ADR template (often Michael Nygard's MADR or alexandria format).
9. Number the ADR sequentially (0001, 0002) and link to related ADRs.
10. Output the ADR in Markdown, ready to commit to the repo's docs/adr/ folder.

## Inputs Needed

- Decision being made
- Context and constraints
- Alternatives considered
- Stakeholders (consulted, approver)
- Project's ADR template (or use MADR default)

## Expected Output

A Markdown ADR with sections: Title, Status (Proposed/Accepted/Superseded), Context, Decision, Consequences, Alternatives, Compliance, Stakeholders. Ready to commit to docs/adr/.

## Example Prompt

> Author an ADR for our decision to migrate from REST to gRPC for internal service-to-service communication. Context: high-throughput, low-latency requirements. Alternatives: REST+JSON, gRPC, Thrift. Consequences: harder to debug, better performance. Stakeholders: platform team (consulted), CTO (approver). Use MADR format.

## Safety Rules

- Never publish internal architecture details in a public ADR — keep internal-only context in a separate doc.
- Do not mark an ADR as 'Accepted' without the approver's sign-off.
- Stop and ask the user if a decision's compliance implications are unclear.
- If the ADR supersedes a previous one, link to it and explain what changed.
- Never include vendor pricing in a public ADR — it may be under NDA.
- If the decision affects a regulated area, flag the compliance review requirement.
