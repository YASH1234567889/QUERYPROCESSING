import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Date": [
        "01-04-2020", "02-04-2020", "03-04-2020", "06-04-2020", "07-04-2020"
    ],
    "Close": [1105.62, 1120.84, 1097.84, 1186.92, 1186.51],
    "Volume": [2343100, 1964900, 2314000, 2664700, 2383700]
}
alphabet_stock_data = pd.DataFrame(data)
alphabet_stock_data['Date'] = pd.to_datetime(alphabet_stock_data['Date'])
plt.figure(figsize=(10, 6))
plt.scatter(alphabet_stock_data['Volume'], alphabet_stock_data['Close'], color='blue', alpha=0.7)
plt.title("Trading Volume vs Stock Prices (Alphabet Inc.)", fontsize=16)
plt.xlabel("Trading Volume", fontsize=12)
plt.ylabel("Stock Prices (Close)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
