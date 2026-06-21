<div align="center">

# 🛡️ Codex Agent Skills

**123 production-ready skills for Codex, Claude Code, Cursor, and any LLM-based coding agent.**

[![Skills](https://img.shields.io/badge/skills-123-blue)](./catalog/index.md)
[![Categories](https://img.shields.io/badge/categories-8-green)](#-skill-categories)
[![License](https://img.shields.io/badge/license-MIT-purple)](./LICENSE)

</div>

---

A curated, opinionated library of Codex agent skills for developers, security engineers, AI builders, DevOps teams, product teams, and automation workflows. Each skill is a standalone Markdown file with YAML frontmatter, structured instructions, real example prompts, and safety rules — ready to paste into any LLM-based coding agent.

## ✨ Highlights

- **123 skills** across **8 categories**, each with the same 8-section structure.
- **YAML frontmatter** on every skill — searchable, machine-readable, indexed.
- **3 ready-made workflows** chaining multiple skills for real-world use cases.
- **Validation tooling** — `scripts/validate.py` checks frontmatter, links, and structure.
- **Generated catalog** — `catalog/index.{md,json}` rebuilt from skills on disk.
- **Community directory** — 50 popular external skills alongside our local library.

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/rksharma-owg/Codex-Skills.git
cd Codex-Skills

# Validate the library
python scripts/validate.py

# Browse the catalog
# → open catalog/index.md in your editor or any Markdown viewer
```

To use a skill:

1. Browse [`catalog/index.md`](./catalog/index.md) and pick a skill.
2. Open the skill file (e.g. [`skills/cybersecurity/secret-scanner.md`](./skills/cybersecurity/secret-scanner.md)).
3. Copy the file contents into your agent's system prompt or skill loader.
4. Use the `## Example Prompt` as your starting message.

📖 **Full usage guide:** [`docs/usage.md`](./docs/usage.md)

## 📦 Skill Categories

| Icon | Category | Skills | What it covers |
|------|----------|-------:|----------------|
| 🛡️ | [Cybersecurity](./skills/cybersecurity/) | 15 | Find, triage, and fix exploitable vulnerabilities across code, containers, and infrastructure. |
| 🔒 | [Secure Coding](./skills/secure-coding/) | 16 | Harden code at the source: validation, encoding, sessions, crypto, and code-review fundamentals. |
| ☁️ | [Cloud Security & Compliance](./skills/cloud-security/) | 19 | Audit AWS/Azure/GCP posture, segment networks, and satisfy PCI, GDPR, SOC 2, HIPAA, ISO 27001. |
| 🚨 | [Incident Response](./skills/incident-response/) | 14 | Detect, contain, and learn from incidents — forensics, RCA, comms, postmortems, and DSAR. |
| 🤖 | [AI Security](./skills/ai-security/) | 9 | Test and harden LLM applications: prompt injection, RAG trust, model supply chain, agent gating. |
| ⚙️ | [DevOps & Engineering Practice](./skills/devops/) | 26 | Ship safer and faster: CI optimization, container hardening, observability, architecture, and docs. |
| 🧪 | [Testing](./skills/testing/) | 10 | Build the testing pyramid: unit, integration, load, mutation, fuzz, contract, E2E, security. |
| 🐙 | [GitHub Automation](./skills/github-automation/) | 14 | Automate the GitHub lifecycle: Actions, releases, branch protection, Dependabot, OIDC, secret scanning. |

**Total: 123 skills** · Browse the full catalog: [`catalog/index.md`](./catalog/index.md)

## 🗂️ Repository Structure

```
codex-skills/
├── skills/                  # The 123 production-ready Codex skills
│   ├── cybersecurity/       # 15 skills
│   ├── secure-coding/       # 15 skills
│   ├── cloud-security/      # 19 skills (incl. compliance)
│   ├── incident-response/   # 14 skills
│   ├── ai-security/         #  9 skills
│   ├── devops/              # 26 skills (incl. code-review & docs)
│   ├── testing/             # 10 skills
│   └── github-automation/   # 14 skills
├── catalog/                 # Indexes + community skill directory
│   ├── index.md             # Human-readable catalog
│   ├── index.json           # Machine-readable catalog
│   └── community-top-50.md  # Curated external community skills
├── templates/               # Skill + workflow templates
├── examples/                # Multi-skill workflow examples
├── docs/                    # Architecture, contributing, usage
├── scripts/                 # validate.py, build_catalog.py
└── shared/                  # Shared reference material
```

## 🔗 Example Workflows

| Workflow | Skills chained | Use case |
|----------|---------------|----------|
| [Pre-Merge Security Gate](./examples/pre-merge-security-gate.md) | secret-scanner → dependency-vulnerability-auditor → sast-triage → owasp-top-10-remediator | Catch secrets, CVEs, and OWASP issues before a PR merges. |
| [Incident Response Orchestration](./examples/incident-response-orchestration.md) | severity-classifier → timeline-builder → forensic-snapshot → credential-responder → rca → comms-drafter → postmortem | Walk an on-call from alert to postmortem for a SEV1/SEV2. |
| [AI Feature Launch Checklist](./examples/ai-feature-launch-checklist.md) | prompt-injection-tester → output-filter → rag-trust → tool-gatekeeper → pii-redactor → eval-harness | Harden an LLM feature before public launch. |

## 🧪 Skill File Anatomy

Every skill follows the same structure:

```markdown
---
id: secret-scanner              # kebab-case, matches filename
name: Secret Scanner             # human title
category: cybersecurity          # one of 8
difficulty: Beginner             # Beginner | Intermediate | Advanced
tags: [cwe, secrets, github-actions]
summary: |
  Hunts for hardcoded credentials in source, configs, and history.
last_reviewed: 2026-06-21
---

# Secret Scanner

## Purpose            # what & why (2-4 sentences)
## When to Use        # trigger conditions
## Codex Instructions # 6-12 numbered steps
## Inputs Needed      # 4-8 bullets
## Expected Output    # exact output structure
## Example Prompt     # paste-ready quote block
## Safety Rules       # 4-8 hard guardrails
```

📖 **Author a new skill:** [`docs/skill-authoring-guide.md`](./docs/skill-authoring-guide.md)

## 🤝 Contributing

Contributions welcome. The quality bar is documented in [`docs/contributing.md`](./docs/contributing.md).

```bash
# Validate your work before opening a PR
python scripts/validate.py --skill skills/<category>/<your-skill>.md

# Rebuild the catalog after adding or editing skills
python scripts/build_catalog.py
```

## 📚 Documentation

- [Architecture](./docs/architecture.md) — repository layout, design principles, why 8 categories
- [Usage Guide](./docs/usage.md) — how to load a skill into your agent
- [Skill Authoring Guide](./docs/skill-authoring-guide.md) — how to write a high-quality skill
- [Contributing](./docs/contributing.md) — workflow, quality bar, commit conventions
- [Full Catalog](./catalog/index.md) — every skill with summary and difficulty
- [Community Top 50](./catalog/community-top-50.md) — popular external Codex skills

## 📄 License

MIT — see [LICENSE](./LICENSE). Use these skills freely in personal, commercial, or open-source projects.

## 🤝 Contributors

| | Contributor | Role |
|---|-------------|------|
| ![@rksharma-owg](https://github.com/rksharma-owg.png?size=40) | [@rksharma-owg](https://github.com/rksharma-owg) | Maintainer |
| ![@anthropics](https://github.com/anthropics.png?size=40) | [Claude](https://claude.ai) · by Anthropic | AI Contributor |

Issues and PRs welcome on [GitHub](https://github.com/rksharma-owg/Codex-Skills).
