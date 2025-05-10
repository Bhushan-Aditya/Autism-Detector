import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

# For simplicity, we check for repetitive up/down hand movement (e.g., hand-flapping)
def detect_repetitive_hand_movement(frames, threshold=10, min_cycles=2):
    """
    frames: iterable of frames (BGR)
    threshold: minimum pixel movement to count as a cycle
    min_cycles: minimum number of up/down cycles to flag as repetitive
    Returns: True if repetitive movement detected, else False
    """
    y_positions = []
    with mp_pose.Pose(static_image_mode=True) as pose:
        for frame in frames:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)
            if results.pose_landmarks:
                # Use right wrist (landmark 16) as example
                wrist = results.pose_landmarks.landmark[16]
                h, w, _ = frame.shape
                y_positions.append(wrist.y * h)
            else:
                y_positions.append(None)
    # Remove None values
    y_positions = [y for y in y_positions if y is not None]
    if len(y_positions) < 5:
        return False
    # Count up/down cycles
    diffs = np.diff(y_positions)
    sign_changes = (diffs[:-1] * diffs[1:] < 0)
    large_enough = (np.abs(diffs[:-1]) > threshold) & (np.abs(diffs[1:]) > threshold)
    cycles = np.sum(sign_changes & large_enough)
    return cycles >= min_cycles 