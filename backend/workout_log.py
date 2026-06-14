import pandas as pd

data = {
    "Exercise": ["Bench", "Squat", "Deadlift"],
    "Weight": [100, 140, 180],
    "Reps": [5, 5, 3],
    "Sets": [3, 3, 3]
}

df = pd.DataFrame(data)

print("\nWorkout Log\n")
print(df)

print("\nAverage Weight Lifted:")
print(df["Weight"].mean())