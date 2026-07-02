from backend.services.event_analyzer import analyze_event
from backend.services.topic_generator import generate_conversation_starters
from backend.services.fact_checker import fact_check


def test_analyze_event():
    result = analyze_event("AI for healthcare")
    assert "Artificial Intelligence" in result


def test_generate_conversation_starters():
    result = generate_conversation_starters(
        ["Artificial Intelligence"],
        ["healthcare"]
    )
    assert len(result) > 0


def test_fact_check():
    result = fact_check("Artificial intelligence")
    assert "summary" in result