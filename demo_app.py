import streamlit as st
import tempfile
from video_utils import extract_frames
from eye_contact import detect_eye_contact
from repetitive_behavior import detect_repetitive_hand_movement
from gesture_delay import detect_gestures
from risk_report import generate_risk_report

st.title("AI-Driven Early Detection of Autism in Toddlers (Demo)")

uploaded_file = st.file_uploader("Upload a short video of your toddler (mp4, mov, avi)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    st.info("Processing video...")
    frames = list(extract_frames(tmp_path, every_n=5, max_frames=60))
    if not frames:
        st.error("No frames extracted from video.")
    else:
        eye_contact = any(detect_eye_contact(f) for f in frames[:10])
        repetitive = detect_repetitive_hand_movement(frames)
        gestures = detect_gestures(frames)
        st.success("Analysis complete!")
        fig, risk_level, risk_factors = generate_risk_report(eye_contact, repetitive, gestures)
        st.pyplot(fig)
        st.write(f"\n**Estimated Risk Level:** {risk_level}")
        st.write("- If two or more risk factors are flagged, consider consulting a developmental pediatrician.")
        st.write("**Risk Factors:**")
        for k, v in risk_factors.items():
            st.write(f"- {k}: {'Yes' if v else 'No'}") 