import sys

def stock_prices(company):
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

    if company in COMPANIES:
        value = COMPANIES.get(company)
        print(STOCKS.get(value))
    else:
        print("Unknown company")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python3 stock_prices.py <company_name>")
        sys.exit(1)

    arg = sys.argv[1].capitalize()
    stock_prices(arg)
