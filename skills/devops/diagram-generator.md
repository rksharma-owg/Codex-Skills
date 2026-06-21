---
id: diagram-generator
name: Diagram Generator
category: devops
difficulty: Intermediate
tags:
  - devops
summary: |
  This Codex skill generates architecture and sequence diagrams from a codebase or written description: system context, container, component, deployment, and sequence diagrams using Mermaid, PlantUML, or Structurizr.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill generates architecture and sequence diagrams from a codebase or written description: system context, container, component, deployment, and sequence diagrams using Mermaid, PlantUML, or Structurizr.

## When to Use

Use when authoring architecture docs, when onboarding engineers need a visual, after a refactor that changed the architecture, or before a design review.

## Codex Instructions

1. Identify the diagram type: system context (high-level), container (services), component (within a service), deployment (infra), sequence (request flow).
2. Choose the tool: Mermaid (Markdown-embeddable), PlantUML (more powerful), Structurizr (model-as-code).
3. For a system context diagram, identify the system, external users, and external systems; draw the trust boundaries.
4. For a container diagram, identify each service, database, queue; draw the dependencies and the data flow.
5. For a component diagram, identify the internal modules of a service and their dependencies.
6. For a deployment diagram, identify the infrastructure (VPC, subnets, clusters, nodes) and where each container runs.
7. For a sequence diagram, identify the actors and the messages exchanged in a specific flow (e.g., user checkout).
8. Use the project's conventions for colors (e.g., green for external, blue for internal).
9. Embed the diagram in the Markdown doc using the chosen tool's syntax (Mermaid code blocks for Mermaid).
10. Output the diagrams as code blocks in Markdown, ready to render in the docs site.

## Inputs Needed

- Diagram type and scope
- Source (codebase, written description, or both)
- Diagram tool (Mermaid, PlantUML, Structurizr)
- Project's diagram conventions (colors, naming)
- Docs site that will render the diagrams

## Expected Output

Diagram source code (Mermaid/PlantUML/Structurizr) embedded in a Markdown doc, ready to render. Plus a brief textual description of each diagram for accessibility.

## Example Prompt

> Generate a system context diagram and a container diagram for our e-commerce platform. System context: customers, web app, mobile app, payment gateway, shipping API. Container diagram: web frontend, mobile BFF, product service, order service, payment service, Postgres, Kafka. Use Mermaid. Embed in docs/architecture.md.

## Safety Rules

- Never include internal hostnames or IP addresses in a diagram that may be published externally.
- Do not document a flow that does not exist yet (planned features) without a 'Planned' label.
- Stop and ask the user if a component's classification (internal vs external) is ambiguous.
- If the diagram references a third-party service, verify the data-sharing agreement allows it.
- Never include customer data flow in a public diagram — abstract it.
- If the diagram is for a compliance audit, verify it matches the actual implementation.
