# Codex Agent Skills

A curated, opinionated library of **121 production-ready Codex agent skills** for developers, security engineers, AI builders, DevOps teams, product teams, and automation workflows. Each skill is a standalone Markdown file that documents a discrete capability Codex (or any LLM-based coding agent) can be invoked to perform, with concrete instructions, inputs, expected output, an example prompt, and safety rules.

## What is a Codex Agent Skill?

A Codex agent skill is a reusable prompt artifact that turns a vague request — "audit this repo for secret leaks" — into a structured, predictable, safe execution. Rather than re-deriving the analysis steps for every invocation, a skill pre-encodes the scope, the steps, the inputs, the output format, and the safety guardrails. When you point Codex at a skill file (or paste its contents into the system prompt), Codex follows the documented workflow instead of improvising.

This library is framework-agnostic: the skills are Markdown, so they work with OpenAI Codex, Claude Code, Cursor, Aider, Continue, or any agent that consumes Markdown. They are organized into 11 categories covering the full software-delivery lifecycle — from threat modeling to incident response, from CI optimization to compliance evidence collection.

## Repository Layout

```
codex-agent-skills/
├── README.md                  # this file
├── cybersecurity/
├── secure-coding/
├── devops/
├── cloud-security/
├── ai-security/
├── code-review/
├── testing/
├── documentation/
├── incident-response/
├── compliance/
├── github-automation/
```

Each skill file follows the same template:

```markdown
# <Skill Name>

## Purpose           # what the skill does and why it exists
## When to Use       # trigger conditions
## Codex Instructions # numbered steps Codex should follow
## Inputs Needed     # what the user must provide
## Expected Output   # the exact output structure
## Example Prompt    # a realistic prompt to paste into Codex
## Safety Rules      # hard guardrails for the skill
```

## Skill Index by Category

**Total skills: 122** across 11 categories.

### Cybersecurity (15 skills)

_Vulnerability hunting, secret detection, SAST triage, container/IaC scanning, OWASP Top 10 remediation, and runtime exploitation defense._

| # | Skill | File |
|---|-------|------|
| 1 | Authz Bypass Finder | [`cybersecurity/authz-bypass-finder.md`](./cybersecurity/authz-bypass-finder.md) |
| 2 | Crypto Usage Reviewer | [`cybersecurity/crypto-usage-reviewer.md`](./cybersecurity/crypto-usage-reviewer.md) |
| 3 | Dependency Vulnerability Auditor | [`cybersecurity/dependency-vulnerability-auditor.md`](./cybersecurity/dependency-vulnerability-auditor.md) |
| 4 | Deserialization Risk Finder | [`cybersecurity/deserialization-risk-finder.md`](./cybersecurity/deserialization-risk-finder.md) |
| 5 | Docker Image Scanner | [`cybersecurity/docker-image-scanner.md`](./cybersecurity/docker-image-scanner.md) |
| 6 | IaC Misconfig Detector | [`cybersecurity/iac-misconfig-detector.md`](./cybersecurity/iac-misconfig-detector.md) |
| 7 | JWT Validator | [`cybersecurity/jwt-validator.md`](./cybersecurity/jwt-validator.md) |
| 8 | OWASP Top 10 Remediator | [`cybersecurity/owasp-top-10-remediator.md`](./cybersecurity/owasp-top-10-remediator.md) |
| 9 | SAST Triage | [`cybersecurity/sast-triage.md`](./cybersecurity/sast-triage.md) |
| 10 | Secret Scanner | [`cybersecurity/secret-scanner.md`](./cybersecurity/secret-scanner.md) |
| 11 | Secrets in Logs Scrubber | [`cybersecurity/secrets-in-logs-scrubber.md`](./cybersecurity/secrets-in-logs-scrubber.md) |
| 12 | SQL Injection Finder | [`cybersecurity/sql-injection-finder.md`](./cybersecurity/sql-injection-finder.md) |
| 13 | SSRF Detector | [`cybersecurity/ssrf-detector.md`](./cybersecurity/ssrf-detector.md) |
| 14 | TLS Config Auditor | [`cybersecurity/tls-config-auditor.md`](./cybersecurity/tls-config-auditor.md) |
| 15 | XSS Finder | [`cybersecurity/xss-finder.md`](./cybersecurity/xss-finder.md) |

