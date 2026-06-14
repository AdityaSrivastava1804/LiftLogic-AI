import json
from datetime import date
import streamlit as st
import pandas as pd
import os

from google import genai
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="LiftLogic",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ LiftLogic")
st.subheader("AI Training Analyst")

st.header("Log Workout")

exercise = st.selectbox(
    "Exercise",
    ["bench", "squat", "deadlift"]
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.0,
    value=100.0
)

sets = st.number_input(
    "Sets",
    min_value=1,
    value=3
)

reps = st.number_input(
    "Reps",
    min_value=1,
    value=5
)

rpe = st.slider(
    "RPE",
    1,
    10,
    8
)

if st.button("Log Workout"):

    workout = pd.DataFrame({
    "Date": [date.today()],
    "Exercise": [exercise],
    "Weight": [weight],
    "Sets": [sets],
    "Reps": [reps],
    "RPE": [rpe]
})

    csv_file = "data/workouts.csv"

    if os.path.exists(csv_file):

        workout.to_csv(
            csv_file,
            mode="a",
            header=False,
            index=False
        )

    else:

        workout.to_csv(
            csv_file,
            index=False
        )

    st.success("✅ Workout Logged Successfully!")

st.header("Workout History")

if os.path.exists("data/workouts.csv"):

    df = pd.read_csv("data/workouts.csv")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Weight Progress")

    chart_df = df[
        df["Exercise"].str.lower() == exercise.lower()
    ]

    if not chart_df.empty:

        st.line_chart(
            chart_df["Weight"]
        )

st.header("Analysis")

