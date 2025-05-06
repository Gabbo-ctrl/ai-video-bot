# AI Video Bot with Subtitles & TikTok Upload

This project automates the creation of short videos based on conspiracy theories and brainrot topics. It generates scripts, converts them into voiceovers, overlays subtitles, adds background music, and uploads the videos to platforms like TikTok.

## Features
- **Randomized Topics**: Topics like "Pope Conspiracy", "Alien Conspiracy", and "What Trends" are automatically selected.
- **Script Generation**: Uses AI (e.g., OpenAI GPT) to generate a script.
- **Text-to-Speech**: Converts the generated script into a voiceover using ElevenLabs or other TTS services.
- **Subtitles**: Automatically adds subtitles to the video based on the voiceover.
- **Background Music**: A default background music file is added to each video.
- **TikTok Upload**: Uploads the video directly to TikTok, automatically including a caption with the topic.
  
## Requirements

You need to have the following Python packages installed:

- [moviepy](https://pypi.org/project/moviepy/)
- [requests](https://pypi.org/project/requests/)
- [whisper](https://github.com/openai/whisper)
- [openai](https://pypi.org/project/openai/)
- [selenium](https://pypi.org/project/selenium/)

Run the following command to install dependencies:
```bash
pip install -r requirements.txt
