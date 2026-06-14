import pandas as pd

df = pd.read_csv("data/workouts.csv")

latest_workout = df.iloc[-1]

exercise = latest_workout["Exercise"]
weight = latest_workout["Weight"]
reps = latest_workout["Reps"]
rpe = latest_workout["RPE"]

print("\nLatest Workout")
print(latest_workout)

target_reps = {
    "bench": 5,
    "squat": 5,
    "deadlift": 3
}

required_reps = target_reps.get(exercise.lower(), 5)
print(f"Required Reps: {required_reps}")

if reps >= required_reps and rpe <= 8:
    next_weight = weight + 2.5
    reason = "Target reps achieved and recovery appears acceptable."
else:
    next_weight = weight
    reason = "Progression not recommended based on current performance."

print("\nRecommendation")
print(f"{exercise}: {next_weight} kg next session")
print(f"Reason: {reason}")