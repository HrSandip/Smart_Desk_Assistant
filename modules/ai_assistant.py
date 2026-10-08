import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Exact .env location
ENV_FILE = PROJECT_ROOT / ".env"

print("Loading .env from:", ENV_FILE)

# Force .env values to override old environment variables
load_dotenv(ENV_FILE, override=True)

api_key = os.getenv("GROQ_API_KEY", "").strip()

print("API key found:", bool(api_key))
print("API key prefix:", api_key[:4] if api_key else "NONE")
print("API key length:", len(api_key))

if not api_key:
    raise ValueError(
        f"GROQ_API_KEY not found in {ENV_FILE}"
    )

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-120b"


def ask_ai(user_message):

    try:

        print("Sending request to Groq...")
        print("Model:", MODEL)

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful voice-controlled smart desk assistant. "
                        "Give clear, concise and useful answers suitable for voice output."
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.3,
            max_tokens=300
        )

        answer = response.choices[0].message.content.strip()

        print("Groq response received.")

        return answer

    except Exception as e:

        print("Groq API error:", e)

        return "Sorry, I could not connect to the AI service."