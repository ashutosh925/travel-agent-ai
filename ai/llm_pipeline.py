from .ollama_handler import get_ollama_response

def process_travel_query(user_input: str) -> str:
    # In the future, you could enhance this by adding more logic (e.g., context, multiple models, etc.)
    response = get_ollama_response(model_name="mistral", user_input=user_input)
    return response
