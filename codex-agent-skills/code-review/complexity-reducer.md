# Complexity Reducer

## Purpose

This Codex skill reduces cyclomatic and cognitive complexity by extracting helper functions, replacing nested conditionals with guard clauses, simplifying boolean expressions via De Morgan's laws, replacing switch statements with lookup tables, and eliminating dead branches. It produces a diff that preserves behavior, verified by the existing test suite.

## When to Use

Use when a function exceeds the project's complexity threshold (commonly 10 for cyclomatic, 15 for cognitive), before adding new logic to an already-complex function, or when onboarding engineers report a function as 'hard to read'.

## Codex Instructions

1. Identify the target function and compute its current cyclomatic and cognitive complexity.
2. Map each branch to its business meaning; if a branch is unreachable or duplicated, flag for removal.
3. Apply guard-clause refactors: invert early-return conditions to flatten the happy path.
4. Extract complex conditions into named boolean helper functions that describe the predicate in plain English.
5. Replace switch statements over closed enumerations with a lookup table (dict, Map) of handlers.
6. Simplify boolean expressions using De Morgan's laws and by extracting repeated sub-expressions.
7. Replace nested loops with early-exit helper functions when the nesting exceeds 3 levels.
8. For each refactor, run the existing test suite and confirm green; if no tests exist, write a characterization test first.
9. Produce a diff and a complexity delta report showing before/after metrics.
10. Flag any function where complexity is inherent to the domain (e.g., a parser) and propose splitting the function rather than micro-refactoring.

## Inputs Needed

- Target function or file path
- Language and complexity metric in use (cyclomatic, cognitive, or both)
- Project complexity thresholds
- Test suite path and how to run it
- Existing characterization tests for the function, if any

## Expected Output

A Markdown report titled 'Complexity Reduction Report' with: (1) Before/After metrics table — Function | Cyclomatic Before | Cyclomatic After | Cognitive Before | Cognitive After; (2) Patch Diff with extracted helpers; (3) Test Run Output confirming green; (4) Follow-up Recommendations for functions that still exceed thresholds.

## Example Prompt

> Reduce complexity of processRefund() in src/billing/refunds.ts. Current cyclomatic complexity is 23, our threshold is 10. Preserve behavior, run npm test after each refactor, and produce a diff.

## Safety Rules

- Never commit refactors without running the full test suite.
- If no tests exist, write characterization tests before refactoring — never refactor untested code blind.
- Do not change public API signatures during complexity reduction; refactor internal structure only.
- Stop and ask the user if a refactor requires changing the test suite architecture.
- Never remove a branch that appears dead without confirming with the user — it may be reachable via reflection or config.
- Do not introduce abstractions (interfaces, generics) purely to lower a metric — only if they improve clarity.
