import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Missing API keys")

    client = Client(api_key, api_secret)

    return client