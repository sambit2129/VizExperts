import cv2

def extract_frames(video_file, frame_times):
    video = cv2.VideoCapture(video_file)
    fps = video.get(cv2.CAP_PROP_FPS)
    images = []

    for time in frame_times:
        frame_number = int(time * fps)
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video.read()
        if ret:
            image_path = f"frame_{time}.jpg"
            cv2.imwrite(image_path, frame)
            images.append(image_path)

    video.release()
    return images

# Usage
video_file = "C:\VizExperts\Test.mp4"
frame_times = [30]  # Seconds where the person points to equipment
image_paths = extract_frames(video_file, frame_times)
print("Extracted Images:", image_paths)
