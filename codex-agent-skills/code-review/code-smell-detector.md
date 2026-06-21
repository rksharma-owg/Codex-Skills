# Code Smell Detector

## Purpose

This Codex skill identifies code smells — long methods, deep nesting, feature envy, primitive obsession, god classes, shotgun surgery, divergent change, data clumps, and inappropriate intimacy — and ranks them by refactor ROI. It complements linters by finding design-level issues that syntax rules cannot detect.

## When to Use

Use during a technical-debt sprint, before refactoring a legacy module, when an architect asks for a 'code health report', or as part of a quarterly engineering review.

## Codex Instructions

1. For each module or class, compute simple metrics: LOC, cyclomatic complexity, number of public methods, number of fields, fan-in and fan-out.
2. Detect long methods (> 50 LOC or > 5 cyclomatic complexity) and flag the top 10 by complexity.
3. Detect deep nesting (> 4 levels of if/for/while) and propose early-return refactors.
4. Detect feature envy by identifying methods that call more methods on another class than on their own.
5. Detect god classes (classes with > 200 LOC, > 20 methods, or low cohesion) and propose a split along the top responsibility axis.
6. Detect data clumps: groups of 3+ parameters that always appear together; propose extracting a value object.
7. Detect shotgun surgery: a single conceptual change requiring edits to > 5 files; propose consolidating the responsibility.
8. Rank findings by ROI: high-impact and low-effort refactors first.
9. For each finding, propose a concrete refactor (extract method, move method, extract class, introduce parameter object) with a code sketch.
10. Output a debt register and a suggested refactor roadmap for the next sprint.

## Inputs Needed

- Repository path or specific module
- Language (some smells are language-specific)
- Existing metrics tool (radon, lizard, complexity-report) or 'manual'
- Scope: single class, single module, or entire repo
- Refactor budget in person-days, if known

## Expected Output

A Markdown report titled 'Code Smell Report' with: (1) Module Summary table — Module | LOC | Complexity | Top Smell; (2) Findings table — Smell | Location | Severity | Refactor | Effort (S/M/L) | ROI; (3) Refactor Roadmap for the next 1-2 sprints.

## Example Prompt

> Analyze src/billing/ in this Python project for code smells. Focus on god classes and long methods. Produce a debt register with ROI ranking and a 2-sprint refactor roadmap.

## Safety Rules

- Never auto-apply refactors — produce a roadmap for human review.
- Do not propose refactors that change public API signatures without flagging the breaking change.
- Stop and ask the user if a refactor requires changing the test suite architecture.
- If a smell is intentional (e.g., a god class that is the framework's entry point), note it rather than proposing a split.
- Do not rank by ROI if effort estimates are unavailable — flag them as 'unknown'.
- Never expose proprietary business logic in the report — keep descriptions generic.
