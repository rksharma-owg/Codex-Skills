#!/usr/bin/env python3
"""
Rebuild /catalog/index.md and /catalog/index.json from the skills on disk.

Usage:
  python scripts/build_catalog.py
"""

from pathlib import Path
import json, re, sys
from datetime import date

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"

CATEGORIES = {
    "cybersecurity": {"title": "Cybersecurity", "icon": "🛡️",
        "tagline": "Find, triage, and fix exploitable vulnerabilities across code, containers, and infrastructure.",
        "capabilities": ["vulnerability hunting", "secret detection", "SAST triage", "OWASP Top 10", "runtime defense"]},
    "secure-coding": {"title": "Secure Coding", "icon": "🔒",
        "tagline": "Harden code at the source: validation, encoding, sessions, crypto, and code-review fundamentals.",
        "capabilities": ["input validation", "output encoding", "parameterization", "session hardening", "PR review"]},
    "cloud-security": {"title": "Cloud Security & Compliance", "icon": "☁️",
        "tagline": "Audit AWS/Azure/GCP posture, segment networks, and satisfy PCI, GDPR, SOC 2, HIPAA, ISO 27001.",
        "capabilities": ["IAM audit", "network segmentation", "compliance mapping", "workload identity", "audit logging"]},
    "incident-response": {"title": "Incident Response", "icon": "🚨",
        "tagline": "Detect, contain, and learn from incidents — forensics, RCA, comms, postmortems, and DSAR.",
        "capabilities": ["severity classification", "RCA", "forensics", "postmortem", "data subject requests"]},
    "ai-security": {"title": "AI Security", "icon": "🤖",
        "tagline": "Test and harden LLM applications: prompt injection, RAG trust, model supply chain, agent gating.",
        "capabilities": ["prompt injection", "LLM output filtering", "RAG trust", "model supply chain", "drift monitoring"]},
    "devops": {"title": "DevOps & Engineering Practice", "icon": "⚙️",
        "tagline": "Ship safer and faster: CI optimization, container hardening, observability, architecture, and docs.",
        "capabilities": ["CI optimization", "container hardening", "observability", "architecture rules", "engineering docs"]},
    "testing": {"title": "Testing", "icon": "🧪",
        "tagline": "Build the testing pyramid: unit, integration, load, mutation, fuzz, contract, E2E, security.",
        "capabilities": ["unit", "integration", "load", "fuzz", "contract", "E2E", "security test planning"]},
    "github-automation": {"title": "GitHub Automation", "icon": "🐙",
        "tagline": "Automate the GitHub lifecycle: Actions, releases, branch protection, Dependabot, OIDC, secret scanning.",
        "capabilities": ["Actions workflows", "release automation", "branch protection", "OIDC federation", "secret scanning"]},
}


def parse_frontmatter(content):
    m = re.match(r"^---\n(.*?)\n---\n+(.*)$", content, re.DOTALL)
    if not m:
        return {}, content
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    # Extract tags
    tags = []
    in_tags = False
    for line in m.group(1).split("\n"):
        if line.strip() == "tags:":
            in_tags = True
            continue
        if in_tags:
            if line.startswith("  -"):
                tags.append(line.strip("- ").strip())
            elif line and not line.startswith(" "):
                in_tags = False
    fm["tags"] = tags
    # Extract summary (multiline)
    summary_match = re.search(r"summary:\s*\|\n((?:  .+\n?)+)", m.group(1))
    if summary_match:
        fm["summary"] = summary_match.group(1).replace("  ", "").strip()
    return fm, m.group(2)


def main():
    catalog = {
        "name": "Codex Agent Skills",
        "version": "2.0.0",
        "description": "A curated library of production-ready Codex agent skills for developers, security engineers, AI builders, DevOps teams, and automation workflows.",
        "total_skills": 0,
        "categories": []
    }

    md_lines = ["# Codex Agent Skills — Catalog", "",
                f"**{0} skills** across **{len(CATEGORIES)} categories**. Each skill is a standalone Markdown file with YAML frontmatter, ready to paste into Codex, Claude Code, Cursor, or any LLM-based coding agent.", "",
                "## Browse by Category", ""]

    total = 0
    for cat_id, cat in CATEGORIES.items():
        cat_dir = SKILLS_DIR / cat_id
        cat_skills = []
        if cat_dir.exists():
            for md in sorted(cat_dir.glob("*.md")):
                content = md.read_text()
                fm, _ = parse_frontmatter(content)
                skill = {
                    "id": fm.get("id", md.stem),
                    "name": fm.get("name", md.stem),
                    "difficulty": fm.get("difficulty", "Intermediate"),
                    "tags": fm.get("tags", []),
                    "summary": fm.get("summary", ""),
                    "file": f"skills/{cat_id}/{md.name}",
                }
                cat_skills.append(skill)

        cat_obj = {
            "id": cat_id,
            "title": cat["title"],
            "icon": cat["icon"],
            "tagline": cat["tagline"],
            "capabilities": cat["capabilities"],
            "skill_count": len(cat_skills),
            "skills": cat_skills,
        }
        catalog["categories"].append(cat_obj)
        catalog["total_skills"] += len(cat_skills)
        total += len(cat_skills)
        md_lines.append(f"- [{cat['icon']} {cat['title']} ({len(cat_skills)})](#{cat_id}) — {cat['tagline']}")

    md_lines[2] = f"**{total} skills** across **{len(CATEGORIES)} categories**. Each skill is a standalone Markdown file with YAML frontmatter, ready to paste into Codex, Claude Code, Cursor, or any LLM-based coding agent."

    md_lines += ["", "## Browse by Difficulty", ""]
    for diff in ["Beginner", "Intermediate", "Advanced"]:
        count = sum(1 for cat in catalog["categories"] for s in cat["skills"] if s["difficulty"] == diff)
        md_lines.append(f"- **{diff}** — {count} skills")
    md_lines += ["", "---", ""]

    for cat in catalog["categories"]:
        md_lines += [f"## {cat['icon']} {cat['title']}", "",
                     f"_{cat['tagline']}_", "",
                     f"**{cat['skill_count']} skills** · Capabilities: {', '.join(cat['capabilities'])}", "",
                     "| # | Skill | Difficulty | Summary | File |",
                     "|---|-------|------------|---------|------|"]
        for i, s in enumerate(cat["skills"], 1):
            summary = s["summary"][:120] + ("…" if len(s["summary"]) > 120 else "")
            summary = summary.replace("|", "\\|")
            md_lines.append(f"| {i} | {s['name']} | {s['difficulty']} | {summary} | [`{s['file']}`](../{s['file']}) |")
        md_lines.append("")

    (REPO / "catalog" / "index.json").write_text(json.dumps(catalog, indent=2))
    (REPO / "catalog" / "index.md").write_text("\n".join(md_lines))
    print(f"Catalog rebuilt. Total skills: {total}")


if __name__ == "__main__":
    main()
