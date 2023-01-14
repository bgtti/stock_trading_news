import requests
from datetime import date
from ui import StockTradingInterface

# Date and time
todays_date = date.today()
todays_formatted = todays_date.strftime("%B %d, %Y")
todays_weekday = todays_date.weekday
is_market_open = "Weekday: the stock market is operating during business hours."
if todays_weekday < 5:
    is_market_open = "Weekend: the stock market might be closed."

# Stock price and info API from https://www.alphavantage.co/
API_KEY = "your api key here"
symbol = "MSFT"

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

print(data)
print(data_overview)

stock_trade_ui = StockTradingInterface()