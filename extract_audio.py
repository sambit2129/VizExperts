from moviepy.editor import VideoFileClip

# Path to your input video
video_path = "C:\VizExperts\Test.mp4"

# Load the video and extract audio
video = VideoFileClip(video_path)
audio_path = "extracted_audio.wav"
video.audio.write_audiofile(audio_path)

print(f"Audio extracted and saved to: {audio_path}")
