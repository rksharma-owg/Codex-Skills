# Usage

## What is a Codex Agent Skill?

A Codex agent skill is a reusable prompt artifact that turns a vague request — "audit this repo for secret leaks" — into a structured, predictable, safe execution. A skill pre-encodes the scope, the steps, the inputs, the output format, and the safety guardrails. When you point Codex at a skill file (or paste its contents into the system prompt), Codex follows the documented workflow instead of improvising.

This library is framework-agnostic: the skills are Markdown, so they work with OpenAI Codex, Claude Code, Cursor, Aider, Continue, or any agent that consumes Markdown.

## Quick Start

### Option 1: Browse and copy

1. Browse [`/catalog/index.md`](../catalog/index.md) to find a skill.
2. Open the skill file, e.g. [`skills/cybersecurity/secret-scanner.md`](../skills/cybersecurity/secret-scanner.md).
3. Copy the entire file contents.
4. Paste into your agent's system prompt, custom instruction, or skill-loading mechanism.
5. Use the `## Example Prompt` as your starting user message, customizing the path/scope to your situation.

### Option 2: Programmatic (for agents that support file-based skills)

```bash
# Clone the repo
git clone https://github.com/rksharma-owg/Codex-Skills.git
cd Codex-Skills

# Validate the skill you want to use
python scripts/validate.py --skill skills/cybersecurity/secret-scanner.md

# Point your agent at the skill file
# (agent-specific — see your agent's docs for loading Markdown skills)
```

### Option 3: Use a workflow

Browse [`/examples/`](../examples/) for multi-skill workflows. Each workflow chains several skills to accomplish a larger goal (pre-merge security gate, incident response, AI feature launch).

## Combining Skills

Most real-world work chains multiple skills. See [`/examples/`](../examples/) for ready-made workflows. To build your own:

1. Pick the skills you need from the catalog.
2. Use [`/templates/workflow-template.md`](../templates/workflow-template.md) as a starting point.
3. Document the inputs, steps, and expected output.
4. Save your workflow under `/examples/` and open a PR.

## Finding Skills

- **By category:** browse [`/catalog/index.md`](../catalog/index.md) for category tables with summaries.
- **By difficulty:** filter by `Beginner`, `Intermediate`, `Advanced` in the catalog.
- **By tag:** search frontmatter `tags` in any skill file, or query `catalog/index.json`.
- **By keyword:** `grep -r "<keyword>" skills/` from the repo root.

## Customizing a Skill

Skills are starting points, not gospel. Common customizations:

- **Tighten the scope.** If a skill scans too broadly, edit `## Codex Instructions` to narrow it.
- **Add project-specific tools.** If your team uses a custom linter, add it to `## Inputs Needed` and `## Codex Instructions`.
- **Soften safety rules.** If a safety rule is too strict for your context, edit `## Safety Rules` — but document why.

## Validating Your Setup

```bash
# Validate the entire library
python scripts/validate.py

# Validate a single skill
python scripts/validate.py --skill skills/cybersecurity/secret-scanner.md

# Rebuild the catalog after adding or editing skills
python scripts/build_catalog.py
```

The validator checks:

- Every `.md` file under `/skills/` has valid YAML frontmatter with required fields.
- Every skill file is in one of the 8 categories.
- Every internal link (to other skills, to `/shared/`, to `/templates/`) resolves.
- Every skill has all 8 required sections (Purpose, When to Use, Codex Instructions, Inputs Needed, Expected Output, Example Prompt, Safety Rules).
