# Dead Code Eliminator

## Purpose

This Codex skill identifies and removes unreachable code: unused private functions, commented-out blocks, unused imports, unused CSS classes, unreachable branches after early returns, and obsolete feature flags. It uses static reachability analysis and cross-references the test suite to avoid removing code invoked only by tests or reflection.

## When to Use

Use during tech-debt sprints, before open-sourcing a repo, when preparing for an acquisition due-diligence review, or after a major feature deletion that likely left orphaned helpers.

## Codex Instructions

1. Build a usage graph: for each symbol (function, class, variable, import), record its definition and all references.
2. Identify symbols with zero references outside their definition — candidates for removal.
3. Cross-reference with the test suite: a symbol used only in tests is not dead but is a candidate for relocation.
4. Identify commented-out code blocks older than 90 days and propose removal with a git-history reference.
5. Identify unreachable branches: code after return/throw, impossible conditions (if false then), and feature flags that have been permanently rolled out.
6. Identify unused CSS classes using a static class extractor over templates and JSX.
7. Identify unused exports in a library's public API by scanning consumers, if available.
8. For each candidate, verify it is not invoked via reflection, dependency injection containers, or string-based config.
9. Produce a removal plan grouped by confidence: High (zero references, no reflection), Medium (used only in tests), Low (requires human confirmation).
10. Output a diff for High-confidence removals and a checklist for Medium/Low items.

## Inputs Needed

- Repository path
- Language and module system (ESM, CJS, Python imports, Go modules)
- Test suite location
- Reflection or DI framework in use (Spring, Angular, NestJS) — affects false positives
- CSS extractor or framework (Tailwind, Bootstrap, custom)

## Expected Output

A Markdown report titled 'Dead Code Removal Report' with: (1) Findings grouped by confidence; (2) Patch Diff for High-confidence removals; (3) Checklist for Medium/Low items requiring human confirmation; (4) Test Run Output confirming no regressions.

## Example Prompt

> Find dead code in this TypeScript React project. We use NestJS for backend and Tailwind for CSS — be careful with dependency-injection decorators and Tailwind purging. Group findings by confidence and produce a diff for high-confidence removals.

## Safety Rules

- Never remove code that is invoked via reflection, decorators, or DI containers without confirming with the user.
- Do not remove exports from a published library's public API without a major version bump.
- Stop and ask the user if a symbol's reachability is ambiguous (e.g., plugin system, runtime config).
- Never remove commented-out code that includes a 'TODO' or 'FIXME' — surface it as a finding instead.
- Run the full test suite after each removal batch to isolate regressions.
- Do not remove CSS classes referenced in CMS-managed HTML or server-rendered strings outside the repo.
