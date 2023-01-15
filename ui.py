import tkinter
UI_COLOR = "#1f1f1f"
LETTERS_COLOR = "#cce2f1"
LINE_COLOR = "#2d3945"
YELLOW = "#e5a135"
LINE_WIDTH = 600
BTN_COLOR = "#7b9ab4"

class StockTradingInterface:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Stock Information")
        self.window.config(padx=20, pady=20, bg=UI_COLOR)

        self.page_title = tkinter.Label(
            text="Microsoft Corp", fg=YELLOW, bg=UI_COLOR, font=("Helvetica", 16), anchor="w")
        self.page_title.grid(row=0, column=0, columnspan=4, sticky="w")
        self.page_sub_title = tkinter.Label(
            text="MSFT | NYSE | USD", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub_title.grid(row=1, column=0, columnspan=4, sticky="w")
        self.page_sub_title = tkinter.Label(
            text="Closing date: 10 July 2023", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub_title.grid(row=2, column=0, columnspan=4, sticky="w")
        self.page_sub2_title = tkinter.Label(
            text="Last closing: $200.00", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.page_sub2_title.grid(row=3, column=0, columnspan=4, sticky="w")

        self.page_logo = tkinter.Canvas(
            height=110, width=110, bg=UI_COLOR, highlightthickness=0, relief='ridge')
        self.logo = tkinter.PhotoImage(
            file="stock_trading_news\logo.png")
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

        def search_stock():
            print("searching")

        self.btn_search = tkinter.Button(
            text="Search", fg=UI_COLOR, bg=BTN_COLOR, command=search_stock, width=15, font=("Helvetica", 10, "bold"))
        self.btn_search.grid(row=5, column=4, sticky="e")

        # line
        self.line2 = tkinter.Canvas(
            height=1, width=LINE_WIDTH, bg=LINE_COLOR, highlightthickness=0, relief='ridge')
        self.line2.grid(row=6, column=0, columnspan=5, pady=10)

        # Stock Overview
        self.stock_overview = tkinter.Label(
            text="Stock overview", fg=YELLOW, bg=UI_COLOR, font=("Helvetica", 16), anchor="w")
        self.stock_overview.grid(row=7, column=0, columnspan=5, sticky="w")

        self.stock_last_price = tkinter.Label(
            text="Last opening: $300 | Last closing: $400 | Delta: Δ 25%", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_last_price.grid(row=8, column=0, columnspan=5, sticky="w")

        self.stock_historic = tkinter.Label(
            text="Last week closing: $300 | Last month closing: $400 | 52-week highest: $400 | 52-week lowest: $400", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_historic.grid(row=9, column=0, columnspan=5, sticky="w")

        self.stock_company = tkinter.Label(
            text="EBITDA: 20000 | Dividend per share: $6 | Revenue per share: $2 | PE: X%", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
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
            height=2, width=65, fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 12, "bold"), wrap=tkinter.WORD, highlightthickness=0, relief='ridge', bd=0)
        self.stock_news1_title.insert(
            tkinter.INSERT, "Winning ticket in Louisville worth $1 million after Mega Millions drawing - WLKY Louisville")
            #text="Winning ticket in Louisville worth $1 million after Mega Millions drawing - WLKY Louisville", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 12, "bold"), anchor="w")
        self.stock_news1_title.grid(row=14, column=0, columnspan=5, sticky="w")

        self.stock_news1_date = tkinter.Label(
            text="2023-01-15T13:51:00Z", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news1_date.grid(row=15, column=0, columnspan=5, sticky="w")

        self.stock_news1_news = tkinter.Text(height=4, width=85, font=("Helvetica", 10))
        self.stock_news1_news.insert(
            tkinter.INSERT, "LOUISVILLE, Ky. —Someone in Louisville is $1 million richer after Friday night's Mega Millions drawing, according to the Kentucky Lottery.\r\nFriday the 13th proved to actually be lucky for a Louisvill… [+677 chars]")
        self.stock_news1_news.grid(row=16, column=0, columnspan=5, sticky="w")

        self.stock_news1_source = tkinter.Label(
            text="https: // kubrick.htvapps.com/htv-prod-media.s3.amazonaws.com", fg=LETTERS_COLOR, bg=UI_COLOR, font=("Helvetica", 10), anchor="w")
        self.stock_news1_source.grid(row=17, column=0, columnspan=5, sticky="w")

        self.window.mainloop()