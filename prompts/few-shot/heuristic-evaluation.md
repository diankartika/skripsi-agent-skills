# Task

Evaluate the provided UI screenshot for usability problems using Nielsen's 10 usability heuristics.

Identify usability problems that are directly observable from the screenshot.

For each identified problem, provide:

* finding_id
* heuristic_id
* heuristic_name
* observation
* evidence
* explanation
* severity
* recommendation

Use a severity scale from 0 to 4:

* 0 = No problem
* 1 = Cosmetic
* 2 = Minor
* 3 = Major
* 4 = Catastrophic

Base every finding on observable evidence from the screenshot.

Do not report problems based solely on personal preference or unsupported assumptions.

# Example

Input:
A checkout page contains a "Pay Now" button, but the button is visually identical to surrounding secondary buttons and does not appear clickable.

Output:
{
"findings": [
{
"finding_id": "F001",
"heuristic_id": "H4",
"heuristic_name": "Consistency and Standards",
"observation": "The primary checkout action is not visually distinguished from secondary actions.",
"evidence": "The 'Pay Now' button has the same visual treatment as surrounding secondary buttons.",
"explanation": "Users may have difficulty distinguishing the primary action from secondary actions when interactive elements use inconsistent visual hierarchy.",
"severity": 2,
"recommendation": "Use a visually distinct treatment for the primary checkout action."
}
]
}

# Evaluation

Now evaluate the provided UI screenshot.

Return the result as valid JSON with a "findings" array.
