# Task

Evaluate the provided UI screenshot for usability problems using Nielsen's 10 usability heuristics.

For each potential usability problem:

1. Inspect the screenshot and identify the relevant interface element.
2. Determine whether the observation represents a genuine usability problem.
3. Identify the Nielsen heuristic that is most directly related to the problem.
4. Verify that the finding is supported by observable evidence in the screenshot.
5. Assess the potential user impact.
6. Assign a severity rating from 0 to 4.
7. Formulate an actionable recommendation.

Do not report problems based solely on personal preference or unsupported assumptions.

Use a severity scale from 0 to 4:

* 0 = No problem
* 1 = Cosmetic
* 2 = Minor
* 3 = Major
* 4 = Catastrophic

Return each finding with:

* finding_id
* heuristic_id
* heuristic_name
* observation
* evidence
* explanation
* severity
* recommendation

Return the result as valid JSON with a "findings" array.

Do not include your internal reasoning process in the output.
