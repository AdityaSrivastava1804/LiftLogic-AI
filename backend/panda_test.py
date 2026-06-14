import pandas as pd

data = {
    "Exercise": ["Bench", "Squat", "Deadlift"],
    "Weight": [100, 140, 180],
    "Reps": [5, 5, 3]
}

df = pd.DataFrame(data)

print(df)