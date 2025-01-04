import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-12-31"
stock_data = yf.download(ticker, start=start_date, end=end_date)
if not stock_data.empty:
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Close'], label="Close Price", color='blue')
    plt.title("Alphabet Inc. (GOOGL) Stock Prices", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Close Price (USD)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("No stock data available for the specified date range.")
