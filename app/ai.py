import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_eco_tip():
    prompt = (
        "Give me a short, practical, and actionable eco-friendly tip for sustainable living. "
        "Keep it under 30 words."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        temperature=0.7,
    )
    tip = response.choices[0].message['content'].strip()
    return tip
