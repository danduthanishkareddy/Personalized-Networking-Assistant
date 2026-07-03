import wikipedia


def fact_check(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)

        return {
            "topic": topic,
            "summary": summary
        }

    except Exception:
        return {
            "topic": topic,
            "summary": "No information found."
        }
    POST /fact-check