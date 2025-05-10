import sys
from video_utils import extract_frames
from eye_contact import detect_eye_contact
from repetitive_behavior import detect_repetitive_hand_movement
from gesture_delay import detect_gestures
from risk_report import generate_risk_report

# Usage: python main.py <video_path>
def main(video_path):
    # Extract frames (sample every 5th frame, up to 60 frames for speed)
    frames = list(extract_frames(video_path, every_n=5, max_frames=60))
    if not frames:
        print("No frames extracted from video.")
        return
    # Eye contact: check in first 10 frames
    eye_contact = any(detect_eye_contact(f) for f in frames[:10])
    # Repetitive movement: check all frames
    repetitive = detect_repetitive_hand_movement(frames)
    # Gestures: check all frames
    gestures = detect_gestures(frames)
    # Report
    generate_risk_report(eye_contact, repetitive, gestures)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <video_path>")
    else:
        main(sys.argv[1]) 