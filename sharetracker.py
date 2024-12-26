import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    info = stock.history(period="1d")
    if not info.empty:
        price = info ['Close'].iloc[-1]
        return price
    else:
        return None


def main():
    print("Welcome to share tracker")
    tickers = input("Enter the stock ticker symbol (e.g. AAPL, GOOG, MSFT):")
    price = get_stock_price(tickers)
    if price:
        print(f"The current price of {tickers} is ${price}")
    else:
        print(f"Unable to retrieve price for {tickers}")

if __name__ == "__main__":
    main()