### Secure Coding (11 skills)

_Input validation, output encoding, parameterized queries, session management, password hashing, CSRF, file upload safety, race conditions, and dangerous-function replacement._

| # | Skill | File |
|---|-------|------|
| 1 | CSRF Token Generator | [`secure-coding/csrf-token-generator.md`](./secure-coding/csrf-token-generator.md) |
| 2 | Dangerous Function Replacer | [`secure-coding/dangerous-function-replacer.md`](./secure-coding/dangerous-function-replacer.md) |
| 3 | Error Message Sanitizer | [`secure-coding/error-message-sanitizer.md`](./secure-coding/error-message-sanitizer.md) |
| 4 | Input Validation Hardener | [`secure-coding/input-validation-hardener.md`](./secure-coding/input-validation-hardener.md) |
| 5 | Memory Safety Reviewer | [`secure-coding/memory-safety-reviewer.md`](./secure-coding/memory-safety-reviewer.md) |
| 6 | Output Encoding Helper | [`secure-coding/output-encoding-helper.md`](./secure-coding/output-encoding-helper.md) |
| 7 | Parameterized Query Generator | [`secure-coding/parameterized-query-generator.md`](./secure-coding/parameterized-query-generator.md) |
| 8 | Password Hashing Advisor | [`secure-coding/password-hashing-advisor.md`](./secure-coding/password-hashing-advisor.md) |
| 9 | Race Condition Finder | [`secure-coding/race-condition-finder.md`](./secure-coding/race-condition-finder.md) |
| 10 | Secure File Upload Handler | [`secure-coding/secure-file-upload-handler.md`](./secure-coding/secure-file-upload-handler.md) |
| 11 | Secure Session Manager | [`secure-coding/secure-session-manager.md`](./secure-coding/secure-session-manager.md) |

### DevOps (15 skills)

_CI/CD optimization, container hardening, Kubernetes/Terraform/Helm auditing, observability bootstrapping, runbooks, blue-green deploys, secrets rotation, and chaos engineering._

| # | Skill | File |
|---|-------|------|
| 1 | Argo Workflow Generator | [`devops/argo-workflow-generator.md`](./devops/argo-workflow-generator.md) |
| 2 | Blue-Green Deploy Planner | [`devops/blue-green-deploy-planner.md`](./devops/blue-green-deploy-planner.md) |
| 3 | Chaos Experiment Designer | [`devops/chaos-experiment-designer.md`](./devops/chaos-experiment-designer.md) |
| 4 | CI Pipeline Optimizer | [`devops/ci-pipeline-optimizer.md`](./devops/ci-pipeline-optimizer.md) |
| 5 | Cost Optimization Analyzer | [`devops/cost-optimization-analyzer.md`](./devops/cost-optimization-analyzer.md) |
| 6 | DNS Config Auditor | [`devops/dns-config-auditor.md`](./devops/dns-config-auditor.md) |
| 7 | Dockerfile Hardener | [`devops/dockerfile-hardener.md`](./devops/dockerfile-hardener.md) |
| 8 | Helm Chart Auditor | [`devops/helm-chart-auditor.md`](./devops/helm-chart-auditor.md) |
| 9 | Incident Runbook Generator | [`devops/incident-runbook-generator.md`](./devops/incident-runbook-generator.md) |
| 10 | Kubernetes Manifest Linter | [`devops/kubernetes-manifest-linter.md`](./devops/kubernetes-manifest-linter.md) |
| 11 | Monitoring Alert Tuner | [`devops/monitoring-alert-tuner.md`](./devops/monitoring-alert-tuner.md) |
| 12 | Observability Bootstrap | [`devops/observability-bootstrap.md`](./devops/observability-bootstrap.md) |
| 13 | Secrets Rotation Planner | [`devops/secrets-rotation-planner.md`](./devops/secrets-rotation-planner.md) |
| 14 | SSL/TLS Certificate Rotator | [`devops/ssl-tls-certificate-rotator.md`](./devops/ssl-tls-certificate-rotator.md) |
| 15 | Terraform Plan Reviewer | [`devops/terraform-plan-reviewer.md`](./devops/terraform-plan-reviewer.md) |

