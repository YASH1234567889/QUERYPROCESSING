import pandas as pd
import matplotlib.pyplot as plt
file_name = "C:/Users/heman/OneDrive/Documents/Query Processing/fdata.txt"
data = pd.read_csv(file_name)
data['Date'] = pd.to_datetime(data['Date'], format='%m-%d-%y')
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Open'], label='Open', marker='o')
plt.plot(data['Date'], data['High'], label='High', marker='o')
plt.plot(data['Date'], data['Low'], label='Low', marker='o')
plt.plot(data['Date'], data['Close'], label='Close', marker='o')
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
