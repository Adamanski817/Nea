import tkinter as tk
import functions as func

class central(tk.Frame):
    def __init__(self,parent): #parent frame ie where the frame will be places ):
        super().__init__(parent)
        self.parent= parent
    

        for i in range (0,3):
            self.columnconfigure(i,weight=1)

        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard core",borderwidth=3,relief="groove")
        self.flashcard_label.grid(row=0,column = 0)
        self.notepad_label = tk.Label(self,text="notepad core",borderwidth=3,relief="groove")
        self.notepad_label.grid(row=0,column = 1)
        self.calender_label = tk.Label(self,text="calender core",borderwidth=3,relief="groove")
        self.calender_label.grid(row=0,column = 2)
        self.to_do_list_label = tk.Label(self,text="to do core",borderwidth=3,relief="groove")
        self.to_do_list_label.grid(row=0,column = 3)

        self.flashcard_button= tk.Button(self,text= "open flashcard", command= lambda: flashcard_module(self))
        self.flashcard_button.grid (row=1,column=0)
        self.notepad_button= tk.Button(self,text= "open notepad", command= lambda: flashcard_module(self))
        self.notepad_button.grid (row=1,column=1)
        self.calender_button= tk.Button(self,text= "open calender", command= lambda: flashcard_module(self))
        self.calender_button.grid (row=1,column=2)
        self.to_do_list_button= tk.Button(self,text= "open to-do list", command= lambda: flashcard_module(self))
        self.to_do_list_button.grid (row=1,column=3)


class flashcard_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title = ("Flashcard Module")
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)

