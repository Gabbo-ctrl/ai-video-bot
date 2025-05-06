# voiceover_gen.py placeholder
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")

def generate_voiceover(text, output_path="voice.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):  # Adam voice
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    response = requests.post(
        url,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75
            }
        }
    )

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    else:
        raise Exception(f"Voice generation failed: {response.text}")
