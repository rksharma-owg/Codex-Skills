# Review Checklist Generator

## Purpose

This Codex skill generates a per-PR review checklist tailored to the change type, language, framework, and affected areas (auth, payments, infra, UI). It moves beyond generic 'looks good' reviews by surfacing the specific risks a reviewer should verify before approving.

## When to Use

Use as a pre-review step for junior engineers, for PRs touching security-sensitive code, when onboarding a new reviewer, or when standardizing review practices across a team.

## Codex Instructions

1. Read the PR diff and classify the change: feature, bugfix, refactor, migration, infra, security, docs.
2. Identify affected areas by file path: auth/, payments/, db/, infra/, ui/.
3. Generate a base checklist of 5-10 items that apply to every PR: tests added, tests pass, no secrets in diff, no debug logs, changelog updated.
4. Add area-specific items: for auth changes, verify session rotation and CSRF; for payments, verify idempotency keys and audit logs; for migrations, verify rollback; for infra, verify secrets are not in plaintext.
5. Add language-specific items: for Go, verify error wrapping; for Rust, verify unsafe blocks have SAFETY comments; for Python, verify no bare except.
6. Rank items by severity: Must-Fix (blocks merge), Should-Fix (should fix but not blocking), Nice-to-Have.
7. Output the checklist as a comment template the reviewer can paste into the PR.
8. If the project uses a review-bot (Reviewable, Reviewable.io, Gerrit), format the checklist accordingly.
9. Track recurring checklist items across PRs to identify systemic gaps that should become linter rules.
10. Suggest lint rules for items that recur frequently — promote human review to automation over time.

## Inputs Needed

- Repository path
- PR diff or branch names
- Language and framework
- Team's review policy (must-fix vs should-fix thresholds)
- Existing linters/SAST tools to avoid duplicating items

## Expected Output

A Markdown checklist with sections: Must-Fix, Should-Fix, Nice-to-Have. Each item is a checkbox with a one-sentence description. Ready to paste into the PR review comment.

## Example Prompt

> Generate a review checklist for PR #678 in this repo. It touches src/auth/ and db/migrations/. We use Python/Django and have bandit + flake8 in CI — don't duplicate items those tools already cover.

## Safety Rules

- Never mark a security item as 'Nice-to-Have' — always Must-Fix or Should-Fix.
- Do not generate items that duplicate existing CI checks — promote them to linters instead.
- Stop and ask the user if the team's must-fix threshold is ambiguous.
- If the PR touches a regulated area (PCI, HIPAA), add the corresponding compliance verification items.
- Never include proprietary business logic in the checklist — keep items generic and reusable.
- Do not auto-post the checklist to the PR — let the reviewer decide what to post.
