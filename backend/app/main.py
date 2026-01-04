from fastapi import FastAPI
import sys
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file (assuming it's in the root or backend root)
# The .env is in the project root: .../rag-personal ai/.env
# This file is at .../rag-personal ai/backend/app/main.py
# So we need to look 2 levels up for .env
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

sys.path.insert(0, str(Path(__file__).parent.parent))

from api import upload, chat, health

app = FastAPI(title="RAG Personal AI Assistant")

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(health.router, tags=["Health"])

@app.get("/")
def root():
    return {"message": "RAG Backend is running 🚀"}
