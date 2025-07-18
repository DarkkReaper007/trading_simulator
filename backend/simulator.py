import random
import time
import pandas as pd

def simulate_stock_price(symbol="AAPL", start_price=150.0):
    price = start_price
    while True:
        price += random.uniform(-1, 1)
        yield {
            "symbol": symbol,
            "price": round(price, 2),
            "timestamp": pd.Timestamp.now().isoformat()
        }
        time.sleep(1)
