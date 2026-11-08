import argparse
import os
import time
from pathlib import Path

from google import genai
from google.genai import types


# ============================================================
# 1. Initialize Gemini
# ============================================================

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


# ============================================================
# 2. Define project paths
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent

PROMPT_DIR = PROJECT_DIR / "prompts"
SKILL_DIR = PROJECT_DIR / "skills" / "heuristic-evaluation"

INPUT_DIR = PROJECT_DIR / "inputs"
OUTPUT_DIR = PROJECT_DIR / "outputs"

SCREENSHOT_PATH = INPUT_DIR / "screenshot.png"


# ============================================================
# 3. Parse command-line arguments
# ============================================================

parser = argparse.ArgumentParser(
    description="Run UI/UX heuristic evaluation with Gemini."
)

parser.add_argument(
    "--prompt",
    choices=["zero-shot", "few-shot", "cot"],
    default="zero-shot",
    help="Prompt engineering strategy to use."
)

parser.add_argument(
    "--skill",
    action="store_true",
    help="Include the heuristic evaluation skill."
)

args = parser.parse_args()


# ============================================================
# 4. Load prompt
# ============================================================

prompt_path = (
    PROMPT_DIR
    / args.prompt
    / "heuristic-evaluation.md"
)

if not prompt_path.exists():
    raise FileNotFoundError(
        f"Prompt not found: {prompt_path}"
    )

prompt = prompt_path.read_text(
    encoding="utf-8"
)


# ============================================================
# 5. Load skill (optional)
# ============================================================

skill_context = ""

if args.skill:

    skill = (
        SKILL_DIR / "SKILL.md"
    ).read_text(encoding="utf-8")

    heuristics = (
        SKILL_DIR
        / "references"
        / "nielsen-heuristics.md"
    ).read_text(encoding="utf-8")

    evaluation_criteria = (
        SKILL_DIR
        / "references"
        / "evaluation-criteria.md"
    ).read_text(encoding="utf-8")

    severity = (
        SKILL_DIR
        / "references"
        / "severity-rating.md"
    ).read_text(encoding="utf-8")

    report_template = (
        SKILL_DIR
        / "templates"
        / "evaluation-report.md"
    ).read_text(encoding="utf-8")

    skill_context = f"""
# SKILL

{skill}

# HEURISTIC REFERENCE

{heuristics}

# EVALUATION CRITERIA

{evaluation_criteria}

# SEVERITY RATING

{severity}

# EVALUATION REPORT CONTRACT

{report_template}
"""


# ============================================================
# 6. Build final prompt
# ============================================================

final_prompt = f"""
{skill_context}

# PROMPT

{prompt}

# TASK

Evaluate the provided UI screenshot according to the
instructions above.

Base every finding on observable evidence from the screenshot.

Return the result according to the requested output format.
"""


# ============================================================
# 7. Load screenshot
# ============================================================

if not SCREENSHOT_PATH.exists():
    raise FileNotFoundError(
        f"Screenshot not found: {SCREENSHOT_PATH}"
    )

with open(SCREENSHOT_PATH, "rb") as f:
    screenshot = f.read()


# ============================================================
# 8. Prepare Gemini request
# ============================================================

contents = [
    types.Part.from_text(
        text=final_prompt
    ),
    types.Part.from_bytes(
        data=screenshot,
        mime_type="image/png"
    ),
]


# ============================================================
# 9. Send request with retry
# ============================================================

MAX_RETRIES = 5

for attempt in range(MAX_RETRIES):

    try:

        print(
            f"Sending request to Gemini "
            f"(attempt {attempt + 1}/{MAX_RETRIES})..."
        )

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=contents,
        )

        break

    except Exception as e:

        if attempt == MAX_RETRIES - 1:
            raise

        wait_time = 2 ** attempt

        print(f"Request failed: {e}")
        print(f"Retrying in {wait_time} seconds...")

        time.sleep(wait_time)


# ============================================================
# 10. Print result
# ============================================================

print("\n========================================")
print("HEURISTIC EVALUATION")
print("========================================")

print(f"Prompt strategy : {args.prompt}")
print(f"Skill enabled   : {args.skill}")

print("\n=== RESULT ===\n")
print(response.text)