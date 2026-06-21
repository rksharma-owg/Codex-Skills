---
id: xss-finder
name: XSS Finder
category: cybersecurity
difficulty: Intermediate
tags:
  - csp
  - cwe
  - cybersecurity
  - owasp
  - semgrep
summary: |
  This Codex skill detects Cross-Site Scripting (XSS) vulnerabilities — reflected, stored, DOM-based, and mutation-based — across web front-ends and server-rendered templates.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill detects Cross-Site Scripting (XSS) vulnerabilities — reflected, stored, DOM-based, and mutation-based — across web front-ends and server-rendered templates. It exists because XSS remains the most common web vulnerability reported by Bugcrowd and HackerOne year after year, and modern frameworks ship "safe by default" templating that developers routinely bypass with `dangerouslySetInnerHTML`, `[innerHTML]`, `v-html`, or unescaped JSP/Jinja output. The skill focuses on source-to-sink taint flow with framework-aware sanitization rules.

## When to Use
Run this skill on any PR touching front-end rendering, template files, server-side response builders, or DOM manipulation code. Also use it during a framework migration (e.g., jQuery → React), when adopting a new rich-text editor or markdown renderer, after a Bug Bounty report flags an XSS, or before shipping a feature that displays user-generated content (comments, profiles, reviews, chat).

## Codex Instructions
1. Identify rendering surfaces per framework: React (`dangerouslySetInnerHTML`), Vue (`v-html`), Angular (`[innerHTML]`, `bypassSecurityTrustHtml`), Svelte (`{@html}`), Jinja2 (`|safe`, `{% autoescape false %}`), Django templates (`mark_safe`, `{% autoescape off %}`), Twig (`|raw`), ERB (`<%==`, `raw`, `html_safe`), JSP (`<%= ... %>` with unescaped), Thymeleaf (`th:utext`), Go `html/template` (`template.HTML`), PHP `echo` without `htmlspecialchars`.
2. Treat as **sources**: URL parameters, hash fragments, `postMessage` data, `localStorage`/`sessionStorage` reads, GraphQL response fields marked as user-content, API responses from untrusted domains, and any field rendered from a database column that accepts user input (stored XSS).
3. Treat as **sinks**: `innerHTML`, `outerHTML`, `document.write`, `eval`, `setTimeout(string)`, `setInterval(string)`, `Function(string)`, jQuery `.html()`, `$()` with HTML strings, `insertAdjacentHTML`, and any framework's unescaped-output directive listed in step 1.
4. Treat as **sanitizers**: DOMPurify (`DOMPurify.sanitize`), `sanitize-html` (Node), `bleach` (Python), OWASP Java HTML Sanitizer, Microsoft AntiXSS / `System.Web.Security.AntiXss.AntiXssEncoder`, Angular's `DomSanitizer` with `sanitize()`, `encodeURIComponent` for URL-context output.
5. Trace taint from source to sink; if no sanitizer is in the path, classify as a confirmed XSS. For DOM XSS, inspect the DOM API flow even when no server round-trip occurs.
6. Distinguish variants: reflected (URL param to HTML), stored (DB to HTML), DOM-based (source to sink entirely in client JS), mutation-based (sanitizer bypass via mXSS in `innerHTML` round-trips with `<svg>`, `<math>`, or `<noscript>` contexts), and self-XSS (lower severity unless chainable to CSRF).
7. Re-baseline severity: stored XSS on a shared page with other users' sessions is Critical; reflected XSS on an authenticated page is High; DOM XSS on a static marketing page is Medium; self-XSS is Low.
8. Map each finding to CWE-79 (Improper Neutralization of Input During Web Page Generation).
9. Propose a patch per finding: prefer framework-safe defaults (let React/Vue/Angular escape automatically); for cases where HTML must be rendered, require DOMPurify with an explicit allowlist. For URL-context output, require `encodeURIComponent`.
10. Recommend a CSP per page that would mitigate the finding if the patch is delayed: `script-src 'self' 'nonce-<random>'` with no `unsafe-inline`.
11. Emit `XSS_FINDINGS.md` plus SARIF for upload to GitHub code scanning.

## Inputs Needed
- Repository path (front-end and/or server-rendered code)
- Framework(s) in use (React, Vue, Angular, Svelte, Django, Rails, Spring MVC, etc.)
- Template engine(s) (Jinja2, Twig, ERB, Handlebars, Thymeleaf, Go html/template)
- Whether user-generated content is stored and rendered (comments, profiles, reviews)
- Existing sanitization library in use (DOMPurify, sanitize-html, bleach, etc.)
- CSP header policy currently in place (or its absence)
- Authentication context (anonymous vs. authenticated pages — affects severity)
- Prior bug bounty / pen test findings to cross-correlate

## Expected Output
A markdown report `XSS_FINDINGS.md` with sections: Executive Summary (frameworks, total findings by severity, top 3 risks), Taint Flows (one subsection per finding: source → transformations → sink, with code snippet), Findings Table (ID, Severity, CWE, Sink File:Line, Variant, Source, Sanitizer Present?, Patch, Recommended CSP), and Regression Tests (suggested unit tests + Semgrep rules). Severity scale: Critical (stored XSS on authenticated page) / High (reflected XSS authenticated) / Medium (reflected XSS anonymous, DOM XSS) / Low (self-XSS). Emit `xss.sarif`.

## Example Prompt
> Find XSS in `/home/z/my-project/community-app` (React 18 + Next.js 14, plus a Django REST backend). We allow users to write markdown comments rendered with `react-markdown` and we just had a Bugcrowd report flag `dangerouslySetInnerHTML` in three components. Trace taint from URL params and API responses to all sinks, propose DOMPurify-based patches, suggest a CSP, and write `XSS_FINDINGS.md` with SARIF.

## Safety Rules
- Never execute the payload in a real browser against a live site; static analysis only.
- Do not recommend `escape()` (deprecated) or hand-rolled regex escaping — always use a vetted library.
- For `innerHTML` round-trips with `<svg>` or `<math>` contexts, flag as mXSS-prone even when a sanitizer is present; recommend re-sanitizing after parse.
- Do not recommend disabling auto-escaping globally in any template engine; recommend per-output overrides only.
- Never recommend `unsafe-inline` in a CSP as a fix — recommend nonces or hashes.
- If the source is a markdown renderer's HTML passthrough, treat as Critical unless the renderer is configured with `html: false` or DOMPurify is in the pipeline.
- Do not auto-apply patches; propose them in the report.
- For stored XSS findings, do not include real user-generated content in the snippet — substitute `[USER CONTENT]`.
