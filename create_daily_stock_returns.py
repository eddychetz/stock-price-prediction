import pandas as pd

file_path = "data\{}_stock_price_data.csv".format(tickers)
def create_daily_stock_returns(file_path):
    data = pd.read_csv(file_path)
    returns_data = data['Adj Close'].pct_change_rate()
    return returns_data