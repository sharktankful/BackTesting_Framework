# 🧠 Simple Backtest Framework - SMA Crossover Strategy

This is a simple backtesting framework for simulating a basic **Moving Average Crossover** trading strategy using historical stock data.

## 📈 What It Does

- Uses **Short-Term and Long-Term Simple Moving Averages (SMA)** to generate buy/sell signals.
- Takes in user input:
  - Stock symbol (e.g., AAPL, TSLA)
  - Investment amount
  - Time period (in years)
- Downloads historical data using **yfinance**.
- Calculates:
  - Portfolio value over time (based on trades)
  - Market value (buy-and-hold performance)
- Plots both on a chart using **matplotlib**.
- Lets you **export the results as a CSV file**.

## 🛠 Technologies Used

- Python 🐍
- pandas
- numpy
- yfinance
- matplotlib

## 📊 Example Output

- DataFrame with:
  - Dates
  - Stock prices
  - Buy/Sell signals
  - Portfolio value
  - Market value
- Line chart showing portfolio vs. market value

## ✅ Features

- Clean and simple user inputs
- Easy CSV export
- Visual comparison of strategy vs. market
- Beginner-friendly structure

## 🚀 How to Run

1. Create a virtual envionrment for your project
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Run main.py and follow the terminal prompts:

   ```bash
   python main.py

## 📌 Future Improvements

- Add performance metrics (Sharpe ratio, max drawdown)  
- Handle trading fees/slippage  
- Support more strategies (e.g., RSI, MACD)  
- Add logging for trade entries and exits  
- Refactor into class-based structure or modules  

## 💡 Why I Built This

I'm learning how to build real-world trading tools as a software engineer.  
This project helped me understand how trading strategies are
