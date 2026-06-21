---
id: crypto-usage-reviewer
name: Crypto Usage Reviewer
category: cybersecurity
difficulty: Intermediate
tags:
  - argo
  - csp
  - cwe
  - cybersecurity
  - ecr
  - hipaa
  - nist
  - owasp
  - pci
  - rds
summary: |
  This Codex skill audits cryptographic usage in source code for weak algorithms, insecure modes, hardcoded keys, custom crypto, and non-compliant random number generation.
last_reviewed: 2026-06-21
---

## Purpose
This Codex skill audits cryptographic usage in source code for weak algorithms, insecure modes, hardcoded keys, custom crypto, and non-compliant random number generation. It exists because crypto flaws are subtle, rarely caught by functional tests, and routinely survive code review — and because the regulatory bar (FIPS 140-2/3, PCI DSS 3.5/3.6, NIST SP 800-131A) keeps rising while MD5, SHA-1, CBC without authentication, and `Math.random()` for security remain stubbornly common in real codebases.

## When to Use
Run this skill on any PR touching encryption, hashing, signing, key derivation, or random-number generation. Also use it during a FIPS-mode migration, after a library deprecation notice (e.g., `pycrypto` → `cryptography`), when rotating an algorithm off SHA-1/MD5 per NIST SP 800-131A, or as part of a pre-certification crypto audit ahead of a FedRAMP or FIPS 140-3 validation effort.

## Codex Instructions
1. Identify crypto APIs per language: Python (`hashlib`, `hmac`, `cryptography`, `pycryptodome`, `Crypto.*`); Node.js (`crypto`, `node-jose`, `bcrypt`); Go (`crypto/*`); Java (`javax.crypto.*`, `java.security.*`, BouncyCastle); C#/.NET (`System.Security.Cryptography`); Ruby (`OpenSSL::Cipher`, `Digest`); Rust (`ring`, `RustCrypto/*`); PHP (`openssl_encrypt`, `hash`, `random_bytes`).
2. Flag weak algorithms: MD5, SHA-1, SHA-0, RIPEMD-128, DES, 3DES, RC4, Blowfish for new code, ECB mode for any block cipher, CBC without an HMAC (no AEAD), RSA without OAEP padding, RSA signing without PSS, DSA, any `MODE_ECB`, AES key sizes <128 bits.
3. Flag insecure RNG: `Math.random()`, `random.random()`, `random.randint()` (Python's non-`SystemRandom`), `rand()`, `mt_rand()` (PHP), `java.util.Random`, `Math.random` — anywhere a security-sensitive value (token, key, nonce, password reset code, session ID, CSRF token) is derived from a non-CSPRNG.
4. Flag hardcoded keys/IVs: any 16/24/32-byte literal used as an AES key, any 16-byte literal used as an IV, any `password = "..."` used as a key directly without KDF, and any constant IV reused across encryptions (Critical — leaks plaintext structure).
5. Flag custom crypto: hand-rolled XOR ciphers, custom block modes, custom KDFs, custom HMAC constructions, and any `// don't use standard library, ours is faster` comment — treat as Critical and recommend the standard primitive.
6. Flag password storage issues: plaintext, MD5/SHA-1/SHA-256 of passwords without salt, bcrypt with cost factor <10, scrypt with N<2^14, Argon2id with m<19 MiB or t<2, PBKDF2 with <600,000 iterations (OWASP 2023 minimum).
7. For each finding, capture: file:line, the API call, the algorithm/mode/key-size, the data being protected, the recommendation, and the compliance driver (NIST SP 800-131A, OWASP Cryptographic Storage Cheat Sheet, FIPS 140-3).
8. Re-baseline severity: hardcoded production key = Critical; MD5 for password storage = Critical; SHA-1 for new signature = High; CBC-without-AEAD for new confidentiality = High; `Math.random()` for a CSRF token = Critical; for a UI animation = Info (false positive).
9. Map findings to CWE: CWE-327 (Broken/Risky Crypto), CWE-326 (Inadequate Encryption Strength), CWE-330 (Insufficient Randomness), CWE-329 (Not Using Unpredictable IV), CWE-798 (Hardcoded Credentials for keys), CWE-916 (Weak Password Hash).
10. Recommend replacements using each language's vetted library: `cryptography.hazmat` (Python), `crypto` (Node), `crypto/*` (Go), BouncyCastle or `java.security` (Java), `System.Security.Cryptography` (.NET). Prefer AEAD (AES-GCM, ChaCha20-Poly1305), HKDF for key derivation, Argon2id for password hashing.
11. Emit `CRYPTO_AUDIT.md` plus SARIF for upload to GitHub code scanning.

## Inputs Needed
- Repository path
- Language/runtime and crypto library in use
- Compliance driver (NIST SP 800-131A, FIPS 140-3, PCI DSS, HIPAA, FedRAMP)
- Whether the runtime is FIPS-validated (affects recommended primitives — no ChaCha20 in some FIPS modules)
- Data classification being protected (PII, PHI, PAN, secrets, internal)
- Existing key-management approach (KMS, Vault, env vars) — affects key-handling findings
- Whether password storage is in scope (separate from data-at-rest encryption)
- Prior pen test / audit findings to cross-correlate

## Expected Output
A markdown report `CRYPTO_AUDIT.md` with sections: Executive Summary (library, total findings by severity, top 3 risks, FIPS-mode status), Findings Table (ID, Severity, CWE, File:Line, API/Algorithm, Issue, Compliance Driver, Recommendation), Password Storage Review (if in scope), RNG Review (CSPRNG usage for security-sensitive values), and Hardening Plan (per-finding code snippet replacements). Severity scale: Critical (hardcoded prod key, MD5 password, custom crypto, `Math.random()` for token) / High (SHA-1 new, CBC no AEAD, weak KDF) / Medium (3DES, RSA without OAEP, low bcrypt cost) / Low (legacy but acceptable). Emit `crypto.sarif`.

## Example Prompt
> Review crypto usage in `/home/z/my-project/encryption-gateway` (Java 21 + BouncyCastle, plus a Python sidecar at `/home/z/my-project/encryption-gateway/sidecar`). We're pursuing FIPS 140-3 validation and need to retire SHA-1 and 3DES by EOY per NIST SP 800-131A. Flag every weak primitive, every hardcoded key, every `Math.random()`-derived token, propose BouncyCastle FIPS-approved replacements, and write `CRYPTO_AUDIT.md` with SARIF.

## Safety Rules
- Never print real production keys, IVs, or password hashes in the report; mask to last 4 chars.
- Do not recommend disabling FIPS mode to use a non-approved primitive; recommend the FIPS-approved equivalent.
- For password storage findings, never recommend MD5, SHA-1, or even SHA-256 with salt — recommend Argon2id (preferred), scrypt, bcrypt, or PBKDF2 per OWASP.
- For RNG findings, never recommend `Math.random()` or `random.random()` for security-sensitive values, even with a "seeded" wrapper — require a CSPRNG (`crypto.randomBytes`, `secrets`, `SecureRandom`, `crypto/rand`).
- Do not auto-apply crypto patches; propose them for review by a crypto-literate engineer.
- If a custom crypto construction is found, treat as Critical even if the author claims it's reviewed — recommend replacement with a standard primitive and an independent third-party audit.
- For hardcoded IVs, recommend a fresh random IV per encryption and never reuse — this is a Critical, not a Medium.
- Keep all recommended key sizes at or above NIST minimums (AES-128 floor, RSA-2048 floor, ECDSA P-256 floor); never recommend shorter for performance.