### Cloud Security (12 skills)

_AWS/Azure/GCP IAM and resource auditing, network segmentation, workload identity migration, multi-cloud inventory, backup/recovery planning, and certificate rotation._

| # | Skill | File |
|---|-------|------|
| 1 | AWS IAM Policy Auditor | [`cloud-security/aws-iam-policy-auditor.md`](./cloud-security/aws-iam-policy-auditor.md) |
| 2 | Azure Security Baseline Checker | [`cloud-security/azure-security-baseline-checker.md`](./cloud-security/azure-security-baseline-checker.md) |
| 3 | Cloud Backup Recovery Planner | [`cloud-security/cloud-backup-recovery-planner.md`](./cloud-security/cloud-backup-recovery-planner.md) |
| 4 | Cloud Network Segmentation Planner | [`cloud-security/cloud-network-segmentation-planner.md`](./cloud-security/cloud-network-segmentation-planner.md) |
| 5 | Cloud Secret Manager Migrator | [`cloud-security/cloud-secret-manager-migrator.md`](./cloud-security/cloud-secret-manager-migrator.md) |
| 6 | Cloud Workload Identity Migrator | [`cloud-security/cloud-workload-identity-migrator.md`](./cloud-security/cloud-workload-identity-migrator.md) |
| 7 | CloudTrail Forensics Helper | [`cloud-security/cloudtrail-forensics-helper.md`](./cloud-security/cloudtrail-forensics-helper.md) |
| 8 | GCP IAM Recommender | [`cloud-security/gcp-iam-recommender.md`](./cloud-security/gcp-iam-recommender.md) |
| 9 | GuardDuty Finding Triager | [`cloud-security/guardduty-finding-triager.md`](./cloud-security/guardduty-finding-triager.md) |
| 10 | Kubernetes NetworkPolicy Generator | [`cloud-security/kubernetes-network-policy-generator.md`](./cloud-security/kubernetes-network-policy-generator.md) |
| 11 | Multi-Cloud Inventory Builder | [`cloud-security/multi-cloud-inventory-builder.md`](./cloud-security/multi-cloud-inventory-builder.md) |
| 12 | S3 Bucket Policy Auditor | [`cloud-security/s3-bucket-policy-auditor.md`](./cloud-security/s3-bucket-policy-auditor.md) |

### AI Security (9 skills)

_Prompt-injection testing, RAG source trust evaluation, LLM output filtering, AI model supply-chain audits, agent tool gatekeeping, PII redaction, and drift monitoring._

| # | Skill | File |
|---|-------|------|
| 1 | AI Agent Tool Gatekeeper | [`ai-security/ai-agent-tool-gatekeeper.md`](./ai-security/ai-agent-tool-gatekeeper.md) |
| 2 | AI Model Supply Chain Auditor | [`ai-security/ai-model-supply-chain-auditor.md`](./ai-security/ai-model-supply-chain-auditor.md) |
| 3 | AI PII Redactor | [`ai-security/ai-pii-redactor.md`](./ai-security/ai-pii-redactor.md) |
| 4 | LLM Evaluation Harness Builder | [`ai-security/llm-evaluation-harness-builder.md`](./ai-security/llm-evaluation-harness-builder.md) |
| 5 | LLM Output Filter Designer | [`ai-security/llm-output-filter-designer.md`](./ai-security/llm-output-filter-designer.md) |
| 6 | Model Drift Monitor | [`ai-security/model-drift-monitor.md`](./ai-security/model-drift-monitor.md) |
| 7 | Prompt Injection Tester | [`ai-security/prompt-injection-tester.md`](./ai-security/prompt-injection-tester.md) |
| 8 | RAG Source Trust Evaluator | [`ai-security/rag-source-trust-evaluator.md`](./ai-security/rag-source-trust-evaluator.md) |
| 9 | Vector DB Security Auditor | [`ai-security/vector-db-security-auditor.md`](./ai-security/vector-db-security-auditor.md) |

