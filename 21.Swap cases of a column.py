import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "bOB", "CHARLIE"],
    "Age": [25, 30, 35],
    "City": ["New York", "london", "PARIS"]
}
df = pd.DataFrame(data)
print(df)
column_to_swap = "Name"
df[column_to_swap] = df[column_to_swap].apply(str.swapcase)
print("\n")
print("DataFrame after swapping cases:")
print(df)
