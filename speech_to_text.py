import os
import whisper

# Set the FFmpeg binary path explicitly
os.environ["PATH"] += os.pathsep + r"C:\Users\HP\Downloads\ffmpeg-7.1-full_build\ffmpeg-7.1-full_build\bin"

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
audio_file = r"C:\VizExperts\extracted_audio.wav"  # Path to your audio file
result = model.transcribe(audio_file)

# Save the transcription to a text file
output_file = r"C:\VizExperts\script.txt"  # Path to save the output text
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result["text"])

print(f"Transcription saved to {output_file}")
