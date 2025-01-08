import sys

def ticket(tick):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if tick in STOCKS:
        price = STOCKS.get(tick)
        for company, ticket_value in COMPANIES.items():
            if ticket_value == tick:
                print(f"{company} {price}")
    else:
        print("Unknown ticker")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python3 stock_prices.py <ticket>")
        sys.exit(1)

    arg = sys.argv[1].upper()
    ticket(arg)
