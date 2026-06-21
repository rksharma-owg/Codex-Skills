---
id: fuzz-test-harness-builder
name: Fuzz Test Harness Builder
category: testing
difficulty: Advanced
tags:
  - afl
  - argo
  - github-actions
  - libfuzzer
  - testing
summary: |
  This Codex skill builds a fuzz test harness for a parser, deserializer, or protocol handler: defines the input corpus, the harness function that feeds bytes to the target, the sanitizer integration (ASan, UBSan), and the CI integration.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill builds a fuzz test harness for a parser, deserializer, or protocol handler: defines the input corpus, the harness function that feeds bytes to the target, the sanitizer integration (ASan, UBSan), and the CI integration. It targets the failure mode of a parser that crashes on malformed input.

## When to Use

Use when launching a parser, codec, or protocol implementation; after a CVE in a parser; or as part of a security hardening sprint.

## Codex Instructions

1. Identify the target function: parser entry point, deserialization function, protocol handler.
2. Choose the fuzzing engine: libFuzzer (C/C++), AFL++, cargo-fuzz (Rust), go-fuzz (Go), Atheris (Python), Jazzer (JVM).
3. Build the harness: a function that takes a byte array, converts it to the target's input format, and calls the target.
4. Compile the target with sanitizers: -fsanitize=address,undefined for C/C++; the engine handles this for Rust/Go/Python/JVM.
5. Assemble a seed corpus from existing test inputs, sample files, and the spec's examples.
6. Run the fuzzer for a bounded duration (e.g., 1 hour of CPU time per PR, 24 hours in nightly).
7. Triage crashes: deduplicate by stack trace, minimize the input, file issues for each unique crash.
8. Add regression tests for each fixed crash to prevent regressions.
9. Integrate into CI: run a 1-minute fuzz on every PR (smoke), a 1-hour fuzz nightly.
10. Output the harness, the seed corpus, the CI integration, and the triage process.

## Inputs Needed

- Target function and language
- Existing test inputs to seed the corpus
- Fuzzing engine availability
- CI time budget for fuzzing
- Issue tracker for filing crashes

## Expected Output

A fuzz harness file, a seed corpus directory, a CI integration snippet, and a triage runbook. Plus any crashes found during an initial smoke fuzz.

## Example Prompt

> Build a fuzz harness for src/parser/png_decode.c using libFuzzer with ASan and UBSan. Seed the corpus with the test PNGs in tests/fixtures/. Run a 5-minute smoke fuzz now, integrate a 1-minute smoke into GitHub Actions on every PR, and a 1-hour nightly. Triage crashes by stack trace.

## Safety Rules

- Never run an unbounded fuzz in CI — it will exhaust the budget.
- Do not commit a crashing input without filing an issue.
- Stop and ask the user if a crash appears to be a security vulnerability.
- If the fuzzer reveals memory corruption, treat it as a security finding.
- Never log full crash inputs at INFO — they may contain PII; log only the hash.
- If the target is in production, verify the fuzzer's crashes have been fixed before the next release.
