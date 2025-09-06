# CodePalAI — Multi-Language AI Code Review Assistant

This project uses OpenAI’s GPT-3.5 model to perform automated code reviews across multiple languages, including Python, JavaScript, Java, C++, and C#. It analyzes your code, identifies potential bugs and bad practices and returns structured feedback along with an improved version.

---

## Features

- Instant AI-powered code reviews
- Supports Python, JavaScript, Java, C++, and C#
- Clear issue summaries and helpful explanations
- Fix suggestions and best practice tips
- Revised "Improved Version" with copy-to-clipboard functionality
- Full test coverage with FastAPI’s TestClient and Pytest
- Clean and responsive UI with React + TailwindCSS
- Dockerized for easy setup

---

## Demo
![CodePalAI Demo](assets/demo01.png?raw=true "Demo Screenshot 1")  
<br>  
![CodePalAI Demo](assets/demo02.png?raw=true "Demo Screenshot 2")

---

## Tech Stack

| Layer       | Tech                        |
|-------------|-----------------------------|
| Frontend    | React + TailwindCSS         |
| Backend     | FastAPI                     |
| AI Engine   | OpenAI GPT-3.5 (via API)    |
| Testing     | Pytest + FastAPI TestClient |
| Container   | Docker, Docker Compose      |

---

## Folder Structure

```
CodePalAI-LLM-Code-Reviewer/
│
├── assets/
│   ├── demo01.png           # Screenshot 1
│   ├── demo02.png           # Screenshot 2
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   └── services/
│   ├── prompts/
│   │   └── code_review.txt  # Prompt template
│   ├── tests/
│   │   └── test_review.py   # Unit tests for the review API
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env                 # API key config
│
├── frontend/
│   ├── src/
│   │   └── App.js           # Main React component
│   ├── package.json
│   └── package-lock.json
│
├── docker-compose.yml
└── README.md
```
---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Juliane-Farmer/CodePalAI-LLM-Code-Reviewer.git
cd CodePalAI-LLM-Code-Reviewer
```

### 2. Configure OpenAI API

Create a `.env` file inside the `backend/` folder:

```env
MODEL_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
MODEL_NAME=gpt-3.5-turbo
```

### 3. Run the App

#### Backend (FastAPI)

```bash
cd backend
docker-compose up --build
```

Backend runs at: http://localhost:8000/docs

#### Frontend (React)

```bash
cd frontend
npm install
npm start
```

Frontend runs at: http://localhost:3000

---

## Running Tests

To run backend tests:

```bash
cd CodePalAI-LLM-Code-Reviewer
PYTHONPATH=backend pytest backend/tests
```

Tests include:
- Valid input
- Missing fields
- Invalid types
- Edge cases (empty code, unsupported language)

---

## Supported Languages

You can paste code in:
- Python
- JavaScript
- Java
- C++
- C#

---


