import streamlit as st

from face_detector import detect_face_emotion
from text_detector import detect_text_emotion
from speech_detector import detect_speech_emotion
from mood_utils import calculate_overall_mood


st.title("Emotional Sense AI")
st.subheader("Multimodal Emotion Detection & Mood Assistant")


col1, col2 = st.columns(2)

with col1:

    st.header("Emotion Detection")

    if st.button("Detect Face Emotion"):
        face_emotion = detect_face_emotion()
        st.write("Face Emotion:", face_emotion)

    text_input = st.text_input("Enter Text")

    if st.button("Analyze Text"):
        text_emotion, conf = detect_text_emotion(text_input)
        st.write("Text Emotion:", text_emotion)

    if st.button("Analyze Speech"):
        speech_text = detect_speech_emotion()
        st.write("Speech Text:", speech_text)


with col2:

    st.header("Mood Booster")

    if st.button("Motivational Quote"):
        st.success("Believe in yourself. Every step counts.")

    if st.button("Tell me a Joke"):
        st.info("Why don't programmers like nature? Too many bugs.")

    if st.button("Riddle"):
        st.warning("What has keys but can't open locks? A piano.")


st.header("Overall Mood Analysis")

if st.button("Calculate Mood"):

    try:
        overall = calculate_overall_mood(face_emotion, text_emotion, "neutral")
        st.success(f"Overall Mood: {overall}")
    except:
        st.error("Run detections first")
