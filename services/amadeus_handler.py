# backend/services/amadeus_handler.py

import requests
import logging
from config import AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET

BASE_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"  # Check the Amadeus API docs for the exact endpoint structure

# Set up logging
logger = logging.getLogger(__name__)

# Constants for Amadeus credentials (You should store these securely, like in environment variables)
CLIENT_ID = AMADEUS_CLIENT_ID  # Replace with your actual client_id
CLIENT_SECRET = AMADEUS_CLIENT_SECRET  # Replace with your actual client_secret

# Function to get OAuth 2.0 Access Token from Amadeus
def get_amadeus_access_token():
    url = BASE_URL
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            access_token = response.json()['access_token']
            logger.info("Successfully retrieved Amadeus access token.")
            return access_token
        else:
            logger.error(f"Failed to retrieve access token: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error occurred while fetching access token: {str(e)}")
        return None

# Function to fetch flight offers from Amadeus API
def get_flight_offers(origin, destination, departure_date):
    access_token = get_amadeus_access_token()
    
    if not access_token:
        return "Error: Unable to fetch access token from Amadeus."
    
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    
    # Set headers with the Bearer token (access token)
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # Parameters for the flight search request
    params = {
        "originLocationCode": origin,  # Origin airport code (e.g., NYC for New York)
        "destinationLocationCode": destination,  # Destination airport code (e.g., LAX for Los Angeles)
        "departureDate": departure_date,  # Departure date in 'YYYY-MM-DD' format
        "adults": 1  # Number of adults
    }
    
    try:
        # Send the GET request to Amadeus API
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                return data['data']  # Return flight offers if available
            else:
                return f"No flight offers found: {data.get('errorMessage', 'Unknown error')}"
        else:
            logger.error(f"Error fetching flight offers: {response.status_code} - {response.text}")
            return f"Error fetching flight offers: {response.status_code} - {response.text}"
    
    except Exception as e:
        logger.error(f"Error occurred while fetching flight offers: {str(e)}")
        return f"Error: Failed to fetch flight offers from Amadeus - {str(e)}"
