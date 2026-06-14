LiftLogic AI

AI-powered strength coaching platform that helps lifters track workouts, detect training plateaus, analyze root causes, predict future PRs, and generate personalized training recommendations.

⸻

Features

Workout Logging

* Log exercises, weight, sets, reps, and RPE
* Store training history in CSV format

Plateau Detection

* Detect stalled progress automatically
* Identify lifts that are no longer improving

Root Cause Analysis

* Analyze possible causes of stalled progress
* Detect issues such as:
    * High fatigue
    * Insufficient intensity
    * Lack of progression

AI Coaching

* Personalized coaching feedback using Gemini AI
* Exercise-specific recommendations
* Actionable next steps for improvement

Coaching Memory

* Stores athlete profile information:
    * Goal
    * Bodyweight
    * Equipment availability
    * Training frequency
    * Preferred lift

Progress Dashboard

* Interactive strength progress charts
* Bench, Squat, and Deadlift tracking
* Personal record visualization

PR Prediction

* Uses Linear Regression to estimate future strength progression
* Predicts upcoming PRs based on training history

AI Training Block Generator

* Generates personalized 4-week training programs
* Adapts to:
    * Training goal
    * Training frequency
    * Priority lift

⸻

Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* Scikit-Learn
* Gemini API
* CSV Data Storage

⸻

Project Structure

LiftLogic-AI/

├── backend/

│   ├── agents/

│   ├── ml/

│   └── analysis/

├── frontend/

│   └── app.py

├── data/

├── models/

├── requirements.txt

└── README.md

⸻

Installation

Clone the repository:

git clone https://github.com/AdityaSrivastava1804/LiftLogic-AI.git
cd LiftLogic-AI

Install dependencies:

python3 -m pip install -r requirements.txt

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY

Run the application:

streamlit run frontend/app.py

⸻

Future Improvements

* User authentication
* Cloud database integration
* Nutrition recommendations
* Advanced ML models
* Mobile application

⸻

Author

Aditya Kumar Srivastava

B.Tech CSE | AI & Data Science Enthusiast

GitHub: https://github.com/AdityaSrivastava1804