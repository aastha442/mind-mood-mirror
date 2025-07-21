import cv2
from deepface import DeepFace
from datetime import datetime
import time
import csv
import speech_recognition as sr
import audioop

# ----------------------
# Voice Emotion Function
# ----------------------
def detect_voice_emotion(duration=3):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙 Listening for voice tone...")
        audio = recognizer.listen(source, phrase_time_limit=duration)

    try:
        raw_data = audio.get_raw_data()
        rms = audioop.rms(raw_data, 2)  # Root Mean Square of audio signal

        # Heuristic thresholds (tweakable)
        if rms < 300:
            return "calm"
        elif rms < 1000:
            return "neutral"
        else:
            return "excited"

    except Exception as e:
        print("Voice tone detection failed:", e)
        return "unknown"

# ----------------------
# Webcam + Facial Setup
# ----------------------
cap = cv2.VideoCapture(0)
print("Press 'q' to quit.\nStarting mood monitoring...")

mood_log = []
last_logged_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Facial emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        facial_emotion = result[0]['dominant_emotion']

        # Show facial emotion on webcam feed
        cv2.putText(frame, f"Face: {facial_emotion}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Log every 10 seconds
        current_time = time.time()
        if current_time - last_logged_time >= 10:
            timestamp = datetime.now().strftime("%H:%M:%S")

            # Voice tone
            voice_emotion = detect_voice_emotion(duration=3)

            # Append to log
            mood_log.append({
                'time': timestamp,
                'facial_emotion': facial_emotion,
                'voice_emotion': voice_emotion
            })

            print(f"[{timestamp}] Face: {facial_emotion} | Voice: {voice_emotion}")
            last_logged_time = current_time

    except Exception as e:
        print("Facial detection failed:", e)

    # Show video
    cv2.imshow("Mind Mood Mirror", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ----------------------
# Save to CSV
# ----------------------
with open('mood_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Facial_Emotion', 'Voice_Emotion'])
    for log in mood_log:
        writer.writerow([log['time'], log['facial_emotion'], log['voice_emotion']])

print("✅ Mood log saved to mood_log.csv")
