# GitHub PR Template Author

## Purpose

This Codex skill authors PR templates (.github/PULL_REQUEST_TEMPLATE.md and multi-template variants) that capture the information reviewers need: summary, why, what changed, test plan, risk, security review.

## When to Use

Use when standardizing PR descriptions, when onboarding new engineers, when reviews reveal missing context, or when adding a security review requirement.

## Codex Instructions

1. Identify the project's review needs: what info does a reviewer need to approve confidently?
2. Author a single template at .github/PULL_REQUEST_TEMPLATE.md, or multiple templates at .github/PULL_REQUEST_TEMPLATE/<name>.md with a chooser.
3. Include sections: Summary (1-2 sentences), Why (link to issue), What Changed (bullets by area), Test Plan (steps), Risk Assessment (Low/Medium/High), Security Review (if applicable), Screenshots (if UI).
4. Use Markdown checkboxes for verification steps the author must complete before requesting review.
5. Include a 'Breaking Change' label that, if checked, blocks merge until a migration guide is added.
6. Include a 'Security' label that, if checked, requests a security reviewer.
7. Test the template by opening a sample PR — verify it renders correctly.
8. Document the template's purpose in CONTRIBUTING.md so authors know how to use it.
9. Recommend a PR linting action (action-autolabel, pull-request-template-check) to enforce required sections.
10. Output the template file and the CONTRIBUTING.md snippet.

## Inputs Needed

- Project's review process and required sections
- Whether multiple templates are needed (feature, bugfix, infra)
- Security review requirement
- Existing CONTRIBUTING.md

## Expected Output

A PR template Markdown file at .github/PULL_REQUEST_TEMPLATE.md (or multiple), plus a CONTRIBUTING.md snippet explaining the template's use.

## Example Prompt

> Author a PR template for our SaaS app. Sections: Summary, Why (link to issue), What Changed (bullets), Test Plan (steps with checkboxes), Risk Assessment (Low/Med/High), Security Review (checkbox, requests security reviewer if checked), Breaking Change (checkbox, blocks merge). Plus a CONTRIBUTING.md snippet.

## Safety Rules

- Never remove a security review section to 'speed up' PRs — it weakens the review process.
- Do not make the template so long that authors skip sections — keep it focused.
- Stop and ask the user if a section's requirement is ambiguous.
- If the template is for a regulated project, include the compliance verification section.
- Never include customer-specific sections in a public template.
- If the template is for a multi-repo org, host it in a .github repo for inheritance.
