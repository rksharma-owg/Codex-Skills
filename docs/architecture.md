# Architecture

## Repository Layout

```
codex-skills/
├── README.md                    # Project overview, quick start, category tables
├── LICENSE                      # MIT
├── skills/                      # The 123 production-ready Codex skills
│   ├── cybersecurity/           # 15 skills
│   ├── secure-coding/           # 15 skills
│   ├── cloud-security/          # 19 skills (incl. compliance)
│   ├── incident-response/       # 14 skills
│   ├── ai-security/             # 9 skills
│   ├── devops/                  # 26 skills (incl. code-review & docs)
│   ├── testing/                 # 10 skills
│   └── github-automation/       # 14 skills
├── catalog/                     # Indexes + community skill directory
│   ├── index.md                 # Human-readable catalog
│   ├── index.json               # Machine-readable catalog
│   ├── community-top-50.md      # Curated external community skills
│   └── community-top-50.json
├── templates/                   # Skill + workflow templates
│   ├── skill-template.md
│   └── workflow-template.md
├── examples/                    # Multi-skill workflow examples
│   ├── pre-merge-security-gate.md
│   ├── incident-response-orchestration.md
│   └── ai-feature-launch-checklist.md
├── docs/                        # This folder
│   ├── architecture.md
│   ├── contributing.md
│   ├── usage.md
│   └── skill-authoring-guide.md
├── scripts/                     # Validation and tooling
│   ├── validate.py              # Validate skills, frontmatter, links
│   └── build_catalog.py         # Rebuild catalog/index.{md,json}
└── shared/                      # Shared reference material
    └── application-security/    # Reference modules backing the app-sec skill
```

## Design Principles

1. **One file per skill.** Each skill is a standalone Markdown file. No skill spans multiple files (with one exception: `application-security.md` is backed by reference modules in `/shared/`).
2. **YAML frontmatter on every skill.** Frontmatter makes the catalog searchable and machine-readable. Required fields: `id`, `name`, `category`, `difficulty`, `tags`, `summary`, `last_reviewed`.
3. **Eight categories, no deeper nesting.** Skills live directly under `/skills/<category>/<skill-id>.md`. No sub-folders within categories. This keeps discovery flat and link paths predictable.
4. **Real content, not placeholders.** Every skill has substantive `## Purpose`, `## Codex Instructions` (6-12 numbered steps), `## Inputs Needed`, `## Expected Output`, `## Example Prompt`, `## Safety Rules`.
5. **Templates first.** New skills start from `/templates/skill-template.md`. New workflows start from `/templates/workflow-template.md`.
6. **Catalog is generated, not hand-edited.** `/catalog/index.{md,json}` is produced by `scripts/build_catalog.py`. Edit skills, then rebuild.

## Skill File Anatomy

```markdown
---
id: secret-scanner                  # kebab-case, matches filename
name: Secret Scanner                # human title
category: cybersecurity             # one of 8
difficulty: Beginner                # Beginner | Intermediate | Advanced
tags: [cwe, secrets, github-actions]# up to 10
summary: |                          # one-paragraph, < 80 words
  This Codex skill hunts for hardcoded credentials...
last_reviewed: 2026-06-21
---

# Secret Scanner

## Purpose           # 2-4 sentences: what & why
## When to Use       # 2-4 sentences: trigger conditions
## Codex Instructions # 6-12 numbered steps
## Inputs Needed     # 4-8 bullets
## Expected Output   # exact output structure
## Example Prompt    # > quote block, paste-ready
## Safety Rules      # 4-8 bullets
```

## Why Eight Categories?

The original skill library had 11 categories. We consolidated to 8 to reduce overlap and match how teams actually use the skills:

- **code-review** merged into `secure-coding` (PR-side) and `devops` (architecture-side).
- **documentation** merged into `devops` (engineering docs), `incident-response` (runbooks), and `github-automation` (changelogs).
- **compliance** merged into `cloud-security` (PCI/GDPR/SOC 2/HIPAA/ISO/access/audit) and `incident-response` (data retention/vendor risk/DSAR).

This keeps every category substantive (9-26 skills each) and avoids the "two-skills-in-a-folder" problem.
