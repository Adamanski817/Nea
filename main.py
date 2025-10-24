import tkinter as tk
import frame_template as ft

class MainApplicatio(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.title("Main Dashboard")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.central_D = ft.central(self)
        self.central_D.grid(row=0,column=0)

application = MainApplicatio()
application.mainloop()

