import pandas as pd

report = pd.read_csv("data/plateau_report.csv")

exercise = report.loc[0, "Exercise"]

print("\n=== ROOT CAUSE ANALYSIS ===\n")
print("Exercise:", exercise)
if exercise == "bench":
    primary_issue = "Triceps"

elif exercise == "squat":
    primary_issue = "Quads/Core"

elif exercise == "deadlift":
    primary_issue = "Posterior Chain"

else:
    primary_issue = "General Weakness"

print("\nPrimary Weakness:")
print(primary_issue)
root_report = pd.DataFrame({
    "Exercise": [exercise],
    "PrimaryIssue": [primary_issue]
})

root_report.to_csv(
    "data/root_cause_report.csv",
    index=False
)

print("\nRoot cause report saved.")