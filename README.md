# 💤 Drowsiness Detection System

> 🚗 Real-Time AI-Powered Driver Monitoring System with Streamlit Interface  
> ⚠️ Detects **drowsiness**, **yawning**, and alerts users with **sound** & **visual cues**

---

## 📌 Overview

**Drowsiness Detection System** is an intelligent application that uses facial landmark analysis to detect driver fatigue in real time. It helps prevent accidents by monitoring **eye** and **mouth activity**, displaying **EAR & MAR values**, and issuing **alerts** through sound and visuals.

Built with:
- 🔍 **MediaPipe FaceMesh** for landmark detection
- 🎨 **Streamlit** for the front-end UI
- 🧠 **OpenCV** for image processing
- 🔊 **Pygame** for audio alerts
- 📊 **Matplotlib** for real-time graphs

---

## 🎯 Features

✅ Real-time webcam feed with facial landmark detection  
🔁 Customizable **EAR** (Eye Aspect Ratio) and **MAR** (Mouth Aspect Ratio) thresholds  
📈 Live EAR & MAR line graph next to video feed  
🟥 Bounding box with live status: **Awake**, **Drowsy**, **Sleeping**  
🔊 Sound alert with looping alarm on detection  
🖱️ Simple Start/Stop detection buttons via Streamlit  
📁 Organized modular code with clean structure

---

## 📁 Project Structure

drowsiness_detection_system/
├── app.py # Streamlit UI
├── video_processor.py # Camera frame logic & facial analysis
├── utils.py # EAR, MAR, sound logic
├── assets/
│ └── alarm.mp3 # Custom alarm sound
├── snapshots/ # (Optional) For saving alert screenshots
├── README.md # You're reading it!



---

## 🧠 Detection Logic

| Metric | Description |
|--------|-------------|
| EAR    | Eye Aspect Ratio – detects blinking or eye closure |
| MAR    | Mouth Aspect Ratio – detects yawning or mouth opening |

### 🔎 Status Logic:
| EAR | MAR | Status     | Color      |
|-----|-----|------------|------------|
| > threshold | any  | **Awake**    | 🟩 Green     |
| < threshold | < threshold | **Drowsy**   | 🟧 Orange    |
| < threshold | > threshold | **Sleeping** | 🟥 Red       |

---

## ⚙️ Setup Instructions

1. 🚀 Clone Repository


git clone https://github.com/Priteshkumar0804/drowsiness-detection-system.git
cd drowsiness-detection-system

2. 🧩 Install Dependencies

pip install -r requirements.txt

3. 🎵 Add Alarm Sound

Place your custom alert sound in the assets/ folder and name it:
assets/alarm.mp3

4. ▶️ Run the App

streamlit run app.py



🔧 Customization Options

Adjust EAR/MAR thresholds from the sidebar
Replace alarm sound with your own in utils.py
Enhance visuals with themes in Streamlit config

📦 Dependencies

Python 3.10+
OpenCV
MediaPipe
Streamlit
Pygame
Matplotlib


📄 License
This project is open source and available under the MIT License.

🙋‍♂️ Author
Pritesh Kumar
GitHub: https://github.com/Priteshkumar0804

⭐ Show Your Support

If you like this project, don't forget to:

⭐ Star this repo
🛠️ Suggest enhancements via Issues or PRs

