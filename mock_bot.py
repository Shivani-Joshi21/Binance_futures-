import random

def get_testnet_price(symbol):
    return round(random.uniform(28000, 30000), 2)

def place_market_order(symbol, side, quantity):
    return {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "status": "FILLED",
        "price": get_testnet_price(symbol)
    }

def get_wallet_balance(asset="USDT"):
    return "10000.00"

def get_open_positions(symbol):
    return [{
        "symbol": symbol,
        "positionAmt": "0.01",
        "entryPrice": "29000",
        "unRealizedProfit": "50",
        "positionSide": "LONG",
    }]
