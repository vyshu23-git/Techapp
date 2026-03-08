from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def detect_text_emotion(text):

    if text.strip() == "":
        return "No Text", 0

    result = emotion_model(text)

    emotion = result[0]['label']
    confidence = result[0]['score']

    return emotion, confidence
