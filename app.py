from datetime import date
from stocks import get_stock_info
from ui import StockTradingInterface

# Date and time
todays_date = date.today()
todays_formatted = todays_date.strftime("%B %d, %Y")

# Stock price and info API from https://www.alphavantage.co/
API_KEY = "Your API KEY Here"
symbol = "MSFT"

# Call function to return an object with the stock information to be presented: data = get_stock_info(API_KEY, symbol)
# the_company = get_stock_info(API_KEY, symbol)
stock_trade_ui = StockTradingInterface()