### Code Review (9 skills)

_PR summaries, code-smell detection, complexity reduction, dead-code elimination, naming enforcement, architecture rule checks, migration reviews, and API contract diffs._

| # | Skill | File |
|---|-------|------|
| 1 | API Contract Diff Reviewer | [`code-review/api-contract-diff-reviewer.md`](./code-review/api-contract-diff-reviewer.md) |
| 2 | Architecture Rule Checker | [`code-review/architecture-rule-checker.md`](./code-review/architecture-rule-checker.md) |
| 3 | Code Smell Detector | [`code-review/code-smell-detector.md`](./code-review/code-smell-detector.md) |
| 4 | Complexity Reducer | [`code-review/complexity-reducer.md`](./code-review/complexity-reducer.md) |
| 5 | Dead Code Eliminator | [`code-review/dead-code-eliminator.md`](./code-review/dead-code-eliminator.md) |
| 6 | Migration Reviewer | [`code-review/migration-reviewer.md`](./code-review/migration-reviewer.md) |
| 7 | Naming Convention Enforcer | [`code-review/naming-convention-enforcer.md`](./code-review/naming-convention-enforcer.md) |
| 8 | PR Summary Writer | [`code-review/pr-summary-writer.md`](./code-review/pr-summary-writer.md) |
| 9 | Review Checklist Generator | [`code-review/review-checklist-generator.md`](./code-review/review-checklist-generator.md) |

### Testing (10 skills)

_Unit, integration, load, mutation, fuzz, contract, E2E, security test planning, regression prioritization, and realistic test data generation._

| # | Skill | File |
|---|-------|------|
| 1 | Contract Test Generator | [`testing/contract-test-generator.md`](./testing/contract-test-generator.md) |
| 2 | E2E Test Designer | [`testing/e2e-test-designer.md`](./testing/e2e-test-designer.md) |
| 3 | Fuzz Test Harness Builder | [`testing/fuzz-test-harness-builder.md`](./testing/fuzz-test-harness-builder.md) |
| 4 | Integration Test Designer | [`testing/integration-test-designer.md`](./testing/integration-test-designer.md) |
| 5 | Load Test Planner | [`testing/load-test-planner.md`](./testing/load-test-planner.md) |
| 6 | Mutation Test Runner | [`testing/mutation-test-runner.md`](./testing/mutation-test-runner.md) |
| 7 | Regression Test Prioritizer | [`testing/regression-test-prioritizer.md`](./testing/regression-test-prioritizer.md) |
| 8 | Security Test Planner | [`testing/security-test-planner.md`](./testing/security-test-planner.md) |
| 9 | Test Data Faker | [`testing/test-data-faker.md`](./testing/test-data-faker.md) |
| 10 | Unit Test Generator | [`testing/unit-test-generator.md`](./testing/unit-test-generator.md) |

### Documentation (8 skills)

_API docs, runbooks, ADRs, changelogs, README audits, onboarding docs, glossaries, and architecture diagrams._

| # | Skill | File |
|---|-------|------|
| 1 | API Documentation Generator | [`documentation/api-doc-generator.md`](./documentation/api-doc-generator.md) |
| 2 | Architecture Decision Record Author | [`documentation/architecture-decision-record-author.md`](./documentation/architecture-decision-record-author.md) |
| 3 | Changelog Generator | [`documentation/changelog-generator.md`](./documentation/changelog-generator.md) |
| 4 | Developer Onboarding Doc Author | [`documentation/developer-onboarding-doc-author.md`](./documentation/developer-onboarding-doc-author.md) |
| 5 | Diagram Generator | [`documentation/diagram-generator.md`](./documentation/diagram-generator.md) |
| 6 | Glossary Builder | [`documentation/glossary-builder.md`](./documentation/glossary-builder.md) |
| 7 | README Auditor | [`documentation/readme-auditor.md`](./documentation/readme-auditor.md) |
| 8 | Runbook Author | [`documentation/runbook-author.md`](./documentation/runbook-author.md) |

### Incident Response (10 skills)

_Severity classification, RCA, timeline building, comms drafting, postmortems, forensic snapshot collection, malware triage, and credential-compromise response._

