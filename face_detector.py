import cv2
from deepface import DeepFace

def detect_face_emotion():

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()

    if not ret:
        cap.release()
        return "No Face"

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        emotion = result[0]["dominant_emotion"]

    except:
        emotion = "Unknown"

    cap.release()

    return emotion
