import tkinter as tk
#import functions as func
import modules as mods 

flashcard_open = False
notepad_open = False
calender_open = False
to_do_list_open = False

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

        self.flashcard_button= tk.Button(self,text= "open flashcard", command= lambda: flashcard_mode(self))
        self.flashcard_button.grid (row=1,column=0)
        self.notepad_button= tk.Button(self,text= "open notepad", command= lambda: notepad_mode(self))
        self.notepad_button.grid (row=1,column=1)
        self.calender_button= tk.Button(self,text= "open calender", command= lambda: calender_mode(self))
        self.calender_button.grid (row=1,column=2)
        self.to_do_list_button= tk.Button(self,text= "open to-do list", command= lambda: to_do_list_mode(self))
        self.to_do_list_button.grid (row=1,column=3)


#possible modulisation of the seperate frames
class Module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)

class flashcard_module(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.title = ("Flashcard Module")
        self.geometry ("1000x700")

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0, weight=1)

        self.flashcard_label = tk.Label(self,text="Flashcard ahh frame",borderwidth=3, relief="groove")
        self.flashcard_label.grid(row=0,column=0)


#button functions to open the different modules
def flashcard_mode(self):
    global flashcard_open
    print(flashcard_open)
    if flashcard_open == False:
        flashcard_open = True
        mods.flashcard_module(self)
    else:
        print("Flashcard is already open")

def notepad_mode(self):
    global notepad_open
    print(notepad_open)
    if notepad_open == False:
        notepad_open   = True
        mods.notepad_module(self)
    else:
        print("Notepad is already open")

def calender_mode(self):
    global calender_open
    print(calender_open)
    if calender_open == False:
        calender_open = True
        mods.calender_module(self)
    else:
        print("calender mode is already open")

def to_do_list_mode(self):
    global to_do_list_open
    print(to_do_list_open)
    if to_do_list_open == False:
        to_do_list_open = True
        mods.to_do_list_module(self)
    else:
        print("To-do list is already open")