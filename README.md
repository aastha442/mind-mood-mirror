# 🧠 Mind Mood Mirror

**Real-time emotion tracker using facial expressions and voice tone.**
Built with Python, DeepFace, Streamlit, and SpeechRecognition — this app helps you reflect on your mood over time through auto-logged emotions and engaging visualizations.

---

## 📹 Features

* 📽️ Real-time facial emotion detection via webcam (DeepFace)
* 🎤 Voice tone recognition using microphone input
* 📊 Mood frequency chart (bar graph)
* 🔢 Emotion timeline (line graph over time)
* 📋 CSV-based mood logging (local)
* 😁 Emoji-enhanced emotion mapping
* ✨ Interactive frontend with Streamlit



## 🛠️ Tech Stack

| Tool              | Purpose                        |
| ----------------- | ------------------------------ |
| Python            | Core programming language      |
| DeepFace          | Facial emotion recognition     |
| SpeechRecognition | Voice tone analysis            |
| OpenCV            | Webcam integration             |
| Streamlit         | Interactive UI dashboard       |
| Pandas            | Data manipulation and analysis |
| Matplotlib        | Mood timeline charting         |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aastha442/mind-mood-mirror.git
cd mind-mood-mirror
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the live emotion tracker (opens webcam + mic)

```bash
python mood_detector.py
```

### 4. Launch the dashboard

```bash
streamlit run streamlit_app.py

---

## 🧠 Future Enhancements

* Voice emotion timeline (line graph)
* Sentiment analysis summary card ("You were mostly happy today")
* REST API to expose logs for mobile/web clients
* Auto-alert if sad/negative mood persists

---


