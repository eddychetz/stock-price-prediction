import pandas as pd

print(f">>> Importing data.....")
data = pd.read_csv("./data/GOOGL_stock_price_data.csv")
print(data.head())
print()
print(f">>> Loading Completed.")
print()
print(f">>> Inspecting data.....")
print(data.info())
print(f">>> The data has {data.shape[0]} rows and {data.shape[1]} columns.")
print()