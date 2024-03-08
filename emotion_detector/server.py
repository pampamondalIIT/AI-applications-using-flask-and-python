"""
Module docstring provides a brief description of the module.
"""

from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotion-detector")
def emotion_analyzer():
    """
    This function analyzes the emotion of the given text.

    Args:
        None

    Returns:
        str: Analysis result
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"The given text has been identified as {response}."

@app.route("/")
def render_index_page():
    """
    Renders the main application page over the Flask channel.

    Args:
        None

    Returns:
        str: Rendered HTML page
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Allow Flask to choose a free port automatically
    app.run(host="0.0.0.0", port =5000)
