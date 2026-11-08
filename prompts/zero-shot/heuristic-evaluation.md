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

Return the result as valid JSON with a "findings" array.
