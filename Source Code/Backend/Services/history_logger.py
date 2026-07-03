import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "Data", "history.json")


def save_history(record):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                history = json.load(file)
            except:
                history = []

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            try:
                return json.load(file)
            except:
                return []

    return []