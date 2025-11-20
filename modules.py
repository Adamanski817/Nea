import tkinter as tk

class flashcard_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Flashcard Module")
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)

class notepad_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("Notepad Module")
        self.geometry("675x1100")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        self.notepad_label = tk.Label(self,text= "Notepad",borderwidth=3, relief="groove")
        self.notepad_label.grid (row=0,column=0)

class calender_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("calender Module")
        self.geometry ("1100x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.calender_label = tk.Label(self,text="Calender",borderwidth=3, relief="groove")
        self.calender_label.grid(row=0,column=0)

class to_do_list_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title("To do list Module")
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="To do list",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)