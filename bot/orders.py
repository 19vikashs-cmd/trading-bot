import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://api.binance.com"


def sign(params):
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    return hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()


def place_market_order(symbol, side, quantity):
    url = BASE_URL + "/api/v3/order"

    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
        "timestamp": int(time.time() * 1000)
    }

    params["signature"] = sign(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(url, params=params, headers=headers)

    data = response.json()

    # ✅ CLEAN OUTPUT HANDLING
    if "code" in data:
        return {
            "status": "FAILED",
            "reason": data["msg"]
        }

    return {
        "status": "SUCCESS",
        "orderId": data.get("orderId"),
        "executedQty": data.get("executedQty"),
        "data": data
    }


def place_limit_order(symbol, side, quantity, price):
    url = BASE_URL + "/api/v3/order"

    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": quantity,
        "price": price,
        "timestamp": int(time.time() * 1000)
    }

    params["signature"] = sign(params)

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(url, params=params, headers=headers)

    data = response.json()

    # ✅ CLEAN OUTPUT HANDLING
    if "code" in data:
        return {
            "status": "FAILED",
            "reason": data["msg"]
        }

    return {
        "status": "SUCCESS",
        "orderId": data.get("orderId"),
        "executedQty": data.get("executedQty"),
        "data": data
    }