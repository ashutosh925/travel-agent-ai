# Real-Time Travel Booking AI Chatbot

## Overview
This project is a real-time AI-powered chatbot designed to assist users in booking travel plans. It leverages FastAPI for the backend and integrates with Ollama's LLM (e.g., Mistral) to provide intelligent responses.

## Folder Structure
```
Real-time-travel-booking-ai-chatbot/
│── backend/             # Backend application (FastAPI, AI services)
│   │── services/        # Service layer handling backend logic
│   │   ├── ollama_handler.py  # Handles interactions with Ollama
│   │   ├── llm_pipeline.py    # Processes AI responses
│   │   ├── chat_service.py    # Manages chat interactions
│   │── main.py          # Entry point for FastAPI
│── front-end/           # Frontend application (if applicable)
│── README.md           # Project documentation
```

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.9+
- pip (Python package manager)
- Virtual environment (optional but recommended)

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/real-time-travel-booking-ai-chatbot.git
cd real-time-travel-booking-ai-chatbot
```

### 2. Set Up Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Install and Run Ollama
Download and install Ollama from:
[https://ollama.com/download](https://ollama.com/download)

Ensure Ollama is running:
```sh
ollama run mistral
```

## Running the Backend
Start the FastAPI server:
```sh
uvicorn backend.main:app --reload
```
The API will be accessible at `http://127.0.0.1:8000`

## API Endpoints
### Chat Interaction
**Endpoint:** `POST /chat`
- **Description:** Sends a user message and gets a response from the AI chatbot.
- **Request Body:**
  ```json
  {
    "message": "I need to book a flight to New York."
  }
  ```
- **Response:**
  ```json
  {
    "response": "Sure! Here are some flight options..."
  }
  ```

## Testing the API
You can test the API using:
```sh
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"message": "Hello"}'
```
Or open `http://127.0.0.1:8000/docs` in your browser for interactive API testing.

## Future Enhancements
- **User Authentication**: Secure user sessions and preferences.
- **Booking Integration**: Connect to airline/hotel booking APIs.
- **Frontend Development**: Build a UI for better interaction.

## Contributing
Feel free to fork and contribute by submitting a pull request!

## License
MIT License. See `LICENSE` for details.
