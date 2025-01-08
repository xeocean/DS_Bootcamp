import sys
from bs4 import BeautifulSoup
import urllib.error, urllib.request


def get_page(ticker, table_name):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            soup = BeautifulSoup(page, "html.parser")
            table = soup.find('div', class_="tableBody")
            row_search = table.find(class_="rowTitle", title=table_name)
            rows_all = row_search.find_parent(class_="row")
            values = rows_all.find_all(class_="column")
            return tuple(value.text.strip() for value in values)
    except urllib.error.HTTPError as e:
        raise ConnectionError(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise ConnectionError(f"Error fetching page: {e.reason}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            tick = sys.argv[1]
            tablename = sys.argv[2]
            print(get_page(tick, tablename))
        else:
            print(f'Use: {sys.argv[0]} <ticker> <table_name>')
    except (AttributeError, ValueError, ConnectionError, RuntimeError) as e:
        print(f"Error: {e}")
