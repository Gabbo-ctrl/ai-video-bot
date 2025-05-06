import os

# === Create folders ===
os.makedirs("assets", exist_ok=True)

# === Write .env template ===
with open(".env", "w") as f:
    f.write("OPENAI_API_KEY=your_openai_key\nELEVENLABS_API_KEY=your_elevenlabs_key\n")

# === Write requirements.txt ===
with open("requirements.txt", "w") as f:
    f.write("openai\nmoviepy\nrequests\nwhisper\npython-dotenv\n")

# === main.py ===
with open("main.py", "w") as f:
    f.write('''from script_gen import generate_script
from voiceover_gen import generate_voiceover
from video_gen import create_video
from subtitle_gen import generate_subtitles
from tiktok_upload import upload_to_tiktok
import random

topics = [
    "Pope conspiracy",
    "Alien conspiracy",
    "What trends are ruining your brain",
    "Brainrot from TikTok",
    "Why society is collapsing"
]

def main():
    topic = random.choice(topics)
    print(f"[+] Topic: {topic}")
    script = generate_script(topic)
    print(f"[+] Script:\\n{script}")
    voice_path = generate_voiceover(script)
    print(f"[+] Voiceover generated: {voice_path}")
    subtitle_text = generate_subtitles(voice_path)
    print(f"[+] Subtitles: {subtitle_text}")
    final_video_path = create_video(voice_path)
    print(f"[+] Video created: {final_video_path}")
    upload_to_tiktok(final_video_path, caption=topic)

if __name__ == "__main__":
    main()
''')

# === script_gen.py ===
with open("script_gen.py", "w") as f:
    f.write('''import openai
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
''')

# === voiceover_gen.py ===
with open("voiceover_gen.py", "w") as f:
    f.write('''import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")

def generate_voiceover(text, output_path="voice.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):
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
''')

# === video_gen.py ===
with open("video_gen.py", "w") as f:
    f.write('''from moviepy.editor import VideoFileClip, AudioFileClip

def create_video(voiceover_path, output_path="final_video.mp4", video_path="assets/stock_clip.mp4", music_path="assets/background_music.mp3"):
    video = VideoFileClip(video_path).subclip(0, 30)
    voice = AudioFileClip(voiceover_path)
    music = AudioFileClip(music_path).volumex(0.2)
    final_video = video.set_audio(voice)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
''')

# === subtitle_gen.py ===
with open("subtitle_gen.py", "w") as f:
    f.write('''import whisper

def generate_subtitles(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]
''')

# === tiktok_upload.py ===
with open("tiktok_upload.py", "w") as f:
    f.write('''def upload_to_tiktok(video_path, caption=""):
    print(f"[!] Uploading {video_path} to TikTok with caption: {caption}")
    print("[+] Upload complete (stubbed)")
''')

print("✅ All files created. Now install dependencies and run main.py")
