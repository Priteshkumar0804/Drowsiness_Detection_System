import pygame
import os
import numpy as np

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
    Plays an alarm sound in a loop if not already playing.
    """
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(alarm_path)
        pygame.mixer.music.play(loops=-1)

def stop_sound():
    """
    Stops the alarm sound if it's playing.
    """
    if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
