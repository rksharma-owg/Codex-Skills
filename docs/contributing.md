# Contributing

Thanks for your interest in improving the Codex Agent Skills library. This doc covers the contribution workflow and quality bar.

## Ways to Contribute

- **Add a new skill** — see [Skill Authoring Guide](./skill-authoring-guide.md).
- **Improve an existing skill** — tighten instructions, fix a broken link, add an example.
- **Add a workflow** — chain multiple skills for a real-world use case, see `/templates/workflow-template.md`.
- **Report a gap** — open an issue if you can't find a skill for a common task.

## Quality Bar

Every merged skill MUST:

1. **Follow the template.** Start from [`/templates/skill-template.md`](../templates/skill-template.md). Keep all eight sections.
2. **Have valid frontmatter.** Required fields: `id`, `name`, `category`, `difficulty`, `tags`, `summary`, `last_reviewed`. Run `python scripts/validate.py` before opening a PR.
3. **Be substantive.** Target 250-500 words of body content per skill. No placeholder text. No "TODO" sections.
4. **Be distinct.** No near-duplicates of existing skills. Search the catalog first.
5. **Reference real tools and standards.** OWASP, CWE, NIST, CIS, AWS, Kubernetes, etc. — name them where applicable.
6. **Have a realistic example prompt.** A user should be able to paste it into Codex with minimal editing.
7. **Have meaningful safety rules.** Generic "be careful" rules are not enough. Cover specific failure modes for the skill.

## Workflow

1. **Open an issue** for any new skill to discuss fit and avoid duplicate work.
2. **Fork and branch** from `main`: `git checkout -b add-<skill-id>-skill`.
3. **Author the skill** from the template. Run `python scripts/validate.py` locally.
4. **Update the catalog** if you added/removed/renamed a skill: `python scripts/build_catalog.py`.
5. **Open a PR** with the title `Add <skill name> skill`. Link the issue.
6. **Address review feedback.** A maintainer will review within 5 business days.

## Commit Message Conventions

- `Add <skill name> skill` — new skill
- `Improve <skill name> skill` — enhancement to existing
- `Refactor <area>` — structural change
- `Fix broken link in <skill>` — small fix

## Code of Conduct

Be kind. Be specific. Be actionable. Disagreements about skill scope or quality are normal — discuss them in the issue, not the PR.

## License

By contributing, you agree your contributions are licensed under the MIT License.
