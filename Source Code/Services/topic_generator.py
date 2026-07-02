def generate_conversation_starters(themes, interests):
    starters = []

    for theme in themes:
        starters.append(
            f"I noticed you're interested in {theme}. What projects have you been working on?"
        )

    if interests:
        for interest in interests:
            starters.append(
                f"I've also been exploring {interest}. What's your experience with it?"
            )

    return starters[:3]