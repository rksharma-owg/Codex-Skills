---
id: github-discussion-category-setup
name: GitHub Discussion Category Setup
category: github-automation
difficulty: Beginner
tags:
  - github-automation
summary: |
  This Codex skill sets up GitHub Discussions categories for a repo: Q&A, ideas, show-and-tell, announcements — with templates that guide users to provide the right info.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill sets up GitHub Discussions categories for a repo: Q&A, ideas, show-and-tell, announcements — with templates that guide users to provide the right info. It targets the failure mode of Discussions that duplicate Issues or lack structure.

## When to Use

Use when introducing Discussions to a repo, when separating user questions from bug reports, or when standardizing Discussions across an org.

## Codex Instructions

1. Identify the discussion categories the project needs: Q&A, Ideas, Show & Tell, Announcements, General.
2. Author a template for each category: what info to provide, what to expect, links to docs.
3. Configure the category's acceptance: who can post (anyone, contributors only), who can mark an answer (maintainers).
4. Configure the announcement category: only maintainers can post, anyone can comment.
5. Set up the conversion flow: an issue can be converted to a discussion (and vice versa) when appropriate.
6. Document the category purposes in the repo's README or CONTRIBUTING.md.
7. Test by posting a sample discussion in each category — verify the template renders.
8. Recommend a triage process: a maintainer reviews new discussions daily and routes them.
9. Output the category config (via API or Probot) and the templates.

## Inputs Needed

- Repository (must have Discussions enabled)
- Category list with purposes
- Templates per category
- Triage process (who, when)

## Expected Output

A set of discussion category templates, a configuration script (GitHub API or Probot) to create them, and a CONTRIBUTING.md snippet.

## Example Prompt

> Set up Discussions for our open-source library. Categories: Q&A (anyone can post, maintainers mark answer), Ideas (anyone can post, maintainers convert to issue if accepted), Show & Tell (anyone), Announcements (maintainers only). Templates per category. Document in CONTRIBUTING.md.

## Safety Rules

- Never auto-delete a discussion — only lock or convert.
- Do not allow Discussions to be used for security reports — route those to a private channel.
- Stop and ask the user if a category's purpose is ambiguous.
- If a Discussion reveals a security issue, convert it to a private report immediately.
- Never log discussion contents that contain PII at INFO.
- If the repo is public, verify the templates do not expose internal-only processes.
