# backend/services/google_maps_handler.py

import requests
from config import GOOGLE_MAPS_API_KEY

BASE_URL = "https://maps.googleapis.com/maps/api"

def get_directions(origin: str, destination: str, mode: str = "transit"):
    endpoint = f"{BASE_URL}/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": GOOGLE_MAPS_API_KEY,
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Log error as needed
        print(f"Error fetching directions from Google Maps: {e}")
        return None
