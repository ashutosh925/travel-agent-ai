# backend/config.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# API Keys
# OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY") | we need this only if we're using ollama API in our project
AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID") # we need this only if we're using amadeus API in our project
AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET") # we need this only if we're using amadeus API in our project
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY") # we need this only if we're using google maps API in our project
OPENTRIPMAP_API_KEY = os.getenv("OPENTRIPMAP_API_KEY") # we need this only if we're using opentripmap API in our project
# ADD OLLAMA_API_KEY in case you using ollama API in your project
if not all([AMADEUS_CLIENT_ID,AMADEUS_CLIENT_SECRET, GOOGLE_MAPS_API_KEY, OPENTRIPMAP_API_KEY]):
    raise Exception("One or more API keys are missing. Please check your .env file.")
