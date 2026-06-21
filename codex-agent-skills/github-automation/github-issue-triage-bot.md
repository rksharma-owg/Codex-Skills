# GitHub Issue Triage Bot

## Purpose

This Codex skill designs a GitHub Actions bot that triages new issues: applies labels based on content, requests more info from the reporter, marks stale issues, and closes duplicates. It targets the failure mode of an issue tracker that grows unbounded.

## When to Use

Use when issue volume exceeds the team's triage capacity, when issues lack labels for routing, or when stale issues clutter the tracker.

## Codex Instructions

1. Identify the triage rules: which labels apply to which issue content (bug, feature, question, security).
2. Choose the bot framework: GitHub Actions with actions/github-script, Probot, or a custom app.
3. Configure the label-on-create action: parse the issue body, apply labels based on keywords.
4. Configure the more-info-needed action: if the issue lacks reproduction steps, comment with a template and apply a 'needs-info' label.
5. Configure the stale-issue action: mark issues with no activity for 30 days as 'stale'; close after 7 more days.
6. Configure the duplicate detection: search for similar issues, comment with a link, apply 'potential-duplicate' label for human review.
7. Configure the security routing: issues with the 'security' label are routed to the security team privately.
8. Test the bot on a staging repo before deploying to production.
9. Document the triage rules in CONTRIBUTING.md so reporters know what to expect.
10. Output the bot workflow YAML and the rules config.

## Inputs Needed

- Triage rules (label-to-content mapping)
- Bot framework preference (Actions, Probot, custom)
- Stale issue policy (days to stale, days to close)
- Security issue routing (private channel)
- CONTRIBUTING.md for documenting the rules

## Expected Output

A GitHub Actions workflow YAML for the triage bot, a rules config file, and a CONTRIBUTING.md snippet documenting the triage process.

## Example Prompt

> Design a triage bot for our open-source repo. Rules: label 'bug' if body contains 'error' or 'crash', 'feature' if it contains 'request' or 'would be nice'. Request more info if no reproduction steps. Mark stale after 30 days, close after 7 more. Route 'security' labeled issues to security@ privately. Document in CONTRIBUTING.md.

## Safety Rules

- Never auto-close a security issue — route it privately first.
- Do not auto-label issues incorrectly — false labels cause routing mistakes.
- Stop and ask the user if a triage rule's intent is ambiguous.
- If the bot breaks the issue tracker, disable it immediately and revert.
- Never log issue contents that contain PII or secrets at INFO.
- If the bot is for a public repo, verify it does not expose internal triage rules.
