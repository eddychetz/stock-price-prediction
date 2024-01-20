import subprocess

def install(package):
    subprocess.check_call(["pip", "install", package])

# try to import package if it exist or else install package using pip
try:
    import yfinance
  
except ImportError:

  install("yfinance")
  
# Data manipulation
import pandas as pd

# Extracting stock data from yahoo finance website
import yfinance as yf

def get_historical_stock_data(tickers: str, period: str, interval: str) -> pd.DataFrame:

  # Acess yf API
  data = yf.download(tickers = tickers, period = period, interval = interval)

  # Write the merged dataframe to a CSV file
  save_path = "data/{}_stock_prices.csv".format(tickers)
    
  print('Save at :',save_path)
  pd.DataFrame(data).to_csv(save_path, index=False)
      
  return data
