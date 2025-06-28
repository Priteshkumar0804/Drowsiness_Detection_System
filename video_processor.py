import cv2
import mediapipe as mp
import numpy as np
from utils import calculate_EAR, calculate_MAR, sound_alert, stop_sound

# Define facial landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [263, 387, 385, 362, 380, 373]
MOUTH = [61, 81, 311, 291, 78, 308]

# Initialize MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

def process_video_frame(ear_thresh=0.25, mar_thresh=0.7, play_sound=False):
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        status = "No Face"
        avg_ear = 0
        mar = 0

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                landmarks = [(int(pt.x * w), int(pt.y * h)) for pt in face_landmarks.landmark]

                # EAR
                left_ear = calculate_EAR([landmarks[i] for i in LEFT_EYE])
                right_ear = calculate_EAR([landmarks[i] for i in RIGHT_EYE])
                avg_ear = (left_ear + right_ear) / 2.0

                # MAR
                mar = calculate_MAR([landmarks[i] for i in MOUTH])

                # Determine status
                if avg_ear < ear_thresh and mar > mar_thresh:
                    status = "Sleeping"
                    color = (0, 0, 255)
                    if play_sound:
                        sound_alert()
                elif avg_ear < ear_thresh:
                    status = "Drowsy"
                    color = (0, 165, 255)
                    if play_sound:
                        sound_alert()
                else:
                    status = "Awake"
                    color = (0, 255, 0)
                    stop_sound()  # Stop alarm if no longer sleeping

                # Annotate frame
                x, y = landmarks[1]
                cv2.putText(frame, f"Status: {status}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                cv2.rectangle(frame, (x - 50, y - 50), (x + 150, y + 150), color, 2)
        else:
            stop_sound()  # Stop alarm if no face detected

        yield frame, avg_ear, mar

    cap.release()
    stop_sound()  # Ensure alarm stops when camera stops
