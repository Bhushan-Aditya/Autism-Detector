# AI-Driven Early Detection of Autism in Toddlers Using Video-Based Multimodal Cues

## 📦 Dependencies / Requirements

This project uses the following main Python libraries:

- **opencv-python**: For video file reading and frame extraction.
- **mediapipe**: For face mesh (eye/gaze tracking), pose, and hand landmark detection.
- **numpy**: For numerical operations and array handling.
- **matplotlib**: For plotting risk factor bar charts.
- **seaborn**: For enhanced data visualization.
- **streamlit**: For the optional web-based user interface.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 📁 File Descriptions

- `main.py` — Command-line entry point. Orchestrates video analysis and risk reporting.
- `demo_app.py` — Streamlit web app for uploading a video and viewing the risk report interactively.
- `video_utils.py` — Functions for loading videos and extracting frames using OpenCV.
- `eye_contact.py` — Uses MediaPipe Face Mesh to estimate if the child is making eye contact.
- `repetitive_behavior.py` — Uses MediaPipe Pose to detect repetitive hand/arm movements (e.g., hand-flapping).
- `gesture_delay.py` — Uses pose and hand landmarks to detect gestures (e.g., pointing, waving) as a proxy for language delay.
- `risk_report.py` — Aggregates detection results, estimates risk level, and generates a visual report.
- `requirements.txt` — List of required Python packages.
- `.gitignore` — Specifies files and folders to be ignored by git (e.g., venv, __pycache__, temp files).

---

## ⚙️ Working / How to Use

### 1. **Command-Line Usage**

Analyze a video and view the risk report:
```bash
python main.py path_to_your_video.mp4
```

### 2. **Streamlit Web App**

Launch the web interface:
```bash
streamlit run demo_app.py
```
- Upload a short video (mp4, mov, avi) of your toddler.
- The app will analyze the video and display a risk report with a bar chart and interpretation.

---

## 🚦 How It Works (Overview)

1. **Video Input**: Loads a video and extracts frames for analysis.
2. **Multimodal Feature Analysis**:
   - **Eye Contact**: Detects if the child is looking at the camera/caregiver using face mesh and gaze estimation.
   - **Repetitive Movements**: Detects repetitive hand/arm movements using pose estimation.
   - **Gestures**: Detects pointing or waving gestures as a proxy for language delay.
3. **Risk Estimation & Report**: Aggregates the above features into a risk score (low/moderate/high) and generates a visual report.

---

## 🔮 Future Scope

- **Accuracy Evaluation**: Integrate with labeled datasets to measure and improve detection accuracy.
- **Advanced Models**: Replace heuristics with machine learning or deep learning models for more robust detection.
- **More Features**: Add detection for additional ASD-related behaviors (e.g., lack of response to name, unusual postures).
- **Privacy Enhancements**: Add face blurring or anonymization options.
- **Report Export**: Allow users to download the risk report as a PDF or image.
- **Mobile App**: Develop a mobile version for easier video capture and analysis.
- **Clinical Validation**: Collaborate with pediatricians for real-world validation and feedback.

---

## ⚠️ Disclaimer

This tool is a research prototype and **not a diagnostic device**. Results are for informational purposes only. For concerns about a child’s development, always consult a qualified healthcare provider.