if st.button("Analyze Workout"):

    if not os.path.exists("data/workouts.csv"):

        st.warning("No workout data found.")

    else:

        df = pd.read_csv("data/workouts.csv")

        exercise_data = df[
            df["Exercise"].str.lower() == exercise.lower()
        ]

        if len(exercise_data) < 3:

            st.warning(
                "Need at least 3 workouts for analysis."
            )

        else:

            recent = exercise_data.tail(3)

            weights = recent["Weight"].tolist()
            rpes = recent["RPE"].tolist()

            plateau_score = 0

            if len(set(weights)) == 1:
                plateau_score += 1

            if rpes[-1] > rpes[0]:
                plateau_score += 1

            if sum(rpes) / len(rpes) >= 8.5:
                plateau_score += 1

            if plateau_score >= 2:

                st.error("🚨 Plateau Detected")

                if exercise == "bench":

                    issue = "Triceps Weakness"

                    recommendations = [
                        "Close-Grip Bench Press",
                        "Skull Crushers",
                        "Weighted Dips",
                        "Overhead Tricep Extensions"
                    ]

                elif exercise == "squat":

                    issue = "Quad/Core Weakness"

                    recommendations = [
                        "Front Squats",
                        "Pause Squats",
                        "Bulgarian Split Squats",
                        "Leg Press"
                    ]

                else:

                    issue = "Posterior Chain Weakness"

                    recommendations = [
                        "Romanian Deadlifts",
                        "Deficit Deadlifts",
                        "Barbell Rows",
                        "Hamstring Curls"
                    ]

                st.subheader("Root Cause")
                st.write(issue)

                st.subheader("Recommendations")

                for rec in recommendations:
                    st.write(f"• {rec}")

                st.subheader("🤖 AI Coach")

                prompt = f"""
                You are LiftLogic AI Coach.

                Exercise: {exercise}

                Root Cause: {issue}

                Recommendations:
                {', '.join(recommendations)}

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

                st.write(response.text)

            else:

                st.success(
                    "✅ No Plateau Detected"
                )

st.header("Program Analysis")

if st.button("Analyze Entire Program"):

    if not os.path.exists("data/workouts.csv"):

        st.warning("No workout data found.")

    else:

        df = pd.read_csv("data/workouts.csv")

        for lift in ["bench", "squat", "deadlift"]:

            lift_data = df[
                df["Exercise"].str.lower() == lift
            ]

            st.subheader(lift.capitalize())

            if len(lift_data) < 3:

                st.warning(
                    f"Not enough data for {lift}"
                )

                continue

            recent = lift_data.tail(3)

            weights = recent["Weight"].tolist()
            rpes = recent["RPE"].tolist()

            plateau_score = 0

            if len(set(weights)) == 1:
                plateau_score += 1

            if rpes[-1] > rpes[0]:
                plateau_score += 1

            if sum(rpes) / len(rpes) >= 8.5:
                plateau_score += 1

            if plateau_score >= 2:

                st.error(
                    f"🚨 Plateau Detected ({lift.capitalize()})"
                )

            else:

                st.success(
                    f"✅ Healthy Progression ({lift.capitalize()})"
                )
st.subheader("AI Training Analyst")
st.header("User Profile")

with open("data/user_profile.json", "r") as f:
    profile = json.load(f)

st.write("Goal:", profile["goal"])
st.write("Bodyweight:", profile["bodyweight"], "kg")
st.write("Equipment:", profile["equipment"])
st.write("Training Days:", profile["training_days"])
st.write("Preferred Lift:", profile["preferred_lift"])


import plotly.express as px

st.header("📈 Progress Dashboard")

if os.path.exists("data/workouts.csv"):

    df = pd.read_csv("data/workouts.csv")

    df["Date"] = pd.to_datetime(df["Date"]).dt.date

    fig = px.line(
    df,
    x="Date",
    y="Weight",
    color="Exercise",
    markers=True,
    title="Strength Progress"
)

st.header("📈 Progress Dashboard")

bench_df = df[df["Exercise"] == "bench"]

squat_df = df[df["Exercise"] == "squat"]

deadlift_df = df[df["Exercise"] == "deadlift"]
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Bench PR", f"{bench_df['Weight'].max()} kg")

with col2:
    st.metric(
    "Squat PR",
    f"{int(squat_df['Weight'].max())} kg"
)
with col3:
    st.metric("Deadlift PR", f"{deadlift_df['Weight'].max()} kg")

st.plotly_chart(fig, use_container_width=True)

df["Estimated1RM"] = df["Weight"] * (1 + df["Reps"] / 30)
fig = px.line(
    df,
    x="Date",
    y="Estimated1RM",
    color="Exercise",
    markers=True,
    title="Estimated 1RM Progress"
)
from sklearn.linear_model import LinearRegression

bench_df = df[df["Exercise"] == "bench"].copy()

bench_df["Session"] = range(len(bench_df))

X = bench_df[["Session"]]
y = bench_df["Estimated1RM"]

model = LinearRegression()
model.fit(X, y)

future_session = pd.DataFrame({
    "Session": [len(bench_df) + 4]
})

prediction = model.predict(future_session)[0]
st.subheader("🔮 PR Prediction")

st.metric(
    "Predicted Bench PR",
    f"{prediction:.1f} kg"
)
st.header("🏋️ AI Training Block Generator")
goal = st.selectbox(
    "Goal",
    ["Strength", "Hypertrophy"]
)

training_days = st.slider(
    "Training Days Per Week",
    3,
    6,
    4
)

preferred_lift = st.selectbox(
    "Priority Lift",
    ["Bench", "Squat", "Deadlift"]
)
if st.button("Generate Training Block"):


    st.write("Button clicked")
    
    prompt = f"""
You are LiftLogic AI Programming Coach.

Goal: {goal}
Training Days Per Week: {training_days}
Priority Lift: {preferred_lift}

Generate a practical 4-week training block.

Requirements:
- Include Week 1 to Week 4
- Include sets and reps
- Include progression
- Include accessory work
- Include a deload if needed
- Use realistic gym programming

Format clearly.
"""
    st.write("Prompt created")
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
    st.write("Gemini responded")
    st.subheader("📋 Generated Program")
    st.write(response.text)   



