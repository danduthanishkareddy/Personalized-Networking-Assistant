import json
import os

FEEDBACK_FILE = "data/feedback.json"


def save_feedback(record):
    feedback = []

    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            try:
                feedback = json.load(file)
            except:
                feedback = []

    feedback.append(record)

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(feedback, file, indent=4)


def get_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            try:
                return json.load(file)
            except:
                return []

    return []