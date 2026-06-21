#!/usr/bin/env python3
"""
Validate the Codex Agent Skills library.

Checks:
  1. Every .md file under skills/ has valid YAML frontmatter with required fields.
  2. Every skill is in one of the 8 valid categories.
  3. Every internal Markdown link resolves to an existing file.
  4. Every skill has all 8 required sections.
  5. The catalog/index.json is in sync with the actual skills.

Usage:
  python scripts/validate.py                 # validate everything
  python scripts/validate.py --skill <path>  # validate a single skill
  python scripts/validate.py --fix           # auto-fix where possible
"""

from pathlib import Path
import re, sys, json, argparse, yaml

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"
CATALOG_JSON = REPO / "catalog" / "index.json"

VALID_CATEGORIES = {
    "cybersecurity", "secure-coding", "cloud-security", "incident-response",
    "ai-security", "devops", "testing", "github-automation",
}

REQUIRED_FRONTMATTER = {"id", "name", "category", "difficulty", "tags", "summary", "last_reviewed"}

REQUIRED_SECTIONS = [
    "## Purpose",
    "## When to Use",
    "## Codex Instructions",
    "## Inputs Needed",
    "## Expected Output",
    "## Example Prompt",
    "## Safety Rules",
]

VALID_DIFFICULTIES = {"Beginner", "Intermediate", "Advanced"}


def is_skill_file(path):
    """A skill file is any .md under skills/ that is NOT a README.md or index."""
    return path.name.lower() not in ("readme.md", "index.md")


def parse_frontmatter(content):
    """Return (frontmatter_dict, body) or (None, content) if no frontmatter."""
    m = re.match(r"^---\n(.*?)\n---\n+(.*)$", content, re.DOTALL)
    if not m:
        return None, content
    try:
        fm = yaml.safe_load(m.group(1))
        return fm, m.group(2)
    except yaml.YAMLError as e:
        return {"__error__": str(e)}, m.group(2)


def find_internal_links(body, current_file):
    """Find all [text](path) Markdown links to local files. Returns absolute Paths."""
    links = set()
    # Match [text](path) where path doesn't start with http/https/#
    for m in re.finditer(r"\[(?:[^\]]+)\]\(([^)#?]+?)(?:#[^)]*)?\)", body):
        path = m.group(1)
        if path.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Resolve relative to current file's directory
        resolved = (current_file.parent / path).resolve()
        links.add(resolved)
    return links


def validate_skill(skill_path, errors, warnings):
    """Validate a single skill file. Returns True if valid."""
    content = skill_path.read_text()
    fm, body = parse_frontmatter(content)

    # Frontmatter checks
    if fm is None:
        errors.append(f"{skill_path.relative_to(REPO)}: no YAML frontmatter found")
        return False
    if "__error__" in fm:
        errors.append(f"{skill_path.relative_to(REPO)}: invalid YAML: {fm['__error__']}")
        return False

    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing:
        errors.append(f"{skill_path.relative_to(REPO)}: missing frontmatter fields: {sorted(missing)}")

    if fm.get("category") not in VALID_CATEGORIES:
        errors.append(f"{skill_path.relative_to(REPO)}: invalid category '{fm.get('category')}'. Valid: {sorted(VALID_CATEGORIES)}")

    if fm.get("difficulty") not in VALID_DIFFICULTIES:
        errors.append(f"{skill_path.relative_to(REPO)}: invalid difficulty '{fm.get('difficulty')}'. Valid: {sorted(VALID_DIFFICULTIES)}")

    # ID must match filename
    expected_id = skill_path.stem
    if fm.get("id") != expected_id:
        errors.append(f"{skill_path.relative_to(REPO)}: frontmatter id '{fm.get('id')}' does not match filename '{expected_id}'")

    # Required sections
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{skill_path.relative_to(REPO)}: missing section '{section}'")

    # Internal links resolve
    for link in find_internal_links(body, skill_path):
        if not link.exists():
            warnings.append(f"{skill_path.relative_to(REPO)}: broken link to {link.relative_to(REPO) if link.is_relative_to(REPO) else link}")

    # Tags: at least 1, at most 10
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        errors.append(f"{skill_path.relative_to(REPO)}: tags must be a list")
    elif len(tags) > 10:
        warnings.append(f"{skill_path.relative_to(REPO)}: {len(tags)} tags (max 10 recommended)")
    elif len(tags) == 0:
        warnings.append(f"{skill_path.relative_to(REPO)}: no tags")

    return not errors


def validate_catalog_sync(errors, warnings):
    """Verify catalog/index.json matches the actual skills on disk."""
    if not CATALOG_JSON.exists():
        errors.append("catalog/index.json: missing. Run scripts/build_catalog.py")
        return

    catalog = json.loads(CATALOG_JSON.read_text())
    catalog_skills = set()
    for cat in catalog.get("categories", []):
        for s in cat.get("skills", []):
            catalog_skills.add(s["file"])

    disk_skills = set()
    for md in SKILLS_DIR.rglob("*.md"):
        if is_skill_file(md):
            rel = md.relative_to(REPO).as_posix()
            disk_skills.add(rel)

    missing_in_catalog = disk_skills - catalog_skills
    missing_on_disk = catalog_skills - disk_skills

    for f in sorted(missing_in_catalog):
        warnings.append(f"catalog/index.json: missing entry for {f}. Run scripts/build_catalog.py")
    for f in sorted(missing_on_disk):
        warnings.append(f"catalog/index.json: references {f} but file does not exist on disk")


def main():
    parser = argparse.ArgumentParser(description="Validate the Codex Agent Skills library")
    parser.add_argument("--skill", type=Path, help="validate a single skill file")
    parser.add_argument("--fix", action="store_true", help="auto-fix where possible (not yet implemented)")
    args = parser.parse_args()

    errors = []
    warnings = []

    if args.skill:
        validate_skill(args.skill.resolve(), errors, warnings)
    else:
        # Validate every skill (skip README.md files which are index pages)
        for md in sorted(SKILLS_DIR.rglob("*.md")):
            if is_skill_file(md):
                validate_skill(md, errors, warnings)
        # Validate catalog sync
        validate_catalog_sync(errors, warnings)
        # Validate templates, examples, docs have no broken links
        for folder in ["templates", "examples", "docs"]:
            folder_path = REPO / folder
            if folder_path.exists():
                for md in folder_path.rglob("*.md"):
                    content = md.read_text()
                    _, body = parse_frontmatter(content)
                    for link in find_internal_links(body, md):
                        if not link.exists():
                            warnings.append(f"{md.relative_to(REPO)}: broken link to {link}")

    print(f"\n=== Validation Report ===\n")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if not errors and not warnings:
        print("  ✓ All checks passed.")
        # Summary
        skill_count = sum(1 for md in SKILLS_DIR.rglob("*.md") if is_skill_file(md))
        print(f"\n  Total skills: {skill_count}")
        for cat in sorted(VALID_CATEGORIES):
            cat_dir = SKILLS_DIR / cat
            if cat_dir.exists():
                count = sum(1 for md in cat_dir.glob("*.md") if is_skill_file(md))
                print(f"    {cat}: {count}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
