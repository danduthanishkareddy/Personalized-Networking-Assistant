from fastapi import APIRouter

from models.schemas import ConversationRequest

from Services.event_analyzer import analyze_event
from Services.topic_generator import generate_conversation_starters
from Services.history_logger import save_history

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


@router.get("/test")
def test():
    return {"message": "API Routes Working!"}