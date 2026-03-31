import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "GEMINI_API_KEY is not set. "
        "Add it to your .env file or set it as an environment variable."
    )

genai.configure(api_key=api_key)

models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)
