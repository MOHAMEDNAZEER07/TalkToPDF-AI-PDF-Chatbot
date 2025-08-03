from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-pro")

def get_gemini_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"🔥 Gemini error: {str(e)}"
    
print(f"Using Gemini model: {model.model_name}")
print("Embedder loaded:", embedder.__class__.__name__)

