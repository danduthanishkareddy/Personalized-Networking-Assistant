def analyze_event(event_description):
    themes = []

    text = event_description.lower()

    if "ai" in text:
        themes.append("Artificial Intelligence")
    if "cloud" in text:
        themes.append("Cloud Computing")
    if "health" in text:
        themes.append("Healthcare")
    if "blockchain" in text:
        themes.append("Blockchain")
    if "data" in text:
        themes.append("Data Science")

    if not themes:
        themes = ["General Networking"]

    return themes