| # | Skill | File |
|---|-------|------|
| 1 | Compromised Credential Responder | [`incident-response/ compromised-credential-responder.md`](./incident-response/ compromised-credential-responder.md) |
| 2 | Forensic Snapshot Collector | [`incident-response/forensic-snapshot-collector.md`](./incident-response/forensic-snapshot-collector.md) |
| 3 | Incident Comms Drafter | [`incident-response/incident-comms-drafter.md`](./incident-response/incident-comms-drafter.md) |
| 4 | Incident Severity Classifier | [`incident-response/incident-severity-classifier.md`](./incident-response/incident-severity-classifier.md) |
| 5 | Incident Timeline Builder | [`incident-response/incident-timeline-builder.md`](./incident-response/incident-timeline-builder.md) |
| 6 | IR Runbook Index Builder | [`incident-response/ir-runbook-index-builder.md`](./incident-response/ir-runbook-index-builder.md) |
| 7 | IR Tabletop Exercise Designer | [`incident-response/ir-tabletop-exercise-designer.md`](./incident-response/ir-tabletop-exercise-designer.md) |
| 8 | Malware Triage Analyzer | [`incident-response/malware-triage-analyzer.md`](./incident-response/malware-triage-analyzer.md) |
| 9 | Postmortem Author | [`incident-response/postmortem-author.md`](./incident-response/postmortem-author.md) |
| 10 | Root Cause Analyzer | [`incident-response/root-cause-analyzer.md`](./incident-response/root-cause-analyzer.md) |

### Compliance (10 skills)

_PCI DSS scope mapping, GDPR data flow, SOC 2 control mapping, HIPAA PHI handling, ISO 27001 implementation, access reviews, retention enforcement, audit log architecture, vendor risk, and DSAR response._

| # | Skill | File |
|---|-------|------|
| 1 | Access Review Orchestrator | [`compliance/access-review-orchestrator.md`](./compliance/access-review-orchestrator.md) |
| 2 | Audit Log Architect | [`compliance/audit-log-architect.md`](./compliance/audit-log-architect.md) |
| 3 | Data Retention Policy Enforcer | [`compliance/data-retention-policy-enforcer.md`](./compliance/data-retention-policy-enforcer.md) |
| 4 | DSAR Responder | [`compliance/dsar-responder.md`](./compliance/dsar-responder.md) |
| 5 | GDPR Data Flow Mapper | [`compliance/gdpr-data-flow-mapper.md`](./compliance/gdpr-data-flow-mapper.md) |
| 6 | HIPAA PHI Handler | [`compliance/hipaa-phi-handler.md`](./compliance/hipaa-phi-handler.md) |
| 7 | ISO 27001 Control Implementer | [`compliance/iso-27001-control-implementer.md`](./compliance/iso-27001-control-implementer.md) |
| 8 | PCI DSS Scope Mapper | [`compliance/pci-dss-scope-mapper.md`](./compliance/pci-dss-scope-mapper.md) |
| 9 | SOC 2 Control Mapper | [`compliance/soc2-control-mapper.md`](./compliance/soc2-control-mapper.md) |
| 10 | Vendor Risk Assessor | [`compliance/vendor-risk-assessor.md`](./compliance/vendor-risk-assessor.md) |

### GitHub Automation (13 skills)

_Actions workflows, release automation, PR templates, CODEOWNERS, branch protection, Dependabot, OIDC cloud federation, repo settings audits, issue triage bots, Discussions setup, Pages deploys, secret scanning, and repo migrations._

