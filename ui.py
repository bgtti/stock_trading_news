import tkinter
from datetime import datetime
from stocks import get_stock_info
from news import get_news
UI_COLOR = "#1f1f1f"
LETTERS_COLOR = "#cce2f1"
LINE_COLOR = "#2d3945"
YELLOW = "#e5a135"
LINE_WIDTH = 600
BTN_COLOR = "#7b9ab4"

class StockTradingInterface:
    def __init__(self, API_KEY, API_KEY_NEWS) -> None:
        # APIS
        API_KEY = API_KEY
        API_KEY_NEWS = API_KEY_NEWS
        # Company variables
        data = get_stock_info(API_KEY, "MSFT")
        news = get_news(API_KEY_NEWS, "Microsoft Corporation")

        def changing_data():
            new_ticker = self.input_ticker.get()
            global data
            data = get_stock_info(API_KEY, new_ticker)
            global news
            news = get_news(API_KEY_NEWS, data.name)
            #changing Label widgets:
            global the_date
            the_date = datetime.strptime(data.last_open_date, "%Y-%m-%d").strftime("%d %B, %Y")
            global delta
            delta = round((((float(data.last_close) - float(data.last_open))/float(data.last_open)) * 100), 1)
            global ebitda
            ebitda = int(data.EBITDA)
            to_change = [self.page_title, self.page_sub_title,
                         self.page_sub1_title, self.page_sub2_title, self.stock_last_price, self.stock_historic, self.stock_company, self.stock_news1_date, self.stock_news1_source]
            the_change = [f"{data.name}", f"{data.ticker} | {data.exchange} | {data.currency}", f"Closing date: {the_date}",
                          f"Last closing: {data.last_close}", f"Last opening: {data.last_open} | Last closing: {data.last_close} | Change: {delta}%", f"Last week opening: {data.last_7_open} | Last month opening: {data.last_30_open} | 52-week highest: {data.high_52_week} | 52-week lowest: {data.low_52_week}", f"EBITDA: {ebitda:,} | Dividend per share: {data.dividend_per_share} | Revenue per share: {data.revenue_per_share} | PE: {data.pe_ratio}", f"{news[0][1]}", f"{news[0][3]}"]
            for i in range (len(to_change)):
                to_change[i]["text"] = the_change[i]
            #changing Text widgets:
            text_widgets = [self.stock_news1_title, self.stock_news1_news,
                            self.stock_news2_title, self.stock_news2_news, self.stock_news3_title, self.stock_news3_news]
            text_replaments = [
                f"{news[0][0]}", f"{news[0][2]}", f"{news[1][0]}", f"{news[1][2]}", f"{news[2][0]}", f"{news[2][2]}"]
            for e in range (len(text_widgets)):
                text_widgets[e].delete(1.0, tkinter.END)
                text_widgets[e].insert(tkinter.INSERT, text_replaments[e])

        #Tk start
        self.window = tkinter.Tk()
        self.window.title(f"Stock Information")
        self.window.config(padx=20, pady=20, bg=UI_COLOR)
            
        #Title, logo, and main info
        self.page_title = tkinter.Label(
            text=f"{data.name}", fg=YELLOW, bg=UI_COLOR, font=("Helvetica", 16), anchor="w")
        self.page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        self.page_sub_title = tkinter.Label(
            text=f"{data.ticker} | {data.exchange} | {data.currency}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub_title.grid(row=1, column=0, columnspan=4, sticky="w")
        the_date = datetime.strptime(
            data.last_open_date, "%Y-%m-%d").strftime("%d %B, %Y")
        self.page_sub1_title = tkinter.Label(
            text=f"Closing date: {the_date}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub1_title.grid(row=2, column=0, columnspan=4, sticky="w")
        self.page_sub2_title = tkinter.Label(
            text=f"Last closing: {data.last_close}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub2_title.grid(row=3, column=0, columnspan=4, sticky="w")

        self.page_logo = tkinter.Canvas(
            height=110, width=110, bg=UI_COLOR, highlightthickness=0, relief='ridge')
        self.logo = tkinter.PhotoImage(
            file="logo.png")
        self.page_logo.create_image(55, 55, image=self.logo)
        self.page_logo.grid(row=0, column=4, rowspan=4, sticky="e")

        # line
        self.line1 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=LINE_COLOR, highlightthickness=0, relief='ridge')
        self.line1.grid(row=4, column=0, columnspan=5, pady=10)

        # search box
        self.input_label_ticker = tkinter.Label(
            text="Search by ticker: ", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.input_label_ticker.grid(row=5, column=0, sticky="w")
        self.input_ticker = tkinter.Entry(width=20)
        self.input_ticker.insert(0, "MSFT")
        self.input_ticker.grid(row=5, column=1, columnspan=3, sticky="w")
        self.input_ticker.focus()

        self.btn_search = tkinter.Button(
            text="Search", fg=UI_COLOR, bg=BTN_COLOR, command=changing_data, width=15, font=("Helvetica", 10, "bold"))
        self.btn_search.grid(row=5, column=4, sticky="e")

        # line
        self.line2 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=LINE_COLOR, highlightthickness=0, relief='ridge')
        self.line2.grid(row=6, column=0, columnspan=5, pady=10)

        # Stock Overview
        self.stock_overview = tkinter.Label(
            text="Stock overview", fg=YELLOW, bg=UI_COLOR, font=("Helvetica", 16), anchor="w")
        self.stock_overview.grid(row=7, column=0, columnspan=5, sticky="w")

        delta = round((((float(data.last_close) - float(data.last_open))/float(data.last_open)) * 100), 1)
        self.stock_last_price = tkinter.Label(
            text=f"Last opening: {data.last_open} | Last closing: {data.last_close} | Change: {delta}%", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_last_price.grid(row=8, column=0, columnspan=5, sticky="w")

        self.stock_historic = tkinter.Label(
            text=f"Last week opening: {data.last_7_open} | Last month opening: {data.last_30_open} | 52-week highest: {data.high_52_week} | 52-week lowest: {data.low_52_week}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_historic.grid(row=9, column=0, columnspan=5, sticky="w")

        ebitda = int(data.EBITDA)
        self.stock_company = tkinter.Label(
            text=f"EBITDA: {ebitda:,} | Dividend per share: {data.dividend_per_share} | Revenue per share: {data.revenue_per_share} | PE: {data.pe_ratio}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_company.grid(row=10, column=0, columnspan=5, sticky="w")

        # line
        self.line3 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=LINE_COLOR, highlightthickness=0, relief='ridge')
        self.line3.grid(row=11, column=0, columnspan=5, pady=10)

        # Stock News
        self.stock_news_title = tkinter.Label(
            text="Latest news", fg=YELLOW, bg=UI_COLOR, font=("Helvetica", 16), anchor="w")
        self.stock_news_title.grid(row=12, column=0, columnspan=5, sticky="w")

        # First news
        self.line4 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=UI_COLOR, highlightthickness=0, relief='ridge')
        self.line4.grid(row=13, column=0, columnspan=5, pady=2)

        self.stock_news1_title = tkinter.Text(
            height=1, width=65, fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 12, "bold"), wrap=tkinter.WORD, highlightthickness=0, relief='ridge', bd=0)
        self.stock_news1_title.insert(
            tkinter.INSERT, f"{news[0][0]}")
        self.stock_news1_title.grid(row=14, column=0, columnspan=5, sticky="w")

        self.stock_news1_date = tkinter.Label(
            text=f"{news[0][1]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news1_date.grid(row=15, column=0, columnspan=5, sticky="w")

        self.stock_news1_news = tkinter.Text(height=3, width=85, font=("Helvetica", 10))
        self.stock_news1_news.insert(
            tkinter.INSERT, f"{news[0][2]}")
        self.stock_news1_news.grid(row=16, column=0, columnspan=5, sticky="w")

        self.stock_news1_source = tkinter.Label(
            text=f"{news[0][3]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news1_source.grid(row=17, column=0, columnspan=5, sticky="w")

        # Second news
        self.line5 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=UI_COLOR, highlightthickness=0, relief='ridge')
        self.line4.grid(row=18, column=0, columnspan=5, pady=2)

        self.stock_news2_title = tkinter.Text(
            height=1, width=65, fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 12, "bold"), wrap=tkinter.WORD, highlightthickness=0, relief='ridge', bd=0)
        self.stock_news2_title.insert(
            tkinter.INSERT, f"{news[1][0]}")
        self.stock_news2_title.grid(row=19, column=0, columnspan=5, sticky="w")

        self.stock_news2_date = tkinter.Label(
            text=f"{news[1][1]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news2_date.grid(row=20, column=0, columnspan=5, sticky="w")

        self.stock_news2_news = tkinter.Text(
            height=3, width=85, font=("Helvetica", 10))
        self.stock_news2_news.insert(
            tkinter.INSERT, f"{news[1][2]}")
        self.stock_news2_news.grid(row=21, column=0, columnspan=5, sticky="w")

        self.stock_news2_source = tkinter.Label(
            text=f"{news[1][3]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news2_source.grid(
            row=22, column=0, columnspan=5, sticky="w")
        
        # Third news
        self.line6 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=UI_COLOR, highlightthickness=0, relief='ridge')
        self.line4.grid(row=23, column=0, columnspan=5, pady=2)

        self.stock_news3_title = tkinter.Text(
            height=1, width=65, fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 12, "bold"), wrap=tkinter.WORD, highlightthickness=0, relief='ridge', bd=0)
        self.stock_news3_title.insert(
            tkinter.INSERT, f"{news[2][0]}")
        self.stock_news3_title.grid(row=24, column=0, columnspan=5, sticky="w")

        self.stock_news3_date = tkinter.Label(
            text=f"{news[2][1]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news3_date.grid(row=25, column=0, columnspan=5, sticky="w")

        self.stock_news3_news = tkinter.Text(
            height=3, width=85, font=("Helvetica", 10))
        self.stock_news3_news.insert(
            tkinter.INSERT, f"{news[2][2]}")
        self.stock_news3_news.grid(row=26, column=0, columnspan=5, sticky="w")

        self.stock_news3_source = tkinter.Label(
            text=f"{news[2][3]}", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news3_source.grid(
            row=27, column=0, columnspan=5, sticky="w")

        self.window.mainloop()