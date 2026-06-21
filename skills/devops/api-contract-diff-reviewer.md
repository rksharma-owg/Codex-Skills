---
id: api-contract-diff-reviewer
name: API Contract Diff Reviewer
category: devops
difficulty: Intermediate
tags:
  - devops
summary: |
  This Codex skill diffs an OpenAPI, Protobuf, or GraphQL schema against the previous version and classifies each change as breaking, additive, or non-impactful.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill diffs an OpenAPI, Protobuf, or GraphQL schema against the previous version and classifies each change as breaking, additive, or non-impactful. It produces a changelog ready for API consumers and a client-SDK impact analysis. It targets the failure mode of an accidental breaking change shipped in a minor version.

## When to Use

Use on every PR that modifies an API contract, before publishing a new SDK version, when forking an internal API for a partner, or as a CI gate on the contracts directory.

## Codex Instructions

1. Parse the previous and current API contract files (OpenAPI YAML/JSON, .proto, .graphql).
2. Compute the diff: added/removed/modified endpoints, fields, parameters, response codes, enum values.
3. Classify each change: Breaking (removed field, narrowed type, new required param), Additive (optional new field, new endpoint), Non-impactful (doc change, formatting).
4. For breaking changes, identify the impact on each known client SDK and propose a deprecation path (e.g., keep the old field as deprecated for one release).
5. Verify version bump in the contract matches the change classification: breaking → major, additive → minor, non-impactful → patch.
6. Check that new required fields have a sensible default for existing clients, or that the field is optional.
7. For enum changes, flag removed values as breaking for clients that switch on the enum.
8. For Protobuf, verify field numbers of existing fields are unchanged; new fields use new field numbers and are optional.
9. Output a contract changelog grouped by Breaking / Additive / Non-impactful, plus an SDK impact table.
10. Recommend a release plan: deprecation notices, version bump, client migration guide.

## Inputs Needed

- Previous and current contract file paths
- Contract format (OpenAPI 3.0, OpenAPI 3.1, Protobuf, GraphQL SDL)
- Client SDK list (web, iOS, Android, partner SDKs)
- Versioning scheme in use (semver, calendrical, custom)
- Deprecation policy (how many releases before removal)

## Expected Output

A Markdown report titled 'API Contract Diff Review' with: (1) Changes table — Change | Type (Breaking/Additive/Non-impactful) | Endpoint/Field | Client Impact; (2) Version Bump Recommendation; (3) Deprecation Plan for breaking changes; (4) Client Migration Guide draft.

## Example Prompt

> Diff openapi.yaml against the previous version on the main branch. We have web, iOS, and Android SDKs — flag every breaking change and propose a deprecation path so we can ship this as a minor version. Generate a client migration guide draft.

## Safety Rules

- Never recommend shipping a breaking change in a minor version — flag the version bump mismatch.
- Do not silently reclassify a breaking change as additive to satisfy a release deadline.
- Stop and ask the user if a client SDK's tolerance for breaking changes is unknown.
- If the contract uses a custom versioning scheme, confirm the mapping before recommending a bump.
- Never expose internal-only endpoints in the public changelog — filter them out.
- If a deprecation timeline is not documented in the project, propose one rather than guessing.
