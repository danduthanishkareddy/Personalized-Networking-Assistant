from fastapi import APIRouter

from models.schemas import (
    ConversationRequest,
    FactCheckRequest,
    FeedbackRequest,
)

from Services.event_analyzer import analyze_event
from Services.topic_generator import generate_conversation_starters
from Services.fact_checker import fact_check
from Services.history_logger import save_history, get_history
from Services.feedback_logger import save_feedback, get_feedback

router = APIRouter()


@router.post("/generate-conversation")
def generate_conversation(request: ConversationRequest):

    event_description = request.event_description
    interests = request.interests

    themes = analyze_event(event_description)

    starters = generate_conversation_starters(themes, interests)

    save_history({
        "event_description": event_description,
        "themes": themes,
        "interests": interests,
        "conversation_starters": starters
    })

    return {
        "extracted_themes": themes,
        "conversation_starters": starters
    }

@router.post("/fact-check")
def fact_check_api(request: FactCheckRequest):

    result = fact_check(request.topic)

    return result

@router.post("/feedback")
def feedback_api(request: FeedbackRequest):

    save_feedback({
        "conversation_starter": request.conversation_starter,
        "feedback": request.feedback
    })

    return {
        "message": "Feedback saved successfully."
    }

@router.get("/history")
def history_api():
    return {
        "history": get_history()
    }

@router.get("/feedback-history")
def feedback_history_api():
    return {
        "feedback_history": get_feedback()
    }

@router.get("/test")
def test():
    return {"message": "API Routes Working!"}