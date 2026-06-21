---
id: pci-dss-scope-mapper
name: PCI DSS Scope Mapper
category: cloud-security
difficulty: Advanced
tags:
  - cloud-security
  - pci
summary: |
  This Codex skill maps an application's architecture to PCI DSS scope: identifies the cardholder data environment (CDE), the systems that touch cardholder data, and the systems that can affect the CDE.
last_reviewed: 2026-06-21
---

## Purpose

This Codex skill maps an application's architecture to PCI DSS scope: identifies the cardholder data environment (CDE), the systems that touch cardholder data, and the systems that can affect the CDE. It targets the failure mode of an over-scoped or under-scoped PCI environment.

## When to Use

Use when launching a payment feature, before a PCI audit, after a major architecture change, or when reducing PCI scope by isolating the CDE.

## Codex Instructions

1. Inventory all systems: services, databases, queues, caches, log aggregators.
2. For each system, determine if it stores, processes, or transmits cardholder data (CHD).
3. Systems that touch CHD are in the CDE; systems that can affect the CDE (e.g., shared auth, shared monitoring) are connected systems.
4. Map the data flow: how CHD enters, where it is stored, how it is transmitted, where it is deleted.
5. Identify scope-reduction opportunities: tokenization (replace CHD with a token outside the CDE), network segmentation (isolate the CDE).
6. Verify the segmentation: a packet capture from a non-CDE system cannot reach a CDE system.
7. Document the scope in a PCI scope diagram, ready for the QSA's review.
8. Identify the PCI controls applicable to each in-scope system: encryption, access control, logging, vuln scanning.
9. Flag systems that are over-scoped (in scope but should not be) and propose scope reduction.
10. Output the PCI scope map and the control applicability matrix.

## Inputs Needed

- Application architecture diagram
- Data flow diagram for payment processing
- Network segmentation design
- Existing PCI controls documentation
- QSA's prior year report (if available)

## Expected Output

A Markdown PCI Scope Report with: (1) CDE Inventory; (2) Connected Systems; (3) Data Flow Diagram; (4) Scope Reduction Opportunities; (5) Control Applicability Matrix.

## Example Prompt

> Map PCI scope for our e-commerce platform. Architecture: web frontend, checkout service, payment service (talks to Stripe), order service, Postgres, Kafka, ELK. Identify the CDE, connected systems, and propose scope reduction via tokenization and network segmentation. Document for our QSA review.

## Safety Rules

- Never reduce PCI scope without QSA approval — under-scoping can result in audit failure.
- Do not store CHD outside the CDE to 'simplify' — that widens scope.
- Stop and ask the user if a system's CHD handling is ambiguous — assume in scope until verified.
- If the scope map reveals CHD in logs, plan to redact or purge immediately.
- Never log full PAN (card number) — log only the last 4 and a hash.
- If the scope reduction requires a new vendor (tokenization provider), verify their PCI compliance.
