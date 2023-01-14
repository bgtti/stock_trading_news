import tkinter
UI_COLOR = "#375362"

class StockTradingInterface:
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title("Stock Information")
        self.window.config(padx=15, pady=15, bg=UI_COLOR)

        self.page_title = tkinter.Label(text="Favorites", fg="white", bg=UI_COLOR)
        self.page_title.grid(row=1, column=1)

        self.canvas = tkinter.Canvas(width=500, height=700, bg="white")
        self.stock_news = self.canvas.create_text(250,350,text="Some Text", fill=UI_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=3)


        self.window.mainloop()