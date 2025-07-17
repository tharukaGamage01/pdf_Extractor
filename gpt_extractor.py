

import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_with_gpt(text):
    prompt = f"""
    Extract hotel details and return JSON with this structure:
    {{
        "hotel_name": "", "hotel_location": "", "hotel_contact": "",
        "rate_seasons": [{{"season": "", "start_date": "", "end_date": "", "rates": {{"RO": "", "BB": "", "HB": "", "FB": ""}}}}],
        "room_categories": [{{"type": "", "description": "", "size": ""}}],
        "meal_plans": [{{"plan": "", "description": "", "rate": ""}}],
        "check_in_time": "", "check_out_time": "",
        "child_policy": "", "cancellation_policy": ""
    }}
    TEXT: {text}
    """
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return res.choices[0].message.content
