from pydantic import BaseModel

class ConversationRequest(BaseModel):
    event_description: str
    interests: list[str]

class ConversationResponse(BaseModel):
    extracted_themes: list[str]
    conversation_starters: list[str]