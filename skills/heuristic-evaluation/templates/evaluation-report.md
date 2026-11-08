# Evaluation Report Contract

## Output Format

Return the heuristic evaluation as a JSON object.

The response must contain a `findings` array.

Each finding must contain:

- `finding_id`
- `heuristic_id`
- `heuristic_name`
- `observation`
- `evidence`
- `explanation`
- `severity`
- `recommendation`

## Schema

```json
{
  "findings": [
    {
      "finding_id": "F001",
      "heuristic_id": "H1",
      "heuristic_name": "Visibility of System Status",
      "observation": "...",
      "evidence": "...",
      "explanation": "...",
      "severity": 2,
      "recommendation": "..."
    }
  ]
}