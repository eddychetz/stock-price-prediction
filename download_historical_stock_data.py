import subprocess

def install(package):
    subprocess.check_call(["pip", "install", package])

# Try to import packages; if they don't exist, install them
try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    install("yfinance")
    import yfinance as yf
    import pandas as pd

def download_historical_stock_data(ticker: str, start_date, end_date):
    try:
        print(f'>>> Downloading {ticker} Stock Data from yfinance Website.')
        
        # Download historical data
        data = yf.download(ticker, start=start_date, end=end_date)
        print(f'>>> Downloading {ticker} is Complete.')

        # Reset the index to get the 'Date' as a column
        data.reset_index(inplace=True)

        # Sort the DataFrame by the 'Date' column in ascending order
        data.sort_values(by='Date', inplace=True)

        # Convert the 'Date' column to datetime format
        data['Date'] = pd.to_datetime(data['Date'])

        # Write the merged DataFrame to a CSV file
        save_path = f"data/{ticker}_stock_price_data.csv"
        data.to_csv(save_path, index=False)
        
        print(f'>>> Saving {ticker} Stock Data.')  
        print(f'>>> Saving {ticker} is Complete and Saved at: {save_path}')
        
        return data

    except Exception as e:
        print(f"Error: {e}")
        return None