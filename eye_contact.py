import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

# Indices for left and right iris in MediaPipe Face Mesh
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

# Indices for left and right eye corners
LEFT_EYE = [33, 133]
RIGHT_EYE = [362, 263]

def estimate_gaze_direction(landmarks, image_w, image_h):
    # Get eye corner and iris center positions
    left_eye = np.mean([[landmarks[i].x * image_w, landmarks[i].y * image_h] for i in LEFT_EYE], axis=0)
    right_eye = np.mean([[landmarks[i].x * image_w, landmarks[i].y * image_h] for i in RIGHT_EYE], axis=0)
    left_iris = np.mean([[landmarks[i].x * image_w, landmarks[i].y * image_h] for i in LEFT_IRIS], axis=0)
    right_iris = np.mean([[landmarks[i].x * image_w, landmarks[i].y * image_h] for i in RIGHT_IRIS], axis=0)
    # Simple heuristic: if iris center is close to midpoint between eye corners, assume looking forward
    left_ratio = np.linalg.norm(left_iris - left_eye) / np.linalg.norm(left_eye - right_eye)
    right_ratio = np.linalg.norm(right_iris - right_eye) / np.linalg.norm(left_eye - right_eye)
    # If both ratios are within a threshold, assume looking at camera
    return 0.10 < left_ratio < 0.40 and 0.10 < right_ratio < 0.40

def detect_eye_contact(frame):
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True) as face_mesh:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            h, w, _ = frame.shape
            return estimate_gaze_direction(landmarks, w, h)
        return False 