import yfinance as yf
import matplotlib.pyplot as plt
from Strategies import moving_average


def main():
    stock = input('Enter a stock name: ')
    amount = float(input('Enter stock spending amount: '))
    short = int(input('Enter short term value: '))
    long = int(input('Enter long term value: '))

    # DOWNLOAD THE STOCK DATA
    data = yf.download(stock, period='1y', interval='1d')

    # RUN STRATEGY
    strategy = moving_average.run(data, amount, short, long)

    # Generates plot chart, compares market vs startegy
    plt.figure(figsize=(12, 6))

    # Money made through Market
    plt.plot(strategy.index,
             strategy['Market_Value'], label='Market', color='blue')
    # Money made through Strategy
    plt.plot(strategy.index,
             strategy['Portfolio_Value'], label='Strategy', color='green')

    # Title
    plt.title(
        f'Strategy vs Market\n{short}-day short MA and {long}-day long MA')

    plt.xlabel('Date')  # X-axis Label
    plt.ylabel('Portfolio Value ($)')  # Y-axis Label

    plt.legend()  # Shows which line is which
    plt.grid()  # Adds grid lines
    plt.show()  # Displays chart

    # SHOWS LAST FEW ROWS
    print(strategy.tail())


if __name__ == "__main__":
    main()
