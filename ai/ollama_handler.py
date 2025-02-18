# backend/services/ollama_handler.py

import ollama
import logging

# Set up logging
logger = logging.getLogger(__name__)

def get_ollama_response(model_name: str, user_input: str) -> str:
    try:
        # Call the Ollama API using the local Mistral model
        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": user_input}])
        
        # Log the response for debugging
        logger.debug(f"Ollama API response: {response}")
        
        # Check the response structure and return the appropriate content
        if 'message' in response and 'content' in response['message']:
            return response['message']['content']
        elif 'text' in response:
            return response['text']
        else:
            logger.error(f"Unexpected response format from Ollama: {response}")
            return "Error: Unexpected response format from Ollama API"
            
    except KeyError as e:
        logger.error(f"KeyError in Ollama response: {str(e)}")
        return "Error: Missing expected data in Ollama API response"
    except Exception as e:
        logger.error(f"Error interacting with Ollama: {str(e)}")
        return f"Error: Failed to process Ollama request - {str(e)}"
