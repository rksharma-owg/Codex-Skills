# PR Summary Writer

## Purpose

This Codex skill reads a git diff and the related issue context, then produces a structured PR description: a one-paragraph summary, a 'Why' section, a 'What Changed' bullet list grouped by area, a 'Test Plan' section, and a 'Risk Assessment'. The summary is tuned for reviewers who need to triage in under 60 seconds.

## When to Use

Use as a pre-submit hook for every PR, when onboarding junior engineers who need a template, or when a team wants consistent PR descriptions for changelog generation.

## Codex Instructions

1. Read the diff between the PR branch and the base branch, plus any linked issue or ticket metadata.
2. Classify the change type: feature, bugfix, refactor, chore, docs, test, perf, security.
3. Group modified files by area (api, ui, db, infra, tests) and count line changes per area.
4. Write a one-sentence summary that names the area and the change, not the file names.
5. Write a 'Why' section linking to the issue and explaining the user or business motivation.
6. Write a 'What Changed' list with 3-7 bullets, each naming a concrete behavior change, not a file rename.
7. Write a 'Test Plan' listing the manual and automated verification steps the reviewer should follow.
8. Write a 'Risk Assessment' rating (Low/Medium/High) with a one-sentence justification covering blast radius and reversibility.
9. If the diff touches security-sensitive areas (auth, crypto, payments), add a 'Security Review' note flagging the relevant reviewer.
10. Output the description in the project's PR template format, ready to paste.

## Inputs Needed

- Repository path
- Base branch (e.g., main) and PR branch name
- Linked issue or ticket URL
- PR template path (e.g., .github/PULL_REQUEST_TEMPLATE.md)
- Project conventions for change-type prefixes (feat:, fix:, etc.)

## Expected Output

A Markdown PR description with sections: Summary, Why, What Changed (bulleted by area), Test Plan, Risk Assessment, and optional Security Review. Ready to paste into the PR description field.

## Example Prompt

> Generate a PR summary for branch feature/wallet-transfer against main. The linked issue is #458 'Users should be able to transfer funds between accounts'. Use the project's PR template at .github/PULL_REQUEST_TEMPLATE.md.

## Safety Rules

- Never include secrets, tokens, or PII from the diff in the summary.
- Do not invent test plan steps that the author has not actually performed — list them as 'TODO'.
- If the diff appears to contain a security regression, flag it in the Security Review section, do not bury it.
- Stop and ask the user if the change type is ambiguous (refactor vs breaking change).
- Do not paste internal hostnames or staging URLs into the public PR description.
- If the diff is too large to summarize meaningfully, recommend splitting the PR rather than producing a vague summary.