| # | Skill | File |
|---|-------|------|
| 1 | GitHub Actions Workflow Author | [`github-automation/github-actions-workflow-author.md`](./github-automation/github-actions-workflow-author.md) |
| 2 | GitHub Branch Protection Designer | [`github-automation/github-branch-protection-designer.md`](./github-automation/github-branch-protection-designer.md) |
| 3 | GitHub CODEOWNERS Generator | [`github-automation/github-codeowners-generator.md`](./github-automation/github-codeowners-generator.md) |
| 4 | GitHub Dependabot Configurator | [`github-automation/github-dependabot-configurator.md`](./github-automation/github-dependabot-configurator.md) |
| 5 | GitHub Discussion Category Setup | [`github-automation/github-discussion-category-setup.md`](./github-automation/github-discussion-category-setup.md) |
| 6 | GitHub Issue Triage Bot | [`github-automation/github-issue-triage-bot.md`](./github-automation/github-issue-triage-bot.md) |
| 7 | GitHub OIDC Cloud Federation Setup | [`github-automation/github-oidc-cloud-federation-setup.md`](./github-automation/github-oidc-cloud-federation-setup.md) |
| 8 | GitHub Pages Deploy Setup | [`github-automation/github-pages-deploy-setup.md`](./github-automation/github-pages-deploy-setup.md) |
| 9 | GitHub PR Template Author | [`github-automation/github-pr-template-author.md`](./github-automation/github-pr-template-author.md) |
| 10 | GitHub Release Automator | [`github-automation/github-release-automator.md`](./github-automation/github-release-automator.md) |
| 11 | GitHub Repo Migrator | [`github-automation/github-repo-migrator.md`](./github-automation/github-repo-migrator.md) |
| 12 | GitHub Repo Settings Auditor | [`github-automation/github-repo-settings-auditor.md`](./github-automation/github-repo-settings-auditor.md) |
| 13 | GitHub Secret Scanning Configurator | [`github-automation/github-secret-scanning-configurator.md`](./github-automation/github-secret-scanning-configurator.md) |

## How to Use a Skill

1. **Browse the index above** and pick the skill that matches your task.
2. **Open the file** and read `## Purpose` and `## When to Use` to confirm it fits.
3. **Provide the inputs** listed under `## Inputs Needed` — repository path, scope, target environment, etc.
4. **Paste the file contents into your agent** (Codex system prompt, Claude Code `/skill` command, Cursor rules file, etc.) or invoke it via your agent's skill-loading mechanism.
5. **Use the Example Prompt** under `## Example Prompt` as a starting point, customizing the path/scope to your situation.
6. **Honor the Safety Rules** — they are written to prevent the most common failure modes for each skill (production data loss, secret exposure, scope creep, compliance violations).

## Combining Skills

Most real-world work chains multiple skills. A few common chains:

- **Pre-merge security gate:** `secret-scanner` → `dependency-vulnerability-auditor` → `sast-triage` → `owasp-top-10-remediator`
- **Incident response:** `incident-severity-classifier` → `incident-timeline-builder` → `forensic-snapshot-collector` → `root-cause-analyzer` → `postmortem-author`
- **Cloud hardening:** `aws-iam-policy-auditor` → `s3-bucket-policy-auditor` → `cloud-network-segmentation-planner` → `cloud-workload-identity-migrator`
- **AI feature launch:** `prompt-injection-tester` → `llm-output-filter-designer` → `rag-source-trust-evaluator` → `ai-agent-tool-gatekeeper` → `llm-evaluation-harness-builder`
- **Compliance audit prep:** `pci-dss-scope-mapper` → `soc2-control-mapper` → `access-review-orchestrator` → `audit-log-architect`
- **CI/CD modernization:** `ci-pipeline-optimizer` → `github-oidc-cloud-federation-setup` → `github-secret-scanning-configurator` → `github-branch-protection-designer`

## Contributing

Contributions are welcome. To add a new skill:

1. Pick the right category folder (or propose a new one in an issue).
2. Copy an existing skill file as a template — keep all eight sections.
3. Write substantive content (target 250–500 words of body per file). Reference real tools, standards, CWE IDs, or framework names. Avoid placeholders.
4. Verify the skill is distinct from existing ones — no near-duplicates.
5. Update this README's skill index for the affected category.
6. Open a PR with the title `Add <skill name> skill`.

## License

Released under the MIT License. See [LICENSE](./LICENSE) for details. Use these skills freely in personal, commercial, or open-source projects. Attribution is appreciated but not required.

## Maintainer

Curated by **Rajesh Sharma** (`rajesh.sharma@owasp.org`). Issues and PRs welcome on the [GitHub repository](https://github.com/rksharma-owg/Codex-Skills).
