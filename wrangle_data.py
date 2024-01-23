import pandas as pd
import datetime as dt
tickers = "GOOGL"
file_path = "data/{}_stock_price_data.csv".format(tickers)
def wrangle_data(file_path, tickers: str):
    
    t0 = dt.datetime.now()
    data = pd.read_csv(file_path)
    data["returns"] = data['Adj Close'].pct_change()*100
    data.rename(columns={'Adj Close':'price','Datetime':'date'}, inplace=True)
    data = data[['date', 'price', 'returns']]
    data = data.dropna(axis=0)
    save_path = "data/{}_returns_data.csv".format(tickers)
    print(">>> Saving Transformed Data.")
    pd.DataFrame(data).to_csv(save_path, index=False)
    print("\n>>> Saving Completed.")
    print(data.head())
    t1 = dt.datetime.now()
    completion_time = t1 - t0
    print(f"\n>>> Transformation Completed with {completion_time} completion time.")