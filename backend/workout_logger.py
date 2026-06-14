import pandas as pd
import os

exercise = input("Exercise: ")
weight = float(input("Weight (kg): "))
sets = int(input("Sets: "))
reps = int(input("Reps: "))
rpe = float(input("RPE: "))

new_entry = pd.DataFrame({
    "Exercise": [exercise],
    "Weight": [weight],
    "Sets": [sets],
    "Reps": [reps],
    "RPE": [rpe]
})

file_name = "data/workouts.csv"

if os.path.exists(file_name):
    old_data = pd.read_csv(file_name)
    updated_data = pd.concat([old_data, new_entry], ignore_index=True)
else:
    updated_data = new_entry

updated_data.to_csv(file_name, index=False)

print("\nWorkout Saved!\n")
print(updated_data)