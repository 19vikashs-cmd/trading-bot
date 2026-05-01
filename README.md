# Trading Bot - Binance Futures Testnet (Python)

## Overview
This project is a Python-based CLI trading bot that interacts with the Binance Futures Testnet API. It supports placing MARKET and LIMIT orders for BTCUSDT with BUY/SELL functionality.

The system is designed with modular architecture including API handling, input validation, logging, and CLI-based execution.

From :contentReference[oaicite:0]{index=0} Futures API structure.

---

## Features
- Market Order execution
- Limit Order execution
- BUY / SELL support
- CLI-based user input (argparse)
- Input validation
- Structured logging system
- Error handling for API and runtime failures

---

## Tech Stack
- Python 3.x
- requests
- python-dotenv
- Binance Futures Testnet API

---

## Project Structure
trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── logs/
│ └── logs.log


---

## Setup Instructions

### 1. Install dependencies

pip install -r requirements.txt

### 2. Configure environment variables (.env)

API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com


---

## How to Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001


### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000


---

## Logging
All API requests, responses, and errors are stored in:

logs/logs.log

---

## Error Handling Remarks

During development and testing, the following issues may occur:

- **API Error (-2015): Invalid API-key or permissions**
  → Occurs when API key is not enabled for trading or testnet mismatch.

- **API Error (-2010): Insufficient balance**
  → Occurs when test account has no USDT balance for executing trades.

- **Network / Testnet access issues**
  → Binance Futures Testnet may be temporarily unavailable or restricted depending on network conditions.

These errors are handled gracefully in the application with proper logging and user-friendly messages.

---

## Important Notes
- This project is designed for Binance Futures Testnet only.
- No real funds are used.
- The bot demonstrates full trading workflow: request creation → signing → API call → response handling.

---

## Author
Python Developer Internship Assignment Submission

