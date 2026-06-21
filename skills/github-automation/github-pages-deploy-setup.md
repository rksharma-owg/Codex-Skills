---
id: github-pages-deploy-setup
name: GitHub Pages Deploy Setup
category: github-automation
difficulty: Beginner
tags:
  - github-actions
  - github-automation
summary: |
  This Codex skill sets up a GitHub Actions workflow to build and deploy a static site (docs, blog, landing page) to GitHub Pages, with a custom domain, HTTPS, and cache headers.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill sets up a GitHub Actions workflow to build and deploy a static site (docs, blog, landing page) to GitHub Pages, with a custom domain, HTTPS, and cache headers.

## When to Use

Use when launching a docs site, a project landing page, or a blog on GitHub Pages, or when migrating from another static host.

## Codex Instructions

1. Identify the static site generator: Jekyll (default), Hugo, Docusaurus, Next.js static export, Astro.
2. Author the build workflow: install dependencies, build the site, upload the artifact.
3. Configure the deploy workflow: deploy-pages action, environment: github-pages, only on main.
4. Configure the custom domain: add a CNAME file in the site's static dir, configure DNS at the registrar.
5. Verify HTTPS: enable 'Enforce HTTPS' in the repo's Pages settings; the cert is auto-provisioned.
6. Configure cache headers: via a _headers file (Cloudflare-style) or .nojekyll for raw serving.
7. Set up a staging deploy: a separate workflow on a staging branch, deployed to a preview environment.
8. Verify the deploy by checking the URL and the HTTP headers.
9. Output the workflow YAML, the CNAME file, and the DNS configuration instructions.

## Inputs Needed

- Static site generator
- Repository (must have Pages enabled)
- Custom domain (or use the default github.io)
- Staging branch (optional)
- Existing DNS provider

## Expected Output

A GitHub Actions workflow YAML for build and deploy, a CNAME file for the custom domain, DNS configuration instructions, and a verification checklist.

## Example Prompt

> Set up a Docusaurus docs site on GitHub Pages with a custom domain docs.example.com. Workflow: build on PR (preview), deploy on main. Add CNAME, enforce HTTPS, configure cache headers via _headers. Staging deploy from a staging branch. Verify with curl -I.

## Safety Rules

- Never deploy the site without building it first — broken builds should fail the deploy.
- Do not expose internal docs on a public Pages site — separate the public and internal sites.
- Stop and ask the user if the custom domain's DNS is managed by a different team.
- If the site handles regulated content, verify the disclaimer is present.
- Never log deploy tokens at any level.
- If the site is for a commercial product, verify the license allows public Pages hosting.
