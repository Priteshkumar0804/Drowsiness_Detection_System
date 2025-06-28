import os
import numpy as np
from playsound import playsound
import threading

# Path to the alarm sound file
alarm_path = os.path.join("assets", "alarm.mp3")

# -----------------------
# EAR Calculation
# -----------------------
def calculate_EAR(eye):
    """
    Calculates the Eye Aspect Ratio (EAR)
    :param eye: List of 6 eye landmark coordinates
    :return: EAR value
    """
    A = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
    B = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
    C = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
    ear = (A + B) / (2.0 * C)
    return ear

# -----------------------
# MAR Calculation
# -----------------------
def calculate_MAR(mouth):
    """
    Calculates the Mouth Aspect Ratio (MAR)
    :param mouth: List of 6 mouth landmark coordinates
    :return: MAR value
    """
    A = np.linalg.norm(np.array(mouth[1]) - np.array(mouth[5]))
    B = np.linalg.norm(np.array(mouth[2]) - np.array(mouth[4]))
    C = np.linalg.norm(np.array(mouth[0]) - np.array(mouth[3]))
    mar = (A + B) / (2.0 * C)
    return mar

# -----------------------
# Sound Alert Control
# -----------------------
def sound_alert():
    """
    Plays the alarm sound in a separate thread.
    """
    threading.Thread(target=playsound, args=(alarm_path,), daemon=True).start()

def stop_sound():
    """
    playsound has no built-in stop function, so this is just a placeholder.
    """
    pass
