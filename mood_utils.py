def calculate_overall_mood(face, text, speech):

    positive = ["happy", "joy", "surprise"]
    negative = ["sad", "anger", "fear"]

    score = 0

    if face in positive:
        score += 1
    if face in negative:
        score -= 1

    if text in positive:
        score += 1
    if text in negative:
        score -= 1

    if speech in positive:
        score += 1
    if speech in negative:
        score -= 1

    if score > 0:
        return "Positive 🙂"
    elif score < 0:
        return "Negative 🙁"
    else:
        return "Neutral 😐"
