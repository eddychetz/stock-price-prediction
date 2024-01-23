import pandas as pd
import pytimetk as tk
import datetime as dt
print(f">>> Importing data.....")
data = pd.read_csv("./data/GOOGL_returns_data.csv")
print(data.head())
print()
print(f">>> Loading Completed.")
print()
print(f">>> Inspecting data.....")
print(data.info())
print(f">>> The data has {data.shape[0]} rows and {data.shape[1]} columns.")
print()
data.date = pd.to_datetime(data.date, format="%Y-%m-%d")
data.plot_timeseries()