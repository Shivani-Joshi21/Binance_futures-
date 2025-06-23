import streamlit as st
from mock_bot import place_market_order, get_wallet_balance, get_testnet_price, get_open_positions

st.set_page_config(page_title="Binance Testnet Bot", layout="centered")
st.title("🟢 Binance Futures Testnet Bot")

# Symbol selection
symbol = st.selectbox("Choose Trading Symbol", ["BTCUSDT", "ETHUSDT"])

# Show live mark price
if symbol:
    mark_price = get_testnet_price(symbol)
    if "Error" in str(mark_price):
        st.error(f"❌ Could not fetch price: {mark_price}")
    else:
        st.metric(label=f"📈 Live Mark Price for {symbol}", value=f"${mark_price}")

# Show wallet balance
usdt_balance = get_wallet_balance("USDT")
st.write(f"📦 USDT Balance: {usdt_balance}")

# Show open positions
st.subheader("📊 Open Position Info")
positions = get_open_positions(symbol)
if "Error" in str(positions):
    st.error(positions)
else:
    for pos in positions:
        if float(pos["positionAmt"]) != 0:
            st.json(pos)

# Place market order
st.subheader("🛒 Place Market Order")
side = st.radio("Side", ["BUY", "SELL"])
qty = st.text_input("Quantity", value="0.001")

if st.button("Place Market Order"):
    order = place_market_order(symbol, side, qty)
    if "Error" in str(order):
        st.error(order)
    else:
        st.success("✅ Market Order Placed!")
        st.json(order)
