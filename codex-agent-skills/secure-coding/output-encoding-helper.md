# Output Encoding Helper

## Purpose

This Codex skill ensures that every value rendered into HTML, JavaScript, CSS, URL, or attribute context is encoded with the correct context-specific encoder, eliminating reflected and stored XSS. It distinguishes between HTML body, HTML attribute, JavaScript string, CSS, and URL contexts, and rewrites template code to use the appropriate escaping function or framework-native safe-render API.

## When to Use

Run this skill when introducing new templates, after a DAST tool flags XSS, when migrating from string concatenation to a template engine, or before releasing a feature that reflects user input into the DOM. It is especially relevant for server-rendered apps, email templates, and PDF generation pipelines.

## Codex Instructions

1. Identify all output sinks: template files, JSX/TSX return values, server-rendered strings, response builders, PDF/HTML email generators.
2. Classify each sink by output context: HTML body, HTML attribute, JavaScript string literal, CSS property, URL query/path, or SVG.
3. For each variable interpolated into a sink, determine if the framework auto-escapes (Jinja2 autoescape, React JSX, Twig autoescape) or requires manual encoding.
4. Where the framework does not auto-escape, inject the correct encoder: htmlEscape for body, attributeEscape for attributes, encodeURIComponent for URL components, JSON.stringify with </script> splitting for inline JS.
5. Replace any explicit `|safe`, `{!! !!}`, `dangerouslySetInnerHTML`, or `<%- %>` bypass with a documented justification and a sanitization step using DOMPurify or equivalent.
6. For URL contexts, enforce protocol allowlist (http, https, mailto) before interpolation to block javascript: and data: URIs.
7. For JavaScript string contexts inserted inside <script> blocks, escape both quotes and the closing </script> sequence to prevent context breakout.
8. Generate a context-aware test for each sink using the OWASP XSS Filter Evasion cheat sheet payloads.
9. Output a diff and a sink map; flag any remaining bypasses that cannot be auto-fixed and require a human decision.
10. Document the chosen encoder library and version so reviewers can verify it is current.

## Inputs Needed

- Template directory or component tree to scan
- Framework and template engine (Jinja2, EJS, Handlebars, JSX, Blade, Twig)
- Existing sanitization libraries available in the project
- List of routes/components known to reflect user input
- Whether CSP is enforced (affects bypass risk)

## Expected Output

A Markdown report titled 'Output Encoding Audit' with: (1) Sink Inventory table mapping each variable to its output context; (2) Findings table with Sink | Context | Current Encoding | Risk | Recommended Encoder | CWE-79; (3) Patch Diff with template changes; (4) Test Plan listing XSS payloads to verify each fix.

## Example Prompt

> Audit templates/ and src/components/ for output encoding gaps. We use Jinja2 with autoescape on, but I want every |safe filter reviewed and every URL interpolation checked for javascript: payloads.

## Safety Rules

- Never replace a sanitization call with a weaker encoder — only upgrade.
- Do not introduce dangerouslySetInnerHTML or equivalent bypasses to 'fix' rendering bugs.
- If a sink legitimately needs raw HTML, require an explicit sanitization step with DOMPurify and a code comment justifying the bypass.
- Do not strip Content-Security-Policy headers or nonce logic from templates.
- Stop and ask the user if a context is ambiguous (e.g., user data interpolated into an SVG <script> block).
- Never log encoded output samples that contain the raw user payload — redact before logging.
