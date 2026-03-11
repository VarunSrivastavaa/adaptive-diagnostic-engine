# AI-Driven Adaptive Diagnostic Engine

An AI-powered adaptive testing system that dynamically adjusts question difficulty based on user performance and generates personalized study recommendations.

This project simulates the behavior of adaptive exams like GRE or GMAT, where the next question depends on the student's ability level.

---

## 🚀 Features

* Adaptive question selection based on ability score
* Dynamic difficulty adjustment
* MongoDB-based question storage
* Session tracking for each user
* FastAPI REST API backend
* AI-generated personalized study recommendations

---

## 🏗️ System Architecture

User → FastAPI API → Adaptive Algorithm → MongoDB
↓
AI Recommendation Engine → Personalized Study Plan

---

## 📂 Project Structure

adaptive-diagnostic-engine

routes/
 └── test_routes.py

app.py
database.py
adaptive_algorithm.py
ai_recommendation.py
seed_questions.py

requirements.txt
README.md
.gitignore

---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/VarunSrivastavaa/adaptive-diagnostic-engine.git

cd adaptive-diagnostic-engine

---

### 2️⃣ Create virtual environment

python -m venv venv

Activate it (Windows):

venv\Scripts\activate

---

### 3️⃣ Install dependencies

pip install -r requirements.txt

---

### 4️⃣ Start MongoDB

Make sure MongoDB is running locally.

Default connection:

mongodb://localhost:27017

---

### 5️⃣ Insert sample questions

python seed_questions.py

---

### 6️⃣ Run the API server

uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000

---

## 📡 API Endpoints

### Start Test

POST /start-test

Response

{
"session_id": "abc123"
}

---

### Get Next Question

GET /next-question/{session_id}

Returns a question based on the user's ability score.

---

### Submit Answer

POST /submit-answer

Example request

{
"session_id": "abc123",
"question_id": "123",
"answer": "12"
}

Response

{
"correct": true,
"new_ability": 0.6
}

---

## 🧠 Adaptive Algorithm

The system maintains an **ability score** for each user.

Initial ability:

0.5

Rules:

Correct Answer → ability + 0.1
Wrong Answer → ability - 0.1

The next question is selected based on the closest difficulty to the current ability score.

Difficulty range:

0.1 → Easy
1.0 → Hard

---

## 🗄️ Database Schema

### Questions Collection

{
question: string,
options: [string],
correct_answer: string,
difficulty: float,
topic: string
}

---

### Sessions Collection

{
session_id: string,
ability: float,
questions_answered: []
}

---

## 🧪 Testing the API

FastAPI provides automatic API documentation.

Open in browser:

http://127.0.0.1:8000/docs

From here you can test all endpoints directly.

---

## 📌 Future Improvements

* Add Machine Learning based difficulty adjustment
* Add user authentication
* Add dashboard for performance tracking
* Deploy using Docker and AWS

---

## 👨‍💻 Author

Varun Prakash Srivastava

GitHub: https://github.com/VarunSrivastavaa
