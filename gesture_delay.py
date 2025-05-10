import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands

def detect_gestures(frames, min_gestures=1):
    """
    Detects pointing or waving gestures in a sequence of frames.
    Returns True if at least min_gestures are detected.
    """
    gesture_count = 0
    with mp_pose.Pose(static_image_mode=True) as pose, mp_hands.Hands(static_image_mode=True) as hands:
        for frame in frames:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pose_results = pose.process(rgb)
            hand_results = hands.process(rgb)
            # Simple heuristic: if hand is above shoulder, count as a gesture
            if pose_results.pose_landmarks:
                landmarks = pose_results.pose_landmarks.landmark
                # Right wrist (16), right shoulder (12)
                if landmarks[16].y < landmarks[12].y:
                    gesture_count += 1
            # If hand landmarks detected, count as a gesture
            if hand_results.multi_hand_landmarks:
                gesture_count += 1
    return gesture_count >= min_gestures 