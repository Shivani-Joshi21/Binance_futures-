import os
import logging
from binance.client import Client
from dotenv import load_dotenv
from binance.exceptions import BinanceAPIException

# Load API keys from .env
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")
if not api_key or not api_secret:
    raise ValueError("❌ API key or secret not found. Make sure your .env file is correct.")

print("✅ API Key loaded:", api_key[:4] + "********")
print("✅ Secret Key loaded:", bool(api_secret))
# Logging config
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize Binance Futures Testnet client
client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

# -------------------------- Functions -------------------------- #



def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        return order
    except BinanceAPIException as e:
        return f"Error placing market order: {e}"

def get_testnet_price(symbol):
    try:
        ticker = client.futures_mark_price(symbol=symbol)
        return float(ticker['markPrice'])
    except BinanceAPIException as e:
        return f"APIError: {e}"

def get_wallet_balance(asset="USDT"):
    try:
        balance = client.futures_account_balance()
        for b in balance:
            if b['asset'] == asset:
                return b['balance']
        return "Asset not found"
    except BinanceAPIException as e:
        return f"Error: {e}"


def get_open_positions(symbol):
    try:
        positions = client.futures_position_information(symbol=symbol)
        return positions
    except BinanceAPIException as e:
        return f"Error: {e}"