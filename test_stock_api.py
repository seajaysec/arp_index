import json
import os
import sys

import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
if not API_KEY:
    raise ValueError("Please set ALPHA_VANTAGE_API_KEY in your .env file")

BASE_URL = "https://www.alphavantage.co/query"


def get_active_stocks():
    """Get most active stocks"""
    params = {"function": "TOP_GAINERS_LOSERS", "apikey": API_KEY}
    response = requests.get(BASE_URL, params=params)
    return response.json()


def get_stock_data(symbol, interval="1d"):
    """Get stock price history"""
    if interval == "1d":
        function = "TIME_SERIES_INTRADAY"
        params = {
            "function": function,
            "symbol": symbol,
            "interval": "5min",
            "apikey": API_KEY,
        }
    else:
        function = "TIME_SERIES_DAILY"
        params = {"function": function, "symbol": symbol, "apikey": API_KEY}

    response = requests.get(BASE_URL, params=params)
    return response.json()


def main():
    # Get active stocks
    print("Fetching active stocks...")
    active_stocks = get_active_stocks()

    # Get price data for first stock
    if active_stocks.get("most_actively_traded"):
        first_symbol = active_stocks["most_actively_traded"][0]["ticker"]
        print(f"Fetching price data for {first_symbol}...")
        price_data = get_stock_data(first_symbol)

        # Save combined results
        result = {"active_stocks": active_stocks, "price_data": price_data}

        with open("test.json", "w") as f:
            json.dump(result, f, indent=2)
        print("Results saved to test.json")
    else:
        print("Error getting active stocks:", active_stocks)


if __name__ == "__main__":
    main()
