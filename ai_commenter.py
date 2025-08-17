# Gemini AI integration
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_ai_comment(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(f"Write a clever, flirty comment for this Hinge prompt, i need direct single comment response to paste your response direct on Hinge : {prompt}")
    return response.text.strip()
