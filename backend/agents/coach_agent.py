

from google import genai
from dotenv import load_dotenv
import pandas as pd
import os
from pathlib import Path
import json

with open("data/user_profile.json", "r") as f:
    profile = json.load(f)

env_file = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(env_file)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

root_report = pd.read_csv("data/root_cause_report.csv")

exercise = root_report.loc[0, "Exercise"]

if "PrimaryIssues" in root_report.columns:
    issues = root_report.loc[0, "PrimaryIssues"]
else:
    issues = root_report.loc[0, "PrimaryIssue"]

prompt = f"""
You are LiftLogic AI Coach.

User Profile:
Goal: {profile['goal']}
Bodyweight: {profile['bodyweight']} kg
Equipment: {profile['equipment']}
Training Days: {profile['training_days']}
Preferred Lift: {profile['preferred_lift']}

Exercise: {exercise}

Root Cause: {issues}

Provide:

1. Analysis
2. Coaching Advice
3. Expected Outcome

Keep response under 150 words.
"""
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n=== LIFTLOGIC AI COACH ===\n")
print(response.text)