# backend/main.py

from fastapi import FastAPI
from ai.llm_pipeline import process_travel_query
from services.amadeus_handler import get_flight_offers
from services.google_maps_handler import get_directions
from services.opentripmap_handler import get_places

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Real-time Travel Booking AI Chatbot API"}

@app.get("/test/ollama")
async def test_ollama(prompt: str):
    result = process_travel_query(user_input=prompt)
    return result if result else {"error": "Failed to get a response from Ollama API"}

@app.get("/test/amadeus")
async def test_amadeus(origin: str, destination: str, departure_date: str):
    result = get_flight_offers(origin, destination, departure_date)
    return result if result else {"error": "Failed to fetch flight offers from Amadeus"}

@app.get("/test/google-maps")
async def test_google_maps(origin: str, destination: str, mode: str = "transit"):
    result = get_directions(origin, destination, mode)
    return result if result else {"error": "Failed to fetch directions from Google Maps"}

@app.get("/test/opentripmap")
async def test_opentripmap(lat: float, lon: float):
    result = get_places(lat, lon)
    return result if result else {"error": "Failed to fetch places from OpenTripMap"}
