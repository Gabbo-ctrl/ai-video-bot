# video_gen.py placeholder
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import os

def create_video(voiceover_path, output_path="final_video.mp4", video_path="assets/stock_clip.mp4", music_path="assets/background_music.mp3"):
    video = VideoFileClip(video_path).subclip(0, 30)  # Clip to 30s max
    voice = AudioFileClip(voiceover_path)
    music = AudioFileClip(music_path).volumex(0.2)
    
    final_audio = voice.audio.set_duration(video.duration).volumex(1.0).fx(lambda clip: clip.volumex(1))
    combined_audio = final_audio.set_audio(music)

    final_video = video.set_audio(voice)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    return output_path
