import pandas as pd
import numpy as np

def run(data: pd.DataFrame, amount: int, short: int, long: int):
    # short and long term moving averages
    short_desc, long_desc = f'{short}MA', f'{long}MA'
     
    data[short_desc] = data['Close'].rolling(window=short).mean()
    data[long_desc] = data['Close'].rolling(window=long).mean()

    # Signal for moving Strategy
    data['Signal'] = np.where(data[short_desc] > data[long_desc], 1, 0) # 1 = BUY if short MA is greater than long MA
    data['Signal'] = np.where(data[short_desc] < data[long_desc], -1, data['Signal']) # -1 = SELL if short MA is less than long MA. 0 = HOLD

    # Position for if I currently bought, sold, or hold the stock
    data['Position'] = data['Signal'].shift(1)

    # Grab the percent change in the stock each day
    data['Return'] = data['Close'].pct_change()
    # Grab the percent change of how much I earned in stock when buy/sold
    data['Strategy_Return'] = data['Position'] * data['Return']

    # Multiplier that shows the ammount made from stock
    data['Cumulative_Market'] = (1 + data['Return']).cumprod()
    # Multiplier that shows amount made from strategy
    data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod()

    # Dollar amount made from holding stock from beginning to end
    data['Market_Value'] = amount * data['Cumulative_Market']
    # Dollar amount made from stock in strategy
    data['Portfolio_Value'] = amount * data['Cumulative_Strategy']
    


    # Return the data
    return data[['Close', short_desc, long_desc, 'Signal', 'Position', 'Return', 'Strategy_Return', 'Portfolio_Value', 'Market_Value']]




'''
if __name__ == "__main__":
    import yfinance as yf

    data = yf.download("AAPL", period="1y", interval="1d")
    result = run(data)
    print(result.head())   
'''