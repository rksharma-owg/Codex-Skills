# Deserialization Risk Finder

## Purpose
This Codex skill detects insecure deserialization vulnerabilities across Java, .NET, Python, Ruby, PHP, and Node.js codebases — including the well-known gadget-chain classes (Java `ObjectInputStream`, .NET `BinaryFormatter`, Python `pickle`, Ruby `Marshal`, PHP `unserialize`, Node.js `node-serialize`). It exists because deserialization flaws (OWASP A08:2021) frequently lead to unauthenticated RCE, are often missed by SAST, and have powered some of the most damaging breaches in history (Apache Commons Collections, Equifax via Struts/BeanUtils, Confluence OGNL).

## When to Use
Run this skill on any PR touching serialization/deserialization code, RPC frameworks, message queues, caching layers, or session storage. Also use it when introducing a library that wraps `ObjectInputStream` (e.g., Spring `HttpInvoker`, Apache Camel), when a CVE drops for a gadget library on your classpath (Commons Collections, BeanUtils, log4j's `JndiLookup`), or during a pre-prod audit of a service that consumes untrusted serialized payloads (B2B integrations, legacy SOAP, memcached session stores).

## Codex Instructions
1. Identify deserialization sinks per language: Java (`ObjectInputStream.readObject`, `XMLDecoder`, `Yaml.load` (SnakeYAML), `XStream.fromXML`, `Jackson` with default typing enabled, `XMLMapper`, `SerializationUtils.deserialize`); .NET (`BinaryFormatter.Deserialize`, `LosFormatter`, `NetDataContractSerializer`, `ObjectStateFormatter`, `JavaScriptSerializer` with `SimpleTypeResolver`); Python (`pickle.loads`, `cPickle`, `yaml.load` without `Loader=SafeLoader`, `shelve`, `marshal.loads`); Ruby (`Marshal.load`); PHP (`unserialize`, `__wakeup`/`__destruct` gadgets); Node.js (`node-serialize.unserialize`, `serialize.unserialize`).
2. Treat as **sources**: any data crossing a trust boundary — HTTP request body, message queue payload, cache value, session blob, file from upload, RMI/IIOP call, SOAP body, gRPC field, database BLOB populated by another service.
3. Treat as **sanitizers**: allowlist-based type filters (Jackson `activateDefaultTyping` with a `BasicPolymorphicTypeValidator` allowlist), `ObjectInputFilter` (Java 9+), `SafeLoader` for PyYAML, JSON-only formats (no native object graph), signed payloads with a verified HMAC before deserialization.
4. For each sink, trace the source. If the path crosses a trust boundary without a sanitizer or allowlist, classify as a confirmed deserialization vulnerability.
5. For Java specifically, scan the dependency tree (use `mvn dependency:tree` or `gradle dependencies`) for known gadget libraries: `commons-collections <= 3.2.1`, `commons-collections4 < 4.1`, `commons-beanutils <= 1.9.2`, `spring-core` (for `SpringPartiallyComparableAdvisor`), `aspectjweaver`, `bcel`, `groovy < 2.4.4`, `jdom`, `xalan`. Flag any gadget library present on a classpath with an untrusted `ObjectInputStream`.
6. For .NET, flag any `BinaryFormatter` usage as Critical — Microsoft marked it obsolete in .NET 5 and recommends `DataContractSerializer` or `System.Text.Json`.
7. For Python, flag any `pickle.loads` on data from a network source as Critical; recommend `json` or `msgpack` with explicit schema validation.
8. For Ruby, flag any `Marshal.load` on data from a network source as Critical; Marshal is never safe on untrusted input.
9. For PHP, flag any `unserialize` on user input as Critical; recommend `json_decode` with schema validation.
10. Re-baseline severity: any sink reachable from unauthenticated input = Critical (potential RCE); from authenticated-only input = High; from internal-only RPC = Medium; from test fixtures = Low.
11. Map each finding to CWE-502 (Deserialization of Untrusted Data).
12. Propose a patch per finding: prefer JSON or Protobuf over native serialization; if native is required, enforce a strict type allowlist via `ObjectInputFilter` / `BasicPolymorphicTypeValidator` / equivalent, and require an HMAC signature on the payload before deserialization.
13. Emit `DESERIAL_AUDIT.md` plus SARIF.

## Inputs Needed
- Repository path
- Language/runtime and serialization library in use
- Build manifest (`pom.xml`, `build.gradle`, `requirements.txt`, `package.json`, `Gemfile`, `*.csproj`) — to scan the dependency tree for gadget libraries
- Trust boundary map: which inputs are authenticated, which are unauthenticated, which are internal-only
- Existing type-allowlist or `ObjectInputFilter` config (so you don't re-flag a sanitized path)
- Whether the service consumes serialized payloads from external partners (B2B integrations)
- Compliance driver (PCI DSS Req. 6.2.4, FedRAMP, SOC 2) if the report feeds an audit
- Prior pen test / CVE history for the codebase

## Expected Output
A markdown report `DESERIAL_AUDIT.md` with sections: Executive Summary (language, total sinks scanned, total findings by severity, gadget libraries detected on classpath), Sinks Inventory (one subsection per sink: file:line, API, source path, sanitizer present?), Gadget Library Analysis (per library: version, CVE history, recommended upgrade or removal), Findings Table (ID, Severity, CWE, Sink File:Line, Source, Sanitizer?, Patch), and Hardening Plan. Severity scale: Critical (untrusted-to-ObjectInputStream/pickle/Marshal/unserialize/BinaryFormatter) / High (authenticated input to native sink) / Medium (internal-only) / Low (test fixtures, sandbox). Emit `deserialization.sarif`.

## Example Prompt
> Audit deserialization in `/home/z/my-project/legacy-b2b-gateway`. It's a Java 17 Spring Boot service that accepts XML payloads from partners via SOAP and uses `XStream.fromXML` plus `ObjectInputStream` for cached session blobs. We still depend on `commons-collections` 3.2.1 (yes, I know). Map all sinks reachable from unauthenticated input, identify gadget libraries in `pom.xml`, propose `ObjectInputFilter`-based allowlists and an XStream replacement, and write `DESERIAL_AUDIT.md` with SARIF.

## Safety Rules
- Never deserialize a real untrusted payload to "verify" a finding — static analysis only.
- Do not recommend disabling `ObjectInputFilter` or any other guard to "make the code work."
- For Java gadget libraries on an untrusted `ObjectInputStream` path, treat as Critical regardless of whether a public PoC exists for that exact version.
- For .NET `BinaryFormatter`, never recommend continuing to use it; always recommend `DataContractSerializer`, `System.Text.Json`, or `MessagePack-CSharp`.
- For Python `pickle`, never recommend `pickle` for untrusted input — there is no safe mode.
- Do not auto-apply patches or modify dependency manifests; propose them for review.
- If a gadget library cannot be upgraded (legacy lock-in), recommend a runtime agent (Contrast, RASP) as defense-in-depth, not as a substitute.
- Never include real serialized payloads or session blobs in the report; substitute `[BASE64 PAYLOAD]` placeholders.
