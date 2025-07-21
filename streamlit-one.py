import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="Mind Mood Mirror",
    page_icon="🧠",
    layout="wide"
)

# Styled title
st.markdown(
    """
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 3em;'>🧠 Mind Mood Mirror</h1>
        <p style='font-size: 1.2em; color: #6c757d;'>
            Track and reflect on your emotional state in real-time using facial and voice analysis.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load mood log CSV
try:
    df = pd.read_csv("mood_log.csv")

    # Emoji map (optional)
    emoji_map = {
        'angry': "😠", 'disgust': "🤢", 'fear': "😨", 'sad': "😢",
        'neutral': "😐", 'happy': "😄", 'surprise': "😲",
        'calm': "😌", 'excited': "🤩"
    }
    df['Facial_Emoji'] = df['Facial_Emotion'].map(emoji_map)
    df['Voice_Emoji'] = df['Voice_Emotion'].map(emoji_map)

    # Summary cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 😊 Most Frequent Facial Emotion")
        st.success(f"{df['Facial_Emotion'].mode()[0]} {emoji_map.get(df['Facial_Emotion'].mode()[0], '')}")
    with col2:
        st.markdown("### 🎙️ Most Frequent Voice Emotion")
        st.info(f"{df['Voice_Emotion'].mode()[0]} {emoji_map.get(df['Voice_Emotion'].mode()[0], '')}")

    # Mood log table
    with st.expander("📄 Click to Expand: Mood Log Table"):
        st.dataframe(df, use_container_width=True)

    # Bar chart - Facial emotion
    st.markdown("### 📊 Facial Emotion Frequency Chart")
    st.bar_chart(df['Facial_Emotion'].value_counts())

    # Line chart - Facial emotion timeline
    st.markdown("### 📈 Facial Mood Timeline")
    mood_map = {
        'angry': 0, 'disgust': 1, 'fear': 2, 'sad': 3, 'neutral': 4,
        'happy': 5, 'surprise': 6, 'calm': 7, 'excited': 8
    }
    df['Emotion_Num'] = df['Facial_Emotion'].map(mood_map)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Time'], df['Emotion_Num'], marker='o', linestyle='-', color='#4A90E2')
    ax.set_yticks(list(mood_map.values()))
    ax.set_yticklabels(list(mood_map.keys()))
    ax.set_xlabel('Time')
    ax.set_ylabel('Mood')
    ax.set_title('Facial Mood Over Time', fontsize=14)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Mood Log CSV", data=csv, file_name="mood_log.csv", mime="text/csv")

except FileNotFoundError:
    st.error("❌ No mood_log.csv file found. Please run the detector first.")

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center; font-size: 0.9em; color: gray;'>
        Built by Aastha Moudgil | Powered by DeepFace, Streamlit & ❤️
    </div>
    """,
    unsafe_allow_html=True
)
