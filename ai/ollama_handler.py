# services/ollama_handler.py

import ollama

def get_ollama_response(model_name: str, user_input: str) -> str:
    try:
        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": user_input}])
        return response['text']
    except Exception as e:
        return f"Error interacting with Ollama: {e}"
