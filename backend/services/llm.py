from openai import OpenAI
import os
from dotenv import load_dotenv

# Load env vars if not already loaded (useful for standalone testing)
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key or "your_openrouter_key" in api_key:
    print("❌ ERROR: OPENROUTER_API_KEY is missing or invalid in .env")

# 🔐 Make sure OPENROUTER_API_KEY is set in .env
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Default to a model, can be overridden by env
MODEL_NAME = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-001")

def generate_answer(question: str, context: str) -> str:
    system_prompt = """You are a helpful assistant.
Answer the question using ONLY the context below. If the answer is not in the context, say so."""

    user_message = f"""Context:
{context}

Question:
{question}
"""

    print(f"DEBUG: Using model: {MODEL_NAME}", flush=True)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "Sorry, I encountered an error generating the response."
