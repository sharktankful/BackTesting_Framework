import yfinance as yf
import matplotlib.pyplot as plt
from Strategies import moving_average
from Utilities import utils


def main():
    stock = input('Enter a stock name: ')
    amount = float(input('Enter stock spending amount: '))
    short = int(input('Enter short term average: '))
    long = int(input('Enter long term average: '))

    # DOWNLOAD THE STOCK DATA
    data = yf.download(stock, period='1y', interval='1d')

    # RUN STRATEGY
    strategy = moving_average.run(data, amount, short, long)

    # SHOWS LAST FEW ROWS
    print(strategy.tail())



    # Downloads Strategy to CSV_Files Folder
    while True:
        user_input = input("=============\nDo you want to save the results to a CSV? (y/n): ").strip()

        if user_input == 'y':
            csv_title = input("=============\nEnter a name for your CSV File: ")
            utils.download_csv(strategy, csv_title)
            print(f"=============\nFile saved as {csv_title}!\nLocation Saved: 'data/{csv_title}'\n=============")
            break
        elif user_input == 'n':
            break
        else:
            print("=============\nNot valid input, enter (y/n).")




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


if __name__ == "__main__":
    main()
