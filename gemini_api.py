import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def get_insights_from_text(text):
    prompt = f"""
You are a smart assistant. Analyze the following PDF content:

{text[:8000]}  # Limit input size for Gemini

Please provide:
1. A brief summary
2. 3–5 key insights
3. Any potential red flags or interesting findings

Format clearly using headings.
"""
    response = model.generate_content(prompt)
    return response.text
