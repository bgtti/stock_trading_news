import requests
import json
from datetime import date, datetime, timedelta

class StockInformation:
    def __init__(self, ticker, name, exchange, currency, EBITDA, dividend_per_share, revenue_per_share, pe_ratio, high_52_week, low_52_week, last_close, last_open, last_open_date, last_7_open, last_30_open) -> None:
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
        self.last_open_date = last_open_date # date from lastest price
        self.last_7_open = last_7_open  # price at open 7 days ago
        self.last_30_open = last_30_open  # price at open 30 days ago


def get_stock_info(API_KEY, symbol):
    # Stock price ("daily adjusted")
    response = requests.get(
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}")
    response.raise_for_status()

    data_stock = response.json()["Time Series (Daily)"]
    data_stock_as_list = [value for (key, value) in data_stock.items()]
    data_stock_keys = [key for (key, value) in data_stock.items()]
    last_close = data_stock_as_list[0]["4. close"]
    last_open = data_stock_as_list[0]["1. open"]
    last_open_date = data_stock_keys[0]
    last_7_open = data_stock_as_list[6]["1. open"]
    last_30_open = data_stock_as_list[29]["1. open"]

    # Company overview
    response_company = requests.get(
        url=f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}")
    response_company.raise_for_status()

    data_company = response_company.json()
    data_company_as_dict = json.loads(json.dumps(data_company))
    ticker = data_company_as_dict["Symbol"]
    name = data_company_as_dict["Name"]
    exchange = data_company_as_dict["Exchange"]
    currency = data_company_as_dict["Currency"]
    EBITDA = data_company_as_dict["EBITDA"]
    dividend_per_share = data_company_as_dict["DividendPerShare"]
    revenue_per_share = data_company_as_dict["RevenuePerShareTTM"]
    pe_ratio = data_company_as_dict["PERatio"]
    high_52_week = data_company_as_dict["52WeekHigh"]
    low_52_week = data_company_as_dict["52WeekLow"]

    this_company = StockInformation(ticker, name, exchange, currency, EBITDA, dividend_per_share, revenue_per_share,
                                    pe_ratio, high_52_week, low_52_week, last_close, last_open, last_open_date, last_7_open, last_30_open)
    
    return this_company


