import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-12-31"
stock_data = yf.download(ticker, start=start_date, end=end_date)
if not stock_data.empty:
    stock_data.reset_index(inplace=True)
    print(stock_data.head())
    plt.figure(figsize=(14, 7))
    plt.bar(stock_data['Date'], stock_data['Volume'], color='orange', edgecolor='black', alpha=0.8)
    plt.title("Alphabet Inc. (GOOGL) Trading Volume", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Trading Volume", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()
else:
    print("No stock data available for the specified date range.")
