# Forensic Snapshot Collector

## Purpose

This Codex skill orchestrates the collection of forensic snapshots during a security incident: disk images, memory dumps, network captures, log bundles, and database snapshots. It preserves evidence before the attacker can destroy it or before a rebuild loses it.

## When to Use

Use during an active security incident (suspected compromise, ransomware, insider threat), before isolating or rebuilding affected systems.

## Codex Instructions

1. Identify the affected systems: instances, containers, databases, accounts.
2. For each system, capture a disk snapshot (EBS snapshot, GCP disk image, Azure disk snapshot) before any change.
3. For each running system, capture a memory dump (LIME for Linux, WinPmem for Windows) if the system is still running.
4. Capture a network capture (tcpdump, packet capture) for the affected subnet if the incident is network-based.
5. Bundle the relevant logs: CloudTrail, VPC Flow Logs, application logs, OS logs — to a secure S3 bucket with a tamper-evident hash.
6. Capture a database snapshot (RDS snapshot, self-managed pg_dump) before any cleanup.
7. Document the chain of custody: who collected what, when, with what tool, stored where.
8. Store all snapshots in a forensic bucket with strict IAM (only the IR team), encryption, and object lock (WORM).
9. Verify the snapshots are complete (size matches expected) and compute SHA-256 hashes for integrity.
10. Output a forensic collection report with the inventory, chain of custody, and verification hashes.

## Inputs Needed

- Affected systems inventory
- Cloud provider and snapshot capabilities
- Forensic storage bucket with object lock
- IR team's IAM role for snapshot creation
- Chain of custody template

## Expected Output

A Markdown forensic collection report with: (1) Snapshot Inventory — System | Snapshot ID | Type | Timestamp | Hash; (2) Chain of Custody log; (3) Storage location with IAM policy; (4) Verification hashes (SHA-256).

## Example Prompt

> Collect forensic snapshots for the suspected compromise of EC2 instance i-abc123 and RDS instance db-xyz. Capture EBS snapshot, memory dump (if running), CloudTrail and VPC Flow Logs for the last 24 hours, and an RDS snapshot. Store in our forensic bucket s3://ir-forensics with object lock. Document chain of custody.

## Safety Rules

- Never reboot or rebuild a system before snapshots are captured — evidence will be lost.
- Do not access the affected system's shell directly — use a jump host with logging.
- Stop and ask the user if a snapshot's storage location is not configured for object lock.
- If the incident involves law enforcement, follow the chain-of-custody requirements they specify.
- Never log credentials or secrets found in memory dumps or disk snapshots — redact.
- If the snapshot collection reveals additional affected systems, expand the scope immediately.
