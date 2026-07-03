# 🤝 Personalized Networking Assistant

> **An AI-powered networking companion that helps users build meaningful professional connections through personalized conversation starters, self-introductions, networking guidance, and intelligent fact verification.**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-Educational-green)

---

## 📖 Overview

The **Personalized Networking Assistant** is an AI-powered web application developed as part of the **Google Cloud GenAI Project**.

The application helps students, professionals, and job seekers prepare for networking events by generating personalized conversation starters, professional self-introductions, networking tips, and fact-verified responses using **Large Language Models (LLMs)** powered by the **Groq API**.

By combining AI with an intuitive web interface, users can confidently initiate conversations and build valuable professional relationships.

---

# ✨ Key Features

- 💬 AI-generated personalized conversation starters
- 🎤 Professional self-introduction generator
- 💡 Intelligent networking tips
- 📅 Event-specific conversation suggestions
- 🧠 Smart event & topic analysis
- 🔍 Fact verification using Wikipedia API
- 📚 Conversation history tracking
- ⭐ User feedback collection
- 🌐 Interactive Streamlit interface
- ⚡ FastAPI REST API backend
- 🧪 Automated testing with PyTest

---

# 🛠️ Tech Stack

### 👨‍💻 Programming Language
- 🐍 Python

### ⚙️ Backend
- ⚡ FastAPI
- 🚀 Uvicorn
- 📦 Pydantic
- 🔐 python-dotenv

### 🎨 Frontend
- 🌐 Streamlit

### 🤖 Artificial Intelligence
- 🧠 Groq API (LLM)
- 📖 Wikipedia API

### 📚 Libraries
- Requests
- HTTPX
- BeautifulSoup4

### 🧪 Testing
- PyTest

### 🔧 Development Tools
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
Personalized-Networking-Assistant
│
├── 1. Brainstorming & Ideation
├── 2. Requirement Analysis
├── 3. Project Design Phase
├── 4. Project Planning Phase
├── 5. Project Development Phase
├── 6. Project Testing
├── 7. Project Documentation
├── 8. Project Demonstration
│
└── Source Code
    ├── app
    │   ├── models
    │   ├── routers
    │   ├── services
    │   ├── config.py
    │   └── main.py
    │
    ├── frontend
    ├── tests
    ├── networking.db
    ├── requirements.txt
    ├── .env.example
    └── .gitignore
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone <repository-url>
```

---

## 2️⃣ Navigate to Source Code

```bash
cd "Source Code"
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Backend

```bash
uvicorn app.main:app --reload
```

📌 Backend URL

```
http://127.0.0.1:8000
```

📖 Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run the Frontend

```bash
streamlit run frontend/app.py
```

🌐 Open your browser:

```
http://localhost:8501
```

---

# 🔄 Application Workflow

```text
User Input
      │
      ▼
Profile & Event Analysis
      │
      ▼
Groq AI Processing
      │
      ▼
Conversation Generation
      │
      ├────────► Self Introduction
      │
      ├────────► Networking Tips
      │
      ├────────► Topic Suggestions
      │
      └────────► Fact Verification
                    │
                    ▼
          Streamlit User Interface
```

---

# 🎯 Project Highlights

✅ AI-powered networking assistant

✅ Personalized conversation generation

✅ Professional self-introductions

✅ Event-based recommendations

✅ Fact verification with Wikipedia

✅ Clean FastAPI architecture

✅ Interactive Streamlit dashboard

✅ Modular and scalable codebase

✅ Automated testing support

---

# 📈 Future Enhancements

- 🌍 Multi-language support
- 🎙️ Voice-enabled conversations
- 📅 Calendar integration
- 📱 Mobile-friendly interface
- 🤝 LinkedIn profile integration
- ☁️ Cloud deployment
- 📊 Analytics dashboard

---

# 👨‍💻 Developer

**Dandu Thanishka Reddy**

🎓 Google Cloud GenAI Project

---

# ⭐ Support

If you found this project useful, don't forget to **⭐ Star this repository** and share your feedback!