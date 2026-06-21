# Memory Safety Reviewer

## Purpose

This Codex skill reviews C, C++, Rust (unsafe), and Zig code for memory safety defects: buffer overflows, use-after-free, double-free, out-of-bounds reads/writes, format string bugs, and integer overflows that lead to memory corruption. It maps findings to CWE-119, CWE-416, CWE-415, CWE-787, CWE-125, and CWE-190.

## When to Use

Use during code review of native code, when integrating a new C/C++ dependency, after a fuzzing campaign reports a crash, or before shipping a parser, codec, or protocol implementation that processes untrusted input.

## Codex Instructions

1. Inventory unsafe constructs: raw pointer arithmetic, malloc/free pairs, memcpy/memmove with computed sizes, sprintf/strcpy/strcat, and unsafe Rust blocks.
2. For each pointer dereference, verify the pointer is non-null, the memory is live, and the offset is within the allocation.
3. For each length computation, check for integer overflow before the multiplication or addition that sizes a buffer.
4. For each format string call, ensure the format string is a compile-time constant; reject user-controlled format strings.
5. For each allocator pair (malloc/free, new/delete), verify the ownership is single and clear; flag double-free and leak patterns.
6. For each array index, verify the index is bounded by a length check that uses the same units (bytes vs elements).
7. Prefer safer alternatives: snprintf over sprintf, strlcpy/strncpy over strcpy, std::vector/raw::Vec over raw arrays, Rust safe slices over unsafe pointer arithmetic.
8. Where unsafe is unavoidable, document the invariant in a SAFETY comment and add a test or fuzz target that exercises the unsafe block.
9. Run the project's static analyzer (clang-tidy, cppcheck, MSVC /analyze, cargo clippy) and cross-reference findings with the manual review.
10. Produce a patch list and a risk-prioritized findings table; for each finding, propose the safe rewrite or the SAFETY-justified unsafe block.

## Inputs Needed

- Source directory or files to review
- Language and compiler (C, C++, Rust unsafe, Zig)
- Static analyzers available (clang-tidy, cppcheck, clippy, PVS-Studio)
- Existing test and fuzz harness coverage
- Whether the code processes untrusted input

## Expected Output

A Markdown report titled 'Memory Safety Audit' with: (1) Findings Table — ID | File:Line | CWE | Severity | Description | Proposed Fix; (2) Patch Diff with safer alternatives; (3) SAFETY Comment Review for any remaining unsafe blocks; (4) Fuzz Plan listing the inputs and harnesses to add.

## Example Prompt

> Review src/parser/ in this C++ library for memory safety. We process untrusted PNG input — focus on buffer handling, integer overflow in size computations, and use-after-free in error paths. Propose safe rewrites where possible.

## Safety Rules

- Never auto-commit unsafe-to-safe rewrites that change API signatures — produce a patch for review.
- Do not remove a SAFETY comment to 'clean up' code; the comment is required documentation.
- If a finding cannot be fixed without an architecture change (e.g., switching to arena allocation), flag it rather than guessing.
- Stop and ask the user if the codebase has custom allocators that affect ownership analysis.
- Never log raw memory dumps at INFO — redact to offsets and lengths only.
- Treat every crash from a fuzzer as a security finding until proven otherwise.
