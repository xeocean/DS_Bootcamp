import sys
from bs4 import BeautifulSoup
import requests
import time

def get_page(ticker, table_name):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if response.url == url:
            page = response.content
            soup = BeautifulSoup(page, "html.parser")
            table = soup.find('div', class_="tableBody")
            row_search = table.find(class_="rowTitle", title=table_name)
            rows_all = row_search.find_parent(class_="row")
            values = rows_all.find_all(class_="column")
            time.sleep(5) # ???
            return tuple(value.text.strip() for value in values)
        else:
            raise ValueError(f"Fail url: current {response.url}")
    else:
        raise ConnectionError(f"Error {response.status_code}")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            tick = sys.argv[1]
            table = sys.argv[2]
            print(get_page(tick, table))
        else:
            print(f'Use: {sys.argv[0]} <ticker> <table_name>')
    except (AttributeError, ValueError, ConnectionError) as e:
        print(f"Error: {e}")
