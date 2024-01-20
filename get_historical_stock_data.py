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

  # Access yf API
  print(f'>>> Downloading {tickers} Stock Data from yfinance Website.')
  data = yf.download(tickers = tickers, period = period, interval = interval)
  
  print(f'>>> Downloading {tickers} is Complete.')

  # Write the merged dataframe to a CSV file
  save_path = "data/{}_stock_price_data.csv".format(tickers)

  pd.DataFrame(data).to_csv(save_path, index=False)
  print(f'>>> Saving {tickers} Stock Data.')  
  print(f'>>> Saving {tickers} is Complete and Saved at: {save_path}')
  return data

tickers = ["GOOGL", "AAPL", "MSFT", "TSLA"]

for symbol in tickers:
  get_historical_stock_data(tickers=symbol, period="12mo", interval="1h")
