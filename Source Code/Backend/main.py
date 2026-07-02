from fastapi import FastAPI
from backend.routes.api_routes import router

app = FastAPI(
    title="Personalized Networking Assistant",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Personalized Networking Assistant!"
    }