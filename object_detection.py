import cv2
import torch
import pandas as pd

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Small version of YOLOv5

# Path to the input video
video_path = "C:\VizExperts\Test.mp4"
cap = cv2.VideoCapture(video_path)

# Process video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run object detection on the frame
    results = model(frame)
    results.render()  # Annotate frame with detections

    # Display frame with detections
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to stop
        break

cap.release()
cv2.destroyAllWindows()
