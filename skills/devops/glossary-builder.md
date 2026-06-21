---
id: glossary-builder
name: Glossary Builder
category: devops
difficulty: Intermediate
tags:
  - argo
  - devops
  - pci
summary: |
  This Codex skill builds a project glossary: domain terms, acronyms, codebase-specific names, and their definitions.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill builds a project glossary: domain terms, acronyms, codebase-specific names, and their definitions. It targets the failure mode of a new engineer who can't follow a conversation because they don't know what 'the widget reconciler' is.

## When to Use

Use when onboarding a new domain, after a rebrand that renamed concepts, when merging two teams with different vocabularies, or when reviewing docs reveals undefined jargon.

## Codex Instructions

1. Scan the codebase, docs, and recent Slack exports (if available) for capitalized terms, acronyms, and unusual nouns.
2. For each term, capture the definition as used in this project — not the generic Wikipedia definition.
3. Cross-reference with the architecture docs and the product spec to verify the definition is accurate.
4. Group terms by category: Domain Concepts, Codebase Names, Acronyms, External Systems.
5. Add a 'See also' link for related terms to help navigation.
6. Mark deprecated terms with a 'Deprecated: use X instead' note.
7. Add a 'First appeared' reference if the term has a known origin (an ADR, a PR).
8. Output the glossary in Markdown, alphabetized, with a table of contents.
9. Recommend integrating the glossary into the project's docs site and IDE spell-check dictionary.

## Inputs Needed

- Repository path and docs folder
- Domain expert availability to verify definitions
- Existing glossary (if any)
- Slack or wiki export for term discovery (optional)

## Expected Output

A Markdown glossary with categories, alphabetized terms, definitions, see-also links, and deprecated markers. Plus a recommendation to integrate with the docs site and IDE spell-check.

## Example Prompt

> Build a glossary for our payments platform. Scan the codebase in src/, docs/, and the recent ADRs. Group by Domain Concepts (Ledger, Settlement, Reconciliation), Codebase Names (widget reconciler, fraud-scorer), Acronyms (PCI, AML, KYC). Verify definitions with the payments domain expert. Output alphabetized Markdown.

## Safety Rules

- Never publish internal-only code names in an external glossary.
- Do not include customer-specific terms in a public glossary.
- Stop and ask the user if a term's definition is ambiguous or contested.
- If a term is a registered trademark, note it.
- Never include proprietary business logic in the definition — keep it conceptual.
- If the glossary reveals an inconsistent use of a term across teams, escalate for alignment before publishing.
