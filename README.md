# 🤝 Personalized Networking Assistant

<div align="center">

### AI-Powered Networking Companion for Students, Professionals, and Job Seekers

*Built with FastAPI • Streamlit • Groq LLM • Wikipedia API*

</div>

---

## 📖 Overview

The **Personalized Networking Assistant** is an AI-powered web application developed as part of the **Google Cloud GenAI Project**. It empowers students, professionals, and job seekers to confidently prepare for networking events by generating personalized conversation starters, engaging self-introductions, networking strategies, and fact-checked discussion topics using **Large Language Models (LLMs)** through the **Groq API**.

Instead of relying on generic conversation suggestions, the application analyzes user profiles and event details to deliver personalized, context-aware recommendations that help users communicate more effectively in professional environments.

---

# ✨ Key Features

## 🤖 AI-Powered Networking Assistant
- Generate personalized conversation starters
- AI-generated professional self-introductions
- Smart networking strategies based on event type
- Personalized communication guidance

## 📅 Intelligent Event Analysis
- Analyze networking events
- Extract event domain and context
- Generate event-specific discussion topics
- Context-aware conversation suggestions

## 🔍 Fact Verification
- Validate AI-generated information
- Wikipedia API integration
- Improve reliability of generated responses
- Reduce misinformation during conversations

## 📚 Conversation Management
- Conversation history logging
- User interaction tracking
- Feedback collection
- Response improvement support

## 🌐 Interactive User Interface
- Modern Streamlit dashboard
- Clean and responsive interface
- Easy profile management
- Simple event input forms

## ⚙️ REST API
- FastAPI backend
- Modular API architecture
- Scalable service design
- Interactive Swagger documentation

---

# 🏗️ System Architecture

```
                    +----------------------+
                    |   Streamlit Frontend |
                    +----------+-----------+
                               |
                               |
                               ▼
                    +----------------------+
                    |   FastAPI Backend    |
                    +----------+-----------+
                               |
       -------------------------------------------------
       |             |             |                   |
       ▼             ▼             ▼                   ▼
 Event Analyzer  Groq LLM   Wikipedia API   History & Feedback
       |             |             |                |
       ----------------------------------------------
                       |
                       ▼
              AI Generated Response
```

---

# 🚀 Technologies Used

## Programming Language

- Python

---

## Backend

- FastAPI
- Uvicorn
- Pydantic
- Python-dotenv

---

## Frontend

- Streamlit

---

## AI & Machine Learning

- Groq API
- Large Language Models (LLMs)
- Prompt Engineering

---

## External APIs

- Wikipedia API

---

## Supporting Libraries

- Requests
- HTTPX
- BeautifulSoup4

---

## Testing

- PyTest

---

## Version Control

- Git
- GitHub

---

# 📂 Repository Structure

```
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
    │
    ├── app
    │   ├── models
    │   ├── routers
    │   ├── services
    │   ├── config.py
    │   └── main.py
    │
    ├── frontend
    │   └── app.py
    │
    ├── tests
    │
    ├── requirements.txt
    ├── networking.db
    ├── .env.example
    └── .gitignore
```

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone <repository-url>
```

---

## Navigate to Source Code

```bash
cd "Source Code"
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a `.env` file inside the **Source Code** directory.

```
API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

Application

```
http://localhost:8501
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🔄 Application Workflow

```
User Profile
      │
      ▼
Event Details
      │
      ▼
Event Analysis
      │
      ▼
Groq LLM Processing
      │
      ▼
Topic Generation
      │
      ▼
Fact Verification
      │
      ▼
Conversation Starters
      │
      ▼
Networking Tips
      │
      ▼
Self Introduction
      │
      ▼
History Logging
      │
      ▼
Feedback Collection
```

---

# 🎯 Project Highlights

- AI-powered networking assistant
- Personalized conversation generation
- Event-aware recommendations
- Fact-checked AI responses
- Modular FastAPI architecture
- Interactive Streamlit interface
- RESTful API services
- Automated testing
- Clean and scalable project structure

---

# 📈 Future Enhancements

- Multi-language conversation generation
- Voice-enabled networking assistant
- LinkedIn profile integration
- Resume analysis
- Calendar and event synchronization
- Real-time speech coaching
- AI-based networking score
- Cloud deployment on Google Cloud Run
- User authentication and profile management

---

# 👨‍💻 Developer

**Dandu Thanishka Reddy**

Google Cloud GenAI Project

---

## ⭐ If you found this project useful, consider giving it a star!