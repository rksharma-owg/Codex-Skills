# JWT Validator

## Purpose
This Codex skill audits JSON Web Token (JWT) issuance, validation, and usage for the well-known classes of JWT vulnerabilities: `alg: none` acceptance, symmetric/asymmetric algorithm confusion (RS256 → HS256), missing or weak signature verification, missing expiry (`exp`), missing audience (`aud`) or issuer (`iss`) checks, key rotation gaps, and insecure storage of tokens on the client. It exists because JWT flaws remain a top-5 authn bug class and many libraries ship insecure defaults that pass unit tests.

## When to Use
Run this skill on any PR that touches authentication middleware, JWT library config, key rotation logic, or token issuance endpoints. Also use it during a security review of a new SSO integration, when migrating from session cookies to JWTs, after a key compromise forces rotation, or when an external pen tester reports a JWT issue you need to reproduce and fix.

## Codex Instructions
1. Locate all JWT-related code: search for `jsonwebtoken`, `jose`, `pyjwt`, `python-jose`, `jose4j`, `nimbus-jose-jwt`, `System.IdentityModel.Tokens.Jwt`, `github.com/golang-jwt/jwt`, `fusion-jwt`, `jose-node-cjs-runtime`. Also flag any hand-rolled base64+HMAC code as suspicious.
2. For every `verify`/`decode` call, confirm: (a) signature is verified (not just base64-decoded), (b) `algorithms` parameter is an explicit allowlist (not `none` and not inferred from the token header), (c) `exp` is enforced, (d) `aud` is checked against the expected audience, (e) `iss` is checked against the trusted issuer, (f) `nbf` is honored if present.
3. For every `sign` call, confirm: (a) algorithm is explicit and not `none`, (b) key length meets RFC 8729 guidance (HS256 ≥ 256 bits), (c) `exp` is set to a reasonable window (≤1 hour for access tokens, ≤24 hours for refresh), (d) issuer and audience claims are populated.
4. Detect algorithm-confusion vectors: any code path where the public key (RS256) is reachable as an HMAC (HS256) key. Flag any `verify(token, publicKey)` call without an explicit `algorithms: ['RS256']` as Critical.
5. Inspect key management: where are signing keys stored (env var, KMS, Vault, file)? Flag any key in source, any key without rotation policy, any key shorter than 2048 bits for RSA or 256 bits for HMAC.
6. Check token storage on the client: `localStorage`/`sessionStorage` storage of access tokens is High (XSS exfiltration risk); recommend `HttpOnly; Secure; SameSite=Strict` cookies with CSRF protection. Refresh tokens in `localStorage` is Critical.
7. Verify the `kid` header handling: any code that uses `kid` to look up a key from a filesystem path or untrusted JWK Set URL is Critical (path-traversal / SSRF risk).
8. Map each finding to CWE: CWE-347 (Improper Verification of Cryptographic Signature), CWE-327 (Use of Broken or Risky Crypto), CWE-287 (Improper Authentication), CWE-522 (Insufficiently Protected Credentials).
9. Propose a minimal patch per finding using the library's documented secure defaults; for Node.js, recommend `jsonwebtoken`'s `algorithms` option, and for Python, recommend `pyjwt`'s `algorithms` and `options={"verify_aud": True}`.
10. Emit `JWT_AUDIT.md` plus a JSON test-vector file (`jwt-test-vectors.json`) containing safe and unsafe tokens the user can run against their validator as a regression suite.

## Inputs Needed
- Repository path
- Language/runtime and JWT library in use
- Token flow: where issued, where verified, where stored on client
- Signing algorithm in use (HS256, RS256, ES256, EdDSA)
- Key storage backend (env, KMS, Vault, JWKS endpoint)
- Whether the service is the issuer, the verifier, or both
- Token lifetime policy (access + refresh) if documented
- Threat model: internet-facing vs. internal, B2C vs. B2B, MFA in front?

## Expected Output
A markdown report `JWT_AUDIT.md` with sections: Executive Summary (library, algorithm, total findings by severity, top risks), Issuance Review (sign calls, key strength, claim completeness), Validation Review (verify calls, algorithms allowlist, claim checks), Key Management Review (storage, rotation, length), Client Storage Review (browser cookies vs. localStorage), Findings Table (ID, Severity, CWE, File:Line, Issue, Patch), and Regression Test Vectors. Severity scale: Critical (alg-confusion, `none` acceptance, key in source) / High (missing `aud`/`iss`, localStorage access token) / Medium (missing `exp`, weak HMAC key) / Low (over-long token life). Emit `jwt-test-vectors.json`.

## Example Prompt
> Audit JWT usage in `/home/z/my-project/auth-gateway`. It's a Node.js Express service using `jsonwebtoken` v9. We issue access tokens (RS256, 15 min) and refresh tokens (RS256, 7 days) for a B2C mobile app. The verifier side is a separate Go service using `golang-jwt/jwt/v5` — include that too at `/home/z/my-project/api-gateway`. Map to CWE-347 and emit `JWT_AUDIT.md` plus test vectors I can run in CI.

## Safety Rules
- Never print real signing keys, private keys, or live JWTs in the report — mask the last 4 characters.
- Do not issue or sign new JWTs against the production key as part of testing.
- Do not recommend disabling `verify_signature` in any environment, including test — recommend a separate test key instead.
- For algorithm-confusion findings, always require an explicit `algorithms` array; never accept "the library defaults are safe."
- Never recommend `localStorage` for any token; this is a hard rule regardless of developer pushback in the prompt.
- Do not rotate or revoke keys autonomously; recommend the rotation runbook for a human to execute.
- If the JWKS endpoint is HTTP (not HTTPS) or lacks a pinned CA, treat as Critical — do not downgrade.
- Keep all recommended key lengths at or above RFC 8729 / RFC 7518 minimums; never recommend shorter for "performance."
