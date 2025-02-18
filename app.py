# backend/app.py

from fastapi import FastAPI
from services.chat_service import router as chat_router

app = FastAPI()

# Include the chat service routes
app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel AI Chatbot API!"}
