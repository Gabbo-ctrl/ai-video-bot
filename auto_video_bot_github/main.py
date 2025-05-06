import openai
import random
import requests
import moviepy.editor as mp
import time

# Import your API keys from the .env file (ensure you've set them)
from dotenv import load_dotenv
import os

load_dotenv()

# Set up your API keys
openai.api_key = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
TIKTOK_EMAIL = os.getenv('TIKTOK_EMAIL')
TIKTOK_PASSWORD = os.getenv('TIKTOK_PASSWORD')

# Sample topics to pick from
topics = [
    "The Pope conspiracy: The Vatican and its secrets",
    "The Alien conspiracy: Are we being visited by extraterrestrials?",
    "What trends are controlling society today?",
    "The brainrot caused by social media",
    "How TikTok rewires your brain"
]

# Pick a random topic
selected_topic = random.choice(topics)
print(f"Selected topic: {selected_topic}")

# Function to generate script using OpenAI (GPT)
def generate_script(topic):
    prompt = f"Write a short script about {topic}. Keep it under 300 words."
    response = openai.Completion.create(
        engine="text-davinci-003",  # Adjust as needed
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

# Generate the script
script = generate_script(selected_topic)
print(f"Generated script: {script}")

# Generate a voiceover (using a service like ElevenLabs)
# Replace with actual API call to ElevenLabs or TTS service
def generate_voiceover(script):
    # Here, you would send the script to ElevenLabs or similar
    # and get back an audio file.
    pass

# Create video with the script and voiceover
def create_video(script, background_music="background_music.mp3", video_clip="stock_clip.mp4"):
    video = mp.VideoFileClip(video_clip)
    # Add background music and voiceover
    audio = mp.AudioFileClip(background_music)
    video = video.set_audio(audio)
    video.write_videofile("output_video.mp4", codec="libx264")

# Run the video creation
create_video(script)

# Upload to TikTok (using a browser automation tool like Selenium)
def upload_to_tiktok(video_path):
    # Use Selenium to automate TikTok login and upload
    pass

# Upload the video
upload_to_tiktok("output_video.mp4")

print("Video successfully uploaded to TikTok!")

