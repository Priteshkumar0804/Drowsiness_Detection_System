import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from video_processor import process_video_frame

st.set_page_config(page_title="Driver Drowsiness Detection", layout="wide")
st.title("👁️ Driver Drowsiness Detection System")

# Sidebar settings
st.sidebar.subheader("🔧 Detection Settings")
ear_thresh = st.sidebar.slider("Set EAR Threshold", 0.1, 0.4, 0.25, 0.01)
mar_thresh = st.sidebar.slider("Set MAR Threshold", 0.3, 1.0, 0.7, 0.01)
play_sound = st.sidebar.checkbox("Enable Sound Alert", value=True)

start_detection = st.sidebar.button("▶️ Start Detection")
stop_detection = st.sidebar.button("⏹️ Stop Detection")

# Columns: Left = Video, Right = Graph
col1, col2 = st.columns(2)
video_placeholder = col1.empty()
graph_placeholder = col2.empty()

ear_values, mar_values = [], []

if start_detection:
    try:
        for frame, ear, mar in process_video_frame(ear_thresh, mar_thresh, play_sound):
            # Show video
            video_placeholder.image(frame, channels="BGR", use_container_width=True)

            # Save values
            ear_values.append(ear)
            mar_values.append(mar)

            # Keep only last 100 points
            if len(ear_values) > 100:
                ear_values.pop(0)
                mar_values.pop(0)

            # Plot graph
            fig, ax = plt.subplots()
            ax.plot(ear_values, label="EAR", color="blue")
            ax.plot(mar_values, label="MAR", color="red")
            ax.axhline(y=ear_thresh, color='blue', linestyle='--', label='EAR Threshold')
            ax.axhline(y=mar_thresh, color='red', linestyle='--', label='MAR Threshold')
            ax.set_ylim(0, 1.2)
            ax.set_title("Real-time EAR and MAR Values")
            ax.set_xlabel("Frames")
            ax.set_ylabel("Ratio")
            ax.legend()
            graph_placeholder.pyplot(fig)

            if stop_detection:
                break
    except Exception as e:
        st.error(f"❌ Error: {e}")
