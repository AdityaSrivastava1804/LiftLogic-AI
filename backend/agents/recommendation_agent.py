import pandas as pd
import os

print("\n=== LiftLogic Recommendation Agent ===\n")

# Check if report exists
if not os.path.exists("data/root_cause_report.csv"):
    print("Error: root_cause_report.csv not found.")
    print("Run root_cause_agent.py first.")
    exit()

# Load report
report = pd.read_csv("data/root_cause_report.csv")

if report.empty:
    print("Error: root_cause_report.csv is empty.")
    exit()

exercise = report.loc[0, "Exercise"]

# Support both PrimaryIssue and PrimaryIssues
if "PrimaryIssues" in report.columns:
    issues = report.loc[0, "PrimaryIssues"]
    issue_list = [x.strip() for x in str(issues).split(",")]

elif "PrimaryIssue" in report.columns:
    issue = report.loc[0, "PrimaryIssue"]
    issue_list = [str(issue)]

else:
    print("Error: No PrimaryIssue or PrimaryIssues column found.")
    print("Columns found:", list(report.columns))
    exit()

print("Exercise:", exercise)
print("Detected Issues:", ", ".join(issue_list))

recommendations = []

# Recovery
if "Recovery" in issue_list:
    recommendations.extend([
        "Sleep 7.5-9 hours daily",
        "Add 1 recovery day",
        "Reduce accumulated fatigue",
        "Monitor stress levels"
    ])

# Bench
if "Triceps" in issue_list:
    recommendations.extend([
        "Close-Grip Bench Press",
        "Skull Crushers",
        "Weighted Dips",
        "Overhead Tricep Extensions"
    ])

# Squat
if "Quads/Core" in issue_list:
    recommendations.extend([
        "Front Squats",
        "Pause Squats",
        "Bulgarian Split Squats",
        "Leg Press"
    ])

# Deadlift
if "Posterior Chain" in issue_list:
    recommendations.extend([
        "Romanian Deadlifts",
        "Deficit Deadlifts",
        "Barbell Rows",
        "Hamstring Curls"
    ])

# Volume
if "Insufficient Volume" in issue_list:
    recommendations.extend([
        "Add 2-4 weekly working sets",
        "Increase training frequency",
        "Add variation work"
    ])

# Fallback
if len(recommendations) == 0:
    recommendations.extend([
        "Review training program",
        "Improve recovery",
        "Increase training consistency"
    ])

print("\n==============================")
print("LIFTLOGIC COACHING REPORT")
print("==============================")

print(f"\nExercise: {exercise}")

print("\nRecommended Actions:\n")

for rec in recommendations:
    print("-", rec)

print("\nEnd of Report")