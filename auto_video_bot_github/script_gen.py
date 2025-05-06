# script_gen.py placeholder
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_script(topic):
    prompt = f"Write a viral short-form video script under 200 words on this topic: {topic}. Use a casual, fast-paced tone."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a content writer for viral short-form videos."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()
