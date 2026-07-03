# 🤝 Personalized Networking Assistant

The **Personalized Networking Assistant** is an AI-powered web application developed as part of the **Google Cloud GenAI Project**. It assists students, professionals, and job seekers in preparing for networking events by generating personalized conversation starters, self-introductions, networking tips, and fact-checked responses using **Large Language Models (LLMs)** through the **Groq API**.

The application combines a **FastAPI backend**, **Streamlit frontend**, and modular AI services to deliver an intelligent and interactive networking experience.

---

# 🚀 Features

- 💬 AI-powered conversation starter generation
- 🎤 Personalized self-introduction generation
- 💡 Smart networking tips
- 📅 Event-based conversation suggestions
- 🧠 Event and topic analysis
- 🔍 Fact verification using Wikipedia API
- 📖 Conversation history logging
- ⭐ User feedback collection
- 🌐 Interactive Streamlit interface
- ⚡ FastAPI REST API backend
- 🧪 Automated testing with PyTest

---

# 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv

### Frontend
- Streamlit

### AI & APIs
- Groq API (LLM Integration)
- Wikipedia API
- Requests

### Testing
- PyTest

### Version Control
- Git
- GitHub

---

# 📂 Repository Structure

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
└── Source Code
    ├── app
    │   ├── models
    │   ├── routers
    │   ├── services
    │   ├── config.py
    │   └── main.py
    ├── frontend
    ├── tests
    ├── networking.db
    ├── requirements.txt
    ├── .env.example
    └── .gitignore
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Navigate to the Source Code

```bash
cd "Source Code"
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Running the Frontend

```bash
streamlit run frontend/app.py
```

Open

```
http://localhost:8501
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📈 Project Workflow

1. User enters profile and event information.
2. Event details are analyzed.
3. The application generates personalized conversation starters.
4. Self-introduction suggestions are created.
5. Networking tips are provided.
6. Facts are verified using the Wikipedia API.
7. Conversation history is stored.
8. User feedback is collected for continuous improvement.

---

# 🎯 Project Outcome

The Personalized Networking Assistant simplifies professional networking by leveraging **Generative AI** and **Groq LLMs** to provide intelligent conversation guidance. The application enables users to confidently initiate conversations, introduce themselves effectively, verify factual information, and receive personalized networking recommendations through an intuitive web interface.

---

# 👨‍💻 Developed By

**Dandu Thanishka Reddy**

**Google Cloud GenAI Project**