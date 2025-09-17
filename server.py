from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.pop('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    response_str = ", ".join(f"'{k}': {v}" for k, v in response.items())

    return f'For the given statement, the system response is {response_str}. The dominant emotion is {dominant_emotion}.'


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)