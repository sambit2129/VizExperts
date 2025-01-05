# VizExperts
Here’s the complete README file for your project, formatted for easy copy-paste:

```markdown


This project automates the creation of a PowerPoint presentation by extracting audio from a video, transcribing it using OpenAI's Whisper model, and integrating generated content along with images. The PowerPoint presentation consists of slides with a title, generated script, and relevant images extracted from the video.

## Project Overview

The project follows these key steps:
1. **Extract audio** from a video.
2. **Transcribe the audio** using the Whisper model.
3. **Create a PowerPoint presentation** with the transcription text and an image from the video.

## Requirements

- Python 3.x
- `moviepy` for audio extraction
- `whisper` for transcription
- `opencv-python` for video frame extraction
- `python-pptx` for PowerPoint generation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/industrial-equipment-overview.git
   cd industrial-equipment-overview
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **FFmpeg**: Make sure you have FFmpeg installed and its path added to the system environment variable.

## Usage

1. **Extract audio from the video**:
   - Place your video file (`Test.mp4`) in the project directory or update the path in the script.
   - Run the script to extract audio:
     ```bash
     python extract_audio.py
     ```

2. **Transcribe the audio**:
   - Make sure your transcription file (`script.txt`) is available.
   - Run the script to transcribe the audio:
     ```bash
     python transcribe_audio.py
     ```

3. **Generate PowerPoint Presentation**:
   - Ensure the transcription text file (`script.txt`) and an image (`frame_52.jpg`) are ready.
   - Run the script to generate the PowerPoint presentation:
     ```bash
     python generate_presentation.py
     ```

The generated PowerPoint will be saved as `output_presentation.pptx`.

## Files

- `extract_audio.py`: Extracts audio from a video file and saves it as `extracted_audio.wav`.
- `transcribe_audio.py`: Transcribes the audio to text using Whisper and saves it in `script.txt`.
- `generate_presentation.py`: Creates a PowerPoint presentation with the transcription and an image.

## Contributing

Feel free to fork this project, make changes, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy and paste this directly into your README file. Make sure to replace the `your-username` placeholder with your actual GitHub username.
