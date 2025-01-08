import sys


def all_stocks(search: list):
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

    def ticket(item_ticket):
        for company, tick in COMPANIES.items():
            if tick == item_ticket:
                print(f'{tick} is a ticker symbol for {company}')

    def price(company):
        value = COMPANIES.get(company)
        price_company = STOCKS.get(value)
        print(f'{company} stock price is {price_company}')

    for item in search:
        if item.upper() in STOCKS:
            ticket(item.upper())
        elif item.capitalize() in COMPANIES:
            price(item.capitalize())
        else:
            print(f'{item} is an unknown company or an unknown ticker symbol')


def format_list(string: str):
    my_list = [name.strip() for name in string.split(",")]
    all_stocks(my_list)


def check_string(string: str):
    return ",," not in string.replace(" ", "")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if check_string(arg):
            format_list(arg)
