# Codex Skills

A professionally organized library of high-signal development skills for daily engineering work.

This repository combines two distinct layers:

- An original curated catalog of top development skills, rewritten for clarity and consistent organization.
- A dedicated application security skill package with source notes and supporting files.

## Highlights

- 50 curated development skills ranked using current adoption data gathered on June 14, 2026.
- One folder per skill for consistent browsing, linking, and future automation.
- Category landing pages for faster navigation by engineering domain.
- Machine-readable metadata for every curated skill entry.
- A dedicated application security package kept alongside the main skills library.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `catalog/top-50.md` | Human-readable ranked overview of the curated top 50 skills. |
| `catalog/top-50.json` | Structured version of the ranked catalog for tooling and automation. |
| `skills/` | Main curated library, organized by category and then by individual skill folder. |
| `skills/<category>/<skill>/README.md` | Professional summary page for a single curated skill. |
| `skills/<category>/<skill>/skill.json` | Structured metadata for a single curated skill. |
| `skills/application-security/` | Application security skill package with source notes and reference files. |

## Skill Categories

| Category | Focus |
| --- | --- |
| [Frontend and UI Engineering](./skills/frontend-ui/README.md) | Patterns and guidance for product-facing engineering, interface systems, styling, and modern React-based implementation. |
| [Backend and Platform Development](./skills/backend-platform/README.md) | Practical references for APIs, backend structure, platform foundations, developer tooling, and service-oriented work. |
| [Testing and QA](./skills/testing-qa/README.md) | Coverage for automated testing, browser workflows, end-to-end quality, and test architecture decisions. |
| [Data and Persistence](./skills/data-persistence/README.md) | Database, schema, migration, query, and GraphQL-oriented skills for teams working with real application data. |
| [Security and Authentication](./skills/security-auth/README.md) | Focused guidance for authentication, authorization, policy review, and secure-by-default application design. |
| [Ops, Debugging, Performance, and Reliability](./skills/ops-debug-performance/README.md) | Operational support for debugging, containers, reliability, observability, and performance improvement work. |

## Editorial Standards

- Prioritized install count as the most consistent public signal of real-world adoption.
- Favored official publishers and recognizable engineering sources where possible.
- Excluded low-signal and obviously off-topic entries from the development-focused core list.
- Rewrote catalog descriptions to keep this repository original, neutral, and easier to review.

## Important Notes

- Curated entries in `skills/` are organizational summaries created for this repository.
- The application security skill package lives directly in `skills/` with its source notes and reference files.
- Original skills should always be installed and maintained from their source repositories.
