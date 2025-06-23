from bot import BasicBot

# Direct assignment of keys for demo purpose
api_key = "your_testnet_api_key_here"
api_secret = "your_testnet_api_secret_here"

bot = BasicBot(api_key, api_secret)

print("\n=== Binance Futures Trading Bot ===")
print("1. Market Order\n2. Limit Order\n3. Stop-Limit Order")
choice = input("Select order type (1/2/3): ").strip()

symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
side = input("Enter order side (BUY/SELL): ").upper()
quantity = float(input("Enter quantity: "))

if choice == '1':
    bot.place_market_order(symbol, side, quantity)
elif choice == '2':
    price = float(input("Enter limit price: "))
    bot.place_limit_order(symbol, side, quantity, price)
elif choice == '3':
    stop_price = float(input("Enter stop price: "))
    limit_price = float(input("Enter limit price: "))
    bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
else:
    print("❌ Invalid choice.")