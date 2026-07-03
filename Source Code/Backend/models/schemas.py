from pydantic import BaseModel

class ConversationRequest(BaseModel):
    event_description: str
    interests: list[str]

class ConversationResponse(BaseModel):
    extracted_themes: list[str]
    conversation_starters: list[str]

class FactCheckRequest(BaseModel):
    topic: str


class FactCheckResponse(BaseModel):
    topic: str
    summary: str

class FeedbackRequest(BaseModel):
    conversation_starter: str
    feedback: str