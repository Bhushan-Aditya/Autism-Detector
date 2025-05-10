import cv2

# Utility to extract frames from a video file or webcam

def extract_frames(video_path, every_n=1, max_frames=None):
    """
    Yields frames from the video at video_path every_n frames.
    If max_frames is set, stops after that many frames.
    """
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    yielded = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % every_n == 0:
            yield frame
            yielded += 1
            if max_frames and yielded >= max_frames:
                break
        frame_count += 1
    cap.release()

# For webcam usage, you can use video_path=0 