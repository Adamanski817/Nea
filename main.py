from tkinter import *
import tkinter as tk
from tkinter import ttk
import frame_template as ft

#Creates the actual tkinter application
class MainApplicatio(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1100x900")   
        self.title("Main Dashboard")
        self.iconphoto(False, tk.PhotoImage(file = 'hampt.png'))

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        #refrences the central frame in the frame template file
        self.central_D = ft.central(self)
        self.central_D.grid(row=0, column= 0)
        

application = MainApplicatio()
application.mainloop()