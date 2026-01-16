
# 🧠 RAG Personal AI Assistant

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Integration-purple)

A powerful **Retrieval-Augmented Generation (RAG) Assistant** that lets you "chat" with your PDF documents. 

It combines **FastAPI** for a robust backend, **ChromaDB** for vector storage, and **Streamlit** for a modern user interface. The AI generation is powered by **OpenRouter**, allowing you to switch between top-tier models like **Gemini 2.0 Flash**, **DeepSeek R1**, **Claude 3.5 Sonnet**, and more!

## ✨ Features

- **📄 Document Ingestion**: Upload PDF documents directly via the UI.
- **🔍 Smart Retrieval**: Automatically chunks, embeds, and indexes your documents using `HuggingFace` embeddings and `ChromaDB`.
- **🤖 Multi-Model AI**: Integrated with **OpenRouter** to give you access to the latest and greatest LLMs without vendor lock-in. 
- **💬 Interactive Chat**: Ask questions, and the AI answers strictly using the context from your uploaded files (reducing hallucinations).
- **🏗️ Modular Architecture**: Clean separation between Frontend (Streamlit) and Backend (FastAPI).

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/JahnaviSingh2005/Rag-ai-assistant.git
cd Rag-ai-assistant
```

### 2. Install Dependencies
Install all required Python packages for both backend and frontend:
```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 3. Configure Environment
Create a `.env` file in the root directory and add your API keys:

```ini
# OpenRouter API Key (Required for Chat)
OPENROUTER_API_KEY=sk-or-v1-your_actual_key_here
OPENROUTER_MODEL=google/gemini-2.0-flash-001  # Change model here easily!

# (Optional) Legacy Gemini Direct Key if needed
GEMINI_API_KEY=your_gemini_key
```

## 🏃‍♂️ How to Run

You will need **two terminal windows** (or tabs) to run the full application.

### Terminal 1: Start the Backend API
```bash
uvicorn backend.app.main:app --reload --port 8000
```
*The API will start at `http://localhost:8000`*  
*Swagger Docs available at `http://localhost:8000/docs`*

### Terminal 2: Start the Frontend UI
```bash
streamlit run frontend/app.py
```
*The app will open automatically in your browser at `http://localhost:8501`*

## 🧪 Testing Connection
We included a script to verify your OpenRouter connection before running the full app:
```bash
python test_openrouter.py
```

## 🛠️ Tech Stack
- **Language**: Python 3
- **Backend Framework**: FastAPI
- **Frontend Framework**: Streamlit
- **Vector Database**: ChromaDB (Local)
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **LLM Provider**: OpenRouter (access to GPT-4, Claude, Gemini, Llama 3, etc.)

---
*Built with ❤️ by Jahnavi Singh*
