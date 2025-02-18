# services/chat_service.py

from fastapi import APIRouter
from ai.llm_pipeline import process_travel_query

router = APIRouter()

@router.post("/chat")
async def chat(user_input: str):
    response = process_travel_query(user_input)
    return {"response": response}
