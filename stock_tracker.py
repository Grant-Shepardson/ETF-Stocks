import yfinance as yf
import pandas as pd
from datetime import datetime
import os

STOCK_TICKERS = ["VTI", "NVDA"]

CSV_FILE = "stock_prices.csv"

rows = []

for ticker in STOCK_TICKERS:

    try:
        stock = yf.Ticker(ticker)

        rows.append({
            "Timestamp": datetime.utcnow(),
            "Ticker": ticker,
            "Price": stock.fast_info["lastPrice"]
        })

    except Exception as e:
        print(f"Error with {ticker}: {e}")

df = pd.DataFrame(rows)

if os.path.exists(CSV_FILE):
    old_df = pd.read_csv(CSV_FILE)
    df = pd.concat([old_df, df])

df.to_csv(CSV_FILE, index=False)

print(df.tail())