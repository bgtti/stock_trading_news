import requests

class StockInformation:
    def __init__(self, ticker, name, exchange, currency, EBITDA, dividend_per_share, revenue_per_share, pe_ratio, high_52_week, low_52_week, last_close, last_open, last_7_close, last_7_open, last_30_open, last_30_close) -> None:
        self.ticker = ticker
        self.name = name
        self.exchange = exchange
        self.currency = currency
        self.EBITDA = EBITDA
        self.dividend_per_share = dividend_per_share
        self.revenue_per_share = revenue_per_share
        self.pe_ratio = pe_ratio
        self.high_52_week = high_52_week  # highest price in the past 52 weeks
        self.low_52_week = low_52_week  # lowest price in the past 52 weeks
        self.last_close = last_close # price at last stock closing date
        self.last_open = last_open  # price at last stock opening date
        self.last_7_close = last_7_close  # price at close 7 days ago
        self.last_7_open = last_7_open  # price at open 7 days ago
        self.last_30_open = last_30_open  # price at open 30 days ago
        self.last_30_close = last_30_close  # price at close 30 days ago


def get_stock_info(API_KEY, symbol):
    # Stock price ("daily adjusted")
    response = requests.get(
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}")
    response.raise_for_status()

    data = response.json()

    # Company overview
    response_overview = requests.get(
        url=f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}")
    response_overview.raise_for_status()

    data_overview = response_overview.json()

# Search endpoint: to build a searchbox to match ticker and symbol : 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
