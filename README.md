# 🤝 Personalized Networking Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit">
  <img src="https://img.shields.io/badge/Groq-AI-orange">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

---


### 🚀 AI-Powered Networking Companion for Smarter Professional Conversations

---

## 📖 Overview

The **Personalized Networking Assistant** is an AI-powered web application developed as part of the **Google Cloud GenAI Project**. It helps students, professionals, and job seekers prepare for networking events by generating personalized conversation starters, professional self-introductions, networking tips, and fact-verified responses using **Groq LLMs**.


## ✨ Features

- 💬 AI-powered conversation starter generation
- 🎤 Personalized self-introduction generator
- 💡 Smart networking tips
- 📅 Event-specific conversation suggestions
- 🧠 Topic and event analysis
- 🔍 Fact verification using Wikipedia API
- 📚 Conversation history management
- ⭐ User feedback collection
- 🌐 Interactive Streamlit interface
- ⚡ FastAPI REST API backend

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| 🐍 Programming | Python |
| ⚡ Backend | FastAPI, Uvicorn, Pydantic |
| 🎨 Frontend | Streamlit |
| 🤖 AI | Groq API |
| 🌐 APIs | Wikipedia API |
| 📦 Libraries | Requests, HTTPX, BeautifulSoup4, python-dotenv |
| 🧪 Testing | PyTest |
| 🔧 Tools | Git, GitHub, VS Code |

---

## 📂 Project Structure

```text
Source Code
│
├── app
├── frontend
├── tests
├── networking.db
├── requirements.txt
└── .env.example
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Source Code

```bash
cd "Source Code"
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure Environment Variables

Before running the application, create a **`.env`** file by copying the **`.env.example`** file.

```powershell
Copy-Item .env.example .env
```

Open the newly created **`.env`** file and replace the placeholder with the API key provided by the project owner.

```env
API_KEY=your_provided_api_key
```

> ⚠️ **Note:** The application requires a valid API key in the `.env` file to run successfully.

### Run Backend

```bash
uvicorn app.main:app --reload
```

📌 API Documentation

```
http://127.0.0.1:8000/docs
```

### Run Frontend

```bash
streamlit run frontend/app.py
```

🌐 Application URL

```
http://localhost:8501
```

---

## 🎯 Highlights

- 🤖 Powered by Groq Large Language Models
- ⚡ FastAPI backend with Streamlit frontend
- 💬 Personalized AI conversation generation
- 🔍 Wikipedia-based fact verification
- 📚 Conversation history management
- 🧩 Modular and scalable architecture

---

## 🔮 Future Enhancements

- 🌍 Multi-language support
- 🎙️ Voice-enabled conversations
- 📅 Calendar integration
- 🤝 LinkedIn profile integration
- ☁️ Cloud deployment

---

## 👥 Project Team

| 👤 Team Member | 🎯 Contribution |
|----------------|-----------------|
| **Garudappagari Pallavi** | 👑 Team Lead, Project Planning & Coordination |
| **Dandu Thanishka Reddy** | 🤖 AI Integration, Backend Development & API Services |
| **Gunturi Teja Sekhar Naidu** | ⚙️ Backend Development, Testing & GitHub Integration |
| **Chandana Ganuga** | 🎨 Frontend Development, UI Design & Documentation |

🎓 **Google Cloud GenAI Project**

---