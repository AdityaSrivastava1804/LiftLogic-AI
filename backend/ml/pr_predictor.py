import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/workouts.csv")

df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")
df["Reps"] = pd.to_numeric(df["Reps"], errors="coerce")

df = df.dropna(subset=["Weight", "Reps"])

df["Estimated1RM"] = (
    df["Weight"] * (1 + df["Reps"] / 30)
)

bench_df = df[df["Exercise"] == "bench"].copy()

bench_df = bench_df.reset_index(drop=True)

bench_df["Session"] = range(len(bench_df))

X = bench_df[["Session"]]
y = bench_df["Estimated1RM"]

model = LinearRegression()
model.fit(X, y)

future_session = pd.DataFrame({
    "Session": [len(bench_df) + 4]
})

prediction = model.predict(future_session)[0]

print("\n=== PR PREDICTION ===\n")

print(
    f"Current Estimated Bench 1RM: "
    f"{bench_df['Estimated1RM'].max():.1f} kg"
)

print(
    f"Predicted Estimated Bench 1RM (4 Sessions): "
    f"{prediction:.1f} kg"
)