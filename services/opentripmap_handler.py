# backend/services/opentripmap_handler.py

import requests
from config import OPENTRIPMAP_API_KEY

BASE_URL = "https://api.opentripmap.com/0.1/en/places"

def get_places(lat: float, lon: float, radius: int = 1000, kinds: str = "interesting_places"):
    endpoint = f"{BASE_URL}/radius"
    params = {
        "apikey": OPENTRIPMAP_API_KEY,
        "radius": radius,
        "lon": lon,
        "lat": lat,
        "kinds": kinds,
        "format": "json"
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Log error as needed
        print(f"Error fetching places from OpenTripMap: {e}")
        return None
