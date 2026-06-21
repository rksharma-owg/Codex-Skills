# Codex Agent Skills — Catalog

**123 skills** across **8 categories**. Each skill is a standalone Markdown file with YAML frontmatter, ready to paste into Codex, Claude Code, Cursor, or any LLM-based coding agent.

## Browse by Category

- [🛡️ Cybersecurity (15)](#cybersecurity) — Find, triage, and fix exploitable vulnerabilities across code, containers, and infrastructure.
- [🔒 Secure Coding (16)](#secure-coding) — Harden code at the source: validation, encoding, sessions, crypto, and code-review fundamentals.
- [☁️ Cloud Security & Compliance (19)](#cloud-security) — Audit AWS/Azure/GCP posture, segment networks, and satisfy PCI, GDPR, SOC 2, HIPAA, ISO 27001.
- [🚨 Incident Response (14)](#incident-response) — Detect, contain, and learn from incidents — forensics, RCA, comms, postmortems, and DSAR.
- [🤖 AI Security (9)](#ai-security) — Test and harden LLM applications: prompt injection, RAG trust, model supply chain, agent gating.
- [⚙️ DevOps & Engineering Practice (26)](#devops) — Ship safer and faster: CI optimization, container hardening, observability, architecture, and docs.
- [🧪 Testing (10)](#testing) — Build the testing pyramid: unit, integration, load, mutation, fuzz, contract, E2E, security.
- [🐙 GitHub Automation (14)](#github-automation) — Automate the GitHub lifecycle: Actions, releases, branch protection, Dependabot, OIDC, secret scanning.

## Browse by Difficulty

- **Beginner** — 14 skills
- **Intermediate** — 81 skills
- **Advanced** — 28 skills

---

## 🛡️ Cybersecurity

_Find, triage, and fix exploitable vulnerabilities across code, containers, and infrastructure._

**15 skills** · Capabilities: vulnerability hunting, secret detection, SAST triage, OWASP Top 10, runtime defense

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Authz Bypass Finder | Intermediate | This Codex skill detects authorization (authz) bypass vulnerabilities — broken object-level authorization (BOLA/IDOR), b… | [`skills/cybersecurity/authz-bypass-finder.md`](../skills/cybersecurity/authz-bypass-finder.md) |
| 2 | Crypto Usage Reviewer | Intermediate | This Codex skill audits cryptographic usage in source code for weak algorithms, insecure modes, hardcoded keys, custom c… | [`skills/cybersecurity/crypto-usage-reviewer.md`](../skills/cybersecurity/crypto-usage-reviewer.md) |
| 3 | Dependency Vulnerability Auditor | Beginner | This Codex skill audits third-party dependencies for known vulnerabilities (CVEs and GHSA advisories), end-of-life packa… | [`skills/cybersecurity/dependency-vulnerability-auditor.md`](../skills/cybersecurity/dependency-vulnerability-auditor.md) |
| 4 | Deserialization Risk Finder | Intermediate | This Codex skill detects insecure deserialization vulnerabilities across Java, .NET, Python, Ruby, PHP, and Node.js code… | [`skills/cybersecurity/deserialization-risk-finder.md`](../skills/cybersecurity/deserialization-risk-finder.md) |
| 5 | Docker Image Scanner | Intermediate | This Codex skill scans container images for OS-package CVEs, misconfigurations, exposed secrets, risky defaults, and blo… | [`skills/cybersecurity/docker-image-scanner.md`](../skills/cybersecurity/docker-image-scanner.md) |
| 6 | IaC Misconfig Detector | Intermediate | This Codex skill detects misconfigurations in Infrastructure-as-Code (Terraform, CloudFormation, Pulumi, Helm, Kustomize… | [`skills/cybersecurity/iac-misconfig-detector.md`](../skills/cybersecurity/iac-misconfig-detector.md) |
| 7 | JWT Validator | Intermediate | This Codex skill audits JSON Web Token (JWT) issuance, validation, and usage for the well-known classes of JWT vulnerabi… | [`skills/cybersecurity/jwt-validator.md`](../skills/cybersecurity/jwt-validator.md) |
| 8 | OWASP Top 10 Remediator | Intermediate | This Codex skill maps a codebase's security findings to the OWASP Top 10 2021 categories (A01 Broken Access Control thro… | [`skills/cybersecurity/owasp-top-10-remediator.md`](../skills/cybersecurity/owasp-top-10-remediator.md) |
| 9 | SAST Triage | Intermediate | This Codex skill triages raw Static Application Security Testing (SAST) output from tools like Semgrep, CodeQL, Snyk Cod… | [`skills/cybersecurity/sast-triage.md`](../skills/cybersecurity/sast-triage.md) |
| 10 | Secret Scanner | Beginner | This Codex skill hunts for hardcoded credentials, API keys, private keys, tokens, and other sensitive material committed… | [`skills/cybersecurity/secret-scanner.md`](../skills/cybersecurity/secret-scanner.md) |
| 11 | Secrets in Logs Scrubber | Intermediate | This Codex skill audits application logs, CI/CD pipeline logs, container logs, and observability pipelines (stdout, file… | [`skills/cybersecurity/secrets-in-logs-scrubber.md`](../skills/cybersecurity/secrets-in-logs-scrubber.md) |
| 12 | SQL Injection Finder | Intermediate | This Codex skill detects SQL Injection (SQLi) vulnerabilities — classic, blind, second-order, and stored-procedure-based… | [`skills/cybersecurity/sql-injection-finder.md`](../skills/cybersecurity/sql-injection-finder.md) |
| 13 | SSRF Detector | Intermediate | This Codex skill detects Server-Side Request Forgery (SSRF) vulnerabilities — classic, blind, and the cloud-metadata var… | [`skills/cybersecurity/ssrf-detector.md`](../skills/cybersecurity/ssrf-detector.md) |
| 14 | TLS Config Auditor | Intermediate | This Codex skill audits TLS/SSL configuration across load balancers, web servers, API gateways, sidecar proxies, languag… | [`skills/cybersecurity/tls-config-auditor.md`](../skills/cybersecurity/tls-config-auditor.md) |
| 15 | XSS Finder | Intermediate | This Codex skill detects Cross-Site Scripting (XSS) vulnerabilities — reflected, stored, DOM-based, and mutation-based —… | [`skills/cybersecurity/xss-finder.md`](../skills/cybersecurity/xss-finder.md) |

## 🔒 Secure Coding

_Harden code at the source: validation, encoding, sessions, crypto, and code-review fundamentals._

**16 skills** · Capabilities: input validation, output encoding, parameterization, session hardening, PR review

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Application Security (Comprehensive) | Advanced | Comprehensive application-security skill covering auth, input validation, data protection, monitoring, secure config, su… | [`skills/secure-coding/application-security.md`](../skills/secure-coding/application-security.md) |
| 2 | Complexity Reducer | Intermediate | This Codex skill reduces cyclomatic and cognitive complexity by extracting helper functions, replacing nested conditiona… | [`skills/secure-coding/complexity-reducer.md`](../skills/secure-coding/complexity-reducer.md) |
| 3 | CSRF Token Generator | Intermediate | This Codex skill implements or hardens Cross-Site Request Forgery protection by generating per-session, signed CSRF toke… | [`skills/secure-coding/csrf-token-generator.md`](../skills/secure-coding/csrf-token-generator.md) |
| 4 | Dangerous Function Replacer | Intermediate | This Codex skill scans for and replaces known-dangerous standard library functions with safe equivalents across language… | [`skills/secure-coding/dangerous-function-replacer.md`](../skills/secure-coding/dangerous-function-replacer.md) |
| 5 | Dead Code Eliminator | Intermediate | This Codex skill identifies and removes unreachable code: unused private functions, commented-out blocks, unused imports… | [`skills/secure-coding/dead-code-eliminator.md`](../skills/secure-coding/dead-code-eliminator.md) |
| 6 | Error Message Sanitizer | Intermediate | This Codex skill audits error messages, stack traces, and exception payloads to ensure they do not leak sensitive inform… | [`skills/secure-coding/error-message-sanitizer.md`](../skills/secure-coding/error-message-sanitizer.md) |
| 7 | Input Validation Hardener | Intermediate | This Codex skill audits every entry point where untrusted data crosses a trust boundary (HTTP handlers, gRPC methods, qu… | [`skills/secure-coding/input-validation-hardener.md`](../skills/secure-coding/input-validation-hardener.md) |
| 8 | Memory Safety Reviewer | Intermediate | This Codex skill reviews C, C++, Rust (unsafe), and Zig code for memory safety defects: buffer overflows, use-after-free… | [`skills/secure-coding/memory-safety-reviewer.md`](../skills/secure-coding/memory-safety-reviewer.md) |
| 9 | Output Encoding Helper | Intermediate | This Codex skill ensures that every value rendered into HTML, JavaScript, CSS, URL, or attribute context is encoded with… | [`skills/secure-coding/output-encoding-helper.md`](../skills/secure-coding/output-encoding-helper.md) |
| 10 | Parameterized Query Generator | Intermediate | This Codex skill converts string-concatenated SQL, NoSQL, OS command, and LDAP queries into parameterized or prepared-st… | [`skills/secure-coding/parameterized-query-generator.md`](../skills/secure-coding/parameterized-query-generator.md) |
| 11 | Password Hashing Advisor | Intermediate | This Codex skill reviews password storage to ensure hashing uses Argon2id (preferred), bcrypt with cost >= 12, or scrypt… | [`skills/secure-coding/password-hashing-advisor.md`](../skills/secure-coding/password-hashing-advisor.md) |
| 12 | PR Summary Writer | Beginner | This Codex skill reads a git diff and the related issue context, then produces a structured PR description: a one-paragr… | [`skills/secure-coding/pr-summary-writer.md`](../skills/secure-coding/pr-summary-writer.md) |
| 13 | Race Condition Finder | Intermediate | This Codex skill identifies Time-of-Check-to-Time-of-Use (TOCTOU) and other concurrency bugs in shared-state code paths:… | [`skills/secure-coding/race-condition-finder.md`](../skills/secure-coding/race-condition-finder.md) |
| 14 | Review Checklist Generator | Beginner | This Codex skill generates a per-PR review checklist tailored to the change type, language, framework, and affected area… | [`skills/secure-coding/review-checklist-generator.md`](../skills/secure-coding/review-checklist-generator.md) |
| 15 | Secure File Upload Handler | Intermediate | This Codex skill designs or audits file upload pipelines to prevent malicious file execution, path traversal via filenam… | [`skills/secure-coding/secure-file-upload-handler.md`](../skills/secure-coding/secure-file-upload-handler.md) |
| 16 | Secure Session Manager | Intermediate | This Codex skill audits and hardens session management: cookie flags, session ID entropy, rotation on authentication, id… | [`skills/secure-coding/secure-session-manager.md`](../skills/secure-coding/secure-session-manager.md) |

## ☁️ Cloud Security & Compliance

_Audit AWS/Azure/GCP posture, segment networks, and satisfy PCI, GDPR, SOC 2, HIPAA, ISO 27001._

**19 skills** · Capabilities: IAM audit, network segmentation, compliance mapping, workload identity, audit logging

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Access Review Orchestrator | Intermediate | This Codex skill orchestrates a quarterly access review: pulls the current access list (who has access to what), sends t… | [`skills/cloud-security/access-review-orchestrator.md`](../skills/cloud-security/access-review-orchestrator.md) |
| 2 | Audit Log Architect | Advanced | This Codex skill designs an audit logging system that meets compliance requirements (SOC 2, HIPAA, PCI): what to log, th… | [`skills/cloud-security/audit-log-architect.md`](../skills/cloud-security/audit-log-architect.md) |
| 3 | AWS IAM Policy Auditor | Intermediate | This Codex skill audits AWS IAM policies (managed and inline) for over-permissive statements: Action '*', Resource '*', … | [`skills/cloud-security/aws-iam-policy-auditor.md`](../skills/cloud-security/aws-iam-policy-auditor.md) |
| 4 | Azure Security Baseline Checker | Intermediate | This Codex skill checks an Azure subscription against the Azure Security Benchmark: MFA on all accounts, no legacy auth,… | [`skills/cloud-security/azure-security-baseline-checker.md`](../skills/cloud-security/azure-security-baseline-checker.md) |
| 5 | Cloud Backup Recovery Planner | Intermediate | This Codex skill designs a backup and recovery plan for cloud workloads: RPO and RTO targets, backup types (snapshot, in… | [`skills/cloud-security/cloud-backup-recovery-planner.md`](../skills/cloud-security/cloud-backup-recovery-planner.md) |
| 6 | Cloud Network Segmentation Planner | Advanced | This Codex skill designs a network segmentation strategy for a cloud workload: VPC design, subnet tiers (public, private… | [`skills/cloud-security/cloud-network-segmentation-planner.md`](../skills/cloud-security/cloud-network-segmentation-planner.md) |
| 7 | Cloud Secret Manager Migrator | Intermediate | This Codex skill migrates secrets from scattered sources (env vars, .env files, hardcoded values, Kubernetes Secrets in … | [`skills/cloud-security/cloud-secret-manager-migrator.md`](../skills/cloud-security/cloud-secret-manager-migrator.md) |
| 8 | Cloud Workload Identity Migrator | Advanced | This Codex skill migrates workloads from long-lived service account keys to workload identity federation (AWS IRSA, GCP … | [`skills/cloud-security/cloud-workload-identity-migrator.md`](../skills/cloud-security/cloud-workload-identity-migrator.md) |
| 9 | CloudTrail Forensics Helper | Intermediate | This Codex skill queries AWS CloudTrail logs to investigate a security incident: identifies the source IP, user agent, A… | [`skills/cloud-security/cloudtrail-forensics-helper.md`](../skills/cloud-security/cloudtrail-forensics-helper.md) |
| 10 | GCP IAM Recommender | Intermediate | This Codex skill uses GCP's IAM Recommender and additional analysis to identify over-permissive IAM bindings, service ac… | [`skills/cloud-security/gcp-iam-recommender.md`](../skills/cloud-security/gcp-iam-recommender.md) |
| 11 | GDPR Data Flow Mapper | Advanced | This Codex skill maps the flow of personal data through an application: collection points, storage locations, processors… | [`skills/cloud-security/gdpr-data-flow-mapper.md`](../skills/cloud-security/gdpr-data-flow-mapper.md) |
| 12 | GuardDuty Finding Triager | Intermediate | This Codex skill triages AWS GuardDuty findings: classifies each as true positive, false positive, or benign-but-actiona… | [`skills/cloud-security/guardduty-finding-triager.md`](../skills/cloud-security/guardduty-finding-triager.md) |
| 13 | HIPAA PHI Handler | Advanced | This Codex skill designs the handling of Protected Health Information (PHI) in an application: minimum necessary access,… | [`skills/cloud-security/hipaa-phi-handler.md`](../skills/cloud-security/hipaa-phi-handler.md) |
| 14 | ISO 27001 Control Implementer | Advanced | This Codex skill designs implementations for ISO 27001 Annex A controls: A.5 (policies), A.6 (organization), A.7 (HR), A… | [`skills/cloud-security/iso-27001-control-implementer.md`](../skills/cloud-security/iso-27001-control-implementer.md) |
| 15 | Kubernetes NetworkPolicy Generator | Advanced | This Codex skill generates NetworkPolicy YAML for a Kubernetes namespace based on the actual observed traffic between po… | [`skills/cloud-security/kubernetes-network-policy-generator.md`](../skills/cloud-security/kubernetes-network-policy-generator.md) |
| 16 | Multi-Cloud Inventory Builder | Intermediate | This Codex skill builds a unified inventory of resources across AWS, Azure, and GCP: compute, storage, network, IAM, and… | [`skills/cloud-security/multi-cloud-inventory-builder.md`](../skills/cloud-security/multi-cloud-inventory-builder.md) |
| 17 | PCI DSS Scope Mapper | Advanced | This Codex skill maps an application's architecture to PCI DSS scope: identifies the cardholder data environment (CDE), … | [`skills/cloud-security/pci-dss-scope-mapper.md`](../skills/cloud-security/pci-dss-scope-mapper.md) |
| 18 | S3 Bucket Policy Auditor | Intermediate | This Codex skill audits S3 buckets for public exposure, missing encryption, missing versioning, missing access logs, and… | [`skills/cloud-security/s3-bucket-policy-auditor.md`](../skills/cloud-security/s3-bucket-policy-auditor.md) |
| 19 | SOC 2 Control Mapper | Advanced | This Codex skill maps an org's controls to the SOC 2 Trust Services Criteria: Security, Availability, Processing Integri… | [`skills/cloud-security/soc2-control-mapper.md`](../skills/cloud-security/soc2-control-mapper.md) |

## 🚨 Incident Response

_Detect, contain, and learn from incidents — forensics, RCA, comms, postmortems, and DSAR._

**14 skills** · Capabilities: severity classification, RCA, forensics, postmortem, data subject requests

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Compromised Credential Responder | Advanced | This Codex skill orchestrates the response to a compromised credential: identify the scope (which systems the credential… | [`skills/incident-response/compromised-credential-responder.md`](../skills/incident-response/compromised-credential-responder.md) |
| 2 | Data Retention Policy Enforcer | Intermediate | This Codex skill designs and implements a data retention policy: per-data-type retention periods, automated deletion mec… | [`skills/incident-response/data-retention-policy-enforcer.md`](../skills/incident-response/data-retention-policy-enforcer.md) |
| 3 | DSAR Responder | Intermediate | This Codex skill orchestrates the response to a Data Subject Access Request (DSAR): verify identity, locate all the user… | [`skills/incident-response/dsar-responder.md`](../skills/incident-response/dsar-responder.md) |
| 4 | Forensic Snapshot Collector | Advanced | This Codex skill orchestrates the collection of forensic snapshots during a security incident: disk images, memory dumps… | [`skills/incident-response/forensic-snapshot-collector.md`](../skills/incident-response/forensic-snapshot-collector.md) |
| 5 | Incident Comms Drafter | Intermediate | This Codex skill drafts customer-facing and internal communications during an incident: status page updates, customer em… | [`skills/incident-response/incident-comms-drafter.md`](../skills/incident-response/incident-comms-drafter.md) |
| 6 | Incident Severity Classifier | Beginner | This Codex skill classifies a reported incident by severity (SEV1 through SEV4) based on impact (users affected, revenue… | [`skills/incident-response/incident-severity-classifier.md`](../skills/incident-response/incident-severity-classifier.md) |
| 7 | Incident Timeline Builder | Intermediate | This Codex skill reconstructs an incident timeline from logs, alerts, chat messages, and commit history: detection time,… | [`skills/incident-response/incident-timeline-builder.md`](../skills/incident-response/incident-timeline-builder.md) |
| 8 | IR Runbook Index Builder | Intermediate | This Codex skill builds and maintains an index of incident response runbooks: by scenario (malware, cred compromise, dat… | [`skills/incident-response/ir-runbook-index-builder.md`](../skills/incident-response/ir-runbook-index-builder.md) |
| 9 | IR Tabletop Exercise Designer | Advanced | This Codex skill designs a tabletop exercise for the incident response team: scenario, inject sequence, expected actions… | [`skills/incident-response/ir-tabletop-exercise-designer.md`](../skills/incident-response/ir-tabletop-exercise-designer.md) |
| 10 | Malware Triage Analyzer | Advanced | This Codex skill performs initial triage on a suspected malware sample: file type, hashes, AV detections (VirusTotal), s… | [`skills/incident-response/malware-triage-analyzer.md`](../skills/incident-response/malware-triage-analyzer.md) |
| 11 | Postmortem Author | Intermediate | This Codex skill authors a blameless postmortem document for a resolved incident: summary, timeline, impact, root cause,… | [`skills/incident-response/postmortem-author.md`](../skills/incident-response/postmortem-author.md) |
| 12 | Root Cause Analyzer | Advanced | This Codex skill performs a 5-Whys or fishbone root cause analysis on an incident: iteratively asks 'why' until reaching… | [`skills/incident-response/root-cause-analyzer.md`](../skills/incident-response/root-cause-analyzer.md) |
| 13 | Runbook Author | Intermediate | This Codex skill authors operational runbooks for an on-call engineer: service overview, common alerts, triage steps, mi… | [`skills/incident-response/runbook-author.md`](../skills/incident-response/runbook-author.md) |
| 14 | Vendor Risk Assessor | Advanced | This Codex skill assesses a vendor's security and compliance posture before onboarding: questionnaire, evidence review (… | [`skills/incident-response/vendor-risk-assessor.md`](../skills/incident-response/vendor-risk-assessor.md) |

## 🤖 AI Security

_Test and harden LLM applications: prompt injection, RAG trust, model supply chain, agent gating._

**9 skills** · Capabilities: prompt injection, LLM output filtering, RAG trust, model supply chain, drift monitoring

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | AI Agent Tool Gatekeeper | Advanced | This Codex skill designs a tool-call gatekeeper for an LLM agent that can invoke tools: allowlist of tools per agent, pa… | [`skills/ai-security/ai-agent-tool-gatekeeper.md`](../skills/ai-security/ai-agent-tool-gatekeeper.md) |
| 2 | AI Model Supply Chain Auditor | Advanced | This Codex skill audits the supply chain of AI models used by an application: model provenance (Hugging Face, OpenAI, in… | [`skills/ai-security/ai-model-supply-chain-auditor.md`](../skills/ai-security/ai-model-supply-chain-auditor.md) |
| 3 | AI PII Redactor | Intermediate | This Codex skill designs a PII redaction layer for an LLM application: detects PII in user input and LLM output (SSN, em… | [`skills/ai-security/ai-pii-redactor.md`](../skills/ai-security/ai-pii-redactor.md) |
| 4 | LLM Evaluation Harness Builder | Advanced | This Codex skill builds an evaluation harness for an LLM application: test cases for accuracy, safety, fairness, robustn… | [`skills/ai-security/llm-evaluation-harness-builder.md`](../skills/ai-security/llm-evaluation-harness-builder.md) |
| 5 | LLM Output Filter Designer | Intermediate | This Codex skill designs output filters for an LLM application: content moderation (toxicity, PII, regulated content), f… | [`skills/ai-security/llm-output-filter-designer.md`](../skills/ai-security/llm-output-filter-designer.md) |
| 6 | Model Drift Monitor | Advanced | This Codex skill designs a monitoring system for ML model drift: input drift (feature distribution shift), output drift … | [`skills/ai-security/model-drift-monitor.md`](../skills/ai-security/model-drift-monitor.md) |
| 7 | Prompt Injection Tester | Advanced | This Codex skill tests an LLM application for prompt injection vulnerabilities: direct injection (user input overrides s… | [`skills/ai-security/prompt-injection-tester.md`](../skills/ai-security/prompt-injection-tester.md) |
| 8 | RAG Source Trust Evaluator | Advanced | This Codex skill evaluates the trustworthiness of retrieval sources in a RAG pipeline: source provenance, freshness, con… | [`skills/ai-security/rag-source-trust-evaluator.md`](../skills/ai-security/rag-source-trust-evaluator.md) |
| 9 | Vector DB Security Auditor | Advanced | This Codex skill audits a vector database (Pinecone, Weaviate, Milvus, pgvector) for security: authentication, authoriza… | [`skills/ai-security/vector-db-security-auditor.md`](../skills/ai-security/vector-db-security-auditor.md) |

## ⚙️ DevOps & Engineering Practice

_Ship safer and faster: CI optimization, container hardening, observability, architecture, and docs._

**26 skills** · Capabilities: CI optimization, container hardening, observability, architecture rules, engineering docs

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | API Contract Diff Reviewer | Intermediate | This Codex skill diffs an OpenAPI, Protobuf, or GraphQL schema against the previous version and classifies each change a… | [`skills/devops/api-contract-diff-reviewer.md`](../skills/devops/api-contract-diff-reviewer.md) |
| 2 | API Documentation Generator | Intermediate | This Codex skill generates API documentation from an OpenAPI, Protobuf, or GraphQL contract: endpoint reference, request… | [`skills/devops/api-doc-generator.md`](../skills/devops/api-doc-generator.md) |
| 3 | Architecture Decision Record Author | Intermediate | This Codex skill authors Architecture Decision Records (ADRs) for significant technical decisions: context, decision, co… | [`skills/devops/architecture-decision-record-author.md`](../skills/devops/architecture-decision-record-author.md) |
| 4 | Architecture Rule Checker | Intermediate | This Codex skill enforces architectural layering rules: domain layer must not depend on infrastructure, controllers must… | [`skills/devops/architecture-rule-checker.md`](../skills/devops/architecture-rule-checker.md) |
| 5 | Argo Workflow Generator | Intermediate | This Codex skill generates Argo Workflow YAML for batch, ETL, and ML pipelines with retry strategies, artifact passing, … | [`skills/devops/argo-workflow-generator.md`](../skills/devops/argo-workflow-generator.md) |
| 6 | Blue-Green Deploy Planner | Intermediate | This Codex skill designs a blue-green deployment strategy for a service: environment setup, traffic switch mechanism, he… | [`skills/devops/blue-green-deploy-planner.md`](../skills/devops/blue-green-deploy-planner.md) |
| 7 | Chaos Experiment Designer | Advanced | This Codex skill designs chaos engineering experiments: hypothesis, blast radius, steady-state definition, injection act… | [`skills/devops/chaos-experiment-designer.md`](../skills/devops/chaos-experiment-designer.md) |
| 8 | CI Pipeline Optimizer | Intermediate | This Codex skill analyzes a CI pipeline (GitHub Actions, GitLab CI, CircleCI) and produces an optimization plan: caching… | [`skills/devops/ci-pipeline-optimizer.md`](../skills/devops/ci-pipeline-optimizer.md) |
| 9 | Code Smell Detector | Intermediate | This Codex skill identifies code smells — long methods, deep nesting, feature envy, primitive obsession, god classes, sh… | [`skills/devops/code-smell-detector.md`](../skills/devops/code-smell-detector.md) |
| 10 | Cost Optimization Analyzer | Intermediate | This Codex skill analyzes a cloud deployment's cost drivers: oversized compute instances, idle load balancers, over-prov… | [`skills/devops/cost-optimization-analyzer.md`](../skills/devops/cost-optimization-analyzer.md) |
| 11 | Developer Onboarding Doc Author | Intermediate | This Codex skill authors a developer onboarding document: environment setup, codebase tour, first PR guide, common pitfa… | [`skills/devops/developer-onboarding-doc-author.md`](../skills/devops/developer-onboarding-doc-author.md) |
| 12 | Diagram Generator | Intermediate | This Codex skill generates architecture and sequence diagrams from a codebase or written description: system context, co… | [`skills/devops/diagram-generator.md`](../skills/devops/diagram-generator.md) |
| 13 | DNS Config Auditor | Intermediate | This Codex skill audits DNS configuration for security and reliability: DNSSEC, CAA records (to restrict certificate aut… | [`skills/devops/dns-config-auditor.md`](../skills/devops/dns-config-auditor.md) |
| 14 | Dockerfile Hardener | Intermediate | This Codex skill rewrites Dockerfiles to follow container security best practices: multi-stage builds, distroless or alp… | [`skills/devops/dockerfile-hardener.md`](../skills/devops/dockerfile-hardener.md) |
| 15 | Glossary Builder | Intermediate | This Codex skill builds a project glossary: domain terms, acronyms, codebase-specific names, and their definitions. | [`skills/devops/glossary-builder.md`](../skills/devops/glossary-builder.md) |
| 16 | Helm Chart Auditor | Intermediate | This Codex skill reviews Helm charts for security and reliability: values.yaml defaults (privileged securityContext, pub… | [`skills/devops/helm-chart-auditor.md`](../skills/devops/helm-chart-auditor.md) |
| 17 | Incident Runbook Generator | Intermediate | This Codex skill generates a per-service incident runbook from the service's observability signals, dependencies, and kn… | [`skills/devops/incident-runbook-generator.md`](../skills/devops/incident-runbook-generator.md) |
| 18 | Kubernetes Manifest Linter | Intermediate | This Codex skill reviews Kubernetes manifests (Deployment, Service, Ingress, ConfigMap, Secret) against security and rel… | [`skills/devops/kubernetes-manifest-linter.md`](../skills/devops/kubernetes-manifest-linter.md) |
| 19 | Migration Reviewer | Intermediate | This Codex skill reviews database migrations for safety: backward compatibility with running app versions, idempotency, … | [`skills/devops/migration-reviewer.md`](../skills/devops/migration-reviewer.md) |
| 20 | Monitoring Alert Tuner | Intermediate | This Codex skill reviews existing alerts and tunes them for precision (low false positives) and recall (low false negati… | [`skills/devops/monitoring-alert-tuner.md`](../skills/devops/monitoring-alert-tuner.md) |
| 21 | Naming Convention Enforcer | Intermediate | This Codex skill audits identifiers against the project's naming conventions and produces safe-rename patches: variables… | [`skills/devops/naming-convention-enforcer.md`](../skills/devops/naming-convention-enforcer.md) |
| 22 | Observability Bootstrap | Intermediate | This Codex skill bootstraps the three pillars of observability — structured logging, metrics, and distributed tracing — … | [`skills/devops/observability-bootstrap.md`](../skills/devops/observability-bootstrap.md) |
| 23 | README Auditor | Beginner | This Codex skill audits a project's README for completeness: project description, installation, usage, configuration, te… | [`skills/devops/readme-auditor.md`](../skills/devops/readme-auditor.md) |
| 24 | Secrets Rotation Planner | Intermediate | This Codex skill designs a rotation plan for a service's secrets (database passwords, API keys, signing keys) that suppo… | [`skills/devops/secrets-rotation-planner.md`](../skills/devops/secrets-rotation-planner.md) |
| 25 | SSL/TLS Certificate Rotator | Intermediate | This Codex skill designs a certificate rotation plan for HTTPS endpoints, mTLS services, and internal PKI: identifies ex… | [`skills/devops/ssl-tls-certificate-rotator.md`](../skills/devops/ssl-tls-certificate-rotator.md) |
| 26 | Terraform Plan Reviewer | Advanced | This Codex skill reviews a Terraform plan output to identify risky changes: resource destruction, replacement (force-new… | [`skills/devops/terraform-plan-reviewer.md`](../skills/devops/terraform-plan-reviewer.md) |

## 🧪 Testing

_Build the testing pyramid: unit, integration, load, mutation, fuzz, contract, E2E, security._

**10 skills** · Capabilities: unit, integration, load, fuzz, contract, E2E, security test planning

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Contract Test Generator | Intermediate | This Codex skill generates contract tests for an API: verifies the server's response matches the OpenAPI/Protobuf contra… | [`skills/testing/contract-test-generator.md`](../skills/testing/contract-test-generator.md) |
| 2 | E2E Test Designer | Intermediate | This Codex skill designs end-to-end tests that verify a user flow through the application: login -> navigate -> perform … | [`skills/testing/e2e-test-designer.md`](../skills/testing/e2e-test-designer.md) |
| 3 | Fuzz Test Harness Builder | Advanced | This Codex skill builds a fuzz test harness for a parser, deserializer, or protocol handler: defines the input corpus, t… | [`skills/testing/fuzz-test-harness-builder.md`](../skills/testing/fuzz-test-harness-builder.md) |
| 4 | Integration Test Designer | Intermediate | This Codex skill designs integration tests that verify multiple components work together: API endpoint to database, queu… | [`skills/testing/integration-test-designer.md`](../skills/testing/integration-test-designer.md) |
| 5 | Load Test Planner | Advanced | This Codex skill designs a load test: defines the workload model (read/write ratio, request mix), the load profile (ramp… | [`skills/testing/load-test-planner.md`](../skills/testing/load-test-planner.md) |
| 6 | Mutation Test Runner | Advanced | This Codex skill runs mutation testing on a codebase to evaluate test suite quality: introduces small code mutations (ch… | [`skills/testing/mutation-test-runner.md`](../skills/testing/mutation-test-runner.md) |
| 7 | Regression Test Prioritizer | Intermediate | This Codex skill analyzes a PR diff and selects the subset of existing tests most likely to catch regressions caused by … | [`skills/testing/regression-test-prioritizer.md`](../skills/testing/regression-test-prioritizer.md) |
| 8 | Security Test Planner | Intermediate | This Codex skill designs a security test plan: SAST, SCA, secret scanning, DAST, IAST, and penetration testing scope. | [`skills/testing/security-test-planner.md`](../skills/testing/security-test-planner.md) |
| 9 | Test Data Faker | Beginner | This Codex skill generates realistic but fake test data for an application: users, orders, payments, products. | [`skills/testing/test-data-faker.md`](../skills/testing/test-data-faker.md) |
| 10 | Unit Test Generator | Beginner | This Codex skill generates unit tests for a target function or class: identifies branches, generates inputs that cover e… | [`skills/testing/unit-test-generator.md`](../skills/testing/unit-test-generator.md) |

## 🐙 GitHub Automation

_Automate the GitHub lifecycle: Actions, releases, branch protection, Dependabot, OIDC, secret scanning._

**14 skills** · Capabilities: Actions workflows, release automation, branch protection, OIDC federation, secret scanning

| # | Skill | Difficulty | Summary | File |
|---|-------|------------|---------|------|
| 1 | Changelog Generator | Beginner | This Codex skill generates a changelog from git history and PR metadata: groups changes by type (Added, Changed, Fixed, … | [`skills/github-automation/changelog-generator.md`](../skills/github-automation/changelog-generator.md) |
| 2 | GitHub Actions Workflow Author | Intermediate | This Codex skill authors a GitHub Actions workflow YAML for a CI/CD pipeline: triggers, jobs, steps, caching, secrets, e… | [`skills/github-automation/github-actions-workflow-author.md`](../skills/github-automation/github-actions-workflow-author.md) |
| 3 | GitHub Branch Protection Designer | Intermediate | This Codex skill designs branch protection rules for a repository: required reviews, required status checks, required li… | [`skills/github-automation/github-branch-protection-designer.md`](../skills/github-automation/github-branch-protection-designer.md) |
| 4 | GitHub CODEOWNERS Generator | Beginner | This Codex skill generates or updates the CODEOWNERS file: maps directories and file patterns to the responsible teams o… | [`skills/github-automation/github-codeowners-generator.md`](../skills/github-automation/github-codeowners-generator.md) |
| 5 | GitHub Dependabot Configurator | Beginner | This Codex skill configures Dependabot for a repository: dependency ecosystems, update schedule, grouping, reviewers, as… | [`skills/github-automation/github-dependabot-configurator.md`](../skills/github-automation/github-dependabot-configurator.md) |
| 6 | GitHub Discussion Category Setup | Beginner | This Codex skill sets up GitHub Discussions categories for a repo: Q&A, ideas, show-and-tell, announcements — with templ… | [`skills/github-automation/github-discussion-category-setup.md`](../skills/github-automation/github-discussion-category-setup.md) |
| 7 | GitHub Issue Triage Bot | Intermediate | This Codex skill designs a GitHub Actions bot that triages new issues: applies labels based on content, requests more in… | [`skills/github-automation/github-issue-triage-bot.md`](../skills/github-automation/github-issue-triage-bot.md) |
| 8 | GitHub OIDC Cloud Federation Setup | Intermediate | This Codex skill sets up OIDC federation between GitHub Actions and a cloud provider (AWS, GCP, Azure) so workflows can … | [`skills/github-automation/github-oidc-cloud-federation-setup.md`](../skills/github-automation/github-oidc-cloud-federation-setup.md) |
| 9 | GitHub Pages Deploy Setup | Beginner | This Codex skill sets up a GitHub Actions workflow to build and deploy a static site (docs, blog, landing page) to GitHu… | [`skills/github-automation/github-pages-deploy-setup.md`](../skills/github-automation/github-pages-deploy-setup.md) |
| 10 | GitHub PR Template Author | Beginner | This Codex skill authors PR templates (.github/PULL_REQUEST_TEMPLATE.md and multi-template variants) that capture the in… | [`skills/github-automation/github-pr-template-author.md`](../skills/github-automation/github-pr-template-author.md) |
| 11 | GitHub Release Automator | Intermediate | This Codex skill automates the GitHub release process: tag creation, release notes generation, asset upload, and the rel… | [`skills/github-automation/github-release-automator.md`](../skills/github-automation/github-release-automator.md) |
| 12 | GitHub Repo Migrator | Intermediate | This Codex skill migrates a repo from one GitHub org to another (or from another platform): clones the source, preserves… | [`skills/github-automation/github-repo-migrator.md`](../skills/github-automation/github-repo-migrator.md) |
| 13 | GitHub Repo Settings Auditor | Intermediate | This Codex skill audits a GitHub repo's settings for security and consistency: visibility, default branch, branch protec… | [`skills/github-automation/github-repo-settings-auditor.md`](../skills/github-automation/github-repo-settings-auditor.md) |
| 14 | GitHub Secret Scanning Configurator | Intermediate | This Codex skill configures GitHub's secret scanning and push protection for a repository: enables scanning, configures … | [`skills/github-automation/github-secret-scanning-configurator.md`](../skills/github-automation/github-secret-scanning-configurator.md) |
