from datetime import date
from stocks import get_stock_info
from ui import StockTradingInterface

# Paste your API Key bellow before running the app
API_KEY = "Your API KEY here: https://www.alphavantage.co/"
API_KEY_NEWS = "Your API KEY here: https://newsapi.org/"

# Starting the ui interface
stock_trade_ui = StockTradingInterface(API_KEY, API_KEY_NEWS)
