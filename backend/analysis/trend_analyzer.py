import pandas as pd

df = pd.read_csv("data/workouts.csv")

exercise_name = input("Exercise to analyze: ").lower()

exercise_data = df[
    df["Exercise"].str.lower() == exercise_name
]

print("\nWorkout History")
print(exercise_data)

if len(exercise_data) < 2:
    print("\nNot enough data for trend analysis.")
    exit()

weights = exercise_data["Weight"]

first_weight = weights.iloc[0]
last_weight = weights.iloc[-1]

print(f"\nFirst Weight: {first_weight}")
print(f"Latest Weight: {last_weight}")

if last_weight > first_weight:
    print("\nTrend: Improving 📈")
elif last_weight < first_weight:
    print("\nTrend: Declining 📉")
else:
    print("\nTrend: Stable ➖")