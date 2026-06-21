---
id: <kebab-case-workflow-id>
name: <Workflow Name>
purpose: <one-sentence purpose>
skills:
  - <skill-id-1>
  - <skill-id-2>
  - <skill-id-3>
---

# <Workflow Name>

## Goal

One paragraph describing what this multi-skill workflow accomplishes. Who is it for? When should they run it? What's the output?

## Skills Used

1. **[`<skill-id-1>`](../skills/<category>/<skill-id-1>.md)** — what it contributes to the workflow.
2. **[`<skill-id-2>`](../skills/<category>/<skill-id-2>.md)** — what it contributes.
3. **[`<skill-id-3>`](../skills/<category>/<skill-id-3>.md)** — what it contributes.

## Inputs

- Input 1 (e.g., repository path)
- Input 2 (e.g., target environment)
- Input 3 (e.g., compliance scope)

## Steps

1. **Step 1 — <action>.** Activate skill `<skill-id-1>`. Provide inputs X, Y, Z. Capture the output to `<artifact-1>.md`.
2. **Step 2 — <action>.** Activate skill `<skill-id-2>`. Use `<artifact-1>.md` as input. Capture the output to `<artifact-2>.md`.
3. **Step 3 — <action>.** Activate skill `<skill-id-3>`. Combine `<artifact-1>` and `<artifact-2>`. Produce the final deliverable.

## Expected Output

Describe the final deliverable. What does the user get at the end of the workflow?

## Example Invocation

> Run the <workflow-name> workflow on this repository: <repo-path>. Target environment: <env>. Compliance scope: <PCI | SOC 2 | GDPR | none>. Produce the final report at <output-path>.

## Safety Notes

- Any safety considerations specific to this workflow (e.g., "do not run destructive steps without explicit approval").
