
import os
import sys
from dotenv import load_dotenv

# Add backend to path to import services
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from backend.services.llm import generate_answer

def test_connection():
    load_dotenv()
    print("Testing OpenRouter Connection...")
    
    key = os.getenv("OPENROUTER_API_KEY")
    if not key or "your_openrouter_key" in key:
        print(f"❌ OPENROUTER_API_KEY is not set correctly in .env. Found: {key}")
        return

    try:
        response = generate_answer("What is 2+2?", "Math context")
        print(f"✅ Success! Response: {response}")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_connection()
