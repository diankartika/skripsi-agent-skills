# Heuristic Evaluation Skill

## Purpose

Evaluate a user interface for usability problems using Nielsen's
10 Usability Heuristics.

The evaluation must be evidence-based and grounded in observable
interface characteristics.

## When to Use

Use this skill when the task involves:

- heuristic evaluation
- usability audit
- UI critique
- usability problem identification
- Nielsen heuristic evaluation

## Required Input

The evaluator may receive:

- UI screenshot
- rendered webpage
- webpage URL
- interface code
- user flow or task context

When multiple inputs are available, prioritize direct visual
evidence from the rendered interface.

## Evaluation Procedure

Follow these steps for every interface.

### Step 1 — Inspect the Interface

Identify observable:

- navigation elements
- interactive components
- content hierarchy
- labels and terminology
- system feedback
- forms and input controls
- error handling
- consistency between components
- accessibility-relevant characteristics

Do not assume behavior that cannot be established from the
provided evidence.

### Step 2 — Identify Potential Problems

For each observable problem:

1. Describe what is observed.
2. Identify the affected user interaction or task.
3. Determine the relevant usability heuristic.
4. Explain why the observation represents a heuristic violation.
5. Determine the severity.
6. Propose an actionable recommendation.

### Step 3 — Validate the Finding

Before reporting a finding, verify:

- Is the problem observable?
- Is the heuristic mapping justified?
- Is there sufficient evidence?
- Is the severity consistent with the severity criteria?

Do not report a finding solely because a design differs from
personal preference.

### Step 4 — Produce Findings

Each finding must contain:

- finding ID
- heuristic
- observation
- evidence
- explanation
- severity
- recommendation

## Evidence Requirement

Every finding must be supported by observable evidence.

Avoid statements such as:

"The interface is confusing."

Instead describe the observable cause:

"The primary navigation contains three labels with similar
wording, making their destinations difficult to distinguish."

## Severity

Use the severity scale defined in:

`references/severity-rating.md`

## Heuristic Definitions

Use:

`references/nielsen-heuristics.md`

for the definitions and interpretation of Nielsen's heuristics.

## Output

Return findings using the structure defined in:

`templates/evaluation-report.md`

## Evaluation Principles

- Evidence over preference.
- Explain the relationship between observation and heuristic.
- Avoid duplicate findings.
- Avoid unsupported assumptions.
- Prefer actionable recommendations.
- Evaluate the interface rather than the quality of its designer.